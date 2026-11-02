from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "learning" / "practice" / "models"))

import earnings_quality as q  # noqa: E402

P = dict(doanh_thu=1000, gia_von=700, phai_thu=150, tai_san_ngan_han=500, ppe=400, chung_khoan=0,
         tong_tai_san=1200, khau_hao=40, sga=100, no_ngan_han=300, vay_dai_han=200, vay_dai_han_den_han=0, lai_rong=80, cfo=90,
         tong_tai_san_dau=1100, loi_nhuan_giu_lai=300, ebit=120, von_chu=700, tong_no=500)
T = dict(doanh_thu=1300, gia_von=960, phai_thu=330, tai_san_ngan_han=700, ppe=410, chung_khoan=0,
         tong_tai_san=1500, khau_hao=38, sga=135, no_ngan_han=450, vay_dai_han=250, vay_dai_han_den_han=0, lai_rong=150, cfo=20,
         tong_tai_san_dau=1200, loi_nhuan_giu_lai=380, ebit=210, von_chu=800, tong_no=700,
         phat_hanh_co_phieu=False)


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
        self.assertAlmostEqual(b["AQI"], 0.2568, places=4)
        self.assertAlmostEqual(b["SGI"], 1.1243, places=4)
        self.assertAlmostEqual(b["DEPI"], 1.5646, places=4)
        self.assertAlmostEqual(b["SGAI"], 0.9323, places=4)
        self.assertAlmostEqual(b["LVGI"], 1.0352, places=4)
        self.assertAlmostEqual(b["TATA"], -0.0072, places=4)
        self.assertAlmostEqual(b["M"], -1.5748, places=3)
        self.assertGreater(b["M"], q.BENEISH_CUTOFF)
        c = q.beneish_contributions(b)
        self.assertAlmostEqual(c["DSRI"], 2.063, places=3)
        self.assertAlmostEqual(c["AQI"], 0.104, places=3)
        # Nếu DSRI = 1 thì M còn -2,72; ngưỡng DSRI để M = -1,78 là 2,02.
        self.assertAlmostEqual(b["M"] - 0.92 * (b["DSRI"] - 1), -2.7177, places=3)
        self.assertAlmostEqual((q.BENEISH_CUTOFF - b["M"]) / 0.92 + b["DSRI"], 2.0192, places=3)

    def test_mat_cau_dung_trung_ma_120(self):
        c, _ = q.load_hpg()
        # mã 100 đã gồm 110+120+130+140+150 (sai số làm tròn của bản chép dưới 0,01 tỷ)
        tong = 8300.890304 + c["dau_tu_tai_chinh_ngan_han"] + c["phai_thu_ngan_han_tong"] + 52828.227344 + 8003.549232
        self.assertAlmostEqual(tong, c["tai_san_ngan_han"], delta=0.01)

    def test_ba_cach_anh_xa_aqi(self):
        kq = {}
        for v in "ABC":
            t, p = q.hpg_inputs(v)
            b = q.beneish(t, p)
            kq[v] = (round(b["AQI"], 4), round(b["DEPI"], 4), round(b["M"], 4))
        self.assertEqual(kq["A"], (0.2568, 1.5646, -1.5748))
        self.assertEqual(kq["B"], (0.2295, 1.5646, -1.5858))
        self.assertEqual(kq["C"], (1.0029, 0.9059, -1.3491))
        # phần tài sản ngoài TSNH và TSCĐ hữu hình: 8,07% (2025) và 31,44% (2024)
        c, p = q.load_hpg()
        khac = lambda f: 1 - (f["tai_san_ngan_han"] + f["tscd_huu_hinh"]) / f["tong_tai_san"]
        self.assertAlmostEqual(khac(c), 0.0807, places=4)
        self.assertAlmostEqual(khac(p), 0.3144, places=4)

    def test_hpg_altman_piotroski(self):
        t, p = q.hpg_inputs()
        z = q.altman_zpp(t)
        self.assertAlmostEqual(z["X1"], 0.0367, places=4)
        self.assertAlmostEqual(z["X2"], 0.1979, places=4)
        self.assertAlmostEqual(z["X3"], 0.0820, places=4)
        self.assertAlmostEqual(z["X4"], 1.0358, places=4)
        self.assertAlmostEqual(z["Z"], 2.525, places=3)
        self.assertEqual(q.altman_zone(z["Z"]), "xám")
        self.assertAlmostEqual(q.altman_zpp_em(t), 5.775, places=3)
        f = q.piotroski(t, p)
        # LEVER theo Piotroski gồm nợ dài hạn đến hạn: (27.479,2 + 8.826,2)/241.194,5 = 15,05% so với
        # (27.080,4 + 3.298,8)/206.136,4 = 14,74%: đòn bẩy tăng, tín hiệu trượt
        self.assertEqual(f["F_dLEVER"], 0)
        self.assertEqual(f["F_SCORE"], 6)
        self.assertEqual((f["F_dTURN"], f["F_dLIQUID"]), (0, 0))
        # cổ tức bằng cổ phiếu tính là phát hành thì EQ_OFFER = 0 và F = 5
        t2, p2 = q.hpg_inputs("A", equity_issued=True)
        self.assertEqual(q.piotroski(t2, p2)["F_SCORE"], 5)
        # định nghĩa hẹp (chỉ mã 338) lệch khỏi bài gốc và cho 7/6
        self.assertEqual(q.piotroski(t, p, lever_def="hep")["F_SCORE"], 7)
        self.assertEqual(q.piotroski(t2, p2, lever_def="hep")["F_SCORE"], 6)
        # độ nhạy của Z'': loại thu nhập tài chính hạ Z'', cộng lại cổ tức bằng cổ phiếu nâng Z'' qua 2,6
        t3 = dict(t, ebit=t["ebit"] - 2081.8)
        self.assertAlmostEqual(q.altman_zpp(t3)["Z"], 2.471, places=3)
        t4 = dict(t, loi_nhuan_giu_lai=t["loi_nhuan_giu_lai"] + 12792.2)
        self.assertAlmostEqual(q.altman_zpp(t4)["X2"], 0.2475, places=4)
        self.assertAlmostEqual(q.altman_zpp(t4)["Z"], 2.687, places=3)
        # Z' (Altman 2000, có X5 = doanh thu/tài sản) cho HPG ≈ 1,49, vùng xám 1,23–2,90
        x5 = t["doanh_thu"] / t["tong_tai_san"]
        zp = 0.717 * z["X1"] + 0.847 * z["X2"] + 3.107 * z["X3"] + 0.420 * z["X4"] + 0.998 * x5
        self.assertAlmostEqual(x5, 0.605, places=3)
        self.assertAlmostEqual(zp, 1.488, places=3)
        # không có dữ liệu phát hành thì không được mặc định "đạt"
        thieu = {k: v for k, v in t.items() if k != "phat_hanh_co_phieu"}
        with self.assertRaises(KeyError):
            q.piotroski(thieu, p)

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
        self.assertAlmostEqual(m - 0.92 * (kh - tong), -2.0282, places=3)
        self.assertLess(m - 0.92 * (kh - tong), q.BENEISH_CUTOFF)
        self.assertGreater(m - 0.92 * (kh - tong), -2.22)  # trên ngưỡng −2,22 nếu có nguồn dùng ngưỡng đó


if __name__ == "__main__":
    unittest.main()
