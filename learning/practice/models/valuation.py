"""Mô hình định giá nhỏ cho bài 010, 011, 012, F1, F2 (chỉ dùng thư viện chuẩn).

Mọi đầu vào ngoài tệp apple_fy2025_inputs.csv là GIẢ ĐỊNH bài học, không phải dự báo.
Chạy: python3 valuation.py
"""
from __future__ import annotations

import csv
from pathlib import Path

HERE = Path(__file__).parent


def load_apple() -> dict[str, float]:
    with open(HERE / "apple_fy2025_inputs.csv", encoding="utf-8") as fh:
        return {r["chi_tieu"]: float(r["gia_tri_trieu_USD"]) for r in csv.DictReader(fh)}


# ---------- 010: chi phí vốn ----------
def capm(rf: float, beta: float, erp: float) -> float:
    return rf + beta * erp


def unlever(beta_l: float, d_over_e: float, tax: float) -> float:
    return beta_l / (1 + (1 - tax) * d_over_e)


def relever(beta_u: float, d_over_e: float, tax: float) -> float:
    return beta_u * (1 + (1 - tax) * d_over_e)


def wacc(ke: float, kd: float, tax: float, equity: float, debt: float) -> float:
    v = equity + debt
    return ke * equity / v + kd * (1 - tax) * debt / v


def convert_rate(r_from: float, infl_from: float, infl_to: float) -> float:
    """Đổi lãi suất danh nghĩa giữa hai tiền tệ qua chênh lệch lạm phát kỳ vọng."""
    return (1 + r_from) * (1 + infl_to) / (1 + infl_from) - 1


# ---------- 011: DCF ----------
def _need_gap(rate: float, g: float, name: str) -> None:
    if rate <= g:
        raise ValueError(f"{name} ({rate:.4f}) phải lớn hơn tăng trưởng dài hạn ({g:.4f})")


def dcf(fcf0: float, growth: list[float], w: float, g_term: float) -> dict[str, float]:
    _need_gap(w, g_term, "WACC")
    f, pv, flows = fcf0, 0.0, []
    for i, g in enumerate(growth, 1):
        f *= 1 + g
        flows.append(f)
        pv += f / (1 + w) ** i
    n = len(growth)
    tv = flows[-1] * (1 + g_term) / (w - g_term)
    pv_tv = tv / (1 + w) ** n
    return {"flows": flows, "pv_flows": pv, "tv": tv, "pv_tv": pv_tv,
            "ev": pv + pv_tv, "tv_share": pv_tv / (pv + pv_tv)}


def per_share(ev: float, net_cash: float, shares: float) -> float:
    return (ev + net_cash) / shares


def implied_growth(fcf0: float, target_ev: float, w: float, g_term: float,
                   years: int = 5) -> float:
    """Tăng trưởng đều g trong `years` năm đầu khiến EV mô hình = target_ev (chia đôi)."""
    lo, hi = -0.5, 0.6
    for _ in range(200):
        mid = (lo + hi) / 2
        if dcf(fcf0, [mid] * years, w, g_term)["ev"] < target_ev:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def implied_wacc(fcf0: float, growth: list[float], g_term: float, target_ev: float) -> float:
    """WACC khiến EV mô hình = target_ev, giữ chuỗi tăng trưởng (chia đôi)."""
    lo, hi = g_term + 1e-4, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if dcf(fcf0, growth, mid, g_term)["ev"] > target_ev:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def sensitivity(fcf0, growth, waccs, g_terms, net_cash, shares):
    return {(w, gt): per_share(dcf(fcf0, growth, w, gt)["ev"], net_cash, shares)
            for w in waccs for gt in g_terms}


# ---------- F1: mô hình ba báo cáo (công ty hư cấu) ----------
def three_statement(base: dict, a: dict, years: int = 3) -> list[dict]:
    rows, prev = [], dict(base)
    for _ in range(years):
        s = prev["revenue"] * (1 + a["growth"])
        cogs = s * (1 - a["gross_margin"])
        opex = s * a["opex_pct"]
        dep = prev["ppe"] * a["dep_rate"]
        ebit = s - cogs - opex - dep
        interest = prev["debt"] * a["rate"]
        pbt = ebit - interest
        tax = max(pbt, 0) * a["tax"]
        ni = pbt - tax
        ar, inv, ap = s * a["dso"] / 365, cogs * a["dio"] / 365, cogs * a["dpo"] / 365
        capex = s * a["capex_pct"]
        ppe = prev["ppe"] + capex - dep
        div = ni * a["payout"]
        d_nwc = (ar - prev["ar"]) + (inv - prev["inv"]) - (ap - prev["ap"])
        cfo = ni + dep - d_nwc
        debt = prev["debt"] - a["repay"]
        cash = prev["cash"] + cfo - capex - a["repay"] - div
        equity = prev["equity"] + ni - div
        assets = cash + ar + inv + ppe
        row = dict(revenue=s, cogs=cogs, opex=opex, dep=dep, ebit=ebit, interest=interest,
                   tax=tax, ni=ni, ar=ar, inv=inv, ap=ap, capex=capex, ppe=ppe, div=div,
                   cfo=cfo, debt=debt, cash=cash, equity=equity, assets=assets,
                   check=assets - (ap + debt + equity))
        rows.append(row)
        prev = row
    return rows


# ---------- F2: DDM, RIM, SOTP ----------
def gordon(d1: float, ke: float, g: float) -> float:
    _need_gap(ke, g, "ke")
    return d1 / (ke - g)


def ddm_two_stage(d0: float, g1: float, n: int, g2: float, ke: float) -> float:
    _need_gap(ke, g2, "ke")
    pv, d = 0.0, d0
    for t in range(1, n + 1):
        d *= 1 + g1
        pv += d / (1 + ke) ** t
    return pv + d * (1 + g2) / (ke - g2) / (1 + ke) ** n


def residual_income(b0: float, roe_path: list[float], ke: float, payout: float,
                    g_term_resid: float | None = None) -> dict[str, float]:
    """Giá trị cuối kỳ của thặng dư chỉ được thêm khi truyền g_term_resid; mặc định coi
    thặng dư về 0 sau giai đoạn rõ (ROE hội tụ về ke)."""
    b, pv, resids = b0, 0.0, []
    for t, roe in enumerate(roe_path, 1):
        ni = b * roe
        ri = ni - ke * b
        resids.append(ri)
        pv += ri / (1 + ke) ** t
        b = b + ni * (1 - payout)
    tv = 0.0
    if g_term_resid is not None:
        _need_gap(ke, g_term_resid, "ke")
        tv = resids[-1] * (1 + g_term_resid) / (ke - g_term_resid) / (1 + ke) ** len(roe_path)
    return {"resids": resids, "pv_resid": pv, "pv_tv": tv, "value": b0 + pv + tv}


def sotp(parts: list[tuple[str, float, float]]) -> float:
    return sum(metric * mult for _, metric, mult in parts)


if __name__ == "__main__":
    a = load_apple()
    net_cash = a["Cash and cash equivalents"] + a["Marketable securities - current"] \
        + a["Marketable securities - non-current"] - a["Commercial paper"] \
        - a["Term debt - current"] - a["Term debt - non-current"]
    fcf0 = a["Cash generated by operating activities"] - a["Payments for PP&E"] \
        - a["Share-based compensation"]
    r = dcf(fcf0, [.06, .055, .05, .045, .04], .088, .03)
    print("net cash", net_cash, "FCF0 (đã trừ SBC)", fcf0)
    print("EV", round(r["ev"]), "TV share", round(r["tv_share"], 4),
          "per share", round(per_share(r["ev"], net_cash, a["Shares outstanding (nghin)"] / 1000), 2))
