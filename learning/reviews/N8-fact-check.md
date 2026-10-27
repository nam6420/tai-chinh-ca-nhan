# Biên bản kiểm nguồn — Bài N8

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-26 16:56 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-26 16:54 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Đọc toàn bài; tìm kiếm/mở nguồn trọng yếu; tái tính ví dụ và toàn bộ đáp án; kiểm kỳ, đơn vị, phạm vi và giới hạn nguồn.`
- Báo cáo đích: `learning/lessons/N8-finding-verifying-sources.md`
- SHA-256 nội dung đích: `3ad1116c84ff377d809a7ce944dc5b3171871362aa9f1025a5798f3955197bb4`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên, chép/tổng hợp kết quả của nhánh độc lập trong cuộc trò chuyện ngày26/10/2026; người kiểm không sửa bài.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản/kỳ/phạm vi | Ngày truy cập | Mục đích |
|---|---|---|---|
| [Investor.gov — Using EDGAR](https://www.investor.gov/introduction-investing/getting-started/researching-investments/using-edgar-research-investments) | Hoa Kỳ; ngày xuất bản CHƯA_BIẾT | 2026-10-26 | Đối chiếu nhận định và dữ liệu |
| [Apple FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | FY kết thúc 27/09/2025; US GAAP; triệu USD; hợp nhất | 2026-10-26 | Đối chiếu nhận định và dữ liệu |

## Phát hiện và kiểm tra

EDGAR, phạm vi hồ sơ, bản sửa, quy đổi triệu/tỷ và nguồn độc lập được phân biệt; không dùng hệ thống Hoa Kỳ cho mọi quốc gia.

Các phát hiện cần sửa đã được xử lý và nhánh kiểm xác nhận lại đúng mã băm trên; giữ nhận định ĐẠT trong phạm vi đã giao. Phép tính theo đầu vào bài không chứng minh dự báo thị trường.

## Hạn chế của lần kiểm duyệt

Không kiểm duyệt toàn bộ giáo trình cũ, không đo hiệu quả học thực tế, không xác nhận thuế/phí hiện hành ngoài phạm vi bài.

Mã băm dùng chuẩn hóa của `scripts/validate_report.py`: bỏ khác biệt nhãn nháp và hai dòng trạng thái vòng đời, không bỏ nội dung trọng yếu. Hai nhánh đọc cùng phiên bản, không xem kết luận của nhau trước khi trả kết quả. Biên bản này lưu kết quả kiểm, không tự chứng minh hiệu quả học tập hay cho phép đặt lệnh.

