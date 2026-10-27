# Dữ liệu

- `raw/`: manifest, link, checksum và bản gốc bất biến nếu kích thước/quyền cho phép.
- `processed/`: dữ liệu đã làm sạch/chuyển đổi kèm script, công thức hoặc mô tả provenance.
- Dữ liệu lớn cục bộ đặt trong `raw/payloads/` hoặc `processed/payloads/` (được Git ignore); manifest/checksum/provenance vẫn phải commit bên ngoài thư mục `payloads/`.

Không commit credential, dữ liệu tài khoản môi giới, thông tin cá nhân nhạy cảm hoặc dataset không có quyền lưu trữ.


## Dữ liệu hỗ trợ giáo trình26/10/2026

- [Mẫu quan sát vĩ mô](processed/macro-observation-template.md): mẫu trống, chưa dữ liệu, không tự cập nhật.
- [Bảng vĩ mô lịch sử của008](raw/macro-lesson-008-legacy-2026-10-26.md): giữ nguyên để truy dấu, chưa xác minh lại trong lượt chỉnh giáo trình; không dùng làm hiện trạng.
- [Phản hồi công cụ khi mở nguồn](raw/lesson-source-responses-2026-10-26.json): bản trích thu thập, có cả lỗi truy cập, không phải toàn văn nguồn.
- [Đầu vào Apple và phép tính](processed/apple-fy2025-learning-calculations.md): số lịch sử riêng với mô hình hư cấu; giữ dấu và đơn vị gốc, công thức rõ.

Nguồn bài mới còn ở sổ nguồn cuối từng bài và26biên bản trong `learning/reviews/`. Không có dữ liệu tài khoản hay giao dịch cá nhân.
