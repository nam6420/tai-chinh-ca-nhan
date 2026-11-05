# Biên bản kiểm nguồn: Ngành Bảo hiểm Việt Nam (VN-insurance) — Vòng 2

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-05 11:55 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-11-05 11:20 Asia/Ho_Chi_Minh`
- Phạm vi: Khung pháp lý Luật Kinh doanh bảo hiểm 31/VBHN-VPQH, Nghị định 46/2023/NĐ-CP, Thông tư 67/2023/TT-BTC (44/VBHN-BTC), bảng so sánh kinh tế đơn vị BVH – PVI – BIC (FY2025 đã kiểm toán), đối chiếu chuẩn mực toàn cầu (GEICO / Berkshire Hathaway FY2025 10-K) và mô-đun tính toán calc_insurance_profiles.py.
- Báo cáo đích: `research/sectors/VN-insurance/report.md`
- SHA-256 nội dung đích: `795fa838ac2d630d3113c949c71bf55e725709df06cd19497fb38e97f111b97f`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Phiên chính ghi từ kết quả nhánh độc lập `source-fact-checker` Vòng 2 ([conversation](conversation://526f4218-bc29-48c8-9ac2-f82677d5dda0)); không tự thay kết luận.

## Các nguồn Internet và tệp gốc đã tự mở trong lượt kiểm duyệt

| Nguồn / Tệp | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích |
|---|---|---|---|
| `31-vbhn-vpqh.pdf`, `46-2023-nd-cp.pdf`, `44-vbhn-btc.pdf` (`https://vanban.chinhphu.vn`) | `2023–2025` | `2026-11-05` | Đối chiếu từng điều khoản: Điều 108, 109, 156, 157 `31/VBHN-VPQH`; Điều 35, 62 `46/2023/NĐ-CP`; Điều 51, 52, 53 `44/VBHN-BTC` |
| `bvh-fy2025-audited-mirror.pdf`, `pvi-fy2025-audited-mirror.pdf`, `bic-fy2025-audited-mirror.pdf` | BCTC hợp nhất kiểm toán FY2025 (`31/12/2025`) | `2026-11-05` | Đối chiếu toàn bộ chỉ tiêu bảng so sánh ngang `BVH – PVI – BIC` và tỷ lệ biên khả năng thanh toán |
| `berkshire-2025ar.pdf` (`https://www.berkshirehathaway.com/2025ar/2025ar.pdf`) | FY2025 (`02/03/2026`) | `2026-11-05` | Đối chiếu số liệu `GEICO` tại trang `K-36` và tổng `Float` tại trang `K-35`, `K-45` |

## Phát hiện và xác nhận xử lý Vòng 2

| Mức | Phát hiện Vòng 1 | Bằng chứng / xử lý ở Vòng 2 | Trạng thái |
|---|---|---|---|
| Nghiêm trọng (Vòng 1) | Sai lệch số liệu `GEICO` năm 2025 ở dòng 85 do dùng bảng ước tính phụ thay vì trang `K-36` `berkshire-2025ar.pdf`. | Đã cập nhật khớp 100% trang `K-36`: `NEP = 44.481 triệu USD` (phí phát hành `45.193 triệu USD`), `Losses & LAE = 32.144 triệu USD` (`72,26%`), `Underwriting expenses = 5.513 triệu USD` (`12,39%`), `Combined Ratio = 84,66%`, lợi nhuận khai thác trước thuế `6.824 triệu USD`. | Đã xử lý triệt để (`0` lỗi tồn đọng) |
| Cao (Vòng 1) | Vốn điều lệ tối thiểu doanh nghiệp tái bảo hiểm và điều khoản trần hoa hồng năm đầu `UL`/`Unit-Linked` (`30%`), quầy tư vấn riêng tại ngân hàng (Điểm e Khoản 1 Điều 62 NĐ 46). | Đã cập nhật chính xác vốn tối thiểu tái bảo hiểm (`500 / 900 / 1.400 tỷ VND`, Khoản 4 Điều 35 NĐ `46/2023/NĐ-CP`), trần hoa hồng năm 1 `30%` cho cả `UL` và `Unit-Linked` từ `01/07/2024` (Mục 3.2 Khoản 3 Điều 51 `44/VBHN-BTC`) và Điểm e Khoản 1 Điều 62 NĐ `46/2023/NĐ-CP`. | Đã xử lý triệt để (`0` lỗi tồn đọng) |
| Cao (Vòng 1) | Tỷ lệ biên khả năng thanh toán năm 2024 của Bảo Việt Nhân thọ (`104%`) và `BIC` năm 2024 trình bày lại (`249%`); đồng bộ hash `SHA-256` trong `source-register.md`. | Đã cập nhật chính xác trên bảng so sánh dòng 80 và đồng bộ 100% mã băm `SHA-256` trong `source-register.md` với `data/raw/insurance-review-sources-2026-11-05.json`. | Đã xử lý triệt để (`0` lỗi tồn đọng) |

## Kiểm tra phép tính

- Đã chạy `python3 -m unittest discover tests` (`111` bài kiểm thử đạt `OK`).
- Toàn bộ bảng chỉ số `BVH`, `PVI`, `BIC` (dòng 61–80) và `GEICO` (dòng 85–88) khớp tuyệt đối với nguồn sơ cấp và mô-đun `research/companies/VN/calc_insurance_profiles.py`.

## Hạn chế của lần kiểm duyệt

- Các tệp BCTC hợp nhất kiểm toán năm 2025 của `BVH`, `PVI`, `BIC` được lưu bản gương từ CDN công bố thông tin Vietstock (khớp chữ ký số/con dấu kiểm toán của `EY Việt Nam` và `PwC Việt Nam`, đã lưu kèm mã băm `SHA-256` trong `data/raw/insurance-review-sources-2026-11-05.json`). Niên giám thị trường bảo hiểm năm 2025 bản chi tiết từng doanh nghiệp chưa niêm yết của Cục Quản lý, giám sát bảo hiểm được gắn nhãn `CHƯA_BIẾT` đúng quy định.

## Kết luận của agent kiểm duyệt

`ĐẠT` (`0` lỗi nghiêm trọng, `0` lỗi cao). Đủ điều kiện gỡ nhãn bản nháp và xuất bản chính thức.
