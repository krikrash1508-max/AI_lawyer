// Klauzula AI v0.2 — front end (no framework). Follows the TO-BE process:
// upload → masked check against playbook + Polish law → report → lawyer decides → new version = next round.
const $ = (s, el = document) => el.querySelector(s);
const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const LEVEL = { risk: "Red flag", review: "Review", ok: "OK" };

let current = null;      // review of the current round
let decisions = {};      // rule_id -> {decision, edit}
let verdict = "";        // "sign" | "edits" — the lawyer's decision for this round
let samples = null;

async function api(path, body) {
  const res = await fetch(path, body ? { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) } : {});
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(data.error || "Server error " + res.status);
  return data;
}
async function getSamples() { return samples || (samples = await api("/api/samples")); }

// ---------- tabs ----------
document.querySelectorAll(".tabs button").forEach((b) => b.addEventListener("click", () => show(b.dataset.view)));
function show(view) {
  document.querySelectorAll(".tabs button").forEach((b) => b.setAttribute("aria-selected", b.dataset.view === view));
  document.querySelectorAll(".view").forEach((v) => (v.hidden = v.id !== "view-" + view));
  if (view === "playbook") loadPlaybook();
}

// ---------- review: a round ----------
async function runReview(payload, nextRound = false) {
  $("#review-error").hidden = true;
  if (nextRound && current) payload.previous = { round: current.round, clauses: current.clauses, findings: current.findings };
  try {
    current = await api("/api/review", payload);
    decisions = {};
    verdict = "";
    renderReview();
    window.scrollTo({ top: 0, behavior: "smooth" });
  } catch (e) {
    if (nextRound) { alert(e.message); return; }
    $("#review-error").textContent = e.message;
    $("#review-error").hidden = false;
  }
}

function readFile(file, nextRound = false) {
  if (file.size > 5 * 1024 * 1024) { alert("The file is larger than 5 MB."); return; }
  const reader = new FileReader();
  reader.onload = () => runReview({ file_b64: reader.result.split(",")[1], filename: file.name }, nextRound);
  reader.readAsDataURL(file);
}

$("#sample-run").addEventListener("click", async () => {
  const s = await getSamples();
  runReview({ text: s.nda_counterparty_v1, filename: "nda_counterparty_v1.txt (sample)" });
});
$("#paste-run").addEventListener("click", () => {
  const text = $("#paste").value.trim();
  if (text) runReview({ text, filename: "pasted text" });
});
$("#file-input").addEventListener("change", (e) => e.target.files[0] && readFile(e.target.files[0]));
const drop = $("#drop");
drop.addEventListener("dragover", (e) => { e.preventDefault(); drop.classList.add("over"); });
drop.addEventListener("dragleave", () => drop.classList.remove("over"));
drop.addEventListener("drop", (e) => { e.preventDefault(); drop.classList.remove("over"); e.dataTransfer.files[0] && readFile(e.dataTransfer.files[0]); });

$("#next-file").addEventListener("change", (e) => { if (e.target.files[0]) readFile(e.target.files[0], true); e.target.value = ""; });
$("#next-sample").addEventListener("click", async () => {
  const s = await getSamples();
  runReview({ text: s.nda_counterparty_v2, filename: "nda_counterparty_v2.txt (sample)" }, true);
});

$("#new-review").addEventListener("click", () => {
  current = null;
  $("#workspace").hidden = true; $("#intake").hidden = false; $("#file-input").value = "";
});

function highlightPII(text) {
  return esc(text).replace(/\[(EMAIL|PHONE|KRS|NIP|PESEL|IBAN|NAME)_\d+\]/g, (m) => `<mark class="pii" title="Masked before analysis">${m}</mark>`);
}
const refLabel = (ref) => (ref === "preamble" ? "" : `<span class="ref">§ ${esc(ref)}</span>`);

function renderReview() {
  const r = current;
  $("#intake").hidden = true;
  $("#workspace").hidden = false;
  $("#sum-file").textContent = `Round ${r.round} · ${r.filename || "contract"}`;
  $("#sum-chips").innerHTML = ["risk", "review", "ok"].map((l) => `<span class="chip ${l}">${r.counts[l]} ${LEVEL[l]}</span>`).join("");
  const masked = Object.entries(r.masked).map(([k, v]) => `${v} ${k}`).join(", ");
  $("#sum-meta").innerHTML = `Playbook: ${esc(r.playbook.title)} v${esc(r.playbook.version)} · ${r.mode === "claude" ? "Claude" : "rule-based check"} · ${r.seconds}s` +
    (masked ? `<br>Masked before analysis: ${esc(masked)}` : "") + (r.note ? `<br>${esc(r.note)}` : "");

  renderSince(r);
  renderDoc(r);

  const open = r.findings.filter((f) => f.level !== "ok");
  const ok = r.findings.filter((f) => f.level === "ok");
  $("#findings").innerHTML = open.map(findingCard).join("") +
    (ok.length ? `<details class="ok-group"><summary>${ok.length} rules met the playbook</summary>${ok.map(findingCard).join("")}</details>` : "");
  bindFindings();
  renderDecision();
}

// What changed since the previous round (the counterparty's new version)
function renderSince(r) {
  const box = $("#since");
  if (!r.risk_changes) { box.hidden = true; return; }
  const changed = r.changes.filter((c) => c.status !== "unchanged").length;
  const rc = r.risk_changes.map((x) => `
    <div class="rc ${x.direction}"><strong>${x.direction === "new_risk" ? "New risk" : "Improved"}</strong>
      <span>${esc(x.topic)}${x.clause_ref ? ` (§ ${esc(x.clause_ref)})` : ""}: ${LEVEL[x.before]} → ${LEVEL[x.after]}. ${esc(x.explanation)}</span></div>`).join("");
  box.innerHTML = `<div class="eyebrow">Since round ${r.round - 1} · ${changed} of ${r.changes.length} clauses changed</div>` +
    (rc || '<p class="hint">No change in risk levels.</p>') +
    `<p class="hint">Tracked changes in a .docx are read as if accepted; changed clauses are marked in the text below.</p>`;
  box.hidden = false;
}

function renderDoc(r) {
  const worst = {};
  r.findings.forEach((f) => {
    if (!f.clause_ref || f.level === "ok") return;
    if (worst[f.clause_ref] !== "risk") worst[f.clause_ref] = f.level;
  });
  const diffHtml = (d) => d.map(([op, t]) => op === "+" ? `<ins>${highlightPII(t)}</ins>` : op === "-" ? `<del>${highlightPII(t)}</del>` : highlightPII(t)).join("");
  const items = r.changes || r.clauses.map((c) => ({ ref: c.ref, heading: c.heading, status: "unchanged", diff: [["=", c.text]] }));
  $("#doc").innerHTML = items.map((c) => `
    <section class="clause ${c.status === "removed" ? "removed" : worst[c.ref] || ""}" ${c.status === "removed" ? "" : `id="clause-${esc(c.ref)}"`}>
      <h3>${refLabel(c.ref)}${esc(c.heading)}${c.status !== "unchanged" ? `<span class="tag">${c.status}</span>` : ""}</h3>
      <p>${diffHtml(c.diff)}</p>
    </section>`).join("");
}

function findingCard(f) {
  const where = f.clause_ref ? `§ ${esc(f.clause_ref)}` : "missing";
  return `
  <div class="finding ${f.level}" data-rule="${esc(f.rule_id)}" data-ref="${esc(f.clause_ref || "")}">
    <header><h4>${esc(f.topic)}</h4><span class="meta">${esc(f.rule_id)} · ${where} · ${LEVEL[f.level]}</span></header>
    ${f.quote ? `<blockquote>${highlightPII(f.quote)}</blockquote>` : ""}
    <p class="why">${esc(f.explanation)}</p>
    <p class="std">Playbook: ${esc(f.standard)}</p>
    ${f.legal_basis ? `<p class="law"><span class="eyebrow">Polish law · to verify</span> ${esc(f.legal_basis)}</p>` : ""}
    ${f.suggested_edit ? `
      <label class="std" for="edit-${esc(f.rule_id)}">Suggested wording (editable)</label>
      <textarea id="edit-${esc(f.rule_id)}" rows="3">${esc(f.suggested_edit)}</textarea>
      <div class="decide">
        <button class="btn" data-act="accepted">Accept edit</button>
        <button class="btn" data-act="rejected">Reject</button>
        <button class="btn" data-act="copy">Copy</button>
        <span class="decision"></span>
      </div>` : ""}
  </div>`;
}

function bindFindings() {
  document.querySelectorAll(".finding").forEach((card) => {
    const rule = card.dataset.rule;
    card.querySelector("header").addEventListener("click", () => {
      document.querySelectorAll(".clause.active").forEach((c) => c.classList.remove("active"));
      const target = card.dataset.ref && document.getElementById("clause-" + card.dataset.ref);
      if (target) { target.classList.add("active"); target.scrollIntoView({ behavior: "smooth", block: "center" }); }
    });
    card.querySelectorAll("[data-act]").forEach((btn) => btn.addEventListener("click", async () => {
      const ta = card.querySelector("textarea");
      if (btn.dataset.act === "copy") {
        try { await navigator.clipboard.writeText(ta.value); btn.textContent = "Copied"; } catch { ta.select(); }
        return;
      }
      decisions[rule] = { decision: btn.dataset.act, edit: ta.value };
      card.classList.remove("accepted", "rejected");
      card.classList.add(btn.dataset.act);
      card.querySelector(".decision").textContent = btn.dataset.act === "accepted" ? "Edit accepted" : "Rejected";
      renderDecision();
    }));
  });
}

// ---------- the lawyer's decision: any red flags? ----------
function renderDecision() {
  const r = current;
  const accepted = Object.values(decisions).filter((d) => d.decision === "accepted").length;
  const openRisk = r.findings.filter((f) => f.level === "risk" && decisions[f.rule_id]?.decision !== "accepted").length;
  $("#dp-question").textContent = r.red_flags ? `Any red flags? Klauzula AI found ${r.red_flags}.` : "Any red flags? Klauzula AI found none.";
  $("#dp-hint").textContent = `${accepted} edit${accepted === 1 ? "" : "s"} accepted` + (openRisk ? ` · ${openRisk} red flag${openRisk === 1 ? "" : "s"} without an accepted edit` : "") + ". You decide.";
  document.querySelectorAll(".verdict").forEach((b) => b.classList.toggle("primary", b.dataset.verdict === verdict));
  $("#dp-out").hidden = !verdict;
  $("#next-round").hidden = verdict !== "edits";
  if (verdict === "sign") {
    $("#dp-result").innerHTML = "<strong>Ready for signing.</strong> " +
      (openRisk ? `Note: ${openRisk} red flag${openRisk === 1 ? " stays" : "s stay"} in the text — the report records that you accepted the risk.` : "The report records your decision for sales.");
  } else if (verdict === "edits") {
    $("#dp-result").innerHTML = accepted
      ? `<strong>${accepted} edit${accepted === 1 ? "" : "s"} for the counterparty.</strong> Export the report; sales / purchasing sends the edits.`
      : "<strong>No edits accepted yet.</strong> Accept the edits you want to send in the cards below, then export.";
  }
}
document.querySelectorAll(".verdict").forEach((b) => b.addEventListener("click", () => { verdict = b.dataset.verdict; renderDecision(); }));

document.querySelectorAll("[data-export]").forEach((b) => b.addEventListener("click", async () => {
  const fmt = b.dataset.export;
  const res = await fetch("/api/export", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ review: current, decisions, verdict, format: fmt }) });
  const blob = await res.blob();
  const name = `klauzula-report-round${current.round}.${fmt === "md" ? "md" : "doc"}`;
  const a = Object.assign(document.createElement("a"), { href: URL.createObjectURL(blob), download: name });
  a.click();
  URL.revokeObjectURL(a.href);
}));

// ---------- playbook ----------
async function loadPlaybook() {
  const pb = await api("/api/playbook");
  $("#pb-title").textContent = `${pb.title} · v${pb.version}`;
  $("#pb-status").textContent = `Status: ${pb.status}. ${pb.legal_basis_status || ""}`;
  $("#pb-table").innerHTML = "<tr><th>Rule</th><th>Topic</th><th>Standard position</th><th>Red flag</th><th>Polish law</th><th>Fallback wording</th></tr>" +
    pb.rules.map((r) => `<tr><td>${esc(r.id)}</td><td>${esc(r.topic)}</td><td>${esc(r.standard)}</td><td>${esc(r.red_flag)}</td><td class="law">${esc(r.legal_basis)}</td><td class="edit">${esc(r.suggested_edit)}</td></tr>`).join("");
}

api("/api/status").then((s) => {
  $("#mode-badge").textContent = s.claude_available ? `Claude mode · ${s.model}` : "Demo mode · rule-based";
}).catch(() => ($("#mode-badge").textContent = "Server offline"));
