# Biên bản kiểm duyệt: Bài P2

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-10-27 09:45 UTC+7 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-10-27 09:40 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi: Công thức niên kim, ví dụ lãi, APR, Thông tư 39 hợp nhất, CIC theo Thông tư 15 và sửa đổi sắp hiệu lực.
- Báo cáo đích: `learning/lessons/P2-personal-debt.md`
- SHA-256 nội dung đích: `e9675a0e3d8875fbc28803e3f1d47a8645fcbf28ce91ec9b0236982e0f938231`
- Kết luận: `CHƯA_BIẾT`
- Lỗi nghiêm trọng chưa xử lý: `0`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| [CFPB — APR](https://www.consumerfinance.gov/ask-cfpb/what-is-the-difference-between-a-loan-interest-rate-and-the-apr-en-733/) | Rà soát 28/08/2026; Hoa Kỳ | 2026-10-27 | Khái niệm APR |
| [CFPB — Debt action plan](https://files.consumerfinance.gov/f/documents/cfpb_your-money-your-goals_debt-action-plan_tool_2018-11.pdf) | 10/2018; Hoa Kỳ | 2026-10-27 | Hai phương pháp trả nợ |
| [86/VBHN-NHNN](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/86-vbhn-nhnn.pdf) | 30/06/2026; hợp nhất đến TT29/2026 hiệu lực 15/08/2026 | 2026-10-27 | Lãi, phí và cơ cấu nợ |
| [TT15/2023](https://datafiles.chinhphu.vn/cpp/files/vbpq/2023/12/15-nhnn.pdf); [TT46/2026](https://vanban.chinhphu.vn/?classid=1&docid=219435&pageid=27160) | Hiệu lực lần lượt 01/01/2025 và 01/11/2026 | 2026-10-27 | Thời điểm hiệu lực quy định CIC |
| [Báo Điện tử Chính phủ — ý kiến NHNN](https://baochinhphu.vn/thoi-han-luu-giu-thong-tin-lich-su-no-xau-102260922073222586.htm) | 22/09/2026 | 2026-10-27 | Thời hạn cung cấp thông tin tiêu cực |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| Đã xử lý | Căn cứ CIC | Bài không dùng Thông tư 03/2013 làm căn cứ hiện hành; phân biệt ngày hiệu lực TT15 và TT46 | Trang Chính phủ, ý kiến NHNN | Giữ phân biệt ngày chốt và ngày hiệu lực | ĐẠT |
| Không lỗi | Lãi, phí, cơ cấu nợ | Các nhận định đã kiểm khớp bản hợp nhất trong phạm vi áp dụng | 86/VBHN-NHNN | Giữ giới hạn từng loại bên cho vay | ĐẠT |
| Trung bình | Trường dữ liệu và phân loại CIC | Chưa xác minh từ hệ thống chỉ tiêu gốc; bài giữ `CHƯA_BIẾT` | PDF TT15 và bản nháp | Kiểm quyết định chỉ tiêu hiện hành, từng ngưỡng và tác động TT46 sau 01/11 | Còn mở |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Khoản phẳng 30 triệu/12 tháng cho khoảng 2,6430%/tháng, 31,716% cộng đơn và 36,758% ghép lãi năm. Khoản dư nợ giảm dần trả khoảng 2.750.400 đồng/tháng; bài tập 10 triệu/10 tháng khoảng 3,4602%/tháng. Các số đã làm tròn khớp giả định.

## Hạn chế của lần kiểm duyệt

Chưa xác minh các trường dữ liệu CIC từ quyết định chỉ tiêu gốc. PDF TT46 đã mở nhưng không trích được điều khoản; văn bản chưa có hiệu lực tại ngày chốt.

## Kết luận của agent kiểm duyệt

`CHƯA_BIẾT`: phép tính và căn cứ đã kiểm khớp nhưng còn dữ kiện CIC và tác động sửa đổi chưa xác minh đầy đủ.
