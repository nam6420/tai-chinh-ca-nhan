# Biên bản kiểm duyệt: Bài V5 — Chỉ số, room ngoại và nâng hạng

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-10-27 11:12 UTC+7`
- Chốt dữ liệu lúc: `2026-10-27 11:09 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Phân loại thị trường, điều kiện từng mã, room, dòng vốn, giả định và phép tính.
- Báo cáo đích: `learning/lessons/V5-index-foreign-room-upgrade.md`
- SHA-256 nội dung đích: `2d3bfe38c78f26012f8e69277ae6139d4042f56fc75c697317134ec209715636`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [FTSE — kết quả phân loại](https://www.lseg.com/en/media-centre/press-releases/ftse-russell/2026/ftse-country-classification-review-september-2026) | 06/10/2026 | 27/10/2026 | Xác nhận hiệu lực 21/09 |
| [FTSE FAQ v1.3](https://www.lseg.com/content/dam/ftse-russell/en_us/documents/policy-documents/ftse-faq-document-vietnam-reclassification.pdf) | 08/2026 | 27/10/2026 | Sàng lọc và các đợt |
| [MSCI — accessibility review](https://www.msci.com/downloads/web/msci-com/indexes/index-resources/market-classification/MSCI%202026%20GLOBAL%20MARKET%20ACCESSIBILITY%20REVIEW%20REPORT.pdf) | 06/2026; dữ liệu đến 31/05 | 27/10/2026 | Hạn chế sở hữu nước ngoài |
| [World Bank — Equity Upgrade](https://www.worldbank.org/en/news/feature/2026/10/09/viet-nam-equity-upgrade-takes-off) | 09/10/2026 | 27/10/2026 | Giới hạn dự báo dòng vốn |
| [VSDC — tỷ lệ sở hữu nước ngoài](https://vsdc.vn/vi/alc/82) | Công bố theo ngày | 27/10/2026 | Ngày dữ liệu room |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Trung bình | Quy mô hạn chế room | Bài chưa đưa bằng chứng MSCI về mức ảnh hưởng toàn thị trường: giới hạn sở hữu ảnh hưởng hơn 10% thị trường Việt Nam và room thấp ảnh hưởng hơn 1% MSCI Vietnam IMI, theo phương pháp và dữ liệu đến 31/05/2026. Không thể ngoại suy thành room hiện tại của một mã. | MSCI review 06/2026 | Bổ sung bằng chứng theo kỳ hoặc giải thích phạm vi; kiểm room từng mã/ngày trước khi áp dụng. | Còn mở; không nghiêm trọng |
| Không có lỗi | FTSE | Nguồn sau sự kiện xác nhận ngày hiệu lực; câu mới tách suy luận không phải mọi mã tự vào rổ. | Thông báo FTSE và FAQ | Không cần | Đã xử lý |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

10 + 20 + 35 + 35 = 100%, hai đợt đầu 30%; đây là tỷ lệ trọng số đầu tư, không phải lợi suất. 40 − 35 = 5 triệu cổ phiếu trong giả định. World Bank dự báo dòng vốn, không xác nhận tiền đã vào.

## Hạn chế của lần kiểm duyệt

Chưa kiểm room từng mã, danh sách thực tế trong rổ hoặc dòng vốn thực tế. MSCI là dữ liệu lịch sử đến 31/05/2026.

## Kết luận của agent kiểm duyệt

`ĐẠT` trên bản hiện tại; không có lỗi nghiêm trọng, giữ điểm trung bình còn mở nêu trên.
