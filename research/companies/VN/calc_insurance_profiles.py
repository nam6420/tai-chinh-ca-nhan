"""Mô-đun tính toán tái lập cho Báo cáo ngành Bảo hiểm Việt Nam và 3 hồ sơ BVH, PVI, BIC.

Toàn bộ đầu vào được lấy trực tiếp từ BCTC hợp nhất năm 2025 đã kiểm toán/công bố
của Tập đoàn Bảo Việt (BVH), CTCP PVI (PVI) và Tổng Công ty Bảo hiểm BIDV (BIC),
đơn vị mặc định: tỷ VND (làm tròn từ VND gốc trên báo cáo).
"""

from __future__ import annotations


def bvh_metrics() -> dict[str, float]:
    """Chỉ số tài chính, nghiệp vụ, đầu tư và vốn của Tập đoàn Bảo Việt (BVH) FY2024-FY2025."""
    # Bảng cân đối kế toán hợp nhất (tỷ VND)
    assets_25 = 291_805.652090226
    assets_24 = 251_286.326838124
    fin_inv_25 = 266_535.565330803
    fin_inv_24 = 231_543.462200166
    repo_25 = 53_229.070825336
    repo_24 = 32_123.608859706
    gross_res_25 = 201_682.485499473
    gross_res_24 = 186_574.100476584
    math_res_25 = 171_409.330097570
    math_res_24 = 157_148.585024401
    min_rate_res_25 = 16_544.350410061
    min_rate_res_24 = 16_741.736693139
    reins_assets_25 = 3_682.410198617
    reins_assets_24 = 3_558.134396677
    equity_total_25 = 25_480.341454325
    equity_total_24 = 23_565.887059923
    nci_25 = 1_029.169530652
    nci_24 = 974.335175004
    equity_parent_25 = equity_total_25 - nci_25
    equity_parent_24 = equity_total_24 - nci_24
    shares_m = 742.322764

    # Kết quả kinh doanh hợp nhất (tỷ VND)
    gwp_25 = 43_716.183432964
    gwp_24 = 42_591.775979851
    gwp_life_25 = 32_641.787248143
    gwp_ul_25 = 27_229.205419410
    gwp_pnt_25 = 11_074.396184821
    inward_25 = 399.971247626
    ceded_25 = 3_808.522584311
    nwp_25 = gwp_25 + inward_25 - ceded_25
    nep_25 = 40_123.665483765
    nep_24 = 39_126.183679044
    ceded_comm_other_25 = 824.585918049
    ceded_comm_25 = 776.403692982
    net_claims_and_benefits_25 = 35_137.291230156
    cat_res_change_25 = -14.015820679
    direct_uw_other_25 = 4_587.029663396
    total_direct_uw_cost_25 = 39_710.305072873
    uw_gross_profit_25 = 1_237.946328941
    uw_gross_profit_24 = -969.112867855
    fin_inc_25 = 14_039.756364318
    fin_exp_25 = 2_919.290603309
    net_fin_25 = fin_inc_25 - fin_exp_25
    net_fin_24 = 10_573.595705785
    sell_exp_25 = 1_674.852380539
    ga_exp_25 = 7_213.126135849
    ebt_25 = 3_554.431272129
    ebt_24 = 2_663.171477296
    npat_25 = 2_921.571759353
    npat_24 = 2_194.168603330
    npat_parent_25 = 2_836.613711079
    npat_parent_24 = 2_110.496926600

    # Biên khả năng thanh toán (TM 40 tr. 84)
    solvency_pnt_25 = 2_692.491 / 1_916.391
    solvency_life_25 = 9_921.645 / 9_269.953

    return {
        "assets_growth": assets_25 / assets_24 - 1.0,
        "fin_inv_share": fin_inv_25 / assets_25,
        "repo_growth": repo_25 / repo_24 - 1.0,
        "net_reserves_25": gross_res_25 - reins_assets_25,
        "ul_share_of_life_gwp": gwp_ul_25 / gwp_life_25,
        "nwp_25": nwp_25,
        "retention_25": nwp_25 / (gwp_25 + inward_25),
        "uw_gross_profit_25": uw_gross_profit_25,
        "uw_swing_25_vs_24": uw_gross_profit_25 - uw_gross_profit_24,
        "net_fin_25": net_fin_25,
        "fin_yield_avg": net_fin_25 / ((fin_inv_25 + fin_inv_24) / 2.0),
        "ebt_growth": ebt_25 / ebt_24 - 1.0,
        "npat_growth": npat_25 / npat_24 - 1.0,
        "eps_25": npat_parent_25 * 1_000.0 / shares_m,
        "bvps_parent_25": equity_parent_25 * 1_000.0 / shares_m,
        "roe_parent_avg": npat_parent_25 / ((equity_parent_25 + equity_parent_24) / 2.0),
        "roe_total_avg": npat_25 / ((equity_total_25 + equity_total_24) / 2.0),
        "solvency_pnt_25": solvency_pnt_25,
        "solvency_life_25": solvency_life_25,
    }


def bvh_scenarios() -> dict[str, dict[str, float]]:
    """Ba kịch bản định giá BVH bằng Justified P/B và Residual Income (tỷ VND, VND/CP)."""
    b0_parent = 24_451.171923673
    shares_m = 742.322764
    bvps_0 = b0_parent * 1_000.0 / shares_m  # 32.938,73 VND/CP
    scenarios = {
        # Bất lợi: lợi suất TPCP giảm kéo cần trích bổ sung dự phòng lãi cam kết tối thiểu, ROE = 9,0%, ke = 11,5%, g = 4,5%
        "bat_loi": {"roe": 0.090, "ke": 0.115, "g": 0.045},
        # Cơ sở: ROE duy trì mức 2025 ~ 11,8%, ke = 11,0%, g = 5,5%
        "co_so": {"roe": 0.118, "ke": 0.110, "g": 0.055},
        # Thuận lợi: Lãi suất TPCP tăng + cải thiện biên khai thác nhân thọ/PNT, ROE = 13,5%, ke = 10,5%, g = 6,0%
        "thuan_loi": {"roe": 0.135, "ke": 0.105, "g": 0.060},
    }
    out: dict[str, dict[str, float]] = {}
    for name, p in scenarios.items():
        pb = (p["roe"] - p["g"]) / (p["ke"] - p["g"])
        val_total = b0_parent * pb
        val_per_share = bvps_0 * pb
        out[name] = {
            "pb_justified": pb,
            "equity_value_bn": val_total,
            "value_per_share_vnd": val_per_share,
        }
    return out


def pvi_metrics() -> dict[str, float]:
    """Chỉ số tài chính, nghiệp vụ, tái bảo hiểm và vốn của CTCP PVI (PVI) FY2024-FY2025."""
    assets_25 = 44_512.136899824
    assets_24 = 31_795.022876106
    fin_inv_25 = 13_358.502923548 + 3_349.046150694
    fin_inv_24 = 9_641.947935060 + 4_687.830111772
    reins_upr_25 = 6_245.604522024
    reins_claim_25 = 15_368.842738541
    reins_assets_25 = reins_upr_25 + reins_claim_25
    reins_assets_24 = 4_886.445006868 + 7_518.471328958
    gross_res_25 = 28_417.498546546
    gross_res_24 = 17_800.976238385
    equity_total_25 = 8_533.908332139
    equity_total_24 = 8_194.456217798
    nci_25 = 349.927852384
    nci_24 = 359.589076910
    equity_parent_25 = equity_total_25 - nci_25
    equity_parent_24 = equity_total_24 - nci_24
    shares_m = 234.241867

    # Cầu nối doanh thu phí và chi phí bảo hiểm (TM 23 & 24, tr. 46-47, 2024 đã điều chỉnh lại theo TM 35)
    gwp_25 = 14_908.335137479
    gwp_24 = 13_356.110796094
    inward_25 = 10_498.980153611
    inward_24 = 7_024.477600720
    ceded_25 = 17_178.017991636
    ceded_24 = 13_050.808415211
    nwp_25 = gwp_25 + inward_25 - ceded_25
    nwp_24 = gwp_24 + inward_24 - ceded_24
    delta_upr_net_25 = 595.397410298
    nep_25 = nwp_25 - delta_upr_net_25
    nep_24 = nwp_24 - 359.784049956
    ceded_comm_25 = 1_337.612501180
    other_ins_inc_25 = 369.795011826

    # Chi bồi thường giữ lại (TM 24, tr. 47)
    net_claims_25 = (
        4_380.074199611
        + 2_374.525678818
        - 4_277.171676079
        + 694.654359552
        + 114.543331025
    )
    other_ins_exp_25 = 4_810.002863360
    ga_exp_25 = 836.355070297

    loss_ratio_25 = net_claims_25 / nep_25
    expense_ratio_pre_comm_25 = (other_ins_exp_25 + ga_exp_25) / nep_25
    expense_ratio_post_comm_25 = (other_ins_exp_25 + ga_exp_25 - ceded_comm_25) / nep_25
    cr_pre_comm_25 = loss_ratio_25 + expense_ratio_pre_comm_25
    cr_post_comm_25 = loss_ratio_25 + expense_ratio_post_comm_25

    fin_inc_25 = 1_411.374681687
    fin_exp_25 = 493.162853723
    net_fin_25 = fin_inc_25 - fin_exp_25
    ebt_25 = 1_459.668566871
    ebt_24 = 1_118.423965239
    npat_25 = 1_152.106947333
    npat_24 = 881.751011899
    npat_parent_25 = 1_102.927654733
    npat_parent_24 = 844.864161439

    return {
        "assets_growth": assets_25 / assets_24 - 1.0,
        "reins_assets_25": reins_assets_25,
        "reins_assets_to_equity": reins_assets_25 / equity_total_25,
        "net_reserves_25": gross_res_25 - reins_assets_25,
        "gwp_growth": gwp_25 / gwp_24 - 1.0,
        "inward_growth": inward_25 / inward_24 - 1.0,
        "nwp_25": nwp_25,
        "retention_25": nwp_25 / (gwp_25 + inward_25),
        "retention_24": nwp_24 / (gwp_24 + inward_24),
        "nep_25": nep_25,
        "net_claims_25": net_claims_25,
        "loss_ratio_25": loss_ratio_25,
        "cr_pre_comm_25": cr_pre_comm_25,
        "cr_post_comm_25": cr_post_comm_25,
        "net_fin_25": net_fin_25,
        "ebt_growth": ebt_25 / ebt_24 - 1.0,
        "npat_growth": npat_25 / npat_24 - 1.0,
        "bvps_parent_25": equity_parent_25 * 1_000.0 / shares_m,
        "roe_parent_avg": npat_parent_25 / ((equity_parent_25 + equity_parent_24) / 2.0),
    }


def pvi_scenarios() -> dict[str, dict[str, float]]:
    """Ba kịch bản định giá PVI bằng Justified P/B (tỷ VND, VND/CP)."""
    b0_parent = 8_183.980479755
    shares_m = 234.241867
    bvps_0 = b0_parent * 1_000.0 / shares_m  # 34.938,16 VND/CP
    scenarios = {
        # Bất lợi: Chu kỳ phí tái BH hạ nhiệt + trích lập dự phòng phải thu tái BH, ROE = 11,0%, ke = 11,5%, g = 4,5%
        "bat_loi": {"roe": 0.110, "ke": 0.115, "g": 0.045},
        # Cơ sở: Duy trì ROE ~ 13,8% trên nền vốn mới 5.000 tỷ của PVI Insurance, ke = 11,0%, g = 5,5%
        "co_so": {"roe": 0.138, "ke": 0.110, "g": 0.055},
        # Thuận lợi: Tín nhiệm A- giúp mở rộng nhận tái quốc tế biên cao, ROE = 15,5%, ke = 10,5%, g = 6,0%
        "thuan_loi": {"roe": 0.155, "ke": 0.105, "g": 0.060},
    }
    out: dict[str, dict[str, float]] = {}
    for name, p in scenarios.items():
        pb = (p["roe"] - p["g"]) / (p["ke"] - p["g"])
        out[name] = {
            "pb_justified": pb,
            "equity_value_bn": b0_parent * pb,
            "value_per_share_vnd": bvps_0 * pb,
        }
    return out


def bic_metrics() -> dict[str, float]:
    """Chỉ số tài chính, nghiệp vụ, kênh bancassurance và vốn của Bảo hiểm BIDV (BIC) FY2024-FY2025 (đã kiểm toán)."""
    # Bảng cân đối kế toán hợp nhất đã kiểm toán (EY ký 20/03/2026, tr. 9-12, tỷ VND)
    assets_25 = 10_092.705915010
    assets_25_pre_audit = 10_079.690742995
    assets_24 = 8_682.527467741
    fin_inv_25 = 5_415.852251577 + 1_805.779366231  # 7.221,631617808 tỷ (TM 6 tr. 36)
    fin_inv_24 = 5_460.118531838 + 972.943307191
    reins_assets_25 = 1_628.703588611  # UPR nhượng tái 674,391 + bồi thường nhượng tái 954,313 (TM 22.1 tr. 48)
    reins_assets_24 = 1_241.247943271
    gross_res_25 = 4_454.523086185  # UPR 2.644,286 + Bồi thường 1.496,494 + Dao động lớn 313,742 (TM 22.1 tr. 48)
    gross_res_24 = 3_798.683632523
    equity_total_25 = 3_383.093966394
    equity_total_24 = 2_965.214390365
    nci_25 = 133.036304507
    nci_24 = 17.431287143
    equity_parent_25 = equity_total_25 - nci_25  # 3.250,057661887 tỷ
    equity_parent_24 = equity_total_24 - nci_24  # 2.947,783103222 tỷ
    shares_m_25 = 202.067057
    shares_m_24 = 117.276895

    # Kết quả kinh doanh hợp nhất đã kiểm toán (tr. 13-15, TM 24-35 tr. 53-59)
    gwp_25 = 5_702.421678651  # Phí gốc 5.751,263 - giảm trừ 48,842 (TM 24 tr. 53)
    gwp_25_pre_audit = 5_696.785755611
    gwp_24 = 5_439.634122416
    gwp_health_25 = 2_357.881583840
    gwp_fire_25 = 1_194.001951659
    gwp_motor_25 = 1_127.539078215
    inward_25 = 92.492770012
    ceded_25 = 1_762.165477998
    nwp_25 = gwp_25 + inward_25 - ceded_25  # 4.032,748970665 tỷ
    nep_25 = 3_948.008937786
    nep_24 = 3_988.870049873
    ceded_comm_other_25 = 338.296783966
    ceded_comm_25 = 272.249081783

    net_claims_25 = 1_149.578924827
    cat_res_25 = 40.347179706
    claims_and_cat_25 = net_claims_25 + cat_res_25  # 1.189,926104533 tỷ
    other_uw_exp_25 = 2_133.190684408  # Trước kiểm toán: 2.101,656175457 tỷ (tăng 31,535 tỷ sau kiểm toán)
    uw_gross_profit_25 = 963.188932811  # Trước kiểm toán: 994,936604120 tỷ
    uw_gross_profit_25_pre_audit = 994.936604120
    uw_gross_profit_24 = 1_190.802670751

    loss_ratio_25 = claims_and_cat_25 / nep_25
    expense_ratio_pre_comm_25 = other_uw_exp_25 / nep_25
    cr_pre_comm_25 = loss_ratio_25 + expense_ratio_pre_comm_25
    cr_post_comm_25 = (claims_and_cat_25 + other_uw_exp_25 - ceded_comm_other_25) / nep_25

    fin_inc_25 = 548.522716461
    fin_exp_25 = 37.245032248
    net_fin_25 = fin_inc_25 - fin_exp_25  # 511,277684213 tỷ
    net_fin_24 = 373.293260480
    ga_exp_25 = 800.171783224  # Trước kiểm toán: 831,077818740 tỷ
    ebt_25 = 678.929298650
    ebt_24 = 652.802918931
    npat_25 = 550.531191252  # Trước kiểm toán: 551,890904204 tỷ
    npat_25_pre_audit = 551.890904204
    npat_24 = 501.049500012
    npat_parent_25 = 542.667153567  # Trước kiểm toán: 544,057298219 tỷ
    npat_parent_24 = 495.808538191

    # Giao dịch bên liên quan với công ty mẹ BIDV (TM 36 tr. 61-62)
    bidv_term_deposit_25 = 4_428.500000000
    bidv_comm_paid_25 = 755.647270189
    bidv_interest_inc_25 = 217.619989365

    # Biên khả năng thanh toán (TM 40.3 tr. 70, triệu VND -> tỷ VND)
    solvency_25 = 2_706.433 / 950.711  # 284,67% (báo cáo ghi 285%)

    # Q4/2025 thiên tai bão lũ (từ BCTC Q4/2025 tr. 7-9, 22)
    uw_gp_q4_25 = 191.366129077
    uw_gp_q4_24 = 463.351491341
    npat_q4_25 = 124.677055774
    npat_q4_24 = 152.958904664

    return {
        "assets_growth": assets_25 / assets_24 - 1.0,
        "fin_inv_25": fin_inv_25,
        "fin_inv_share": fin_inv_25 / assets_25,
        "net_reserves_25": gross_res_25 - reins_assets_25,
        "charter_cap_growth": shares_m_25 / shares_m_24 - 1.0,
        "health_share_gwp": gwp_health_25 / gwp_25,
        "fire_share_gwp": gwp_fire_25 / gwp_25,
        "motor_share_gwp": gwp_motor_25 / gwp_25,
        "nwp_25": nwp_25,
        "retention_25": nwp_25 / (gwp_25 + inward_25),
        "loss_ratio_25": loss_ratio_25,
        "cr_pre_comm_25": cr_pre_comm_25,
        "cr_post_comm_25": cr_post_comm_25,
        "uw_gp_audit_delta": uw_gross_profit_25 - uw_gross_profit_25_pre_audit,
        "npat_audit_delta": npat_25 - npat_25_pre_audit,
        "bidv_deposit_share_htm": bidv_term_deposit_25 / 6_665.623099527,
        "bidv_comm_share_gwp": bidv_comm_paid_25 / gwp_25,
        "solvency_25": solvency_25,
        "uw_gp_drop_q4": uw_gp_q4_25 / uw_gp_q4_24 - 1.0,
        "npat_drop_q4": npat_q4_25 / npat_q4_24 - 1.0,
        "net_fin_growth": net_fin_25 / net_fin_24 - 1.0,
        "ebt_growth": ebt_25 / ebt_24 - 1.0,
        "npat_growth": npat_25 / npat_24 - 1.0,
        "bvps_parent_25": equity_parent_25 * 1_000.0 / shares_m_25,
        "roe_parent_avg": npat_parent_25 / ((equity_parent_25 + equity_parent_24) / 2.0),
    }


def bic_scenarios() -> dict[str, dict[str, float]]:
    """Ba kịch bản định giá BIC bằng Justified P/B (tỷ VND, VND/CP) trên vốn chủ công ty mẹ đã kiểm toán."""
    b0_parent = 3_250.057661887
    shares_m = 202.067057
    bvps_0 = b0_parent * 1_000.0 / shares_m  # 16.084,05 VND/CP
    scenarios = {
        # Bất lợi: Bão lũ lặp lại + siết hoa hồng bancassurance sức khỏe, ROE = 13,5%, ke = 11,5%, g = 4,5%
        "bat_loi": {"roe": 0.135, "ke": 0.115, "g": 0.045},
        # Cơ sở: Combined ratio giữ mức ~83-85%, ROE = 16,5%, ke = 11,0%, g = 5,5%
        "co_so": {"roe": 0.165, "ke": 0.110, "g": 0.055},
        # Thuận lợi: Bancassurance qua BIDV phục hồi + mở rộng LVI/CVI, ROE = 18,5%, ke = 10,5%, g = 6,0%
        "thuan_loi": {"roe": 0.185, "ke": 0.105, "g": 0.060},
    }
    out: dict[str, dict[str, float]] = {}
    for name, p in scenarios.items():
        pb = (p["roe"] - p["g"]) / (p["ke"] - p["g"])
        out[name] = {
            "pb_justified": pb,
            "equity_value_bn": b0_parent * pb,
            "value_per_share_vnd": bvps_0 * pb,
        }
    return out
