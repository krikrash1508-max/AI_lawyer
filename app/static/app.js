// Klauzula v0.1 — front end (no framework).
const $ = (s, el = document) => el.querySelector(s);
const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const LEVEL = { risk: "Red flag", review: "Review", ok: "OK" };

let current = null;      // last review result
let decisions = {};      // rule_id -> {decision, edit, comment}
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

// ---------- review ----------
async function runReview(payload) {
  $("#review-error").hidden = true;
  try {
    current = await api("/api/review", payload);
    decisions = {};
    renderReview();
  } catch (e) {
    $("#review-error").textContent = e.message;
    $("#review-error").hidden = false;
  }
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

function readFile(file) {
  if (file.size > 5 * 1024 * 1024) { $("#review-error").textContent = "The file is larger than 5 MB."; $("#review-error").hidden = false; return; }
  const reader = new FileReader();
  reader.onload = () => runReview({ file_b64: reader.result.split(",")[1], filename: file.name });
  reader.readAsDataURL(file);
}

$("#new-review").addEventListener("click", () => {
  $("#workspace").hidden = true; $("#intake").hidden = false; $("#file-input").value = "";
});

function highlightPII(text) {
  return esc(text).replace(/\[(EMAIL|PHONE|KRS|NIP|PESEL|IBAN)_\d+\]/g, (m) => `<mark class="pii" title="Masked before analysis">${m}</mark>`);
}

function renderReview() {
  const r = current;
  $("#intake").hidden = true;
  $("#workspace").hidden = false;
  $("#sum-file").textContent = r.filename || "contract";
  $("#sum-chips").innerHTML = ["risk", "review", "ok"].map((l) => `<span class="chip ${l}">${r.counts[l]} ${LEVEL[l]}</span>`).join("");
  const masked = Object.entries(r.masked).map(([k, v]) => `${v} ${k}`).join(", ");
  $("#sum-meta").innerHTML = `Playbook: ${esc(r.playbook.title)} v${esc(r.playbook.version)} · ${r.mode === "claude" ? "Claude" : "rule-based check"} · ${r.seconds}s` +
    (masked ? `<br>Masked before analysis: ${esc(masked)}` : "") + (r.note ? `<br>${esc(r.note)}` : "");

  // contract text: color each clause by its worst finding
  const worst = {};
  r.findings.forEach((f) => {
    if (!f.clause_ref || f.level === "ok") return;
    if (worst[f.clause_ref] !== "risk") worst[f.clause_ref] = f.level;
  });
  $("#doc").innerHTML = r.clauses.map((c) => `
    <section class="clause ${worst[c.ref] || ""}" id="clause-${esc(c.ref)}">
      <h3>${c.ref === "preamble" ? "" : `<span class="ref">§ ${esc(c.ref)}</span>`}${esc(c.heading)}</h3>
      <p>${highlightPII(c.text)}</p>
    </section>`).join("");

  const open = r.findings.filter((f) => f.level !== "ok");
  const ok = r.findings.filter((f) => f.level === "ok");
  $("#findings").innerHTML = open.map(findingCard).join("") +
    (ok.length ? `<details class="ok-group"><summary>${ok.length} rules met the playbook</summary>${ok.map(findingCard).join("")}</details>` : "");
  bindFindings();
}

function findingCard(f) {
  const where = f.clause_ref ? `§ ${esc(f.clause_ref)}` : "missing";
  return `
  <div class="finding ${f.level}" data-rule="${esc(f.rule_id)}" data-ref="${esc(f.clause_ref || "")}">
    <header><h4>${esc(f.topic)}</h4><span class="meta">${esc(f.rule_id)} · ${where} · ${LEVEL[f.level]}</span></header>
    ${f.quote ? `<blockquote>${highlightPII(f.quote)}</blockquote>` : ""}
    <p class="why">${esc(f.explanation)}</p>
    <p class="std">Playbook: ${esc(f.standard)}</p>
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
    }));
  });
}

document.querySelectorAll("[data-export]").forEach((b) => b.addEventListener("click", async () => {
  const fmt = b.dataset.export;
  const res = await fetch("/api/export", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ review: current, decisions, format: fmt }) });
  const blob = await res.blob();
  const a = Object.assign(document.createElement("a"), { href: URL.createObjectURL(blob), download: fmt === "md" ? "nda-review.md" : "nda-review.doc" });
  a.click();
  URL.revokeObjectURL(a.href);
}));

// ---------- compare ----------
$("#compare-sample").addEventListener("click", async () => {
  const s = await getSamples();
  $("#old-text").value = s.nda_counterparty_v1;
  $("#new-text").value = s.nda_counterparty_v2;
});
$("#compare-run").addEventListener("click", async () => {
  $("#compare-error").hidden = true;
  try {
    const r = await api("/api/compare", { old_text: $("#old-text").value, new_text: $("#new-text").value });
    renderCompare(r);
  } catch (e) { $("#compare-error").textContent = e.message; $("#compare-error").hidden = false; }
});

function renderCompare(r) {
  const rc = r.risk_changes.map((x) => `
    <div class="rc ${x.direction}"><strong>${x.direction === "new_risk" ? "New risk" : "Improved"}</strong>
      <span>${esc(x.topic)}: ${LEVEL[x.before]} → ${LEVEL[x.after]}. ${esc(x.explanation)}</span></div>`).join("");
  const changed = r.changes.filter((c) => c.status !== "unchanged");
  const diff = changed.map((c) => `
    <section class="clause">
      <h3>${c.ref === "preamble" ? "" : `<span class="ref">§ ${esc(c.ref)}</span>`}${esc(c.heading)}<span class="tag">${c.status}</span></h3>
      <p>${c.diff.map(([op, t]) => op === "+" ? `<ins>${highlightPII(t)}</ins>` : op === "-" ? `<del>${highlightPII(t)}</del>` : highlightPII(t)).join("")}</p>
    </section>`).join("");
  $("#compare-result").innerHTML =
    `<div class="risk-changes"><div class="eyebrow">Effect on the playbook</div>${rc || '<p class="hint">No change in risk levels.</p>'}</div>` +
    `<div class="eyebrow">${changed.length} of ${r.changes.length} clauses changed</div><div class="diff">${diff}</div>`;
}

// ---------- playbook ----------
async function loadPlaybook() {
  const pb = await api("/api/playbook");
  $("#pb-title").textContent = `${pb.title} · v${pb.version}`;
  $("#pb-status").textContent = `Status: ${pb.status}`;
  $("#pb-table").innerHTML = "<tr><th>Rule</th><th>Topic</th><th>Standard position</th><th>Red flag</th><th>Fallback wording</th></tr>" +
    pb.rules.map((r) => `<tr><td>${esc(r.id)}</td><td>${esc(r.topic)}</td><td>${esc(r.standard)}</td><td>${esc(r.red_flag)}</td><td class="edit">${esc(r.suggested_edit)}</td></tr>`).join("");
}

api("/api/status").then((s) => {
  $("#mode-badge").textContent = s.claude_available ? `Claude mode · ${s.model}` : "Demo mode · rule-based";
}).catch(() => ($("#mode-badge").textContent = "Server offline"));
