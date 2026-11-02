"""Công cụ sàng lọc chất lượng lợi nhuận (bài Q1): Beneish M-score, Altman Z'', Piotroski F-score.

Chỉ dùng thư viện chuẩn Python 3. Đây là công cụ SÀNG LỌC, không phải bằng chứng gian lận.
Hệ số Beneish lấy từ nguồn thứ cấp (Wikipedia), chưa đối chiếu bài gốc; hệ số Altman Z'' và hằng số 3,25
đã đối chiếu với bản sao Altman (2000), còn cận vùng 2,6/1,1 chỉ có ở Wikipedia.
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


def altman_zpp_em(f) -> float:
    """Biến thể thị trường mới nổi (Wikipedia, mở 2026-11-01): cộng hằng số 3,25 vào Z''; cùng vùng
    2,6 và 1,1 theo trang đó. Hằng số khớp Altman (2000); vùng của biến thể này là CHƯA_BIẾT."""
    return 3.25 + altman_zpp(f)["Z"]


def altman_zone(z: float) -> str:
    if z > ALTMAN_ZPP_SAFE:
        return "an toàn"
    if z < ALTMAN_ZPP_DISTRESS:
        return "nguy cơ"
    return "xám"


# ---------- Piotroski ----------
def piotroski(t, p, lever_def: str = "piotroski") -> dict[str, int]:
    """t, p: năm hiện tại và năm trước; mỗi dict cần 'tong_tai_san_dau' (tổng tài sản đầu kỳ của chính
    năm đó). t BẮT BUỘC có 'phat_hanh_co_phieu' (True nếu công ty phát hành cổ phiếu phổ thông trong
    năm): không có mặc định, vì "không có dữ liệu" khác "không phát hành".
    lever_def="piotroski": LEVER = nợ dài hạn GỒM phần đến hạn (khóa 'vay_dai_han_den_han') / tổng tài sản
    bình quân, theo bảng biến của Piotroski (2000); "hep": chỉ nợ dài hạn (mã 338), lệch khỏi bài gốc."""
    if "phat_hanh_co_phieu" not in t:
        raise KeyError("phat_hanh_co_phieu: cần nguồn cho tín hiệu EQ_OFFER")
    roa = lambda f: f["lai_rong"] / f["tong_tai_san_dau"]
    cfo = lambda f: f["cfo"] / f["tong_tai_san_dau"]
    gm = lambda f: (f["doanh_thu"] - f["gia_von"]) / f["doanh_thu"]
    turn = lambda f: f["doanh_thu"] / f["tong_tai_san_dau"]
    debt = (lambda f: f["vay_dai_han"] + f["vay_dai_han_den_han"]) if lever_def == "piotroski" else (lambda f: f["vay_dai_han"])
    lever = lambda f: debt(f) / ((f["tong_tai_san_dau"] + f["tong_tai_san"]) / 2)
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
        "EQ_OFFER": int(not t["phat_hanh_co_phieu"]),
    }
    s["F_SCORE"] = sum(s.values())
    return s


def hpg_inputs(variant: str = "A", equity_issued: bool = False):
    """Chuyển tệp CSV HPG sang khóa chuẩn. Mã 100 (tài sản ngắn hạn) ĐÃ gồm mã 120 (đầu tư ngắn hạn),
    nên không cộng mã 120 lần nữa vào "chứng khoán" của AQI. Ba cách ánh xạ cho AQI:
      A: chứng khoán = 0, PP&E = mã 221 (mặc định);
      B: chứng khoán = mã 250 (đầu tư tài chính dài hạn), PP&E = mã 221;
      C: chứng khoán = mã 250, PP&E = mã 221 + mã 240 (xây dựng dở dang).
    Beneish không định nghĩa "securities" trên trang đã mở, nên cả ba đều là lựa chọn của người soạn.
    equity_issued: có coi cổ tức bằng cổ phiếu là phát hành cổ phiếu (EQ_OFFER) không.
    Tổng tài sản cuối FY2023 là số báo cáo thường niên 2023 (187.783 tỷ), có thể khác cơ sở trình bày lại."""
    c, p = load_hpg()

    def conv(f):
        ppe = f["tscd_huu_hinh"] + (f["xay_dung_do_dang"] if variant == "C" else 0.0)
        sec = 0.0 if variant == "A" else f["dau_tu_tai_chinh_dai_han"]
        return {"doanh_thu": f["doanh_thu_thuan"], "gia_von": f["gia_von"], "phai_thu": f["phai_thu_khach_hang"],
                "tai_san_ngan_han": f["tai_san_ngan_han"], "ppe": ppe, "chung_khoan": sec,
                "tong_tai_san": f["tong_tai_san"], "khau_hao": f["khau_hao"],
                "sga": f["chi_phi_ban_hang"] + f["chi_phi_quan_ly"], "no_ngan_han": f["no_ngan_han"],
                "vay_dai_han": f["vay_dai_han"], "vay_dai_han_den_han": f["no_dai_han_den_han"], "lai_rong": f["lnst_chung"], "cfo": f["cfo"],
                "loi_nhuan_giu_lai": f["loi_nhuan_chua_phan_phoi"],
                "ebit": f["loi_nhuan_truoc_thue"] + f["chi_phi_lai_vay"], "von_chu": f["von_chu_so_huu"],
                "tong_no": f["tong_tai_san"] - f["von_chu_so_huu"]}
    t, q = conv(c), conv(p)
    t["tong_tai_san_dau"] = q["tong_tai_san"]
    q["tong_tai_san_dau"] = 187783.0
    t["phat_hanh_co_phieu"] = equity_issued
    return t, q


def main() -> None:
    t, p = hpg_inputs()
    b = beneish(t, p)
    print({k: round(v, 4) for k, v in b.items()})
    print({k: round(v, 3) for k, v in beneish_contributions(b).items()})
    z = altman_zpp(t)
    print({k: round(v, 4) for k, v in z.items()}, altman_zone(z["Z"]))
    print(piotroski(t, p))
    for v in "ABC":
        tv, pv = hpg_inputs(v)
        print(v, round(aqi(tv, pv), 4), round(beneish(tv, pv)["M"], 4))


if __name__ == "__main__":
    main()
