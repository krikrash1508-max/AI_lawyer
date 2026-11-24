"""Run: python3 -m unittest discover -s app/tests"""
import io
import sys
import unittest
import zipfile
from pathlib import Path

APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))

import engine  # noqa: E402
from engine import masking, parser, report  # noqa: E402

V1 = (APP / "samples" / "nda_counterparty_v1.txt").read_text(encoding="utf-8")
V2 = (APP / "samples" / "nda_counterparty_v2.txt").read_text(encoding="utf-8")
V3 = (APP / "samples" / "nda_counterparty_v3.txt").read_text(encoding="utf-8")


def levels(result):
    return {f["rule_id"]: f["level"] for f in result["findings"]}


class EngineTest(unittest.TestCase):
    def test_masking(self):
        text, counts = masking.mask("Mail a@b.pl, tel. +48 600 100 200, PESEL 90010112345, NIP 000-000-00-00")
        self.assertEqual(counts, {"EMAIL": 1, "PHONE": 1, "NIP": 1, "PESEL": 1})
        self.assertNotIn("a@b.pl", text)

    def test_masking_names(self):
        text, counts = masking.mask("Spółka reprezentowana przez Annę Nowak-Kowalską oraz Pan Łukasz Żak; "
                                    "represented by the Management Board.")
        self.assertEqual(counts, {"NAME": 2})
        self.assertNotIn("Nowak", text)
        self.assertIn("represented by the Management Board", text)  # no capitalised name → unchanged
        self.assertNotIn("Przykładowy", engine.review(V1, use_claude=False)["clauses"][0]["text"])

    def test_masking_signatures_v3(self):
        text, counts = masking.mask(V3)
        for surname in ("Przykładow", "Testowa", "Wymyślony", "Zmyślony", "Fikcyjna"):
            self.assertNotIn(surname, text)
        self.assertEqual(counts["NAME"], 5)  # five people, one label each
        self.assertEqual(text.count("[NAME_1]"), 4)  # Jan Przykładowy: preamble, J. …, Mr …'s, signature
        for kept in ("Alfa Logistics sp. z o.o.", "Beta Software Ltd.", "Prezes Zarządu", "Managing Director",
                     "Authorised Signatory", "Republic of Poland", '("Alfa")'):
            self.assertIn(kept, text)

    def test_masking_signatures_polish(self):
        text, counts = masking.mask(
            "Spółkę reprezentuje Prezes Zarządu Jan Kowalski.\n"
            "§ 1. Zgoda Jana Kowalskiego jest wymagana.\n"
            "Podpisy\n"
            "Za Alfa sp. z o.o.:\n"
            "Jan Kowalski\n"
            "Za Beta S.A.:\n"
            "Katarzyna Nowak, Członek Zarządu\n")
        self.assertNotIn("Kowalsk", text)
        self.assertNotIn("Nowak", text)
        self.assertEqual(counts["NAME"], 2)
        self.assertIn("Za Alfa sp. z o.o.", text)

    def test_masking_keeps_contract_terms(self):
        text = "The Receiving Party shall notify the Disclosing Party.\nSignatures\nReceiving Party\nConfidential Information"
        self.assertEqual(masking.mask(text), (text, {}))

    def test_legal_basis(self):
        f = {x["rule_id"]: x for x in engine.review(V1, use_claude=False)["findings"]}
        self.assertIn("484", f["NDA-06"]["legal_basis"])
        self.assertTrue(all(x["legal_basis"] for x in f.values()))

    def test_clauses(self):
        refs = [c["ref"] for c in parser.split_clauses(V1)]
        self.assertEqual(refs, ["preamble", "1", "2", "3", "4", "5", "6", "7", "8"])

    def test_sample_v1_red_flags(self):
        lv = levels(engine.review(V1, use_claude=False))
        for rid in ("NDA-01", "NDA-02", "NDA-03", "NDA-04", "NDA-06", "NDA-08"):
            self.assertEqual(lv[rid], "risk", rid)
        self.assertEqual(lv["NDA-09"], "ok")

    def test_sample_v2(self):
        lv = levels(engine.review(V2, use_claude=False))
        self.assertEqual(lv["NDA-01"], "ok")
        self.assertEqual(lv["NDA-03"], "ok")
        self.assertEqual(lv["NDA-07"], "risk")  # new indemnity

    def test_next_round_finds_new_risk(self):
        r1 = engine.review(V1, use_claude=False)
        r2 = engine.review(V2, use_claude=False, previous={"round": r1["round"], "clauses": r1["clauses"],
                                                            "findings": r1["findings"]})
        self.assertEqual(r2["round"], 2)
        new = [x["rule_id"] for x in r2["risk_changes"] if x["direction"] == "new_risk"]
        self.assertEqual(new, ["NDA-07"])
        status = {c["ref"]: c["status"] for c in r2["changes"]}
        self.assertEqual(status["6"], "removed")

    def test_report_verdict(self):
        r = engine.review(V1, use_claude=False)
        md = report.to_markdown(r, {"NDA-01": {"decision": "accepted", "edit": "Polish law applies."}}, "edits")
        self.assertIn("Edits to send to the counterparty", md)
        self.assertIn("Polish law applies.", md)
        self.assertIn("Ready for signing", report.to_markdown(r, {}, "sign"))

    def test_docx(self):
        xml = ('<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>'
               "<w:p><w:r><w:t>1. Term</w:t></w:r></w:p><w:p><w:r><w:t>Valid for 3 years.</w:t></w:r></w:p>"
               "</w:body></w:document>")
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w") as zf:
            zf.writestr("word/document.xml", xml)
        self.assertEqual(parser.docx_to_text(buf.getvalue()), "1. Term\nValid for 3 years.")


if __name__ == "__main__":
    unittest.main()
