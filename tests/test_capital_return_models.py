from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "learning" / "practice" / "models"))

import capital_return as c  # noqa: E402


class BaiQ2(unittest.TestCase):
    def test_mua_lai_hu_cau(self):
        r = c.buyback(100e6, 1000e9, 200e9, 100000)
        self.assertEqual(r["co_phieu_mua"], 2e6)
        self.assertEqual(r["co_phieu_con_lai"], 98e6)
        self.assertAlmostEqual(r["eps_truoc"], 10000.0)
        self.assertAlmostEqual(r["eps_sau"], 10204.08, places=2)
        # giá trị nội tại 150.000: mua lại ở 100.000 làm tăng giá trị mỗi cổ phiếu
        self.assertAlmostEqual(c.value_per_share_after_buyback(15000e9, 100e6, 200e9, 100000), 151020.41, places=2)
        # giá trị nội tại 60.000: mua lại ở 100.000 làm giảm
        self.assertAlmostEqual(c.value_per_share_after_buyback(6000e9, 100e6, 200e9, 100000), 59183.67, places=2)
        self.assertAlmostEqual(c.breakeven_price(15000e9, 100e6), 150000.0)

    def test_sbc_hu_cau(self):
        phat_hanh = c.sbc_dilution_shares(100e9, 100000)
        self.assertEqual(phat_hanh, 1e6)
        self.assertEqual(c.net_buyback_shares(200e9, 100000, phat_hanh), 1e6)
        self.assertEqual(c.net_buyback_shares(100e9, 100000, phat_hanh), 0.0)

    def test_co_phieu_thuong(self):
        self.assertAlmostEqual(c.adjust_for_bonus(1000, 0.2), 833.33, places=2)
        self.assertAlmostEqual(c.bonus_ratio(6396250200, 7675465855), 0.2, places=4)

    def test_apple(self):
        a = c.load_apple()
        y = "FY2025"
        self.assertEqual(c.fcf_after_sbc(a["cfo"][y], a["capex"][y], a["sbc"][y]), 85904)
        self.assertAlmostEqual(c.payout_ratio(a["dividends_paid"][y], a["net_income"][y]), 0.1377, places=4)
        tong = c.total_cash_returned(a["dividends_paid"][y], a["repurchases_cash"][y], a["tax_net_share_settlement"][y])
        self.assertEqual(tong, 112092)
        self.assertEqual(a["cfo"][y] - a["capex"][y], 98767)
        self.assertAlmostEqual(a["sbc"][y] / a["cfo"][y], 0.1154, places=4)
        self.assertAlmostEqual(a["net_income"][y] / (a["diluted_shares_wtd"][y] / 1000), 7.465, places=3)
        self.assertAlmostEqual(c.shrink(a["basic_shares_wtd"]["FY2024"], a["basic_shares_wtd"][y]), -0.0258, places=4)
        self.assertAlmostEqual(c.shrink(a["shares_outstanding_end"]["FY2024"], a["shares_outstanding_end"][y]),
                               -0.0227, places=4)
        self.assertAlmostEqual(c.dilution_pct(a["diluted_shares_wtd"][y], a["basic_shares_wtd"][y]), 0.00376, places=5)
        giam_rong = a["shares_outstanding_end"]["FY2024"] - a["shares_outstanding_end"][y]
        self.assertEqual(giam_rong, 343526)
        # bẫy: giá "ngụ ý" bằng tiền mua lại chia cổ phiếu giảm ròng ~ 264 USD, không phải giá mua thật
        self.assertAlmostEqual(a["repurchases_cash"][y] / (giam_rong / 1000), 264.06, places=2)

    def test_eps_tang_nho_ben_nao(self):
        a = c.load_apple()
        ni = a["net_income"]["FY2025"] / a["net_income"]["FY2024"]
        sh = a["diluted_shares_wtd"]["FY2025"] / a["diluted_shares_wtd"]["FY2024"]
        self.assertAlmostEqual(ni - 1, 0.19495, places=5)
        self.assertAlmostEqual(sh - 1, -0.0262, places=4)
        self.assertAlmostEqual(ni / sh - 1, 0.2271, places=4)
        self.assertAlmostEqual(a["eps_diluted"]["FY2025"] / a["eps_diluted"]["FY2024"] - 1, 0.2270, places=3)

    def test_bai_ban(self):
        a = c.load_apple()
        y = "FY2025"
        sai = a["net_income"][y] / a["diluted_shares_wtd"][y]
        self.assertAlmostEqual(sai, 0.007465, places=6)
        self.assertAlmostEqual(sai * 1000, 7.465, places=3)
        tra_co_dong = c.total_cash_returned(a["dividends_paid"][y], a["repurchases_cash"][y])
        self.assertEqual(tra_co_dong, 106132)
        self.assertEqual(a["cfo"][y] - a["capex"][y] - tra_co_dong, -7365)
        self.assertEqual(c.fcf_after_sbc(a["cfo"][y], a["capex"][y], a["sbc"][y]) - tra_co_dong, -20228)
        # ở giá 200.000 chỉ mua 1 triệu cổ phiếu: EPS chỉ tăng ~1,01%
        r2 = c.buyback(100e6, 1000e9, 200e9, 200000)
        self.assertAlmostEqual(r2["eps_sau"] / r2["eps_truoc"] - 1, 0.0101, places=4)
        r = c.buyback(50e6, 500e9, 100e9, 50000)
        self.assertAlmostEqual(r["eps_sau"], 10416.67, places=2)
        self.assertAlmostEqual(c.adjust_for_bonus(10000, 0.1), 9090.91, places=2)

    def test_tra_co_dong_so_voi_dong_tien_ba_nam(self):
        a = c.load_apple()
        chenh = {}
        for fy in ("FY2025", "FY2024", "FY2023"):
            tra = a["dividends_paid"][fy] + a["repurchases_cash"][fy]
            fcf = a["cfo"][fy] - a["capex"][fy]
            chenh[fy] = tra - fcf
        self.assertEqual(chenh, {"FY2025": 7365, "FY2024": 1376, "FY2023": -7009})

    def test_gia_mua_trung_binh_apple(self):
        # Note 10 của 10-K: mua lại 401.672 nghìn cổ phiếu, phát hành ròng 58.146 nghìn
        self.assertEqual(401672 - 58146, 343526)
        self.assertAlmostEqual(89300 / 401.672, 222.3, places=1)
        self.assertAlmostEqual(90711 / 401.672, 225.8, places=1)

    def test_hpg_loi_nhuan_chua_phan_phoi(self):
        # thuyết minh 26 (trang in 38), tỷ VND
        dau, cuoi = 49599.1, 51037.9
        bien_dong = -12792.2 + 15453.2 - 496.0 - 600.0 + 6.4 - 129.1 - 3.5
        self.assertAlmostEqual(dau + bien_dong, cuoi, delta=0.2)


if __name__ == "__main__":
    unittest.main()
