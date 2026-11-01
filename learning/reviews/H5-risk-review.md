# Biên bản kiểm duyệt: H5 — Thống kê và backtest

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-10-27 11:48 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-27 11:40 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Toàn bài, nguồn, phép tính và giới hạn áp dụng.
- Báo cáo đích: `learning/lessons/H5-statistics-backtest-overfitting.md`
- SHA-256 nội dung đích: `cd1cac9443a07322402c827ca0e24811317599f61a64d8dd372965065ecf6d8e`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [NIST — thiết kế thí nghiệm](https://itl.nist.gov/div898/handbook/ppc/section1/ppc136.htm) | Không ghi ngày | 27/10/2026 | Tương quan và nhân quả
| [Sullivan, Timmermann & White — DP303](https://www.fmg.ac.uk/sites/default/files/2020-11/dp303.pdf) | 10/1998; Hoa Kỳ lịch sử | 27/10/2026 | Data snooping và kiểm định ngoài mẫu |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Không chặn | Phạm vi và ứng dụng | Không có lỗi chặn; nghiên cứu lịch sử Hoa Kỳ không chứng minh mọi quy tắc vô hiệu hay kết quả tại Việt Nam. | Các nguồn trên | Kiểm quy định/thị trường cụ thể khi áp dụng. | Theo mô tả |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

100 × 0,05 = 5 kết quả dương giả kỳ vọng; 1 − 0,95^100 ≈ 99,408% nếu các kiểm định độc lập.

## Hạn chế của lần kiểm duyệt

Không khẳng định kết quả tương lai hoặc phương án giao dịch cho người cụ thể; tài liệu lịch sử và nguồn nước ngoài có phạm vi riêng.

## Kết luận của agent kiểm duyệt

`ĐẠT` trong phạm vi phản biện; không có lỗi nghiêm trọng chưa xử lý.
