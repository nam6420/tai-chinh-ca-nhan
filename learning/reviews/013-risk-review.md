# Biên bản phản biện rủi ro — Bài 013

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-10-26 17:14 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-26 17:12 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Đọc toàn bài; kiểm giả định, trường hợp công thức không còn đúng, giới hạn quốc gia/ngành, điều kiện bác bỏ và nguy cơ hiểu thành lời khuyên cá nhân; tự tìm nguồn phản chứng.`
- Báo cáo đích: `learning/lessons/013-banks-insurers.md`
- SHA-256 nội dung đích: `1754fcda84e81ac1802d761fdd0e92fb78795bcadeccf6258ec06b3f8c5268fc`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên, chép/tổng hợp kết quả của nhánh độc lập trong cuộc trò chuyện ngày26/10/2026; người kiểm không sửa bài.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản/kỳ/phạm vi | Ngày truy cập | Mục đích |
|---|---|---|---|
| [Federal Reserve — IFDP1197](https://www.federalreserve.gov/econresdata/ifdp/2017/files/ifdp1197.pdf) | 02/2017; nghiên cứu đa quốc gia, không phải ngưỡng quản lý | 2026-10-26 | Phản chứng và giới hạn áp dụng |
| [NAIC — Glossary](https://content.naic.org/glossary-insurance-terms) | Hoa Kỳ; ngày xuất bản CHƯA_BIẾT; định nghĩa chung có thể khác theo thực thể | 2026-10-26 | Phản chứng và giới hạn áp dụng |
| [Berkshire FY2025 Annual Report](https://www.berkshirehathaway.com/2025ar/2025ar.pdf) | FY2025; Hoa Kỳ; US GAAP; phần định nghĩa float | 2026-10-26 | Phản chứng và giới hạn áp dụng |
| [IFRS Foundation — IFRS17](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-17-insurance-contracts/) | Chuẩn quốc tế; áp dụng tùy quốc gia; trang hiện hành | 2026-10-26 | Phản chứng và giới hạn áp dụng |

## Phát hiện và kiểm tra

Đã chuyển định nghĩa NIM chính sang Fed, combined ratio sang NAIC; bỏ số trang JPM không nhất quán. CET1 và giới hạn IFRS17/phạm vi quốc gia được đối chiếu.

Các phát hiện cần sửa đã được xử lý và nhánh kiểm xác nhận lại đúng mã băm trên; giữ nhận định ĐẠT trong phạm vi đã giao. Phép tính theo đầu vào bài không chứng minh dự báo thị trường.

## Hạn chế của lần kiểm duyệt

Nhánh kiểm nguồn không mở trực tiếp được PDF OCC và Allstate gốc ở lượt kiểm; định nghĩa chính đã đối chiếu từ Fed/NAIC, Allstate bổ sung và JPMorgan báo cáo năm. Không suy lỗi truy cập thành nội dung sai.

Mã băm dùng chuẩn hóa của `scripts/validate_report.py`: bỏ khác biệt nhãn nháp và hai dòng trạng thái vòng đời, không bỏ nội dung trọng yếu. Hai nhánh đọc cùng phiên bản, không xem kết luận của nhau trước khi trả kết quả. Biên bản này lưu kết quả kiểm, không tự chứng minh hiệu quả học tập hay cho phép đặt lệnh.

