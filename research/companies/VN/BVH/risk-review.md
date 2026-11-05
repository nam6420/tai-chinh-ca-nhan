# Biên bản phản biện rủi ro: Tập đoàn Bảo Việt (BVH)

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-05 11:56 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-11-05 11:20 Asia/Ho_Chi_Minh`
- Phạm vi: Mô hình tập đoàn bảo hiểm nhân thọ + phi nhân thọ của BVH, chất lượng lợi nhuận FY2025 (hoàn nhập dự phòng đảm bảo lãi suất cam kết tối thiểu +197,39 tỷ VND), đòn bẩy giao dịch mua bán lại TPCP (Repo 53.229,07 tỷ VND), danh mục trái phiếu doanh nghiệp (37.424,15 tỷ VND), biên khả năng thanh toán mảng nhân thọ (107%), 3 kịch bản định giá Justified P/B và điều kiện làm luận điểm mất hiệu lực.
- Báo cáo đích: `research/companies/VN/BVH/report.md`
- SHA-256 nội dung đích: `492b1d938d1e3338cffd2177d676d858715e7e215da001a157dc9a6ce22ce1ab`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Phiên chính ghi từ kết quả nhánh độc lập `risk_bear_reviewer` ([conversation](conversation://4a892290-8931-423e-ab78-33d09d4a1966)); không tự thay kết luận.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| `https://static2.vietstock.vn/data/HOSE/2025/BCTC/VN/NAM/BVH_Baocaotaichinh_2025_Kiemtoan_Hopnhat.pdf` | BCTC hợp nhất kiểm toán FY2025 của `BVH` (EY Việt Nam ký 31/03/2026) | 2026-11-05 | Kiểm tra số dư `Repo` TPCP (`53.229,07 tỷ VND`, Mã 324 & TM 22 tr. 60), chi phí lãi Repo (`1.908,90 tỷ VND`, TM 32 tr. 74), dự phòng lãi cam kết tối thiểu (`16.544,35 tỷ VND`, TM 24.1 tr. 61) và biên khả năng thanh toán nhân thọ (`107%`, TM 40 tr. 84) |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| `TRUNG_BÌNH` | Mục Ban lãnh đạo, quản trị và phân bổ vốn & Kịch bản định giá (dòng 85–90, 99–101) | Báo cáo ghi nhận `BVH` duy trì cổ tức tiền mặt đều đặn (`1.055,1 VND/CP`, tổng `783,22 tỷ VND` năm 2025) và chỉ ra đệm biên khả năng thanh toán của Tổng Công ty Bảo Việt Nhân thọ chỉ còn dư `651,69 tỷ VND` (`107%`). Phản biện rủi ro nhấn mạnh thêm rủi ro nghẽn dòng tiền cổ tức về công ty mẹ (`Upstream Dividend Trap`): vì công ty con nhân thọ đang tiến sát ngưỡng `100%` và phải chuẩn bị vốn cho `RBC 01/01/2028`, công ty mẹ `BVH` có thể phải giữ lại toàn bộ lợi nhuận tại Bảo Việt Nhân thọ (thậm chí bơm thêm vốn), làm hạn chế khả năng tăng tỷ lệ chi trả cổ tức tiền mặt cho cổ đông `BVH` trong giai đoạn 2026–2028. | TM 40 (tr. 84) BCTC hợp nhất FY2025 của `BVH`: biên thanh toán Bảo Việt Nhân thọ giảm từ `120%` (2024) xuống `107%` (2025). | Lưu vết rủi ro hạn chế tăng cổ tức tiền mặt do nhu cầu giữ lại vốn tại công ty con nhân thọ vào `risk-review.md`. | `ĐÃ_GHI_NHẬN` |
| `THẤP` | Mục Lịch sử và chất lượng tài chính — Đầu tư công ty liên kết và bên liên quan (dòng 26, 73–75) | Bên cạnh các khoản tồn đọng lịch sử đã trích lập dự phòng 100% tại `ALCII`, `VFC`, `Vinashin` (TM 14 & 38.3), `BVH` còn nắm `49,52%` vốn tại Ngân hàng TMCP Bảo Việt (`BaoViet Bank`) và có phát sinh giao dịch tiền gửi/Repo trong hệ sinh thái. Dù đã thuyết minh theo chuẩn `VAS`, nhà đầu tư vẫn cần theo dõi chất lượng tài sản và biên lãi của `BaoViet Bank` trong trường hợp lãi suất biến động mạnh. | TM 1 (tr. 16), TM 14 (tr. 48–55) BCTC hợp nhất FY2025 của `BVH`. | Ghi chú điểm theo dõi định kỳ này vào `risk-review.md`. | `ĐÃ_GHI_NHẬN` |

## Kiểm tra phép tính và bằng chứng trái chiều

- Toàn bộ phép tính trong hàm `bvh_metrics()` và `bvh_scenarios()` của `calc_insurance_profiles.py` hoàn toàn chính xác. Kịch bản Bất lợi (`Bear`) đặt `ROE = 9,0% < k_e = 11,5%`, `g = 4,5%`, cho `P/B hợp lý = 0,6429x` (`21.174,90 VND/CP`, chiết khấu `-35,7%` so với `BVPS = 32.938,73 VND/CP`), phản ánh rất trung thực rủi ro hủy giá trị cổ đông nếu lợi suất TPCP giảm buộc `BVH` phải trích lập lại hàng nghìn tỷ đồng dự phòng đảm bảo lãi suất cam kết tối thiểu hoặc nếu chi phí lãi `Repo` (`53.229,07 tỷ VND`, gấp `2,09x` VCSH) vượt lợi suất danh mục đầu tư (`4,47%`).
- Báo cáo đã mổ xẻ bản chất kế toán đằng sau mức tăng `+33,15%` LNST năm 2025 (nhờ chênh lệch `3.279,30 tỷ VND` chi phí trích dự phòng đảm bảo lãi suất cam kết tối thiểu giữa năm 2024 và 2025), chỉ rõ khoản `36.590,01 tỷ VND` trái phiếu doanh nghiệp dài hạn chưa công bố tên tổ chức phát hành (`CHƯA_BIẾT`) và sự phình to `+42,57%` của chi phí quản lý doanh nghiệp (`7.213,13 tỷ VND`).

## Hạn chế của lần kiểm duyệt

- Báo cáo đã nêu rõ hai điểm `CHƯA_BIẾT`: danh sách tên tổ chức phát hành của `36.590,01 tỷ VND` trái phiếu doanh nghiệp dài hạn `HTM` và bảng độ nhạy định phí (`Actuarial Sensitivity`) của dự phòng toán học khi lãi suất kỹ thuật dịch chuyển `±50 bps`.

## Kết luận của agent kiểm duyệt

`ĐẠT` (`0` lỗi nghiêm trọng, `0` lỗi cao). Kịch bản `Bear`, rủi ro `Repo` `53.229,07 tỷ VND`, rủi ro biên thanh toán nhân thọ `107%` và điều kiện làm luận điểm mất hiệu lực đã được phản ánh trung thực, đầy đủ.
