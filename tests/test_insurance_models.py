from __future__ import annotations

import math
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "learning" / "practice" / "models"))
import insurance as ins


class TestInsuranceModels(unittest.TestCase):
    def test_load_historical_inputs_and_jpm_geico_bvh_bic_identities(self):
        data = ins.load_historical_inputs()
        # 1. JPMorgan Chase FY2025 (triệu USD)
        nii = float(data[("JPM", "Net interest income")]["2025"])
        nonint_rev = float(data[("JPM", "Noninterest revenue")]["2025"])
        tot_rev = float(data[("JPM", "Total net revenue")]["2025"])
        nonint_exp = float(data[("JPM", "Total noninterest expense")]["2025"])
        ppop = float(data[("JPM", "Pre-provision profit")]["2025"])
        pcl = float(data[("JPM", "Provision for credit losses")]["2025"])
        ni = float(data[("JPM", "Net income")]["2025"])
        loans = float(data[("JPM", "Loans period-end")]["2025"])
        npa = float(data[("JPM", "Nonperforming assets")]["2025"])
        alll = float(data[("JPM", "Allowance for loan losses")]["2025"])
        ce = float(data[("JPM", "Common stockholders equity")]["2025"])

        self.assertEqual(nii + nonint_rev, tot_rev)
        self.assertEqual(tot_rev - nonint_exp, ppop)

        jpm_bridge = ins.bank_operating_bridge(
            nii=nii,
            noninterest_rev=nonint_rev,
            noninterest_exp=nonint_exp,
            provision=pcl,
            tax=(ppop - pcl) - ni,
            earning_assets=3800000.0,
            total_loans=loans,
            npl=npa,
            allowance_for_loan_losses=alll,
            common_equity=ce,
            rwa=2000000.0,
            cet1_capital=292000.0,
        )
        self.assertEqual(jpm_bridge["total_revenue"], 182447.0)
        self.assertEqual(jpm_bridge["ppop"], 86807.0)
        self.assertEqual(jpm_bridge["net_income"], 57048.0)
        self.assertAlmostEqual(jpm_bridge["cir"], 95640.0 / 182447.0)
        self.assertAlmostEqual(jpm_bridge["cet1_ratio"], 0.146)

        # 2. GEICO FY2025 (triệu USD)
        pw = float(data[("GEICO", "Premiums written")]["2025"])
        pe = float(data[("GEICO", "Premiums earned")]["2025"])
        losses = float(data[("GEICO", "Losses and loss adjustment expenses")]["2025"])
        uw_exp = float(data[("GEICO", "Underwriting expenses")]["2025"])
        tot_le = float(data[("GEICO", "Total losses and expenses")]["2025"])
        uw_profit = float(data[("GEICO", "Pre-tax underwriting earnings")]["2025"])
        self.assertEqual(losses + uw_exp, tot_le)
        self.assertEqual(pe - tot_le, uw_profit)

        geico = ins.pc_underwriting_bridge(
            direct_premium=pw,
            inward_reinsurance_premium=0.0,
            outward_reinsurance_ceded=0.0,
            change_in_gross_upr=pw - pe,
            change_in_ceded_upr=0.0,
            net_incurred_claims=losses,
            net_underwriting_expenses=uw_exp,
            float_balance=float(data[("BRK_INS", "Insurance float year-end")]["2025"]),
            investment_income=float(data[("BRK_INS", "Net investment income pre-tax")]["2025"]),
        )
        self.assertEqual(geico["net_earned_premium"], 44481.0)
        self.assertEqual(geico["underwriting_profit"], 6824.0)
        self.assertAlmostEqual(round(geico["loss_ratio"] * 100, 1), 72.3)
        self.assertAlmostEqual(round(geico["expense_ratio"] * 100, 1), 12.4)
        self.assertAlmostEqual(round(geico["combined_ratio"] * 100, 1), 84.7)
        self.assertLess(geico["cost_of_float"], 0.0)

        # 3. BIC FY2025 (triệu VND): kiểm tra cầu nối doanh thu phí bảo hiểm thuần
        bic = ins.pc_underwriting_bridge(
            direct_premium=float(data[("BIC", "Phi bao hiem goc")]["2025"]),
            inward_reinsurance_premium=float(data[("BIC", "Phi nhan tai bao hiem")]["2025"]),
            outward_reinsurance_ceded=-float(data[("BIC", "Tong phi nhuong tai bao hiem")]["2025"]),
            change_in_gross_upr=-float(data[("BIC", "Tang du phong phi goc va nhan tai")]["2025"]),
            change_in_ceded_upr=float(data[("BIC", "Tang du phong phi nhuong tai")]["2025"]),
            net_incurred_claims=-float(data[("BIC", "Tong chi boi thuong bao hiem")]["2025"])
            - float(data[("BIC", "Tang du phong dao dong lon")]["2025"]),
            net_underwriting_expenses=-float(data[("BIC", "Chi phi khac hoat dong KDBH")]["2025"]),
            reinsurance_commission_and_other=float(data[("BIC", "Hoa hong nhuong tai va doanh thu khac KDBH")]["2025"]),
        )
        self.assertAlmostEqual(bic["net_earned_premium"], 3948219.0, places=0)
        self.assertAlmostEqual(bic["underwriting_profit"], 994937.0, places=0)

    def test_upr_methods_and_vas_gross_vs_net_reserves(self):
        self.assertEqual(ins.upr_percentage(1000.0, is_cargo_short_term=True), 250.0)
        self.assertEqual(ins.upr_percentage(1000.0, is_cargo_short_term=False), 500.0)
        self.assertEqual(ins.upr_1_8(800.0, 800.0, 800.0, 800.0), 1600.0)
        self.assertAlmostEqual(ins.upr_1_24([240.0] * 12), 1440.0)
        self.assertAlmostEqual(ins.upr_daily(365.0, 100, 365), 100.0)

        # Kiểm chứng số thực Thuyết minh 24 BCTC hợp nhất kiểm toán FY2025 của Tập đoàn Bảo Việt (triệu VND):
        # Dự phòng PNT gốc & nhận tái (bảng trên tr. 61 BCTC) = 5.564.312,424 + 3.164.674,687 + 172.891,835 + 329.353,303 = 9.231.232,250
        # Tài sản tái bảo hiểm PNT = 1.890.740,497 + 1.791.669,701 = 3.682.410,199 -> Dự phòng thuần = 5.548.822,052
        bvh_res = ins.vas_gross_vs_net_reserves(
            gross_upr=5564312.424245,
            gross_claim_reserve=3164674.687097,
            ceded_upr_asset=1890740.497412,
            ceded_claim_asset=1791669.701205,
            other_gross_reserves=172891.835464 + 329353.303474,
        )
        self.assertAlmostEqual(bvh_res["liability_reserves_gross"], 9231232.250280, places=3)
        self.assertAlmostEqual(bvh_res["reinsurance_assets"], 3682410.198617, places=3)
        self.assertAlmostEqual(bvh_res["net_total_reserves"], 5548822.051663, places=3)

    def test_chain_ladder_reproduces_tt67_vbhn44_official_example(self):
        cl = ins.chain_ladder_reserve(ins.TT67_INCREMENTAL_TRIANGLE)
        self.assertEqual(cl["factors"], [1.625, 1.236, 1.163, 1.089, 1.047, 1.030, 1.013])
        self.assertEqual(cl["total_paid"], 149872.0)
        self.assertEqual(cl["total_ultimate"], 208341.0)
        self.assertEqual(cl["total_reserve"], 58469.0)
        self.assertEqual(
            cl["ultimates"],
            [14032.0, 14197.0, 18266.0, 23595.0, 28346.0, 29716.0, 38055.0, 42134.0],
        )
        self.assertEqual(
            cl["reserves_by_year"],
            [0.0, 182.0, 760.0, 1996.0, 4519.0, 8238.0, 15802.0, 26972.0],
        )

    def test_reserve_understatement_and_life_tech_rate_and_ifrs17_csm(self):
        adj = ins.reserve_understatement_adjustment(
            reported_net_income=1000.0,
            reported_equity=5000.0,
            reserve_shortfall_pretax=500.0,
            tax_rate=0.20,
            market_cap=7500.0,
        )
        self.assertEqual(adj["after_tax_shortfall"], 400.0)
        self.assertEqual(adj["adjusted_net_income"], 600.0)
        self.assertEqual(adj["adjusted_equity"], 4600.0)
        self.assertAlmostEqual(adj["reported_roe"], 0.20)
        self.assertAlmostEqual(adj["adjusted_roe"], 600.0 / 4600.0)
        self.assertAlmostEqual(adj["reported_pb"], 1.50)
        self.assertAlmostEqual(adj["adjusted_pb"], 7500.0 / 4600.0)

        # Trần lãi suất kỹ thuật (Điều 38 Khoản 2(b) VBHN 44/2026/VBHN-TT-BTC)
        self.assertAlmostEqual(ins.vn_life_max_tech_rate(0.03, 0.05, 0.04), 0.024)
        sens = ins.math_reserve_rate_sensitivity(1000.0, 15.0, 0.035, 0.025)
        self.assertGreater(sens["reserve_increase"], 0.0)
        self.assertAlmostEqual(sens["pct_change"], ((1.035 / 1.025) ** 15) - 1.0)

        # IFRS 17 CSM roll-forward (bình thường và hợp đồng có rủi ro lỗ - onerous)
        normal = ins.ifrs17_csm_rollforward(1000.0, 200.0, 0.04, -40.0, 150.0, 850.0)
        self.assertEqual(normal["interest_accretion"], 40.0)
        self.assertEqual(normal["pre_release_csm"], 1200.0)
        self.assertEqual(normal["loss_component_recognized"], 0.0)
        self.assertAlmostEqual(normal["csm_released_to_revenue"], 180.0)
        self.assertAlmostEqual(normal["closing_csm"], 1020.0)

        onerous = ins.ifrs17_csm_rollforward(200.0, 0.0, 0.05, -260.0, 100.0, 400.0)
        self.assertEqual(onerous["pre_release_csm"], 0.0)
        self.assertEqual(onerous["loss_component_recognized"], 50.0)
        self.assertEqual(onerous["csm_released_to_revenue"], 0.0)
        self.assertEqual(onerous["closing_csm"], 0.0)

    def test_solvency_margin_pnt_and_ul_vs_term_invest(self):
        sm = ins.solvency_margin_pnt(
            net_retained_premium=4000.0,
            total_gross_and_assumed_premium=9000.0,
            owners_equity_eligible=2000.0,
            unsecured_corp_bonds=200.0,
            listed_shares_and_fund_units=400.0,
            unlisted_shares=100.0,
            tangible_fixed_and_intangible_software_land_inventory=200.0,
            overdue_receivables_over_2y_or_illiquid=50.0,
            secured_corp_bonds=100.0,
        )
        # max(0.25*4000=1000, 0.125*9000=1125) = 1125
        self.assertEqual(sm["minimum_solvency_margin"], 1125.0)
        # deductions = 50 + 1 + 6 + 60 + 20 + 50 = 187
        self.assertEqual(sm["asset_haircut_deductions"], 187.0)
        self.assertEqual(sm["actual_solvency_margin"], 1813.0)
        self.assertAlmostEqual(sm["solvency_ratio"], 1813.0 / 1125.0)

        # Kiểm tra trần phí ban đầu Điều 22 Khoản 3 VBHN 44/2026/VBHN-TT-BTC
        self.assertEqual([ins.vn_ul_initial_fee_rate(y) for y in range(1, 12)],
                         [0.50, 0.30, 0.20, 0.20, 0.20, 0.02, 0.02, 0.02, 0.02, 0.02, 0.0])

        comp = ins.ul_vs_term_invest(
            annual_total_budget=20.0,
            base_premium_ul=20.0,
            sum_assured=1000.0,
            coi_rates_per_1000=[1.8, 1.9, 2.0, 2.1, 2.2, 2.4, 2.6, 2.8, 3.0, 3.3],
            annual_admin_fee_ul=0.42,
            gross_fund_return=0.065,
            ul_fund_mgmt_fee_rate=0.02,
            term_annual_premium=1.8,
            etf_expense_ratio=0.005,
        )
        # Tổng phí ban đầu 10 năm trên phí cơ bản 20 tr.đ/năm = 20 * (0.5 + 0.3 + 0.6 + 0.1) = 30 tr.đ
        self.assertAlmostEqual(comp["total_initial_fees_paid"], 30.0)
        self.assertGreater(comp["final_diy_portfolio_value"], comp["final_ul_account_value"])
        self.assertGreater(comp["schedule"][2]["wealth_gap_diy_minus_ul_surrender"], 0.0)

    def test_invalid_inputs_raise_value_error(self):
        bad_calls = [
            lambda: ins.upr_daily(100.0, 400, 365),
            lambda: ins.upr_1_24([10.0] * 11),
            lambda: ins.chain_ladder_reserve([[100.0]]),
            lambda: ins.vn_ul_initial_fee_rate(0),
            lambda: ins.ul_vs_term_invest(20.0, 25.0, 1000.0, [2.0], 0.4, 0.06, 0.02, 1.8),
            lambda: ins.ul_vs_term_invest(20.0, 15.0, 1000.0, [2.0], 0.4, 0.06, 0.02, 1.8, topup_initial_fee_rate_first_10y=0.05),
            lambda: ins.bank_operating_bridge(10, 5, 20, 1, 0, 0, 100, 1, 1, 10),
            lambda: ins.pc_underwriting_bridge(10, 0, 15, 0, 0, 5, 2),
            lambda: ins.solvency_margin_pnt(0, 0, 100),
            lambda: ins.upr_percentage(math.nan),
        ]
        for call in bad_calls:
            with self.assertRaises(ValueError):
                call()


if __name__ == "__main__":
    unittest.main()
