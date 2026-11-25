# Biên bản kiểm duyệt: MIXUE Group (2097.HK), đọc báo cáo tài chính FY2022–FY2025 và H1 2026 (bản nháp v2)

> Điều phối viên lưu bản tóm lược từ báo cáo của subagent `source-fact-checker` (lần kiểm 2). Giữ nguyên kết luận, mức độ và bằng chứng chính; không thêm nhận định mới.

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-25 08:50 +07` (giờ máy theo agent; bắt đầu khoảng 08:42)
- Chốt dữ liệu lúc: `2026-11-25 08:35 +07` (khớp báo cáo đích v2)
- Phạm vi: toàn bộ v2; 13 phát hiện lần 1; nội dung mới (cầu nối H1 2026, tồn kho, nhân viên, chủ nhượng quyền, tỷ giá, cổ đông, FULU, cổ tức đặc biệt, bảng cửa hàng, doanh thu ngoài đại lục, tỷ lệ đóng cửa hàng, thuế, CAGR, nhãn nhận định, nguồn thứ cấp T1–T8)
- Báo cáo đích: `research/companies/HK/reviews/2097-mixue-draft-v2-sha-ddcbc7c1.md` (bản sao nguyên vẹn của v2)
- SHA-256 nội dung đích: `ddcbc7c1b55849ad6c4d6fdc068966a6a18d0f5d05b66e8013d83ec3d6916f2d` (agent tự tính bằng `validate_report.py --print-hash`, khớp)
- Kết luận: `KHÔNG_ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `1`

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

Ngày truy cập 2026-11-25. Agent tải lại 7 PDF HKEXnews chính (S1–S7) bằng `WebFetch`, băm SHA-256 và so với `SHA256SUMS.txt`: 7/7 khớp; đọc văn bản bằng `pdftotext`. Mở thêm: kết quả bỏ phiếu ĐHĐCĐ 2026-06-26 (S9, `5fc40111…`), thông báo cổ tức đặc biệt 2026-08-27 (S10, `82814b83…`), thông báo họp cổ đông bất thường 2026-09-11 (HKEXnews, một nghị quyết thường về cổ tức đặc biệt, họp 2026-09-30), thông báo họp HĐQT 2026-08-17, bản sao Eastmoney của kết quả biểu quyết 2026-09-30 (S11, chưa tìm thấy bản HKEXnews gốc), và các bài thứ cấp KrASIA/Nikkei, The Standard (Meituan Q2; vụ chanh cũ), Inside Retail (Chagee), Caixin (hai bài), 36Kr, Huxiu.

## Phát hiện lần 1: trạng thái trong v2

12/13 mục `ĐÃ_SỬA` (nguyên nhân biên gộp 2022, cổ tức đặc biệt, ban lãnh đạo, khách hàng ≥10%, nợ hợp đồng, máy rót và thiết bị, ngoại hối và FULU trong mẫu số, nhãn và thuế suất, số làm tròn, CAGR/ROE/ngày tồn kho, số liệu có sẵn trong nguồn, nhãn cột); 1 mục `SỬA_CHƯA_ĐỦ` (#4, lưu trữ nguồn: S9, S10 và văn kiện ĐHĐCĐ bất thường chưa được lưu kèm mã băm).

## Phát hiện mới trong v2

| Mức độ | Mã | Phát hiện | Bằng chứng | Trạng thái (sau khi sửa v3) |
|---|---|---|---|---|
| NGHIÊM_TRỌNG | N1 | v2 gộp hai nhà sáng lập thành 40,57% chung và suy ra "khai hai lần, sở hữu chung". Nguồn ghi **từng** người ≈ 40,57% là chủ sở hữu hưởng lợi, hai nền tảng nhân viên giữ số bằng nhau, nên cách đọc tự nhiên là hai lô riêng (tổng ≈ 81–82%); nguồn không nêu tổng chung | S5 bảng "Interests in our Company"; điều phối viên tự kiểm trên PDF: cả hai ghi riêng 100.098.196 và 53.899.028 cổ phiếu | Đã sửa trong v3: tách số từng người, tổng chung `CHƯA_BIẾT` |
| CAO | N2 | v2 bỏ sót việc mua FULU là giao dịch bên liên quan: bà Tian Haixia (vợ ông Zhang Hongfu) nắm ≈ 60,05% FULU; công ty mua 51% bằng 285,6 triệu RMB tiền mặt; lợi thế thương mại 91,85 triệu; v2 còn ghi giá mua là chưa biết | S5 báo cáo HĐQT trang 58–59, thuyết minh 40–41; điều phối viên đã grep và xác nhận | Đã sửa trong v3 |
| TRUNG_BÌNH | N3 | Câu "sụt lợi nhuận chủ yếu từ chi phí, không phải từ biên gộp": phân rã theo hiệu ứng cho biên gộp góp ≈ 184,6 triệu (≈ 37%), tỷ lệ chi phí ≈ 350,7 triệu (≈ 71%), lỗ tỷ giá thêm ≈ 111,6 triệu (≈ 23%) | tái tính từ S7 | Đã sửa trong v3 |
| TRUNG_BÌNH | N4 | Việc đổi CEO hiệu lực 2026-03-24 nằm **trong** H1 2026, không phải "ngay trước"; gắn nhãn `PHÉP_TÍNH` là sai và gợi nhân quả | S5, S7 | Đã sửa trong v3 |
| THẤP | N5 | Ô "1.795 ngoài đại lục cuối 2022" đúng (270 cuối 2021; 1.795 cuối 2022; tổng 20.001 và 28.983); chú thích "cần đối chiếu lại" lỗi thời | S1 trang 333 | Đã sửa trong v3 |
| THẤP | N6 | Nguồn thứ cấp T1–T8 gắn nhãn đúng; ba điểm không truy được: HK$ 201,2 ngày 10/7, 22,8 triệu cổ phiếu nộp CSRC, "Auntea Jenny doanh thu tăng mạnh" (Caixin chỉ nêu lợi nhuận); câu "người viết chưa tự mở" lỗi thời | các bài T | Đã sửa trong v3 (bỏ ba điểm, cập nhật câu) |
| THẤP | N7 | Nhãn: mục rủi ro 3 có vế `SUY_LUẬN` gắn chung `SỰ_THẬT`; mô tả JD.com không có nguồn trong sổ | S5 | Đã sửa trong v3 |
| THẤP | N8 | Làm tròn: chênh thuế 2,35% → 2,4%; chi phí/doanh thu H1 2025 9,08%; "≈ 5,2%" thuộc mức 153,8 triệu, không thuộc phần tăng 111,6 triệu (3,75%); "giảm thêm 1,2 điểm" là so với H1 2025, dễ hiểu nhầm | tái tính | Đã sửa trong v3 |
| THẤP | N9 | Ô tăng trưởng H1 2025 để `n/a` dù S6 cho +39,3%; thiếu tăng trưởng lợi nhuận theo nửa năm (+44,1% H1 2025; +25,0% H2 2025; −14,7% H1 2026); thiếu bằng chứng trái chiều trích lập tồn kho H1 giảm (21,0 so với 32,5 triệu) | S6, S7 thuyết minh 5 | Đã sửa trong v3 |
| THẤP | N10 | S9, S10, thông báo ĐHĐCĐ và S11 chưa lưu kèm SHA-256 trong `data/raw`; việc đã trả cổ tức chưa xác minh | repo | Đã lưu S9, S10 và thông báo họp 2026-09-11 vào `data/raw/mixue-hkex/` kèm SHA-256; S11 (bản sao Eastmoney) và việc đã trả vẫn chưa xác minh |

## Kiểm tra phép tính

Agent tái tính bằng `python3 -I` từ JSON sau khi đối chiếu đầu vào với PDF. Mọi phép tính của v2 khớp ở độ chính xác trình bày: tăng trưởng, biên, CAGR (2022→2025 35,21% và 43,33%; 2021→2025 lợi nhuận 32,69%), thuế suất hiệu dụng, H1 2026, doanh thu hàng hóa/cửa hàng (−16,5% / −14,6% / −17,2%), tỷ lệ đóng cửa hàng, doanh thu H2 (+32,03%), tồn kho (+65,80% so với +37,81%; ngày tồn kho cuối kỳ 48,2 → 58,0), nợ hợp đồng (1,45%; 5,28 ngày), ROE, OCF/lợi nhuận, FCF, cổ tức đặc biệt (1.005,99 triệu; HK$ 3,0830/cổ phiếu), tiền IPO (35,5%). Ngoại lệ: lỗi làm tròn ở N8.

## Hạn chế của lần kiểm duyệt

`WebFetch` không đọc được văn bản PDF (dùng `pdftotext` trên bản tải về sau khi so mã băm). Hầu hết nguồn chính là hồ sơ của chính doanh nghiệp; chưa có nguồn độc lập thứ hai cho số liệu tài chính. ĐHĐCĐ bất thường 2026-09-30 chỉ mở được qua bản sao Eastmoney. Chưa đọc toàn văn S3, S5 hay cáo bạch đầy đủ, nên N1 dựa vào cấu trúc bảng S5; cần mở mục "Substantial Shareholders" của cáo bạch để chốt. Bài Caixin 2026-01-10 chỉ đọc được phần đầu.

## Kết luận của agent kiểm duyệt

`KHÔNG_ĐẠT`. Không còn lỗi nghiêm trọng về số liệu tài chính; 12/13 phát hiện lần 1 đã sửa. Còn 1 lỗi nghiêm trọng (tổng sở hữu của hai nhà sáng lập, N1) và 1 phát hiện mức CAO (FULU là giao dịch bên liên quan, N2); cần sửa N1–N2, nên sửa N3–N4, rồi chạy lại kiểm nguồn lần 3 trên bản v3 cố định. Phản biện rủi ro là bước riêng, không nằm trong biên bản này.
