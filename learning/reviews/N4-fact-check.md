# Biên bản kiểm nguồn — Bài N4

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-26 16:56 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-26 16:54 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Đọc toàn bài; tìm kiếm/mở nguồn trọng yếu; tái tính ví dụ và toàn bộ đáp án; kiểm kỳ, đơn vị, phạm vi và giới hạn nguồn.`
- Báo cáo đích: `learning/lessons/N4-time-value-returns.md`
- SHA-256 nội dung đích: `b6eae1288f29fdcceed3f196b9019036145c886fd2cff453f2031afec068d9e9`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên, chép/tổng hợp kết quả của nhánh độc lập trong cuộc trò chuyện ngày26/10/2026; người kiểm không sửa bài.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản/kỳ/phạm vi | Ngày truy cập | Mục đích |
|---|---|---|---|
| [California BOE — Time Value of Money](https://www.boe.ca.gov/info/tvm/lesson1.html) | Hoa Kỳ; tài liệu giáo dục, ngày xuất bản CHƯA_BIẾT; đơn vị tùy ví dụ | 2026-10-26 | Đối chiếu nhận định và dữ liệu |
| [Investor.gov — Compound Interest Calculator](https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator) | Hoa Kỳ; công cụ hiện hành; chưa thấy ngày xuất bản | 2026-10-26 | Đối chiếu nhận định và dữ liệu |

## Phát hiện và kiểm tra

Đã tái tính lãi kép, PV/FV, lợi suất năm hóa, cổ tức và lợi suất thực; góp cuối kỳ phân biệt với góp giữa kỳ.

Các phát hiện cần sửa đã được xử lý và nhánh kiểm xác nhận lại đúng mã băm trên; giữ nhận định ĐẠT trong phạm vi đã giao. Phép tính theo đầu vào bài không chứng minh dự báo thị trường.

## Hạn chế của lần kiểm duyệt

Không kiểm duyệt toàn bộ giáo trình cũ, không đo hiệu quả học thực tế, không xác nhận thuế/phí hiện hành ngoài phạm vi bài.

Mã băm dùng chuẩn hóa của `scripts/validate_report.py`: bỏ khác biệt nhãn nháp và hai dòng trạng thái vòng đời, không bỏ nội dung trọng yếu. Hai nhánh đọc cùng phiên bản, không xem kết luận của nhau trước khi trả kết quả. Biên bản này lưu kết quả kiểm, không tự chứng minh hiệu quả học tập hay cho phép đặt lệnh.

