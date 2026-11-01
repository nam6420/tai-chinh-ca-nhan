# Mô hình thực hành

Chỉ dùng thư viện chuẩn Python 3. Chạy `python3 valuation.py`; kiểm bằng `python3 -m unittest discover tests` ở thư mục gốc.

- `apple_fy2025_inputs.csv`: số lịch sử từ Form 10-K Apple FY2025 (triệu USD), mở 2026-10-31.
- `valuation.py`: chi phí vốn (010), DCF và định giá ngược (011), kịch bản (012), ba báo cáo hư cấu (F1), DDM/RIM/SOTP (F2).
- Mọi giả định tương lai là giả định bài học, không phải dự báo. Chưa có bảng tính Excel: người học dựng lại công thức theo hàm trong tệp.
- `hpg_cycle_inputs.csv`: doanh thu, lợi nhuận, vốn chủ HPG FY2021–FY2025 (tỷ VND; trộn báo cáo thường niên 2023 và BCTC kiểm toán FY2025), mở 2026-11-01.
- `cyclical.py`: chuẩn hóa lợi nhuận công ty chu kỳ (bài Q3): trung bình tuyệt đối, biên, trung vị, bỏ năm cực đoan, ROE, chiết khấu lùi.
