# Biên bản kiểm duyệt: Bài B1 — Công ty chứng khoán, phí, thuế và lưu ký

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-27 11:02 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-10-27 10:57 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Vai trò trung gian, chọn công ty, biểu phí PHS/VFS, thuế, lưu ký và phép tính.
- Báo cáo đích: `learning/lessons/B1-broker-fees-custody.md`
- SHA-256 nội dung đích: `f749dce8337f964dc9da7ee1e448fc2551b8a5218eac65f7635e40c5113cbcdb`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [SEC — Brokers](https://www.investor.gov/introduction-investing/getting-started/working-investment-professional/brokers) | Không ghi ngày; Hoa Kỳ | 27/10/2026 | Dịch vụ, phí, xung đột lợi ích |
| [PHS — biểu phí](https://www.phs.vn/san-pham-dich-vu/bieu-phi-giao-dich-chung-khoan-co-so-26) | Áp dụng từ 30/03/2026 | 27/10/2026 | Phí theo kênh và bậc |
| [VFS — biểu phí](https://www.vfs.com.vn/ho-tro/bieu-phi) | Không ghi ngày hiệu lực chung | 27/10/2026 | Phí giao dịch và lưu ký |
| [Chính phủ — thuế chuyển nhượng](https://xaydungchinhsach.chinhphu.vn/thue-thu-nhap-ca-nhan-doi-voi-thu-nhap-tu-chuyen-nhuong-chung-khoan-119260703164200344.htm) | 04/07/2026 | 27/10/2026 | Điều 54 Nghị định 253 và phạm vi thuế |
| [Nghị định 253/2026/NĐ-CP](https://vanban.chinhphu.vn/?docid=218684&orggroupid=2&pageid=27160) | 30/06/2026; hiệu lực 01/07/2026 | 27/10/2026 | Metadata văn bản gốc |
| [Thông tư 102/2021/TT-BTC](https://vanban.chinhphu.vn/?docid=204547&pageid=27160) | 17/11/2021; hiệu lực 01/01/2022 | 27/10/2026 | Giá dịch vụ chứng khoán |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Không có lỗi | Vai trò và phí | SEC cho khung Hoa Kỳ; biểu phí PHS và VFS khác theo điều kiện. Bài không coi một biểu giá là giá chung. | Các nguồn trên | Không cần | Đã kiểm |
| Không có lỗi | Thuế | Mức 0,1% theo giá chuyển nhượng trong phạm vi nguồn nêu, không mặc nhiên áp cho mọi trường hợp. | Bài Chính phủ, metadata nghị định | Không cần | Đã kiểm |
| Giới hạn | Giấy phép và lưu ký | Chưa xác nhận danh sách giấy phép mới nhất và không có mức phí lưu ký chung. | Mục `CHƯA_BIẾT` trong bài | Kiểm trực tiếp theo công ty và thời điểm | Đã công khai |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

50.000.000 × 0,2% = 100.000 đồng; 45.000.000 × 0,2% = 90.000 đồng; 45.000.000 × 0,1% = 45.000 đồng; tổng = 235.000 đồng, theo giả định, chưa tính các khoản khác.

## Hạn chế của lần kiểm duyệt

PDF nghị định mở được nhưng web không trích văn bản; nội dung Điều 54 đối chiếu qua trang giải thích chính thức Chính phủ. VFS không ghi ngày hiệu lực chung. Không xác định thuế cá nhân cụ thể hay xác nhận danh sách giấy phép mới nhất.

## Kết luận của agent kiểm duyệt

`ĐẠT` trong phạm vi đã kiểm; không có lỗi nghiêm trọng chưa xử lý.
