"""Lấy và kiểm dữ liệu (bài Q4): XBRL của SEC (EDGAR) và bản chép tay báo cáo Việt Nam.

Chỉ dùng thư viện chuẩn Python 3. Không có kiểm tra nào ở đây là bằng chứng; chúng chỉ phát hiện
chỗ cần mở lại tài liệu gốc.
Chạy: python3 data_pull.py
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import re
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
SEC_BASE = "https://data.sec.gov/api/xbrl"


# ---------- EDGAR / XBRL ----------
MIN_GAP_SECONDS = 0.2  # SEC: tối đa 10 yêu cầu/giây (tổng mọi máy); 0,2 giây chừa biên an toàn
_last_call = 0.0


def fetch_companyfacts(cik: int, user_agent: str, opener=urllib.request.urlopen, sleep=time.sleep,
                       cache: dict | None = None) -> dict:
    """Gọi API companyfacts của SEC. SEC yêu cầu khai tên và liên hệ trong User-Agent, giới hạn
    tần suất (hiện 10 yêu cầu/giây) và không cho công cụ tự động cào cả trang; đọc "Fair Access"
    trên sec.gov trước khi chạy. Hàm này KHÔNG được gọi trong test với mạng thật; truyền
    user_agent của bạn, đừng dùng email của người khác. Cần dữ liệu của nhiều công ty thì tải
    tệp companyfacts.zip thay vì gọi từng công ty."""
    if not re.search(r"\S+@\S+\.\S+", user_agent) or " " not in user_agent.strip():
        raise ValueError("user_agent cần có tên và email liên hệ của bạn, ví dụ 'Ten Ban ten@vidu.com'")
    key = (cik,)
    if cache is not None and key in cache:
        return cache[key]
    global _last_call
    wait = MIN_GAP_SECONDS - (time.monotonic() - _last_call)
    if wait > 0:
        sleep(wait)
    _last_call = time.monotonic()
    req = urllib.request.Request(f"{SEC_BASE}/companyfacts/CIK{cik:010d}.json",
                                 headers={"User-Agent": user_agent})
    with opener(req, timeout=60) as resp:
        data = json.load(resp)
    if cache is not None:
        cache[key] = data
    return data


def load_facts(path: Path | None = None) -> dict:
    with open(path or HERE / "apple_xbrl_subset.json", encoding="utf-8") as fh:
        return json.load(fh)


def rows(facts: dict, tag: str, unit: str = "USD", taxonomy: str = "us-gaap") -> list[dict]:
    return facts["facts"][taxonomy][tag]["units"][unit]


def duration_days(r: dict) -> int | None:
    if "start" not in r:
        return None
    return (dt.date.fromisoformat(r["end"]) - dt.date.fromisoformat(r["start"])).days


def annual_series(facts: dict, tag: str, unit: str = "USD", taxonomy: str = "us-gaap") -> dict[str, float]:
    """Giá trị cả năm theo ngày kết thúc kỳ. Lọc theo độ dài kỳ (350–380 ngày), KHÔNG theo `fy`,
    vì `fy` là năm tài chính của hồ sơ báo cáo chứ không phải của kỳ. Cùng một kỳ xuất hiện trong
    nhiều hồ sơ (10-K, 10-K/A, 10-K năm sau): quy ước ở đây là lấy hồ sơ nộp muộn nhất, hòa thì lấy
    `accn` lớn hơn (chắc chỉ khi cùng một bên nộp); đó chỉ là quy ước (số muộn nhất có thể là số trình bày lại), tùy mục đích có thể
    cần số của hồ sơ gốc. 350–380 ngày là quy ước cho năm 52/53 tuần."""
    best: dict[str, dict] = {}
    for r in rows(facts, tag, unit, taxonomy):
        d = duration_days(r)
        if d is None or not 350 <= d <= 380:
            continue
        if r["end"] not in best or (r["filed"], r.get("accn", "")) > (best[r["end"]]["filed"], best[r["end"]].get("accn", "")):
            best[r["end"]] = r
    return {end: r["val"] for end, r in sorted(best.items())}


def pick_tag(facts: dict, candidates: list[str], unit: str = "USD", taxonomy: str = "us-gaap") -> str:
    """Trong các tag ứng viên, chọn tag có kỳ năm MỚI NHẤT (hòa thì theo thứ tự). Công ty đổi tag
    giữa các thời kỳ: `Revenues` của Apple chỉ có số đến FY2018, doanh thu mới nằm ở tag theo hợp
    đồng khách hàng. Chọn "tag đầu tiên có dữ liệu" sẽ lấy nhầm tag đã ngừng dùng."""
    best_tag, best_end = None, ""
    for tag in candidates:
        if tag not in facts["facts"][taxonomy]:
            continue
        s = annual_series(facts, tag, unit, taxonomy)
        if s and max(s) > best_end:
            best_tag, best_end = tag, max(s)
    if best_tag is None:
        raise KeyError(candidates)
    return best_tag


def conflicting_values(facts: dict, tag: str, unit: str, taxonomy: str = "us-gaap") -> list[tuple]:
    """Các kỳ có nhiều hơn một giá trị khác nhau giữa các hồ sơ (điều chỉnh hồi tố, chia tách...)."""
    by: dict[tuple, set] = {}
    for r in rows(facts, tag, unit, taxonomy):
        by.setdefault((r.get("start"), r["end"]), set()).add(r["val"])
    return sorted((k, sorted(v)) for k, v in by.items() if len(v) > 1)


def ytd_value(facts: dict, tag: str, end: str, days: tuple[int, int], unit: str = "USD") -> float:
    """Giá trị lũy kế từ đầu năm tài chính đến `end` (ví dụ 9 tháng: 265–280 ngày). Cùng quy ước chọn hồ sơ
    như `annual_series` (nộp muộn nhất, hòa thì `accn` lớn hơn) để số cả năm và số lũy kế cùng một cơ sở;
    nếu hai số thuộc hai lần trình bày khác nhau thì quý 4 suy ra có thể sai: kiểm `filed`/`accn` của cả hai."""
    best = None
    for r in rows(facts, tag, unit):
        d = duration_days(r)
        if r["end"] != end or d is None or not days[0] <= d <= days[1]:
            continue
        if best is None or (r["filed"], r.get("accn", "")) > (best["filed"], best.get("accn", "")):
            best = r
    if best is None:
        raise KeyError((tag, end))
    return best["val"]


def derive_q4(fy_value: float, nine_month_value: float) -> float:
    """Báo cáo năm không có số quý 4 riêng: quý 4 = cả năm trừ 9 tháng lũy kế."""
    return fy_value - nine_month_value


def to_millions(value: float) -> float:
    return value / 1e6


# ---------- bản chép tay báo cáo Việt Nam ----------
def load_transcription(path: Path | None = None) -> tuple[dict[str, float], dict[str, float]]:
    cur, prev = {}, {}
    with open(path or HERE / "hpg_fy2025_transcription.csv", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            cur[r["chi_tieu"]] = float(r["FY2025"])
            prev[r["chi_tieu"]] = float(r["FY2024"])
    return cur, prev


def check_identity(name: str, left: float, right: float, tol: float = 1e-5) -> dict:
    """tol tính theo đơn vị đang dùng (tỷ VND). Mặc định 1e-5 tỷ (10.000 đồng) cho số chép đủ 6 chữ số thập phân;
    chỉ nâng lên 0,01 khi so với số đã làm tròn đến 0,01 tỷ (10 triệu đồng)."""
    return {"ten": name, "trai": left, "phai": right, "lech": left - right, "dat": abs(left - right) <= tol}


def statement_checks(f: dict[str, float], tol: float = 1e-5) -> list[dict]:
    return [
        check_identity("tài sản = nợ phải trả + vốn chủ", f["tong_tai_san"], f["no_phai_tra"] + f["von_chu_so_huu"], tol),
        check_identity("tiền cuối năm: bảng cân đối = lưu chuyển tiền tệ", f["tien_cuoi_nam_bang_can_doi"], f["tien_cuoi_nam_luu_chuyen"], tol),
        check_identity("lợi nhuận sau thuế = trước thuế − thuế hiện hành − thuế hoãn lại",
                       f["lnst"], f["loi_nhuan_truoc_thue"] - f["thue_hien_hanh"] - f["thue_hoan_lai"], tol),
        check_identity("lợi nhuận mẹ + không kiểm soát = lợi nhuận sau thuế",
                       f["lnst"], f["lnst_cong_ty_me"] + f["lnst_co_dong_khong_kiem_soat"], tol),
        check_identity("lợi nhuận gộp = doanh thu thuần − giá vốn", f["loi_nhuan_gop"], f["doanh_thu_thuan"] - f["gia_von"], tol),
    ]


def main() -> None:
    facts = load_facts()
    for tag in ("NetIncomeLoss", "ShareBasedCompensation", "PaymentsForRepurchaseOfCommonStock"):
        print(tag, {k: round(to_millions(v)) for k, v in annual_series(facts, tag).items() if k >= "2023"})
    cur, prev = load_transcription()
    for year, f in (("FY2025", cur), ("FY2024", prev)):
        for c in statement_checks(f):
            print(year, c["ten"], "ĐẠT" if c["dat"] else f"LỆCH {c['lech']:.3f}")


if __name__ == "__main__":
    main()
