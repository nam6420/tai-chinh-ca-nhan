from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research" / "companies" / "VN"))

import calc_wave2 as c  # noqa: E402


class FPT(unittest.TestCase):
    def test_so_hoc(self):
        m = c.fpt_metrics()
        self.assertAlmostEqual(m["rev_growth_like_for_like"], 0.1242, places=4)
        self.assertAlmostEqual(m["gross_margin"], 0.3195, places=4)
        self.assertAlmostEqual(m["assoc_share_of_pbt"], 0.2532, places=4)
        self.assertAlmostEqual(m["net_debt"], -12230.5, places=1)
        self.assertAlmostEqual(m["cfo_over_np"], 0.1224, places=4)
        self.assertAlmostEqual(m["fcf_simple"], -1076.8, places=1)
        self.assertAlmostEqual(m["capital_growth"], 0.1070, places=4)
        self.assertAlmostEqual(m["jpy_vs_vnd"], -0.0639, places=4)
        self.assertAlmostEqual(m["esop_discount"], 0.8689, places=4)

    def test_kich_ban(self):
        s = c.fpt_scenarios()
        self.assertAlmostEqual(s["bat_loi"], 10092.7, places=1)
        self.assertAlmostEqual(s["co_so"], 10501.2, places=1)
        self.assertAlmostEqual(s["thuan_loi"], 10773.5, places=1)
        self.assertAlmostEqual(s["cang"], 9412.0, places=1)
        r = c.fpt_stress_reference()
        self.assertAlmostEqual(r["total"], 434.5, places=1)
        self.assertAlmostEqual(r["cang_drop"], 1089.2, places=1)
        k = c.fpt_stress_mechanism()
        self.assertAlmostEqual(k["q4"], 1513.6, places=1)
        self.assertAlmostEqual(k["fy"], 9291.7, places=1)
        self.assertAlmostEqual(k["ftel_share_est"], 1552.4, places=1)


class VNM(unittest.TestCase):
    def test_so_hoc(self):
        m = c.vnm_metrics()
        self.assertAlmostEqual(m["rev_growth"], 0.1451, places=4)
        self.assertAlmostEqual(m["gm_9t26"], 0.4253, places=4)
        self.assertAlmostEqual(m["net_cash"], 18055.49, places=2)
        self.assertAlmostEqual(m["rm_growth"], 0.3280, places=4)
        self.assertAlmostEqual(m["cogs_growth"], 0.1206, places=4)
        self.assertAlmostEqual(m["div25_total"], 9091.3, places=1)
        self.assertAlmostEqual(m["payout25"], 0.9661, places=4)

    def test_kich_ban(self):
        s = c.vnm_scenarios()
        self.assertAlmostEqual(s["bat_loi"], 11116.3, places=1)
        self.assertAlmostEqual(s["co_so"], 11524.1, places=1)
        self.assertAlmostEqual(s["thuan_loi"], 11968.4, places=1)
        self.assertAlmostEqual(s["cang"], 10264.2, places=1)

    def test_cau_noi_goc_va_q4_loi(self):
        b = c.vnm_bridge()
        self.assertAlmostEqual(b["q3_non_core"], 439.72, places=2)
        self.assertAlmostEqual(b["q3_share"], 0.7736, places=4)
        self.assertAlmostEqual(b["n9_non_core"], 588.83, places=2)
        self.assertAlmostEqual(b["n9_share"], 0.2419, places=4)
        self.assertAlmostEqual(b["core_q3"], 3052.93, places=2)
        self.assertAlmostEqual(b["core_9t"], 9054.77, places=2)
        self.assertAlmostEqual(b["q3_vs_q2_lnst"], -0.0640, places=4)
        self.assertAlmostEqual(b["q1_lnst"], 2428.76, places=2)
        self.assertAlmostEqual(b["deposit_rate_annual"], 0.0592, places=4)
        self.assertAlmostEqual(b["per_1pp"], 265.4, places=1)
        k = c.vnm_core()
        self.assertAlmostEqual(k["q4_core"], 2403.8, places=1)
        self.assertAlmostEqual(k["q4_core_vs_q4_25"], 0.8463, places=4)
        self.assertAlmostEqual(k["fy_core"], 10963.7, places=1)
        self.assertAlmostEqual(k["run_rate_vs_fy25"], 0.0218, places=4)
        self.assertAlmostEqual(k["cang_run_rate_vs_fy25"], -0.2756, places=4)

    def test_cau_noi_va_ke_hoach(self):
        m = c.vnm_metrics()
        self.assertAlmostEqual(m["payout_eps25"], 1.0799, places=4)
        self.assertAlmostEqual(m["pbt_q3_growth"], 568.4, places=1)
        self.assertAlmostEqual(m["non_core_q3"], 439.72, places=2)
        self.assertAlmostEqual(m["non_core_share"], 0.7736, places=4)
        self.assertAlmostEqual(m["plan_implied_q4"], 1223.16, places=2)
        self.assertAlmostEqual(m["scn_vs_fy25_bad"], 0.1813, places=4)
        self.assertAlmostEqual(m["inv_growth_ytd"], 0.1437, places=4)
        self.assertAlmostEqual(m["usd_share_st_debt"], 0.7937, places=4)
        self.assertAlmostEqual(m["np_9t_over_fy25"], 0.9096, places=4)


class VCB(unittest.TestCase):
    def test_so_hoc(self):
        m = c.vcb_metrics()
        self.assertEqual(m["pbt_check_9t"], 40440.0)
        self.assertEqual(m["pbt_6t_plus_q3"], 40440.0)
        self.assertEqual(m["pbt_check_fy25"], 44020.0)
        self.assertAlmostEqual(m["pbt_growth_9t"], 0.2205, places=4)
        self.assertAlmostEqual(m["cir_9t"], 0.3201, places=4)
        self.assertEqual(m["fy25_npl_sum"], 9646.0)
        self.assertEqual(m["fy25_npl_gap"], 182.0)
        self.assertAlmostEqual(m["npl_ratio_simple"], 0.0070, places=4)
        self.assertAlmostEqual(m["pbt_9t_ex_one_off"], 37535.0, places=1)
        self.assertAlmostEqual(m["pbt_growth_ex_one_off"], 0.1329, places=4)
        self.assertAlmostEqual(m["pbt_q2_ex_one_off"], 14514.0, places=1)
        self.assertAlmostEqual(m["q3_vs_q2_ex_one_off"], -0.2271, places=4)
        self.assertAlmostEqual(m["credit_cost_annualised"], 0.0067, places=4)
        self.assertAlmostEqual(m["credit_cost_q3_run_rate"], 0.0136, places=4)
        self.assertAlmostEqual(m["room_left_pp"], 4.0, places=1)
        self.assertAlmostEqual(m["implied_use_q3"], 5040.2, places=1)
        self.assertAlmostEqual(m["bonus_pct"], 0.1279, places=4)
        self.assertAlmostEqual(m["capital_growth_all"], 0.1929, places=4)
        self.assertAlmostEqual(m["state_after_private"], 0.7023, places=4)

    def test_kich_ban_va_stress(self):
        s = c.vcb_scenarios()
        self.assertAlmostEqual(s["bat_loi"], 49414.4, places=1)
        self.assertAlmostEqual(s["co_so"], 51658.0, places=1)
        self.assertAlmostEqual(s["thuan_loi"], 53598.5, places=1)
        self.assertAlmostEqual(s["cang"], 44617.8, places=1)
        self.assertAlmostEqual(s["rat_cang"], 43733.8, places=1)
        m = c.vcb_metrics()
        self.assertAlmostEqual(m["prov_stock_change_h1_from_cover"], 4956.2, places=1)
        self.assertAlmostEqual(m["prov_charge_h1"], 2996.0, places=1)
        self.assertAlmostEqual(m["implied_use_9t"], 3080.0, places=1)
        r = c.vcb_coverage_stress(0.01)
        self.assertAlmostEqual(r["coverage"], 1.7088, places=4)
        self.assertAlmostEqual(r["extra_for_200"], 5300.0, places=1)
        r = c.vcb_coverage_stress(0.015)
        self.assertAlmostEqual(r["coverage"], 1.1392, places=4)
        self.assertAlmostEqual(r["extra_for_200"], 23500.0, places=1)


class HPG(unittest.TestCase):
    def test_so_hoc(self):
        m = c.hpg_metrics()
        self.assertAlmostEqual(m["gm"][2021], 0.2746, places=4)
        self.assertAlmostEqual(m["gm_pooled_5"], 0.1614, places=4)
        self.assertAlmostEqual(m["gm_pooled_4"], 0.1309, places=4)
        self.assertAlmostEqual(m["np_avg_5"], 15454.3, places=1)
        self.assertAlmostEqual(m["np_avg_4"], 10698.4, places=1)
        self.assertAlmostEqual(m["mcap"], 177302.3, places=1)
        self.assertAlmostEqual(m["pe_on_avg5"], 11.47, places=2)
        self.assertAlmostEqual(m["pe_on_avg4"], 16.57, places=2)
        self.assertAlmostEqual(m["interest_cover_fy25"], 9.06, places=2)
        self.assertAlmostEqual(m["cfo_over_np_fy24"], 0.5498, places=4)

    def test_kich_ban(self):
        s = c.hpg_scenarios()
        self.assertAlmostEqual(s["cuc_doan"]["gp_fy"], 36228.0, places=0)
        self.assertAlmostEqual(s["cuc_doan"]["gp_over_interest_q4"], 2.673, places=3)
        self.assertAlmostEqual(s["bat_loi"]["gp_fy"], 38922.0, places=0)
        self.assertAlmostEqual(s["bat_loi"]["gp_over_interest_q4"], 3.993, places=3)
        self.assertAlmostEqual(s["co_so"]["gp_fy"], 42018.1, places=1)
        self.assertAlmostEqual(s["co_so"]["gp_over_interest_q4"], 6.338, places=3)
        self.assertAlmostEqual(s["thuan_loi"]["gp_fy"], 42697.0, places=1)

    def test_chu_ky_xau_va_gia(self):
        s = c.hpg_scenarios()
        self.assertAlmostEqual(s["chu_ky_xau"]["gp_fy"], 33718.5, places=1)
        self.assertAlmostEqual(s["chu_ky_xau"]["gp_over_interest_q4"], 1.443, places=3)
        n = c.hpg_interest_sensitivity()
        self.assertAlmostEqual(n[0.30]["bat_loi"], 3.533, places=3)
        self.assertAlmostEqual(n[0.50]["co_so"], 4.225, places=3)
        a = c.hpg_price_adjust()
        self.assertAlmostEqual(a["change_adj"], -0.1630, places=4)
        self.assertAlmostEqual(a["change_raw"], -0.2391, places=4)

    def test_lai_vay_va_dot_bien(self):
        m = c.hpg_metrics()
        self.assertAlmostEqual(m["interest_q3_yoy"], 2.185, places=3)
        self.assertAlmostEqual(m["one_off_share_np"], 0.2070, places=4)
        self.assertAlmostEqual(m["minh_bought_share"], 0.666, places=3)
        self.assertAlmostEqual(m["assets_growth"], 0.5903, places=4)


class Vong3(unittest.TestCase):
    def test_fpt(self):
        r = c.fpt_round3()
        self.assertAlmostEqual(r["q4_25_est"], 2502.4, places=1)
        self.assertAlmostEqual(r["q4_vs_q4_25"]["co_so"], 0.0882, places=4)
        self.assertAlmostEqual(r["q4_vs_q4_25"]["cang"], -0.3471, places=4)
        self.assertAlmostEqual(r["q4_vs_q4_25"]["cang2"], -0.3952, places=4)
        self.assertAlmostEqual(r["q4_vs_q4_25"]["bat_loi"], -0.0750, places=4)
        self.assertAlmostEqual(r["q4_vs_q4_25"]["thuan_loi"], 0.1970, places=4)
        self.assertAlmostEqual(r["price_2810_vs_peak_adj"], -0.4343, places=4)
        self.assertAlmostEqual(r["esop_discount_2810_adj"], 0.8316, places=4)
        self.assertAlmostEqual(r["ftel_div_share_year_low"], 0.2899, places=4)
        self.assertAlmostEqual(r["ftel_div_share_year_high"], 0.3221, places=4)
        self.assertAlmostEqual(r["pe_trailing_est"], 9.78, places=2)
        self.assertAlmostEqual(r["cfo_plus_27_over_np"], 0.2827, places=4)
        self.assertAlmostEqual(r["capital_growth_formula"], 0.1069, places=4)
        self.assertAlmostEqual(r["run_rate"], 10892.4, places=1)
        self.assertAlmostEqual(r["sign_q3_growth"], 0.0371, places=4)
        self.assertAlmostEqual(r["rev_for_q3_growth"], 0.0823, places=4)
        self.assertAlmostEqual(r["ftel_9t_share_of_assoc"], 0.6034, places=4)
        self.assertAlmostEqual(r["ftel_scaled_share"], 0.5244, places=4)
        self.assertAlmostEqual(r["tax_rate_ex_assoc"], 0.1517, places=4)
        self.assertAlmostEqual(r["price_1507_vs_peak"], -0.3638, places=4)
        self.assertAlmostEqual(r["price_2810_vs_peak"], -0.4857, places=4)
        self.assertAlmostEqual(r["esop_discount_2810"], 0.8148, places=4)

    def test_vnm(self):
        r = c.vnm_round3()
        self.assertAlmostEqual(r["q3_net_non_core"], 379.66, places=2)
        self.assertAlmostEqual(r["q3_net_share"], 0.6679, places=4)
        self.assertAlmostEqual(r["n9_net_share"], 0.1553, places=4)
        self.assertAlmostEqual(r["core_net_q3_growth"], 0.0626, places=4)
        self.assertAlmostEqual(r["core_net_9t_growth"], 0.2760, places=4)
        self.assertAlmostEqual(r["q4_core_net"], 2452.5, places=1)
        self.assertAlmostEqual(r["fy_core_net_vs_fy25"], 0.1703, places=4)
        self.assertAlmostEqual(r["run_core_net_vs_fy25"], 0.0425, places=4)
        self.assertAlmostEqual(r["cang_drop_pre_tax"], 1400.6, places=1)
        self.assertAlmostEqual(r["cang_gm_needed"], 0.3500, places=4)
        self.assertAlmostEqual(r["gm_q3_vs_guidance"], -0.0174, places=4)
        self.assertAlmostEqual(r["net_cash_after_interim"], 12830.6, places=1)
        self.assertAlmostEqual(r["net_cash_end26_illus"], 14975.4, places=1)
        self.assertAlmostEqual(r["transport_growth"], 0.4476, places=4)
        self.assertAlmostEqual(r["usd_off_balance_share"], 0.1106, places=4)

    def test_vnm_vong4(self):
        r = c.vnm_round4()
        self.assertAlmostEqual(r["fin_cost_9t_growth"], 0.8680, places=4)
        self.assertAlmostEqual(r["fn_group"], 24.99, places=2)
        self.assertAlmostEqual(r["duoi_q1_2025"]["vs_q4_25"], -0.4473, places=4)
        self.assertAlmostEqual(r["duoi_q1_2025"]["fy"], 10129.93, places=2)
        self.assertAlmostEqual(r["duoi_q1_2025"]["run_rate_vs_25"], -0.3326, places=4)
        self.assertAlmostEqual(r["duoi_q1_2023"]["vs_q4_25"], -0.3290, places=4)
        self.assertAlmostEqual(r["duoi_q1_2023"]["fy_vs_25"], 0.1122, places=4)

    def test_vcb(self):
        r = c.vcb_round3()
        self.assertAlmostEqual(r["q4_25"], 10887.0, places=1)
        self.assertAlmostEqual(r["q4_vs_q4_25"]["rat_cang"], -0.6975, places=4)
        self.assertAlmostEqual(r["q4_vs_q4_25"]["co_so"], 0.0304, places=4)
        self.assertAlmostEqual(r["q4_vs_q4_25"]["thuan_loi"], 0.2086, places=4)
        self.assertAlmostEqual(r["run_rate"], 44872.0, places=1)
        self.assertAlmostEqual(r["plan_lo"], 46221.0, places=1)
        self.assertAlmostEqual(r["base_vs_plan_lo"], 0.1176, places=4)
        self.assertAlmostEqual(r["implied_prov_thuan_loi"], 4243.5, places=1)
        self.assertAlmostEqual(r["pbt_if_prov_500"], 57342.0, places=1)
        self.assertAlmostEqual(r["mbs_pbt_miss"], -0.2299, places=4)
        self.assertAlmostEqual(r["mbs_prov_ratio"], 9.0, places=1)
        self.assertAlmostEqual(r["npl_start_groups"], 9714.0, places=1)
        self.assertAlmostEqual(r["g34_ratio"], 3.977, places=3)
        self.assertAlmostEqual(r["nonint_gap"], 770.0, places=1)

    def test_vcb_vong4(self):
        r = c.vcb_round4()
        self.assertAlmostEqual(r["run_rate"], 44872.0, places=1)
        self.assertAlmostEqual(r["run_rate_vs_fy25"], 0.0194, places=4)
        self.assertAlmostEqual(r["base_cum_vs_run_rate"], 0.1512, places=4)
        self.assertAlmostEqual(r["bond_prov_up"], 2997.0, places=1)
        self.assertAlmostEqual(r["prov_sum_vs_expense"], 9097.0, places=1)
        self.assertAlmostEqual(r["prov_gap"], 83.0, places=1)
        self.assertAlmostEqual(r["bond_share_of_expense"], 0.3265, places=4)
        self.assertAlmostEqual(r["g2_q3_vs_q2"], 0.1220, places=4)
        self.assertAlmostEqual(r["loans_over_deposits"], 1.0225, places=4)
        self.assertAlmostEqual(r["fx_excess_q3"], 660.0, places=1)
        self.assertAlmostEqual(r["fy_ex_fx"], 50998.0, places=1)
        self.assertAlmostEqual(r["policy_net_q"][0], -2309.0, places=1)
        self.assertAlmostEqual(r["policy_net_q"][1], -3583.0, places=1)

    def test_hpg(self):
        r = c.hpg_round3()
        s = r["scenarios"]
        self.assertAlmostEqual(s["chu_ky_xau"]["gp_less_sell"], 1797.5, places=1)
        self.assertAlmostEqual(s["chu_ky_xau"]["gp_less_sell_less_interest"], -242.6, places=1)
        self.assertAlmostEqual(s["chu_ky_xau"]["rev_vs_q4_25"], -0.2221, places=4)
        self.assertAlmostEqual(s["cuc_doan"]["gp_less_sell"], 3891.5, places=1)
        self.assertAlmostEqual(s["chu_ky_xau"]["gp_run_rate"], 11774.1, places=1)
        self.assertAlmostEqual(r["q2_np"], 6424.0, places=1)
        self.assertAlmostEqual(r["q3_vs_q2_np"], 0.2866, places=4)
        self.assertAlmostEqual(r["np_q1_ex_share"], 0.1624, places=4)
        self.assertAlmostEqual(r["margin_gap_q3"], 0.0014, places=4)
        self.assertAlmostEqual(r["margin_gap_9t"], 0.0013, places=4)
        self.assertAlmostEqual(r["inv_q2_vs_fy25"], 0.0526, places=4)
        self.assertAlmostEqual(r["interest_q3_vs_q2"], 0.1671, places=4)


class Vong4Hpg(unittest.TestCase):
    def test_hpg_vong4(self):
        r = c.hpg_round4()
        self.assertAlmostEqual(r["hard_sell"]["chu_ky_xau"]["after_sell_hard_interest"], -814.6, places=1)
        self.assertAlmostEqual(r["hard_sell"]["cuc_doan"]["after_sell_hard_interest"], 1694.9, places=1)
        self.assertAlmostEqual(r["replay_q4_22_pre_tax"], -3758.1, places=1)
        self.assertAlmostEqual(r["q4_22_margin"], -0.0343, places=4)
        self.assertAlmostEqual(r["interest_ratio_vs_q4_22"], 2.187, places=3)
        self.assertAlmostEqual(r["rev_q3_vs_q2_same_basis"], 0.1280, places=4)
        self.assertAlmostEqual(r["h1_deductions"], 810.0, places=1)
        self.assertAlmostEqual(r["short_share_q3_25"], 0.2928, places=4)
        self.assertAlmostEqual(r["short_share_q3_26"], 0.7435, places=4)


if __name__ == "__main__":
    unittest.main()
