# Biên bản kiểm duyệt: F4 — Ngân hàng Việt Nam

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-27 12:03 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-27 11:58 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Toàn bài, nguồn, kỳ dữ liệu, giả định và phép tính; kiểm lại bản cập nhật nếu có.
- Báo cáo đích: `learning/lessons/F4-vietnam-bank-analysis.md`
- SHA-256 nội dung đích: `4cbad2b67bbf16568fe8573b958288f25e1a2a781ce2138c115eab999cd9fe7e`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [Techcombank — báo cáo 2025](https://techcombank.com/content/dam/techcombank/public-site/documents/bao-cao-ket-qua-kinh-doanh-2025-ke-hoach-2026-eng.pdf) | 03/04/2026, kỳ 2025 | 27/10/2026 | NPL được ngân hàng công bố |
| [TT31/2024](https://vanban.chinhphu.vn/?classid=1&docid=210625&pageid=27160) | Hiệu lực 01/07/2024 | 27/10/2026 | Phân loại tài sản có, metadata |
| [TT37/2025](https://vanban.chinhphu.vn/?classid=1&docid=215867&pageid=27160&typegroupid=6) | Hiệu lực 15/12/2025 | 27/10/2026 | Sửa đổi TT31 |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Không có lỗi | Phạm vi và diễn giải | Các số, nguồn và phép tính khớp phạm vi đã kiểm; các giới hạn cụ thể được công khai. | Các nguồn trên | Kiểm thêm hồ sơ cụ thể trước áp dụng. | Đã kiểm |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

NIM 40/1.000 = 4%; CIR 30/100 = 30%; NPL 20/1.000 = 2%; độ bao phủ 15/20 = 75%.

## Hạn chế của lần kiểm duyệt

Toàn văn TT31 chưa được nhánh kiểm nguồn mở; bài để công thức pháp lý cụ thể CHƯA_BIẾT. Số TCB là công bố ngân hàng, không tái lập từ bảng nhóm nợ gốc.

## Kết luận của agent kiểm duyệt

`ĐẠT` trong phạm vi đã kiểm; không có lỗi nghiêm trọng chưa xử lý.
