from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research" / "companies" / "VN"))

import calc_insurance_profiles as cip  # noqa: E402


class TestInsuranceProfiles(unittest.TestCase):
    def test_bvh_metrics_and_scenarios(self):
        m = cip.bvh_metrics()
        self.assertAlmostEqual(m["assets_growth"], 0.1612, places=4)
        self.assertAlmostEqual(m["fin_inv_share"], 0.9134, places=4)
        self.assertAlmostEqual(m["repo_growth"], 0.6570, places=4)
        self.assertAlmostEqual(m["net_reserves_25"], 198_000.0753, places=3)
        self.assertAlmostEqual(m["ul_share_of_life_gwp"], 0.8342, places=4)
        self.assertAlmostEqual(m["nwp_25"], 40_307.6321, places=3)
        self.assertAlmostEqual(m["retention_25"], 0.9137, places=4)
        self.assertAlmostEqual(m["uw_gross_profit_25"], 1_237.9463, places=3)
        self.assertAlmostEqual(m["uw_swing_25_vs_24"], 2_207.0592, places=3)
        self.assertAlmostEqual(m["net_fin_25"], 11_120.4658, places=3)
        self.assertAlmostEqual(m["fin_yield_avg"], 0.0447, places=4)
        self.assertAlmostEqual(m["ebt_growth"], 0.3347, places=4)
        self.assertAlmostEqual(m["npat_growth"], 0.3315, places=4)
        self.assertAlmostEqual(m["eps_25"], 3_821.267, places=2)
        self.assertAlmostEqual(m["bvps_parent_25"], 32_938.73, places=1)
        self.assertAlmostEqual(m["roe_parent_avg"], 0.1206, places=4)
        self.assertAlmostEqual(m["solvency_pnt_25"], 1.4050, places=4)
        self.assertAlmostEqual(m["solvency_life_25"], 1.0703, places=4)

        s = cip.bvh_scenarios()
        self.assertAlmostEqual(s["bat_loi"]["pb_justified"], 0.6429, places=4)
        self.assertAlmostEqual(s["co_so"]["pb_justified"], 1.1455, places=4)
        self.assertAlmostEqual(s["thuan_loi"]["pb_justified"], 1.6667, places=4)

    def test_pvi_metrics_and_scenarios(self):
        m = cip.pvi_metrics()
        self.assertAlmostEqual(m["assets_growth"], 0.4000, places=4)
        self.assertAlmostEqual(m["reins_assets_25"], 21_614.4473, places=3)
        self.assertAlmostEqual(m["reins_assets_to_equity"], 2.5328, places=4)
        self.assertAlmostEqual(m["net_reserves_25"], 6_803.0513, places=3)
        self.assertAlmostEqual(m["gwp_growth"], 0.1162, places=4)
        self.assertAlmostEqual(m["inward_growth"], 0.4946, places=4)
        self.assertAlmostEqual(m["nwp_25"], 8_229.2973, places=3)
        self.assertAlmostEqual(m["retention_25"], 0.3239, places=4)
        self.assertAlmostEqual(m["retention_24"], 0.3596, places=4)
        self.assertAlmostEqual(m["nep_25"], 7_633.8999, places=3)
        self.assertAlmostEqual(m["net_claims_25"], 3_286.6259, places=3)
        self.assertAlmostEqual(m["loss_ratio_25"], 0.4305, places=4)
        self.assertAlmostEqual(m["cr_pre_comm_25"], 1.1702, places=4)
        self.assertAlmostEqual(m["cr_post_comm_25"], 0.9950, places=4)
        self.assertAlmostEqual(m["net_fin_25"], 918.2118, places=3)
        self.assertAlmostEqual(m["ebt_growth"], 0.3051, places=4)
        self.assertAlmostEqual(m["npat_growth"], 0.3066, places=4)
        self.assertAlmostEqual(m["bvps_parent_25"], 34_938.16, places=1)
        self.assertAlmostEqual(m["roe_parent_avg"], 0.1377, places=4)

        s = cip.pvi_scenarios()
        self.assertAlmostEqual(s["bat_loi"]["pb_justified"], 0.9286, places=4)
        self.assertAlmostEqual(s["co_so"]["pb_justified"], 1.5091, places=4)
        self.assertAlmostEqual(s["thuan_loi"]["pb_justified"], 2.1111, places=4)

    def test_bic_metrics_and_scenarios(self):
        m = cip.bic_metrics()
        self.assertAlmostEqual(m["assets_growth"], 0.1624, places=4)
        self.assertAlmostEqual(m["fin_inv_25"], 7_221.6316, places=3)
        self.assertAlmostEqual(m["fin_inv_share"], 0.7155, places=4)
        self.assertAlmostEqual(m["net_reserves_25"], 2_825.8195, places=3)
        self.assertAlmostEqual(m["charter_cap_growth"], 0.7230, places=4)
        self.assertAlmostEqual(m["health_share_gwp"], 0.4135, places=4)
        self.assertAlmostEqual(m["fire_share_gwp"], 0.2094, places=4)
        self.assertAlmostEqual(m["motor_share_gwp"], 0.1977, places=4)
        self.assertAlmostEqual(m["nwp_25"], 4_032.7490, places=3)
        self.assertAlmostEqual(m["retention_25"], 0.6959, places=4)
        self.assertAlmostEqual(m["loss_ratio_25"], 0.3014, places=4)
        self.assertAlmostEqual(m["cr_pre_comm_25"], 0.8417, places=4)
        self.assertAlmostEqual(m["cr_post_comm_25"], 0.7560, places=4)
        self.assertAlmostEqual(m["uw_gp_audit_delta"], -31.7477, places=3)
        self.assertAlmostEqual(m["npat_audit_delta"], -1.3597, places=3)
        self.assertAlmostEqual(m["bidv_deposit_share_htm"], 0.6644, places=4)
        self.assertAlmostEqual(m["bidv_comm_share_gwp"], 0.1325, places=4)
        self.assertAlmostEqual(m["solvency_25"], 2.8467, places=4)
        self.assertAlmostEqual(m["uw_gp_drop_q4"], -0.5870, places=4)
        self.assertAlmostEqual(m["npat_drop_q4"], -0.1849, places=4)
        self.assertAlmostEqual(m["net_fin_growth"], 0.3696, places=4)
        self.assertAlmostEqual(m["ebt_growth"], 0.0400, places=4)
        self.assertAlmostEqual(m["npat_growth"], 0.0988, places=4)
        self.assertAlmostEqual(m["bvps_parent_25"], 16_084.05, places=1)
        self.assertAlmostEqual(m["roe_parent_avg"], 0.1751, places=4)

        s = cip.bic_scenarios()
        self.assertAlmostEqual(s["bat_loi"]["pb_justified"], 1.2857, places=4)
        self.assertAlmostEqual(s["co_so"]["pb_justified"], 2.0000, places=4)
        self.assertAlmostEqual(s["thuan_loi"]["pb_justified"], 2.7778, places=4)


if __name__ == "__main__":
    unittest.main()
