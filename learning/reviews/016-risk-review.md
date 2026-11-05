# Biên bản phản biện rủi ro — Bài 016

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-10-26 17:14 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-26 17:12 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Đọc toàn bài; kiểm giả định, trường hợp công thức không còn đúng, giới hạn quốc gia/ngành, điều kiện bác bỏ và nguy cơ hiểu thành lời khuyên cá nhân; tự tìm nguồn phản chứng.`
- Báo cáo đích: `learning/lessons/016-company-research-capstone.md`
- SHA-256 nội dung đích: `fe99f73ecf7651783038d7c751036ddd15e7b5dcedcf6ac5f512c13d7386ec59`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên, chép/tổng hợp kết quả của nhánh độc lập trong cuộc trò chuyện ngày26/10/2026; người kiểm không sửa bài.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản/kỳ/phạm vi | Ngày truy cập | Mục đích |
|---|---|---|---|
| [Apple FY2025 Form10-K](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | FY27/09/2025; nộp31/10/2025; Hoa Kỳ; US GAAP; hợp nhất; triệuUSD; số lịch sử | 2026-10-26 | Phản chứng và giới hạn áp dụng |
| [SEC — Filing Detail](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/0000320193-25-000079-index.htm) | Hồ sơ nộp31/10/2025; kỳ báo cáo27/09/2025 | 2026-10-26 | Phản chứng và giới hạn áp dụng |
| [Damodaran — Valuation](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/val.html) | NYU; phương pháp, ngày phiên bản CHƯA_BIẾT | 2026-10-26 | Phản chứng và giới hạn áp dụng |

## Phát hiện và kiểm tra

Số Apple và ngày nộp31/10/2025 khớp;26,92%,99,53%,98.767 triệuUSD đúng; kịch bản Sao Biển tách riêng. Worksheet đã tồn tại và các mô hình số được kiểm.

Các phát hiện cần sửa đã được xử lý và nhánh kiểm xác nhận lại đúng mã băm trên; giữ nhận định ĐẠT trong phạm vi đã giao. Phép tính theo đầu vào bài không chứng minh dự báo thị trường.

## Hạn chế của lần kiểm duyệt

Đây là bài hướng dẫn, không phải báo cáo định giá Apple. Worksheet đã kiểm các mô hình số; cập nhật sau đó chỉ thêm chỉ dẫn thời điểm ôn, không đổi đầu vào/phép tính.

Mã băm dùng chuẩn hóa của `scripts/validate_report.py`: bỏ khác biệt nhãn nháp và hai dòng trạng thái vòng đời, không bỏ nội dung trọng yếu. Hai nhánh đọc cùng phiên bản, không xem kết luận của nhau trước khi trả kết quả. Biên bản này lưu kết quả kiểm, không tự chứng minh hiệu quả học tập hay cho phép đặt lệnh.

