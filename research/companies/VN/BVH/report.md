# Tập đoàn Bảo Việt (BVH)

- Chốt dữ liệu lúc: `2026-11-05 11:20 Asia/Ho_Chi_Minh`
- Quốc gia / thị trường / sở giao dịch: `Việt Nam / Cổ phiếu Bảo hiểm - Tài chính / HOSE`
- Chuẩn kế toán: `VAS và chế độ kế toán doanh nghiệp bảo hiểm (Thông tư 232/2012/TT-BTC, Thông tư 199/2014/TT-BTC)`
- Tiền tệ / đơn vị báo cáo: `VND; bảng dưới tính bằng tỷ VND nếu không ghi khác`
- Đề bài nghiên cứu: [Đợt 3 — Ngành Bảo hiểm Việt Nam và ba hồ sơ mẫu BVH, PVI, BIC](../../../briefs/vn-insurance-sector-and-profiles-2026-11-05.md)
- Sổ nguồn: [source-register.md](source-register.md)
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

## Tóm tắt bài học

Tập đoàn Bảo Việt (`BVH`) là tập đoàn tài chính - bảo hiểm lớn nhất Việt Nam theo quy mô tổng tài sản (**`291.805,65 tỷ VND`** tại ngày `31/12/2025`, gấp `6,56 lần` `PVI` và `28,91 lần` `BIC`) [S1, tr. 7]. Hồ sơ `BVH` được thiết kế để người học nắm vững **cách giải phẫu một tập đoàn bảo hiểm hỗn hợp lấy nhân thọ làm trụ cột**:
1. **Đừng nhìn tăng trưởng phí bảo hiểm gốc (`+2,64%`) rồi vội kết luận kinh doanh đi ngang:** Trong năm 2025, lợi nhuận sau thuế hợp nhất của `BVH` tăng vọt **`+33,15%`** (lên **`2.921,57 tỷ VND`**) nhờ hoạt động kinh doanh bảo hiểm đảo chiều từ lỗ gộp **`-969,11 tỷ VND`** (năm 2024) sang lãi gộp **`+1.237,95 tỷ VND`** (năm 2025) — một cú xoay trục **`+2.207,06 tỷ VND`** đến từ việc không còn phải trích lập hàng nghìn tỷ đồng dự phòng đảm bảo lãi suất cam kết tối thiểu như năm 2024 (`+197,39 tỷ VND` hoàn nhập năm 2025 so với `-3.081,91 tỷ VND` trích thêm năm 2024) [S1, tr. 11, 61, 71].
2. **Đòn bẩy ngầm trên danh mục trái phiếu Chính phủ qua giao dịch Repo:** `BVH` nắm **`266.535,57 tỷ VND`** đầu tư tài chính thuần (`91,34%` tổng tài sản), nhưng đồng thời vay tái cấp vốn qua **giao dịch mua bán lại trái phiếu Chính phủ (`Repo`) tới `53.229,07 tỷ VND`** (tăng **`+65,70%`** so với cuối năm 2024), tiêu tốn **`1.746,88 tỷ VND`** chi phí repo và lãi vay trong năm 2025 (trong đó chi phí repo phân bổ trực tiếp là `1.577,01 tỷ VND`) [S1, tr. 8, 48, 60, 70].
3. **Điểm nghẽn an toàn vốn nằm ở mảng Nhân thọ (`107%`):** Trong khi Bảo hiểm Bảo Việt (phi nhân thọ) có biên khả năng thanh toán đạt **`141%`** (`2024: 145%`), Tổng Công ty Bảo Việt Nhân thọ có tỷ lệ biên khả năng thanh toán tại `31/12/2025` chỉ đạt **`107%`** (`9.921,65 tỷ / 9.269,95 tỷ`, nhích nhẹ `+3 điểm phần trăm` từ mức `104%` cuối năm 2024), đứng sát ngưỡng pháp định tối thiểu `100%` trước thềm chuyển sang mô hình vốn trên cơ sở rủi ro (`RBC`) vào năm 2028 [S1, tr. 84; S2].

*Giới hạn lưu trữ nguồn:* Toàn bộ số liệu tài chính năm 2024–2025 được đọc trực tiếp từ ảnh trang bản PDF BCTC hợp nhất năm 2025 đã kiểm toán bởi Ernst & Young Việt Nam (ký ngày `31/03/2026`, số `11623354/E-68737085-HN`, 115 trang PDF / 111 trang đánh số BCTC) lưu trên CDN Vietstock [S1]; bản PDF có đầy đủ chữ ký và con dấu của doanh nghiệp và kiểm toán viên nhưng chưa đối chiếu khớp byte trực tiếp với tệp lưu trên miền `baoviet.com.vn`/HOSE.

## Mô hình kinh doanh

`SỰ_THẬT` Tập đoàn Bảo Việt (`BVH`) vận hành theo mô hình công ty mẹ - công ty con (Thuyết minh 1, trang 15–18 BCTC hợp nhất 2025), bao gồm:
- **Tổng Công ty Bảo Việt Nhân thọ** (`100%` sở hữu): kinh doanh bảo hiểm nhân thọ, đóng góp **`32.641,79 tỷ VND`** phí bảo hiểm gốc năm 2025 (`74,67%` tổng phí bảo hiểm gốc toàn Tập đoàn), trong đó riêng dòng sản phẩm **bảo hiểm liên kết chung (`Universal Life — UL`) đạt `27.229,21 tỷ VND`** (chiếm **`83,42%`** tổng phí nhân thọ!) [S1, tr. 66].
- **Tổng Công ty Bảo hiểm Bảo Việt** (`100%` sở hữu): kinh doanh bảo hiểm phi nhân thọ và sức khỏe, đạt **`11.074,40 tỷ VND`** phí gốc (`25,33%` tổng phí gốc Tập đoàn), dẫn đầu bởi bảo hiểm con người (`5.128,79 tỷ VND`), bảo hiểm tài sản (`4.672,96 tỷ VND`) và bảo hiểm trách nhiệm (`1.272,64 tỷ VND`) [S1, tr. 66].
- **Khối Quản lý quỹ, Chứng khoán và Đầu tư:** Công ty TNHH Quản lý Quỹ Bảo Việt (`BVF`, `100%` sở hữu), CTCP Chứng khoán Bảo Việt (`BVSC`, `59,92%` sở hữu) và các công ty liên doanh/liên kết như Ngân hàng TMCP Bảo Việt (`BaoViet Bank`, sở hữu `49,52%`), Bảo hiểm Tokio Marine Việt Nam (`49,00%`), CTCP Công nghệ thông tin `PLT` (`35,00%`) [S1, tr. 16, 18, 51].

`SỰ_THẬT` và `PHÉP_TÍNH` Trong năm 2025, tổng doanh thu phí bảo hiểm gốc đạt **`43.716,18 tỷ VND`** (`+2,64%` so với `42.591,78 tỷ VND` năm 2024), cộng phí nhận tái bảo hiểm **`399,97 tỷ VND`**, trừ phí nhượng tái bảo hiểm **`-3.808,52 tỷ VND`**, cho phí bảo hiểm giữ lại thuần (`NWP`) **`40.307,63 tỷ VND`** (tỷ lệ giữ lại **`91,37%`**) và doanh thu phí bảo hiểm thuần được hưởng (`NEP`, Mã 08) **`40.123,67 tỷ VND`** [S1, tr. 10, 66–67]. Doanh thu thuần hoạt động kinh doanh bảo hiểm (Mã 15, cộng hoa hồng nhượng tái và thu khác KDBH `824,59 tỷ VND`, trong đó hoa hồng nhượng tái là `776,40 tỷ VND`) đạt **`40.948,25 tỷ VND`**. Trừ tổng chi trực tiếp hoạt động kinh doanh bảo hiểm (Mã 41: **`39.710,31 tỷ VND`**), Tập đoàn ghi nhận **lợi nhuận gộp hoạt động kinh doanh bảo hiểm (Mã 42) đạt `+1.237,95 tỷ VND`** (so với mức lỗ gộp **`-969,11 tỷ VND`** năm 2024). Song song đó, danh mục đầu tư khổng lồ mang về **`14.039,76 tỷ VND`** doanh thu hoạt động tài chính, trừ **`2.919,29 tỷ VND`** chi phí tài chính, tạo ra **`11.120,47 tỷ VND` lợi nhuận tài chính thuần (Mã 44)** (`+5,17%` so với `10.573,60 tỷ VND` năm 2024) [S1, tr. 10–11, 70].

`SUY_LUẬN` Về bản chất kinh tế, `BVH` là một định chế quản lý tài sản nợ - có (`Asset-Liability Management — ALM`) khổng lồ: nguồn vốn `Float` ròng từ người mua bảo hiểm (**`198.000,08 tỷ VND`** dự phòng nghiệp vụ giữ lại ròng, gấp **`7,77 lần`** tổng vốn chủ sở hữu) được đầu tư vào tiền gửi ngân hàng và trái phiếu Chính phủ/doanh nghiệp để hưởng phần chênh lệch lãi suất (`Spread`) sau khi bù đắp chi phí dự phòng toán học và chi phí vận hành hệ thống đại lý.

## Bối cảnh ngành, vĩ mô và so sánh toàn cầu

`SỰ_THẬT` Sau giai đoạn thị trường bảo hiểm nhân thọ Việt Nam suy giảm năm 2023–2024 và chịu sự điều chỉnh của Luật Kinh doanh bảo hiểm (`31/VBHN-VPQH`), Nghị định `46/2023/NĐ-CP` và Thông tư `67/2023/TT-BTC` (`44/VBHN-BTC` khống chế trần hoa hồng năm đầu sản phẩm `UL` ở mức `30%`), tổng phí bảo hiểm nhân thọ toàn thị trường năm 2025 ước đạt khoảng `145.085–148.786 tỷ VND` [S2, S3, S4, S5]. Với `32.641,79 tỷ VND` phí nhân thọ gốc, Bảo Việt Nhân thọ nắm khoảng **`21,9%–22,5%` thị phần phí nhân thọ toàn ngành** (`PHÉP_TÍNH`: `32.641,79 / 148.786 = 21,94%`; `32.641,79 / 145.085 = 22,50%`), giữ vị trí số 1 về tổng doanh thu phí bảo hiểm nhân thọ tại Việt Nam.

`SỰ_THẬT` và `SUY_LUẬN` Đặt cạnh tập đoàn bảo hiểm hỗn hợp hàng đầu thế giới là **Berkshire Hathaway Inc.** (Mỹ, `US GAAP`, báo cáo năm 2025 [S6]), cả hai đều sử dụng nguồn vốn `Float` từ bảo hiểm để đầu tư sinh lời, nhưng cơ cấu tài sản và chi phí `Float` trái ngược nhau:
- Berkshire Hathaway phân bổ phần lớn danh mục đầu tư vào cổ phiếu niêm yết và tín phiếu Kho bạc Mỹ ngắn hạn, đồng thời tạo ra lợi nhuận khai thác bảo hiểm dương bền vững (`7.258 triệu USD` sau thuế năm 2025 trên `176 tỷ USD` `Float`).
- Ngược lại, `BVH` chịu ràng buộc của Thông tư `67/2023/TT-BTC` và nghĩa vụ cam kết lãi suất tối thiểu cho sản phẩm `UL` và nhân thọ truyền thống, nên phân bổ **`96,90%`** danh mục đầu tư tài chính thuần vào các khoản đầu tư nắm giữ đến ngày đáo hạn (`HTM`: **`258.282,06 tỷ / 266.535,57 tỷ VND`**), chủ yếu là tiền gửi ngân hàng và trái phiếu Chính phủ/doanh nghiệp [S1, tr. 48]. Khi lợi suất trái phiếu Chính phủ biến động, nghĩa vụ trích lập dự phòng đảm bảo lãi suất cam kết tối thiểu của `BVH` lập tức co giãn hàng nghìn tỷ đồng.

## Lịch sử và chất lượng tài chính

`SỰ_THẬT` và `PHÉP_TÍNH` Bảng tổng hợp các chỉ tiêu trọng yếu từ BCTC hợp nhất năm 2025 đã kiểm toán của `BVH` (công thức tái lập trong [`calc_insurance_profiles.py`](../calc_insurance_profiles.py)):

| Chỉ tiêu | FY2024 | FY2025 | Biến động / Tỷ lệ | Nhãn | Nguồn / Thuyết minh & Công thức |
|---|---:|---:|---:|---|---|
| **Tổng tài sản cuối năm** | `251.286,33` | `291.805,65` | `+16,12%` | `SỰ_THẬT` / `PHÉP_TÍNH` | Bảng CĐKT Mã 270 [S1, tr. 7]; `291.805,65 / 251.286,33 - 1` |
| **Đầu tư tài chính thuần (Ngắn hạn + Dài hạn)** | `231.543,46` | `266.535,57` | `+15,11%` (`91,34%` TS) | `SỰ_THẬT` / `PHÉP_TÍNH` | TM 14 [S1, tr. 48]; `HTM` chiếm `258.282,06 tỷ` (`96,90%`) |
| **Giao dịch mua bán lại TPCP (`Repo` phải trả)** | `32.123,61` | `53.229,07` | `+65,70%` | `SỰ_THẬT` / `PHÉP_TÍNH` | Mã 324 & TM 22 [S1, tr. 8, 60]; lãi suất Repo `3,4%–5,5%/năm` |
| **Dự phòng nghiệp vụ bảo hiểm gộp** | `186.574,10` | `201.682,49` | `+8,10%` | `SỰ_THẬT` / `PHÉP_TÍNH` | Mã 344 & TM 24 [S1, tr. 9, 61]: Nhân thọ `192.451,25`; PNT `9.231,23` |
| *— Trong đó: Dự phòng toán học nhân thọ* | `157.148,59` | `171.409,33` | `+9,07%` | `SỰ_THẬT` / `PHÉP_TÍNH` | TM 24.1 [S1, tr. 61]; trích thêm trong năm `14.260,75 tỷ` |
| *— Trong đó: Dự phòng đảm bảo lãi suất cam kết* | `16.741,74` | `16.544,35` | `-1,18%` (hoàn nhập `197,39`) | `SỰ_THẬT` / `PHÉP_TÍNH` | TM 24.1 [S1, tr. 61]; năm 2024 phải trích thêm `3.081,91 tỷ` |
| **Tài sản tái bảo hiểm** | `3.558,13` | `3.682,41` | `+3,49%` | `SỰ_THẬT` / `PHÉP_TÍNH` | Mã 190 & TM 24 [S1, tr. 6, 61] |
| **Tổng vốn chủ sở hữu / Vốn chủ công ty mẹ** | `23.565,89` / `22.591,55` | `25.480,34` / `24.451,17` | `+8,12%` / `+8,23%` | `SỰ_THẬT` / `PHÉP_TÍNH` | Mã 410 [S1, tr. 9]; trừ lợi ích CĐKKS `1.029,17 tỷ` (2025) |
| **Doanh thu phí bảo hiểm gốc (`GWP`)** | `42.591,78` | `43.716,18` | `+2,64%` | `SỰ_THẬT` / `PHÉP_TÍNH` | Mã 02 & TM 26.1 [S1, tr. 10, 66]: Nhân thọ `32.641,79`, PNT `11.074,40` |
| **Phí giữ lại thuần (`NWP`) / Tỷ lệ giữ lại** | `39.297,03` | `40.307,63` | `91,37%` (2025) | `PHÉP_TÍNH` | `43.716,18 + 399,97 - 3.808,52`; chia cho `(43.716,18 + 399,97)` |
| **Doanh thu phí bảo hiểm thuần (`NEP`)** | `39.126,18` | `40.123,67` | `+2,55%` | `SỰ_THẬT` / `PHÉP_TÍNH` | Mã 08 [S1, tr. 10] |
| **Tổng chi bồi thường & trả tiền bảo hiểm giữ lại** | `36.661,95` | `35.137,29` | `-4,16%` | `SỰ_THẬT` / `PHÉP_TÍNH` | Mã 29 & TM 28 [S1, tr. 10, 67–68] |
| **Lợi nhuận gộp hoạt động kinh doanh bảo hiểm** | `-969,11` | `+1.237,95` | Đảo chiều `+2.207,06` | `SỰ_THẬT` / `PHÉP_TÍNH` | Mã 42 [S1, tr. 11]; `1.237,95 - (-969,11) = +2.207,06 tỷ` |
| **Lợi nhuận hoạt động tài chính thuần** | `10.573,60` | `11.120,47` | `+5,17%` (lợi suất `4,47%`) | `SỰ_THẬT` / `PHÉP_TÍNH` | Mã 44 (`14.039,76 - 2.919,29`) [S1, tr. 11, 70]; chia ĐTTC bình quân |
| **Chi phí bán hàng + Chi phí quản lý doanh nghiệp** | `1.346,80 + 5.724,60` | `1.674,85 + 7.213,13` | `8.887,98` (`+25,69%`) | `SỰ_THẬT` / `PHÉP_TÍNH` | Mã 46 & 47, TM 32 & 33 [S1, tr. 11, 70–71]; năm 2024 tổng là `7.071,40 tỷ` |
| **Tổng lợi nhuận kế toán trước thuế (`EBT`)** | `2.663,17` | `3.554,43` | `+33,47%` | `SỰ_THẬT` / `PHÉP_TÍNH` | Mã 50 [S1, tr. 11] |
| **Lợi nhuận sau thuế hợp nhất / Công ty mẹ** | `2.194,17` / `2.110,50` | `2.921,57` / `2.836,61` | `+33,15%` / `+34,40%` | `SỰ_THẬT` / `PHÉP_TÍNH` | Mã 60 & 61 [S1, tr. 12] |
| **Lãi cơ bản trên cổ phiếu (`EPS`) / `BVPS` mẹ** | `2.785` / `30.433,60` | `3.821` / `32.938,73` | `ROE mẹ bình quân 12,06%` | `SỰ_THẬT` / `PHÉP_TÍNH` | Mã 70 & TM 36 [S1, tr. 12, 75]; `24.451,17 tỷ / 742,323 triệu CP` |
| **Biên khả năng thanh toán Nhân thọ / Phi nhân thọ** | `104%` / `145%` | `107%` / `141%` | Nhân thọ `+3 đ%`; PNT `-4 đ%` | `SỰ_THẬT` | TM 40 [S1, tr. 84]: Nhân thọ `9.921,65 / 9.269,95 tỷ`; PNT `2.692,49 / 1.916,39 tỷ` |

### Ba điểm mổ xẻ chất lượng báo cáo tài chính

1. **Giải mã cú đảo chiều lợi nhuận gộp bảo hiểm `+2.207,06 tỷ VND` (Báo cáo KQKD Mã 22–26 tr. 10 & Thuyết minh 24 tr. 61):**
   - `SỰ_THẬT` Tại sao phí bảo hiểm thuần (`NEP`) năm 2025 chỉ tăng `+2,55%` (`+997,48 tỷ VND`) mà lợi nhuận gộp kinh doanh bảo hiểm lại tăng thêm **`+2.207,06 tỷ VND`** (từ lỗ `-969,11 tỷ VND` sang lãi `+1.237,95 tỷ VND`)? Khi đọc Báo cáo KQKD (trang 10, Mã 22) và Thuyết minh 24 (trang 61), dòng *"Tăng dự phòng nghiệp vụ bảo hiểm gốc"* giảm mạnh từ **`18.168,73 tỷ VND`** (năm 2024) xuống **`14.622,82 tỷ VND`** (năm 2025), tức giảm **`3.545,91 tỷ VND`** chi phí trích lập dự phòng! Đối chiếu chi tiết Mã 24 (trang 10) và Thuyết minh 24 (trang 61), riêng quỹ **Dự phòng đảm bảo lãi suất cam kết tối thiểu** năm 2024 phải trích thêm **`3.081,91 tỷ VND`**, nhưng năm 2025 được **hoàn nhập `+197,39 tỷ VND`** (chênh lệch **`3.279,30 tỷ VND`** chi phí kế toán giữa hai năm) [S1, tr. 10, 61].
   - `SUY_LUẬN` Phần lớn mức tăng trưởng lợi nhuận kỷ lục năm 2025 của `BVH` đến từ sự giảm nhẹ áp lực trích lập dự phòng lãi suất cam kết tối thiểu khi mặt bằng lãi suất năm 2025 ổn định hơn năm 2024, chứ không phải do biên khai thác sản phẩm mới đột nhiên mở rộng gấp bội.
2. **Chi phí quản lý doanh nghiệp tăng `+26,00%` do tăng chi phí nhân công và dịch vụ mua ngoài (Thuyết minh 33 tr. 71):**
   - `SỰ_THẬT` Chi phí quản lý doanh nghiệp hợp nhất năm 2025 tăng từ `5.724,60 tỷ VND` lên **`7.213,13 tỷ VND`** (`+1.488,53 tỷ VND`, tức `+26,00%`), trong đó chi phí nhân công trực tiếp liên quan hoạt động bảo hiểm tăng từ `2.823,44 tỷ VND` lên **`3.790,25 tỷ VND`** (`+34,24%`) và chi phí dịch vụ mua ngoài tăng từ `1.420,62 tỷ VND` lên **`1.729,43 tỷ VND`** [S1, tr. 71]. Cùng với chi phí bán hàng tăng `+24,36%` (từ `1.346,80 tỷ` lên `1.674,85 tỷ VND`, chủ yếu là chi khen thưởng và hỗ trợ đại lý `1.553,87 tỷ VND` tại Thuyết minh 32 trang 70), tổng chi phí bán hàng và quản lý doanh nghiệp năm 2025 đạt **`8.887,98 tỷ VND`** (`+25,69%`).
3. **Đòn bẩy Repo trái phiếu Chính phủ và các khoản nợ quá hạn tồn đọng lịch sử (Thuyết minh 14 tr. 48–50, Thuyết minh 22 tr. 60, Thuyết minh 38.3 tr. 82):**
   - `SỰ_THẬT` Tại ngày `31/12/2025`, danh mục đầu tư `HTM` (`258.282,06 tỷ VND`) của `BVH` gồm: tiền gửi ngắn hạn **`119.262,75 tỷ VND`** (lãi suất tối đa `9,0%/năm`), tiền gửi dài hạn **`26.951,38 tỷ VND`** (`5,2%–7,6%/năm`), trái phiếu Chính phủ **`71.271,91 tỷ VND`** (kỳ hạn 14–30 năm, lãi suất đến `8,9%/năm`), trái phiếu doanh nghiệp ngắn và dài hạn **`37.424,15 tỷ VND`** (`834,15 + 36.590,01 tỷ VND`, kỳ hạn 7–10 năm), và tạm ứng từ giá trị hoàn lại hợp đồng bảo hiểm **`4.206,03 tỷ VND`** [S1, tr. 48, 50].
   - `SỰ_THẬT` Để tối ưu thanh khoản và hưởng chênh lệch lãi suất (`Carry Trade`) mà không phải bán đứt trái phiếu Chính phủ lãi suất cao, `BVH` thực hiện giao dịch bán và cam kết mua lại (`Repo`) trái phiếu Chính phủ với số dư phải trả cuối năm 2025 lên tới **`53.229,07 tỷ VND`** (tăng `+65,70%` so với `32.123,61 tỷ VND` đầu năm, kỳ hạn dưới 12 tháng, trong đó Repo với công ty liên kết `BaoViet Bank` là `36.878,36 tỷ VND`) [S1, tr. 60, 73]. Tổng chi phí repo và lãi vay năm 2025 trên báo cáo KQKD là **`1.746,88 tỷ VND`** (năm 2024: `1.031,80 tỷ VND`), trong đó chi phí repo phân bổ trực tiếp là **`1.577,01 tỷ VND`** (năm 2024: `982,81 tỷ VND`) [S1, tr. 60, 70].
   - `SỰ_THẬT` Về nợ xấu/tài sản quá hạn lịch sử, Thuyết minh 14.2 (trang 50) và Thuyết minh 38.3 (trang 82) công khai các hợp đồng tiền gửi và trái phiếu quá hạn từ giai đoạn 2007–2010 tại Công ty Cho thuê Tài chính II - Agribank (`ALCII`, nợ gốc tiền gửi chưa thanh toán **`326,60 tỷ VND`**, nợ lãi trong hạn **`52,99 tỷ VND`**, nợ lãi quá hạn trên gốc **`421,21 tỷ VND`** và nợ lãi quá hạn trên lãi **`69,07 tỷ VND`**; ngày `26/12/2025` đã thu hồi được `4,50 tỷ VND` qua Cục Thi hành án dân sự TP.HCM), Công ty Tài chính Công nghiệp Tàu thủy (`VFC`) và Tập đoàn Công nghiệp Tàu thủy Việt Nam (`VNS`), với tổng dự phòng phải thu ngắn hạn khó đòi toàn Tập đoàn tại `31/12/2025` là **`544,82 tỷ VND`** (Mã 137 trang 6) và dự phòng đầu tư tài chính dài hạn là **`85,40 tỷ VND`** (Mã 254 trang 7) [S1, tr. 6, 7, 50, 82].

## Ban lãnh đạo, quản trị và phân bổ vốn

`SỰ_THẬT` Cơ cấu cổ đông tại ngày `31/12/2025` (Thuyết minh 1, trang 15 và Thuyết minh 25.2, trang 65) rất cô đặc:
- **Bộ Tài chính** (đại diện chủ sở hữu Nhà nước): nắm **`65,00%`** vốn điều lệ (`4.825,10 tỷ VND` theo mệnh giá).
- **Công ty Bảo hiểm Nhân thọ Sumitomo (`Sumitomo Life Insurance Company` — Nhật Bản):** cổ đông chiến lược nước ngoài nắm **`22,09%`** (`1.639,79 tỷ VND` theo mệnh giá).
- **Tổng Công ty Đầu tư và Kinh doanh Vốn Nhà nước (`SCIC`):** nắm **`2,98%`** (`221,21 tỷ VND`).
- **Các cổ đông khác:** nắm **`9,93%`** (`737,13 tỷ VND`) [S1, tr. 15, 65].

`SỰ_THẬT` và `PHÉP_TÍNH` Về phân bổ vốn và cổ tức:
- Vốn điều lệ của `BVH` giữ nguyên ở mức **`7.423,23 tỷ VND`** (`742.322.764` cổ phiếu phổ thông) trong nhiều năm qua.
- Trong năm 2025, `BVH` đã chi trả cổ tức tiền mặt từ lợi nhuận năm 2024 với tỷ lệ **`10,551%` mệnh giá** (**`1.055,1 VND/cổ phiếu`**, tổng số tiền chi trả **`783,22 tỷ VND`**, tương ứng tỷ lệ chi trả cổ tức khoảng `37,11%` lợi nhuận sau thuế công ty mẹ năm 2024; năm 2024 chi trả `1.003,7 VND/CP`, tổng `745,07 tỷ VND`) [S1, tr. 65].

`SUY_LUẬN` Sự hiện diện của Bộ Tài chính (`65,00%`) và Sumitomo Life (`22,09%`) mang lại kỷ luật quản trị, hỗ trợ kỹ thuật định phí (`Actuarial`) và chính sách cổ tức tiền mặt đều đặn hàng năm. Tuy nhiên, việc vốn điều lệ giữ nguyên ở `7.423,23 tỷ VND` (và vốn điều lệ của Bảo Việt Nhân thọ giữ ở `6.000 tỷ VND` từ năm 2021) trong khi quy mô dự phòng nhân thọ tiến sát `200.000 tỷ VND` khiến biên khả năng thanh toán của Tổng Công ty Bảo Việt Nhân thọ chỉ ở mức **`107%`** cuối năm 2025 (tăng nhẹ `+3 điểm phần trăm` so với mức **`104%`** cuối năm 2024) [S1, tr. 16, 84]. Đây là bài toán phân bổ vốn trọng yếu nhất mà Hội đồng Quản trị `BVH` phải giải quyết trước mốc `RBC 01/01/2028`.

## Các kịch bản định giá

`KỊCH_BẢN` và `PHÉP_TÍNH` Hồ sơ sử dụng mô hình **P/B hợp lý (`Justified P/B`) kết hợp Thu nhập thặng dư (`Residual Income`)** trên giá trị sổ sách vốn chủ sở hữu công ty mẹ tại `31/12/2025` (**`B_0 = 24.451,17 tỷ VND`**, tương đương **`BVPS_0 = 32.938,73 VND/cổ phiếu`** cho `742,323 triệu` cổ phiếu lưu hành). Công thức chuẩn:
$$\text{P/B hợp lý} = \frac{ROE - g}{k_e - g}, \quad V_0 = B_0 \times \text{P/B hợp lý}$$
Mọi con số dưới đây được tính và kiểm thử tự động trong hàm `bvh_scenarios()` của [`calc_insurance_profiles.py`](../calc_insurance_profiles.py) (không phải giá mục tiêu hay khuyến nghị mua/bán):

| Kịch bản | Giả định chính (`ROE`, `k_e`, `g`) | Phương pháp / đầu vào | Khoảng giá trị hợp lý minh họa | Điều gì phải đúng |
|---|---|---|---|---|
| **Bất lợi (`Bear`)** | `ROE = 9,0%`, chi phí vốn chủ `k_e = 11,5%`, tăng trưởng bền vững `g = 4,5%` | `P/B = (0,090 - 0,045) / (0,115 - 0,045) = 0,6429x`; nhân với `B_0 = 24.451,17 tỷ` | Vốn chủ hợp lý: **`15.718,61 tỷ VND`** (**`21.174,90 VND/CP`**, chiết khấu `35,7%` so với sổ sách) | Lợi suất TPCP giảm trở lại buộc Bảo Việt Nhân thọ phải trích bổ sung dự phòng đảm bảo lãi suất cam kết tối thiểu từ `1.500–2.500 tỷ/năm`; chênh lệch lãi Repo thu hẹp |
| **Cơ sở (`Base`)** | `ROE = 11,8%` (sát mức thực hiện 2025 là `12,06%`), `k_e = 11,0%`, `g = 5,5%` | `P/B = (0,118 - 0,055) / (0,110 - 0,055) = 1,1455x`; nhân với `B_0 = 24.451,17 tỷ` | Vốn chủ hợp lý: **`28.007,71 tỷ VND`** (**`37.729,82 VND/CP`**, cao hơn sổ sách `14,5%`) | Lợi suất tiền gửi và TPCP duy trì quanh `4,5%–5,0%/năm`; mảng bảo hiểm giữ lợi nhuận gộp dương `~1.000–1.300 tỷ/năm`; không phát sinh trích lập đột biến dự phòng lãi suất tối thiểu |
| **Thuận lợi (`Bull`)** | `ROE = 13,5%`, `k_e = 10,5%`, `g = 6,0%` | `P/B = (0,135 - 0,060) / (0,105 - 0,060) = 1,6667x`; nhân với `B_0 = 24.451,17 tỷ` | Vốn chủ hợp lý: **`40.751,95 tỷ VND`** (**`54.897,89 VND/CP`**, gấp `1,67 lần` sổ sách) | Lợi suất TPCP kỳ hạn dài tăng thêm `50–100 bps` giúp hoàn nhập tiếp dự phòng lãi suất cam kết tối thiểu; kênh đại lý nhân thọ phục hồi tăng trưởng phí mới trên `10%/năm` |

## Rủi ro và bằng chứng trái chiều

1. **Biên khả năng thanh toán của Bảo Việt Nhân thọ ở mức mỏng `107%` (Thuyết minh 40, trang 84):**
   - `SỰ_THẬT` Tại ngày `31/12/2025`, biên khả năng thanh toán hiện có của Tổng Công ty Bảo Việt Nhân thọ là **`9.921.645 triệu VND`** so với biên khả năng thanh toán tối thiểu **`9.269.953 triệu VND`**, tức tỷ lệ đạt **`107%`** (tăng nhẹ `+3 điểm phần trăm` so với mức **`104%`** tại `31/12/2024`: **`8.879.831 / 8.554.813 triệu VND`**; trong khi đó Tổng Công ty Bảo hiểm Bảo Việt đạt **`141%`** tại `31/12/2025` so với **`145%`** tại `31/12/2024`: `2.692.491 / 1.916.391 triệu VND`) [S1, tr. 84].
   - `SUY_LUẬN` Khoảng đệm dư thừa tuyệt đối của Bảo Việt Nhân thọ chỉ còn **`651,69 tỷ VND`** trên quy mô dự phòng nhân thọ `192.451,25 tỷ VND` (`0,34%` dự phòng!). Nếu dự phòng toán học tiếp tục tăng `~9%/năm` mà vốn chủ của Bảo Việt Nhân thọ không tăng tương ứng, hoặc khi chuyển sang khung vốn trên cơ sở rủi ro (`RBC`) từ `01/01/2028`, `BVH` sẽ buộc phải giữ lại lợi nhuận nhiều hơn hoặc bơm thêm vốn cho công ty con nhân thọ.
2. **Rủi ro thanh khoản và lãi suất ngắn hạn từ số dư Repo trái phiếu Chính phủ `53.229,07 tỷ VND` (Thuyết minh 22, trang 60):**
   - `SỰ_THẬT` Số dư giao dịch bán và cam kết mua lại trái phiếu Chính phủ (`Repo`) tăng từ `32.123,61 tỷ VND` lên **`53.229,07 tỷ VND`** (`+65,70%`), gấp **`2,09 lần`** tổng vốn chủ sở hữu hợp nhất của `BVH` [S1, tr. 8, 60].
   - `SUY_LUẬN` Dùng nguồn vốn Repo ngắn hạn (chi phí repo phân bổ năm 2025 là `1.577,01 tỷ VND` và tổng chi phí repo + lãi vay là `1.746,88 tỷ VND`) để tài trợ danh mục trái phiếu Chính phủ/tiền gửi dài hạn tạo ra rủi ro tái cấp vốn (`Rollover Risk`): nếu lãi suất thị trường liên ngân hàng/Repo tăng đột ngột lên trên `6,5%–7,5%/năm`, chi phí tài chính của `BVH` sẽ tăng thêm `1.000–1.500 tỷ VND/năm`, ăn mòn trực tiếp lợi nhuận ròng.
3. **Danh mục trái phiếu doanh nghiệp `37.424,15 tỷ VND` (Thuyết minh 14.1 & 14.2, trang 48, 50):**
   - `SỰ_THẬT` Trong danh mục đầu tư nắm giữ đến ngày đáo hạn (`HTM`), `BVH` nắm giữ **`834,15 tỷ VND`** trái phiếu doanh nghiệp ngắn hạn và **`36.590,01 tỷ VND`** trái phiếu doanh nghiệp dài hạn (kỳ hạn từ 7 đến 10 năm, lãi suất tối đa đến `8,90%/năm`), tổng cộng **`37.424,15 tỷ VND`**, tương đương **`146,87%`** tổng vốn chủ sở hữu hợp nhất [S1, tr. 48, 50]. Thuyết minh 14.2 không công bố chi tiết tên từng tổ chức phát hành của khoản `36.590,01 tỷ VND` trái phiếu doanh nghiệp dài hạn (`CHƯA_BIẾT`).
4. **Bằng chứng thuận chiều đối trọng:**
   - `SỰ_THẬT` Bất chấp các rủi ro trên, dòng tiền thuần từ hoạt động kinh doanh năm 2025 của `BVH` đạt dương **`+5.793,87 tỷ VND`** (năm 2024: **`+8.419,20 tỷ VND`**) và tiền & tương đương tiền cuối năm tăng gần gấp 3 lần lên **`4.194,68 tỷ VND`** [S1, tr. 13–14], cho thấy dòng tiền thu phí và lãi đầu tư thực thu vẫn vượt xa dòng tiền chi trả quyền lợi bảo hiểm hàng năm, giúp Tập đoàn không phải bán tháo tài sản dài hạn.

## Điều kiện làm luận điểm mất hiệu lực

Luận điểm cơ sở rằng *"BVH đã vượt qua đáy chu kỳ trích lập dự phòng năm 2024 để duy trì ROE công ty mẹ quanh mức 11,5%–12,5%"* sẽ bị bác bỏ nếu:
1. Tỷ lệ biên khả năng thanh toán của Tổng Công ty Bảo Việt Nhân thọ rơi xuống **dưới `100%`**, kích hoạt biện pháp kiểm soát/yêu cầu tăng vốn bắt buộc theo Luật Kinh doanh bảo hiểm.
2. Quỹ dự phòng đảm bảo lãi suất cam kết tối thiểu (Thuyết minh 24.1) quay lại trạng thái phải **trích lập bổ sung trên `2.000 tỷ VND/năm`**, đẩy lợi nhuận gộp hoạt động kinh doanh bảo hiểm hợp nhất quay lại mức âm.
3. Lãi suất vay Repo trái phiếu Chính phủ bình quân vượt quá lợi suất danh mục đầu tư tài chính bình quân (`4,47%/năm`), biến đòn bẩy Repo từ công cụ hỗ trợ lợi nhuận thành gánh nặng lỗ chênh lệch lãi suất (`Negative Carry`).

## Điều chưa biết và lần kiểm tra tiếp theo

- `CHƯA_BIẾT` Cơ cấu chi tiết theo tên tổ chức phát hành và tài sản bảo đảm của danh mục **`36.590,01 tỷ VND`** trái phiếu doanh nghiệp dài hạn nắm giữ đến ngày đáo hạn (Thuyết minh 14.2 trang 50 chỉ nêu tổng số dư, kỳ hạn 7–10 năm và lãi suất đến `8,90%/năm`).
- `CHƯA_BIẾT` Bảng phân tích độ nhạy định phí (`Actuarial Sensitivity`) của dự phòng toán học nhân thọ (`171.409,33 tỷ VND`) khi lãi suất kỹ thuật thay đổi `±50 bps` (do VAS hiện hành chưa bắt buộc công bố bảng độ nhạy dòng tiền chiết khấu như `IFRS 17`).
- **Lần kiểm tra tiếp theo:** BCTC hợp nhất bán niên năm 2026 đã soát xét (công bố tháng 08/2026), tập trung kiểm tra Thuyết minh Dự phòng nghiệp vụ nhân thọ, số dư Repo trái phiếu Chính phủ (Mã 324) và Biên khả năng thanh toán của Bảo Việt Nhân thọ.

## Sổ nguồn tóm tắt

Chi tiết đầy đủ xem tại [source-register.md](source-register.md).

| Mã | Nhận định / đầu vào | Nhãn | Nguồn | Ngày xuất bản | Kỳ báo cáo | Ngày truy cập | Đơn vị / tiền tệ | Phiên bản / ghi chú |
|---|---|---|---|---|---|---|---|---|
| S1 | Toàn bộ số liệu Bảng CĐKT, KQKD, LCTT và Thuyết minh 1–43 của Tập đoàn Bảo Việt (`BVH`) | `SỰ_THẬT` | BCTC hợp nhất FY2025 đã kiểm toán của BVH (Ernst & Young Việt Nam, số 11623354/E-68737085-HN) | 31/03/2026 | FY2025 & FY2024 | 2026-11-05 | VND | 115 trang PDF; SHA-256 `9a2c2537...14dadde` |
| S2 | Lộ trình vốn trên cơ sở rủi ro (`RBC`) từ 01/01/2028 và quy định tách pháp nhân nhân thọ/phi nhân thọ | `SỰ_THẬT` | Văn bản hợp nhất Luật Kinh doanh bảo hiểm số 31/VBHN-VPQH | 2025 | Hiện hành | 2026-11-05 | Văn bản luật | Bản PDF Công báo Chính phủ |
| S3 | Quy định về dự phòng nghiệp vụ nhân thọ và biên khả năng thanh toán tối thiểu | `SỰ_THẬT` | Nghị định 46/2023/NĐ-CP | 01/07/2023 | Hiện hành | 2026-11-05 | Tỷ VND / % | Bản PDF ký số Chính phủ |
| S4 | Trần hoa hồng đại lý bảo hiểm liên kết chung (`UL` năm đầu tối đa 30%) và giới hạn đầu tư | `SỰ_THẬT` | Thông tư 67/2023/TT-BTC (hợp nhất tại 44/VBHN-BTC) | 2025 | Hiện hành | 2026-11-05 | % | Bản PDF Công báo Chính phủ |
| S5 | Tổng doanh thu phí nhân thọ toàn thị trường năm 2025 (~145.085–148.786 tỷ VND) | `SỰ_THẬT` (thứ cấp) | Thống kê Cục Quản lý, giám sát bảo hiểm — Bộ Tài chính | 2026 | FY2025 | 2026-11-05 | Tỷ VND | Dùng để ước tính thị phần nhân thọ của BVH (~21,9%–22,5%) |
| S6 | Đối chiếu quy mô Float (`176 tỷ USD`) và lợi nhuận khai thác bảo hiểm của Berkshire Hathaway | `SỰ_THẬT` | Berkshire Hathaway Inc. 2025 Annual Report | 2026 | FY2025 | 2026-11-05 | Triệu USD / Tỷ USD | US GAAP |

## Biên bản kiểm duyệt

- Biên bản kiểm nguồn: [fact-check.md](fact-check.md)
- Biên bản phản biện rủi ro: [risk-review.md](risk-review.md)
- Bất đồng chưa giải quyết: `Không có`

> Chỉ dùng cho học tập và nghiên cứu. Đây không phải tư vấn tài chính cá nhân hay khuyến nghị giao dịch.
