# Biên bản kiểm nguồn: Tập đoàn Bảo Việt (BVH) — Vòng 2

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-05 11:55 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-11-05 11:20 Asia/Ho_Chi_Minh`
- Phạm vi: BCTC hợp nhất kiểm toán năm 2025 của Tập đoàn Bảo Việt (BVH, EY Việt Nam ký 31/03/2026), cơ cấu phí gốc nhân thọ / phi nhân thọ, dự phòng toán học và dự phòng đảm bảo lãi suất cam kết tối thiểu, giao dịch Repo TPCP, danh mục đầu tư tài chính, biên khả năng thanh toán và 3 kịch bản định giá Justified P/B.
- Báo cáo đích: `research/companies/VN/BVH/report.md`
- SHA-256 nội dung đích: `492b1d938d1e3338cffd2177d676d858715e7e215da001a157dc9a6ce22ce1ab`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Phiên chính ghi từ kết quả nhánh độc lập `source-fact-checker` Vòng 2 ([conversation](conversation://526f4218-bc29-48c8-9ac2-f82677d5dda0)); không tự thay kết luận.

## Các nguồn Internet và tệp gốc đã tự mở trong lượt kiểm duyệt

| Nguồn / Tệp | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích |
|---|---|---|---|
| `bvh-fy2025-audited-mirror.pdf` (`https://static2.vietstock.vn/data/HOSE/2025/BCTC/VN/NAM/BVH_Baocaotaichinh_2025_Kiemtoan_Hopnhat.pdf`) | Ký `31/03/2026`; kỳ năm 2025 (`01/01/2025–31/12/2025`) | `2026-11-05` | Đọc trực tiếp trang 4–14 (BCĐKT, KQKD, LCTT) và Thuyết minh 1, 5, 7, 14, 22, 24, 26–33, 35, 38.3, 40 (trang 16–84) |
| `31-vbhn-vpqh.pdf`, `46-2023-nd-cp.pdf`, `44-vbhn-btc.pdf` | `2023–2025` | `2026-11-05` | Đối chiếu quy định dự phòng nghiệp vụ bảo hiểm nhân thọ, trần hoa hồng đại lý và biên khả năng thanh toán |

## Phát hiện và xác nhận xử lý Vòng 2

| Mức | Phát hiện Vòng 1 | Bằng chứng / xử lý ở Vòng 2 | Trạng thái |
|---|---|---|---|
| Nghiêm trọng (Vòng 1) | Tỷ lệ biên khả năng thanh toán ngày `31/12/2024` của Tổng Công ty Bảo Việt Nhân thọ bị ghi nhầm là `120%` (và Bảo hiểm Bảo Việt `148%`). | Đã đối chiếu trực tiếp trang 84 (Thuyết minh 40) và sửa chính xác trên toàn báo cáo: ngày `31/12/2024`, biên thanh toán của Bảo Việt Nhân thọ là **`104%`** (`8.879.831 / 8.554.813 triệu VND`, tăng nhẹ `+3 điểm phần trăm` lên **`107%`** tại `31/12/2025`), và của Bảo hiểm Bảo Việt là **`145%`** (`2.592.334 / 1.788.087 triệu VND`, đạt **`141%`** tại `31/12/2025`). | Đã xử lý triệt để (`0` lỗi tồn đọng) |
| Cao (Vòng 1) | Số liệu năm 2024 của Chi phí bán hàng (Mã 46) và Chi phí quản lý doanh nghiệp (Mã 47). | Đã cập nhật chính xác theo trang 11 và Thuyết minh 32–33 (trang 70–71): năm 2024 Chi phí bán hàng `1.346,80 tỷ VND`, Chi phí QLDN `5.724,60 tỷ VND` (tổng `7.071,40 tỷ VND`; năm 2025 tăng `+25,69%` lên `8.887,98 tỷ VND`, trong đó CPQLDN tăng `+26,00%` lên `7.213,13 tỷ VND`). | Đã xử lý triệt để (`0` lỗi tồn đọng) |
| Cao (Vòng 1) | Tách bạch tổng chi phí repo & lãi vay (`1.746,88 tỷ VND`, TM 31.2 tr. 70) với chi phí repo phân bổ trực tiếp (`1.577,01 tỷ VND`, TM 22 tr. 60), dòng tiền HĐKD 2024 (`+8.419,20 tỷ VND`) và số dư tiền gửi quá hạn `ALCII` (TM 38.3 tr. 82). | Đã cập nhật đầy đủ và chính xác toàn bộ các khoản mục trên kèm dẫn chiếu số trang và mã thuyết minh. | Đã xử lý triệt để (`0` lỗi tồn đọng) |
| Thấp (Vòng 1) | Mã số chỉ tiêu trên KQKD (`Mã 15, 41, 42, 44, 46, 47, 50, 60, 61, 70`), số hiệu kiểm toán `11623354/E-68737085-HN` và tên công ty liên kết `PLT` (`35,00%`). | Đã chuẩn hóa đồng bộ trên `report.md` và `source-register.md`. | Đã xử lý triệt để (`0` lỗi tồn đọng) |

## Kiểm tra phép tính

- Đã chạy `bvh_metrics()` và `bvh_scenarios()` trong `research/companies/VN/calc_insurance_profiles.py` (`unittest OK`):
  - Tăng trưởng tổng tài sản: `291.805,65 / 251.286,33 - 1 = +16,12%`.
  - Tăng trưởng số dư Repo: `53.229,07 / 32.123,61 - 1 = +65,70%`.
  - Chênh lệch lợi nhuận gộp HĐKD bảo hiểm 2025 vs 2024: `1.237,95 - (-969,11) = +2.207,06 tỷ VND`.
  - `BVPS` công ty mẹ cuối 2025: `24.451,171923673 tỷ VND / 742,322764 triệu CP = 32.938,73 VND/CP`.
  - `ROE` công ty mẹ bình quân: `2.836,61 / ((24.451,17 + 22.591,55) / 2) = 12,06%`.
  - Định giá `Justified P/B`: Bất lợi `0,6429x` (`21.174,90 VND/CP`), Cơ sở `1,1455x` (`37.729,82 VND/CP`), Thuận lợi `1,6667x` (`54.897,89 VND/CP`).

## Hạn chế của lần kiểm duyệt

- Tệp PDF BCTC hợp nhất kiểm toán năm 2025 (`5.729.696 byte`, SHA-256 `ac79ffac4e21a2d2f046b6baaaef1f612703871c2ec79d38036b6852fa420a18`) là bản quét có chữ ký và dấu đỏ của Tập đoàn Bảo Việt và Công ty TNHH Ernst & Young Việt Nam lưu trên CDN Vietstock. Các thông tin ngoài thuyết minh `VAS` (danh sách tên tổ chức phát hành của `36.590,01 tỷ VND` TPDN dài hạn và độ nhạy định phí dự phòng toán học) được gắn nhãn `CHƯA_BIẾT` rõ ràng.

## Kết luận của agent kiểm duyệt

`ĐẠT` (`0` lỗi nghiêm trọng, `0` lỗi cao). Đủ điều kiện gỡ nhãn bản nháp và xuất bản chính thức.
