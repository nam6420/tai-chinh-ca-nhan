# Biên bản kiểm duyệt: H6 — Phân tích kỹ thuật và vi cấu trúc

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-27 11:51 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-27 11:41 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Toàn bài, nguồn phương pháp, các phép tính và phạm vi áp dụng.
- Báo cáo đích: `learning/lessons/H6-technical-analysis-market-microstructure.md`
- SHA-256 nội dung đích: `7892d145a3d7976a04fd8221cbf693a84859d9366100e7b0094607aa00e88343`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [Lo, Mamaysky & Wang — bản gốc MIT](https://www.mit.edu/~wangj/pap/LoMamayskyWang00.pdf) | 08/2000; Hoa Kỳ 1962–1996 | 27/10/2026 | Bằng chứng mẫu giá
| [Sullivan, Timmermann & White](https://www.fmg.ac.uk/sites/default/files/2020-11/dp303.pdf) | 1998; Hoa Kỳ lịch sử | 27/10/2026 | Data snooping
| [SEC — Ask Price](https://www.investor.gov/introduction-investing/investing-basics/glossary/ask-price) | Không ghi ngày; Hoa Kỳ | 27/10/2026 | Bid, ask và spread
| [SEC — loại lệnh](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-14) | 2017, cập nhật 2026 | 27/10/2026 | Giá và khả năng khớp |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Không có lỗi | Toàn bài | Nhận định và giả định trọng yếu phù hợp trong phạm vi nguồn được nêu. | Các nguồn trên | Không cần | Đã kiểm |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Spread = 2; giá giữa 101; 2/101 ≈ 1,98%; 2/102 ≈ 1,96% trước phí.

## Hạn chế của lần kiểm duyệt

URL NBER trong bài trả 403 khi kiểm; nhánh mở bản PDF gốc bài tạp chí trên máy chủ MIT. Không suy hiệu quả lịch sử thành lợi nhuận sau phí hoặc ở Việt Nam.

## Kết luận của agent kiểm duyệt

`ĐẠT` trong phạm vi đã kiểm; không có lỗi nghiêm trọng chưa xử lý.
