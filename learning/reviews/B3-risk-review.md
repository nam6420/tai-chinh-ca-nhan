# Biên bản kiểm duyệt: Bài B3

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-10-27 10:40 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-27 10:39 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Toàn bài; phản biện lời khuyên thu hồi tiền, xử lý khẩn cấp, bảo mật và bài tập.
- Báo cáo đích: `learning/lessons/B3-account-security-scams.md`
- SHA-256 nội dung đích: `6e63d8d9fae5c1b9822cab22b5121f58177d4600d5c8386a7ffc57d316c907f1`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [FINRA — Mạo danh cơ quan quản lý](https://www.finra.org/investors/insights/regulator-imposter-scams) | Bài nháp ghi 29/04/2026; ngày không hiện trong phần đã mở | 2026-10-27 | Lừa đảo thu hồi tiền, phí trả trước |
| [NCSC — Phishing](https://www.ncsc.gov.uk/section/respond-recover/phishing) | Ngày xuất bản không hiện trong phần đã mở | 2026-10-27 | Quét thiết bị và liên hệ ngân hàng khi lộ thông tin |
| [NCSC — Xóa thiết bị](https://www.ncsc.gov.uk/collection/device-security-guidance/managing-deployed-devices/erasing-devices) | Rà soát 13/05/2025; Anh | 2026-10-27 | Giới hạn của việc gỡ ứng dụng |
| [Bộ Công an — nhóm chat](https://mps.gov.vn/bai-viet/canh-bao-thu-doan-lua-dao-thong-qua-cac-hoi-nhom-nhom-chat-dau-tu-chung-khoan-d2-t38878) | 04/05/2024 | 2026-10-27 | Thủ đoạn lừa đảo đầu tư |
| [VNX — Danh sách thành viên](https://www.vnx.vn/vi/danh-sach-thanh-vien) | Không thấy ngày cập nhật | 2026-10-27 | Phạm vi tư cách thành viên và thị trường |
| [Luật Chứng khoán — Cổng Chính phủ](https://vanban.chinhphu.vn/?docid=198541&pageid=27160) | 26/11/2019; hiệu lực 01/01/2021 | 2026-10-27 | Thử kiểm Điều 91; PDF không trích được điều khoản |
| [UBCKNN — Cảnh báo giả danh](https://ssc.gov.vn/webcenter/portal/ubck/pages_r/l/chitit?dDocName=APPSSCGOVVN1620152970) | 17/03/2025 theo kết quả tìm kiếm | 2026-10-27 | Thử kiểm tra giấy phép và báo công an; trang trả nội dung động không đọc được |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Không còn mở | Lời mời thu hồi tiền | Bản mới thu hẹp câu khái quát thành cảnh giác với lời mời không mong muốn, tự kiểm chứng kênh hỗ trợ | FINRA mô tả lừa đảo thu hồi tiền và phí trả trước | Không cần sửa thêm trong phạm vi phản biện | Đã xử lý |
| Đã xử lý | Thiết bị bị can thiệp | Bài nói gỡ ứng dụng có thể chưa đủ, dùng thiết bị tin cậy và nêu hướng dẫn quét/làm sạch của NCSC | NCSC — Phishing | Giữ hướng dẫn tham khảo và giới hạn nguồn Anh | Đã xử lý |
| Đã xử lý | Danh sách VNX | Danh sách thành viên được nêu như đối chiếu bổ sung, không thay giấy phép UBCKNN và không loại trừ mạo danh | VNX | Giữ phân biệt hai loại danh sách | Đã xử lý |
| Đã xử lý | Giấy phép và Điều 91 | Bản mới giữ địa chỉ danh sách giấy phép và hiệu lực Điều 91 ở `CHƯA_BIẾT`, không khẳng định nội dung pháp lý chưa đối chiếu | VNX và hồ sơ Luật trên Cổng Chính phủ | Giữ giới hạn | Đã xử lý trong phạm vi rủi ro |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Phép tính tình huống đã rà không đổi; không phát hiện lỗi số học. Phân biệt lời mời không mong muốn với kênh tự xác minh giúp tránh làm người bị hại né mọi hỗ trợ.

## Hạn chế của lần kiểm duyệt

Không kiểm từng trích dẫn, pháp luật ngân hàng hay thủ tục tra soát. Trang UBCKNN chỉ trả nội dung động; nhánh phản biện dùng kết quả tìm kiếm cho phần cảnh báo nên không coi đó là bằng chứng trực tiếp trong biên bản này. Chưa xác minh thủ tục ngân hàng cụ thể.

## Kết luận của agent kiểm duyệt

`ĐẠT` trong phạm vi phản biện rủi ro; không thay cho kiểm nguồn toàn bài.
