# Biên bản kiểm duyệt: H6 — Phân tích kỹ thuật và vi cấu trúc

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-10-27 11:49 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-27 11:41 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Toàn bài, nguồn, phép tính và giới hạn áp dụng.
- Báo cáo đích: `learning/lessons/H6-technical-analysis-market-microstructure.md`
- SHA-256 nội dung đích: `7892d145a3d7976a04fd8221cbf693a84859d9366100e7b0094607aa00e88343`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [Lo, Mamaysky & Wang — bài gốc](https://www.mit.edu/~wangj/pap/LoMamayskyWang00.pdf) | 2000; cổ phiếu Hoa Kỳ 1962–1996 | 27/10/2026 | Bằng chứng về mẫu giá
| [Sullivan, Timmermann & White](https://www.fmg.ac.uk/sites/default/files/2020-11/dp303.pdf) | 1998; Hoa Kỳ lịch sử | 27/10/2026 | Data snooping và ngoài mẫu
| [SEC — loại lệnh](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-14) | 12/07/2017, cập nhật 18/08/2026 | 27/10/2026 | Rủi ro lệnh thị trường/giới hạn |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Không chặn | Phạm vi và ứng dụng | Thấp: bài chưa nêu rõ lệnh thị trường không bảo đảm khớp trong mọi điều kiện; đã phân biệt quy tắc Việt Nam và dẫn V2. | Các nguồn trên | Kiểm quy định/thị trường cụ thể khi áp dụng. | Theo mô tả |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Ask − bid = 2; giá giữa 101; 2/101 ≈ 1,98%; mua 102 bán 100 mất 2/102 ≈ 1,96% trước phí.

## Hạn chế của lần kiểm duyệt

Không khẳng định kết quả tương lai hoặc phương án giao dịch cho người cụ thể; tài liệu lịch sử và nguồn nước ngoài có phạm vi riêng.

## Kết luận của agent kiểm duyệt

`ĐẠT` trong phạm vi phản biện; không có lỗi nghiêm trọng chưa xử lý.
