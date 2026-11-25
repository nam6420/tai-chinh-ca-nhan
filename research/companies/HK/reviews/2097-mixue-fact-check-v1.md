# Biên bản kiểm duyệt: MIXUE Group (2097.HK), đọc báo cáo tài chính FY2022–FY2025 và H1 2026 (bản nháp v1)

> Điều phối viên lưu bản tóm lược từ báo cáo của subagent `source-fact-checker` (bản đầy đủ nằm trong báo cáo hand-back của phiên làm việc). Bản tóm lược giữ nguyên kết luận, mức độ và bằng chứng chính; không thêm nhận định mới.

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-25 08:27 +07` (giờ máy theo báo cáo của agent; bắt đầu khoảng 08:21)
- Chốt dữ liệu lúc: `2026-11-25 08:11 +07` (khớp báo cáo đích v1)
- Phạm vi: lãi lỗ 2021–2025, cơ cấu doanh thu 2022–2025, bảng cân đối, dòng tiền, cửa hàng, H1 2026, tỷ lệ chi phí, lời giải thích của công ty, ban lãnh đạo, tuyên bố khách hàng ≥10%, ghi chú IPO, nhãn nhận định, tái tính phép tính
- Báo cáo đích: `research/companies/HK/reviews/2097-mixue-draft-v1-sha-a682acf7.md` (bản sao nguyên vẹn của bản nháp v1; bản đang làm việc `research/companies/HK/2097-mixue-financial-statements-2026-11-25.md` đã được sửa thành v2)
- SHA-256 nội dung đích: `a682acf7ef69738aea03104173140ff21aa1ea50e1cbd87e2a15f529876ef6b7`
- Kết luận: `KHÔNG_ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `1` (tại thời điểm kiểm duyệt v1)

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

Agent tải lại 7 PDF HKEXnews bằng `WebFetch` trong lượt này, băm SHA-256 và so với `data/raw/mixue-hkex/SHA256SUMS.txt`: cả 7 khớp; sau đó đọc văn bản bằng `pdftotext`. Ngày truy cập: 2026-11-25.

| URL | Kỳ dữ liệu | Mục đích |
|---|---|---|
| https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0221/11543478/2025022100039.pdf | Cáo bạch, FY2021–FY2023, 9T2024 | Lãi lỗ, cơ cấu doanh thu, giải thích biên gộp 2022, capex, cửa hàng 2021–2022 |
| https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0326/2025032601256.pdf | FY2024 | Cửa hàng, chủ nhượng quyền, khách hàng ≥10% |
| https://www.hkexnews.hk/listedco/listconews/sehk/2025/0423/2025042301969.pdf | AR 2024 | Đối chiếu tóm tắt 2021–2024 |
| https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0324/2026032400179.pdf | FY2025 | Lãi lỗ, cân đối, doanh thu theo loại, MD&A |
| https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0423/2026042301901.pdf | AR 2025 | Dòng tiền, lãnh đạo, lợi thế thương mại, sử dụng tiền IPO |
| https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0827/2025082700283.pdf | H1 2025 | Đối chiếu số so sánh |
| https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0827/2026082700177.pdf | H1 2026 | Lãi lỗ H1, MD&A, cổ tức đặc biệt, ngoại hối |
| https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0626/2026062602855.pdf | Kết quả ĐHĐCĐ 2026-06-26 | Số cổ phiếu 379.618.800 |
| https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0827/2026082700183.pdf | Thông báo cổ tức 2026-08-27 | Cổ tức đặc biệt RMB 2,65/cổ phiếu |
| https://pdf.dfcfw.com/pdf/H2_AN202609301830055247_1.pdf | ĐHĐCĐ bất thường 2026-09-30 (bản sao Eastmoney, không phải HKEXnews) | Xác nhận thông qua cổ tức đặc biệt; chưa mở bản gốc |

## Phát hiện

| # | Mức độ | Phần | Phát hiện | Bằng chứng | Trạng thái (sau khi sửa v2) |
|---|---|---|---|---|---|
| 1 | NGHIÊM_TRỌNG | Nguyên nhân biên gộp 2022 và phí nhượng quyền được miễn | v1 ghi nguyên nhân là `CHƯA_BIẾT` và nói phí miễn làm doanh thu dịch vụ "tăng chậm (+40,6%)". Cáo bạch giải thích biên gộp hàng hóa giảm 31,4% → 27,8% do giá nguyên liệu biến động và giảm giá trung bình 15% cho 69 mặt hàng (23,1% doanh thu 2022) nhằm giảm tác động COVID-19; doanh thu dịch vụ +40,6% là tăng nhanh | S1 chương Financial Information; điều phối viên tự kiểm lại bằng `pdftotext` | Đã sửa trong v2 |
| 2 | CAO | Cổ tức | v1 bỏ sót cổ tức đặc biệt RMB 2,65/cổ phiếu (≈ RMB 1.006,0 triệu), trả vào khoảng 2026-11-06, đã được ĐHĐCĐ bất thường thông qua 2026-09-30 (theo bản sao Eastmoney) | S7 trang 16, thuyết minh 7; 379.618.800 × 2,65 = 1.005,99 triệu | Đã sửa trong v2; "đã trả" chưa xác minh |
| 3 | TRUNG_BÌNH | Ban lãnh đạo | v1 dựa vào báo chí chưa mở trong khi S5 xác nhận trực tiếp việc Zhang Hongfu sang đồng chủ tịch và Zhang Yuan làm CEO từ 2026-03-24 | S5 báo cáo quản trị | Đã sửa trong v2 |
| 4 | TRUNG_BÌNH | Ghi chú IPO trong JSON | Giá chào bán HK$202,5 đúng và có nguồn gốc mở được (S1, S2, S3, S5); ghi chú "chưa mở" lỗi thời; văn kiện ĐHĐCĐ chưa lưu | S1, S2, S3, S5 | Đã sửa JSON; văn kiện ĐHĐCĐ vẫn chưa lưu trong `data/raw` |
| 5 | THẤP | Khách hàng ≥10% | Đúng nhưng cần nêu kỳ: FY2023–FY2025 và H1 2025–H1 2026; FY2022 chưa xác nhận | S4 thuyết minh 2, S2, S7, S5 | Đã sửa trong v2 |
| 6 | TRUNG_BÌNH | "Nợ hợp đồng lớn" | Không có căn cứ: nợ hợp đồng 485,1 triệu = 1,4% doanh thu 2025 (≈ 5,3 ngày doanh thu) | S4 thuyết minh 3 | Đã sửa trong v2 |
| 7 | TRUNG_BÌNH | Doanh thu thiết bị và máy rót thông minh | Nguồn không xác nhận mối liên hệ; S7: máy rót tăng lên trên 18.000 cửa hàng nhưng doanh thu thiết bị H1 2026 giảm 18,2% | S4, S7 | Đã sửa trong v2 |
| 8 | TRUNG_BÌNH | H1 2026 | Thiếu lỗ ngoại hối (153,8 triệu so với 42,2 triệu) và việc 1.354 cửa hàng FULU nằm trong mẫu số số cửa hàng | S7 thuyết minh 5; S4 | Đã sửa trong v2 |
| 9 | THẤP | Nhãn, thuế suất | "Giảm đều" sai (2023 và 2024 cùng 23,3%); vế suy luận gắn nhầm nhãn | tái tính | Đã sửa trong v2 |
| 10 | THẤP | Số làm tròn từ lời văn | Capex 2021–2023 và số chi phí H1 làm tròn trong JSON; bảng chính xác có sẵn (capex PPE 944.523; 997.293; 1.685.292; S&D H1 1.122.937/913.679; admin 610.046/437.650; thuế 656.435/750.068) | S1 bảng Capital expenditures; S7 báo cáo lãi lỗ | JSON đã cập nhật |
| 11 | THẤP | CAGR, ROE, ngày tồn kho | Cần nêu năm gốc, CAGR lợi nhuận 2021→2025 là 32,7%, ngày tồn kho theo số cuối kỳ 48,2 → 58,0 | tái tính | Đã sửa trong v2 |
| 12 | THẤP | `CHƯA_BIẾT` có sẵn trong nguồn | Doanh thu ngoài đại lục 2021–2023 (50,1; 540,6; 1.486,9 triệu RMB) và tổng cửa hàng 2021–2022 (20.001; 28.983) có trong S1 | S1 | Đã sửa trong v2 |
| 13 | THẤP | Nhãn cột / mốc thời gian | "Tiền và số dư ngân hàng" gồm tiền gửi có kỳ hạn; số cơ sở sản xuất/kho thuộc cuối 2025 (30/6/2026: 6 cơ sở, 31 kho) | S4, S7 | Đã sửa trong v2 |

Các nhận định ĐẠT (không phát hiện sai): lãi lỗ 2021–2025, cơ cấu doanh thu 2022–2025, bảng cân đối 2021–2025, OCF, chuyển động cửa hàng, số liệu H1 2026, lời giải thích biên gộp 2025 và H1 2026, ngày xuất bản và số trang của sổ nguồn.

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Agent tái tính bằng `python3 -I` từ JSON sau khi đối chiếu đầu vào với PDF: tăng trưởng, biên, CAGR, ROE bình quân, OCF/lợi nhuận, FCF, ngày tồn kho, doanh thu/cửa hàng, thay đổi H1; **mọi phép tính khớp bản nháp ở độ chính xác trình bày**. Bằng chứng trái chiều đề xuất: doanh thu nửa cuối 2025 tăng +32,0% so với nửa cuối 2024 (điểm gãy đến đột ngột ở H1 2026); cổ tức đặc biệt; biên gộp dịch vụ nhượng quyền vẫn tăng sau khi miễn phí.

## Hạn chế của lần kiểm duyệt

`WebFetch` không đọc được văn bản PDF; agent dùng `pdftotext` trên bản chính nó tải về và so mã băm với repo. Toàn bộ nguồn chính là hồ sơ của chính doanh nghiệp; chưa có nguồn độc lập thứ hai. ĐHĐCĐ bất thường chỉ mở qua bản sao Eastmoney. Chưa đọc toàn văn S3 và S5.

## Kết luận của agent kiểm duyệt

`KHÔNG_ĐẠT` ở bản v1: số liệu gốc nhìn chung đúng, nhưng có 1 lỗi nghiêm trọng (nguyên nhân biên gộp 2022) và các thiếu sót mức CAO/TRUNG_BÌNH. Agent yêu cầu chạy lại kiểm nguồn trên bản nháp mới trước khi đổi trạng thái.
