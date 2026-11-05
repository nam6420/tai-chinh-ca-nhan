# Biên bản kiểm nguồn: Công ty Cổ phần PVI (PVI) — Vòng 2

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-05 11:55 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-11-05 11:20 Asia/Ho_Chi_Minh`
- Phạm vi: BCTC hợp nhất kiểm toán năm 2025 của CTCP PVI (PVI, PwC Việt Nam ký 11/03/2026, số HAN 4235), cầu nối doanh thu phí gốc – nhận tái – nhượng tái, cơ cấu dự phòng nghiệp vụ và tài sản tái bảo hiểm, báo cáo bộ phận (Bảo hiểm phi nhân thọ vs. Tái bảo hiểm), thuyết minh điều chỉnh hồi tố năm 2024 theo Kiểm toán Nhà nước và 3 kịch bản định giá Justified P/B.
- Báo cáo đích: `research/companies/VN/PVI/report.md`
- SHA-256 nội dung đích: `a964f9640c703ba69c77a7bbf93d95f9adb119b4d43c63d51766211a3134177c`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Phiên chính ghi từ kết quả nhánh độc lập `source-fact-checker` Vòng 2 ([conversation](conversation://526f4218-bc29-48c8-9ac2-f82677d5dda0)); không tự thay kết luận.

## Các nguồn Internet và tệp gốc đã tự mở trong lượt kiểm duyệt

| Nguồn / Tệp | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích |
|---|---|---|---|
| `pvi-fy2025-audited-mirror.pdf` (`https://static2.vietstock.vn/data/HNX/2025/BCTC/VN/NAM/PVI_Baocaotaichinh_2025_Kiemtoan_Hopnhat.pdf`) | Ký `11/03/2026`; kỳ năm 2025 (`01/01/2025–31/12/2025`) | `2026-11-05` | Đọc trực tiếp trang 3–9 (Báo cáo kiểm toán `HAN 4235`, BCĐKT, KQKD, LCTT) và Thuyết minh 1, 3, 4, 5, 6, 7, 18, 19, 23–28, 31, 35, 37 (trang 10–64) |
| `31-vbhn-vpqh.pdf`, `46-2023-nd-cp.pdf`, `44-vbhn-btc.pdf` | `2023–2025` | `2026-11-05` | Đối chiếu quy định nhượng tái bảo hiểm, dự phòng nghiệp vụ phi nhân thọ và lộ trình vốn `RBC` |

## Phát hiện và xác nhận xử lý Vòng 2

| Mức | Phát hiện Vòng 1 | Bằng chứng / xử lý ở Vòng 2 | Trạng thái |
|---|---|---|---|
| Cao (Vòng 1) | Cơ cấu chi tiết 3 quỹ dự phòng nghiệp vụ ngắn hạn gộp (`28.417,50 tỷ VND`) tại Thuyết minh 18(a) trang 42. | Đã cập nhật khớp 100% Thuyết minh 18(a) trang 42: Dự phòng phí chưa được hưởng gộp `9.797,97 tỷ VND` (`2024: 7.843,41 tỷ`), Dự phòng bồi thường gộp `18.126,64 tỷ VND` (`2024: 9.579,22 tỷ`, `+89,23%`), Dự phòng dao động lớn `492,89 tỷ VND` (`2024: 378,34 tỷ`), và dự phòng bồi thường giữ lại ròng `2.757,80 tỷ VND` (`2024: 2.060,75 tỷ VND`). | Đã xử lý triệt để (`0` lỗi tồn đọng) |
| Cao (Vòng 1) | Số liệu Lưu chuyển tiền tệ (trang 8–9), Phải thu hoạt động bảo hiểm (Thuyết minh 5 trang 32) và Nợ xấu / phải thu quá hạn (Thuyết minh 6a & 7 trang 33–34). | Đã cập nhật chính xác: dòng tiền thuần HĐKD `+723,89 tỷ VND` (`2024: +1.575,93 tỷ VND`), HĐĐT `+330,86 tỷ VND`, tiền cuối kỳ `1.012,81 tỷ VND`; Phải thu ngắn hạn khách hàng hoạt động bảo hiểm `2.084,58 tỷ VND` (gồm phải thu phí gốc `614,55 tỷ` và phải thu nhận/nhượng tái bảo hiểm `1.470,03 tỷ VND`; tổng phơi nhiễm tái bảo hiểm `21.614,45 + 1.470,03 = 23.084,48 tỷ VND` = `2,70x` VCSH); phải thu ngắn hạn quá hạn/khó đòi giá gốc `376,63 tỷ VND`, dự phòng `206,47 tỷ VND` (trong đó gốc trái phiếu Sông Đà Thăng Long quá hạn từ 2013 là `180,77 tỷ VND`, đã trích lập 100%). | Đã xử lý triệt để (`0` lỗi tồn đọng) |
| Cao (Vòng 1) | Đồng bộ số liệu so sánh năm 2024 điều chỉnh lại theo Thuyết minh 23–27 (trang 46–48) và Thuyết minh 35 (trang 58–62, theo Công văn `233/KTNN-TH` ngày `22/09/2025` của Kiểm toán Nhà nước). | Đã đồng bộ nhất quán cột năm 2024 đã điều chỉnh lại trên toàn báo cáo, sổ đăng ký nguồn và `calc_insurance_profiles.py`. | Đã xử lý triệt để (`0` lỗi tồn đọng) |
| Trung bình (Vòng 1) | Tỷ lệ sở hữu tại `PVI AM` (`61,96%`), số lượng cổ phiếu của các cổ đông lớn (TM 19b tr. 43), số hiệu kiểm toán `HAN 4235` và mã băm `SHA-256` của `S1`. | Đã cập nhật chính xác trên `report.md` và `source-register.md` (`SHA-256: 2bc0badc1c60d2fdca5c6dbc0fd5e70ca31faf1e3bb0ce07f4fc6f4b8ebbf126`, `22.514.367 byte`). | Đã xử lý triệt để (`0` lỗi tồn đọng) |

## Kiểm tra phép tính

- Đã chạy `pvi_metrics()` và `pvi_scenarios()` trong `research/companies/VN/calc_insurance_profiles.py` (`unittest OK`):
  - Cầu nối doanh thu phí 2025: `14.908,34 + 10.498,98 - 17.178,02 = 8.229,30 tỷ VND` (`NWP`, tỷ lệ giữ lại `32,39%`); trừ tăng dự phòng phí giữ lại `595,40 tỷ VND` ra `NEP = 7.633,90 tỷ VND`.
  - Chi bồi thường giữ lại ròng 2025: `4.380,07 + 2.374,53 - 4.277,17 + 694,65 + 114,54 = 3.286,63 tỷ VND` (`Loss Ratio = 43,05%`).
  - `Combined Ratio` tính đủ `G&A` (`836,36 tỷ VND`): trước hoa hồng nhượng tái `117,02%`, sau hoa hồng nhượng tái (`1.337,61 tỷ VND`) `99,50%`.
  - `BVPS` công ty mẹ cuối 2025: `8.183,980479755 tỷ VND / 234,241867 triệu CP = 34.938,16 VND/CP`; `ROE` công ty mẹ bình quân `13,77%`.
  - Định giá `Justified P/B`: Bất lợi `0,9286x` (`32.442,58 VND/CP`), Cơ sở `1,5091x` (`52.724,86 VND/CP`), Thuận lợi `2,1111x` (`73.758,34 VND/CP`).

## Hạn chế của lần kiểm duyệt

- Tệp PDF BCTC hợp nhất kiểm toán năm 2025 của `PVI` là bản quét có chữ ký và dấu đỏ của CTCP PVI và Công ty TNHH PwC (Việt Nam) lưu trên CDN Vietstock. Các thông tin ngoài thuyết minh `VAS` (cơ cấu bậc tín nhiệm `AAA/AA/A/BBB` của danh mục nhà nhận tái bảo hiểm và biên thanh toán riêng lẻ của `PVI Insurance` / `Hanoi Re`) được gắn nhãn `CHƯA_BIẾT` rõ ràng.

## Kết luận của agent kiểm duyệt

`ĐẠT` (`0` lỗi nghiêm trọng, `0` lỗi cao). Đủ điều kiện gỡ nhãn bản nháp và xuất bản chính thức.
