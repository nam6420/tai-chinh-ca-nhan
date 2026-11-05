# Bài F8 — Phân tích doanh nghiệp bảo hiểm Việt Nam: dự phòng nghiệp vụ, tái bảo hiểm, đầu tư tài chính và vốn trên cơ sở rủi ro (`RBC`)

- Ngày: `2026-11-05`
- Chốt dữ liệu lúc: `2026-11-05 10:35 UTC+7 (Asia/Ho_Chi_Minh)`
- Bậc chiều sâu: `Bậc S — 3 buổi học, 10 bài tập + mô hình Python`
- Mục tiêu: Đọc và kiểm toán chéo BCTC doanh nghiệp bảo hiểm Việt Nam theo `Thông tư 232/2012/TT-BTC`, `Thông tư 199/2014/TT-BTC`, `Luật KDBH (31/VBHN-VPQH)`, `Nghị định 46/2023/NĐ-CP` và `VBHN 44/2026/VBHN-TT-BTC` (`29/09/2026`); chạy tam giác `Chain-Ladder` chuẩn Bộ Tài chính; tính tỷ lệ giữ lại, hiệu quả nhượng tái, trần đầu tư, biên khả năng thanh toán (`Mẫu 7-PNT`) và vốn `RBC` trên số liệu `FY2025` của **`BVH`**, **`PVI`** và **`BIC`**.
- Bài trước liên quan: `013`, `F2`, `F4`, `F7`; dẫn tiếp sang `P4`.
- Thời lượng: `3 buổi học` + thực hành [`practice/models/insurance.py`](../practice/models/insurance.py) và [`geico_berkshire_fy2025_inputs.csv`](../practice/models/geico_berkshire_fy2025_inputs.csv).
- Câu hỏi cốt lõi: **Làm sao phân biệt doanh nghiệp bảo hiểm có kỷ luật khai thác thật sự với doanh nghiệp báo lãi ảo nhờ trích thiếu dự phòng `IBNR`, phụ thuộc hoa hồng nhượng tái hoặc đầu tư vượt trần pháp định?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

---

## Hiểu bài này trong 1 phút

BCTC doanh nghiệp bảo hiểm Việt Nam (`BVH`, `PVI`, `BIC`...) rất dễ gây hiểu lầm nếu đọc như doanh nghiệp sản xuất:
1. **Hàng trăm nghìn tỷ đồng tiền gửi và trái phiếu không phải "tiền mặt ròng" của cổ đông:** Tại Tập đoàn Bảo Việt (`BVH`) cuối năm `2025` (BCTC hợp nhất kiểm toán tr. 6–9, TM 14 tr. 48), danh mục đầu tư tài chính thuần đạt **`266.535,57 tỷ đồng`**, nhưng đối ứng bên Nợ phải trả là **`201.682,49 tỷ đồng` dự phòng nghiệp vụ** (dự phòng toán học nhân thọ `171.409,33 tỷ đồng` và dự phòng lãi cam kết tối thiểu `16.544,35 tỷ đồng`). VCSH hợp nhất của `BVH` chỉ là `25.480,34 tỷ đồng` (`8,73%` tổng tài sản `291.805,65 tỷ đồng`).
2. **Cấu trúc lợi nhuận phụ thuộc mô hình giữ lại và nhượng tái bảo hiểm:**
   - Phi nhân thọ bán lẻ như **Bảo hiểm BIDV (`BIC`)** đạt lãi gộp bảo hiểm `+994,94 tỷ đồng` năm `2025` (`Combined Ratio` giữ lại trước hoa hồng nhượng tái đạt `83,37%`, sau hoa hồng nhượng tái và thu khác còn `74,80%`) nhờ tỷ lệ bồi thường giữ lại `30,14%`.
   - Bảo hiểm công nghiệp — năng lượng — hàng không và tái bảo hiểm như **PVI Holdings (`PVI`)** thu `14.908,34 tỷ đồng` phí gốc và `10.498,98 tỷ đồng` phí nhận tái (tổng `25.407,32 tỷ đồng`), nhượng tái `17.178,02 tỷ đồng` (giữ lại `32,39%` tổng phí để bảo vệ vốn trước siêu rủi ro nhà máy, giàn khoan, tàu bay, bão lớn) và thu `1.337,61 tỷ đồng` **hoa hồng nhượng tái**.

Bốn trụ cột phân tích: (1) Dự phòng nghiệp vụ và tam giác `Chain-Ladder` (`Điều 35–40 VBHN 44/2026/VBHN-TT-BTC`); (2) Tái bảo hiểm, quy tắc không bù trừ (`vas_gross_vs_net_reserves()`) và rủi ro đối tác sau siêu bão `Yagi`; (3) Trần đầu tư `Điều 43 Nghị định 46/2023/NĐ-CP`; (4) Biên KNTT (`Mẫu 7-PNT`, `solvency_margin_pnt()`) và vốn `RBC` (`01/01/2028`).

---

## Ôn bài cũ và phạm vi bài học

- **Ôn bài cũ:** Bài `013` xây dựng cầu nối `GWP` $\to$ `NWP` $\to$ `UPR` $\to$ `NEP`, `Combined Ratio`, `Insurance Float` và `RIM`. Bài `F2` & `F4` đối chiếu chéo Bảng CĐKT, BCKQKD và Thuyết minh.
- **Bài này làm gì:** Buổi 1 giải phẫu kế toán bảo hiểm (`Thông tư 232/2012/TT-BTC`, `Thông tư 199/2014/TT-BTC`), dự phòng theo `Nghị định 46/2023/NĐ-CP` & `VBHN 44/2026/VBHN-TT-BTC` và tam giác `Chain-Ladder`; Buổi 2 phân tích tái bảo hiểm, trần đầu tư (`Điều 43 NĐ 46`), độ nhạy lãi suất dự phòng toán học (`vn_life_max_tech_rate()`, `math_reserve_rate_sensitivity()`) và BCTC `FY2025` của `BVH`, `PVI`, `BIC`; Buổi 3 phân tích vốn pháp định (`Điều 35 NĐ 46`), Biên KNTT (`Mẫu 7-PNT`), `RBC` (`01/01/2028`) và `RIM`.
- **Bài này chưa làm gì:** Chưa bóc tách hợp đồng bảo hiểm cá nhân (xem **[Bài P4](P4-personal-insurance-contracts-and-costs.md)**).

---

## Buổi 1 — Kế toán bảo hiểm Việt Nam, Dự phòng nghiệp vụ và Tam giác bồi thường `Chain-Ladder`

### 1.1. Giải phẫu BCKQKD và Bảng cân đối bảo hiểm Việt Nam (`Thông tư 232/2012/TT-BTC`)

Cầu nối doanh thu — chi phí bảo hiểm theo chuẩn `VAS` (hàm `pc_underwriting_bridge()` trong [`practice/models/insurance.py`](../practice/models/insurance.py)):

1. **Tổng phí gốc và nhận tái (`Gross & Assumed Written Premium`):** $\text{GWP} + \text{Phí nhận tái bảo hiểm}$ (sau giảm/hoàn phí).
2. **Phí giữ lại trước dự phòng (`NWP`):** Trừ **Tổng phí nhượng tái bảo hiểm (`Outward Reinsurance Ceded`)**.
3. **Doanh thu phí bảo hiểm thuần (`NEP`):**
   $$\text{NEP} = \text{NWP} - \left(\Delta \text{UPR}_{\text{gộp}} - \Delta \text{UPR}_{\text{nhượng tái}}\right)$$
4. **Doanh thu thuần HĐKDBH:** $\text{NEP} + \text{Hoa hồng nhượng tái bảo hiểm} + \text{Doanh thu khác HĐKDBH}$.
5. **Tổng chi trực tiếp HĐKDBH:** (i) Chi bồi thường gốc & nhận tái trừ giảm trừ (thu đòi người thứ ba, hàng xử lý 100%) và trừ **Thu bồi thường nhượng tái**; (ii) **Tăng/giảm dự phòng nghiệp vụ gốc** (dự phòng toán học, lãi cam kết tối thiểu, chia lãi, đảm bảo cân đối với nhân thọ) và **Tăng/giảm dự phòng bồi thường giữ lại** (`OSLR` + `IBNR`) cùng **Dự phòng dao động lớn (`Catastrophe Reserve`)**; (iii) Chi hoa hồng gốc và chi khác HĐKDBH.
6. **Quy tắc không bù trừ trên Bảng CĐKT (`vas_gross_vs_net_reserves()`):** `SỰ_THẬT` Theo `Thông tư 232/2012/TT-BTC`, **Dự phòng nghiệp vụ gốc và nhận tái** ghi nguyên giá bên **Nợ phải trả**, còn **Dự phòng phí nhượng tái** và **Dự phòng bồi thường nhượng tái** ghi tách biệt bên **Tài sản (`Tài sản tái bảo hiểm`)**.

### 1.2. Các loại dự phòng nghiệp vụ bắt buộc (`Điều 35–40 VBHN 44/2026/VBHN-TT-BTC`)

`SỰ_THẬT` Theo `Điều 35–40` của `VBHN 44/2026/VBHN-TT-BTC` ngày `29/09/2026` ([VBHN 44/2026/VBHN-TT-BTC](https://vanban.chinhphu.vn/?pageid=27160&docid=217205)):

- **Bảo hiểm Phi nhân thọ (`Điều 35, 36, 37`):**
  1. **Dự phòng phí chưa được hưởng (`UPR` — `Điều 35`, hàm `upr_percentage()`, `upr_1_8()`, `upr_1_24()`, `upr_daily()`):**
     - Tỷ lệ `%` tổng phí (`Khoản 1 Điều 35`): Hàng hóa vận chuyển $\le 1$ năm trích **`25%`**; loại hình khác $\le 1$ năm trích **`50%`**.
     - Hệ số thời hạn (`Khoản 2 Điều 35`): Hệ số `1/8` theo quý (`1/8, 3/8, 5/8, 7/8`); hệ số `1/24` theo tháng ($\frac{2m-1}{24}$); hoặc theo ngày ($\text{Phí} \times \frac{\text{Số ngày còn lại}}{\text{Tổng số ngày HĐ}}$).
  2. **Dự phòng bồi thường (`Claim Reserve` — `Điều 36`):** Gồm **OSLR (`Khoản 1`)** theo từng hồ sơ khiếu nại và **IBNR (`Khoản 2`)** theo **tam giác phát sinh bồi thường `Chain-Ladder`** hoặc công thức độ trễ / tối thiểu `3%–5%` phí giữ lại.
  3. **Dự phòng dao động lớn (`Catastrophe Reserve` — `Điều 37`):** Trích **`1%–3%`** phí giữ lại hàng năm đến khi số dư đạt **`100%` phí giữ lại trong năm** của nghiệp vụ đó.
- **Bảo hiểm Nhân thọ (`Điều 38, 39, 40`):**
  1. **Dự phòng toán học (`Mathematical Reserve` — `Điều 38`):** Hiện giá số tiền bảo hiểm phải trả tương lai trừ hiện giá phí thuần sẽ thu tương lai (Zillmer $\le 3\%$ số tiền bảo hiểm, không thấp hơn giá trị hoàn lại; bảng tử vong $\ge 80\%$ `CSO 1980`). Theo `Điểm b Khoản 2 Điều 38` (`vn_life_max_tech_rate()`), **lãi suất kỹ thuật tối đa** bằng $\min$ của: (i) **`80%` lãi suất TPCP kỳ hạn $\ge 10$ năm bình quân 24 tháng liền trước**; (ii) **lợi suất đầu tư bình quân 4 quý liền trước**; và (iii) **lãi suất tính phí sản phẩm**.
  2. **Dự phòng phí chưa được hưởng**, **Dự phòng bồi thường**, **Dự phòng chia lãi (`Điều 39`)**, **Dự phòng đảm bảo lãi suất cam kết** và **Dự phòng đảm bảo cân đối (`Điều 40`)**.

### 1.3. Tam giác phát sinh bồi thường (`Chain-Ladder`) chuẩn Bộ Tài chính (`Điều 36 VBHN 44/2026/VBHN-TT-BTC`)

`SỰ_THẬT` Tại `Điểm a Khoản 2 Điều 36 VBHN 44/2026/VBHN-TT-BTC` (tr. `42–45`), Bộ Tài chính ban hành tam giác bồi thường thực trả (`TT67_INCREMENTAL_TRIANGLE`) và lũy kế `2016–2023` (đơn vị: `triệu đồng`), cài đặt trong `incremental_to_cumulative_triangle()` và `chain_ladder_reserve()`:

| Năm tổn thất | Năm PT 1 | Năm PT 2 | Năm PT 3 | Năm PT 4 | Năm PT 5 | Năm PT 6 | Năm PT 7 | Năm PT 8 (`Ultimate`) | Đã trả đến cuối 2023 | Dự phòng cần trích (`IBNR + OSLR`) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **2016** | `5.445` | `8.602` | `11.052` | `12.464` | `13.064` | `13.416` | `13.847` | `14.032` | `14.032` | **`0`** |
| **2017** | `5.847` | `9.333` | `10.699` | `11.547` | `12.592` | `13.646` | `14.015` | ***`14.197`*** | `14.015` | **`182`** |
| **2018** | `5.981` | `10.835` | `12.783` | `15.337` | `17.017` | `17.506` | ***`18.031`*** | ***`18.266`*** | `17.506` | **`760`** |
| **2019** | `7.835` | `12.288` | `16.176` | `19.511` | `21.599` | ***`22.614`*** | ***`23.293`*** | ***`23.595`*** | `21.599` | **`1.996`** |
| **2020** | `9.763` | `16.280` | `19.843` | `23.827` | ***`25.948`*** | ***`27.167`*** | ***`27.982`*** | ***`28.346`*** | `23.827` | **`4.519`** |
| **2021** | `10.745` | `16.929` | `21.478` | ***`24.979`*** | ***`27.202`*** | ***`28.481`*** | ***`29.335`*** | ***`29.716`*** | `21.478` | **`8.238`** |
| **2022** | `14.137` | `22.253` | ***`27.505`*** | ***`31.988`*** | ***`34.835`*** | ***`36.472`*** | ***`37.566`*** | ***`38.055`*** | `22.253` | **`15.802`** |
| **2023** | `15.162` | ***`24.638`*** | ***`30.453`*** | ***`35.417`*** | ***`38.569`*** | ***`40.382`*** | ***`41.593`*** | ***`42.134`*** | `15.162` | **`26.972`** |
| **Hệ số $f_{k \to k+1}$** | | **`1,625`** | **`1,236`** | **`1,163`** | **`1,089`** | **`1,047`** | **`1,030`** | **`1,013`** | **Tổng (`149.872`):** | **`58.469`** |

- **Quy tắc 4 bước (`average_method="simple_tt67"`):** (1) Cộng dồn sang bảng lũy kế $C_{i, k}$; (2) Tính $f_{i, k\to k+1} = C_{i, k+1} / C_{i, k}$ (làm tròn `3 chữ số thập phân`); (3) Lấy trung bình giản đơn từng cột được $f = [1,625;\; 1,236;\; 1,163;\; 1,089;\; 1,047;\; 1,030;\; 1,013]$; (4) Nhân liên tiếp giá trị trên đường chéo với các hệ số $f$ còn lại đến cột 8 (`Ultimate = 208.341 triệu đồng`) rồi trừ số đã trả (`149.872 triệu đồng`), được dự phòng cần trích **`58.469 triệu đồng`**.
- **Ba điều kiện làm `Chain-Ladder` thuần túy bị gãy (`Model Risk`):**
  1. **Đột biến lạm phát bồi thường (`Claims & Medical Inflation`):** Giá phụ tùng ô tô và viện phí tăng vọt so với quá khứ làm hệ số lịch sử đánh giá thấp nghĩa vụ thực tế.
  2. **Tắc nghẽn giám định sau thiên tai / dịch bệnh:** Làm số thực trả Năm 1 thấp bất thường; nhân hệ số $f$ lịch sử với cơ sở Năm 1 bị nén sẽ gây thiếu hụt dự phòng.
  3. **Nghiệp vụ đuôi dài (`Long-tail Lines`):** Ở năm tổn thất mới nhất, số tiền đã trả còn nhỏ và nhiễu; chuyên gia định phí (`Actuary`) phải kết hợp **`Bornhuetter-Ferguson (B-F)`** (pha trộn `Expected Loss Ratio` với dữ liệu thực tế) hoặc trung bình gia quyền quy mô (`average_method="volume_weighted"`).

---

## Buổi 2 — Tái bảo hiểm, Danh mục đầu tư tài chính và So sánh `BVH` — `PVI` — `BIC`

### 2.1. Kinh tế học Tái bảo hiểm (`Reinsurance`), rủi ro đối tác và cú sốc siêu bão `Yagi` (`09/2024`)

1. **Tỷ lệ giữ lại phí (`Retention Ratio`):** $\frac{\text{NWP}}{\text{GWP + Assumed Premium}}$. Bán lẻ phân tán (`BIC`) giữ lại cao (**`69,58%`**); bảo hiểm công nghiệp — năng lượng — hàng không và tái bảo hiểm (`PVI`) giữ lại thấp (**`32,39%`**) để bảo vệ vốn và tuân thủ trần giữ lại đơn lẻ $\le$ **`10%` VCSH** (`Khoản 4 Điều 33 VBHN 44/2026/VBHN-TT-BTC`).
2. **Tỷ lệ hoa hồng nhượng tái (`Ceding Commission Rate`):** $\frac{\text{Hoa hồng nhượng tái}}{\text{Phí nhượng tái}}$.
3. **Rủi ro tín dụng đối tác tái bảo hiểm (`Reinsurance Credit Risk`) và siêu bão `Yagi` (`09/2024`):**
   - Nhượng tái không xóa nghĩa vụ pháp lý của công ty gốc với khách hàng (`Khoản 2 Điều 28 VBHN 44`). `SỰ_THẬT` Theo `Khoản 2 Điều 33 Nghị định 46/2023/NĐ-CP` và `Điều 19, 23, 25 VBHN 44`, nhà nhận tái nước ngoài đứng đầu và nhà nhận tái $\ge 10\%$ trách nhiệm phải đạt xếp hạng tối thiểu **`"BBB"` (S&P/Fitch), `"B++"` (A.M. Best) hoặc `"Baa1"` (Moody's)**.
   - **Bằng chứng thực tế từ siêu bão `Yagi` (`09/2024`):** Theo Bộ Tài chính, bão `Yagi` gây thiệt hại thuộc phạm vi bảo hiểm khoảng **`13.000 tỷ đồng`** toàn ngành. Nhờ nhượng tái phần lớn rủi ro tài sản — kỹ thuật, `Loss Ratio` giữ lại năm `2025` của `PVI` chỉ ở mức `43,05%`, nhưng trên Bảng CĐKT hợp nhất kiểm toán `FY2025` của `PVI` (TM 5, tr. 32), **Dự phòng bồi thường nhượng tái** tăng hơn gấp đôi từ `7.518,47 tỷ` cuối `2024` lên **`15.368,84 tỷ đồng`** cuối `2025` (nằm trong **Tài sản tái bảo hiểm `21.614,45 tỷ đồng`**, gấp **`2,53 lần`** VCSH `8.533,91 tỷ đồng`).
   - **Hệ quả chu kỳ (`Reinsurance Hardening`):** Sau thảm họa lớn, nhà tái bảo hiểm quốc tế thường tăng phí tái tục, nâng mức tự giữ lại (`Retention`) và giảm tỷ lệ hoa hồng nhượng tái.

### 2.2. Giới hạn đầu tư từ nguồn dự phòng nghiệp vụ (`Điều 43 Nghị định 46/2023/NĐ-CP`) và Rủi ro lãi suất nhân thọ

`SỰ_THẬT` Theo `Điều 100 Luật KDBH (31/VBHN-VPQH)` và **`Điều 43 Nghị định 46/2023/NĐ-CP`** ([Nghị định 46/2023/NĐ-CP](https://vanban.chinhphu.vn/?pageid=27160&docid=208265)):

| Nhóm tài sản đầu tư từ nguồn dự phòng nghiệp vụ | Trần **DNBH Nhân thọ** (`Khoản 2 Điều 43`) | Trần **DNBH Phi nhân thọ & Tái BH** (`Khoản 3 Điều 43`) |
|---|---|---|
| 1. TPCP, tín phiếu Kho bạc, TP được CP bảo lãnh, Tiền gửi tại TCTD | **Không hạn chế (`100%`)** | **Không hạn chế (`100%`)** |
| 2. Cổ phiếu, trái phiếu doanh nghiệp (có/không bảo lãnh), CCQ | Tối đa **`50%`** | Tối đa **`35%`** |
| 3. Kinh doanh bất động sản (trừ mua CP/CCQ BĐS hoặc trụ sở từ VCSH) | **Cấm tuyệt đối (`0%`)** (`Điều 100 Luật KDBH`) | **Cấm tuyệt đối (`0%`)** (`Điều 100 Luật KDBH`) |
| 4. Góp vốn vào các doanh nghiệp khác | Tối đa **`20%`** | Tối đa **`20%`** |

- **Độ nhạy lãi suất ngược chiều (`vn_life_max_tech_rate()` & `math_reserve_rate_sensitivity()`):** Phi nhân thọ (`BIC`, `PVI`) có nghĩa vụ ngắn hạn nên hưởng lợi ngay khi lãi suất tiền gửi tăng. Ngược lại, nhân thọ (`BVH`) chịu cú sốc kép khi lợi suất TPCP $\ge 10$ năm giảm sâu: trần lãi suất kỹ thuật bị khóa ở $\min(80\% \times \text{lãi suất TPCP } \ge 10\text{Y bình quân 24 tháng},\; \text{lợi suất đầu tư 4 quý},\; \text{lãi suất tính phí})$ (`Điểm b Khoản 2 Điều 38 VBHN 44`). Khi lãi suất kỹ thuật giảm từ $r_{\text{cũ}}$ xuống $r_{\text{mới}}$ trên kỳ hạn $D$ năm, dự phòng toán học phải tăng theo $\left(\frac{1+r_{\text{cũ}}}{1+r_{\text{mới}}}\right)^D - 1$, buộc `BVH` duy trì **Dự phòng toán học `171.409,33 tỷ đồng`** và **Dự phòng lãi cam kết tối thiểu `16.544,35 tỷ đồng`** cuối `2025`.

---

## Buổi 3 — Vốn pháp định, Biên khả năng thanh toán (`Mẫu 7-PNT`), Lộ trình Vốn `RBC` (`01/01/2028`) và Định giá

- **Vốn điều lệ tối thiểu (`Điều 35 Nghị định 46/2023/NĐ-CP`):** Phi nhân thọ **`400–500 tỷ đồng`**; Nhân thọ **`750–1.300 tỷ đồng`** (`1.000 tỷ` nếu có `UL/ILP` hoặc hưu trí; `1.300 tỷ` nếu kinh doanh cả 3 nhóm); Tái bảo hiểm **`400–1.100 tỷ đồng`**.
- **Hai giai đoạn áp dụng chuẩn an toàn vốn (`Điều 157 Luật KDBH 31/VBHN-VPQH`):**
  1. **Đến trước `01/01/2028` — Biên KNTT (`Mẫu 7-PNT / 7-NT` tại `VBHN 44/2026/VBHN-TT-BTC` tr. `137–138`, hàm `solvency_margin_pnt()`):**
     - **Biên KNTT tối thiểu (PNT):** $\text{MSM}_{\text{PNT}} = \max(25\% \times \text{Tổng phí giữ lại},\; 12,5\% \times \text{Tổng phí gốc và nhận tái})$.
     - **Biên KNTT thực tế:** VCSH hợp lệ trừ giảm trừ tài sản (`Asset Haircuts`): loại trừ **`100%`** phải thu quá hạn $\ge 2$ năm/tạm ứng/trả trước; cắt giảm **`1%`** TPDN có bảo đảm, **`3%`** TPDN không bảo đảm, **`15%`** cổ phiếu niêm yết & CCQ, **`20%`** cổ phiếu chưa niêm yết, **`25%`** TSCĐ hữu hình, phần mềm, quyền sử dụng đất, hàng tồn kho. Tại `31/12/2025` (TM 40 tr. 84 BCTC `BVH`): **Bảo hiểm Bảo Việt (PNT)** đạt `2.692,49 / 1.916,39 =` **`141%`**; **Bảo Việt Nhân thọ** đạt `9.921,65 / 9.269,95 =` **`107%`**.
  2. **Từ `01/01/2028` (`Khoản 2 Điều 157 Luật KDBH`) — Vốn trên cơ sở rủi ro (`RBC`, `Điều 94, 95, 108, 109 Luật KDBH`):**
     $$C_{\text{req}} = \sqrt{R_{\text{ins}}^2 + R_{\text{mkt}}^2} + R_{\text{cred}} + R_{\text{op}}, \qquad \text{CAR} = \frac{\text{Available Capital}}{C_{\text{req}}} \times 100\%$$
     $\text{CAR} \ge 100\%$: **An toàn**; $80\% \le \text{CAR} < 100\%$: **Tự khắc phục sớm (`Điều 108`)**; $\text{CAR} < 80\%$: **Kiểm soát đặc biệt (`Điều 109`)**.

---

## Ví dụ từ nguồn thật

Đối chiếu BCTC hợp nhất `FY2025` (kết thúc `31/12/2025`, chuẩn `VAS`, đơn vị: `tỷ đồng`) của **`BVH`** (EY Việt Nam kiểm toán `31/03/2026`), **`PVI`** (PwC Việt Nam kiểm toán `15/02/2026`) và **`BIC`** (ký `23/01/2026`), đã nạp trong [`geico_berkshire_fy2025_inputs.csv`](../practice/models/geico_berkshire_fy2025_inputs.csv):

| Chỉ tiêu tài chính & nghiệp vụ (`FY2025`, đơn vị: `tỷ đồng`) | **Tập đoàn Bảo Việt (`BVH`)** *(Nhân thọ + Phi nhân thọ)* | **PVI Holdings (`PVI`)** *(Bảo hiểm Công nghiệp & Tái BH)* | **Bảo hiểm BIDV (`BIC`)** *(Phi nhân thọ Bán lẻ / Bancassurance)* |
|---|---:|---:|---:|
| **A. Bảng cân đối kế toán tại `31/12/2025`** | | | |
| 1. Tổng cộng tài sản (`Total Assets`) | `291.805,65` *(tr. 7)* | `44.512,14` *(tr. 5)* | `10.079,69` *(tr. 4)* |
| 2. Tổng danh mục đầu tư tài chính thuần (ngắn + dài hạn) | `266.535,57` *(TM 14, tr. 48)* | `16.707,55` *(tr. 5, chưa kể BĐSĐT `661,03`)* | `7.202,47` *(tr. 3–4)* |
| 3. Dự phòng nghiệp vụ gốc & nhận tái (`Gross Reserves`) | `201.682,49` *(Mã 344, tr. 8)* | `28.417,50` *(TM 18a, tr. 42)* | `4.447,34` *(Mã 329, tr. 5)* |
| 4. Tài sản tái bảo hiểm (`Reinsurance Assets`) | `3.682,41` *(Mã 190, tr. 6)* | `21.614,45` *(TM 5, tr. 32)* | `1.625,29` *(Mã 190, tr. 3)* |
| 5. Dự phòng nghiệp vụ giữ lại thuần (`Net Reserves`) (`PHÉP_TÍNH`) | `198.000,08` *(PNT thuần: `5.548,82`)* | `6.803,05` | `2.822,05` |
| 6. Vốn chủ sở hữu hợp nhất (`Owners' Equity`) | `25.480,34` *(Mã 400, tr. 9)* | `8.533,91` *(Mã 400, tr. 6)* | `3.384,46` *(Mã 400, tr. 6)* |
| **B. Khai thác Bảo hiểm & Tái bảo hiểm `FY2025`** | | | |
| 7. Phí bảo hiểm gốc (`GWP`) | `43.716,18` *(NT `32.641,79` + PNT `11.074,40`)* | `14.908,34` *(TM 23, tr. 46)* | `5.696,79` *(Mã 01.1, tr. 8)* |
| 8. Phí nhận tái bảo hiểm (`Assumed Premium`) | `399,97` *(Mã 03, tr. 10)* | `10.498,98` *(TM 23, tr. 46)* | `92,70` *(Mã 01.2, tr. 8)* |
| 9. Tổng phí nhượng tái bảo hiểm (`Ceded Premium`) | `-3.808,52` *(Mã 06, tr. 10)* | `-17.178,02` *(TM 23, tr. 46)* | `-1.760,93` *(Mã 02.1, tr. 8)* |
| 10. Phí bảo hiểm giữ lại trước dự phòng (`NWP`) (`PHÉP_TÍNH`) | `40.307,63` | `8.229,30` | `4.028,55` |
| 11. Tỷ lệ giữ lại phí (`Retention Ratio`) (`PHÉP_TÍNH`) | **`91,37%`** *(PNT giữ lại `66,78%`)* | **`32,39%`** | **`69,58%`** |
| 12. Doanh thu phí bảo hiểm thuần đã hưởng (`NEP`) | `40.123,67` *(Mã 08, tr. 10)* | `7.633,90` *(TM 23, tr. 46)* | `3.948,22` *(Mã 03, tr. 8)* |
| 13. Hoa hồng nhượng tái & thu khác HĐKDBH | `824,59` *(HH nhượng tái `776,40`)* | `1.337,61` *(HH nhượng tái, tr. 46)* | `338,33` *(HH nhượng tái `272,28`)* |
| 14. Chi bồi thường & trích dự phòng giữ lại (`Net Claims & Reserves`) | `35.123,28` *(trích DP toán học `+14.260,75`)* | `3.286,62` *(TM 24, tr. 47)* | `1.189,95` *(Bồi thường `1.149,65` + DPĐĐL `40,31`)* |
| 15. `Loss Ratio` giữ lại (trên `NEP`) (`PHÉP_TÍNH`) | *Tách riêng NT & PNT* | **`43,05%`** *(trước DPĐĐL: `41,55%`)* | **`30,14%`** *(trước DPĐĐL: `29,12%`)* |
| 16. `Combined Ratio` giữ lại trước / sau HH nhượng tái (`PHÉP_TÍNH`) | *Tách riêng NT & PNT* | **`106,06%` / `88,54%`** | **`83,37%` / `74,80%`** |
| **C. Đầu tư Tài chính & Lợi nhuận Ròng `FY2025`** | | | |
| 17. Doanh thu tài chính / Lợi nhuận tài chính thuần | `14.039,76` / `11.120,47` *(tr. 11)* | `1.411,37` / `918,21` *(tr. 7)* | `548,56` / `510,29` *(tr. 7 & 9)* |
| 18. Tổng lợi nhuận trước thuế (`EBT`) / Sau thuế (`NPAT`) | `3.554,43` / `2.921,57` *(tr. 11–12)* | `1.459,67` / `1.152,11` *(tr. 7)* | `678,79` / `551,89` *(tr. 7 & 9)* |

`SUY_LUẬN` Ba cột số liệu thể hiện 3 mô hình kinh tế: (1) Tại **`BVH`**, chi bồi thường gồm khoản trích dự phòng toán học nhân thọ `+14.260,75 tỷ đồng`, mảng bảo hiểm lãi gộp `+1.237,95 tỷ đồng` (đảo chiều từ lỗ `-969,11 tỷ` năm `2024`), cộng `+11.120,47 tỷ đồng` lãi tài chính thuần từ danh mục `266.535,57 tỷ đồng` giúp `NPAT` đạt `2.921,57 tỷ đồng`; (2) Tại **`PVI`**, công ty nhượng tái `67,61%` tổng phí và thu `1.337,61 tỷ đồng` hoa hồng nhượng tái, đưa `Combined Ratio` ròng về `88,54%`; (3) Tại **`BIC`**, kỷ luật khai thác bán lẻ (`Loss Ratio = 30,14%`, `Combined Ratio` ròng `74,80%`, lãi gộp bảo hiểm `+994,94 tỷ đồng`) cộng lãi tài chính `+510,29 tỷ đồng` giúp `NPAT` đạt `551,89 tỷ đồng`.

---

## Bài tập

Tự giải trước khi mở Đáp án; kiểm chứng bằng `python3 learning/practice/models/insurance.py`.

1. **(Cầu nối phí và tái bảo hiểm của `PVI` `FY2025`):** Từ TM 23–24 BCTC `FY2025` của `PVI` (`GWP = 14.908,34 tỷ`, phí nhận tái `10.498,98 tỷ`, phí nhượng tái `17.178,02 tỷ`, $\Delta \text{UPR} = 595,40\text{ tỷ}$, hoa hồng nhượng tái `1.337,61 tỷ`, chi bồi thường và DP giữ lại `3.286,62 tỷ`, chi khác HĐKDBH `4.810,00 tỷ`), tính: (a) Tổng phí gốc và nhận tái; (b) `NWP` và `Retention Ratio`; (c) `NEP` và `Ceding Commission Rate`; (d) `Combined Ratio` trước và sau HH nhượng tái.
2. **(Hiệu quả khai thác của `BIC` `FY2025`):** Dùng `pc_underwriting_bridge()` với BCTC `FY2025` của `BIC` (`GWP = 5.696,79 tỷ`, phí nhận tái `92,70 tỷ`, phí nhượng tái `1.760,93 tỷ`, tăng DP phí gốc & nhận tái `215,37 tỷ`, tăng DP phí nhượng tái `135,04 tỷ`, chi bồi thường + tăng DP dao động lớn `1.149,65 + 40,31 = 1.189,95 tỷ`, chi khác HĐKDBH `2.101,66 tỷ`, HH nhượng tái & thu khác `338,33 tỷ`), tính: (a) `NEP`; (b) `Loss Ratio` giữ lại; (c) `Expense Ratio` và `Combined Ratio` trước và sau khi trừ `338,33 tỷ`; (d) Lãi gộp HĐKDBH.
3. **(Hệ số phát sinh cột `1 -> 2` trong Tam giác `Chain-Ladder`):** Từ bảng tam giác lũy kế tại `Điều 36 VBHN 44/2026/VBHN-TT-BTC` ở Buổi 1, tính $f_{i, 1\to 2} = C_{i, 2}/C_{i, 1}$ cho từng năm `2016–2022` (làm tròn 3 chữ số thập phân) và trung bình cộng giản đơn của 7 hệ số đó.
4. **(Phóng chiếu `Ultimate Loss` và dự phòng năm `2022` & `2023` bằng `chain_ladder_reserve()`):** Dùng $f = [1,625;\; 1,236;\; 1,163;\; 1,089;\; 1,047;\; 1,030;\; 1,013]$ (nhân liên tiếp không làm tròn trung gian, làm tròn kết quả cuối đến hàng đơn vị theo bảng tr. 44–45 `VBHN 44`), tính `Ultimate Loss` ở cột 8 và dự phòng cần trích cuối năm `2023` cho năm `2022` (cột 2 = `22.253`) và `2023` (cột 1 = `15.162`).
5. **(Trần dự phòng dao động lớn theo `Điều 37 VBHN 44/2026/VBHN-TT-BTC`):** Nghiệp vụ xe cơ giới có phí giữ lại năm `2025` là `2.400 tỷ đồng`, số dư quỹ DP dao động lớn đầu năm là `2.360 tỷ đồng`, tỷ lệ trích đăng ký `2,5%`. Năm `2025` được trích tối đa bao nhiêu tỷ đồng vào quỹ này? Vì sao không được trích `60 tỷ đồng`?
6. **(Kiểm tra giới hạn đầu tư theo `Điều 43 Nghị định 46/2023/NĐ-CP`):** DNBH phi nhân thọ có nguồn dự phòng nhàn rỗi `6.000 tỷ đồng`, dự kiến phân bổ: tiền gửi `2.700 tỷ`; TPCP `800 tỷ`; cổ phiếu và TPDN `2.250 tỷ`; mua đất nền và căn hộ trực tiếp `250 tỷ`. Chỉ ra **2 vi phạm pháp luật** và số tiền vượt trần.
7. **(Biên khả năng thanh toán theo `Mẫu 7-PNT` — hàm `solvency_margin_pnt()`):** DNBH phi nhân thọ có tổng phí gốc và nhận tái `9.000 tỷ`, phí giữ lại `4.000 tỷ`, VCSH đủ điều kiện `2.000 tỷ`, nắm giữ: TPDN có bảo đảm `100 tỷ`, TPDN không bảo đảm `200 tỷ`, cổ phiếu niêm yết & CCQ `400 tỷ`, cổ phiếu chưa niêm yết `100 tỷ`, TSCĐ hữu hình & phần mềm `200 tỷ`, phải thu quá hạn $> 2$ năm `50 tỷ`. Tính: (a) Biên KNTT tối thiểu; (b) Tổng giảm trừ tài sản; (c) Biên KNTT thực tế và Tỷ lệ biên KNTT.
8. **(Trần lãi suất kỹ thuật và độ nhạy Dự phòng toán học theo `Điều 38 VBHN 44` — hàm `vn_life_max_tech_rate()` & `math_reserve_rate_sensitivity()`):** Lãi suất TPCP $\ge 10$ năm bình quân 24 tháng trước là `3,00%/năm`, lợi suất đầu tư 4 quý trước là `5,00%/năm`, lãi suất tính phí là `4,00%/năm`. Tính: (a) Trần lãi suất kỹ thuật tối đa; (b) Nếu lãi suất kỹ thuật chiết khấu dòng nghĩa vụ thuần `1.000 tỷ đồng` kỳ hạn $D = 15\text{ năm}$ hạ từ `3,50%` xuống `2,50%`, dự phòng toán học phải trích tăng bao nhiêu tỷ đồng và bao nhiêu `%`?
9. **(Rủi ro tập trung tái bảo hiểm tại `PVI` sau siêu bão `Yagi`):** Cuối `2025`, `PVI` có Tài sản tái bảo hiểm `21.614,45 tỷ đồng` (dự phòng bồi thường nhượng tái `15.368,84 tỷ`) và VCSH `8.533,91 tỷ đồng`. Tính `Reinsurance Assets / Equity` và mức giảm VCSH trước thuế nếu `5%` dự phòng bồi thường nhượng tái không thu hồi được.
10. **(Định giá `RIM` khi phát hiện trích thiếu dự phòng `Chain-Ladder` — hàm `reserve_understatement_adjustment()`):** DNBH có VCSH báo cáo `3.200 tỷ đồng` (`200 triệu CP`, thị giá `21.000 đồng/CP`), dự phòng bồi thường báo cáo `980 tỷ` nhưng `Chain-Ladder` cần trích `1.280 tỷ` (thiếu `300 tỷ` trước thuế, thuế `20%`). Với $\text{ROE} = 14,5\%$, payout `50%`, $r_e = 12,5\%$, $g = 5,0\%$ sau năm 5, tính $B_0^{\text{adj}}$ và giá trị ước tính theo mô hình mỗi cổ phiếu bằng `RIM` 5 năm.

---

## Đáp án

<details>
<summary>Mở sau khi đã tự giải cả 10 bài tập</summary>

1. **`PHÉP_TÍNH`:** (a) Tổng phí gốc & nhận tái $= 14.908,34 + 10.498,98 = 25.407,32\text{ tỷ đồng}$; (b) `NWP` $= 25.407,32 - 17.178,02 = 8.229,30\text{ tỷ đồng}$, `Retention Ratio` $= 32,39\%$; (c) `NEP` $= 8.229,30 - 595,40 = 7.633,90\text{ tỷ đồng}$, `Ceding Commission Rate` $= 1.337,61 / 17.178,02 = 7,79\%$; (d) `Loss Ratio` $= 3.286,62 / 7.633,90 = 43,05\%$; `Expense Ratio` trước HH nhượng tái $= 4.810,00 / 7.633,90 = 63,01\% \implies \text{Combined Ratio (Gross)} = 106,06\%$; sau khi trừ `1.337,61 tỷ` HH nhượng tái, chi phí ròng $= 3.472,39\text{ tỷ}$ (`45,49%` `NEP`) $\implies$ **`Combined Ratio (Net)` $= 88,54\%$**.
2. **`PHÉP_TÍNH`:** Chạy `pc_underwriting_bridge()`: (a) `NWP` $= 4.028,55\text{ tỷ}$; tăng DP phí giữ lại thuần $= 215,37 - 135,04 = 80,33\text{ tỷ} \implies \text{NEP} = 3.948,22\text{ tỷ đồng}$. (b) `Loss Ratio` $= 1.189,95 / 3.948,22 = 30,14\%$. (c) Trước HH nhượng tái & thu khác: `Expense Ratio` $= 53,23\% \implies \text{Combined Ratio} = 83,37\%$; sau khi trừ `338,33 tỷ`: chi phí ròng $= 1.763,33\text{ tỷ}$ (`44,66%`) $\implies$ **`Combined Ratio (Net)` $= 74,80\%$**. (d) Lợi nhuận gộp HĐKDBH $= +994,94\text{ tỷ đồng}$ (khớp Mã `19` tr. 9 BCTC `BIC`).
3. **`PHÉP_TÍNH`:** $f_{2016} = 1,580$; $f_{2017} = 1,596$; $f_{2018} = 1,812$; $f_{2019} = 1,568$; $f_{2020} = 1,668$; $f_{2021} = 1,576$; $f_{2022} = 1,574$. Trung bình cộng giản đơn $= 11,374 / 7 = 1,624857\dots \approx$ **`1,625`** (khớp bảng chuẩn tại `Điều 36 VBHN 44/2026/VBHN-TT-BTC`).
4. **`PHÉP_TÍNH`:** (a) Năm `2022`: $\text{Ultimate}_{2022} = 22.253 \times 1,236 \times 1,163 \times 1,089 \times 1,047 \times 1,030 \times 1,013 = 38.055\text{ triệu đồng}$; Dự phòng cần trích $= 38.055 - 22.253 = 15.802\text{ triệu đồng}$. (b) Năm `2023`: $\text{Ultimate}_{2023} = 15.162 \times 1,625 \times 1,236 \times 1,163 \times 1,089 \times 1,047 \times 1,030 \times 1,013 = 42.134\text{ triệu đồng}$; Dự phòng cần trích $= 42.134 - 15.162 = 26.972\text{ triệu đồng}$ (hai năm chiếm **`73,16%`** tổng dự phòng `58.469 triệu đồng`).
5. **`PHÉP_TÍNH` & `SỰ_THẬT`:** Theo `Điều 37 VBHN 44/2026/VBHN-TT-BTC`, quỹ dự phòng dao động lớn trích đến khi đạt `100%` phí giữ lại trong năm (`2.400 tỷ đồng`). Vì đầu năm đã có `2.360 tỷ đồng`, công ty chỉ được trích tối đa $2.400 - 2.360 = 40\text{ tỷ đồng}$.
6. **`PHÉP_TÍNH` & `SỰ_THẬT`:** (1) Mua đất nền/căn hộ trực tiếp `250 tỷ đồng` vi phạm điều cấm kinh doanh BĐS tại `Khoản 3 Điều 100 Luật KDBH` (vượt trần `250 tỷ đồng`); (2) Cổ phiếu + TPDN `2.250 tỷ đồng` (`37,5%`) vượt trần `35%` (`2.100 tỷ đồng`) tại `Khoản 3 Điều 43 Nghị định 46/2023/NĐ-CP` một khoản `150 tỷ đồng`.
7. **`PHÉP_TÍNH`:** Chạy `solvency_margin_pnt()`: (a) Biên KNTT tối thiểu $= \max(25\% \times 4.000 = 1.000,\; 12,5\% \times 9.000 = 1.125) = 1.125\text{ tỷ đồng}$. (b) Tổng giảm trừ tài sản $= 50 + 1 + 6 + 60 + 20 + 50 = 187\text{ tỷ đồng}$. (c) Biên KNTT thực tế $= 2.000 - 187 = 1.813\text{ tỷ đồng}$; Tỷ lệ biên KNTT $= 161,16\%$.
8. **`PHÉP_TÍNH`:** (a) Chạy `vn_life_max_tech_rate(0.03, 0.05, 0.04)`: $\min(2,40\%,\; 5,00\%,\; 4,00\%) =$ **`2,40%/năm`**. (b) Chạy `math_reserve_rate_sensitivity(1000.0, 15.0, 0.035, 0.025)`: dự phòng cũ $= 596,89\text{ tỷ}$; dự phòng mới $= 690,47\text{ tỷ} \implies$ tăng thêm **`+93,57 tỷ đồng`** (**`+15,68%`**).
9. **`PHÉP_TÍNH`:** `Reinsurance Assets / Equity` $= 21.614,45 / 8.533,91 = 253,28\%$. Nếu `5%` dự phòng bồi thường nhượng tái (`15.368,84 tỷ`) không thu hồi được, khoản lỗ trước thuế là `768,44 tỷ đồng`, làm giảm **`9,00%`** VCSH (`52,65%` `EBT` năm `2025` của `PVI`).
10. **`PHÉP_TÍNH`:** Chạy `reserve_understatement_adjustment()`: thiếu hụt sau thuế $= 240\text{ tỷ} \implies B_0^{\text{adj}} = 2.960\text{ tỷ đồng}$ (`14.800 đồng/CP`). Chiết khấu `RIM` 5 năm cho $PV(\text{RI}_{1..5}) = 247,56\text{ tỷ}$, $PV(\text{Terminal RI}) = 656,36\text{ tỷ} \implies V_0^{\text{adj}} = 3.863,92\text{ tỷ đồng}$, tương đương **`19.320 đồng/cổ phiếu`**.

</details>

---

## Bài làm với dữ liệu thiếu hoặc lệch

**Đề bài:** Khi đọc BCTC hợp nhất kiểm toán `FY2025` của Tập đoàn Bảo Việt (`BVH`), bạn gặp 3 điểm lệch bề mặt:
1. Ở **BCKQKD hợp nhất (tr. 10)**, Mã `01` (*Doanh thu phí bảo hiểm*) là `43.728.345.353.632 VND`, nhưng ở **TM 37 (Báo cáo bộ phận, tr. 77)**, cột *Hoạt động bảo hiểm* ghi `43.730.843 triệu đồng` (cao hơn `2.498 triệu đồng`).
2. Ở **Mã `09` (tr. 10)**, *Hoa hồng nhượng tái bảo hiểm và doanh thu khác HĐKDBH* là `824.585.918.049 VND`, nhưng ở **TM 18 (tr. 57)**, *Thu hoa hồng nhượng tái bảo hiểm* chỉ là `776.403.692.982 VND` (dòng *Bảo hiểm nhân thọ* ghi âm `(2.229.860.912) VND`).
3. Ở **TM 24 (Dự phòng nghiệp vụ, tr. 61)**, bảng trên ghi *Dự phòng đảm bảo cân đối* cuối ngày `31/12/2025` là `329.353.303.473 VND`, còn bảng dưới (*Dự phòng thuần*) ghi `329.353.303.474 VND` (lệch `1 VND`).

Bạn làm sạch và đối chiếu 3 điểm này như thế nào?

<details>
<summary>Xem quy trình đối chiếu chéo 3 bước</summary>

1. **`PHÉP_TÍNH` (Loại trừ giao dịch nội bộ khi hợp nhất — TM 37 tr. 77):** Khoản `(2.498) triệu đồng` ở cột *Điều chỉnh hợp nhất* là phí bảo hiểm các đơn vị trong Tập đoàn Bảo Việt mua của nhau, phải loại trừ khi hợp nhất (`43.730.843 - 2.498 = 43.728.345 triệu đồng`).
2. **`PHÉP_TÍNH` (Tách Hoa hồng nhượng tái khỏi Doanh thu khác HĐKDBH — TM 18 tr. 57):** Mã `09` (`824,59 tỷ đồng`) gộp *Thu hoa hồng nhượng tái* (`776,40 tỷ đồng`) và *Doanh thu khác HĐKDBH* (`48,18 tỷ đồng`). Khi tính `Ceding Commission Rate` lấy `776,40 tỷ đồng`; khi chạy cầu nối lợi nhuận gộp (`pc_underwriting_bridge()`) đưa đủ `824,59 tỷ đồng` để khớp Mã `15` (`40.948,25 tỷ đồng`).
3. **`PHÉP_TÍNH` (Xử lý sai số làm tròn 1 VND ở TM 24 tr. 61 — hàm `vas_gross_vs_net_reserves()`):** Tổng dự phòng PNT gốc & nhận tái (`9.231.232.250.280 VND`) trừ Tài sản tái bảo hiểm (`3.682.410.198.617 VND`) bằng đúng `5.548.822.051.663 VND`; lệch `1 VND` do làm tròn dòng thành phần, không trọng yếu.

</details>

---

## Sai ở đâu

**Nhận định sai lầm:** *"Tập đoàn Bảo Việt (`BVH`) chi tới `35.137 tỷ đồng` bồi thường và trả tiền bảo hiểm năm `2025` trên `40.124 tỷ đồng` phí thuần nên mảng bảo hiểm hầu như không tạo ra giá trị! Ngược lại, Công ty Bảo hiểm Phi nhân thọ Z vừa hạ tỷ lệ trích dự phòng `IBNR` từ `8%` xuống `2%` phí giữ lại giúp lợi nhuận tăng gấp đôi, lại vừa lấy `30%` quỹ dự phòng nghiệp vụ đi mua đất nền vùng ven đón sóng hạ tầng — cổ phiếu Z chắc chắn là siêu cổ phiếu!"*

<details>
<summary>Mở sau khi tự tìm lỗi</summary>

1. **Đọc tách rời chi phí trích dự phòng toán học và lợi nhuận tài chính của bảo hiểm nhân thọ (`BVH`):** Trong `35.137,29 tỷ đồng` chi bồi thường và trả tiền bảo hiểm của `BVH` năm `2025` (tr. 10), có tới **`14.260,75 tỷ đồng` là khoản trích tăng Dự phòng toán học** tích lũy cho khách hàng nhân thọ (và mảng bảo hiểm `BVH` vẫn lãi gộp `+1.237,95 tỷ đồng`). Chính khối dự phòng `201.682,49 tỷ đồng` đem đầu tư TPCP và tiền gửi đã tạo ra **`+11.120,47 tỷ đồng` lợi nhuận tài chính thuần**.
2. **Tung hô lợi nhuận ảo từ cắt giảm dự phòng `IBNR`:** Dự phòng `IBNR` phải tính khách quan theo tam giác `Chain-Ladder` (`Điều 36 VBHN 44/2026/VBHN-TT-BTC`). Hạ `IBNR` từ `8%` xuống `2%` là rút ruột dự phòng để báo lãi khống hôm nay.
3. **Cổ vũ hành vi vi phạm điều cấm đầu tư bất động sản:** `Khoản 3 Điều 100 Luật KDBH` **nghiêm cấm** dùng nguồn dự phòng nghiệp vụ để kinh doanh bất động sản trực tiếp.

</details>

---

## Kiểm tra chuyển bài

1. Ba khoản dự phòng lớn trên BCTC của `BVH` (*Dự phòng toán học `171.409,33 tỷ`*, *Dự phòng chia lãi `3.974,18 tỷ`*, *Dự phòng lãi cam kết tối thiểu `16.544,35 tỷ`*) tương ứng với những quyền lợi nào trong hợp đồng bảo hiểm nhân thọ cá nhân ở Bài `P4`?
2. Vì sao chi phí hoa hồng và khai thác năm đầu trên BCTC công ty bảo hiểm rất lớn lại khiến **Giá trị hoàn lại (`Surrender Value`)** của người mua bảo hiểm gần như bằng `0` nếu hủy hợp đồng trong 1–2 năm đầu?
3. Nếu một doanh nghiệp bảo hiểm tại Việt Nam mất khả năng thanh toán, cơ chế pháp lý nào và quỹ nào theo `Nghị định 46/2023/NĐ-CP` sẽ bảo vệ người mua bảo hiểm cá nhân?

<details>
<summary>Mở sau khi tự trả lời</summary>

1. *Dự phòng toán học* bảo đảm giá trị tài khoản/hoàn lại và quyền lợi tử vong/đáo hạn cơ bản; *Dự phòng chia lãi* trả bảo tức/lãi chia thêm cho hợp đồng truyền thống có tham gia chia lãi; *Dự phòng lãi cam kết tối thiểu* bù đắp sàn lãi suất cam kết của hợp đồng liên kết chung (`UL`) và hưu trí.
2. Công ty bảo hiểm trả hoa hồng đại lý năm đầu tới `30%–40%` phí (`Điều 51 VBHN 44/2026/VBHN-TT-BTC`) cộng chi phí thẩm định, phát hành nên khấu trừ **Phí ban đầu (`tối đa 50%` năm 1 với `UL`/`ILP` định kỳ theo `Điều 22 Khoản 3 VBHN 44`)** và **Phí hủy hợp đồng (`Surrender Charge`)** rất nặng những năm đầu.
3. Bộ Tài chính yêu cầu chuyển giao danh mục hợp đồng (`Điều 92, 110 Luật KDBH`) và trường hợp phá sản thì **Quỹ bảo vệ người được bảo hiểm** chi trả tối đa `90%` mức trách nhiệm nhưng không quá **`200 triệu đồng/người/hợp đồng`** theo `Điều 95 Nghị định 46/2023/NĐ-CP` (chi tiết tại **[Bài P4](P4-personal-insurance-contracts-and-costs.md)**).

</details>

---

## Ranh giới an toàn và điều tôi vẫn chưa hiểu

- **Ranh giới an toàn:** Bài giảng dùng BCTC `FY2025` của `BVH`, `PVI`, `BIC` làm học liệu phân tích kế toán và định lượng; không phải khuyến nghị mua, bán hay nắm giữ cổ phiếu `BVH`, `PVI`, `BIC`.
- **Điều tôi vẫn chưa hiểu (`CHƯA_BIẾT`):** Khi Bộ Tài chính ban hành thông tư quy định chi tiết hệ số rủi ro từng cấu phần để áp dụng bắt buộc mô hình `RBC` từ `01/01/2028` (`Khoản 2 Điều 157 Luật KDBH`), tỷ lệ `CAR` của từng doanh nghiệp sẽ thay đổi cụ thể ra sao so với tỷ lệ biên khả năng thanh toán (`Solvency I`) hiện hành?

---

## Nguồn Internet đã mở

| Nguồn pháp quy / Báo cáo tài chính sơ cấp | Kỳ báo cáo / Phiên bản / Phạm vi | Ngày truy cập | Nội dung đối chiếu trong bài |
|---|---|---|---|
| [Văn bản hợp nhất Luật Kinh doanh bảo hiểm `31/VBHN-VPQH` (`22/08/2025`)](https://vanban.chinhphu.vn/?pageid=27160&docid=215622) | Quốc hội; Luật KDBH `08/2022/QH15` | `2026-11-05` | Dự phòng (`Điều 97`), cấm kinh doanh BĐS từ dự phòng (`Điều 100`), vốn `RBC` từ `01/01/2028` (`Điều 94, 95, 108, 109, 157`) |
| [Nghị định `46/2023/NĐ-CP` (`01/07/2023`)](https://vanban.chinhphu.vn/?pageid=27160&docid=208265) | Chính phủ Việt Nam | `2026-11-05` | Tín nhiệm tái BH (`Điều 33`), vốn tối thiểu (`Điều 35`), dự phòng (`Điều 37–38`), trần đầu tư (`Điều 43`) |
| [Văn bản hợp nhất `44/2026/VBHN-TT-BTC` (`29/09/2026`)](https://vanban.chinhphu.vn/?pageid=27160&docid=217205) | Bộ Tài chính; hợp nhất `TT 67/2023` & `TT 96/2026` | `2026-11-05` | Trần giữ lại `10%` VCSH (`Điều 33`), tam giác `Chain-Ladder` `208.341 - 149.872 = 58.469` (`Điều 35–37`, tr. 42–45), dự phòng NT (`Điều 38–40`), Biên KNTT (`Mẫu 7-PNT`, tr. 137–138) |
| [BCTC hợp nhất kiểm toán `FY2025` — Tập đoàn Bảo Việt (`BVH`)](https://static2.vietstock.vn/data/HOSE/2025/BCTC/VN/NAM/BVH_Baocaotaichinh_2025_Kiemtoan_Hopnhat.pdf) | `31/12/2025`; `VAS`; EY Việt Nam (`31/03/2026`) | `2026-11-05` | CĐKT (tr. 6–9), KQKD (tr. 10–12), TM 14 Đầu tư (`266.535,57 tỷ`, tr. 48), TM 18 HH nhượng tái (`776,40 tỷ`, tr. 57), TM 24 Dự phòng (`201.682,49 tỷ`, tr. 61), TM 40 Biên KNTT (`141%` & `107%`, tr. 84) |
| [BCTC hợp nhất kiểm toán `FY2025` — PVI Holdings (`PVI`)](https://pvi.com.vn/) | `31/12/2025`; `VAS`; PwC Việt Nam (`15/02/2026`) | `2026-11-05` | CĐKT (tr. 5–6), KQKD (tr. 7), TM 5 Tài sản tái BH (`21.614,45 tỷ`, tr. 32), TM 18a Dự phòng (`28.417,50 tỷ`, tr. 42), TM 23–24 (tr. 46–47) |
| [BCTC hợp nhất Quý IV / cả năm `2025` — Bảo hiểm BIDV (`BIC`)](https://static2.vietstock.vn/data/HOSE/2025/BCTC/VN/QUY%204/BIC_Baocaotaichinh_Q4_2025_Hopnhat.pdf) | `31/12/2025`; `VAS`; ký `23/01/2026` | `2026-11-05` | CĐKT (tr. 3–6), KQKD Phần I & II cả năm 2025 (tr. 7–9), TM 5–12 (tr. 18–20) |
| [`learning/practice/models/insurance.py`](../practice/models/insurance.py) & [`geico_berkshire_fy2025_inputs.csv`](../practice/models/geico_berkshire_fy2025_inputs.csv) | Mô hình Python 3 của kho học tập | `2026-11-05` | Tam giác `Chain-Ladder`, cầu nối P&C, `vas_gross_vs_net_reserves()`, `solvency_margin_pnt()` và độ nhạy dự phòng |
