# Biên bản kiểm duyệt: Bài B3

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-27 10:44 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-27 10:39 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Mẫu lừa đảo, giấy phép, bảo mật, xử lý thiết bị nghi nhiễm và phép tính tình huống.
- Báo cáo đích: `learning/lessons/B3-account-security-scams.md`
- SHA-256 nội dung đích: `6e63d8d9fae5c1b9822cab22b5121f58177d4600d5c8386a7ffc57d316c907f1`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [Bộ Công an — nhóm chat đầu tư](https://mps.gov.vn/bai-viet/canh-bao-thu-doan-lua-dao-thong-qua-cac-hoi-nhom-nhom-chat-dau-tu-chung-khoan-d2-t38878); [25 kịch bản](https://mps.gov.vn/bai-viet/nang-cao-canh-giac-truoc-25-kich-ban-lua-dao-tren-khong-gian-mang-nam-2026-1788865614) | 04/05/2024 và 08/09/2026 | 2026-10-27 | Các mẫu lừa đảo chung |
| [FBI/IC3](https://www.ic3.gov/PSA/2026/PSA260615) | 15/06/2026; Hoa Kỳ | 2026-10-27 | Bằng chứng khi báo cáo |
| [NCSC — phishing](https://www.ncsc.gov.uk/section/respond-recover/phishing); [NCSC — xóa thiết bị](https://www.ncsc.gov.uk/collection/device-security-guidance/managing-deployed-devices/erasing-devices) | Trang đầu không ghi ngày; trang xóa thiết bị rà soát 13/05/2025; Anh | 2026-10-27 | Xử lý thiết bị nghi nhiễm |
| [NCSC — 2SV](https://www.ncsc.gov.uk/guidance/setting-2-step-verification-2sv); [FINRA — mạo danh](https://syndication.finra.org/content/protecting-yourself-regulator-imposter-scams) | NCSC rà soát 10/01/2022; FINRA 29/04/2026 | 2026-10-27 | Bảo mật và thu hồi tiền |
| [UBCKNN — danh sách công ty chứng khoán](https://ssc.gov.vn/cs/idcplg?IdcService=GET_FILE&dDocName=APPSSCGOVVN1620121656&dID=122060&filename=dsach+ctck.pdf) | Dữ liệu đến 15/11/2022 | 2026-10-27 | Kiểm độ mới của danh sách |
| [VNX — danh sách thành viên](https://www.vnx.vn/vi/danh-sach-thanh-vien) | Không ghi ngày chốt | 2026-10-27 | Đối chiếu tư cách thành viên và phạm vi, không thay giấy phép |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Đã xử lý | Thiết bị nghi nhiễm | NCSC hỗ trợ quét và cho biết chỉ gỡ ứng dụng có thể chưa đủ; bản mới dẫn trực tiếp cả hai trang | Hai trang NCSC | Giữ giới hạn nguồn Anh | ĐẠT |
| Chưa biết có chủ đích | Giấy phép và vụ STICCAPITAL | Danh sách UBCKNN mở được là bản 2022; vụ cụ thể theo báo chí. Bản mới không khẳng định đường dẫn danh sách hiện hành | PDF UBCKNN; bảng nguồn bài | Tìm danh sách mới và cảnh báo gốc | CHƯA_BIẾT |
| Không lỗi | Danh sách thành viên VNX | VNX hiển thị thành viên, thị trường; bài phân biệt tư cách thành viên với giấy phép và rủi ro mạo danh | Trang VNX | Giữ giới hạn về ngày dữ liệu và phạm vi | ĐẠT |
| Chưa biết có chủ đích | Điều 91 | Bản mới không diễn giải điều khoản chưa đối chiếu | Bản nháp | Mở văn bản hợp nhất chính thức nếu bổ sung | CHƯA_BIẾT |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Số hiển thị tăng 30%; tổng nạp 80 triệu, phí 5 triệu, nếu nộp phí thì đã chuyển 85 triệu, đã rút 2 triệu đồng; đúng theo kịch bản. IC3 hỗ trợ việc lưu ảnh tin nhắn và thông tin ứng dụng trong bối cảnh báo cáo ở Hoa Kỳ.

## Hạn chế của lần kiểm duyệt

Chưa kiểm hết nguồn thứ cấp, Điều 91 hiện hành và danh sách cấp phép mới. Nhánh kiểm nguồn đã đính chính nhận xét về CISA: nguồn đó không còn trong bản này.

## Kết luận của agent kiểm duyệt

`ĐẠT` trong phạm vi các nhận định bài đang khẳng định. Địa chỉ danh sách giấy phép hiện hành và Điều 91 vẫn `CHƯA_BIẾT`; kết luận không xác nhận các mục đó.
