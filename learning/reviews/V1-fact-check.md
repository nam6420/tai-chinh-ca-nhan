# Biên bản kiểm duyệt: Bài V1

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-27 10:44 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-27 10:41 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Cơ quan và sở giao dịch, UPCoM, chuyển sàn, dự thảo sửa luật và FTSE.
- Báo cáo đích: `learning/lessons/V1-vietnam-market-structure.md`
- SHA-256 nội dung đích: `17e384b64beb1af4c05fe5ea298322b821a28d0782edf55d8112a9d16e016188`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [VNX — lịch sử](https://www.vnx.vn/vi/lich-su-phat-trien); [chức năng](https://vnx.vn/vi/chuc-nang-nhiem-vu) | Trang chính thức; không ghi ngày sửa | 2026-10-27 | Mô hình sở hữu và phân vai |
| [VNX — danh mục](https://vnx.vn/vi/van-ban-phap-ly/6); [QĐ 23/2026](https://stream.vnx.vn/VNX//Legal/20260324164637497VNX.-Quy-che-CK-CNY_QD23....pdf) | Hiệu lực 18/03/2026 | 2026-10-27 | Metadata và ảnh gốc về UPCoM |
| [VNX — lịch chuyển sàn](https://vnx.vn/vi/thong-tin-tu-sgdck/VNX_QLHD/10005424) | 30/09/2026 | 2026-10-27 | Mốc và phạm vi chuyển giao |
| [VSDC — đăng ký](https://vsdc.vn/vi/sd/5YN8KJbNJhbnPYBYIu6YXw); [lưu ký](https://vsdc.vn/vi/sd/rft7xrkuPfGyGNk-dm6arA); [Quỹ hỗ trợ thanh toán](https://vsdc.vn/vi/alc/86) | Trang dịch vụ và báo cáo quỹ năm 2026 | 2026-10-27 | Các vai trò khái quát và công bố về quỹ |
| [Thông tư 145/2026](https://vanban.chinhphu.vn/?docid=219758&pageid=27160); [Cổng Chính phủ — tóm tắt](https://xaydungchinhsach.chinhphu.vn/mot-so-noi-dung-chinh-cua-thong-tu-145-2026-tt-btc-quy-dinh-hoat-dong-dang-ky-luu-ky-bu-tru-va-thanh-toan-giao-dich-chung-khoan-119261005165752419.htm) | Ban hành 30/09/2026; hiệu lực 16/11/2026 | 2026-10-27 | Mốc thay thế TT119 và giới hạn chuyển tiếp |
| [Thông tư 139/2025 — PDF gốc](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/139-btc.pdf) | Ban hành, hiệu lực 30/12/2025 | 2026-10-27 | Ảnh trang 2: hạn chuyển giao 31/12/2026 và ngày hiệu lực |
| [FTSE Russell — FAQ v1.3](https://www.lseg.com/content/dam/ftse-russell/en_us/documents/policy-documents/ftse-faq-document-vietnam-reclassification.pdf) | 08/2026 | 2026-10-27 | Tỷ lệ và cơ chế các đợt |
| [Báo Điện tử Chính phủ — dự thảo sửa luật](https://baochinhphu.vn/sua-doi-bo-sung-3-du-an-luat-theo-huong-cat-giam-cac-dieu-kien-kinh-doanh-don-gian-hoa-thu-tuc-hanh-chinh-102261017164446458.htm) | 17/10/2026 | 2026-10-27 | Trình dự thảo |
| [Ngân hàng Thế giới](https://www.worldbank.org/en/news/feature/2026/10/09/viet-nam-equity-upgrade-takes-off) | 09/10/2026 | 2026-10-27 | Bối cảnh vốn hữu hạn và cổ phiếu lớn |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Đã xử lý | UPCoM, nguồn FTSE | Đáp án UPCoM đã đồng bộ với QĐ23; FAQ v1.3 xác nhận các đợt, không còn nói chỉ có nguồn thứ cấp | VNX, FTSE | Giữ nguồn gốc | ĐẠT |
| Đã xử lý | Ngày 31/12/2026 | Ảnh trang 2 Thông tư 139 xác nhận hạn chuyển giao 31/12/2026 và ngày hiệu lực 30/12/2025 | PDF gốc | Giữ nguồn gốc | ĐẠT |
| Đã xử lý | Số liệu mã và vốn hóa | Các số chưa tái tính được bỏ khỏi khẳng định; số UPCoM hiện hành giữ chưa biết | Bản nháp; Vietstock | Đối chiếu dữ liệu HNX/VNX nếu bổ sung | ĐẠT trong phạm vi hiện tại |
| Trung bình | Luật, quỹ, CCP, sự cố | Chưa kiểm toàn văn và các thông báo gốc liên quan | Giới hạn lượt kiểm | Đối chiếu văn bản và thông báo trực tiếp | CHƯA_BIẾT |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Tỷ lệ thêm trọng số FTSE 10%+20%+35%+35%=100%; đã đối chiếu FAQ gốc. Chưa tái tính 299 mã hay tổng vốn hóa.

## Hạn chế của lần kiểm duyệt

Chưa kiểm toàn văn Luật 54/2019, Luật 56/2024, số liệu thị trường, sự cố thanh toán và chi tiết các quỹ. Đã xem ảnh trang 2 Thông tư 139 và trang gốc Điều 15 của Quy chế 23; nhánh kiểm nguồn đã rút lại nhận xét cũ về mâu thuẫn UPCoM và FTSE sau khi đọc đúng bản.

## Kết luận của agent kiểm duyệt

`ĐẠT` cho các nhận định đang khẳng định trong phạm vi kiểm; quan hệ pháp lý chi tiết giữa các quỹ và điều khoản chuyển tiếp vẫn `CHƯA_BIẾT`.
