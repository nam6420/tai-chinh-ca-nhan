# Biên bản kiểm duyệt: F1 — Mô hình ba báo cáo và độ nhạy

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-10-27 12:02 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-27 11:54 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Toàn bài; cầu nối ba báo cáo, phân loại dòng tiền, phép tính và độ nhạy.
- Báo cáo đích: `learning/lessons/F1-three-statement-model-sensitivity.md`
- SHA-256 nội dung đích: `2fe7fb3aa2c168d6b682cdf61926ce8e1920989d063977011f8df6e8c3f69d78`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [IFRS Foundation — IAS 7](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/) | Trang chuẩn IFRS, cập nhật bao gồm sửa đổi 2024 | 27/10/2026 | Dòng tiền và phương pháp gián tiếp |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Không có lỗi | Phương pháp và giả định | Bài nêu giả định lãi/thuế và giới hạn phân loại theo chuẩn; các bảng cân và cầu nối khớp. | IAS 7 và phép tính | Không cần | Đã kiểm |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Lợi nhuận trước thuế 16, thuế 3,2, sau thuế 12,8; CFO 17,8; tiền cuối 15,8; phải thu 25, TSCĐ ròng 65; tài sản 105,8 = nợ 35 + vốn 70,8. Tăng doanh thu 10 theo giả định làm lợi nhuận, tiền và vốn chủ cùng tăng 8 tỷ.

## Hạn chế của lần kiểm duyệt

Mô hình hư cấu một kỳ, không xác nhận chính sách và dữ liệu của doanh nghiệp thật; IFRS 18 có sửa đổi liên quan IAS 7 cần kiểm hiệu lực cho kỳ cụ thể.

## Kết luận của agent kiểm duyệt

`ĐẠT` trong phạm vi đã kiểm; không có lỗi nghiêm trọng chưa xử lý.
