# Biên bản kiểm duyệt: Bài V5 — Chỉ số, room ngoại và nâng hạng

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-27 11:10 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-10-27 11:09 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Phân loại FTSE/MSCI, lộ trình, room ngoại, nhận định World Bank, phép tính và giới hạn dữ liệu.
- Báo cáo đích: `learning/lessons/V5-index-foreign-room-upgrade.md`
- SHA-256 nội dung đích: `2d3bfe38c78f26012f8e69277ae6139d4042f56fc75c697317134ec209715636`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [FTSE — kết quả phân loại](https://www.lseg.com/en/media-centre/press-releases/ftse-russell/2026/ftse-country-classification-review-september-2026) | 06/10/2026 | 27/10/2026 | Xác nhận hiệu lực 21/09/2026 |
| [FTSE — FAQ v1.3](https://www.lseg.com/content/dam/ftse-russell/en_us/documents/policy-documents/ftse-faq-document-vietnam-reclassification.pdf) | 08/2026 | 27/10/2026 | Lộ trình và sàng lọc room |
| [FTSE — rà soát giữa kỳ](https://www.lseg.com/en/media-centre/press-releases/ftse-russell/2026/ftse-russell-announces-results-march-2026-semi-annual-country-classification-review-equities-fixed-income) | 07/04/2026; kỳ 03/2026 | 27/10/2026 | Cải cách tiếp cận |
| [MSCI — accessibility review](https://www.msci.com/downloads/web/msci-com/indexes/index-resources/market-classification/MSCI%202026%20GLOBAL%20MARKET%20ACCESSIBILITY%20REVIEW%20REPORT.pdf) | 06/2026 | 27/10/2026 | Việt Nam theo kỳ báo cáo |
| [MSCI — classification review](https://ir.msci.com/news-releases/news-release-details/msci-announces-results-msci-2026-market-classification-review) | 23/06/2026 | 27/10/2026 | Đối chiếu kết quả phân loại |
| [World Bank — Equity Upgrade](https://www.worldbank.org/en/news/feature/2026/10/09/viet-nam-equity-upgrade-takes-off) | 09/10/2026 | 27/10/2026 | Dự báo và giới hạn dòng vốn |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Không có lỗi | FTSE và room | Thông báo 06/10 xác nhận hiệu lực 21/09; FAQ xác nhận các đợt và sàng lọc foreign headroom. Không phải mọi mã tự vào rổ là `SUY_LUẬN`. | Hai tài liệu FTSE | Không cần | Đã kiểm |
| Không có lỗi | MSCI và dòng vốn | MSCI được giới hạn theo kỳ tháng 06; nhận định của World Bank là dự báo. | MSCI và World Bank | Không cần | Đã kiểm |
| Giới hạn | Chỉ số, room từng mã | Chưa kiểm phương pháp VN-Index/VN30, room của mã cụ thể hoặc dòng vốn thực tế. | Mục `CHƯA_BIẾT` | Kiểm tại thời điểm sử dụng. | Còn mở |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

10% + 20% + 35% + 35% = 100%; sau hai đợt 30%; room giả định 40 − 35 = 5 triệu cổ phiếu. Phần trăm là tỷ lệ trọng số đầu tư theo FTSE, không phải lợi suất hay dòng vốn chắc chắn.

## Hạn chế của lần kiểm duyệt

Không xác minh room hoặc trọng số từng mã, dòng vốn sau từng đợt hay tình trạng sau kỳ của báo cáo MSCI. Dự báo World Bank không là tiền thực nhận.

## Kết luận của agent kiểm duyệt

`ĐẠT` trong phạm vi đã kiểm; không có lỗi nghiêm trọng chưa xử lý.
