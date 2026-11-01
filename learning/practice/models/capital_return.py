"""SBC, pha loãng, mua lại cổ phiếu và cổ tức (bài Q2). Chỉ dùng thư viện chuẩn Python 3.

Số Apple FY2025 nằm trong apple_capital_return_inputs.csv (triệu USD, cổ phiếu tính bằng nghìn).
Mọi giả định giá và giá trị nội tại trong ví dụ hư cấu là GIẢ ĐỊNH bài học.
Chạy: python3 capital_return.py
"""
from __future__ import annotations

import csv
from pathlib import Path

HERE = Path(__file__).parent


def load_apple() -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {}
    with open(HERE / "apple_capital_return_inputs.csv", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            out[r["chi_tieu"]] = {y: float(r[y]) for y in ("FY2025", "FY2024", "FY2023") if r[y] != ""}
    return out


def fcf_after_sbc(cfo: float, capex: float, sbc: float) -> float:
    """FCF đơn giản trừ SBC (SBC coi như chi phí thật; chưa phải FCFF)."""
    return cfo - capex - sbc


def payout_ratio(dividends: float, net_income: float) -> float:
    return dividends / net_income


def total_cash_returned(dividends: float, repurchases: float, tax_settlement: float = 0.0) -> float:
    return dividends + repurchases + tax_settlement


def shrink(shares_start: float, shares_end: float) -> float:
    """Phần trăm thay đổi số cổ phiếu (âm là giảm)."""
    return shares_end / shares_start - 1


def dilution_pct(diluted: float, basic: float) -> float:
    return diluted / basic - 1


# ---------- mua lại: tác động EPS và giá trị mỗi cổ phiếu ----------
def buyback(shares: float, net_income: float, amount: float, price: float) -> dict[str, float]:
    bought = amount / price
    new_shares = shares - bought
    return {"co_phieu_mua": bought, "co_phieu_con_lai": new_shares,
            "eps_truoc": net_income / shares, "eps_sau": net_income / new_shares}


def value_per_share_after_buyback(equity_value: float, shares: float, amount: float, price: float) -> float:
    """Giá trị nội tại mỗi cổ phiếu sau khi chi `amount` tiền mặt mua lại ở `price`.
    Giả định đơn giản: giá trị vốn chủ trước mua lại là equity_value (gồm tiền sẽ chi)."""
    return (equity_value - amount) / (shares - amount / price)


def breakeven_price(equity_value: float, shares: float) -> float:
    """Mua lại không làm tăng cũng không giảm giá trị mỗi cổ phiếu khi giá = giá trị nội tại."""
    return equity_value / shares


# ---------- SBC ----------
def sbc_dilution_shares(grant_value: float, price: float) -> float:
    """Số cổ phiếu phát hành thêm để trả SBC có giá trị grant_value ở giá price."""
    return grant_value / price


def net_buyback_shares(amount: float, price: float, issued_for_sbc: float) -> float:
    """Số cổ phiếu giảm ròng sau mua lại trừ cổ phiếu phát hành cho SBC."""
    return amount / price - issued_for_sbc


# ---------- cổ phiếu thưởng ----------
def adjust_for_bonus(eps_old: float, bonus_per_hold: float) -> float:
    """EPS điều chỉnh khi thưởng `bonus_per_hold` cổ phiếu cho mỗi 1 cổ phiếu cũ (10:2 là 0,2)."""
    return eps_old / (1 + bonus_per_hold)


def bonus_ratio(shares_before: float, shares_after: float) -> float:
    return shares_after / shares_before - 1


def main() -> None:
    a = load_apple()
    for y in ("FY2025", "FY2024", "FY2023"):
        ni, sbc = a["net_income"][y], a["sbc"][y]
        div, bb, tx = a["dividends_paid"][y], a["repurchases_cash"][y], a["tax_net_share_settlement"][y]
        cfo, capex = a["cfo"][y], a["capex"][y]
        print(y, "FCF trừ SBC", fcf_after_sbc(cfo, capex, sbc), "payout", round(payout_ratio(div, ni), 4),
              "tổng chi cho cổ đông", total_cash_returned(div, bb, tx), "SBC/CFO", round(sbc / cfo, 4))
    print("co phieu luu hanh cuoi nam doi:", round(shrink(a["shares_outstanding_end"]["FY2024"],
                                                          a["shares_outstanding_end"]["FY2025"]), 4))


if __name__ == "__main__":
    main()
