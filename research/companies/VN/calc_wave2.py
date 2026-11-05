#!/usr/bin/env python3
"""Tái tính các con số của bốn hồ sơ Đợt 2 (FPT, VNM, VCB, HPG) bằng thư viện chuẩn.

Đầu vào chép từ báo cáo gốc đã dẫn trong source-register.md của từng mã.
Đơn vị: tỷ VND nếu không ghi khác. Kết quả của kịch bản là KỊCH_BẢN, không là dự báo.
"""

from __future__ import annotations

# ---- FPT (BCTC hợp nhất Q3/2026; FTEL ghi nhận theo vốn chủ từ 01/01/2026)
FPT = {
    "rev_9t26": 40022.7, "rev_9t25_adj": 35600.5,
    "gp_9t26": 12789.0, "assoc_9t26": 2220.3, "pbt_9t26": 8770.2,
    "pbt_9t25_adj": 7495.5,
    "np_parent_9t26": 7778.1, "np_parent_q3": 2723.1, "np_total_9t26": 7776.4,
    "cfo_9t26": 952.0, "capex_9t26": 2028.8,
    "cash": 7377.3, "st_invest": 21449.7, "debt_st": 14316.5, "debt_lt": 2280.0,
    "equity": 44039.4, "nci": 1165.8,
    "paid_in_end25": 17035.1, "paid_in_q3": 18857.3,
    "plan_pbt_2026": 11629.0,
    "growth_jp_vnd": 0.172, "growth_jp_jpy": 0.252,
    "esop_price": 10000.0, "esop_market_price": 76300.0,
    "q3_rev": 13754.2, "q3_assoc": 796.9,
    "ftel_np_2025": 3400.0, "ftel_stake": 0.4566,
}


def fpt_metrics(d=FPT):
    debt = d["debt_st"] + d["debt_lt"]
    return {
        "rev_growth_like_for_like": d["rev_9t26"] / d["rev_9t25_adj"] - 1,
        "gross_margin": d["gp_9t26"] / d["rev_9t26"],
        "assoc_share_of_pbt": d["assoc_9t26"] / d["pbt_9t26"],
        "pbt_margin": d["pbt_9t26"] / d["rev_9t26"],
        "pbt_growth_like_for_like": d["pbt_9t26"] / d["pbt_9t25_adj"] - 1,
        "debt": debt,
        "net_debt": debt - (d["cash"] + d["st_invest"]),
        "debt_to_equity": debt / d["equity"],
        "equity_parent": d["equity"] - d["nci"],
        "cfo_over_np": d["cfo_9t26"] / d["np_total_9t26"],
        "fcf_simple": d["cfo_9t26"] - d["capex_9t26"],
        "capital_growth": d["paid_in_q3"] / d["paid_in_end25"] - 1,
        "pbt_vs_plan": d["pbt_9t26"] / d["plan_pbt_2026"],
        "jpy_vs_vnd": (1 + d["growth_jp_vnd"]) / (1 + d["growth_jp_jpy"]) - 1,
        "esop_discount": 1 - d["esop_price"] / d["esop_market_price"],
    }


def fpt_scenarios(d=FPT):
    """LNST công ty mẹ cả năm 2026 = 9T + Q4 giả định theo tỷ lệ của Q3."""
    return {
        name: d["np_parent_9t26"] + k * d["np_parent_q3"]
        for name, k in (("cang", 0.60), ("bat_loi", 0.85), ("co_so", 1.00),
                        ("thuan_loi", 1.10))
    }


def fpt_stress_mechanism(d=FPT):
    """Q4 = Q3, lợi nhuận liên kết bằng 0, biên gộp giảm 3 điểm; không tính lá chắn thuế (thận trọng)."""
    q4 = d["np_parent_q3"] - d["q3_assoc"] - 0.03 * d["q3_rev"]
    return {"q4": q4, "fy": d["np_parent_9t26"] + q4,
            "ftel_share_est": d["ftel_np_2025"] * d["ftel_stake"]}


def fpt_stress_reference(d=FPT):
    """Tác động trước thuế của biên gộp giảm 2 điểm và lợi nhuận liên kết giảm 20% ở Q4 (Q4 = Q3)."""
    gp_hit = 0.02 * d["q3_rev"]
    assoc_hit = 0.20 * d["q3_assoc"]
    q4_drop = (1 - 0.60) * d["np_parent_q3"]
    return {"gp_hit": gp_hit, "assoc_hit": assoc_hit,
            "total": gp_hit + assoc_hit, "cang_drop": q4_drop}


# Đầu vào bổ sung vòng 3 (số làm tròn từ thông cáo S2/S16/S19; sai số vài điểm phần trăm)
FPT_R3 = {
    "np_parent_fy25": 9369.0, "np_parent_9t25": 6866.6,  # S1 mã 61 cột 2025
    "ftel_div_low": 450.0, "ftel_div_high": 500.0, "eps_9t26": 4142.0,
    "cfo_adj_mã27": 1246.0,
    "sign_9t": 36137.0, "sign_9t_g": 0.231, "sign_6t": 26338.0, "sign_6t_g": 0.323,
    "rev_for_9t": 28538.0, "rev_for_9t_g": 0.116,
    "rev_for_6t": 18902.0, "rev_for_6t_g": 0.134,
    "ftel_np_9t26": 2934.0,
    "price_peak": 105000.0, "price_1507": 66800.0, "price_2810": 54000.0,
}


def fpt_round3(d=FPT, r=FPT_R3):
    """So Q4 với Q4/2025, tốc độ chạy năm, quý 3 riêng, FTEL 9 tháng, thuế, giá so với đỉnh."""
    q4_25 = r["np_parent_fy25"] - r["np_parent_9t25"]
    q4 = {"cang2": d["np_parent_q3"] - d["q3_assoc"] - 0.03 * d["q3_rev"],
          "cang": 0.60 * d["np_parent_q3"], "bat_loi": 0.85 * d["np_parent_q3"],
          "co_so": d["np_parent_q3"], "thuan_loi": 1.10 * d["np_parent_q3"]}
    sign_q3 = r["sign_9t"] - r["sign_6t"]
    sign_q3_prev = r["sign_9t"] / (1 + r["sign_9t_g"]) - r["sign_6t"] / (1 + r["sign_6t_g"])
    rev_q3 = r["rev_for_9t"] - r["rev_for_6t"]
    rev_q3_prev = (r["rev_for_9t"] / (1 + r["rev_for_9t_g"])
                   - r["rev_for_6t"] / (1 + r["rev_for_6t_g"]))
    tax_cost = d["pbt_9t26"] - d["np_total_9t26"]
    return {
        "q4_25_est": q4_25,
        "q4_vs_q4_25": {k: v / q4_25 - 1 for k, v in q4.items()},
        "run_rate": 4 * d["np_parent_q3"],
        "run_rate_down10": 0.9 * 4 * d["np_parent_q3"],
        "sign_q3": sign_q3, "sign_q3_growth": sign_q3 / sign_q3_prev - 1,
        "rev_for_q3": rev_q3, "rev_for_q3_growth": rev_q3 / rev_q3_prev - 1,
        "ftel_9t_share": r["ftel_np_9t26"] * d["ftel_stake"],
        "ftel_9t_share_of_assoc": r["ftel_np_9t26"] * d["ftel_stake"] / d["assoc_9t26"],
        "ftel_scaled_9t": d["ftel_np_2025"] * d["ftel_stake"] * 0.75,
        "ftel_scaled_share": d["ftel_np_2025"] * d["ftel_stake"] * 0.75 / d["assoc_9t26"],
        "tax_cost": tax_cost,
        "tax_rate_ex_assoc": tax_cost / (d["pbt_9t26"] - d["assoc_9t26"]),
        "price_1507_vs_peak": r["price_1507"] / r["price_peak"] - 1,
        "price_2810_vs_peak": r["price_2810"] / r["price_peak"] - 1,
        "esop_discount_2810": 1 - d["esop_price"] / r["price_2810"],
        "peak_adj": r["price_peak"] / 1.1,
        "price_2810_vs_peak_adj": r["price_2810"] / (r["price_peak"] / 1.1) - 1,
        "esop_discount_2810_adj": 1 - (d["esop_price"] / 1.1) / r["price_2810"],
        "ftel_div_share_year_low": r["ftel_div_low"] / (d["ftel_np_2025"] * d["ftel_stake"]),
        "ftel_div_share_year_high": r["ftel_div_high"] / (d["ftel_np_2025"] * d["ftel_stake"]),
        "pe_trailing_est": r["price_2810"] / (r["eps_9t26"] * 4 / 3),
        "cfo_plus_27_over_np": (d["cfo_9t26"] + r["cfo_adj_mã27"]) / d["np_total_9t26"],
        "capital_growth_formula": (1 + 0.0063) * 1.10 - 1,
    }


# ---- VNM (BCTC hợp nhất Q3/2026 đã soát xét; số 2025 phân loại lại)
VNM = {
    "rev_9t26": 53461.20, "rev_9t25": 46688.78,
    "gp_9t26": 22736.56, "gp_9t25": 19269.62,
    "sell_9t26": 11713.83, "sell_9t25": 10454.86,
    "np_parent_9t26": 8559.93, "np_parent_9t25": 6569.83,
    "np_parent_q3": 2964.17,
    "np_parent_q4_25": 2840.37,
    "np_total_9t26": 8604.84,
    "cfo_9t26": 7745.82, "capex_9t26": 1311.51,
    "cash": 3611.99, "dep_st": 22925.58, "debt_st": 8384.69, "debt_lt": 97.39,
    "equity": 38264.20, "nci": 3792.93,
    "shares_m": 2089.955445,
    "dps_final25": 1850, "dps_interim25": 2500, "dps_interim26": 2500,
    "dps_total25": 4350, "np_parent_fy25": 6569.83 + 2840.37,
    "dom_9t26": 41313.48, "dom_9t25": 37190.13,
    "for_9t26": 12147.72, "for_9t25": 9498.65,
    "rm_9t26": 29329.78, "rm_9t25": 22086.04,
    "cogs_9t26": 30724.64, "cogs_9t25": 27419.16,
    "plan_np_2026": 9828.0,
    "np_fy25_total": 9413.59, "eps_fy25": 4028.0,
    "fin_income_q3": 600.34, "fin_income_q3_prev": 395.84,
    "assoc_q3": 40.73, "assoc_q3_prev": -194.49, "pbt_q3": 3694.00,
    "fin_9t": 1413.10, "fin_9t_prev": 1138.51, "assoc_9t": 139.70,
    "assoc_9t_prev": -174.54, "pbt_9t": 10607.57, "pbt_9t_prev": 8172.99,
    "tax_9t": 2002.73, "gm_q3": 0.4136, "gm_q2": 0.435, "rev_q3": 18465.19,
    "np_parent_q2": 3167.0, "interest_deposit_9t": 1179.11,
    "pbt_q3_prev": 3125.60, "inv_now": 7468.56, "inv_start": 6529.98,
    "cogs_9t26": 30724.64, "usd_debt_st": 6654.69,
    "net_cash_start": 1794.88 + 21890.95 - (9393.74 + 62.91),
    "div_paid_9t": 3901.21,
}


def vnm_metrics(d=VNM):
    debt = d["debt_st"] + d["debt_lt"]
    total_div = d["dps_total25"] * d["shares_m"] / 1000
    return {
        "rev_growth": d["rev_9t26"] / d["rev_9t25"] - 1,
        "gm_9t26": d["gp_9t26"] / d["rev_9t26"],
        "gm_9t25": d["gp_9t25"] / d["rev_9t25"],
        "sell_ratio_9t26": d["sell_9t26"] / d["rev_9t26"],
        "sell_ratio_9t25": d["sell_9t25"] / d["rev_9t25"],
        "np_growth": d["np_parent_9t26"] / d["np_parent_9t25"] - 1,
        "net_cash": d["cash"] + d["dep_st"] - debt,
        "cfo_over_np": d["cfo_9t26"] / d["np_total_9t26"],
        "fcf_simple": d["cfo_9t26"] - d["capex_9t26"],
        "dom_growth": d["dom_9t26"] / d["dom_9t25"] - 1,
        "for_growth": d["for_9t26"] / d["for_9t25"] - 1,
        "for_share": d["for_9t26"] / d["rev_9t26"],
        "rm_growth": d["rm_9t26"] / d["rm_9t25"] - 1,
        "cogs_growth": d["cogs_9t26"] / d["cogs_9t25"] - 1,
        "div25_total": total_div,
        "payout25": total_div / d["np_parent_fy25"],
        "div_interim26_total": d["dps_interim26"] * d["shares_m"] / 1000,
        "np_vs_plan": d["np_total_9t26"] / d["plan_np_2026"],
        "payout_eps25": d["dps_total25"] / d["eps_fy25"],
        "pbt_q3_growth": d["pbt_q3"] - d["pbt_q3_prev"],
        "non_core_q3": (d["fin_income_q3"] - d["fin_income_q3_prev"])
        + (d["assoc_q3"] - d["assoc_q3_prev"]),
        "non_core_share": ((d["fin_income_q3"] - d["fin_income_q3_prev"])
                           + (d["assoc_q3"] - d["assoc_q3_prev"]))
        / (d["pbt_q3"] - d["pbt_q3_prev"]),
        "inv_growth_ytd": d["inv_now"] / d["inv_start"] - 1,
        "plan_implied_q4": d["plan_np_2026"] - d["np_total_9t26"],
        "usd_share_st_debt": d["usd_debt_st"] / d["debt_st"],
        "np_9t_over_fy25": d["np_parent_9t26"] / d["np_parent_fy25"],
        "scn_vs_fy25_bad": vnm_scenarios(d)["bat_loi"] / d["np_parent_fy25"] - 1,
    }


def vnm_core(d=VNM):
    """Q4 lõi: Q3 trừ phần tăng thu nhập tài chính và lãi liên kết, biên gộp về 40,0%; thuế theo thuế suất hiệu dụng 9T."""
    tax = d["tax_9t"] / d["pbt_9t"]
    non_core_pre = ((d["fin_income_q3"] - d["fin_income_q3_prev"])
                    + (d["assoc_q3"] - d["assoc_q3_prev"]))
    gm_hit_pre = (d["gm_q3"] - 0.40) * d["rev_q3"]
    q4 = d["np_parent_q3"] - (non_core_pre + gm_hit_pre) * (1 - tax)
    return {"tax": tax, "non_core_pre": non_core_pre, "gm_hit_pre": gm_hit_pre,
            "q4_core": q4, "q4_core_vs_q4_25": q4 / d["np_parent_q4_25"],
            "fy_core": d["np_parent_9t26"] + q4, "run_rate": 4 * q4,
            "run_rate_vs_fy25": 4 * q4 / d["np_parent_fy25"] - 1,
            "cang_run_rate": 4 * 0.60 * d["np_parent_q4_25"],
            "cang_run_rate_vs_fy25": 4 * 0.60 * d["np_parent_q4_25"] / d["np_parent_fy25"] - 1}


def vnm_runrate(d=VNM):
    """Q4 giả định, so với Q4/2025 và tốc độ chạy năm (4 x Q4) so với LNST mẹ FY2025."""
    out = {}
    for name, q4 in (("cang", 0.60 * d["np_parent_q4_25"]),
                     ("bat_loi", 0.90 * d["np_parent_q4_25"]),
                     ("q4_loi", vnm_core(d)["q4_core"]),
                     ("co_so", d["np_parent_q3"]),
                     ("thuan_loi", 1.20 * d["np_parent_q4_25"])):
        out[name] = {"q4": q4, "vs_q4_25": q4 / d["np_parent_q4_25"] - 1,
                     "fy": d["np_parent_9t26"] + q4, "fy_vs_25": (d["np_parent_9t26"] + q4) / d["np_parent_fy25"] - 1,
                     "run_rate": 4 * q4, "run_rate_vs_25": 4 * q4 / d["np_parent_fy25"] - 1}
    return out


def vnm_bridge(d=VNM):
    """Cầu nối lợi nhuận trước thuế từ số gốc S1: Q3 và 9 tháng."""
    q3_inc = (d["fin_income_q3"] - d["fin_income_q3_prev"]) + (d["assoc_q3"] - d["assoc_q3_prev"])
    n9_inc = (d["fin_9t"] - d["fin_9t_prev"]) + (d["assoc_9t"] - d["assoc_9t_prev"])
    return {
        "q3_non_core": q3_inc, "q3_share": q3_inc / (d["pbt_q3"] - d["pbt_q3_prev"]),
        "n9_non_core": n9_inc,
        "n9_share": n9_inc / (d["pbt_9t"] - d["pbt_9t_prev"]),
        "core_q3": d["pbt_q3"] - d["fin_income_q3"] - d["assoc_q3"],
        "core_q3_prev": d["pbt_q3_prev"] - d["fin_income_q3_prev"] - d["assoc_q3_prev"],
        "core_9t": d["pbt_9t"] - d["fin_9t"] - d["assoc_9t"],
        "core_9t_prev": d["pbt_9t_prev"] - d["fin_9t_prev"] - d["assoc_9t_prev"],
        "q3_vs_q2_lnst": d["np_parent_q3"] / d["np_parent_q2"] - 1,
        "q1_lnst": d["np_parent_9t26"] - d["np_parent_q2"] - d["np_parent_q3"],
        "deposit_rate_9m": d["interest_deposit_9t"] / (d["cash"] + d["dep_st"]),
        "deposit_rate_annual": d["interest_deposit_9t"] / (d["cash"] + d["dep_st"]) * 12 / 9,
        "per_1pp": (d["cash"] + d["dep_st"]) * 0.01,
        "per_1pp_after_tax": (d["cash"] + d["dep_st"]) * 0.01 * (1 - d["tax_9t"] / d["pbt_9t"]),
    }


def vnm_scenarios(d=VNM):
    """LNST công ty mẹ 2026 = 9T + Q4 giả định."""
    q4 = {
        "cang": 0.60 * d["np_parent_q4_25"],
        "bat_loi": 0.90 * d["np_parent_q4_25"],
        "co_so": d["np_parent_q3"],
        "thuan_loi": 1.20 * d["np_parent_q4_25"],
    }
    return {k: d["np_parent_9t26"] + v for k, v in q4.items()}


# Đầu vào bổ sung vòng 3 (S1: thuyết minh VI.4 chi phí tài chính; S11/S13/S21: báo chí)
VNM_R3 = {
    "fin_cost_q3": 151.41, "fin_cost_q3_prev": 91.35,
    "fin_cost_9t": 453.30, "fin_cost_9t_prev": 242.67,
    "gm_q4_25": 0.4044, "q1_rev_press": 16178.0, "rev_q2_press": 18847.0,
    "gp_9t26": 22736.56, "gm_guidance_2h": 0.431,
    "div_interim26": 2500 * 2089.955445 / 1000,
}


def vnm_round3(d=VNM, r=VNM_R3):
    """Cầu nối ròng (trừ cả chi phí tài chính), Q4 lõi ròng, neo kịch bản căng, thời điểm cổ tức."""
    tax = d["tax_9t"] / d["pbt_9t"]
    q3_net_inc = (d["fin_income_q3"] - r["fin_cost_q3"]) - (d["fin_income_q3_prev"] - r["fin_cost_q3_prev"]) \
        + (d["assoc_q3"] - d["assoc_q3_prev"])
    n9_net_inc = (d["fin_9t"] - r["fin_cost_9t"]) - (d["fin_9t_prev"] - r["fin_cost_9t_prev"]) \
        + (d["assoc_9t"] - d["assoc_9t_prev"])
    core_q3 = d["pbt_q3"] - (d["fin_income_q3"] - r["fin_cost_q3"]) - d["assoc_q3"]
    core_q3_prev = d["pbt_q3_prev"] - (d["fin_income_q3_prev"] - r["fin_cost_q3_prev"]) - d["assoc_q3_prev"]
    core_9t = d["pbt_9t"] - (d["fin_9t"] - r["fin_cost_9t"]) - d["assoc_9t"]
    core_9t_prev = d["pbt_9t_prev"] - (d["fin_9t_prev"] - r["fin_cost_9t_prev"]) - d["assoc_9t_prev"]
    gm_hit = (d["gm_q3"] - 0.40) * d["rev_q3"]
    q4_net = d["np_parent_q3"] - (q3_net_inc + gm_hit) * (1 - tax)
    cang_q4 = 0.60 * d["np_parent_q4_25"]
    gap_pre = (q4_net - cang_q4) / (1 - tax)
    q4_other = d["gp_9t26"] - 8198.4 - 7636.55
    return {
        "q3_net_non_core": q3_net_inc,
        "q3_net_share": q3_net_inc / (d["pbt_q3"] - d["pbt_q3_prev"]),
        "n9_net_non_core": n9_net_inc,
        "n9_net_share": n9_net_inc / (d["pbt_9t"] - d["pbt_9t_prev"]),
        "core_net_q3": core_q3, "core_net_q3_growth": core_q3 / core_q3_prev - 1,
        "core_net_9t": core_9t, "core_net_9t_growth": core_9t / core_9t_prev - 1,
        "q4_core_net": q4_net, "q4_core_net_vs_q4_25": q4_net / d["np_parent_q4_25"] - 1,
        "fy_core_net": d["np_parent_9t26"] + q4_net,
        "fy_core_net_vs_fy25": (d["np_parent_9t26"] + q4_net) / d["np_parent_fy25"] - 1,
        "run_core_net": 4 * q4_net, "run_core_net_vs_fy25": 4 * q4_net / d["np_parent_fy25"] - 1,
        "cang_drop_after_tax": d["np_parent_q4_25"] - cang_q4,
        "cang_drop_pre_tax": (d["np_parent_q4_25"] - cang_q4) / (1 - tax),
        "cang_gap_vs_core_pre_tax": gap_pre,
        "cang_extra_margin_pts": gap_pre / d["rev_q3"],
        "cang_gm_needed": 0.40 - gap_pre / d["rev_q3"],
        "gm_q3_vs_guidance": d["gm_q3"] - r["gm_guidance_2h"],
        "q1_gm_est": q4_other / r["q1_rev_press"],
        "q1_rev_implied": d["rev_9t26"] - r["rev_q2_press"] - d["rev_q3"],
        "div_interim26": r["div_interim26"],
        "net_cash_after_interim": 18055.49 - r["div_interim26"],
        "fcf_per_quarter": (d["cfo_9t26"] - d["capex_9t26"]) / 3,
        "net_cash_end26_illus": 18055.49 + (d["cfo_9t26"] - d["capex_9t26"]) / 3 - r["div_interim26"],
        "transport_growth": 933.046 / 644.543 - 1,
        "fin_cost_q3_growth": r["fin_cost_q3"] / r["fin_cost_q3_prev"] - 1,
        "usd_off_balance_share": 735.86 / d["usd_debt_st"],
    }


def vnm_round4(d=VNM, r=VNM_R3):
    """Kịch bản đuôi neo lịch sử (Q1/2025 khoảng 1.570 tỷ; Q1/2023 1.906 tỷ), tăng chi phí tài chính 9T, nhóm F&N."""
    out = {"fin_cost_9t_growth": r["fin_cost_9t"] / r["fin_cost_9t_prev"] - 1,
           "fn_group": 22.29 + 2.7,
           "q1_25_est": 2429.0 / 1.55}
    for name, q4 in (("duoi_q1_2025", 1570.0), ("duoi_q1_2023", 1906.0)):
        out[name] = {"q4": q4, "vs_q4_25": q4 / d["np_parent_q4_25"] - 1,
                     "fy": d["np_parent_9t26"] + q4,
                     "fy_vs_25": (d["np_parent_9t26"] + q4) / d["np_parent_fy25"] - 1,
                     "run_rate": 4 * q4, "run_rate_vs_25": 4 * q4 / d["np_parent_fy25"] - 1}
    return out


# ---- VCB (số báo chí và báo cáo thứ cấp; chưa đối chiếu BCTC gốc)
VCB = {
    "pbt_9t26": 40440.0, "pbt_9t25": 33133.0, "pbt_q3_26": 11218.0,
    "pbt_6t26": 29222.0,
    "ppop_9t26": 49620.0, "prov_9t26": 9180.0,
    "toi_9t26": 72983.0, "nii_9t26": 57179.0, "opex_9t26": 23363.0,
    "loans_9t26": 1820000.0,
    "npl_9t26": 12818.0, "prov_stock": 31100.0,
    "npl_fy25_parts": (761.0, 199.0, 8686.0), "npl_fy25_reported": 9464.0,
    "pbt_fy25": 44020.0, "ppop_fy25": 47205.0, "prov_fy25": 3185.0,
    "one_off_q2": 2905.0, "pbt_q2": 17419.0, "ppop_q3": 17402.0,
    "prov_q3": 6184.0, "npl_q2": 10737.0, "cover_q2": 2.79,
    "cap_bonus": 10687.0, "cap_now": 83557.0, "cap_private": 5431.0,
    "state_share": 0.748,
    "prov_stock_start": 25000.0, "pbt_q4_floor_prov_mult": 2.0,
}


def vcb_metrics(d=VCB):
    return {
        "pbt_growth_9t": d["pbt_9t26"] / d["pbt_9t25"] - 1,
        "pbt_check_9t": d["ppop_9t26"] - d["prov_9t26"],
        "pbt_check_fy25": d["ppop_fy25"] - d["prov_fy25"],
        "pbt_6t_plus_q3": d["pbt_6t26"] + d["pbt_q3_26"],
        "cir_9t": d["opex_9t26"] / d["toi_9t26"],
        "nii_share": d["nii_9t26"] / d["toi_9t26"],
        "nonint_9t": d["toi_9t26"] - d["nii_9t26"],
        "npl_ratio_simple": d["npl_9t26"] / d["loans_9t26"],
        "coverage_simple": d["prov_stock"] / d["npl_9t26"],
        "fy25_npl_sum": sum(d["npl_fy25_parts"]),
        "fy25_npl_gap": sum(d["npl_fy25_parts"]) - d["npl_fy25_reported"],
        "credit_cost_annualised": d["prov_9t26"] / d["loans_9t26"] * 12 / 9,
        "room_left_pp": 13.0 - 9.0,
        "pbt_9t_ex_one_off": d["pbt_9t26"] - d["one_off_q2"],
        "pbt_growth_ex_one_off": (d["pbt_9t26"] - d["one_off_q2"]) / d["pbt_9t25"] - 1,
        "pbt_h1_ex_one_off": d["pbt_6t26"] - d["one_off_q2"],
        "pbt_q2_ex_one_off": d["pbt_q2"] - d["one_off_q2"],
        "q3_vs_q2_ex_one_off": d["pbt_q3_26"] / (d["pbt_q2"] - d["one_off_q2"]) - 1,
        "credit_cost_q3_run_rate": d["prov_q3"] * 4 / d["loans_9t26"],
        "fy26_base_vs_fy25": (d["pbt_9t26"] + d["pbt_q3_26"]) / d["pbt_fy25"] - 1,
        "prov_stock_q2_from_cover": d["cover_q2"] * d["npl_q2"],
        "prov_stock_change_h1_from_cover": d["cover_q2"] * d["npl_q2"] - d["prov_stock_start"],
        "prov_charge_h1": d["prov_9t26"] - d["prov_q3"],
        "implied_use_9t": d["prov_9t26"] - (d["prov_stock"] - d["prov_stock_start"]),
        "prov_stock_change_q3": d["prov_stock"] - d["cover_q2"] * d["npl_q2"],
        "implied_use_q3": d["prov_q3"] - (d["prov_stock"] - d["cover_q2"] * d["npl_q2"]),
        "bonus_pct": d["cap_bonus"] / d["cap_now"],
        "capital_growth_all": (d["cap_now"] + d["cap_bonus"] + d["cap_private"]) / d["cap_now"] - 1,
        "state_after_private": d["state_share"] / 1.065,
    }


def vcb_scenarios(d=VCB):
    """LNTT hợp nhất cả năm 2026 = 9T + Q4 giả định theo Q3 hoặc nửa đầu năm."""
    h1_avg_ex = (d["pbt_6t26"] - d["one_off_q2"]) / 2
    very = 0.90 * d["ppop_q3"] - d["pbt_q4_floor_prov_mult"] * d["prov_q3"]
    stress = 0.90 * d["ppop_q3"] - (d["prov_q3"] + vcb_coverage_stress(0.01, d)["extra_for_200"])
    q4 = {
        "rat_cang": very,
        "cang": stress,
        "bat_loi": 0.80 * d["pbt_q3_26"],
        "co_so": d["pbt_q3_26"],
        "thuan_loi": h1_avg_ex,
    }
    return {k: d["pbt_9t26"] + v for k, v in q4.items()}


def vcb_coverage_stress(npl_ratio, d=VCB):
    """Bao phủ nếu nợ xấu đạt npl_ratio trên dư nợ; dư nợ lấy theo số cuối kỳ."""
    npl = npl_ratio * d["loans_9t26"]
    return {
        "npl": npl,
        "coverage": d["prov_stock"] / npl,
        "extra_for_200": max(0.0, 2.0 * npl - d["prov_stock"]),
    }


VCB_R3 = {
    "pbt_fy25": 44020.0, "pbt_9t25": 33133.0,
    "plan_growth_low": 0.05, "plan_growth_high": 0.10,
    "mbs_pbt_q3": 14567.0, "mbs_prov_q3": 687.0,
    "g3_start": 761.0, "g4_start": 302.0, "g5_start": 8651.0,
    "g3_q3": 2571.0, "g4_q3": 1657.0, "g5_q3": 8589.0,
    "loans_q2": 1760000.0, "loans_q3": 1820000.0,
    "mgmt_nii_q3": 20386.0, "mgmt_nii_q2": 19142.0,
}


def vcb_round3(d=VCB, r=VCB_R3):
    q4_25 = r["pbt_fy25"] - r["pbt_9t25"]
    q4 = {
        "rat_cang": 0.90 * d["ppop_q3"] - 2 * d["prov_q3"],
        "cang_bao_phu": 0.90 * d["ppop_q3"] - (d["prov_q3"] + 5300.0),
        "bat_loi": 0.80 * d["pbt_q3_26"],
        "co_so": d["pbt_q3_26"],
        "thuan_loi": (d["pbt_6t26"] - d["one_off_q2"]) / 2,
    }
    plan_lo = r["pbt_fy25"] * (1 + r["plan_growth_low"])
    plan_hi = r["pbt_fy25"] * (1 + r["plan_growth_high"])
    start = r["g3_start"] + r["g4_start"] + r["g5_start"]
    now = r["g3_q3"] + r["g4_q3"] + r["g5_q3"]
    return {
        "q4_25": q4_25,
        "q4": q4,
        "q4_vs_q4_25": {k: v / q4_25 - 1 for k, v in q4.items()},
        "fy": {k: d["pbt_9t26"] + v for k, v in q4.items()},
        "run_rate": 4 * d["pbt_q3_26"],
        "plan_lo": plan_lo, "plan_hi": plan_hi,
        "q4_implied_plan_lo": plan_lo - d["pbt_9t26"],
        "q4_implied_plan_hi": plan_hi - d["pbt_9t26"],
        "base_vs_plan_lo": (d["pbt_9t26"] + d["pbt_q3_26"]) / plan_lo - 1,
        "bad_vs_plan_lo": (d["pbt_9t26"] + q4["bat_loi"]) / plan_lo - 1,
        "very_tight_vs_plan_lo": (d["pbt_9t26"] + q4["rat_cang"]) / plan_lo - 1,
        "implied_prov_thuan_loi": d["ppop_q3"] - q4["thuan_loi"],
        "implied_prov_bat_loi": d["ppop_q3"] - q4["bat_loi"],
        "pbt_if_prov_500": d["pbt_9t26"] + d["ppop_q3"] - 500.0,
        "mbs_pbt_miss": d["pbt_q3_26"] / r["mbs_pbt_q3"] - 1,
        "mbs_prov_ratio": d["prov_q3"] / r["mbs_prov_q3"],
        "npl_start_groups": start, "npl_q3_groups": now,
        "npl_start_growth": now / start - 1,
        "g34_start": r["g3_start"] + r["g4_start"], "g34_q3": r["g3_q3"] + r["g4_q3"],
        "g34_ratio": (r["g3_q3"] + r["g4_q3"]) / (r["g3_start"] + r["g4_start"]),
        "g5_share_q3": r["g5_q3"] / now,
        "loans_q3_vs_q2": r["loans_q3"] / r["loans_q2"] - 1,
        "prov_share_ppop_q3": d["prov_q3"] / d["ppop_q3"],
        "nonint_components": 2707.0 + 6408.0 + 5919.0,
        "nonint_gap": d["toi_9t26"] - d["nii_9t26"] - (2707.0 + 6408.0 + 5919.0),
        "prov_9m_share_q3": d["prov_q3"] / d["prov_9t26"],
    }


def vcb_round4(d=VCB, r=VCB_R3):
    """Sửa chiều tốc độ chạy năm; dự phòng trái phiếu; nhóm 2; kịch bản trừ ngoại hối; độ nhạy Công văn 9608 (minh họa)."""
    run_rate = 4 * d["pbt_q3_26"]
    bond_start, bond_now = 3307.0, 6304.0
    loan_prov_up = d["prov_stock"] - d["prov_stock_start"]
    fx_6t = 6408.0 - 2576.0
    fx_excess = 2576.0 - fx_6t / 2
    sme_loans = 0.56 * d["loans_9t26"]
    term_deposits = 0.68 * 1780000.0
    lend_cut_lo, lend_cut_hi = 0.015 * sme_loans, 0.02 * sme_loans
    dep_gain = 0.005 * term_deposits
    return {
        "run_rate": run_rate,
        "run_rate_vs_fy25": run_rate / r["pbt_fy25"] - 1,
        "base_cum_vs_run_rate": (d["pbt_9t26"] + d["pbt_q3_26"]) / run_rate - 1,
        "bond_prov_up": bond_now - bond_start,
        "bond_prov_growth": bond_now / bond_start - 1,
        "loan_prov_up": loan_prov_up,
        "prov_sum_vs_expense": loan_prov_up + (bond_now - bond_start),
        "prov_gap": d["prov_9t26"] - (loan_prov_up + (bond_now - bond_start)),
        "bond_share_of_expense": (bond_now - bond_start) / d["prov_9t26"],
        "g2_q3_vs_q2": 4995.0 / 4452.0 - 1,
        "g2_q3_ratio_loans": 4995.0 / d["loans_9t26"],
        "loans_over_deposits": d["loans_9t26"] / 1780000.0,
        "fx_6t_avg_q": fx_6t / 2, "fx_excess_q3": fx_excess,
        "pbt_q4_ex_fx": d["pbt_q3_26"] - fx_excess,
        "fy_ex_fx": d["pbt_9t26"] + d["pbt_q3_26"] - fx_excess,
        "sme_loans": sme_loans,
        "policy_lend_cut_q": (lend_cut_lo / 4, lend_cut_hi / 4),
        "policy_dep_gain_q": dep_gain / 4,
        "policy_net_q": ((dep_gain - lend_cut_lo) / 4, (dep_gain - lend_cut_hi) / 4),
        "coverage_q3_vs_fy25": (243.0, 257.0),
    }


# ---- HPG (BCTC kiểm toán FY2025; Tổng quan Q3/2026 của công ty, chưa kiểm toán)
HPG_YEARS = {
    # năm: (doanh thu thuần, lợi nhuận gộp, LNST công ty mẹ)
    2021: (149680.0, 41108.0, 34478.0),
    2022: (141409.0, 16763.0, 8484.0),
    2023: (118953.0, 12938.0, 6835.0),
    2024: (138855.1, 18497.5, 12021.4),
    2025: (156116.1, 24497.8, 15453.2),
}
HPG = {
    "rev_9t26": 171539.0, "gp_9t26": 30775.0, "rev_q3": 62669.0,
    "gp_q3": 11922.0, "rev_q3_25": 36794.0,
    "np_total_9t26": 23746.0, "interest_q3": 1774.0, "interest_fy25": 3114.9,
    "ebitda_fy25": 28232.0,
    "debt_fy25": 64695.0 + 27479.0, "debt_q3": 105737.0,
    "equity_fy25": 131220.0, "equity_q3": 149568.0,
    "cash_fy25": 8300.9, "dep_st_fy25": 19484.4,
    "shares_m": 8442.96452, "price": 21000.0,
    "capital_2023": 58147.9, "capital_mid26": 84430.0,
    "cfo_fy25": 17365.9, "capex_fy25": 25748.3,
    "cfo_fy24": 6608.3, "capex_fy24": 35495.0,
    "np_total_fy24": 12020.0, "np_total_fy25": 15514.9,
    "interest_q3_25": 812.0, "one_off_q1": 4915.0, "gp_margin_2023": 12938.0 / 118953.0,
    "minh_bought": 33.3, "minh_registered": 50.0,
}


def hpg_metrics(years=HPG_YEARS, d=HPG):
    gm = {y: v[1] / v[0] for y, v in years.items()}
    ys = sorted(years)
    all5 = ys
    last4 = ys[1:]

    def pooled(sel):
        return sum(years[y][1] for y in sel) / sum(years[y][0] for y in sel)

    def avg_np(sel):
        return sum(years[y][2] for y in sel) / len(sel)

    mcap = d["shares_m"] * d["price"] / 1000
    return {
        "gm": gm,
        "gm_9t26": d["gp_9t26"] / d["rev_9t26"],
        "gm_q3": d["gp_q3"] / d["rev_q3"],
        "rev_q3_growth": d["rev_q3"] / d["rev_q3_25"] - 1,
        "gm_simple_avg_5": sum(gm.values()) / 5,
        "gm_pooled_5": pooled(all5),
        "gm_pooled_4": pooled(last4),
        "np_avg_5": avg_np(all5),
        "np_avg_4": avg_np(last4),
        "np_margin_5": sum(v[2] for v in years.values())
        / sum(v[0] for v in years.values()),
        "mcap": mcap,
        "pe_on_avg5": mcap / avg_np(all5),
        "pe_on_avg4": mcap / avg_np(last4),
        "debt_to_equity_fy25": d["debt_fy25"] / d["equity_fy25"],
        "debt_to_equity_q3": d["debt_q3"] / d["equity_q3"],
        "net_debt_fy25_cash_only": d["debt_fy25"] - d["cash_fy25"],
        "net_debt_fy25_with_dep": d["debt_fy25"] - d["cash_fy25"] - d["dep_st_fy25"],
        "interest_cover_fy25": d["ebitda_fy25"] / d["interest_fy25"],
        "interest_q3_annualised": d["interest_q3"] * 4,
        "share_growth": d["capital_mid26"] / d["capital_2023"],
        "cfo_over_np_fy24": d["cfo_fy24"] / d["np_total_fy24"],
        "cfo_over_np_fy25": d["cfo_fy25"] / d["np_total_fy25"],
        "fcf_fy24": d["cfo_fy24"] - d["capex_fy24"],
        "fcf_fy25": d["cfo_fy25"] - d["capex_fy25"],
        "interest_q3_yoy": d["interest_q3"] / d["interest_q3_25"],
        "one_off_share_np": d["one_off_q1"] / d["np_total_9t26"],
        "minh_bought_share": d["minh_bought"] / d["minh_registered"],
        "assets_growth": 283450.0 / 178236.0 - 1,
    }


def hpg_scenarios(d=HPG):
    """Lợi nhuận gộp cả năm 2026 = 9 tháng đã thực hiện + Q4 giả định.

    Q4: doanh thu = hệ số x doanh thu Q3; biên gộp giả định; lãi vay Q4 = hệ số x lãi vay Q3.
    Chưa trừ chi phí bán hàng, quản lý, khấu hao ngoài giá vốn và thuế (CHƯA_BIẾT).
    """
    out = {}
    for name, rev_k, margin, int_k in (
        ("chu_ky_xau", None, 0.08, 1.15),
        ("cuc_doan", 0.80, d["gp_margin_2023"], 1.15),
        ("bat_loi", 1.00, 0.13, 1.15),
        ("co_so", 1.00, d["gp_9t26"] / d["rev_9t26"], 1.00),
        ("thuan_loi", 1.00, d["gp_q3"] / d["rev_q3"], 1.00),
    ):
        rev_q4 = d["rev_q3_25"] if rev_k is None else rev_k * d["rev_q3"]
        gp_q4 = rev_q4 * margin
        interest_q4 = int_k * d["interest_q3"]
        out[name] = {
            "rev_q4": rev_q4, "margin": margin, "gp_q4": gp_q4,
            "gp_fy": d["gp_9t26"] + gp_q4,
            "interest_q4": interest_q4,
            "gp_over_interest_q4": gp_q4 / interest_q4,
        }
    return out


def hpg_interest_sensitivity(d=HPG):
    """Gộp Q4 / lãi vay Q4 khi lãi vay Q4 tăng 15%, 30%, 50% so với Q3; kịch bản bất lợi và cơ sở."""
    s = hpg_scenarios(d)
    out = {}
    for up in (0.15, 0.30, 0.50):
        interest = d["interest_q3"] * (1 + up)
        out[up] = {k: s[k]["gp_q4"] / interest for k in ("bat_loi", "co_so")}
        out[up]["interest"] = interest
    return out


def hpg_price_adjust(d=HPG):
    """Giá 27.600 (06/05, trước thưởng 10%) điều chỉnh theo hệ số 1,1 rồi so với 21.000 (30/10)."""
    adj = 27600.0 / 1.1
    return {"adj": adj, "change_adj": d["price"] / adj - 1,
            "change_raw": d["price"] / 27600.0 - 1}


HPG_R3 = {
    "sell_q2": 1718.0, "rev_q2": 55159.0, "rev_q4_25": 47302.0,
    "deductions_q3": 455.0, "deductions_9t": 1265.0, "deductions_q3_25": 387.0,
    "inv_q1": 43500.0, "inv_q2": 55608.0, "inv_fy25": 52828.0,
    "np_q1": 9056.0, "np_6t": 15480.0, "np_q3": 8265.0,
    "np_q1_ex": 5200.0, "forecast_vdsc": 5369.0,
    "debt_q1": 90600.0, "interest_q1": 1333.0, "interest_q2": 1520.0,
    "interest_q3": 1774.0,
}


def hpg_round3(d=HPG, r=HPG_R3):
    """Chỉ báo gộp trừ chi phí bán hàng so với lãi vay, so Q4 với Q4/2025, quy năm, đối chiếu doanh thu gộp."""
    s = hpg_scenarios(d)
    out = {}
    for name, v in s.items():
        sell = r["sell_q2"] * v["rev_q4"] / r["rev_q2"]
        interest = v["interest_q4"]
        out[name] = {
            "sell_est": sell,
            "gp_less_sell": v["gp_q4"] - sell,
            "gp_less_sell_less_interest": v["gp_q4"] - sell - interest,
            "rev_vs_q4_25": v["rev_q4"] / r["rev_q4_25"] - 1,
            "gp_run_rate": 4 * v["gp_q4"],
        }
    q2_np = r["np_6t"] - r["np_q1"]
    return {
        "scenarios": out,
        "run_rate_gp_q3": 4 * d["gp_q3"],
        "q2_np": q2_np, "q3_vs_q2_np": r["np_q3"] / q2_np - 1,
        "q3_np_vs_vdsc": r["np_q3"] / r["forecast_vdsc"],
        "np_q1_ex_share": (r["np_q1"] - r["np_q1_ex"]) / d["np_total_9t26"],
        "q3_rev_net_est": d["rev_q3"] - r["deductions_q3"],
        "q3_margin_net": d["gp_q3"] / (d["rev_q3"] - r["deductions_q3"]),
        "q3_margin_gross": d["gp_q3"] / d["rev_q3"],
        "margin_gap_q3": d["gp_q3"] / (d["rev_q3"] - r["deductions_q3"]) - d["gp_q3"] / d["rev_q3"],
        "margin_net_9t": d["gp_9t26"] / (d["rev_9t26"] - r["deductions_9t"]),
        "margin_gap_9t": d["gp_9t26"] / (d["rev_9t26"] - r["deductions_9t"]) - d["gp_9t26"] / d["rev_9t26"],
        "inv_q2_vs_fy25": r["inv_q2"] / r["inv_fy25"] - 1,
        "inv_q2_vs_q1": r["inv_q2"] / r["inv_q1"] - 1,
        "interest_q3_vs_q2": r["interest_q3"] / r["interest_q2"] - 1,
        "interest_q3_vs_q2_abs": r["interest_q3"] - r["interest_q2"],
        "interest_chain": (r["interest_q1"], r["interest_q2"], r["interest_q3"]),
        "debt_q3_vs_q1": d["debt_q3"] - r["debt_q1"],
    }


def hpg_round4(d=HPG, r=HPG_R3):
    """Chi phí bán hàng cứng, tiền lệ Q4/2022 (ABS), doanh thu cùng cơ sở, cơ cấu kỳ hạn nợ một năm trước."""
    s = hpg_scenarios(d)
    sell_hard = r["sell_q2"]
    out = {}
    for name in ("chu_ky_xau", "cuc_doan"):
        v = s[name]
        out[name] = {"after_sell_hard": v["gp_q4"] - sell_hard,
                     "after_sell_hard_interest": v["gp_q4"] - sell_hard - v["interest_q4"]}
    interest_q4 = s["chu_ky_xau"]["interest_q4"]
    q4_22 = {"rev": 25826.0, "gp": -885.0, "sell": 716.0, "sell_q4_21": 711.0,
             "interest": 933.0, "np": -1992.0}
    return {
        "hard_sell": out,
        "replay_q4_22_pre_tax": 0.0 - sell_hard - interest_q4,
        "q4_22_margin": q4_22["gp"] / q4_22["rev"],
        "interest_ratio_vs_q4_22": interest_q4 / q4_22["interest"],
        "sell_change_q4_22": q4_22["sell"] / q4_22["sell_q4_21"] - 1,
        "rev_q3_vs_q2_same_basis": d["rev_q3"] / 55557.0 - 1,
        "rev_q3_vs_q2_net": (d["rev_q3"] - r["deductions_q3"]) / 55159.0 - 1,
        "h1_deductions": r["deductions_9t"] - r["deductions_q3"],
        "short_share_q3_25": 28356.0 / 96838.0,
        "short_share_q3_26": 78615.0 / d["debt_q3"],
        "sell_share_q2": r["sell_q2"] / 55159.0,
    }


def main():
    import json
    for name, fn in (("FPT", fpt_metrics), ("VNM", vnm_metrics),
                     ("VCB", vcb_metrics), ("HPG", hpg_metrics)):
        print(name, json.dumps(fn(), indent=1, ensure_ascii=False))
    print("FPT kịch bản", fpt_scenarios())
    print("VNM kịch bản", vnm_scenarios())
    print("VCB kịch bản", vcb_scenarios())
    print("HPG kịch bản", hpg_scenarios())
    for r in (0.0071, 0.01, 0.015):
        print("VCB stress", r, vcb_coverage_stress(r))


if __name__ == "__main__":
    main()


def hpg_liquidity_round5():
    """S48 BCTC Q3/2026 PDF 2/4/7, đầu vào VND gốc, đổi ra tỷ VND."""
    cash = 6_852_876_731_299 / 1e9
    term = 39_273_855_125_563 / 1e9
    short = 78_615_048_528_530 / 1e9
    long = 27_121_713_203_040 / 1e9
    cfo = 20_936_329_304_403 / 1e9
    capex = 14_607_166_041_086 / 1e9
    return {"net_debt_cash_only": short + long - cash,
            "net_debt_including_term": short + long - cash - term,
            "liquid_over_short": (cash + term) / short,
            "fcf_simple": cfo - capex}


def vcb_provisions_round5():
    """S33 thuyết minh 5–7, đơn vị gốc TRIỆU VND. Không suy chi phí trái phiếu từ số dư."""
    opening, general_charge, specific_charge, fx = 24_980_391, 1_002_848, 5_186_666, -1_798
    closing = opening + general_charge + specific_charge + fx
    npl = 2_571_437 + 1_657_212 + 8_588_936
    old_npl = 761_291 + 301_991 + 8_650_658
    return {"closing_vnd_million": closing, "npl_vnd_million": npl,
            "opening_npl_vnd_million": old_npl,
            "coverage": closing / npl, "npl_ratio": npl / 1_816_093_286,
            "group34_ratio": (2_571_437 + 1_657_212) / (761_291 + 301_991)}


def ftel_growth_round6():
    """S27 BCTC FTEL PDF6/mã60 và10: VND, cùng kỳ và phạm vi hợp nhất."""
    return {"np_9t_growth": 2_933_945_150_076 / 2_580_935_694_440 - 1,
            "np_q3_growth": 1_022_467_701_403 / 904_823_140_859 - 1,
            "rev_9t_growth": 16_690_579_638_134 / 14_286_916_907_543 - 1}
