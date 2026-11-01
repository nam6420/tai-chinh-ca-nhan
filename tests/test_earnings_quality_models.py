from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "learning" / "practice" / "models"))

import earnings_quality as q  # noqa: E402

P = dict(doanh_thu=1000, gia_von=700, phai_thu=150, tai_san_ngan_han=500, ppe=400, chung_khoan=0,
         tong_tai_san=1200, khau_hao=40, sga=100, no_ngan_han=300, vay_dai_han=200, lai_rong=80, cfo=90,
         tong_tai_san_dau=1100, loi_nhuan_giu_lai=300, ebit=120, von_chu=700, tong_no=500)
T = dict(doanh_thu=1300, gia_von=960, phai_thu=330, tai_san_ngan_han=700, ppe=410, chung_khoan=0,
         tong_tai_san=1500, khau_hao=38, sga=135, no_ngan_han=450, vay_dai_han=250, lai_rong=150, cfo=20,
         tong_tai_san_dau=1200, loi_nhuan_giu_lai=380, ebit=210, von_chu=800, tong_no=700)


class BaiQ1(unittest.TestCase):
    def test_vi_du_hu_cau_beneish(self):
        b = q.beneish(T, P)
        self.assertAlmostEqual(b["DSRI"], 1.6923, places=4)
        self.assertAlmostEqual(b["GMI"], 1.1471, places=4)
        self.assertAlmostEqual(b["AQI"], 1.04, places=4)
        self.assertAlmostEqual(b["SGI"], 1.3, places=4)
        self.assertAlmostEqual(b["TATA"], 0.0867, places=4)
        self.assertAlmostEqual(b["M"], -1.1138, places=3)
        self.assertGreater(b["M"], q.BENEISH_CUTOFF)

    def test_vi_du_hu_cau_altman_va_piotroski(self):
        z = q.altman_zpp(T)
        self.assertAlmostEqual(z["Z"], 4.06, places=2)
        self.assertEqual(q.altman_zone(z["Z"]), "an toàn")
        f = q.piotroski(T, P)
        self.assertEqual(f["F_SCORE"], 5)
        self.assertEqual(f["F_ACCRUAL"], 0)

    def test_hpg_fy2025(self):
        t, p = q.hpg_inputs()
        b = q.beneish(t, p)
        self.assertAlmostEqual(b["DSRI"], 2.2423, places=4)
        self.assertAlmostEqual(b["GMI"], 0.8489, places=4)
        self.assertAlmostEqual(b["AQI"], 0.0225, places=4)
        self.assertAlmostEqual(b["SGI"], 1.1243, places=4)
        self.assertAlmostEqual(b["DEPI"], 1.5646, places=4)
        self.assertAlmostEqual(b["SGAI"], 0.9323, places=4)
        self.assertAlmostEqual(b["LVGI"], 1.0352, places=4)
        self.assertAlmostEqual(b["TATA"], -0.0072, places=4)
        self.assertAlmostEqual(b["M"], -1.6694, places=3)
        self.assertGreater(b["M"], q.BENEISH_CUTOFF)
        c = q.beneish_contributions(b)
        self.assertAlmostEqual(c["DSRI"], 2.063, places=3)
        # Nếu DSRI = 1 thì M còn -2,81; ngưỡng DSRI để M = -1,78 là 2,12.
        self.assertAlmostEqual(b["M"] - 0.92 * (b["DSRI"] - 1), -2.8123, places=3)
        self.assertAlmostEqual((q.BENEISH_CUTOFF - b["M"]) / 0.92 + b["DSRI"], 2.1221, places=3)

    def test_hpg_altman_piotroski(self):
        t, p = q.hpg_inputs()
        z = q.altman_zpp(t)
        self.assertAlmostEqual(z["X1"], 0.0367, places=4)
        self.assertAlmostEqual(z["X2"], 0.1979, places=4)
        self.assertAlmostEqual(z["X3"], 0.0820, places=4)
        self.assertAlmostEqual(z["X4"], 1.0358, places=4)
        self.assertAlmostEqual(z["Z"], 2.525, places=3)
        self.assertEqual(q.altman_zone(z["Z"]), "xám")
        f = q.piotroski(t, p)
        self.assertEqual(f["F_SCORE"], 7)
        self.assertEqual((f["F_dTURN"], f["F_dLIQUID"]), (0, 0))

    def test_so_goc_hpg(self):
        c, p = q.load_hpg()
        self.assertAlmostEqual(c["phai_thu_khach_hang"] / p["phai_thu_khach_hang"] - 1, 1.5211, places=3)
        self.assertAlmostEqual(c["doanh_thu_thuan"] / p["doanh_thu_thuan"] - 1, 0.1243, places=3)
        ten_khach = [1837.277743, 1641.168856, 679.338510, 592.625072, 617.303505]
        self.assertAlmostEqual(sum(ten_khach), 5367.7137, places=3)
        self.assertAlmostEqual(sum(ten_khach) / c["phai_thu_khach_hang"], 0.4892, places=3)
        dau = [482.424804, 0.0, 0.0, 60.730027, 218.586863]
        self.assertAlmostEqual(sum(dau) / p["phai_thu_khach_hang"], 0.1750, places=3)
        self.assertAlmostEqual(c["tscd_huu_hinh"] / p["tscd_huu_hinh"] - 1, 0.9841, places=3)

    def test_dinh_nghia_phai_thu_doi_co_dsri(self):
        c, p = q.load_hpg()
        dt_c, dt_p = c["doanh_thu_thuan"], p["doanh_thu_thuan"]
        kh = (c["phai_thu_khach_hang"] / dt_c) / (p["phai_thu_khach_hang"] / dt_p)
        tong = (c["phai_thu_ngan_han_tong"] / dt_c) / (p["phai_thu_ngan_han_tong"] / dt_p)
        lech = (c["phai_thu_ngan_han_tong"] / dt_c) / (p["phai_thu_khach_hang"] / dt_p)
        self.assertAlmostEqual(kh, 2.2423, places=4)
        self.assertAlmostEqual(tong, 1.7494, places=4)
        self.assertAlmostEqual(lech, 3.0742, places=4)
        t, pp = q.hpg_inputs()
        m = q.beneish(t, pp)["M"]
        self.assertAlmostEqual(m - 0.92 * (kh - tong), -2.1229, places=3)
        self.assertLess(m - 0.92 * (kh - tong), q.BENEISH_CUTOFF)


if __name__ == "__main__":
    unittest.main()
