# Biên bản kiểm duyệt: Bài P1

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-27 09:45 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-27 09:40 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Ngân sách, quỹ khẩn cấp, phép tính, hạn mức và quy trình bảo hiểm tiền gửi, Điều 35 Luật Kinh doanh bảo hiểm, tỷ lệ đóng bảo hiểm bắt buộc.
- Báo cáo đích: `learning/lessons/P1-budget-emergency-fund-insurance.md`
- SHA-256 nội dung đích: `089cda636e1e05b898be5eadebcd5eea9139ec14b5f92c46b333f6a8fb7c62cb`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [CFPB — Emergency fund](https://www.consumerfinance.gov/an-essential-guide-to-building-an-emergency-fund/) | Sửa 29/10/2025; Hoa Kỳ | 2026-10-27 | Mục đích và mức quỹ |
| [CFPB — Budgeting](https://www.consumerfinance.gov/archive/blog/budgeting-how-to-create-a-budget-and-stick-with-it/) | 05/06/2019; Hoa Kỳ | 2026-10-27 | Ngân sách |
| [FINRA — Financial hardship](https://www.finra.org/investors/insights/prepare-survive-financial-hardship) | 23/04/2024; Hoa Kỳ | 2026-10-27 | Mốc quỹ tham khảo |
| [Thông tư 05/2026](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/05-nhnn.pdf); [DIV — hạn mức](https://www.div.gov.vn/tu-ngay-13-7-2026-han-muc-chi-tra-tien-bao-hiem-cua-bao-hiem-tien-gui-viet-nam-la-350-trieu-dong) | Hiệu lực 13/07/2026; DIV 15/07/2026 | 2026-10-27 | Hạn mức 350 triệu đồng |
| [Luật BHTG 111/2025](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat111-2025.pdf); [DIV — loại trừ](https://div.gov.vn/to-chuc-tham-gia-bao-hiem-tien-gui-can-luu-y-gi-khi-tinh-va-nop-phi-bao-hiem-tien-gui) | Luật hiệu lực 01/05/2026; DIV 04/09/2026 | 2026-10-27 | Phạm vi loại trừ; PDF luật không trích được điều khoản |
| [DIV — quy trình chi trả](https://www.div.gov.vn/quy-trinh-chi-tra-bao-hiem-tien-gui-theo-luat-bao-hiem-tien-gui-nam-2025-bao-dam-tot-hon-quyen-loi-nguoi-gui-tien) | 29/06/2026; Việt Nam | 2026-10-27 | Mốc 45 ngày và cơ chế đặc biệt |
| [Luật Kinh doanh bảo hiểm hợp nhất](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/31-vbhn-vpqh.pdf) | 13/03/2026 | 2026-10-27 | Điều 35, 21 ngày |
| [Luật BHXH 2024](https://xaydungchinhsach.chinhphu.vn/toan-van-luat-so-41-2024-qh15-bao-hiem-xa-hoi-119240723163650489.htm); [NĐ 188/2025](https://xaydungchinhsach.chinhphu.vn/nghi-dinh-188-2025-nd-cp-quy-dinh-moi-ve-doi-tuong-muc-dong-muc-ho-tro-dong-bao-hiem-y-te-119250711175642187.htm); [NĐ 374/2025](https://baochinhphu.vn/quy-dinh-moi-ve-muc-dong-va-huong-bao-hiem-that-nghiep-102260107171705469.htm) | Hiệu lực lần lượt 01/07/2025, 15/08/2025, 01/01/2026 | 2026-10-27 | Các thành phần BHXH, BHYT, BHTN |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Không lỗi | Hạn mức và chi trả | 350 triệu đồng theo người và tổ chức; DIV nêu mốc chi trả 45 ngày từ khi phát sinh nghĩa vụ | Thông tư 05 và DIV | Giữ điều kiện của tiền gửi được bảo hiểm và hạn mức thông thường | ĐẠT |
| Không lỗi | Thời gian cân nhắc 21 ngày | Điều 35 nêu hợp đồng trên một năm, tính từ khi nhận hợp đồng; có thể trừ chi phí hợp lý theo thỏa thuận | Văn bản hợp nhất | Giữ điều kiện | ĐẠT |
| Không lỗi | Tỷ lệ đóng | Tổng 10,5% và 21,5% gồm các quỹ BHXH, BHYT, BHTN cho đối tượng được nêu | Luật BHXH, NĐ 188 và NĐ 374 | Không suy rộng cho mọi đối tượng | ĐẠT |
| Chưa biết | Loại trừ BHTG | Chưa đối chiếu đầy đủ từng điều khoản luật gốc; bài giữ giới hạn này | PDF luật và DIV | Kiểm toàn văn trước khi áp dụng | CHƯA_BIẾT |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Quỹ ba tháng `3 × 12.300.000 = 36.900.000`, thiếu `21.900.000`, góp 3 triệu/tháng cần 8 tháng làm tròn lên. Sáu tháng là 73,8 triệu, thiếu 58,8 triệu, cần 20 tháng. Ví dụ 400−350=50 triệu và 500−350=150 triệu đúng theo giả định.

## Hạn chế của lần kiểm duyệt

PDF Luật BHTG không trích được điều khoản để đối chiếu đầy đủ ngoại lệ. Phí bảo hiểm liên kết đầu tư vẫn dựa nguồn thứ cấp và được ghi chưa xác minh.

## Kết luận của agent kiểm duyệt

`ĐẠT` cho nhận định có nguồn trong phạm vi trên; các điều kiện chưa xác minh vẫn giữ `CHƯA_BIẾT`.
