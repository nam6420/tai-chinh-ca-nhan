from __future__ import annotations

import io
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "learning" / "practice" / "models"))

import capital_return as cr  # noqa: E402
import data_pull as dp  # noqa: E402


class FakeResp(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


class BaiQ4(unittest.TestCase):
    def setUp(self):
        self.facts = dp.load_facts()

    def test_khop_voi_bang_q2(self):
        a = cr.load_apple()
        pairs = [("NetIncomeLoss", "net_income"), ("ShareBasedCompensation", "sbc"),
                 ("NetCashProvidedByUsedInOperatingActivities", "cfo"),
                 ("PaymentsToAcquirePropertyPlantAndEquipment", "capex"),
                 ("PaymentsForRepurchaseOfCommonStock", "repurchases_cash"),
                 ("PaymentsOfDividends", "dividends_paid"),
                 ("PaymentsRelatedToTaxWithholdingForShareBasedCompensation", "tax_net_share_settlement")]
        ends = {"FY2025": "2025-09-27", "FY2024": "2024-09-28", "FY2023": "2023-09-30"}
        for tag, key in pairs:
            s = dp.annual_series(self.facts, tag)
            for fy, end in ends.items():
                self.assertEqual(dp.to_millions(s[end]), a[key][fy], (tag, fy))
        basic = dp.annual_series(self.facts, "WeightedAverageNumberOfSharesOutstandingBasic", "shares")
        self.assertEqual(basic["2025-09-27"] / 1000, a["basic_shares_wtd"]["FY2025"])

    def test_fy_la_nam_cua_ho_so_khong_phai_cua_ky(self):
        hs = [r for r in dp.rows(self.facts, "NetIncomeLoss") if r["fy"] == 2025 and dp.duration_days(r) and dp.duration_days(r) > 350]
        self.assertEqual(sorted({r["end"] for r in hs}), ["2023-09-30", "2024-09-28", "2025-09-27"])

    def test_chon_tag_doanh_thu(self):
        self.assertEqual(dp.pick_tag(self.facts, ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax"]),
                         "RevenueFromContractWithCustomerExcludingAssessedTax")
        self.assertEqual(list(dp.annual_series(self.facts, "Revenues")), ["2018-09-29"])
        s = dp.annual_series(self.facts, "RevenueFromContractWithCustomerExcludingAssessedTax")
        self.assertEqual(dp.to_millions(s["2025-09-27"]), 416161)

    def test_hai_khai_niem_mua_lai(self):
        cash = dp.annual_series(self.facts, "PaymentsForRepurchaseOfCommonStock")["2025-09-27"]
        bang_von = dp.annual_series(self.facts, "StockRepurchasedAndRetiredDuringPeriodValue")["2025-09-27"]
        self.assertEqual((cash, bang_von), (90711e6, 89300e6))
        self.assertAlmostEqual(dp.to_millions(cash - bang_von), 1411.0)

    def test_quy_4_suy_ra(self):
        fy = dp.annual_series(self.facts, "NetIncomeLoss")["2025-09-27"]
        nine = dp.ytd_value(self.facts, "NetIncomeLoss", "2025-06-28", (265, 280))
        self.assertEqual(dp.to_millions(nine), 84544)
        self.assertEqual(dp.to_millions(dp.derive_q4(fy, nine)), 27466)

    def test_hoi_to_chia_tach(self):
        cf = dict(dp.conflicting_values(self.facts, "CommonStockDividendsPerShareDeclared", "USD/shares"))
        self.assertEqual(cf[("2018-09-30", "2019-09-28")], [0.75, 3])
        sh = dict(dp.conflicting_values(self.facts, "CommonStockSharesOutstanding", "shares"))
        gia = sh[(None, "2019-09-28")]
        self.assertEqual(gia, [4443236000, 17772945000])
        self.assertAlmostEqual(gia[1] / gia[0], 4.0, places=3)

    def test_fetch_can_user_agent_va_dung_url(self):
        with self.assertRaises(ValueError):
            dp.fetch_companyfacts(320193, "script-khong-co-lien-he")
        seen = {}

        def opener(req, timeout):
            seen["url"] = req.full_url
            seen["ua"] = req.headers["User-agent"]
            return FakeResp(json.dumps({"ok": 1}).encode())

        out = dp.fetch_companyfacts(320193, "Ten Nguoi Hoc ten@vi-du.invalid", opener)
        self.assertEqual(out, {"ok": 1})
        self.assertEqual(seen["url"], "https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json")

    def test_ban_chep_hpg(self):
        cur, prev = dp.load_transcription()
        for f in (cur, prev):
            self.assertTrue(all(c["dat"] for c in dp.statement_checks(f)))
        # lỗi chép: đảo hai chữ số của nợ phải trả
        sai = dict(cur, no_phai_tra=126697.189941)
        kq = dp.statement_checks(sai)
        self.assertFalse(kq[0]["dat"])
        self.assertAlmostEqual(kq[0]["lech"], -18.0, places=3)
        self.assertTrue(all(c["dat"] for c in kq[1:]))
        # lệch đơn vị: một ô tính bằng triệu VND thay vì tỷ VND
        sai2 = dict(cur, von_chu_so_huu=131220010.877)
        self.assertFalse(dp.statement_checks(sai2)[0]["dat"])


if __name__ == "__main__":
    unittest.main()
