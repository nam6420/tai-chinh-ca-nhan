# Biên bản kiểm duyệt: A2 — Quỹ mở, ETF và sai lệch theo dõi

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-10-27 11:35 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-27 11:34 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Toàn bài, nguồn, pháp lý, giả định và bài tập; xác nhận lại phần sửa.
- Báo cáo đích: `learning/lessons/A2-mutual-funds-etfs-fees.md`
- SHA-256 nội dung đích: `c0c31fbe62578faf72a886c9242c2757c9027e367a3b26124a19a1984a165c0b`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [SEBI — Circular 69](https://www.sebi.gov.in/sebi_data/attachdocs/may-2022/1653307308174.pdf) | 23/05/2022; Ấn Độ | 27/10/2026 | Phân biệt TE và TD |
| [SEC — ETF](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-24) | 23/02/2023; Hoa Kỳ | 27/10/2026 | Thanh khoản và giá so với NAV |
| [NSE — Tracking Error](https://www.nseindia.com/static/products-services/indices-tracking-error) | Phương pháp Ấn Độ | 27/10/2026 | Độ biến động chênh lệch |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Không có lỗi | Bản cập nhật | Phần mới dẫn SEBI cho phân biệt TE/TD và SEC cho thanh khoản; không dùng quy định Ấn Độ hoặc Hoa Kỳ làm quy định Việt Nam. Điểm thiếu nguồn trước đã được xử lý. | Các nguồn trên | Kiểm thêm trường hợp cụ thể trước sử dụng. | Đã kiểm |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

NAV mẫu 10.000 đồng; premium 1%; 250 × 21.000 trừ phí 1% = 5.197.500 đồng; bài tập NAV 20.000, premium 2%, sau phí 1.980.000; 3% − 5% = −2 điểm phần trăm.

## Hạn chế của lần kiểm duyệt

Chưa xác định phí, phương pháp theo văn bản Việt Nam và giá của từng quỹ cụ thể; bài giữ CHƯA_BIẾT.

## Kết luận của agent kiểm duyệt

`ĐẠT` trong phạm vi đã kiểm; không có lỗi nghiêm trọng chưa xử lý.
