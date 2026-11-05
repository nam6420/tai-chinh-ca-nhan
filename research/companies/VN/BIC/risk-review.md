# Biên bản phản biện rủi ro: Tổng Công ty Cổ phần Bảo hiểm Ngân hàng Đầu tư và Phát triển Việt Nam (BIC)

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-05 11:56 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-11-05 11:20 Asia/Ho_Chi_Minh`
- Phạm vi: Mô hình bảo hiểm bán lẻ qua ngân hàng mẹ BIDV (Bancassurance) của BIC, chênh lệch trước và sau kiểm toán FY2025 (-31,75 tỷ VND lợi nhuận gộp bảo hiểm do tái phân loại +31,53 tỷ VND chi phí), rủi ro tập trung kép tại BIDV (66,44% danh mục HTM = 4.428,50 tỷ VND tiền gửi và 13,25% GWP = 755,65 tỷ VND hoa hồng đại lý), sự sụt giảm -6,40% phí bảo hiểm sức khỏe/người vay, sự phụ thuộc vào lãi bán cổ phiếu tự doanh (163,33 tỷ VND), 3 kịch bản định giá Justified P/B và điều kiện làm luận điểm mất hiệu lực.
- Báo cáo đích: `research/companies/VN/BIC/report.md`
- SHA-256 nội dung đích: `320bb3acd1fe936935b9c56c1ff313790e2fd76c8bfa876341b51c9dde5a948b`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Phiên chính ghi từ kết quả nhánh độc lập `risk_bear_reviewer` ([conversation](conversation://4a892290-8931-423e-ab78-33d09d4a1966)); không tự thay kết luận.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày xuất bản / kỳ dữ liệu | Ngày truy cập | Mục đích kiểm tra |
|---|---|---|---|
| `https://static2.vietstock.vn/data/HOSE/2025/BCTC/VN/NAM/BIC_Baocaotaichinh_2025_Kiemtoan_Hopnhat.pdf` & `BIC_Baocaotaichinh_Q4_2025_Hopnhat.pdf` | BCTC hợp nhất kiểm toán FY2025 (`20/03/2026`, EY Việt Nam) và BCTC Q4/2025 (`28/01/2026`) của `BIC` | 2026-11-05 | Đối chiếu chéo số trước/sau kiểm toán, Thuyết minh 36 (giao dịch bên liên quan với `BIDV` tr. 61–62), Thuyết minh 41.1 (tam giác phát triển tổn thất tr. 73) và Thuyết minh 43 (điều chỉnh hồi tố theo Kiểm toán Nhà nước tr. 83–85) |

## Phát hiện

| Mức độ | Nhận định / phần | Phát hiện | Bằng chứng | Cách khắc phục | Trạng thái |
|---|---|---|---|---|---|
| `TRUNG_BÌNH` | Mục Các kịch bản định giá — Độ khắc nghiệt của Kịch bản Bất lợi (`Bear`) (dòng 101–103) | Trong bảng kịch bản định giá (dòng 103), kịch bản Bất lợi (`Bear`) giả định `ROE = 13,5% > k_e = 11,5%`, `g = 4,5%`, dẫn tới `P/B hợp lý = 1,2857x` (`20.679,50 VND/CP`, vẫn cao hơn giá trị sổ sách `+28,6%`). Dưới góc nhìn phản biện giá xuống (`Bear Case`), nếu xảy ra cú sốc kép: (1) không còn khoản lãi tự doanh cổ phiếu `163,33 tỷ VND` + hoàn nhập dự phòng `24,99 tỷ VND` (`188,32 tỷ VND` trước thuế, tương đương `27,7%` `EBT` năm 2025) mà danh mục cổ phiếu `506,01 tỷ VND` quay sang trích dự phòng giảm giá, đồng thời (2) `Loss Ratio` tăng từ `30,14%` lên `36%–38%` do bão lũ hoặc `BIDV` nâng mức chia sẻ hoa hồng, thì `ROE` công ty mẹ của `BIC` sẽ lùi về vùng `9,5%–10,5% < k_e = 11,5%`, ứng với mức định giá đáy chu kỳ `P/B = 0,71x–0,86x` (`11.500–13.800 VND/CP`). | Trong năm 2025, nếu loại trừ `163,33 tỷ VND` lãi bán cổ phiếu kinh doanh (tăng `+111,78 tỷ VND` so với 2024, TM 31 tr. 56), lợi nhuận trước thuế cốt lõi của `BIC` thực chất giảm nhẹ do lợi nhuận gộp bảo hiểm giảm `-19,11%` (`-227,61 tỷ VND`). | Ghi nhận thêm kịch bản Bear khắc nghiệt (`Severe Bear`: `ROE = 10,0% < k_e = 11,5%` cho `P/B = 0,786x` ~ `12.637 VND/CP`) vào biên bản phản biện rủi ro (`risk-review.md`) để người đọc thấy biên độ giảm giá nếu lợi nhuận tự doanh cổ phiếu đảo chiều cùng lúc với chu kỳ bão lũ. | `ĐÃ_GHI_NHẬN` |
| `THẤP` | Mục Mô hình kinh doanh & Điều kiện mất hiệu lực — Rủi ro mở rộng sang Lào (`LVI`) và Campuchia (`CVI`) (dòng 24–25, 126) | Ngày `01/07/2025`, `BIC` chi `106,99 tỷ VND` mua `51%` `CVI` tại Campuchia (bên cạnh `65%` tại `LVI` — Lào). Thị trường Lào và Campuchia có rủi ro biến động tỷ giá hối đoái (`LAK/VND`, `KHR/USD`), rủi ro thanh khoản ngân hàng địa phương và tập quán giám định bồi thường khác biệt so với Việt Nam. | TM 1 (tr. 18–19) và TM 4.1 (tr. 34–35) BCTC hợp nhất kiểm toán FY2025 của `BIC`. | Đã được báo cáo nêu tại điều kiện mất hiệu lực số 3 (dòng 126); ghi chú theo dõi tiếp vào `risk-review.md`. | `ĐÃ_GHI_NHẬN` |

## Kiểm tra phép tính và bằng chứng trái chiều

- Toàn bộ số liệu và tỷ số trong `bic_metrics()` và `bic_scenarios()` của `calc_insurance_profiles.py` khớp chính xác tuyệt đối với BCTC hợp nhất năm 2025 đã kiểm toán bởi EY Việt Nam (`20/03/2026`) và BCTC Q4/2025 (`28/01/2026`).
- Báo cáo `BIC` thể hiện chất lượng kiểm toán chéo và phản biện rất cao khi chủ động chỉ ra 4 điểm trọng yếu:
  1. Chênh lệch trước và sau kiểm toán (`-31,75 tỷ VND` lợi nhuận gộp bảo hiểm) do EY tái phân loại `+31,53 tỷ VND` từ Chi phí quản lý doanh nghiệp sang Chi phí trực tiếp kinh doanh bảo hiểm — qua đó chứng minh nếu cộng đủ `800,17 tỷ VND` G&A thì `Combined Ratio` sau hoa hồng nhượng tái thực chất là `95,87%` chứ không phải con số bề mặt `75,60%`.
  2. Rủi ro phụ thuộc hai đầu vào ngân hàng mẹ `BIDV` (TM 36 tr. 61–62): gửi `4.428,50 tỷ VND` tiền gửi có kỳ hạn tại `BIDV` (`66,44%` tổng danh mục `HTM`, gấp `1,31x` VCSH) và trả `755,65 tỷ VND` hoa hồng đại lý + `38,09 tỷ VND` hỗ trợ tiếp thị cho `BIDV` (`13,25%` `GWP`).
  3. Sự suy giảm `-4,00%` của mảng Bảo hiểm sức khỏe & tai nạn cá nhân (`2.357,88 tỷ VND`, chiếm `41,35%` `GWP`) và cú sụt giảm `-58,70%` lãi gộp bảo hiểm Q4/2025 vì thiên tai bão lũ.
  4. Sự phụ thuộc của tăng trưởng `EBT` năm 2025 vào lãi bán cổ phiếu kinh doanh (`163,33 tỷ VND`), đối trọng khách quan với khoản lãi chưa thực hiện (`Unrealized Gain`) `+130,21 tỷ VND` trên danh mục cổ phiếu cuối năm (`636,22 tỷ` thị giá so với `506,01 tỷ` giá trị ghi sổ thuần, TM 6.1 tr. 37).

## Hạn chế của lần kiểm duyệt

- Báo cáo đã nêu rõ điểm `CHƯA_BIẾT` về tỷ trọng doanh thu phí bảo hiểm gốc từng dòng sản phẩm được phát hành trực tiếp qua quầy `BIDV` so với kênh đại lý ngoài `BIDV` (do Thuyết minh 36 chỉ công bố tổng hoa hồng trả cho `BIDV`).

## Kết luận của agent kiểm duyệt

`ĐẠT` (`0` lỗi nghiêm trọng, `0` lỗi cao). Toàn bộ rủi ro cấu trúc, giao dịch bên liên quan với `BIDV`, chênh lệch kiểm toán và bằng chứng trái chiều đã được phản ánh đầy đủ, minh bạch.
