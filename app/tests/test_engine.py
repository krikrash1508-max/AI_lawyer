"""Run: python3 -m unittest discover -s app/tests"""
import io
import sys
import unittest
import zipfile
from pathlib import Path

APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))

import engine  # noqa: E402
from engine import compare, masking, parser  # noqa: E402

V1 = (APP / "samples" / "nda_counterparty_v1.txt").read_text(encoding="utf-8")
V2 = (APP / "samples" / "nda_counterparty_v2.txt").read_text(encoding="utf-8")


def levels(result):
    return {f["rule_id"]: f["level"] for f in result["findings"]}


class EngineTest(unittest.TestCase):
    def test_masking(self):
        text, counts = masking.mask("Mail a@b.pl, tel. +48 600 100 200, PESEL 90010112345, NIP 000-000-00-00")
        self.assertEqual(counts, {"EMAIL": 1, "PHONE": 1, "NIP": 1, "PESEL": 1})
        self.assertNotIn("a@b.pl", text)

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

    def test_compare_finds_new_risk(self):
        pb = engine.load_playbook()
        r = compare.compare(parser.split_clauses(V1), parser.split_clauses(V2), pb)
        new = [x["rule_id"] for x in r["risk_changes"] if x["direction"] == "new_risk"]
        self.assertEqual(new, ["NDA-07"])
        status = {c["ref"]: c["status"] for c in r["changes"]}
        self.assertEqual(status["6"], "removed")

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
