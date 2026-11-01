"""Chuẩn hóa lợi nhuận công ty chu kỳ (bài Q3). Chỉ dùng thư viện chuẩn Python 3.

Số lịch sử HPG nằm trong hpg_cycle_inputs.csv (tỷ VND). Mọi tham số tương lai là GIẢ ĐỊNH bài học.
Chạy: python3 cyclical.py
"""
from __future__ import annotations

import csv
import statistics
from pathlib import Path

HERE = Path(__file__).parent

# Số 9 tháng 2026 (chưa kiểm toán, tỷ VND), từ "Tổng quan tình hình kinh doanh Quý III-2026".
# LNST là lợi nhuận sau thuế CHUNG (chưa tách cổ đông công ty mẹ); doanh thu là số báo cáo công bố.
NINE_M_2026 = {"doanh_thu": 171539.0, "loi_nhuan_gop": 30775.0, "lnst_chung": 23746.0, "von_chu": 149568.0}


def load_hpg() -> list[dict[str, float | str]]:
    rows = []
    with open(HERE / "hpg_cycle_inputs.csv", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            rows.append({k: (v if k in ("nam", "nguon") else float(v)) for k, v in r.items()})
    return rows


def margins(rows, num: str, den: str = "doanh_thu_thuan") -> list[float]:
    return [r[num] / r[den] for r in rows]


def avg_dollar(values: list[float]) -> float:
    """Trung bình số tuyệt đối. Sai khi quy mô công ty đã đổi (Damodaran, tr. 619)."""
    return sum(values) / len(values)


def avg_margin_norm(revenue_now: float, margin_list: list[float]) -> float:
    """Biên trung bình giản đơn nhân doanh thu hiện tại."""
    return revenue_now * sum(margin_list) / len(margin_list)


def weighted_margin_norm(revenue_now: float, nums: list[float], dens: list[float]) -> float:
    """Biên gia quyền (tổng tử / tổng mẫu) nhân doanh thu hiện tại."""
    return revenue_now * sum(nums) / sum(dens)


def median_margin_norm(revenue_now: float, margin_list: list[float]) -> float:
    return revenue_now * statistics.median(margin_list)


def trimmed(values: list[float], drop_max: int = 1, drop_min: int = 0) -> list[float]:
    s = sorted(values)
    return s[drop_min: len(s) - drop_max]


def roe_norm(equity_now: float, roe_list: list[float]) -> float:
    """ROE trung bình nhân vốn chủ hiện tại (xấp xỉ: ROE = lợi nhuận / vốn chủ cuối năm)."""
    return equity_now * sum(roe_list) / len(roe_list)


def discount_back(normalized: float, rate: float, years: float) -> float:
    """Nếu phải mất `years` năm mới về mức chuẩn, giá trị hiện tại thấp hơn (Damodaran, tr. 619)."""
    return normalized / (1 + rate) ** years


def cycle_gap(reported: float, normalized: float) -> float:
    """reported/normalized - 1: dương là lợi nhuận đang cao hơn mức chuẩn."""
    return reported / normalized - 1


def pe(price: float, earnings_per_share: float) -> float:
    return price / earnings_per_share


def interest_cover(ebit_like: float, interest: float) -> float:
    return ebit_like / interest


def main() -> None:
    rows = load_hpg()
    pat = [r["lnst_cong_ty_me"] for r in rows]
    rev = [r["doanh_thu_thuan"] for r in rows]
    m = margins(rows, "lnst_cong_ty_me")
    now = rows[-1]
    print("Biên LNST mẹ/doanh thu:", [round(x * 100, 2) for x in m])
    print("TB số tuyệt đối 5 năm:", round(avg_dollar(pat), 1))
    print("TB bỏ năm đỉnh:", round(avg_dollar(trimmed(pat)), 1))
    print("Biên TB x DT 2025:", round(avg_margin_norm(now["doanh_thu_thuan"], m), 1))
    print("Biên gia quyền x DT 2025:", round(weighted_margin_norm(now["doanh_thu_thuan"], pat, rev), 1))
    print("Biên trung vị x DT 2025:", round(median_margin_norm(now["doanh_thu_thuan"], m), 1))
    print("Biên TB bỏ đỉnh x DT 2025:", round(avg_margin_norm(now["doanh_thu_thuan"], trimmed(m)), 1))
    roe = [r["lnst_cong_ty_me"] / r["von_chu_cuoi_nam"] for r in rows]
    print("ROE xấp xỉ:", [round(x * 100, 2) for x in roe])
    print("ROE TB x vốn chủ 2025:", round(roe_norm(now["von_chu_cuoi_nam"], roe), 1))


if __name__ == "__main__":
    main()
