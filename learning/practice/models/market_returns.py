"""Phép tính học tập N1/N4/N5; không dữ liệu thị trường hoặc lựa chọn đầu tư.

Tiền giữ đơn vị người gọi truyền vào. Tỷ lệ là số thập phân. Người gọi phải
xác minh ngày, tiền tệ và cơ sở cổ tức trước khi ghép đầu vào.
"""
from __future__ import annotations

import math


def _finite(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError("Đầu vào phải là số hữu hạn, không được thiếu")
    return float(value)


def _nonnegative(value):
    value = _finite(value)
    if value < 0:
        raise ValueError("Số tiền, giá hoặc số lượng phải không âm")
    return value


def _positive(value):
    value = _finite(value)
    if value <= 0:
        raise ValueError("Mẫu số/thời hạn phải dương")
    return value


def _rate(value):
    value = _finite(value)
    if value <= -1:
        raise ValueError("Tỷ lệ ghép/chiết khấu phải lớn hơn -100%")
    return value


def issuance(shares, price, costs=0):
    return _nonnegative(shares) * _nonnegative(price) - _nonnegative(costs)


def ownership(held, outstanding):
    held, outstanding = _nonnegative(held), _positive(outstanding)
    if held > outstanding:
        raise ValueError("Số đang giữ không được vượt tổng lưu hành trong bài toán")
    return held / outstanding


def market_cap(price, outstanding):
    return _nonnegative(price) * _positive(outstanding)


def enterprise_value(equity_value, debt, cash):
    """EV giản lược chỉ có vốn hóa, nợ và tiền; không tự phân loại khoản mục."""
    return _nonnegative(equity_value) + _nonnegative(debt) - _nonnegative(cash)


def book_fill(asks, quantity, limit=None):
    """Sổ bán tĩnh hư cấu, không có ưu tiên thời gian/hủy lệnh/biên độ thị trường."""
    quantity = _positive(quantity)
    limit = math.inf if limit is None else _nonnegative(limit)
    levels = [(_positive(price), _nonnegative(qty)) for price, qty in asks]
    if levels != sorted(levels, key=lambda x: x[0]):
        raise ValueError("Mức giá bán phải tăng dần")
    remaining, cost = quantity, 0.0
    for price, available in levels:
        if price > limit:
            break
        take = min(remaining, available)
        cost += take * price
        remaining -= take
        if remaining == 0:
            break
    filled = quantity - remaining
    return {"filled": filled, "unfilled": remaining, "cost": cost,
            "average_price": cost / filled if filled else None}


def future_value(pv, rate, periods):
    return _nonnegative(pv) * (1 + _rate(rate)) ** _nonnegative(periods)


def present_value(fv, rate, periods):
    return _nonnegative(fv) / (1 + _rate(rate)) ** _nonnegative(periods)


def cagr(begin, end, years):
    return (_nonnegative(end) / _positive(begin)) ** (1 / _positive(years)) - 1


def effective_annual_rate(nominal, compounds_per_year):
    m = _positive(compounds_per_year)
    if not m.is_integer():
        raise ValueError("Số lần ghép trong năm phải là số nguyên")
    return (1 + _rate(_finite(nominal) / m)) ** m - 1


def equivalent_period_rate(annual_effective, periods_per_year):
    return (1 + _rate(annual_effective)) ** (1 / _positive(periods_per_year)) - 1


def real_return(nominal, inflation):
    nominal = _finite(nominal)
    if nominal < -1:
        raise ValueError("Lợi suất danh nghĩa không thấp hơn -100% trong mô hình")
    return (1 + nominal) / (1 + _rate(inflation)) - 1


def total_return(begin_price, end_price, dividend=0):
    return (_nonnegative(end_price) + _nonnegative(dividend)) / _positive(begin_price) - 1


def monthly_contributions(initial, contribution, monthly_rate, months, timing="end"):
    """Mô phỏng từng kỳ, không suy APR/hiệu dụng từ tên đầu vào."""
    balance, contribution = _nonnegative(initial), _nonnegative(contribution)
    rate, months = _rate(monthly_rate), _nonnegative(months)
    if not months.is_integer() or timing not in ("start", "end"):
        raise ValueError("Số tháng nguyên và timing start/end là bắt buộc")
    for _ in range(int(months)):
        if timing == "start":
            balance += contribution
        balance *= 1 + rate
        if timing == "end":
            balance += contribution
    return balance


def _weights(weights):
    weights = [_nonnegative(w) for w in weights]
    if not weights or not math.isclose(sum(weights), 1, abs_tol=1e-10, rel_tol=0):
        raise ValueError("Trọng số danh mục không đòn bẩy phải cộng thành 1")
    return weights


def weighted_return(weights, returns):
    weights, returns = _weights(weights), [_finite(r) for r in returns]
    if len(weights) != len(returns) or any(r < -1 for r in returns):
        raise ValueError("Số khoản phải khớp; mỗi lợi suất không dưới -100%")
    return sum(w * r for w, r in zip(weights, returns))


def evolve(amounts, returns):
    amounts, returns = [_nonnegative(x) for x in amounts], [_finite(r) for r in returns]
    if not amounts or len(amounts) != len(returns) or any(r < -1 for r in returns):
        raise ValueError("Cần đủ số tiền và lợi suất từng khoản")
    closing = [a * (1 + r) for a, r in zip(amounts, returns)]
    total = sum(closing)
    return {"amounts": closing, "total": total,
            "weights": [a / total for a in closing] if total else None}


def rebalance(amounts, targets):
    """Chênh tiền về mục tiêu hư cấu, chưa phí/thuế, không tự đặt giao dịch."""
    amounts, targets = [_nonnegative(a) for a in amounts], _weights(targets)
    if len(amounts) != len(targets):
        raise ValueError("Số khoản và mục tiêu phải khớp")
    total = _positive(sum(amounts))
    destination = [total * w for w in targets]
    return {"targets": destination, "transfers": [d - a for d, a in zip(destination, amounts)]}


def compound_returns(returns):
    result = 1.0
    for rate in returns:
        rate = _finite(rate)
        if rate < -1:
            raise ValueError("Lợi suất tài sản không đòn bẩy không dưới -100%")
        result *= 1 + rate
    return result - 1


def currency_return(asset_return, currency_change):
    """Tỷ giá là nội tệ/1 ngoại tệ; tăng nghĩa ngoại tệ mạnh lên."""
    return compound_returns([asset_return, currency_change])


def after_fee_growth(principal, gross_rate, end_year_fee_rate, years):
    fee = _nonnegative(end_year_fee_rate)
    years = _nonnegative(years)
    if fee >= 1 or not years.is_integer():
        raise ValueError("Phí phải dưới 100%; mô hình thu phí cuối năm dùng năm nguyên")
    return _nonnegative(principal) * ((1 + _rate(gross_rate)) * (1 - fee)) ** int(years)


def lesson_examples():
    """Đầu vào lịch sử chỉ để tái lập bài; không cập nhật từ Internet khi chạy."""
    drift = evolve([50, 30, 20], [.10, -.05, .02])
    reset = rebalance(drift["amounts"], [.5, .3, .2])
    return {
        "n1_primary_net": issuance(200_000, 10_000, 100_000_000),
        "n1_secondary_gross": issuance(50_000, 10_000),
        "n1_ev": enterprise_value(market_cap(12_500, 80_000_000), 400e9, 150e9),
        "n1_book": book_fill([(20_100, 300), (20_300, 100)], 400),
        "n1_apple_hypothetical_cap": market_cap(250, 14_776_353_000),
        "n4_pv150": present_value(150, .08, 3),
        "n4_pv150_at10": present_value(150, .10, 3),
        "n4_effective12": effective_annual_rate(.12, 12),
        "n4_month_effective12": equivalent_period_rate(.12, 12),
        "n4_real8_4": real_return(.08, .04),
        "n4_real8_10": real_return(.08, .10),
        "n4_apple_cagr": cagr(100, 234, 5),
        "n4_sp500_cagr": cagr(100, 217, 5),
        "n4_contributions_end": monthly_contributions(10, 2, .005, 36),
        "n4_contributions_start": monthly_contributions(10, 2, .005, 36, "start"),
        "n4_transfer_fv": future_value(25, .06, 4),
        "n4_transfer_real": real_return(currency_return(.09, -.05), .04),
        "n5_drift": drift,
        "n5_no_rebalance_year2": evolve(drift["amounts"], [-.2, .1, 0]),
        "n5_rebalanced_year2": evolve(reset["targets"], [-.2, .1, 0]),
        "n5_two_year_fee": after_fee_growth(100, .05, .01, 2),
        "n5_voo_gap_pp": 15.70 - 15.74,
        "n5_static_fee": 100_000_000 * .0003,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(lesson_examples(), ensure_ascii=False, indent=2))
