# Biên bản kiểm duyệt: MIXUE Group (2097.HK), đọc báo cáo tài chính FY2022–FY2025 và H1 2026 (bản nháp v3)

> Điều phối viên lưu bản tóm lược từ báo cáo của subagent `source-fact-checker` (lần kiểm 3). Giữ nguyên kết luận, mức độ và bằng chứng chính; không thêm nhận định mới.

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-25 09:20 +07` (giờ máy theo agent; bắt đầu khoảng 09:09)
- Chốt dữ liệu lúc: `2026-11-25 09:05 +07` (khớp báo cáo đích v3)
- Phạm vi: 10 phát hiện N1–N10 của lần 2; toàn bộ nội dung mới của v3 (Ban lãnh đạo, quản trị, phân bổ vốn; Bối cảnh ngành; đoạn chi phí H1 2026; phân rã lợi nhuận; thanh khoản; bảng cửa hàng; ngưỡng kịch bản; nhãn; sổ nguồn)
- Báo cáo đích: `research/companies/HK/reviews/2097-mixue-draft-v3-sha-39cd1668.md` (bản sao nguyên vẹn của v3)
- SHA-256 nội dung đích: `39cd1668d645ec6b0b3da5e42b48de20b68b58ae0d56a9932ac5c78278607df7` (agent tự tính bằng `validate_report.py --print-hash`, khớp)
- Kết luận: `KHÔNG_ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `1`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

Ngày truy cập 2026-11-25; PDF tải bằng `curl`, băm SHA-256, đọc bằng `pdftotext`. Gồm: S9, S10, thông báo họp cổ đông bất thường 2026-09-11 (băm khớp 3/3); **bản HKEXnews gốc kết quả biểu quyết ĐHĐCĐ bất thường 2026-09-30** (`2026093002215.pdf`, `6f6805fe…`; khớp bản sao Eastmoney); **cáo bạch đầy đủ 558 trang** (`2025022100009.pdf`, `c9014020…`); **báo cáo giữa kỳ 2026 đầy đủ** (`2026092300280.pdf`, ngày 2026-09-23, `0e1ddcd2…`); thông báo cấp quyền thưởng 2026-09-28 (`bcd2952b…`); thông tin nội bộ về lưu hành toàn phần cổ phiếu H 2026-05-03; thông báo thay đổi HĐQT, ban kiểm soát, quản lý 2026-03-24; danh mục công bố của công ty (`titleSearchServlet`, không có công bố từ 2026-11-06 đến 2026-11-25); báo cáo gốc giữa kỳ của Guming (2026-08-26), Meituan (2026-08-28), Auntea Jenny (mã 2589, 2026-08-28), Luckin (SEC 6-K 2026-11-03); Inside Retail (Chagee), Caixin (Nayuki), KrASIA/Nikkei, Investing.com, Tân Hoa Xã (2026-08-12), Winshang (2023). Băm 10/10 PDF trong repo khớp `SHA256SUMS.txt`.

## Phát hiện lần 2: trạng thái trong v3

N1 (sở hữu hai nhà sáng lập): `ĐÃ_SỬA`, và cáo bạch đã xác nhận cách đọc "hai lô riêng" cùng thỏa thuận hành động phối hợp (v3 vẫn để tổng chung `CHƯA_BIẾT`). N2 (FULU bên liên quan): `ĐÃ_SỬA` về bản chất, còn lỗi diễn đạt (F3). N3, N4, N5, N6, N7, N8, N9: `ĐÃ_SỬA`. N10 (lưu trữ nguồn, S11): `SỬA_CHƯA_ĐỦ` (bản HKEXnews gốc nay đã có).

## Phát hiện mới trong v3

| Mức độ | Mã | Phát hiện | Bằng chứng | Trạng thái (sau khi sửa v4) |
|---|---|---|---|---|
| NGHIÊM_TRỌNG | F1 | v3 viết hai lần rằng báo cáo lưu chuyển tiền tệ H1 2026 chưa có. Sai: báo cáo giữa kỳ đầy đủ đã đăng 2026-09-23. OCF H1 2026 = 2.049,8 triệu so với 3.275,4 triệu (−37,4%); OCF/lợi nhuận 0,88 so với 1,20; chỉ báo #5 và mốc kịch bản Cơ sở của chính v3 đã bị vi phạm; mục Thanh khoản dùng "tiền tăng 8,3%" như bằng chứng ngược chiều | Interim Report 2026, báo cáo lưu chuyển tiền tệ; điều phối viên tự grep: 2.049.818 / 3.275.383 | Đã sửa trong v4 |
| TRUNG_BÌNH | F2 | Quyền thưởng và lưu hành toàn phần có nguồn gốc: 12.023.300 quyền cho 1.234 người ngày 2026-09-28 (3,167%); chuyển 22.823.988 cổ phiếu (6,01%) thành cổ phiếu H nộp CSRC 2026-04-30 | HKEXnews 2026-09-28, 2026-05-03 | Đã sửa trong v4 |
| TRUNG_BÌNH | F3 | "Mua 51% bằng 285,6 triệu tiền mặt" và "mua từ người nhà cổ đông": 285,6 triệu là tiền công ty góp tăng vốn vào chính FULU; dòng tiền ròng ra chỉ ≈ 13,7 triệu; mua thêm 2% từ ông Zhao Jie với 11,2 triệu; ngoài 60,05% của bà Tian Haixia còn 20,41% qua Mailang Tongzhou | S5 báo cáo HĐQT tr. 58–59, thuyết minh 40; điều phối viên đã grep | Đã sửa trong v4 |
| THẤP | F4 | S11 nâng lên bản HKEXnews gốc; hai người dự họp có thể gồm hai nhà sáng lập, việc ít người dự là bình thường (đại hội thường niên 14 người, 94,21%) nên không phải dấu hiệu bất thường; việc đã trả cổ tức `CHƯA_BIẾT` | HKEXnews 2026-09-30 | Đã sửa trong v4 |
| THẤP | F5 | Người phụ trách tài chính: bà Cui Haijing, "Head of Finance" | HKEXnews 2026-03-24 | Đã sửa trong v4 |
| THẤP | F6 | Cổ tức tới hai nhà sáng lập ≈ 816,2 triệu RMB (81,1%), trước thuế | tái tính | Đã sửa trong v4 |
| THẤP | F7 | Làm tròn/nhãn: chi phí quản lý H2 2025 là 643,9 (không phải 643,8); Guming chi phí bán hàng H1 2025 = 5,52% (không phải 5,51%); Guming doanh thu/cửa hàng +2,7% là phép chia, chỉ số công bố là GMV/cửa hàng +3,4%; Luckin −11,1% là cửa hàng tự vận hành; Chagee −16,1% là GMV cùng cửa hàng Đại Trung Hoa | Guming tr. 16–17; Luckin 6-K; Inside Retail | Đã sửa trong v4 |
| THẤP | F8 | Tổng chi phí nhân sự +102,3 triệu (1.000,1 so với 897,8) có sẵn trong S7 trang 5, gồm cả giá vốn và R&D; nhân sự giải thích tối đa ≈ 27%, và câu "chủ yếu do nhân sự" khó khớp | S7 trang 5 | Đã sửa trong v4 |
| THẤP | F9 | Sổ nguồn thiếu URL cho Guming, Meituan, Auntea Jenny (mã 2589), Luckin; JSON và báo cáo dùng nhãn S không đồng bộ | tệp JSON | Đã sửa trong v4 (JSON cập nhật) |

Các nhận định của v3 kiểm lại và khớp nguồn gốc: số liệu Guming, Meituan (lỗ hoạt động H1 −3.778,6; Q2 +2.691,2; Q1 −6.469,8), Auntea Jenny (13.155 so với 9.436), Luckin (−11,1%), Chagee (−16,1%) và Nayuki (−13,1%), giá Investing.com (−11,8%), Tân Hoa Xã 2026-08-12, Winshang (thực tế 2023-06-26), lãnh đạo, tiền IPO, nhân viên, cổ tức đặc biệt, tiền 21.640,7 triệu, trích lập tồn kho, bảng cửa hàng, ngưỡng kịch bản.

## Kiểm tra phép tính

Tái tính bằng `python3 -I`: khớp ở độ chính xác trình bày, trừ các lỗi ở F7. Gồm: biên gộp H2 2025 30,75%; phân rã hiệu ứng (−184,6 và +107,9 triệu; biên gộp 37,5% mức giảm); tỷ lệ chi phí 11,39% so với 9,08%; sở hữu (153.997.224 = 40,57%; hai người 81,13%; gồm nền tảng 81,99%; 315.044.663 khớp 83,55% của cáo bạch); cổ tức (HK$ 3,0830; 90,30% hiện diện); FULU (285.600 − 271.875 = 13.725); pha loãng 3,167%; OCF/lợi nhuận H1 2026 0,884 và H1 2025 1,205.

## Hạn chế của lần kiểm duyệt

`WebFetch` không đọc được văn bản PDF (dùng `curl` + `pdftotext` ngoài repo). Chưa đọc toàn văn S3, S5, cáo bạch hay báo cáo giữa kỳ; chỉ đọc các phần liên quan. Việc đã trả cổ tức ngày 2026-11-06 vẫn chưa xác minh. Chagee và Nayuki chưa có báo cáo gốc đọc được qua nguồn của bên này (Nayuki chỉ có bản tóm tắt). Chưa tìm được bản chính thức của dự thảo giám sát nhượng quyền 2023.

## Kết luận của agent kiểm duyệt

`KHÔNG_ĐẠT`. Mười phát hiện lần 2 đã xử lý đúng hướng; số liệu mới về đối thủ, giá, quy định và phép tính khớp nguồn gốc. Còn 1 lỗi nghiêm trọng (F1: báo cáo lưu chuyển tiền tệ H1 2026 đã có sẵn và vi phạm hai mốc do chính v3 đặt ra). Cần sửa F1–F4 và F7, rồi chạy lại kiểm nguồn lần 4 trên bản v4 cố định, kèm Interim Report 2026 và cáo bạch đã lưu cùng mã băm. Phản biện rủi ro là bước riêng.
