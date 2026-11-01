"""Công cụ sàng lọc chất lượng lợi nhuận (bài Q1): Beneish M-score, Altman Z'', Piotroski F-score.

Chỉ dùng thư viện chuẩn Python 3. Đây là công cụ SÀNG LỌC, không phải bằng chứng gian lận.
Hệ số Beneish và Altman lấy từ nguồn thứ cấp (Wikipedia, mở 2026-11-01), chưa đối chiếu bài gốc.
Số HPG FY2025 nằm trong hpg_fy2025_statements.csv (tỷ VND).
Chạy: python3 earnings_quality.py
"""
from __future__ import annotations

import csv
from pathlib import Path

HERE = Path(__file__).parent

BENEISH_CUTOFF = -1.78
ALTMAN_ZPP_SAFE, ALTMAN_ZPP_DISTRESS = 2.6, 1.1


def load_hpg() -> tuple[dict[str, float], dict[str, float]]:
    """Trả về (năm hiện tại FY2025, năm trước FY2024) theo tên chỉ tiêu."""
    cur, prev = {}, {}
    with open(HERE / "hpg_fy2025_statements.csv", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            cur[r["chi_tieu"]] = float(r["FY2025"])
            prev[r["chi_tieu"]] = float(r["FY2024"])
    return cur, prev


# ---------- Beneish ----------
def dsri(t, p) -> float:
    return (t["phai_thu"] / t["doanh_thu"]) / (p["phai_thu"] / p["doanh_thu"])


def gmi(t, p) -> float:
    gm = lambda f: (f["doanh_thu"] - f["gia_von"]) / f["doanh_thu"]
    return gm(p) / gm(t)


def aqi(t, p) -> float:
    q = lambda f: 1 - (f["tai_san_ngan_han"] + f["ppe"] + f["chung_khoan"]) / f["tong_tai_san"]
    return q(t) / q(p)


def sgi(t, p) -> float:
    return t["doanh_thu"] / p["doanh_thu"]


def depi(t, p) -> float:
    rate = lambda f: f["khau_hao"] / (f["ppe"] + f["khau_hao"])
    return rate(p) / rate(t)


def sgai(t, p) -> float:
    r = lambda f: f["sga"] / f["doanh_thu"]
    return r(t) / r(p)


def lvgi(t, p) -> float:
    lv = lambda f: (f["no_ngan_han"] + f["vay_dai_han"]) / f["tong_tai_san"]
    return lv(t) / lv(p)


def tata(t) -> float:
    return (t["lai_rong"] - t["cfo"]) / t["tong_tai_san"]


def beneish(t, p) -> dict[str, float]:
    v = {"DSRI": dsri(t, p), "GMI": gmi(t, p), "AQI": aqi(t, p), "SGI": sgi(t, p),
         "DEPI": depi(t, p), "SGAI": sgai(t, p), "LVGI": lvgi(t, p), "TATA": tata(t)}
    v["M"] = (-4.84 + 0.92 * v["DSRI"] + 0.528 * v["GMI"] + 0.404 * v["AQI"] + 0.892 * v["SGI"]
              + 0.115 * v["DEPI"] - 0.172 * v["SGAI"] + 4.679 * v["TATA"] - 0.327 * v["LVGI"])
    return v


def beneish_contributions(v: dict[str, float]) -> dict[str, float]:
    """Đóng góp của từng biến vào M (hệ số × giá trị), để thấy biến nào đẩy điểm lên."""
    w = {"DSRI": 0.92, "GMI": 0.528, "AQI": 0.404, "SGI": 0.892, "DEPI": 0.115,
         "SGAI": -0.172, "TATA": 4.679, "LVGI": -0.327}
    return {k: w[k] * v[k] for k in w}


# ---------- Altman Z'' (không sản xuất / thị trường mới nổi, dùng vốn chủ sổ sách) ----------
def altman_zpp(f) -> dict[str, float]:
    x1 = (f["tai_san_ngan_han"] - f["no_ngan_han"]) / f["tong_tai_san"]
    x2 = f["loi_nhuan_giu_lai"] / f["tong_tai_san"]
    x3 = f["ebit"] / f["tong_tai_san"]
    x4 = f["von_chu"] / f["tong_no"]
    return {"X1": x1, "X2": x2, "X3": x3, "X4": x4,
            "Z": 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4}


def altman_zone(z: float) -> str:
    if z > ALTMAN_ZPP_SAFE:
        return "an toàn"
    if z < ALTMAN_ZPP_DISTRESS:
        return "nguy cơ"
    return "xám"


# ---------- Piotroski ----------
def piotroski(t, p) -> dict[str, int]:
    """t, p: năm hiện tại và năm trước; p cần thêm 'tong_tai_san_dau' (tổng tài sản đầu kỳ của p).
    t['tong_tai_san_dau'] = tổng tài sản cuối năm trước. Mọi chỉ tiêu theo định nghĩa Piotroski (2000)."""
    roa = lambda f: f["lai_rong"] / f["tong_tai_san_dau"]
    cfo = lambda f: f["cfo"] / f["tong_tai_san_dau"]
    gm = lambda f: (f["doanh_thu"] - f["gia_von"]) / f["doanh_thu"]
    turn = lambda f: f["doanh_thu"] / f["tong_tai_san_dau"]
    lever = lambda f: f["vay_dai_han"] / ((f["tong_tai_san_dau"] + f["tong_tai_san"]) / 2)
    cur = lambda f: f["tai_san_ngan_han"] / f["no_ngan_han"]
    s = {
        "F_ROA": int(roa(t) > 0),
        "F_CFO": int(cfo(t) > 0),
        "F_dROA": int(roa(t) > roa(p)),
        "F_ACCRUAL": int(cfo(t) > roa(t)),
        "F_dMARGIN": int(gm(t) > gm(p)),
        "F_dTURN": int(turn(t) > turn(p)),
        "F_dLEVER": int(lever(t) < lever(p)),
        "F_dLIQUID": int(cur(t) > cur(p)),
        "EQ_OFFER": int(not t.get("phat_hanh_co_phieu", False)),
    }
    s["F_SCORE"] = sum(s.values())
    return s


def hpg_inputs():
    """Chuyển tệp CSV HPG sang khóa chuẩn của các hàm trên. Tổng tài sản cuối FY2023 là số
    trong báo cáo thường niên 2023 (187.783 tỷ), có thể khác cơ sở trình bày lại của FY2024."""
    c, p = load_hpg()
    def conv(f):
        return {"doanh_thu": f["doanh_thu_thuan"], "gia_von": f["gia_von"], "phai_thu": f["phai_thu_khach_hang"],
                "tai_san_ngan_han": f["tai_san_ngan_han"], "ppe": f["tscd_huu_hinh"],
                "chung_khoan": f["dau_tu_tai_chinh_ngan_han"], "tong_tai_san": f["tong_tai_san"],
                "khau_hao": f["khau_hao"], "sga": f["chi_phi_ban_hang"] + f["chi_phi_quan_ly"],
                "no_ngan_han": f["no_ngan_han"], "vay_dai_han": f["vay_dai_han"], "lai_rong": f["lnst_chung"],
                "cfo": f["cfo"], "loi_nhuan_giu_lai": f["loi_nhuan_chua_phan_phoi"],
                "ebit": f["loi_nhuan_truoc_thue"] + f["chi_phi_lai_vay"], "von_chu": f["von_chu_so_huu"],
                "tong_no": f["tong_tai_san"] - f["von_chu_so_huu"]}
    t, q = conv(c), conv(p)
    t["tong_tai_san_dau"] = q["tong_tai_san"]
    q["tong_tai_san_dau"] = 187783.0
    return t, q


def main() -> None:
    t, p = hpg_inputs()
    b = beneish(t, p)
    print({k: round(v, 4) for k, v in b.items()})
    print({k: round(v, 3) for k, v in beneish_contributions(b).items()})
    z = altman_zpp(t)
    print({k: round(v, 4) for k, v in z.items()}, altman_zone(z["Z"]))
    print(piotroski(t, p))


if __name__ == "__main__":
    main()
