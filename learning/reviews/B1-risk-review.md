# Biên bản kiểm duyệt: Bài B1 — Công ty chứng khoán, phí, thuế và lưu ký

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-10-27 11:04 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-27 10:57 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Toàn bài; phí, thuế, lưu ký, ranh giới tư vấn và bài tập.
- Báo cáo đích: `learning/lessons/B1-broker-fees-custody.md`
- SHA-256 nội dung đích: `f749dce8337f964dc9da7ee1e448fc2551b8a5218eac65f7635e40c5113cbcdb`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [PHS — biểu phí](https://www.phs.vn/san-pham-dich-vu/bieu-phi-giao-dich-chung-khoan-co-so-26) | Áp dụng từ 30/03/2026 | 27/10/2026 | Phí theo kênh, bậc và lưu ký |
| [VFS — biểu phí](https://www.vfs.com.vn/ho-tro/bieu-phi) | Không ghi ngày hiệu lực trong phần đã mở | 27/10/2026 | Phí và khoản thu hộ/thu riêng |
| [Chính phủ — thuế chuyển nhượng](https://xaydungchinhsach.chinhphu.vn/thue-thu-nhap-ca-nhan-doi-voi-thu-nhap-tu-chuyen-nhuong-chung-khoan-119260703164200344.htm) | 04/07/2026 | 27/10/2026 | Phạm vi và cơ sở tính thuế |
| [SEC — Brokers](https://www.investor.gov/introduction-investing/getting-started/working-investment-professional/brokers) | Không ghi ngày; Hoa Kỳ | 27/10/2026 | Khung tìm hiểu trung gian |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Thấp | Ví dụ phí | Mức 0,2% là giả định; PHS có các mức khác nhau theo kênh. | PHS | Kiểm kênh và ngày hiệu lực khi dùng thực tế. | Đã giới hạn |
| Thấp | Thuế | 0,1% tính trên giá chuyển nhượng trong phạm vi nguồn; không xác định nghĩa vụ cá nhân. | Chính phủ | Giữ điều kiện áp dụng, cập nhật khi luật đổi. | Đã giới hạn |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Phí mua 50.000.000 × 0,2% = 100.000 đồng; phí bán 45.000.000 × 0,2% = 90.000 đồng; thuế giả định 45.000.000 × 0,1% = 45.000 đồng; tổng = 235.000 đồng. Biểu PHS và VFS phân biệt các cấu phần phí lưu ký.

## Hạn chế của lần kiểm duyệt

Chưa xác minh danh sách giấy phép UBCKNN mới nhất hoặc hợp đồng cụ thể; không dùng hướng dẫn Hoa Kỳ như quy định Việt Nam.

## Kết luận của agent kiểm duyệt

`ĐẠT` trong phạm vi phản biện; không có lỗi nghiêm trọng chưa xử lý.
