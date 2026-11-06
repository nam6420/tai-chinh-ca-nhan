# Bài 013 — Ngân hàng và bảo hiểm: hai mô hình bảng cân đối ngược cần đọc riêng

- Ngày: `2026-11-05`
- Chốt dữ liệu lúc: `2026-11-05 09:30 UTC+7 (Asia/Ho_Chi_Minh)`
- Bậc chiều sâu: `Bậc S — Bài giảng thực chiến (3 buổi học, 10 bài tập tính tay + mô hình Python)`
- Mục tiêu: Phân biệt bảng cân đối ngược của ngân hàng và bảo hiểm; tính đúng `NII`, `NIM`, `CIR`, `PPOP`, `CET1`, cầu nối `GWP` $\to$ `NWP` $\to$ `UPR` $\to$ `NEP`, `Loss Ratio`, `Expense Ratio`, `Combined Ratio`, `Insurance Float` và chi phí `Float`; hiểu cơ chế `CSM` theo `IFRS 17` và định giá bằng `Justified P/B` và `Residual Income Model (RIM)`.
- Bài trước liên quan: [N2](N2-statement-line-items.md), [005](005-debt-liquidity-survival.md), [007](007-notes-and-accounting-red-flags.md), [009](009-valuation-multiples.md), [010](010-cost-of-capital.md); dẫn tiếp sang [F4](F4-vietnam-bank-analysis.md), [F8](F8-vietnam-insurance-analysis.md) (bảo hiểm Việt Nam chuyên sâu) và [P4](P4-personal-insurance-contracts-and-costs.md) (đọc hợp đồng bảo hiểm cá nhân).
- Thời lượng: `3 buổi học` + thực hành [`practice/models/insurance.py`](../practice/models/insurance.py) và [`geico_berkshire_fy2025_inputs.csv`](../practice/models/geico_berkshire_fy2025_inputs.csv).
- Câu hỏi cốt lõi: **Vì sao tiền gửi ngân hàng và phí bảo hiểm thu trước không phải là doanh thu thuần kiểu cửa hàng bán lẻ, và vì sao định giá ngân hàng — bảo hiểm bằng `EV/EBITDA` hay `FCF` thông thường sẽ dẫn tới sai lầm nghiêm trọng?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

---

## Hiểu bài này trong 1 phút

Ở doanh nghiệp sản xuất hoặc bán lẻ thông thường, công ty bỏ tiền mua nguyên vật liệu, trả lương trước rồi mới thu tiền bán hàng; nợ vay là nguồn tài trợ bên ngoài, còn tiền mặt nằm yên trên bảng cân đối là tài sản tự do của cổ đông.

Ngược lại, **ngân hàng** và **công ty bảo hiểm** vận hành với **bảng cân đối ngược (`inverted balance sheet`)**:
1. **Ngân hàng** kinh doanh chính đồng tiền: nhận tiền gửi của dân cư và doanh nghiệp (nợ phải trả) để cho vay hoặc mua trái phiếu (tài sản sinh lời). Lãi thu về ghi nhận ngay hôm nay, nhưng rủi ro người vay vỡ nợ (`Credit Loss`) xuất hiện trễ sau 1–3 năm khi chu kỳ kinh tế đảo chiều.
2. **Công ty bảo hiểm** bán lời hứa bồi thường tương lai: khách hàng đóng phí ngay hôm nay, còn sự kiện tai nạn, cháy nổ hay tử vong xảy ra sau nhiều tháng hoặc nhiều chục năm. Toàn bộ khoản tiền thu trước nhưng chưa thực hiện xong nghĩa vụ tạo thành **nguồn vốn tạm giữ từ phí bảo hiểm (`Insurance Float`)** nằm bên phần **Nợ phải trả (`Technical Reserves` — dự phòng nghiệp vụ)**, không phải tiền tự do của cổ đông.

Vì nợ phải trả chính là "nguyên liệu sản xuất" của ngân hàng và bảo hiểm, mọi chỉ số tách nợ ra khỏi hoạt động kinh doanh như `EBITDA` (lợi nhuận trước lãi vay, thuế và khấu hao), `EV/EBITDA` (giá trị doanh nghiệp trên `EBITDA`), `ROIC` (tỷ suất sinh lời trên vốn đầu tư) hay `Free Cash Flow (FCF)` (dòng tiền tự do sau `CapEx`) đều vô nghĩa. Để phân tích và định giá hai nhóm ngành này, người học phải đi từ **chất lượng tài sản — đủ đầy dự phòng — an toàn vốn pháp định** rồi mới tới **tỷ suất sinh lời trên vốn chủ sở hữu (`ROE`)** và **mô hình thu nhập thặng dư (`Residual Income Model — RIM`)**.

---

## Ôn bài cũ và phạm vi bài học

- **Ôn bài cũ:** Bài [005](005-debt-liquidity-survival.md) cho thấy chênh lệch kỳ hạn giữa tài sản và nợ phải trả (`Asset-Liability Mismatch — ALM`) có thể gây mất thanh khoản dù báo cáo đang lãi. Bài [007](007-notes-and-accounting-red-flags.md) cho thấy ước tính kế toán nhạy cảm nhất ở ngân hàng là **chi phí dự phòng rủi ro tín dụng (`Provision for Credit Losses`)**, còn ở bảo hiểm là **dự phòng bồi thường cho tổn thất đã phát sinh nhưng chưa báo cáo (`IBNR — Incurred But Not Reported`)**.
- **Bài này làm gì:** Buổi 1 giải phẫu ngân hàng thương mại (`NII`, `NIM`, `CIR`, `PPOP`, `NPL`, `RWA`, `CET1`) qua `Form 10-K FY2025` của **JPMorgan Chase & Co.**; Buổi 2 giải phẫu bảo hiểm phi nhân thọ (`P&C`), cầu nối phí `GWP` $\to$ `NEP`, `Combined Ratio` và `Insurance Float` qua `Form 10-K FY2025` của **Berkshire Hathaway / GEICO**; Buổi 3 phân tích bảo hiểm nhân thọ theo `IFRS 17` (`CSM`) và định giá bằng `Justified P/B` & `RIM`.
- **Bài này chưa làm gì:** Chưa đi vào kế toán bảo hiểm Việt Nam (`Thông tư 232/2012/TT-BTC`), tam giác `Chain-Ladder` theo `VBHN 44/2026/VBHN-TT-BTC` và vốn `RBC` (học ở **[Bài F8](F8-vietnam-insurance-analysis.md)**); chưa bóc tách hợp đồng bảo hiểm cá nhân `UL`/`ILP` (học ở **[Bài P4](P4-personal-insurance-contracts-and-costs.md)**).

---

## Buổi 1 — Ngân hàng thương mại: Bảng cân đối ngược, `NII`, `PPOP`, chất lượng tín dụng và vốn `CET1`

### 1.1. Bốn tầng lọc trên báo cáo thu nhập ngân hàng

Một ngân hàng có `100 tỷ đồng` vốn tự có và huy động `900 tỷ đồng` tiền gửi (tổng tài sản `1.000 tỷ đồng`, đòn bẩy `Assets / Equity = 10x`) tạo ra lợi nhuận qua 4 tầng (hàm `bank_operating_bridge()` trong [`practice/models/insurance.py`](../practice/models/insurance.py)):

1. **Thu nhập lãi ròng (`Net Interest Income — NII`) và Biên lãi ròng (`Net Interest Margin — NIM`):**
   $$\text{NII} = \text{Interest Income (Thu nhập lãi)} - \text{Interest Expense (Chi phí lãi)}, \qquad \text{NIM} = \frac{\text{NII}}{\text{Average Earning Assets (Tài sản sinh lãi bình quân)}}$$
   `SỰ_THẬT` Theo tài liệu nghiên cứu *IFDP 1197* của Cục Dự trữ Liên bang Hoa Kỳ (Federal Reserve), `NIM` đo chênh lệch thu nhập lãi ròng trên mỗi đồng tài sản sinh lãi bình quân trước khi trừ chi phí vận hành và tổn thất tín dụng ([Federal Reserve IFDP 1197](https://www.federalreserve.gov/econresdata/ifdp/2017/files/ifdp1197.pdf)).
2. **Tổng thu nhập hoạt động (`Total Net Revenue / Total Operating Income — TOI`):** Cộng `NII` với **Thu nhập ngoài lãi (`Noninterest Revenue`)** từ phí thanh toán, quản lý tài sản, ngân hàng đầu tư, ngoại hối:
   $$\text{TOI} = \text{NII} + \text{Noninterest Revenue}$$
3. **Chi phí hoạt động (`Noninterest Expense — OPEX`), Tỷ lệ chi phí (`Cost-to-Income Ratio — CIR`) và Lợi nhuận trước dự phòng (`Pre-Provision Operating Profit — PPOP`):**
   $$\text{CIR} = \frac{\text{Noninterest Expense}}{\text{TOI}}, \qquad \text{PPOP} = \text{TOI} - \text{Noninterest Expense}$$
   `PPOP` là bộ đệm sinh lời cốt lõi hàng năm trước khi bù đắp nợ xấu.
4. **Chi phí dự phòng tín dụng (`Provision for Credit Losses`) và Lợi nhuận trước thuế (`EBT`):**
   $$\text{EBT} = \text{PPOP} - \text{Provision for Credit Losses}$$
   Một ngân hàng có `NIM` rất cao do cho vay tiêu dùng tín chấp nhưng nếu `Provision` ngốn mất `70%–80%` `PPOP` khi suy thoái thì lợi nhuận cổ đông vẫn sụp đổ.

### 1.2. Chất lượng tài sản (`NPL`, `LLR`, `NCO`), Khung vốn `Basel III` (`RWA`, `CET1`) và Rủi ro thanh khoản / lãi suất (`SVB`, `Credit Suisse`)

- **Đệm dự phòng nợ xấu:** Trên bảng cân đối, **Quỹ dự phòng rủi ro tín dụng tích lũy (`Allowance for Loan Losses — LLR` hoặc `Total Allowance for Credit Losses — ACL`)** dùng để hấp thụ các khoản xóa nợ ròng (`Net Charge-Offs — NCO`). Sức khỏe bộ đệm được đo bằng **Tỷ lệ bao phủ nợ xấu (`NPL Coverage Ratio`)**:
  $$\text{NPL Coverage} = \frac{\text{Allowance for Loan Losses (LLR)}}{\text{Nonperforming Loans / Assets (NPL / NPA)}}$$
- **Tài sản có trọng số rủi ro (`Risk-Weighted Assets — RWA`) và Vốn cấp 1 phổ thông (`Common Equity Tier 1 — CET1`):**
  Trái phiếu Chính phủ có trọng số rủi ro thấp hơn hẳn cho vay bất động sản hay thẻ tín dụng. Khung `Basel III` nhân từng tài sản và cam kết ngoại bảng với hệ số rủi ro để tính `RWA`. Lớp vốn chịu lỗ đầu tiên là `CET1` (vốn cổ phần phổ thông + lợi nhuận giữ lại trừ lợi thế thương mại `Goodwill` và tài sản vô hình):
  $$\text{CET1 Ratio} = \frac{\text{CET1 Capital}}{\text{Risk-Weighted Assets (RWA)}}$$
- **Bằng chứng phản biện — Vì sao `CET1` cao vẫn có thể sụp đổ chỉ sau 48 giờ (`SVB` và `Credit Suisse`, `03/2023`)?**
  `SUY_LUẬN` Tỷ lệ `CET1` chỉ đo khả năng chịu lỗ kế toán trên `RWA`, **không đo thanh khoản tức thời** và đôi khi bỏ sót khoản lỗ chưa thực hiện trên danh mục trái phiếu nắm giữ đến ngày đáo hạn (`Held-to-Maturity — HTM`). Tháng `03/2023`, **Silicon Valley Bank (`SVB`)** và **Credit Suisse** sụp đổ dù báo cáo tỷ lệ `CET1` cao hơn mức tối thiểu pháp định vì hai điểm mù: (1) **Rủi ro lãi suất trên sổ ngân hàng (`IRRBB`)**: khi Cục Dự trữ Liên bang (`Fed`) tăng lãi suất nhanh, danh mục trái phiếu dài hạn lãi suất cố định (`AFS` & `HTM`) mất giá hàng chục tỷ USD; và (2) **Rủi ro rút tiền gửi hàng loạt (`Bank Run`)**: tỷ trọng tiền gửi không được bảo hiểm cao rút ồ ạt buộc ngân hàng phải bán cắt lỗ trái phiếu, biến lỗ chưa thực hiện thành lỗ thật xóa sạch vốn chủ sở hữu. Do đó, đọc ngân hàng bắt buộc phải kiểm tra song hành **`CET1`**, **lỗ chưa thực hiện trên danh mục `AFS`/`HTM`** và **tỷ lệ bao phủ thanh khoản (`LCR` / `LDR`)**.

---

## Buổi 2 — Bảo hiểm phi nhân thọ (`P&C`): Cầu nối phí, `Combined Ratio` và `Insurance Float`

### 2.1. Cầu nối kế toán từ phí thu tiền (`GWP`) đến phí đã hưởng (`NEP`)

Khi khách hàng đóng `12 triệu đồng` phí bảo hiểm xe ô tô 1 năm vào ngày `01/07/2025`, đến `31/12/2025` công ty mới bảo vệ chiếc xe được `6 tháng` (`6 triệu đồng`), còn `6 triệu đồng` của 6 tháng đầu năm 2026 phải treo ở khoản nợ **Dự phòng phí chưa được hưởng (`Unearned Premium Reserve — UPR`)**. Cầu nối 4 bước (hàm `pc_underwriting_bridge()` trong [`practice/models/insurance.py`](../practice/models/insurance.py)):

1. **Phí bảo hiểm gốc (`Gross Written Premium — GWP`):** Tổng phí phát hành trong kỳ.
2. **Phí bảo hiểm giữ lại thuần (`Net Written Premium — NWP`):** Trừ phí nhượng tái bảo hiểm (`Ceded Premium`):
   $$\text{NWP} = \text{GWP} - \text{Ceded Premium}$$
3. **Thay đổi dự phòng phí chưa được hưởng (`\Delta UPR`):** $\Delta \text{UPR} = \text{UPR}_{\text{cuối kỳ}} - \text{UPR}_{\text{đầu kỳ}}$.
4. **Phí bảo hiểm thuần đã hưởng (`Net Earned Premium — NEP`):** Doanh thu thực sự của kỳ báo cáo:
   $$\text{NEP} = \text{NWP} - \Delta \text{UPR}$$

### 2.2. Bộ ba tỷ lệ khai thác (`Loss Ratio`, `Expense Ratio`, `Combined Ratio`)

`SỰ_THẬT` Theo Hiệp hội Quốc gia các Ủy viên Bảo hiểm Hoa Kỳ (`NAIC`), hiệu quả khai thác bảo hiểm phi nhân thọ được đo bằng 3 tỷ lệ ([NAIC Glossary](https://content.naic.org/glossary-insurance-terms)):
$$\text{Loss Ratio} = \frac{\text{Incurred Losses + LAE}}{\text{NEP}}, \qquad \text{Expense Ratio} = \frac{\text{Underwriting Expenses}}{\text{NEP (GAAP) hoặc NWP (SAP)}}$$
$$\text{Combined Ratio} = \text{Loss Ratio} + \text{Expense Ratio}$$
- $\text{Combined Ratio} < 100\%$: **Lãi khai thác (`Underwriting Profit`)** trước cả khi tính thu nhập đầu tư.
- $\text{Combined Ratio} > 100\%$: **Lỗ khai thác (`Underwriting Loss`)**.

### 2.3. Kinh tế học của `Insurance Float`, chi phí vốn âm và rủi ro đảo chiều chu kỳ (`GEICO FY2022`)

`SỰ_THẬT` Trong `Form 10-K FY2025` (trang `K-41`), Berkshire Hathaway định nghĩa `Float` là nguồn tiền giữ trước khi bồi thường, xấp xỉ tổng dự phòng bồi thường chưa trả (`Unpaid Losses & LAE`), dự phòng nhân thọ/niên kim, dự phòng phí chưa được hưởng (`UPR`) và nợ phải trả người được bảo hiểm trừ đi phí chờ thu và chi phí khai thác hoãn lại ([Berkshire FY2025 10-K](https://www.berkshirehathaway.com/2025ar/2025ar.pdf)). Chi phí của `Float`:
$$\text{Cost of Float} = \frac{-\text{Underwriting Profit}}{\text{Average Float (hoặc Ending Float)}}$$
Khi $\text{Combined Ratio} < 100\%$, doanh nghiệp vừa được cầm tiền `Float` đi đầu tư hưởng lãi, vừa có lãi khai thác — tức **`Cost of Float < 0%` (chi phí vốn âm)**. Tuy nhiên, `Float` **không phải lúc nào cũng miễn phí**:
- **Bằng chứng phản biện từ cú sốc lạm phát bồi thường (`GEICO FY2022`):** Năm `2022`, do giá xe cũ, phụ tùng thay thế và chi phí nhân công sửa chữa tại Hoa Kỳ tăng vọt nhanh hơn tốc độ xin tăng biểu phí, `GEICO` chịu **lỗ khai thác trước thuế `-1.880 triệu USD`** (`Combined Ratio = 104,8%`), khiến chi phí `Float` của riêng `GEICO` năm đó trở thành số dương đắt đỏ trước khi tái định giá phí thành công vào giai đoạn `2023–2025`.
- **Điều chỉnh dự phòng các năm trước (`Prior-Year Reserve Development`):** Bồi thường ghi nhận trên báo cáo lãi lỗ năm nay gồm cả tổn thất năm hiện hành (`Current Accident Year`) và điều chỉnh dự phòng của các năm tai nạn cũ. Nếu năm trước trích dư (`Favorable Development`), hoàn nhập dự phòng sẽ làm giảm `Loss Ratio` năm nay; ngược lại nếu trích thiếu (`Adverse Development`), công ty phải trích bù làm `Loss Ratio` vọt lên trên `100%`.

---

## Buổi 3 — Bảo hiểm nhân thọ (`IFRS 17` vs. `US GAAP LDTI` vs. `VAS`) và Khung định giá (`Justified P/B` & `RIM`)

### 3.1. Chuẩn mực `IFRS 17` (`CSM`) và sự khác biệt với `US GAAP (LDTI)` & `VAS`

Hợp đồng nhân thọ kéo dài `15–40 năm` nên không thể dùng `Combined Ratio` ngắn hạn. `SỰ_THẬT` Chuẩn mực quốc tế **`IFRS 17 — Insurance Contracts`** (hiệu lực từ `01/01/2023`) của `IFRS Foundation` đặt trọng tâm vào **Biên lợi nhuận dịch vụ hợp đồng (`Contractual Service Margin — CSM`)** ([IFRS 17 Standard Page](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-17-insurance-contracts/)):
1. **Cấm ghi nhận lãi ngày đầu (`No Day-One Gain`):** Lãi dự kiến khi phát hành hợp đồng mới phải khóa vào khoản nợ `CSM` và phân bổ dần vào lợi nhuận qua từng năm cung cấp dịch vụ (`CSM Release`).
2. **Phương trình vận động của `CSM` (hàm `ifrs17_csm_rollforward()` trong [`practice/models/insurance.py`](../practice/models/insurance.py)):**
   $$\text{CSM}_{\text{cuối}} = \text{CSM}_{\text{đầu}} + \text{CSM}_{\text{hợp đồng mới}} + \text{Lãi tích lũy (Interest Accretion)} \pm \text{Điều chỉnh dòng tiền tương lai} - \text{CSM Release}$$
3. **Bất đối xứng với hợp đồng chịu lỗ (`Onerous Contracts`):** Nếu giả định tương lai xấu đi làm `CSM` giảm về `0` mà vẫn còn lỗ, phần lỗ vượt quá (`Loss Component`) **phải ghi nhận lỗ ngay lập tức vào báo cáo lãi lỗ trong kỳ**.
4. **Ba mô hình đo lường trong `IFRS 17`:** `GMM` (mô hình chuẩn cho nhân thọ dài hạn), `VFA` (cho hợp đồng chia lãi trực tiếp / liên kết đầu tư `UL`/`ILP`), và `PAA` (cho hợp đồng ngắn hạn $\le 12$ tháng như phi nhân thọ `P&C`).
5. **Phân biệt 3 chế độ kế toán trên thế giới khi so sánh cổ phiếu bảo hiểm:**
   - **`IFRS 17` (Châu Âu, Anh, Canada, Úc, Hàn Quốc, Singapore, Hồng Kông...):** Tách riêng khoản nợ `CSM` trên bảng cân đối; thay đổi giả định phi tài chính được hấp thụ vào `CSM` trước khi chạm tới báo cáo lãi lỗ.
   - **`US GAAP — FASB ASU 2018-12 (`LDTI`)` (Hoa Kỳ — áp dụng cho các tập đoàn Mỹ như `Berkshire Hathaway`):** **Không có `CSM`**; lợi nhuận chưa hưởng nằm ẩn trong tỷ lệ phí thuần (`Net Premium Ratio — NPR` tối đa `100%`), mọi thay đổi giả định dòng tiền đi thẳng vào báo cáo lãi lỗ (`P&L`), còn biến động lãi suất chiết khấu đi vào thu nhập toàn diện khác (`OCI`).
   - **`VAS — Thông tư 232/2012/TT-BTC` (Việt Nam — `BVH`, `PVI`, `BIC`):** Chưa áp dụng `IFRS 17` (chưa tách `CSM`); phí nhân thọ thu về trích lập trực tiếp vào **Dự phòng toán học (`Mathematical Reserve`)** nằm trong chi phí kinh doanh bảo hiểm (sẽ giải phẫu ở **[Bài F8](F8-vietnam-insurance-analysis.md)**).

### 3.2. Định giá bằng `Justified P/B` và `Residual Income Model (RIM)` có điều chỉnh thiếu hụt dự phòng

1. **Hệ số `Justified P/B` tăng trưởng đều:** Với $\text{ROE}$ bền vững, chi phí vốn chủ sở hữu $r_e$ và tăng trưởng dài hạn $g < r_e$:
   $$\text{Justified } \frac{P}{B} = \frac{\text{ROE} - g}{r_e - g}$$
2. **Mô hình thu nhập thặng dư (`RIM`) khi phát hiện trích thiếu dự phòng trước thuế $\Delta R$ (thuế suất $t$):**
   Điều chỉnh giảm vốn chủ sở hữu đầu kỳ ngay lập tức theo hàm `reserve_understatement_adjustment()` trong [`practice/models/insurance.py`](../practice/models/insurance.py): $B_0^{\text{adj}} = B_0 - \Delta R(1 - t)$. Thu nhập thặng dư năm $k$ là $\text{RI}_k = (\text{ROE} - r_e) B_{k-1}^{\text{adj}}$, và giá trị ước tính theo mô hình là:
   $$V_0 = B_0^{\text{adj}} + \sum_{k=1}^{T} \frac{\text{RI}_k}{(1 + r_e)^k} + \frac{\text{RI}_{T+1}}{(r_e - g)(1 + r_e)^T}$$
3. **Ba điều kiện biên làm mô hình `Justified P/B` và `RIM` mất hiệu lực:**
   - **Ràng buộc vốn pháp định và rủi ro pha loãng (`Dilution Risk`):** Nếu tăng trưởng tài sản $g$ vượt quá tốc độ tích lũy vốn tự có khiến `CET1` (ngân hàng) hoặc `CAR` (bảo hiểm) thủng ngưỡng an toàn, doanh nghiệp buộc phải cắt cổ tức hoặc phát hành thêm cổ phiếu ở vùng `P/B < 1,0x`, làm pha loãng vĩnh viễn giá trị sổ sách trên mỗi cổ phiếu (`BVPS`).
   - **Ngoại suy `ROE` đỉnh chu kỳ vào vĩnh viễn:** Dùng `ROE` của năm tín dụng ấm áp (`Provision` cực thấp) hoặc năm không có siêu bão (`Catastrophe Loss = 0`) làm $\text{ROE}$ dài hạn sẽ thổi phồng giá trị cuối kỳ (`Terminal Value`). Phải dùng **`ROE` chuẩn hóa qua chu kỳ (`Normalized Across-the-Cycle ROE`)**.
   - **Lỗ ẩn vượt quá vốn chủ sở hữu:** Khi khoản thiếu hụt dự phòng $\Delta R(1-t)$ hoặc lỗ trái phiếu `HTM` lớn đến mức xóa gần hết $B_0$, cổ phiếu chuyển sang trạng thái quyền chọn mua kiệt giá (`Distressed Equity`) và không thể định giá bằng `RIM` tuyến tính.

---

## Ví dụ từ nguồn thật

Số liệu dưới đây trích từ `Form 10-K FY2025` của **JPMorgan Chase & Co.** và **Berkshire Hathaway Inc.** (kỳ kết thúc `31/12/2025`, `US GAAP`, đơn vị: `triệu USD`), nạp sẵn trong [`geico_berkshire_fy2025_inputs.csv`](../practice/models/geico_berkshire_fy2025_inputs.csv).

### Bảng 1 — Giải phẫu Ngân hàng: JPMorgan Chase & Co. (`FY2024` vs. `FY2025`)

`SỰ_THẬT` Nguồn: [JPMorgan Chase FY2025 Form 10-K](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2025/4th-quarter/corp-10k-2025.pdf) (trang `44`, `47`, `59`, `61`, `94`, `111`, `165` và `167`, đơn vị: `triệu USD`):

| Chỉ tiêu tài chính & an toàn vốn | `FY2024` | `FY2025` | Công thức / Ý nghĩa (`PHÉP_TÍNH` & `SUY_LUẬN`) |
|---|---:|---:|---|
| 1. Thu nhập lãi ròng (`NII` — Reported `GAAP`, tr. 47 & 165) | `$92.583` | `$95.443` | Tăng `+3,09%`; chiếm `52,31%` `TOI`. Theo cơ sở `Managed FTE` (tr. 59): `$95.868M`, `NIM = 2,54%` |
| 2. Thu nhập ngoài lãi (`Noninterest Revenue`, tr. 47 & 165) | `$84.973` | `$87.004` | Phí ngân hàng đầu tư, quản lý tài sản, thị trường, thẻ và dịch vụ thanh toán |
| 3. Tổng doanh thu thuần (`Total Net Revenue — TOI`) | `$177.556` | `$182.447` | `PHÉP_TÍNH`: `95.443 + 87.004 = 182.447 triệu USD` |
| 4. Chi phí hoạt động (`Noninterest Expense`, tr. 47 & 165) | `$91.797` | `$95.640` | `CIR (Overhead Ratio)` = `95.640 / 182.447 = 52,42%` (báo cáo `52%`) |
| 5. Lợi nhuận trước dự phòng (`PPOP`) | `$85.759` | `$86.807` | `PHÉP_TÍNH`: `182.447 - 95.640 = 86.807 triệu USD` |
| 6. Chi phí dự phòng tín dụng (`Provision`, tr. 47 & 165) | `$10.678` | `$14.212` | Tăng `+33,10%`, tiêu thụ `16,37%` `PPOP` (`14.212 / 86.807`) |
| 7. Lợi nhuận trước thuế (`EBT`) & Lợi nhuận ròng (tr. 165) | `$75.081` / `$58.471` | `$72.595` / `$57.048` | `72.595 = 86.807 - 14.212`; Thuế TNDN = `$15.547M`; `ROE = 17%`, `ROTCE = 20%` |
| 8. Tổng tài sản / Cho vay / Tiền gửi cuối kỳ (tr. 47 & 167) | `$4.002.814` | `$4.424.900` | Cho vay `$1.493.429M`; Tiền gửi `$2.559.320M` (`Loans-to-Deposits = 58%`) |
| 9. Dự phòng rủi ro cho vay (`LLR`) / Tổng `ACL` / `NPA` | `$24.345` / `$26.866` | `$25.765` / `$31.230` | `LLR` nội bảng `$25.765M` (tr. 167); Tổng `ACL` `$31.230M` (tr. 44); `NPA = $10.359M` (tr. 111) |
| 10. Vốn `CET1` (`CET1 Capital`, tr. 94) | `$275.502` | `$288.469` | Thấp hơn Vốn CP phổ thông (`$342.393M`, tr. 61) do trừ `Goodwill` & tài sản vô hình |
| 11. `RWA` và `CET1 Ratio` — Standardized (tr. 94) | `15,7%` | `$1.981.692` (`14,6%`) | `PHÉP_TÍNH`: `288.469 / 1.981.692 = 14,5567%` (báo cáo `14,6%`) |
| 12. `RWA` và `CET1 Ratio` — Advanced (tr. 94) | `15,8%` | `$2.045.249` (`14,1%`) | `PHÉP_TÍNH`: `288.469 / 2.045.249 = 14,1043%` (báo cáo `14,1%`) |

### Bảng 2 — Giải phẫu Bảo hiểm P&C và `Float`: GEICO & Berkshire Hathaway (`FY2023–FY2025`)

`SỰ_THẬT` Nguồn: [Berkshire Hathaway Inc. FY2025 Form 10-K](https://www.berkshirehathaway.com/2025ar/2025ar.pdf) (trang `K-35`, `K-36`, `K-40`, `K-41`, đơn vị: `triệu USD`):

| Chỉ tiêu khai thác & đầu tư bảo hiểm | `FY2023` | `FY2024` | `FY2025` | Công thức kiểm chứng (`PHÉP_TÍNH`) |
|---|---:|---:|---:|---|
| **A. GEICO (Bảo hiểm xe cơ giới Hoa Kỳ)** | | | | |
| 1. Phí phát hành (`Premiums Written`) | `$39.837` | `$42.916` | `$45.193` | Tăng `+5,31%` năm 2025 |
| 2. Phí đã hưởng (`Premiums Earned — NEP`) | `$39.264` | `$42.252` | `$44.481` | Chênh `45.193 - 44.481 = 712 triệu USD` tăng dự phòng `UPR` ròng |
| 3. Bồi thường & giải quyết (`Losses & LAE`) | `$31.814` | `$30.331` | `$32.144` | `Loss Ratio 2025` = `32.144 / 44.481 = 72,2646%` (báo cáo `72,3%`) |
| 4. Chi phí khai thác (`Underwriting Expenses`) | `$3.815` | `$4.108` | `$5.513` | `Expense Ratio 2025` = `5.513 / 44.481 = 12,3941%` (báo cáo `12,4%`) |
| 5. Tổng bồi thường & chi phí | `$35.629` | `$34.439` | `$37.657` | `Combined Ratio 2025` = `37.657 / 44.481 = 84,6586%` (báo cáo `84,7%`) |
| 6. Lãi khai thác trước thuế (`Pre-tax UW Gain`) | `$3.635` | `$7.813` | `$6.824` | `44.481 - 37.657 = 6.824 triệu USD` (`UW Margin = +15,34%`) |
| **B. Hợp nhất Bảo hiểm Berkshire Hathaway** | | | | |
| 7. Lãi khai thác hợp nhất trước / sau thuế | `$6.913` / `$5.428` | `$11.405` / `$9.020` | `$9.460` / `$7.258` | `GEICO ($6.824M) + BH Primary ($785M) + BHRG ($1.851M) = $9.460M` |
| 8. Thu nhập đầu tư bảo hiểm trước / sau thuế | `$11.610` / `$9.567` | `$16.748` / `$13.670` | `$15.261` / `$12.513` | Năm 2025: Lãi trái phiếu/tín phiếu `$10.175M` + Cổ tức `$5.086M` |
| 9. Nguồn vốn `Insurance Float` cuối năm | `$169.000` | `$171.000` | `$176.000` | Xấp xỉ `176 tỷ USD` tại `31/12/2025` |
| 10. Chi phí `Float` trước thuế trên `Float` bình quân | `-4,15%` | `-6,71%` | `-5,45%` | Năm 2025: `-9.460 / ((171.000 + 176.000)/2) = -5,4524%` |

---

## Bài tập

Tự giải trước khi mở Đáp án; kiểm tra lại bằng `python3 learning/practice/models/insurance.py`.

1. **(`NII`, `NIM`, `CIR`, `PPOP`, `EBT`):** Ngân hàng có thu nhập lãi `18.500 tỷ đồng`, chi phí lãi `10.100 tỷ`, thu nhập ngoài lãi `3.600 tỷ`, `OPEX = 4.800 tỷ`, `Provision = 3.200 tỷ`, tài sản sinh lãi bình quân `200.000 tỷ`. Tính `NII`, `NIM`, `TOI`, `CIR`, `PPOP` và `EBT`.
2. **(`RWA` và `CET1` của JPMorgan `FY2025`):** Với `CET1 = 288.469 triệu USD`, `Total Assets = 4.424.900 triệu USD`, `RWA Standardized = 1.981.692 triệu USD` và `RWA Advanced = 2.045.249 triệu USD`, hãy tính: (a) `CET1 Ratio` theo hai phương pháp; (b) `CET1 / Total Assets`; và giải thích vì sao không được thay `RWA` bằng `Total Assets`.
3. **(Độ nhạy bộ đệm tín dụng):** Cuối năm `2025`, JPMorgan có dự phòng rủi ro cho vay nội bảng (`Allowance for loan losses`, trang 167) là `25.765 triệu USD` và tài sản không sinh lời (`NPA`, trang 111) là `10.359 triệu USD`. Nếu `NPA` tăng gấp đôi lên `20.718 triệu USD` và ngân hàng muốn giữ tỷ lệ bao phủ `Allowance for loan losses / NPA = 150%`, ngân hàng cần trích thêm bao nhiêu triệu USD dự phòng và chiếm bao nhiêu phần trăm `PPOP` năm `2025` (`86.807 triệu USD`)?
4. **(Cầu nối `GWP` $\to$ `NEP`):** Công ty bảo hiểm P&C có `GWP = 5.200 tỷ đồng`, nhượng tái bảo hiểm `1.200 tỷ`, `UPR` đầu năm `1.650 tỷ` và cuối năm `1.950 tỷ`. Tính `Retention Ratio`, `NWP`, `\Delta UPR` và `NEP`.
5. **(Chỉ số khai thác GEICO `FY2025`):** Từ `Premiums Written = 45.193 triệu USD`, `NEP = 44.481 triệu USD`, `Losses & LAE = 32.144 triệu USD`, `Underwriting Expenses = 5.513 triệu USD`, hãy tính: (a) `Loss Ratio`, `Expense Ratio`, `Combined Ratio` theo mẫu số `NEP`; (b) Lãi khai thác trước thuế; (c) `Expense Ratio` và `Combined Ratio` nếu chia chi phí khai thác cho `Premiums Written` theo chuẩn `SAP (NAIC)`.
6. **(Chu kỳ khai thác GEICO `2023–2025`):** So sánh năm `2023` (`NEP = 39.264`, `Losses & LAE = 31.814`, `UW Expenses = 3.815`) với năm `2025`. Tính mức thay đổi điểm phần trăm của `Loss Ratio`, `Expense Ratio`, `Combined Ratio` từ `2023` sang `2025` và giải thích vì sao lãi khai thác năm `2025` thấp hơn năm `2024` (`7.813 triệu USD`).
7. **(Kinh tế học của `Float` tại Berkshire `FY2025`):** Với lãi khai thác hợp nhất trước thuế `9.460 triệu USD`, thu nhập đầu tư trước thuế `15.261 triệu USD`, `Float` đầu năm `171.000 triệu USD` và cuối năm `176.000 triệu USD`, hãy tính: (a) `Float` bình quân; (b) `Cost of Float` trên `Float` bình quân và cuối kỳ; (c) Tổng tỷ suất sinh lời trước thuế (khai thác + đầu tư) trên `Float` bình quân.
8. **(`CSM` và `Onerous Contracts` theo `IFRS 17`):** Công ty nhân thọ có `CSM` đầu năm `8.000 tỷ đồng`, hợp đồng mới cộng thêm `1.500 tỷ`, lãi tích lũy `400 tỷ`. Cuối năm, giả định chi trả tương lai xấu đi làm tăng nghĩa vụ `900 tỷ` ở nhóm hợp đồng A (đang có `CSM` lớn) và tăng `350 tỷ` ở nhóm hợp đồng B (chỉ còn `100 tỷ` `CSM`). Tỷ lệ phân bổ `CSM Release` trong năm là `10%`. Tính: (a) Khoản lỗ ghi nhận ngay (`Loss Component`) của nhóm B; (b) `CSM` trước và sau phân bổ; (c) Ảnh hưởng ròng của `CSM Release` và `Loss Component` lên lợi nhuận trước thuế.
9. **(`Justified P/B`):** Ngân hàng có `BVPS = 30.000 đồng`, $r_e = 12,5\%$, $g = 5,5\%$. Tính `Justified P/B` và giá trị ước tính theo mô hình mỗi cổ phiếu dưới bộ giả định đã cho khi: (a) $\text{ROE} = 16,0\%$; (b) $\text{ROE} = 11,0\%$.
10. **(`Residual Income Model` có điều chỉnh thiếu hụt dự phòng):** Công ty bảo hiểm có vốn chủ sở hữu báo cáo $B_0 = 10.000\text{ tỷ đồng}$, $\text{ROE} = 15,0\%$, tỷ lệ chi trả cổ tức `40%`, $r_e = 12,0\%$, $g = 5,0\%$ sau năm 5, nhưng trích thiếu dự phòng `IBNR` `1.500 tỷ đồng` trước thuế (thuế suất `20%`). Tính: (a) $B_0^{\text{adj}}$; (b) Giá trị ước tính theo mô hình $V_0^{\text{adj}}$ và hệ số `P/B` ước tính trên $B_0$; (c) Mức định giá sai nếu bỏ qua khoản thiếu hụt dự phòng.

---

## Đáp án

<details>
<summary>Mở sau khi đã tự giải cả 10 bài tập</summary>

1. **`PHÉP_TÍNH`:** `NII` $= 18.500 - 10.100 = 8.400\text{ tỷ}$; `NIM` $= 8.400 / 200.000 = 4,20\%$; `TOI` $= 8.400 + 3.600 = 12.000\text{ tỷ}$; `CIR` $= 4.800 / 12.000 = 40,00\%$; `PPOP` $= 12.000 - 4.800 = 7.200\text{ tỷ}$; `EBT` $= 7.200 - 3.200 = 4.000\text{ tỷ đồng}$.
2. **`PHÉP_TÍNH` & `SUY_LUẬN`:** (a) Standardized: $288.469 / 1.981.692 = 14,56\%$ (`10-K`: `14,6%`); Advanced: $288.469 / 2.045.249 = 14,10\%$ (`10-K`: `14,1%`). (b) `CET1 / Total Assets` $= 288.469 / 4.424.900 = 6,52\%$. Không thay `RWA` bằng `Total Assets` vì `Total Assets` không phân biệt trọng số rủi ro giữa trái phiếu Chính phủ và khoản vay rủi ro cao, đồng thời bỏ sót cam kết ngoại bảng.
3. **`PHÉP_TÍNH`:** Dự phòng mục tiêu $= 20.718 \times 150\% = 31.077\text{ triệu USD}$. Cần trích thêm $= 31.077 - 25.765 = 5.312\text{ triệu USD}$, chỉ chiếm $5.312 / 86.807 = 6,12\%$ `PPOP` năm `2025` (nếu tính trên tổng quỹ dự phòng rủi ro tín dụng `ACL = 31.230 triệu USD` gồm cả cam kết ngoại bảng tại trang 44 thì bộ đệm hiện có đã vượt mức `31.077 triệu USD`).
4. **`PHÉP_TÍNH`:** `NWP` $= 5.200 - 1.200 = 4.000\text{ tỷ}$; `Retention Ratio` $= 4.000 / 5.200 = 76,92\%$; $\Delta \text{UPR} = 1.950 - 1.650 = +300\text{ tỷ}$; `NEP` $= 4.000 - 300 = 3.700\text{ tỷ đồng}$.
5. **`PHÉP_TÍNH`:** (a) Trên `NEP = 44.481`: `Loss Ratio` $= 32.144 / 44.481 = 72,26\%$ (`10-K`: `72,3%`); `Expense Ratio (GAAP)` $= 5.513 / 44.481 = 12,39\%$ (`10-K`: `12,4%`); `Combined Ratio (GAAP)` $= 37.657 / 44.481 = 84,66\%$ (`10-K`: `84,7%`). (b) Lãi khai thác $= 44.481 - 37.657 = 6.824\text{ triệu USD}$. (c) Theo `SAP` chia chi phí cho `NWP = 45.193`: `Expense Ratio (SAP)` $= 5.513 / 45.193 = 12,20\% \implies \text{Combined Ratio (SAP)} = 72,26\% + 12,20\% = 84,46\%$.
6. **`PHÉP_TÍNH` & `SUY_LUẬN`:** Năm `2023`: `Loss Ratio` $= 81,03\%$, `Expense Ratio` $= 9,72\%$, `Combined Ratio` $= 90,74\%$. Từ `2023` sang `2025`: `Loss Ratio` giảm `-8,76 điểm %`, `Expense Ratio` tăng `+2,68 điểm %`, `Combined Ratio` cải thiện `-6,08 điểm %`. So với năm `2024` (`Combined Ratio = 81,51%`), năm `2025` GEICO tăng chi phí quảng cáo/khai thác thêm `1.405 triệu USD` (`+34,2%`) để mở rộng thị phần nên lãi khai thác giảm từ `7.813` xuống `6.824 triệu USD`.
7. **`PHÉP_TÍNH`:** (a) `Average Float` $= (171.000 + 176.000)/2 = 173.500\text{ triệu USD}$. (b) `Cost of Float` trên `Float` bình quân $= -9.460 / 173.500 = -5,45\%$; trên `Float` cuối kỳ $= -9.460 / 176.000 = -5,38\%$. (c) Tổng sinh lời trước thuế trên `Float` bình quân $= (9.460 + 15.261) / 173.500 = 24.721 / 173.500 = 14,25\%/\text{năm}$.
8. **`PHÉP_TÍNH`:** (a) Nhóm B dùng hết `100 tỷ` `CSM` và phải ghi nhận lỗ ngay `Loss Component` $= 350 - 100 = 250\text{ tỷ đồng}$. (b) `CSM` trước phân bổ $= 8.000 + 1.500 + 400 - 900 - 100 = 8.900\text{ tỷ}$; `CSM Release` (`10%`) $= 890\text{ tỷ}$; `CSM` cuối kỳ $= 8.900 - 890 = 8.010\text{ tỷ đồng}$. (c) Ảnh hưởng ròng lên `EBT` $= +890 - 250 = +640\text{ tỷ đồng}$.
9. **`PHÉP_TÍNH`:** (a) $\text{ROE} = 16\%$: $\text{Justified } P/B = (0,16 - 0,055)/(0,125 - 0,055) = 1,50\times \implies P_0 = 45.000\text{ đồng}$. (b) $\text{ROE} = 11\%$: $\text{Justified } P/B = (0,11 - 0,055)/0,07 = 0,7857\times \implies P_0 = 23.571\text{ đồng}$ (giảm `-47,6%`).
10. **`PHÉP_TÍNH`:** (a) Chạy `reserve_understatement_adjustment()`: thiếu hụt sau thuế $= 1.500 \times (1 - 0,20) = 1.200\text{ tỷ} \implies B_0^{\text{adj}} = 10.000 - 1.200 = 8.800\text{ tỷ đồng}$. (b) Tăng trưởng vốn 5 năm đầu $= 15\% \times 60\% = 9,0\%/\text{năm}$; chiết khấu 5 năm theo công thức `RIM` cho $PV(\text{RI}_{1..5}) = 1.117,11\text{ tỷ}$, $PV(\text{Terminal RI}) = 3.171,84\text{ tỷ} \implies V_0^{\text{adj}} = 8.800 + 1.117,11 + 3.171,84 = 13.088,95\text{ tỷ đồng}$ (`P/B` ước tính trên $B_0$ báo cáo $= 1,31\times$). (c) Nếu không điều chỉnh dự phòng, $V_0^{\text{unadj}} = 14.873,81\text{ tỷ đồng}$ (`P/B = 1,49x`), tức ước tính cao hơn thực tế `1.784,86 tỷ đồng`.

</details>

---

## Bài làm với dữ liệu thiếu hoặc lệch

**Đề bài:** Slide giới thiệu của Công ty bảo hiểm P&C `A` viết: *"Combined Ratio năm 2025 đạt `96,0%` (tốt hơn Công ty B `97,5%`)"*. Mở thuyết minh kiểm toán của `A`, bạn thấy: `NWP = 1.250 triệu USD`, `NEP = 1.000 triệu USD`, `Incurred Losses & LAE = 710 triệu USD`, `Underwriting Expenses = 312,5 triệu USD`. Trong khi đó, Công ty `B` có `NWP = 1.020`, `NEP = 1.000`, `Losses & LAE = 705`, `Underwriting Expenses = 270` và tính cả hai tỷ lệ trên mẫu số `NEP = 1.000`. Đồng thời, một bản tin tóm tắt chỉ nêu *"JPMorgan có CET1 `14,6%`"* mà bỏ qua bảng vốn trang 91 của `Form 10-K`. Hãy làm sạch dữ liệu và kết luận.

<details>
<summary>Xem cách làm sạch dữ liệu và kết luận chuẩn</summary>

1. **`PHÉP_TÍNH` (Chuẩn hóa mẫu số `Combined Ratio` giữa `A` và `B`):** Công ty `A` đã ghép `Loss Ratio` chia cho `NEP` (`710 / 1.000 = 71,0%`) với `Expense Ratio` chia cho `NWP` đang tăng nóng (`312,5 / 1.250 = 25,0%`) để ra `96,0%`. Đặt về cùng mẫu số `NEP = 1.000 triệu USD` theo báo cáo lãi lỗ `GAAP`, tổng chi phí của `A` là $710 + 312,5 = 1.022,5\text{ triệu USD} \implies$ **`Combined Ratio (GAAP)` của `A` là `102,25%`** (lỗ khai thác `-22,5 triệu USD`), kém xa Công ty `B` (`97,5%`, lãi khai thác `+25,0 triệu USD`). Ngay cả khi quy đổi Công ty `B` sang chuẩn `SAP` (`705/1.000 + 270/1.020 = 96,97%`), vẫn phải báo cáo rõ cả hai cơ sở `GAAP` và `SAP`, không được lấy số `SAP` của công ty tăng trưởng phí nóng so với số `GAAP` của công ty ổn định.
2. **`SUY_LUẬN` (Nguyên tắc chọn tỷ lệ `CET1` ràng buộc):** JPMorgan công bố hai tỷ lệ `CET1`: `Standardized = 14,6%` và `Advanced = 14,1%`. Theo quy định sàn vốn Collins (`Collins Floor`), người phân tích phải dùng mức thấp hơn (`14,1%`) làm biên an toàn vốn ràng buộc.

</details>

---

## Sai ở đâu

**Nhận định sai lầm:** *"Công ty Bảo hiểm X có vốn hóa `15.000 tỷ đồng` nhưng giữ `45.000 tỷ đồng` tiền mặt và tiền gửi trên bảng cân đối — tức `EV = -30.000 tỷ đồng`, mua cổ phiếu được tặng không `30.000 tỷ` tiền mặt! Còn Ngân hàng Y vừa nâng `NIM` từ `3,5%` lên `5,8%` nhờ cho vay tiêu dùng tín chấp và `NPL` cuối năm chỉ `1,2%`, chắc chắn lợi nhuận tăng vọt không rủi ro."*

<details>
<summary>Mở sau khi tự tìm lỗi</summary>

1. **Đánh đồng `Insurance Float` với tiền mặt tự do của cổ đông:** `45.000 tỷ đồng` tiền gửi của Bảo hiểm X là tài sản đối ứng với **Dự phòng nghiệp vụ (`Technical Reserves`)** bên phần Nợ phải trả để chi trả cho khách hàng trong tương lai, không được phép rút ra chia cho cổ đông.
2. **Nhìn `NIM` mà bỏ qua chi phí dự phòng tín dụng (`Provision`):** Đẩy `NIM` lên `5,8%` bằng cho vay tín chấp đi kèm chi phí rủi ro tín dụng `4%–8%/năm` trên dư nợ; khi kinh tế suy thoái `Provision` có thể xóa sạch `PPOP`.
3. **Ảo ảnh mẫu số của `NPL` khi tín dụng tăng nóng (`Seasoning Effect`):** Khoản vay mới giải ngân làm mẫu số (Tổng dư nợ) phình to ngay, trong khi cần 90–180 ngày để khoản vay xấu lộ diện ở tử số (`NPL`). Phải kiểm tra nợ xấu theo thế hệ giải ngân (`Vintage Analysis`) hoặc chia `NPL` cho dư nợ 1–2 năm trước.

</details>

---

## Kiểm tra chuyển bài

1. Khi đọc báo cáo hợp nhất của Tập đoàn Bảo Việt (`BVH` — có cả nhân thọ và phi nhân thọ), vì sao không được dùng một con số `Combined Ratio` gộp chung toàn tập đoàn?
2. Nếu một công ty bảo hiểm phi nhân thọ muốn báo lãi trước thuế cao hơn thực tế `200 tỷ đồng` mà không bán thêm hợp đồng mới, ban điều hành có thể can thiệp vào khoản mục nào trên bảng cân đối?
3. Dưới chuẩn `IFRS 17`, hợp đồng liên kết đầu tư (`UL`/`ILP`) tạo ra `CSM` cho công ty bảo hiểm từ những khoản phí nào trừ vào tài khoản của người mua bảo hiểm ở Bài `P4`?

<details>
<summary>Mở sau khi tự trả lời</summary>

1. Mảng phi nhân thọ ghi nhận phí ngắn hạn 1 năm theo `UPR` và đo bằng `Combined Ratio`; mảng nhân thọ kéo dài nhiều thập kỷ, phần lớn phí thu về phải trích vào dự phòng toán học và dùng lãi đầu tư tài chính để trả quyền lợi dài hạn nên `Combined Ratio` không có ý nghĩa cho nhân thọ.
2. Ban điều hành có thể ước tính thấp **Dự phòng bồi thường cho tổn thất đã phát sinh nhưng chưa thông báo (`IBNR`)** hoặc giảm hệ số phát triển đuôi trong tam giác `Chain-Ladder` (sẽ kiểm toán chi tiết ở **[Bài F8](F8-vietnam-insurance-analysis.md)**).
3. Từ 6 lớp phí: phí ban đầu (`50%–75%` năm đầu), phí bảo hiểm rủi ro (`COI`), phí quản lý hợp đồng, phí quản lý quỹ hàng năm và phí hủy hợp đồng trước hạn (sẽ tính từng đồng ở **[Bài P4](P4-personal-insurance-contracts-and-costs.md)**).

</details>

---

## Ranh giới an toàn và điều tôi vẫn chưa hiểu

- **Ranh giới an toàn:** Bài giảng phục vụ mục đích học tập và nghiên cứu dựa trên bằng chứng sơ cấp; không phải khuyến nghị mua, bán hay nắm giữ cổ phiếu `JPM`, `BRK.A/BRK.B` hay bất kỳ định chế tài chính nào.
- **Điều tôi vẫn chưa hiểu (`CHƯA_BIẾT`):** Lộ trình áp dụng `IFRS 17` tại Việt Nam sau giai đoạn chuẩn bị sẽ làm thay đổi số dư vốn chủ sở hữu và `CSM` của các doanh nghiệp bảo hiểm nhân thọ trong nước ở mức độ nào?

---

## Nguồn Internet đã mở

| Nguồn sơ cấp / chuẩn mực | Kỳ báo cáo / Phiên bản / Phạm vi | Ngày truy cập | Nội dung đối chiếu trong bài |
|---|---|---|---|
| [JPMorgan Chase & Co. — FY2025 Form 10-K](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2025/4th-quarter/corp-10k-2025.pdf) | Kỳ kết thúc `31/12/2025`; Hoa Kỳ; `US GAAP`; đơn vị `triệu USD` | `2026-11-05` | Bảng KQKD, bảng cân đối (trang 44, 47, 59, 61, 111, 165, 167) và bảng vốn `CET1`/`RWA` Standardized & Advanced (trang 94) |
| [Berkshire Hathaway Inc. — FY2025 Form 10-K](https://www.berkshirehathaway.com/2025ar/2025ar.pdf) | Kỳ kết thúc `31/12/2025`; Hoa Kỳ; `US GAAP`; đơn vị `triệu USD` | `2026-11-05` | Kết quả khai thác GEICO (trang `K-36`), hợp nhất bảo hiểm (trang `K-35`), đầu tư (`K-40`) và `Insurance Float` (`K-41`) |
| [Federal Reserve — IFDP 1197](https://www.federalreserve.gov/econresdata/ifdp/2017/files/ifdp1197.pdf) | Xuất bản `02/2017`; Cục Dự trữ Liên bang Hoa Kỳ | `2026-11-05` | Định nghĩa chuẩn của `Net Interest Margin (NIM)` |
| [NAIC — Glossary of Insurance Terms](https://content.naic.org/glossary-insurance-terms) | Hiệp hội Quốc gia các Ủy viên Bảo hiểm Hoa Kỳ (`NAIC`) | `2026-11-05` | Định nghĩa `Loss Ratio`, `Expense Ratio`, `Combined Ratio`, `NEP` và `UPR` |
| [IFRS Foundation — IFRS 17 Insurance Contracts](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-17-insurance-contracts/) | Chuẩn mực quốc tế `IFRS 17` (hiệu lực `01/01/2023`) | `2026-11-05` | Cơ chế `CSM`, `GMM`, `VFA`, `PAA` và hợp đồng chịu lỗ (`Onerous Contracts`) |
| [`learning/practice/models/insurance.py`](../practice/models/insurance.py) & [`geico_berkshire_fy2025_inputs.csv`](../practice/models/geico_berkshire_fy2025_inputs.csv) | Mô hình Python 3 của kho học tập | `2026-11-05` | Tái lập toàn bộ phép tính cầu nối phí, `Combined Ratio`, `Cost of Float` và định giá `RIM` |
