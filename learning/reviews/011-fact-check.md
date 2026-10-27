# Biên bản kiểm nguồn — Bài 011

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-26 17:05 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-26 17:04 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Đọc toàn bài; tìm kiếm/mở nguồn trọng yếu; tái tính ví dụ và toàn bộ đáp án; kiểm kỳ, đơn vị, phạm vi và giới hạn nguồn.`
- Báo cáo đích: `learning/lessons/011-dcf-reverse-dcf.md`
- SHA-256 nội dung đích: `14c62076d36e09f46589c44b53c9dedcff7121785cec9b3c5128f647d143eb6c`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên, chép/tổng hợp kết quả của nhánh độc lập trong cuộc trò chuyện ngày26/10/2026; người kiểm không sửa bài.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản/kỳ/phạm vi | Ngày truy cập | Mục đích |
|---|---|---|---|
| [Damodaran — Approaches](https://pages.stern.nyu.edu/adamodar/New_Home_Page/lectures/approach.html) | NYU; phương pháp, ngày phiên bản CHƯA_BIẾT | 2026-10-26 | Đối chiếu nhận định và dữ liệu |
| [Damodaran — Valuation](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/val.html) | NYU; phương pháp, ngày phiên bản CHƯA_BIẾT | 2026-10-26 | Đối chiếu nhận định và dữ liệu |
| [Apple FY2025 Form10-K](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Hoa Kỳ; US GAAP; FY27/09/2025; triệu USD | 2026-10-26 | Đối chiếu nhận định và dữ liệu |

## Phát hiện và kiểm tra

FCFF3=112,2, TV2=1.402,5, EV1.340,9091 tỷ, vốn chủ1.140,9091 tỷ và đảo g1,333% khớp; ghép đúng dòng tiền/tỷ lệ.

Các phát hiện cần sửa đã được xử lý và nhánh kiểm xác nhận lại đúng mã băm trên; giữ nhận định ĐẠT trong phạm vi đã giao. Phép tính theo đầu vào bài không chứng minh dự báo thị trường.

## Hạn chế của lần kiểm duyệt

Không kiểm duyệt toàn bộ giáo trình cũ, không đo hiệu quả học thực tế, không xác nhận thuế/phí hiện hành ngoài phạm vi bài.

Mã băm dùng chuẩn hóa của `scripts/validate_report.py`: bỏ khác biệt nhãn nháp và hai dòng trạng thái vòng đời, không bỏ nội dung trọng yếu. Hai nhánh đọc cùng phiên bản, không xem kết luận của nhau trước khi trả kết quả. Biên bản này lưu kết quả kiểm, không tự chứng minh hiệu quả học tập hay cho phép đặt lệnh.

