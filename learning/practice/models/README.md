# Mô hình thực hành

Chỉ dùng thư viện chuẩn Python 3. Chạy `python3 valuation.py`; kiểm bằng `python3 -m unittest discover tests` ở thư mục gốc.

- `apple_fy2025_inputs.csv`: số lịch sử từ Form 10-K Apple FY2025 (triệu USD), mở 2026-10-31.
- `valuation.py`: chi phí vốn (010), DCF và định giá ngược (011), kịch bản (012), ba báo cáo hư cấu (F1), DDM/RIM/SOTP (F2).
- Mọi giả định tương lai là giả định bài học, không phải dự báo. Chưa có bảng tính Excel: người học dựng lại công thức theo hàm trong tệp.
- `hpg_cycle_inputs.csv`: doanh thu, lợi nhuận, vốn chủ HPG FY2021–FY2025 (tỷ VND; trộn báo cáo thường niên 2023 và BCTC kiểm toán FY2025), mở 2026-11-01.
- `cyclical.py`: chuẩn hóa lợi nhuận công ty chu kỳ (bài Q3): trung bình tuyệt đối, biên, trung vị, bỏ năm cực đoan, ROE, chiết khấu lùi.
- `hpg_fy2025_statements.csv`: số báo cáo tài chính hợp nhất kiểm toán FY2025 và cột năm trước của HPG (tỷ VND), mở 2026-11-01.
- `earnings_quality.py`: Beneish M-score, Altman Z'', Piotroski F-score (bài Q1). Hệ số Beneish/Altman từ nguồn thứ cấp, chưa đối chiếu bài gốc.
- `apple_capital_return_inputs.csv`: SBC, mua lại, cổ tức, số cổ phiếu và EPS của Apple FY2023–FY2025 (triệu USD; cổ phiếu nghìn), mở 2026-11-01.
- `capital_return.py`: SBC, pha loãng, mua lại (EPS và giá trị mỗi cổ phiếu), cổ tức, cổ phiếu thưởng (bài Q2).
- `apple_xbrl_subset.json`: tập con 14 tag của companyfacts Apple (SEC), tải 2026-11-01, giữ nguyên giá trị, để chạy offline.
- `hpg_fy2025_transcription.csv`: bản chép 14 chỉ tiêu báo cáo HPG FY2025/FY2024 (tỷ VND) cho các phép kiểm đẳng thức.
- `data_pull.py`: gọi companyfacts (cần User-Agent của bạn), lọc kỳ, chọn tag, quý 4 suy ra, kiểm đẳng thức (bài Q4).
