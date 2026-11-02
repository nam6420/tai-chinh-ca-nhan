from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "learning" / "practice" / "models"))

import cyclical as c  # noqa: E402

REV = [60, 70, 80, 100, 120]
MARGIN = [0.18, 0.06, 0.05, 0.08, 0.10]
PROFIT = [r * m for r, m in zip(REV, MARGIN)]


class BaiQ3(unittest.TestCase):
    def test_vi_du_hu_cau(self):
        self.assertEqual([round(p, 1) for p in PROFIT], [10.8, 4.2, 4.0, 8.0, 12.0])
        self.assertAlmostEqual(c.avg_dollar(PROFIT), 7.8, places=6)
        self.assertAlmostEqual(c.avg_margin_norm(120, MARGIN), 11.28, places=6)
        self.assertAlmostEqual(c.avg_margin_norm(120, c.trimmed(MARGIN)), 8.7, places=6)
        self.assertAlmostEqual(c.median_margin_norm(120, MARGIN), 9.6, places=6)
        self.assertAlmostEqual(c.cycle_gap(12.0, 9.6), 0.25, places=6)
        self.assertAlmostEqual(c.discount_back(9.6, 0.10, 2), 7.9339, places=4)
        self.assertAlmostEqual(c.pe(12000, 1200), 10.0, places=6)
        self.assertAlmostEqual(c.pe(12000, 960), 12.5, places=6)

    def test_du_lieu_hpg(self):
        rows = c.load_hpg()
        self.assertEqual([r["nam"] for r in rows], ["FY2021", "FY2022", "FY2023", "FY2024", "FY2025"])
        m = c.margins(rows, "lnst_cong_ty_me")
        self.assertEqual([round(x * 100, 2) for x in m], [23.03, 6.0, 5.75, 8.66, 9.9])
        gm = c.margins(rows, "loi_nhuan_gop")
        self.assertEqual([round(x * 100, 1) for x in gm], [27.5, 11.9, 10.9, 13.3, 15.7])
        pat = [r["lnst_cong_ty_me"] for r in rows]
        rev = [r["doanh_thu_thuan"] for r in rows]
        now = rows[-1]
        self.assertAlmostEqual(c.avg_dollar(pat), 15454.3, places=1)
        self.assertAlmostEqual(c.avg_dollar(c.trimmed(pat)), 10698.4, places=1)
        self.assertAlmostEqual(c.avg_margin_norm(now["doanh_thu_thuan"], m), 16653.2, delta=0.1)
        self.assertAlmostEqual(c.weighted_margin_norm(now["doanh_thu_thuan"], pat, rev), 17110.8, delta=0.1)
        self.assertAlmostEqual(c.median_margin_norm(now["doanh_thu_thuan"], m), 13515.8, delta=0.1)
        self.assertAlmostEqual(c.avg_margin_norm(now["doanh_thu_thuan"], c.trimmed(m)), 11826.4, delta=0.1)
        self.assertAlmostEqual(c.avg_margin_norm(now["doanh_thu_thuan"], c.trimmed(m, 1, 1)), 12778.4, delta=0.1)
        self.assertAlmostEqual(c.avg_dollar(c.trimmed(pat, 1, 1)), 11986.2, delta=0.1)
        roe = [r["lnst_cong_ty_me"] / r["von_chu_cuoi_nam"] for r in rows]
        self.assertEqual([round(x * 100, 2) for x in roe], [37.98, 8.83, 6.65, 10.49, 11.78])
        self.assertAlmostEqual(c.roe_norm(now["von_chu_cuoi_nam"], roe), 19870.6, delta=0.1)

    def test_quy_mo_va_chi_phi_cung(self):
        rows = c.load_hpg()
        self.assertAlmostEqual(rows[-1]["von_chu_cuoi_nam"] / rows[0]["von_chu_cuoi_nam"] - 1, 0.4455, places=3)
        self.assertAlmostEqual(rows[-1]["doanh_thu_thuan"] / rows[0]["doanh_thu_thuan"] - 1, 0.0430, places=3)
        sga = [r["chi_phi_ban_hang"] + r["chi_phi_quan_ly"] for r in rows]
        self.assertAlmostEqual(sga[1], 3685.0, places=1)
        self.assertAlmostEqual(sga[2], 3268.0, places=1)
        self.assertAlmostEqual(rows[2]["doanh_thu_thuan"] / rows[1]["doanh_thu_thuan"] - 1, -0.1588, places=3)
        self.assertAlmostEqual(sga[2] / sga[1] - 1, -0.1131, places=3)

    def test_nhom_thep_va_mau_so_9_thang(self):
        self.assertAlmostEqual(18396 / 165784, 0.1110, places=4)
        self.assertEqual(171539 - 139499, 32040)
        self.assertEqual(32040 - 30775, 1265)
        self.assertAlmostEqual(23746 / (139499 + 30775), 0.1395, places=4)
        self.assertAlmostEqual(30775 / (139499 + 30775), 0.1807, places=4)
        # Thép Xanh: bỏ cả đỉnh và đáy cho biên 8% và 9,6
        m = [0.18, 0.06, 0.05, 0.08, 0.10]
        self.assertAlmostEqual(c.avg_margin_norm(120, c.trimmed(m, 1, 1)), 9.6, places=6)

    def test_chin_thang_2026(self):
        n = c.NINE_M_2026
        self.assertAlmostEqual(n["lnst_chung"] / n["doanh_thu"], 0.1384, places=4)
        self.assertAlmostEqual(n["loi_nhuan_gop"] / n["doanh_thu"], 0.1794, places=4)
        self.assertAlmostEqual(n["von_chu"] / c.load_hpg()[-1]["von_chu_cuoi_nam"] - 1, 0.1399, places=3)
        m = c.margins(c.load_hpg(), "lnst_cong_ty_me")
        tb_bo_dinh = sum(c.trimmed(m)) / 4
        self.assertAlmostEqual(tb_bo_dinh, 0.07577, places=4)
        self.assertAlmostEqual(n["lnst_chung"] / n["doanh_thu"] / tb_bo_dinh, 1.827, places=2)

    def test_bien_2017_2019_theo_bao_cao_thuong_nien_2019(self):
        # báo cáo thường niên 2019: doanh thu và lợi nhuận sau thuế hợp nhất, tỷ VND
        for dt, ln, bien in ((46855, 8015, 0.17), (56580, 8600, 0.15), (64678, 7578, 0.12)):
            self.assertAlmostEqual(ln / dt, bien, delta=0.005)

    def test_bien_9t_2026_tru_tho_khoan_mot_lan(self):
        # khoản chuyển nhượng dự án Phố Nối khoảng 3,8 nghìn tỷ (thứ cấp, chưa rõ trước/sau thuế)
        self.assertAlmostEqual((23746 - 3800) / 171539, 0.1163, places=4)
        self.assertAlmostEqual(4627 / 1878, 2.46, places=2)
        self.assertAlmostEqual(92174.2 / 131220.0, 0.702, places=3)
        self.assertAlmostEqual(105737 / 149568, 0.707, places=3)

    def test_lai_vay_theo_quy_va_quy_mo(self):
        # bản tổng quan Q3/2026 (trang 5): chi phí lãi vay theo quý, tỷ VND
        q25 = [627, 439, 812, 1237]
        q26 = [1333, 1520, 1774]
        self.assertAlmostEqual(sum(q25), 3114.9, delta=1.0)  # khớp mã 23 của BCTC FY2025
        self.assertEqual(sum(q26), 4627)
        self.assertAlmostEqual(sum(q26) / sum(q25), 1.49, places=2)
        self.assertAlmostEqual(171539 / 111031 - 1, 0.545, places=3)
        self.assertAlmostEqual(18396 / 165784, 0.1110, places=4)
        # lãi vay/doanh thu và nợ/vốn chủ
        self.assertAlmostEqual(sum(q26) / 171539, 0.0270, places=4)
        self.assertAlmostEqual(sum(q25) / 156116.1, 0.0200, places=4)
        self.assertAlmostEqual(sum(q25[:3]) / 111031, 0.0169, places=4)
        self.assertAlmostEqual(105737 / 149568, 0.707, places=3)


if __name__ == "__main__":
    unittest.main()
