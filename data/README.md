# Dữ liệu

- `raw/`: manifest, link, checksum và bản gốc bất biến nếu kích thước/quyền cho phép.
- `processed/`: dữ liệu đã làm sạch/chuyển đổi kèm script, công thức hoặc mô tả provenance.
- Dữ liệu lớn cục bộ đặt trong `raw/payloads/` hoặc `processed/payloads/` (được Git ignore); manifest/checksum/provenance vẫn phải commit bên ngoài thư mục `payloads/`.

Không commit credential, dữ liệu tài khoản môi giới, thông tin cá nhân nhạy cảm hoặc dataset không có quyền lưu trữ.
