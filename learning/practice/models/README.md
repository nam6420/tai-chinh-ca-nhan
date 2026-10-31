# Mô hình thực hành

Chỉ dùng thư viện chuẩn Python 3. Chạy `python3 valuation.py`; kiểm bằng `python3 -m unittest discover tests` ở thư mục gốc.

- `apple_fy2025_inputs.csv`: số lịch sử từ Form 10-K Apple FY2025 (triệu USD), mở 2026-10-31.
- `valuation.py`: chi phí vốn (010), DCF và định giá ngược (011), kịch bản (012), ba báo cáo hư cấu (F1), DDM/RIM/SOTP (F2).
- Mọi giả định tương lai là giả định bài học, không phải dự báo. Chưa có bảng tính Excel: người học dựng lại công thức theo hàm trong tệp.
