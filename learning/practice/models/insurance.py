"""Mô hình thực hành cho Ngân hàng, Bảo hiểm doanh nghiệp và Bảo hiểm cá nhân (bài 013, F8, P4).

Chỉ dùng thư viện chuẩn Python 3.
Đầu vào lịch sử lấy từ geico_berkshire_fy2025_inputs.csv (JPM FY2025 10-K, Berkshire/GEICO FY2025 10-K,
BCTC hợp nhất kiểm toán FY2025 của BVH và BCTC hợp nhất Q4/2025 của BIC) và ví dụ tam giác bồi thường
tại Điều 36 Văn bản hợp nhất số 44/2026/VBHN-TT-BTC (hợp nhất Thông tư 67/2023/TT-BTC và 96/2026/TT-BTC).
Mọi giả định tương lai là giả định bài học để kiểm tra độ nhạy, không phải dự báo hay khuyến nghị.

Chạy từ thư mục gốc: python3 learning/practice/models/insurance.py
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

HERE = Path(__file__).parent

# Bảng mẫu tam giác bồi thường thực trả từng năm 2016-2023 (triệu đồng)
# tại Điều 36 Khoản 2(a) Văn bản hợp nhất số 44/2026/VBHN-TT-BTC (tr. 42-45)
TT67_INCREMENTAL_TRIANGLE: list[list[float]] = [
    [5445, 3157, 2450, 1412, 600, 352, 431, 185],
    [5847, 3486, 1366, 848, 1045, 1054, 369],
    [5981, 4854, 1948, 2554, 1680, 489],
    [7835, 4453, 3888, 3335, 2088],
    [9763, 6517, 3563, 3984],
    [10745, 6184, 4549],
    [14137, 8116],
    [15162],
]


def _check_num(val: float, name: str, allow_negative: bool = True, allow_zero: bool = True) -> float:
    if val is None or isinstance(val, bool) or not isinstance(val, (int, float)):
        raise ValueError(f"{name} phải là số hữu hạn")
    if math.isnan(val) or math.isinf(val):
        raise ValueError(f"{name} không được là NaN hoặc vô cực")
    if not allow_negative and val < 0:
        raise ValueError(f"{name} không được âm ({val})")
    if not allow_zero and val == 0:
        raise ValueError(f"{name} phải khác 0")
    return float(val)


def load_historical_inputs() -> dict[tuple[str, str], dict[str, float | str]]:
    """Đọc tệp geico_berkshire_fy2025_inputs.csv thành từ điển theo khóa (đối_tượng, chỉ_tiêu)."""
    out: dict[tuple[str, str], dict[str, float | str]] = {}
    with open(HERE / "geico_berkshire_fy2025_inputs.csv", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            key = (row["doi_tuong"], row["chi_tieu"])
            out[key] = {
                "2025": float(row["nam_2025"]),
                "2024": float(row["nam_2024"]),
                "2023": float(row["nam_2023"]),
                "don_vi": row["don_vi"],
                "nguon": row["nguon"],
            }
    return out


# ==============================================================================
# 1. NGÂN HÀNG & CẦU NỐI DỰ PHÒNG (BÀI 013)
# ==============================================================================
def bank_operating_bridge(
    nii: float,
    noninterest_rev: float,
    noninterest_exp: float,
    provision: float,
    tax: float,
    earning_assets: float,
    total_loans: float,
    npl: float,
    allowance_for_loan_losses: float,
    common_equity: float,
    rwa: float | None = None,
    cet1_capital: float | None = None,
) -> dict[str, float | None]:
    """Cầu nối thu nhập, hiệu quả chi phí, chất lượng tài sản và đệm vốn ngân hàng."""
    _check_num(nii, "nii")
    _check_num(noninterest_rev, "noninterest_rev")
    _check_num(noninterest_exp, "noninterest_exp", allow_negative=False)
    _check_num(provision, "provision")
    _check_num(tax, "tax")
    _check_num(earning_assets, "earning_assets", allow_negative=False, allow_zero=False)
    _check_num(total_loans, "total_loans", allow_negative=False, allow_zero=False)
    _check_num(npl, "npl", allow_negative=False)
    _check_num(allowance_for_loan_losses, "allowance_for_loan_losses", allow_negative=False)
    _check_num(common_equity, "common_equity", allow_negative=False, allow_zero=False)

    total_rev = nii + noninterest_rev
    if total_rev <= 0:
        raise ValueError("Tổng thu nhập hoạt động phải dương để tính CIR")
    ppop = total_rev - noninterest_exp
    pbt = ppop - provision
    net_income = pbt - tax
    nim = nii / earning_assets
    cir = noninterest_exp / total_rev
    credit_cost_rate = provision / total_loans
    npl_ratio = npl / total_loans
    llr_coverage = (allowance_for_loan_losses / npl) if npl > 0 else None
    roe = net_income / common_equity
    cet1_ratio = None
    if rwa is not None and cet1_capital is not None:
        _check_num(rwa, "rwa", allow_negative=False, allow_zero=False)
        _check_num(cet1_capital, "cet1_capital", allow_negative=False)
        cet1_ratio = cet1_capital / rwa

    return {
        "total_revenue": total_rev,
        "ppop": ppop,
        "pbt": pbt,
        "net_income": net_income,
        "nim": nim,
        "cir": cir,
        "credit_cost_rate": credit_cost_rate,
        "npl_ratio": npl_ratio,
        "llr_coverage": llr_coverage,
        "roe": roe,
        "cet1_ratio": cet1_ratio,
    }


def reserve_understatement_adjustment(
    reported_net_income: float,
    reported_equity: float,
    reserve_shortfall_pretax: float,
    tax_rate: float = 0.20,
    market_cap: float | None = None,
) -> dict[str, float | None]:
    """Đánh giá tác động khi ngân hàng trích thiếu dự phòng tín dụng hoặc hãng bảo hiểm
    trích thiếu dự phòng nghiệp vụ một lượng `reserve_shortfall_pretax` trước thuế.
    """
    _check_num(reported_net_income, "reported_net_income")
    _check_num(reported_equity, "reported_equity", allow_negative=False, allow_zero=False)
    _check_num(reserve_shortfall_pretax, "reserve_shortfall_pretax", allow_negative=False)
    _check_num(tax_rate, "tax_rate", allow_negative=False)
    if tax_rate >= 1:
        raise ValueError("Thuế suất phải nhỏ hơn 1")

    after_tax_hit = reserve_shortfall_pretax * (1.0 - tax_rate)
    adjusted_ni = reported_net_income - after_tax_hit
    adjusted_equity = reported_equity - after_tax_hit
    if adjusted_equity <= 0:
        raise ValueError("Vốn chủ sở hữu sau điều chỉnh bị xóa sạch hoặc âm")

    reported_roe = reported_net_income / reported_equity
    adjusted_roe = adjusted_ni / adjusted_equity
    reported_pb = (market_cap / reported_equity) if market_cap is not None else None
    adjusted_pb = (market_cap / adjusted_equity) if market_cap is not None else None

    return {
        "after_tax_shortfall": after_tax_hit,
        "adjusted_net_income": adjusted_ni,
        "adjusted_equity": adjusted_equity,
        "reported_roe": reported_roe,
        "adjusted_roe": adjusted_roe,
        "reported_pb": reported_pb,
        "adjusted_pb": adjusted_pb,
    }


# ==============================================================================
# 2. BẢO HIỂM PHI NHÂN THỌ (P&C): PHÍ, DỰ PHÒNG, TÁI BẢO HIỂM & FLOAT (013, F8)
# ==============================================================================
def pc_underwriting_bridge(
    direct_premium: float,
    inward_reinsurance_premium: float,
    outward_reinsurance_ceded: float,
    change_in_gross_upr: float,
    change_in_ceded_upr: float,
    net_incurred_claims: float,
    net_underwriting_expenses: float,
    float_balance: float = 0.0,
    investment_income: float = 0.0,
    reinsurance_commission_and_other: float = 0.0,
) -> dict[str, float | None]:
    """Cầu nối doanh thu phí và hiệu quả nghiệp vụ bảo hiểm phi nhân thọ.

    Quy ước dấu theo BCTC bảo hiểm Việt Nam (Thông tư 232/2012/TT-BTC) và US GAAP:
    - `change_in_gross_upr`: mức tăng dự phòng phí gốc & nhận tái trong kỳ (>0 làm giảm NEP).
    - `change_in_ceded_upr`: mức tăng dự phòng phí nhượng tái trong kỳ (>0 làm giảm phí nhượng tái thuần,
      tức cộng lại vào NEP).
    - `net_incurred_claims`: tổng chi bồi thường và tăng dự phòng bồi thường giữ lại thuần (>0 là chi phí).
    - `net_underwriting_expenses`: chi phí khai thác, hoa hồng, quản lý nghiệp vụ thuần sau khi trừ
      hoa hồng nhượng tái (hoặc truyền riêng `reinsurance_commission_and_other`).
    """
    _check_num(direct_premium, "direct_premium", allow_negative=False)
    _check_num(inward_reinsurance_premium, "inward_reinsurance_premium", allow_negative=False)
    _check_num(outward_reinsurance_ceded, "outward_reinsurance_ceded", allow_negative=False)
    _check_num(change_in_gross_upr, "change_in_gross_upr")
    _check_num(change_in_ceded_upr, "change_in_ceded_upr")
    _check_num(net_incurred_claims, "net_incurred_claims", allow_negative=False)
    _check_num(net_underwriting_expenses, "net_underwriting_expenses", allow_negative=False)
    _check_num(float_balance, "float_balance", allow_negative=False)
    _check_num(investment_income, "investment_income")
    _check_num(reinsurance_commission_and_other, "reinsurance_commission_and_other")

    gross_written_premium = direct_premium + inward_reinsurance_premium
    net_written_premium = gross_written_premium - outward_reinsurance_ceded
    net_upr_increase = change_in_gross_upr - change_in_ceded_upr
    net_earned_premium = net_written_premium - net_upr_increase
    if net_earned_premium <= 0:
        raise ValueError("Doanh thu phí bảo hiểm thuần (NEP) phải dương")

    retention_ratio = (net_written_premium / gross_written_premium) if gross_written_premium > 0 else None
    effective_net_expense = net_underwriting_expenses - reinsurance_commission_and_other

    loss_ratio = net_incurred_claims / net_earned_premium
    expense_ratio = effective_net_expense / net_earned_premium
    combined_ratio = loss_ratio + expense_ratio
    underwriting_profit = net_earned_premium - net_incurred_claims - effective_net_expense
    total_operating_profit = underwriting_profit + investment_income
    cost_of_float = (-underwriting_profit / float_balance) if float_balance > 0 else None
    float_investment_yield = (investment_income / float_balance) if float_balance > 0 else None

    return {
        "gross_written_premium": gross_written_premium,
        "net_written_premium": net_written_premium,
        "net_upr_increase": net_upr_increase,
        "net_earned_premium": net_earned_premium,
        "retention_ratio": retention_ratio,
        "loss_ratio": loss_ratio,
        "expense_ratio": expense_ratio,
        "combined_ratio": combined_ratio,
        "underwriting_profit": underwriting_profit,
        "total_operating_profit": total_operating_profit,
        "cost_of_float": cost_of_float,
        "float_investment_yield": float_investment_yield,
    }


def upr_percentage(premium: float, is_cargo_short_term: bool = False) -> float:
    """Dự phòng phí chưa được hưởng theo tỷ lệ phần trăm của tổng phí bảo hiểm
    (Điều 35 Khoản 1 Văn bản hợp nhất 44/2026/VBHN-TT-BTC):
    - Hàng hóa vận chuyển thời hạn từ 1 năm trở xuống: 25%.
    - Các loại hình bảo hiểm khác thời hạn từ 1 năm trở xuống: 50%.
    """
    _check_num(premium, "premium", allow_negative=False)
    return premium * (0.25 if is_cargo_short_term else 0.50)


def upr_1_8(q1: float, q2: float, q3: float, q4: float) -> float:
    """Dự phòng phí chưa được hưởng theo phương pháp hệ số 1/8 đối với hợp đồng kỳ hạn 1 năm
    còn hiệu lực vào ngày cuối năm (Điều 35 Khoản 2(a) VBHN 44/2026/VBHN-TT-BTC):
    Quý I: 1/8; Quý II: 3/8; Quý III: 5/8; Quý IV: 7/8.
    """
    for idx, q in enumerate([q1, q2, q3, q4], 1):
        _check_num(q, f"q{idx}", allow_negative=False)
    return (1.0 * q1 + 3.0 * q2 + 5.0 * q3 + 7.0 * q4) / 8.0


def upr_1_24(monthly_premiums: list[float]) -> float:
    """Dự phòng phí chưa được hưởng theo phương pháp hệ số 1/24 đối với hợp đồng kỳ hạn 1 năm
    phát sinh từ tháng 1 đến tháng 12 (Điều 35 Khoản 2(a) VBHN 44/2026/VBHN-TT-BTC):
    Tháng m (m = 1..12) có tỷ lệ phí chưa được hưởng = (2m - 1) / 24.
    """
    if len(monthly_premiums) != 12:
        raise ValueError("Phương pháp 1/24 cho hợp đồng 1 năm cần đúng 12 tháng phí bảo hiểm")
    total = 0.0
    for m, p in enumerate(monthly_premiums, 1):
        _check_num(p, f"thang_{m}", allow_negative=False)
        total += p * (2 * m - 1) / 24.0
    return total


def upr_daily(premium: float, remaining_days: int | float, total_days: int | float) -> float:
    """Dự phòng phí chưa được hưởng theo công thức tính theo ngày
    (Điều 35 Khoản 2(b) VBHN 44/2026/VBHN-TT-BTC).
    """
    _check_num(premium, "premium", allow_negative=False)
    _check_num(remaining_days, "remaining_days", allow_negative=False)
    _check_num(total_days, "total_days", allow_negative=False, allow_zero=False)
    if remaining_days > total_days:
        raise ValueError("Số ngày còn lại không được vượt quá tổng số ngày của hợp đồng")
    return premium * remaining_days / total_days


def vas_gross_vs_net_reserves(
    gross_upr: float,
    gross_claim_reserve: float,
    ceded_upr_asset: float,
    ceded_claim_asset: float,
    other_gross_reserves: float = 0.0,
) -> dict[str, float]:
    """Đối chiếu quy tắc kế toán bảo hiểm Việt Nam (Thông tư 232/2012/TT-BTC):
    Không được bù trừ trực tiếp Dự phòng nghiệp vụ gốc & nhận tái (bên Nợ phải trả)
    với Tài sản tái bảo hiểm (bên Tài sản).
    """
    for val, name in [
        (gross_upr, "gross_upr"),
        (gross_claim_reserve, "gross_claim_reserve"),
        (ceded_upr_asset, "ceded_upr_asset"),
        (ceded_claim_asset, "ceded_claim_asset"),
        (other_gross_reserves, "other_gross_reserves"),
    ]:
        _check_num(val, name, allow_negative=False)

    total_liability_reserves = gross_upr + gross_claim_reserve + other_gross_reserves
    total_reinsurance_assets = ceded_upr_asset + ceded_claim_asset
    net_upr = gross_upr - ceded_upr_asset
    net_claim_reserve = gross_claim_reserve - ceded_claim_asset
    net_total_reserves = total_liability_reserves - total_reinsurance_assets

    return {
        "liability_reserves_gross": total_liability_reserves,
        "reinsurance_assets": total_reinsurance_assets,
        "net_upr": net_upr,
        "net_claim_reserve": net_claim_reserve,
        "net_total_reserves": net_total_reserves,
    }


# ==============================================================================
# 3. TAM GIÁC BỒI THƯỜNG CHAIN-LADDER, NHÂN THỌ (IFRS 17 & TT 67) & BIÊN KNTT
# ==============================================================================
def incremental_to_cumulative_triangle(incremental: list[list[float]]) -> list[list[float]]:
    """Bước 2 tại Điều 36 Khoản 2(a) VBHN 44/2026/VBHN-TT-BTC:
    Chuyển bảng thống kê bồi thường thực trả từng năm sang bồi thường thực trả lũy kế.
    """
    if not incremental:
        raise ValueError("Tam giác bồi thường không được rỗng")
    n = len(incremental)
    cumulative: list[list[float]] = []
    for i, row in enumerate(incremental):
        expected_len = n - i
        if len(row) != expected_len:
            raise ValueError(f"Dòng {i} phải có {expected_len} cột, nhưng nhận {len(row)}")
        running = 0.0
        cum_row: list[float] = []
        for val in row:
            _check_num(val, f"incremental[{i}]", allow_negative=False)
            running += val
            cum_row.append(running)
        cumulative.append(cum_row)
    return cumulative


def chain_ladder_reserve(
    incremental_or_cumulative: list[list[float]],
    is_cumulative: bool = False,
    average_method: str = "simple_tt67",
    factor_decimals: int | None = 3,
    round_projected_cells: bool = True,
) -> dict[str, object]:
    """Phương pháp hệ số phát sinh bồi thường (Chain-Ladder) theo Điều 36 Khoản 2(a)
    Văn bản hợp nhất số 44/2026/VBHN-TT-BTC (tr. 42-45).

    - `average_method="simple_tt67"` (mặc định): tính hệ số phát sinh từng dòng (làm tròn `factor_decimals`),
      sau đó lấy trung bình cộng giản đơn của cột theo đúng Bước 3 tại Điều 36 Khoản 2(a) VBHN 44/2026/VBHN-TT-BTC,
      tái lập chính xác tuyệt đối bảng mẫu của Bộ Tài chính (Tổng ước tính 208.341 - Đã trả 149.872 = Dự phòng 58.469).
    - `average_method="volume_weighted"`: tính trung bình gia quyền theo quy mô bồi thường lũy kế
      (tổng cột sau chia tổng cột trước — chuẩn actuarial quốc tế).
    """
    cum = (
        [list(r) for r in incremental_or_cumulative]
        if is_cumulative
        else incremental_to_cumulative_triangle(incremental_or_cumulative)
    )
    n = len(cum)
    if n < 2:
        raise ValueError("Tam giác bồi thường cần ít nhất 2 năm tai nạn")
    for i, row in enumerate(cum):
        if len(row) != n - i:
            raise ValueError(f"Dòng lũy kế {i} phải có {n - i} phần tử")

    factors: list[float] = []
    for col in range(n - 1):
        rows_count = n - 1 - col
        if average_method == "simple_tt67":
            row_ratios: list[float] = []
            for r in range(rows_count):
                if cum[r][col] <= 0:
                    raise ValueError(f"Giá trị lũy kế dòng {r} cột {col} phải dương")
                ratio = cum[r][col + 1] / cum[r][col]
                if factor_decimals is not None:
                    ratio = round(ratio, factor_decimals)
                row_ratios.append(ratio)
            f = sum(row_ratios) / len(row_ratios)
        elif average_method == "volume_weighted":
            num = sum(cum[r][col + 1] for r in range(rows_count))
            den = sum(cum[r][col] for r in range(rows_count))
            if den <= 0:
                raise ValueError(f"Tổng cột {col} phải dương để tính hệ số phát sinh")
            f = num / den
        else:
            raise ValueError("average_method phải là 'simple_tt67' hoặc 'volume_weighted'")

        if factor_decimals is not None:
            f = round(f, factor_decimals)
        factors.append(f)

    full_matrix: list[list[float]] = [list(r) for r in cum]
    paid_to_date: list[float] = []
    ultimates: list[float] = []
    reserves_by_year: list[float] = []

    for i in range(n):
        paid = full_matrix[i][-1]
        paid_to_date.append(paid)
        while len(full_matrix[i]) < n:
            col_idx = len(full_matrix[i]) - 1
            nxt = full_matrix[i][-1] * factors[col_idx]
            full_matrix[i].append(nxt)
        if round_projected_cells:
            full_matrix[i] = [float(round(x)) for x in full_matrix[i]]
        ult = full_matrix[i][-1]
        ultimates.append(ult)
        reserves_by_year.append(ult - paid)

    total_paid = sum(paid_to_date)
    total_ultimate = sum(ultimates)
    total_reserve = total_ultimate - total_paid

    return {
        "factors": factors,
        "paid_to_date": paid_to_date,
        "ultimates": ultimates,
        "reserves_by_year": reserves_by_year,
        "total_paid": total_paid,
        "total_ultimate": total_ultimate,
        "total_reserve": total_reserve,
        "full_matrix": full_matrix,
    }


def vn_life_max_tech_rate(
    gov_bond_yield_10y_avg_24m: float,
    inv_return_4q_avg: float,
    pricing_rate: float,
) -> float:
    """Lãi suất kỹ thuật tối đa dùng để trích lập dự phòng toán học bảo hiểm nhân thọ
    (Điều 38 Khoản 2(b) Văn bản hợp nhất số 44/2026/VBHN-TT-BTC):
    Không vượt quá số nhỏ nhất của:
    (1) 80% lãi suất trái phiếu Chính phủ kỳ hạn >= 10 năm bình quân 24 tháng liền trước;
    (2) Tỷ suất lợi nhuận đầu tư của doanh nghiệp trong 4 quý liền trước;
    (3) Lãi suất tính phí của từng sản phẩm.
    """
    _check_num(gov_bond_yield_10y_avg_24m, "gov_bond_yield_10y_avg_24m", allow_negative=False)
    _check_num(inv_return_4q_avg, "inv_return_4q_avg", allow_negative=False)
    _check_num(pricing_rate, "pricing_rate", allow_negative=False)
    return min(0.80 * gov_bond_yield_10y_avg_24m, inv_return_4q_avg, pricing_rate)


def math_reserve_rate_sensitivity(
    future_net_cash_outflow: float,
    duration_years: float,
    old_tech_rate: float,
    new_tech_rate: float,
) -> dict[str, float]:
    """Độ nhạy của Dự phòng toán học (giản lược bằng giá trị hiện tại nghĩa vụ thuần kỳ hạn `duration_years`)
    khi lãi suất kỹ thuật giảm từ `old_tech_rate` xuống `new_tech_rate`.
    """
    _check_num(future_net_cash_outflow, "future_net_cash_outflow", allow_negative=False, allow_zero=False)
    _check_num(duration_years, "duration_years", allow_negative=False, allow_zero=False)
    _check_num(old_tech_rate, "old_tech_rate", allow_negative=False)
    _check_num(new_tech_rate, "new_tech_rate", allow_negative=False)

    old_reserve = future_net_cash_outflow / ((1.0 + old_tech_rate) ** duration_years)
    new_reserve = future_net_cash_outflow / ((1.0 + new_tech_rate) ** duration_years)
    reserve_increase = new_reserve - old_reserve
    pct_change = reserve_increase / old_reserve

    return {
        "old_reserve": old_reserve,
        "new_reserve": new_reserve,
        "reserve_increase": reserve_increase,
        "pct_change": pct_change,
    }


def ifrs17_csm_rollforward(
    opening_csm: float,
    new_contracts_csm: float,
    accretion_rate: float,
    fulfillment_cf_change_future: float,
    coverage_units_current: float,
    coverage_units_remaining_after: float,
) -> dict[str, float]:
    """Cuộn số dư Biên lợi nhuận dịch vụ hợp đồng (Contractual Service Margin - CSM) theo chuẩn IFRS 17:
    - Cộng CSM của hợp đồng mới phát hành trong kỳ (`new_contracts_csm`).
    - Cộng lãi tích lũy trên CSM (`accretion_rate` tính trên số dư đầu kỳ; giản lược hợp đồng mới phát sinh cuối kỳ).
    - Điều chỉnh thay đổi ước tính dòng tiền hoàn thành nghĩa vụ tương lai (`fulfillment_cf_change_future`:
      >0 nếu ước tính thuận lợi làm tăng CSM, <0 nếu ước tính bất lợi làm giảm CSM).
    - Nếu thay đổi bất lợi vượt quá số dư CSM trước phân bổ, CSM chạm sàn 0 và phần vượt bị ghi nhận ngay
      làm Cấu phần lỗ (`loss_component_recognized`) trên báo cáo kết quả kinh doanh (Onerous contracts).
    - Phân bổ CSM vào doanh thu bảo hiểm trong kỳ theo tỷ lệ Đơn vị bảo vệ (`coverage_units`).
    """
    _check_num(opening_csm, "opening_csm", allow_negative=False)
    _check_num(new_contracts_csm, "new_contracts_csm", allow_negative=False)
    _check_num(accretion_rate, "accretion_rate", allow_negative=False)
    _check_num(fulfillment_cf_change_future, "fulfillment_cf_change_future")
    _check_num(coverage_units_current, "coverage_units_current", allow_negative=False)
    _check_num(coverage_units_remaining_after, "coverage_units_remaining_after", allow_negative=False)
    total_units = coverage_units_current + coverage_units_remaining_after
    if total_units <= 0:
        raise ValueError("Tổng đơn vị bảo vệ (coverage units) phải dương")

    interest_accretion = opening_csm * accretion_rate
    pre_adjust_csm = opening_csm + new_contracts_csm + interest_accretion + fulfillment_cf_change_future

    if pre_adjust_csm < 0:
        loss_component = -pre_adjust_csm
        csm_before_release = 0.0
    else:
        loss_component = 0.0
        csm_before_release = pre_adjust_csm

    release_ratio = coverage_units_current / total_units
    csm_released = csm_before_release * release_ratio
    closing_csm = csm_before_release - csm_released

    return {
        "opening_csm": opening_csm,
        "interest_accretion": interest_accretion,
        "pre_release_csm": csm_before_release,
        "loss_component_recognized": loss_component,
        "release_ratio": release_ratio,
        "csm_released_to_revenue": csm_released,
        "closing_csm": closing_csm,
    }


def solvency_margin_pnt(
    net_retained_premium: float,
    total_gross_and_assumed_premium: float,
    owners_equity_eligible: float,
    unsecured_corp_bonds: float = 0.0,
    listed_shares_and_fund_units: float = 0.0,
    unlisted_shares: float = 0.0,
    tangible_fixed_and_intangible_software_land_inventory: float = 0.0,
    overdue_receivables_over_2y_or_illiquid: float = 0.0,
    secured_corp_bonds: float = 0.0,
) -> dict[str, float]:
    """Tính Biên khả năng thanh toán tối thiểu và Biên khả năng thanh toán thực tế của doanh nghiệp
    bảo hiểm phi nhân thọ theo Mẫu biểu 7-PNT (Văn bản hợp nhất số 44/2026/VBHN-TT-BTC, tr. 137-138):
    - Biên KNTT tối thiểu = max(25% tổng phí giữ lại, 12.5% tổng phí bảo hiểm gốc và nhận tái).
    - Các khoản loại trừ một phần giá trị tài sản:
      + Trái phiếu DN có bảo đảm: 1%
      + Trái phiếu DN không có bảo đảm: 3%
      + Cổ phiếu niêm yết và chứng chỉ quỹ: 15%
      + Cổ phiếu chưa niêm yết: 20%
      + Tài sản cố định hữu hình, phần mềm, quyền sử dụng đất, hàng tồn kho: 25%
      + Tài sản bị loại trừ toàn bộ (phải thu quá hạn >= 2 năm, tạm ứng, trả trước...): 100%.
    """
    for val, name in [
        (net_retained_premium, "net_retained_premium"),
        (total_gross_and_assumed_premium, "total_gross_and_assumed_premium"),
        (owners_equity_eligible, "owners_equity_eligible"),
        (unsecured_corp_bonds, "unsecured_corp_bonds"),
        (listed_shares_and_fund_units, "listed_shares_and_fund_units"),
        (unlisted_shares, "unlisted_shares"),
        (tangible_fixed_and_intangible_software_land_inventory, "tangible_fixed_and_intangible_software_land_inventory"),
        (overdue_receivables_over_2y_or_illiquid, "overdue_receivables_over_2y_or_illiquid"),
        (secured_corp_bonds, "secured_corp_bonds"),
    ]:
        _check_num(val, name, allow_negative=False)

    min_solvency_margin = max(0.25 * net_retained_premium, 0.125 * total_gross_and_assumed_premium)
    if min_solvency_margin <= 0:
        raise ValueError("Biên khả năng thanh toán tối thiểu phải dương")

    total_deductions = (
        1.00 * overdue_receivables_over_2y_or_illiquid
        + 0.01 * secured_corp_bonds
        + 0.03 * unsecured_corp_bonds
        + 0.15 * listed_shares_and_fund_units
        + 0.20 * unlisted_shares
        + 0.25 * tangible_fixed_and_intangible_software_land_inventory
    )
    actual_solvency_margin = owners_equity_eligible - total_deductions
    solvency_ratio = actual_solvency_margin / min_solvency_margin

    return {
        "minimum_solvency_margin": min_solvency_margin,
        "asset_haircut_deductions": total_deductions,
        "actual_solvency_margin": actual_solvency_margin,
        "solvency_ratio": solvency_ratio,
    }


# ==============================================================================
# 4. BẢO HIỂM CÁ NHÂN: CẤU TRÚC PHÍ UL/ILP VS. TỬ KỲ + TỰ ĐẦU TƯ (BÀI P4)
# ==============================================================================
# Trần phí ban đầu tối đa đối với bảo hiểm liên kết đầu tư đóng phí định kỳ
# theo Điều 22 Khoản 3 Văn bản hợp nhất số 44/2026/VBHN-TT-BTC:
# Năm 1: 50%; Năm 2: 30%; Năm 3-5: 20%; Năm 6-10: 2%; Từ năm 11: 0%.
VN_MAX_UL_INITIAL_FEE_RATES: list[float] = [
    0.50,  # Năm 1
    0.30,  # Năm 2
    0.20,  # Năm 3
    0.20,  # Năm 4
    0.20,  # Năm 5
    0.02,  # Năm 6
    0.02,  # Năm 7
    0.02,  # Năm 8
    0.02,  # Năm 9
    0.02,  # Năm 10
]


def vn_ul_initial_fee_rate(policy_year: int) -> float:
    """Trả về tỷ lệ phí ban đầu tối đa tính trên phí bảo hiểm cơ bản năm hợp đồng `policy_year` (1-indexed)
    theo Điều 22 Khoản 3(a) VBHN 44/2026/VBHN-TT-BTC.
    """
    if not isinstance(policy_year, int) or policy_year < 1:
        raise ValueError("Năm hợp đồng (policy_year) phải là số nguyên >= 1")
    if policy_year <= len(VN_MAX_UL_INITIAL_FEE_RATES):
        return VN_MAX_UL_INITIAL_FEE_RATES[policy_year - 1]
    return 0.0


def ul_vs_term_invest(
    annual_total_budget: float,
    base_premium_ul: float,
    sum_assured: float,
    coi_rates_per_1000: list[float],
    annual_admin_fee_ul: float,
    gross_fund_return: float,
    ul_fund_mgmt_fee_rate: float,
    term_annual_premium: float,
    etf_expense_ratio: float = 0.005,
    surrender_charge_rates: list[float] | None = None,
    initial_fee_rates: list[float] | None = None,
    topup_initial_fee_rate_first_10y: float = 0.015,
) -> dict[str, object]:
    """So sánh dòng tiền nhiều năm giữa hai phương án với cùng ngân sách hàng năm `annual_total_budget`
    và cùng số tiền bảo hiểm tử vong `sum_assured`:

    - Phương án A (Bảo hiểm liên kết đầu tư UL/ILP):
      Đóng `base_premium_ul` (phí cơ bản) + `topup = annual_total_budget - base_premium_ul` (phí đóng thêm).
      Khấu trừ phí ban đầu (theo trần Điều 22 VBHN 44/2026/VBHN-TT-BTC hoặc biểu phí truyền vào),
      phí quản lý hợp đồng (`annual_admin_fee_ul`), phí rủi ro (`COI = NAR * coi_rate / 1000`,
      với `NAR = max(sum_assured - account_value, 0)` cho quyền lợi cơ bản),
      sau đó sinh lời ở mức `gross_fund_return - ul_fund_mgmt_fee_rate`.
      Giá trị hoàn lại = Giá trị tài khoản * (1 - tỷ lệ phí chấm dứt trước hạn).

    - Phương án B (Mua Bảo hiểm Tử kỳ thuần túy + Tự đầu tư phần chênh lệch):
      Đóng `term_annual_premium` (không có giá trị hoàn lại) và đầu tư `annual_total_budget - term_annual_premium`
      vào quỹ chỉ số/tài sản có cùng tỷ suất sinh lời gộp `gross_fund_return` trừ phí quỹ `etf_expense_ratio`.
    """
    _check_num(annual_total_budget, "annual_total_budget", allow_negative=False, allow_zero=False)
    _check_num(base_premium_ul, "base_premium_ul", allow_negative=False, allow_zero=False)
    if base_premium_ul > annual_total_budget:
        raise ValueError("Phí cơ bản UL không được vượt quá tổng ngân sách năm")
    _check_num(sum_assured, "sum_assured", allow_negative=False, allow_zero=False)
    _check_num(annual_admin_fee_ul, "annual_admin_fee_ul", allow_negative=False)
    _check_num(gross_fund_return, "gross_fund_return")
    _check_num(ul_fund_mgmt_fee_rate, "ul_fund_mgmt_fee_rate", allow_negative=False)
    _check_num(term_annual_premium, "term_annual_premium", allow_negative=False)
    if term_annual_premium > annual_total_budget:
        raise ValueError("Phí bảo hiểm tử kỳ không được vượt quá tổng ngân sách năm")
    _check_num(etf_expense_ratio, "etf_expense_ratio", allow_negative=False)
    _check_num(topup_initial_fee_rate_first_10y, "topup_initial_fee_rate_first_10y", allow_negative=False)
    if topup_initial_fee_rate_first_10y > 0.015 + 1e-9:
        raise ValueError("Phí ban đầu đối với phí đóng thêm không vượt quá 1,5% trong 10 năm đầu (Điều 22 Khoản 3)")

    years = len(coi_rates_per_1000)
    if years < 1:
        raise ValueError("Danh sách tỷ lệ phí rủi ro (coi_rates_per_1000) không được rỗng")

    if surrender_charge_rates is None:
        # Biểu phí chấm dứt hợp đồng trước hạn minh họa phổ biến trên thị trường trong những năm đầu
        surrender_charge_rates = [0.80, 0.60, 0.40, 0.25, 0.15, 0.05] + [0.0] * max(0, years - 6)
    if len(surrender_charge_rates) < years:
        surrender_charge_rates = list(surrender_charge_rates) + [0.0] * (years - len(surrender_charge_rates))

    topup_premium = annual_total_budget - base_premium_ul
    ul_net_return = gross_fund_return - ul_fund_mgmt_fee_rate
    diy_net_return = gross_fund_return - etf_expense_ratio

    ul_account_value = 0.0
    diy_portfolio_value = 0.0
    schedule: list[dict[str, float | int]] = []

    for yr in range(1, years + 1):
        coi_rate = _check_num(coi_rates_per_1000[yr - 1], f"coi_rate_{yr}", allow_negative=False)
        base_fee_rate = (
            _check_num(initial_fee_rates[yr - 1], f"initial_fee_rate_{yr}", allow_negative=False)
            if initial_fee_rates is not None and yr <= len(initial_fee_rates)
            else vn_ul_initial_fee_rate(yr)
        )
        topup_fee_rate = topup_initial_fee_rate_first_10y if yr <= 10 else 0.0
        initial_fee = base_premium_ul * base_fee_rate + topup_premium * topup_fee_rate

        # Dòng tiền đầu năm vào giá trị tài khoản trước khi khấu trừ COI và phí quản lý hợp đồng
        av_after_contribution = ul_account_value + annual_total_budget - initial_fee
        net_amount_at_risk = max(sum_assured - av_after_contribution, 0.0)
        coi_charge = (net_amount_at_risk / 1000.0) * coi_rate
        av_before_growth = max(av_after_contribution - coi_charge - annual_admin_fee_ul, 0.0)
        ul_account_value = av_before_growth * (1.0 + ul_net_return)

        surr_rate = _check_num(surrender_charge_rates[yr - 1], f"surrender_rate_{yr}", allow_negative=False)
        cash_surrender_value = ul_account_value * (1.0 - surr_rate)

        # Phương án B: mua Tử kỳ đầu năm, đầu tư phần chênh lệch suốt năm ở mức diy_net_return
        diy_invest_contribution = annual_total_budget - term_annual_premium
        diy_portfolio_value = (diy_portfolio_value + diy_invest_contribution) * (1.0 + diy_net_return)

        schedule.append({
            "year": yr,
            "initial_fee": initial_fee,
            "coi_charge": coi_charge,
            "admin_fee": annual_admin_fee_ul,
            "ul_account_value": ul_account_value,
            "ul_surrender_value": cash_surrender_value,
            "diy_portfolio_value": diy_portfolio_value,
            "wealth_gap_diy_minus_ul_surrender": diy_portfolio_value - cash_surrender_value,
            "wealth_gap_diy_minus_ul_av": diy_portfolio_value - ul_account_value,
        })

    return {
        "years": years,
        "ul_net_return": ul_net_return,
        "diy_net_return": diy_net_return,
        "final_ul_account_value": ul_account_value,
        "final_ul_surrender_value": schedule[-1]["ul_surrender_value"],
        "final_diy_portfolio_value": diy_portfolio_value,
        "total_initial_fees_paid": sum(float(r["initial_fee"]) for r in schedule),
        "total_coi_paid": sum(float(r["coi_charge"]) for r in schedule),
        "schedule": schedule,
    }


if __name__ == "__main__":
    data = load_historical_inputs()
    # 1. GEICO FY2025 (triệu USD)
    geico_pe = float(data[("GEICO", "Premiums earned")]["2025"])
    geico_loss = float(data[("GEICO", "Losses and loss adjustment expenses")]["2025"])
    geico_exp = float(data[("GEICO", "Underwriting expenses")]["2025"])
    geico_pw = float(data[("GEICO", "Premiums written")]["2025"])
    geico_res = pc_underwriting_bridge(
        direct_premium=geico_pw,
        inward_reinsurance_premium=0.0,
        outward_reinsurance_ceded=0.0,
        change_in_gross_upr=geico_pw - geico_pe,
        change_in_ceded_upr=0.0,
        net_incurred_claims=geico_loss,
        net_underwriting_expenses=geico_exp,
        float_balance=float(data[("BRK_INS", "Insurance float year-end")]["2025"]),
        investment_income=float(data[("BRK_INS", "Net investment income pre-tax")]["2025"]),
    )
    print(
        f"GEICO FY2025: NEP=${geico_res['net_earned_premium']:.0f}M | "
        f"Loss ratio={geico_res['loss_ratio']:.4%} | Expense ratio={geico_res['expense_ratio']:.4%} | "
        f"Combined ratio={geico_res['combined_ratio']:.4%} | UW Profit=${geico_res['underwriting_profit']:.0f}M"
    )

    # 2. Tam giác bồi thường Chain-Ladder (Điều 36 VBHN 44/2026/VBHN-TT-BTC)
    cl = chain_ladder_reserve(TT67_INCREMENTAL_TRIANGLE)
    print(
        f"Chain-Ladder TT67/VBHN44: Đã trả={cl['total_paid']:.0f} tr.đ | "
        f"Tổng ước tính cuối cùng={cl['total_ultimate']:.0f} tr.đ | "
        f"Dự phòng bồi thường cần trích={cl['total_reserve']:.0f} tr.đ"
    )

    # 3. So sánh UL đóng phí định kỳ 20 tr.đ/năm vs. Mua Tử kỳ 1,8 tr.đ/năm + Tự đầu tư 18,2 tr.đ/năm trong 10 năm
    comp = ul_vs_term_invest(
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
    print(
        f"Sau 10 năm (triệu VND): Giá trị tài khoản UL={comp['final_ul_account_value']:.2f} | "
        f"Tài sản tự đầu tư (kèm Tử kỳ)={comp['final_diy_portfolio_value']:.2f}"
    )
