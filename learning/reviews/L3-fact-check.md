# Biên bản kiểm duyệt: Bài L3 — Thuế thu nhập cá nhân và hồ sơ đầu tư

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-27 11:20 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-10-27 11:02 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Toàn bài; thuế chuyển nhượng, phạm vi ví dụ, cư trú, phép tính và giới hạn kê khai.
- Báo cáo đích: `learning/lessons/L3-personal-income-tax-reporting.md`
- SHA-256 nội dung đích: `1ae218402b9a8ed8d9008aa945154ae1835ae111787908701ee6d239b25d42af`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [Nghị định 253/2026/NĐ-CP](https://vanban.chinhphu.vn/?docid=218684&pageid=27160&typegroupid=4) | 30/06/2026; hiệu lực 01/07/2026 | 27/10/2026 | Số hiệu, hiệu lực và tệp gốc |
| [Chính phủ — thuế chuyển nhượng chứng khoán](https://xaydungchinhsach.chinhphu.vn/thue-thu-nhap-ca-nhan-doi-voi-thu-nhap-tu-chuyen-nhuong-chung-khoan-119260703164200344.htm) | 04/07/2026 | 27/10/2026 | Hướng dẫn trích Điều 54, giá chuyển nhượng |
| [Luật thuế TNCN hợp nhất 112/VBHN-VPQH](https://vanban.chinhphu.vn/?docid=218215&pageid=27160) | 20/05/2026 | 27/10/2026 | Số hiệu và phiên bản |
| [Chính phủ — toàn văn luật thuế TNCN](https://xaydungchinhsach.chinhphu.vn/luat-thue-thu-nhap-ca-nhan-119260623093630882.htm) | Năm 2026 | 27/10/2026 | Phạm vi và hiệu lực luật |
| [Chính phủ — thuế tiền lương cư trú/không cư trú](https://xaydungchinhsach.chinhphu.vn/quy-dinh-thue-thu-nhap-ca-nhan-doi-voi-thu-nhap-tu-tien-luong-tien-cong-119260327070011016.htm) | Năm 2026; Luật 109/2025 | 27/10/2026 | Đối chiếu khác biệt khái quát về cư trú |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Không có lỗi | Thuế ví dụ cổ phiếu | Hướng dẫn trích Điều 54 nêu 0,1% trên giá chuyển nhượng từng lần; giá niêm yết theo giá bán thực tế. Bài giới hạn phạm vi ví dụ. | Hướng dẫn Chính phủ | Không cần | Đã kiểm |
| Không có lỗi | Cư trú | Bài chỉ nói phạm vi thu nhập khác theo cư trú, không xác định nghĩa vụ cá nhân. | Luật hợp nhất, hướng dẫn Chính phủ | Giữ `CHƯA_BIẾT` cho trường hợp cụ thể. | Đã giới hạn |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

100.000.000 × 0,1% = 100.000 đồng; 50.000.000 × 0,1% = 50.000 đồng. Mua 120 triệu, bán 100 triệu: lỗ 20 triệu không thay cơ sở giá chuyển nhượng trong ví dụ.

## Hạn chế của lần kiểm duyệt

PDF nghị định gốc được mở nhưng không hiển thị văn bản qua trình đọc; nội dung Điều 54 đối chiếu qua hướng dẫn chính thức của Báo điện tử Chính phủ, cùng metadata nghị định. Không xác nhận khấu trừ, thời hạn hoặc kê khai chi tiết của cá nhân cụ thể.

## Kết luận của agent kiểm duyệt

`ĐẠT` trong phạm vi đã kiểm; không có lỗi nghiêm trọng chưa xử lý.
