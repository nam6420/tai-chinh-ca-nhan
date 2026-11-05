# Biên bản kiểm nguồn: Tổng Công ty Cổ phần Bảo hiểm Ngân hàng Đầu tư và Phát triển Việt Nam (BIC) — Vòng 2

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-05 11:55 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-11-05 11:20 Asia/Ho_Chi_Minh`
- Phạm vi: BCTC hợp nhất kiểm toán năm 2025 của BIC (EY Việt Nam ký 20/03/2026, số 61665798/68900051-HN) đối chiếu chéo với BCTC hợp nhất Quý 4/2025 (28/01/2026), cơ cấu phí gốc theo nghiệp vụ, giao dịch bên liên quan với ngân hàng mẹ BIDV, tam giác phát triển tổn thất (Loss Development Triangle), thuyết minh điều chỉnh hồi tố năm 2024 theo Kiểm toán Nhà nước và 3 kịch bản định giá Justified P/B.
- Báo cáo đích: `research/companies/VN/BIC/report.md`
- SHA-256 nội dung đích: `320bb3acd1fe936935b9c56c1ff313790e2fd76c8bfa876341b51c9dde5a948b`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Phiên chính ghi từ kết quả nhánh độc lập `source-fact-checker` Vòng 2 ([conversation](conversation://526f4218-bc29-48c8-9ac2-f82677d5dda0)); không tự thay kết luận.

## Các nguồn Internet và tệp gốc đã tự mở trong lượt kiểm duyệt

| Nguồn / Tệp | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích |
|---|---|---|---|
| `bic-fy2025-audited-mirror.pdf` (`https://static2.vietstock.vn/data/HOSE/2025/BCTC/VN/NAM/BIC_Baocaotaichinh_2025_Kiemtoan_Hopnhat.pdf`) | Ký `20/03/2026`; kỳ năm 2025 (`01/01/2025–31/12/2025`) | `2026-11-05` | Đọc trực tiếp trang 5–17 (Báo cáo kiểm toán, BCĐKT, KQKD, LCTT) và Thuyết minh 1, 4, 6, 7, 13, 22, 23, 24–35, 36, 40.3, 41.1, 43 (trang 18–85) |
| `bic-q4-fy2025-signed-mirror.pdf` (`https://static2.vietstock.vn/data/HOSE/2025/BCTC/VN/QUY%204/BIC_Baocaotaichinh_Q4_2025_Hopnhat.pdf`) | Ký `28/01/2026`; Quý 4 & cả năm 2025 chưa kiểm toán | `2026-11-05` | Đối chiếu chéo số liệu riêng Quý 4/2025 (tác động bão lũ) và chênh lệch trước – sau kiểm toán năm 2025 |

## Phát hiện và xác nhận xử lý Vòng 2

| Mức | Phát hiện Vòng 1 | Bằng chứng / xử lý ở Vòng 2 | Trạng thái |
|---|---|---|---|
| Cao (Vòng 1) | Tỷ lệ biên khả năng thanh toán tại `31/12/2024 (trình bày lại)` tại Thuyết minh 40.3 (trang 67 BCTC / trang PDF 70). | Đã cập nhật chính xác trên bảng chỉ tiêu (dòng 68): tại `31/12/2024 (trình bày lại)`, biên khả năng thanh toán là **`249%`** (`2.373,53 tỷ / 953,78 tỷ VND`), tăng `+36 điểm phần trăm` lên **`285%`** (`2.706,43 tỷ / 950,71 tỷ VND`) tại `31/12/2025`. | Đã xử lý triệt để (`0` lỗi tồn đọng) |
| Cao (Vòng 1) | Số liệu năm 2024 trình bày lại của cơ cấu phí bảo hiểm gốc thuần theo nghiệp vụ (Thuyết minh 24.1 trang 53 PDF) và một số dòng chi phí năm 2024 trên KQKD kiểm toán. | Đã cập nhật khớp 100% BCTC kiểm toán năm 2025: năm 2024 trình bày lại mảng Sức khỏe & tai nạn con người `2.519,23 tỷ VND` (`2025: 2.357,88 tỷ`, giảm `-6,40%`), Cháy nổ `1.028,64 tỷ VND` (`+16,08%`), Xe cơ giới `1.052,77 tỷ VND` (`+7,10%`), `NWP` 2024 `4.016,27 tỷ VND`, Chi bồi thường giữ lại + DP dao động lớn 2024 `971,80 tỷ VND`, Chi khác KDBH trực tiếp 2024 `2.102,23 tỷ VND`, CPQLDN 2024 `911,83 tỷ VND`, `EPS` 2024 trình bày lại `3.634 VND/CP`, tiền gửi có kỳ hạn tại `BIDV` đầu năm `4.197,20 tỷ VND`. | Đã xử lý triệt để (`0` lỗi tồn đọng) |
| Cao (Vòng 1) | `EBT` trước kiểm toán (`678,79 tỷ VND`), hoàn nhập dự phòng chứng khoán kinh doanh & đầu tư (`21,87 tỷ VND`), Thông báo Kiểm toán Nhà nước số `380/TB-KTNN` ngày `09/10/2025` (TM 43 tr. 83–84), tổng ước tính bồi thường giữ lại lũy kế (`4.456,46 tỷ VND`, TM 41.1 tr. 73), tỷ lệ sở hữu `BIDV Metlife` (`4,37%`) và mã băm `SHA-256` của `S2`. | Đã cập nhật chính xác toàn bộ trên `report.md` và `source-register.md` (`S2 SHA-256: 27d4788f34794923cd3c1989bfd30d72f8229a115ee3f2f86a9dd70e4e34f5d8`, `2.826.711 byte`). | Đã xử lý triệt để (`0` lỗi tồn đọng) |

## Kiểm tra phép tính

- Đã chạy `bic_metrics()` và `bic_scenarios()` trong `research/companies/VN/calc_insurance_profiles.py` (`unittest OK`):
  - Chênh lệch kiểm toán lợi nhuận gộp HĐKD bảo hiểm: `963,19 - 994,94 = -31,75 tỷ VND` (do tái phân loại `+31,53 tỷ VND` từ CPQLDN sang Chi khác HĐKD bảo hiểm trực tiếp).
  - Tỷ lệ bồi thường giữ lại (`Loss Ratio`): `1.189,93 / 3.948,01 = 30,14%`; `Combined Ratio` trực tiếp trước hoa hồng nhượng tái `84,17%`, sau hoa hồng nhượng tái `75,60%` (và `95,87%` nếu cộng đủ `800,17 tỷ VND` CPQLDN).
  - Tập trung tại ngân hàng mẹ `BIDV`: tiền gửi có kỳ hạn `4.428,50 / 6.665,62 = 66,44%` danh mục `HTM` (`1,31x` VCSH); hoa hồng đại lý `755,65 / 5.702,42 = 13,25%` `GWP`.
  - `BVPS` công ty mẹ cuối 2025: `3.250,057661887 tỷ VND / 202,067057 triệu CP = 16.084,05 VND/CP`; `ROE` công ty mẹ bình quân `17,51%`.
  - Định giá `Justified P/B`: Bất lợi `1,2857x` (`20.679,50 VND/CP`), Cơ sở `2,0000x` (`32.168,11 VND/CP`), Thuận lợi `2,7778x` (`44.677,93 VND/CP`).

## Hạn chế của lần kiểm duyệt

- Tệp PDF BCTC hợp nhất kiểm toán năm 2025 và BCTC Quý 4/2025 của `BIC` là bản ký số/dấu đỏ chính thức lưu trên CDN Vietstock. Tỷ trọng phí bảo hiểm gốc từng dòng sản phẩm bán qua quầy `BIDV` so với kênh đại lý ngoài `BIDV` chưa được tách riêng trên Thuyết minh 36 nên được gắn nhãn `CHƯA_BIẾT` đúng quy định.

## Kết luận của agent kiểm duyệt

`ĐẠT` (`0` lỗi nghiêm trọng, `0` lỗi cao). Đủ điều kiện gỡ nhãn bản nháp và xuất bản chính thức.
