# Biên bản kiểm nguồn — Bài 001

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-26 18:31 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-26 18:31 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Phần đã đổi trong đợt 2026-10-26: khối đầu, bài luyện thêm và đáp án, ranh giới an toàn, việc chuyển hộp IFRS 18 (đối chiếu nguyên văn bằng git diff), câu IAS 7/IFRS 18, ghi chú PDF IAS 7, giờ chốt. Không kiểm lại phần thân bài soạn ngày 2026-08-10.`
- Báo cáo đích: `learning/lessons/001-business-financial-statements.md`
- SHA-256 nội dung đích: `45eb073f910d25057879d26fc360185197789dca3dda850e6468541c34ff3b56`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên (phiên Claude Code), chép/tổng hợp kết quả của nhánh độc lập trong cuộc trò chuyện ngày 26/10/2026; người kiểm không sửa bài.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản/kỳ/phạm vi | Ngày truy cập | Mục đích |
|---|---|---|---|
| [KPMG — IFRS 18 changes to the statement of cash flows](https://kpmg.com/us/en/articles/2026/ifrs-18-changes-statement-cash-flows.html) | 01/06/2026; nguồn thứ cấp | 2026-10-26 | Hiệu lực, điểm xuất phát, phân loại |
| [BDO — IFR Bulletin 2026/05](https://www.bdo.global/getmedia/d27359ee-5875-45ff-9d36-18b8aa59c8fd/IFRB_2026_05.pdf?ext=.pdf) | 08/2026; nguồn thứ cấp | 2026-10-26 | IAS 7.33A, 34A, 34B–34D |
| [AASB — IAS 7/AASB 107, Interest and dividends](https://standards.aasb.gov.au/node/6600) | Bản quốc gia của văn bản IASB, đã sửa theo AASB 18 | 2026-10-26 | Nguyên văn 33A, 34A, 34B |
| [IFRS 18 — IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/) | Ban hành 04/2024 | 2026-10-26 | Nội dung hộp IFRS 18 |

## Phát hiện và kiểm tra

- Vòng 1: **ĐẠT CÓ ĐIỀU KIỆN** — thiếu nguồn đã mở cho câu IAS 7; thiếu giờ ở mốc chốt; đáp án Bài 6 bỏ sót khoản −5. Đã sửa.
- Vòng 2: **KHÔNG_ĐẠT** — mốc giờ ở tương lai; định nghĩa "không có hoạt động kinh doanh chính được chỉ định" sai. Đã sửa theo câu thay thế của nhánh kiểm.
- Vòng cuối (bản trên): câu IAS 7 khớp KPMG, BDO và nguyên văn AASB (cổ tức đã trả luôn xếp vào tài chính; 34A cho lãi vay đã trả; lãi/cổ tức nhận được xếp vào đầu tư). Hộp IFRS 18 chuyển nguyên văn. Phép tính bài luyện thêm khớp.

## Hạn chế của lần kiểm duyệt

Văn bản IAS 7 sửa đổi đọc qua bản AASB 107 và BDO, không phải bản của IFRS Foundation (PDF IAS 7 không mở công khai được). Bài 001 **chưa** qua phản biện rủi ro trong đợt này.

Mã băm dùng chuẩn hóa của `scripts/validate_report.py`. Hai nhánh đọc cùng phiên bản, không xem kết luận của nhau trước khi trả kết quả. Biên bản không chứng minh hiệu quả học tập và không cho phép đặt lệnh.
