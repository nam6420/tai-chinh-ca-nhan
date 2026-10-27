# Biên bản kiểm duyệt: Apple Inc. (AAPL)

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-27 12:21 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-27 12:14 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Mô hình kinh doanh, FY2025 và 9 tháng FY2026, kỳ/đơn vị, phép tính, quản trị, WTO và kịch bản FCFE.
- Báo cáo đích: `research/companies/US/AAPL/report.md`
- SHA-256 nội dung đích: `411cbb77caf9aa9b9be31cc05281e105c1869e880a196ab4e46953a3e44ed5f1`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [Apple 10-K tại SEC](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Nộp 31/10/2025, FY kết thúc 27/09/2025 | 27/10/2026 | Doanh thu, cơ cấu, CFO/capex, rủi ro |
| [Apple 10-Q tại SEC](https://www.sec.gov/Archives/edgar/data/320193/000032019326000020/aapl-20260627.htm) | Nộp 31/07/2026; 9 tháng đến 27/06/2026 | 27/10/2026 | Kỳ gần nhất, dữ liệu chưa kiểm toán |
| [Apple — chuyển giao lãnh đạo](https://www.apple.com/newsroom/2026/04/tim-cook-to-become-apple-executive-chairman-john-ternus-to-become-apple-ceo/) | 20/04/2026; hiệu lực 01/09/2026 | 27/10/2026 | CEO và chủ tịch điều hành |
| [WTO — Trade Outlook](https://www.wto.org/english/news_e/news26_e/stat_08oct26_510_e.htm) | 08/10/2026; dự báo 2026–2027 | 27/10/2026 | Bối cảnh thương mại toàn cầu |
| [Apple Investor Relations](https://investor.apple.com/investor-relations/) | Trang động | 27/10/2026 | Khả năng truy cập và trạng thái nguồn |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Không có lỗi | Kỳ, đơn vị và số liệu | 10-K FY2025 và 10-Q 9 tháng FY2026 có các số được bài quy đổi đúng từ triệu sang tỷ USD. | SEC filings | Giữ khác biệt kỳ, 10-Q chưa kiểm toán. | Đã kiểm |
| Không có lỗi | Lãnh đạo và bối cảnh | Apple xác nhận Ternus từ 01/09/2026; WTO là dự báo chung, không phải dự báo Apple. | Apple, WTO | Không cần | Đã kiểm |
| Giới hạn | FCFE và định giá | Các đầu vào kịch bản là giả định; không suy từ CFO trừ capex thành FCFE xác nhận, không so giá thị trường. | Báo cáo | Giữ phạm vi và điều chưa biết. | Đã công khai |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

209,586/416,161 ≈ 50,36%; 195,201/416,161 ≈ 46,91%; 111,482 − 12,715 = 98,767 tỷ USD; 364,357/313,695 − 1 ≈ 16,15%. Các kịch bản `80/(12%−2%) = 800`, `100/(10%−3%) ≈ 1.428,6`, `120/(9%−4%) = 2.400` tỷ USD đúng theo giả định.

## Hạn chế của lần kiểm duyệt

SEC/Apple là nguồn gốc nhưng quản trị/chuỗi cung ứng là thông tin doanh nghiệp tự công bố; không xác minh độc lập mọi rủi ro. Nhóm so sánh, giá thị trường, FCFE thực, pháp lý cập nhật và kết quả sau kỳ 10-Q vẫn chưa biết. WTO không dự báo doanh số Apple.

## Kết luận của agent kiểm duyệt

`ĐẠT` trong phạm vi đã kiểm; không có lỗi nghiêm trọng chưa xử lý.
