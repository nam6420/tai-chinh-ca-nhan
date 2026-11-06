# Bài 003: Chất lượng doanh nghiệp — lợi thế cạnh tranh, ROIC và khả năng tái đầu tư

- Ngày: `2026-11-06`
- Chốt dữ liệu lúc: `2026-11-06 10:40 UTC+7 (Asia/Ho_Chi_Minh)`
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Mục tiêu: Hiểu vì sao lợi nhuận cao một năm chưa chứng minh doanh nghiệp chất lượng; nắm 5 nguồn **lợi thế cạnh tranh bền vững (`Economic Moat`)** và bằng chứng định lượng kiểm chứng; tính từng bước **Lợi nhuận hoạt động sau thuế (`NOPAT`)**, **Vốn đầu tư (`Invested Capital — IC`)** theo hai góc nhìn (Tài sản và Nguồn vốn) và **Tỷ suất lợi nhuận trên vốn đầu tư (`ROIC`)**; phân rã `ROIC` thành biên lợi nhuận × vòng quay vốn, hiểu phương trình tăng trưởng `g = Tỷ lệ tái đầu tư × ROIC`, và nhận diện cờ đỏ quản trị (`pha loãng`, `giao dịch bên liên quan`, `goodwill`).
- Thời lượng: Ba phiên học + thực hành với [valuation.py](../practice/models/valuation.py).
- Bài trước liên quan: Thứ tự đọc 9/23 của Nhánh 1 — học ngay sau [Bài N4: Giá trị thời gian của tiền và lợi suất](N4-time-value-returns.md) (kế thừa [Bài 002](002-finding-a-cheap-stock.md), [Bài N2](N2-statement-line-items.md) và [Bài 001](001-business-financial-statements.md)). Học tiếp: [Bài 004: Dòng tiền và chất lượng lợi nhuận](004-cash-flow-and-earnings-quality.md).
- Câu hỏi cốt lõi: **Điều gì giúp một doanh nghiệp tạo ra tỷ suất sinh lời trên vốn (`ROIC`) cao hơn chi phí vốn suốt nhiều năm mà không bị đối thủ cạnh tranh san phẳng?**

> Đây là bài học nền tảng toàn cầu, không phải khuyến nghị mua, bán hay nắm giữ chứng khoán. Các ví dụ số học về Quán cà phê Sao Biển và các công ty A, B, C là hư cấu; phần ví dụ thực tế dùng số liệu kiểm toán từ `Form 10-K FY2025` của Apple Inc.

---

## Hiểu bài này trong 1 phút

`SUY_LUẬN` Ở [Bài 002](002-finding-a-cheap-stock.md), bạn đã biết không mua cổ phiếu chỉ vì thị giá thấp hay `P/E` thấp. Bài 003 giải quyết ngộ nhận tiếp theo: **thấy doanh nghiệp năm nay báo lãi lớn liền nghĩ đó là một doanh nghiệp tuyệt vời.**

Hình dung một quán ăn: bán đắt hàng trong một ngày lễ chưa đủ để kết luận quán làm ăn giỏi quanh năm. Cần xem qua nhiều mùa: khách có tự nguyện quay lại không, tăng giá nhẹ khách có bỏ đi không, và nếu mở thêm chi nhánh thứ hai thì tiền vốn bỏ ra có sinh lời cao như quán đầu tiên không.

Trong kinh doanh, khi một ngành có lợi nhuận cao, đối thủ mới sẽ nhảy vào mở xưởng, giảm giá và giành khách, kéo lợi nhuận cả ngành về mức bình thường.
- `SỰ_THẬT` Nghiên cứu của **McKinsey** trên khoảng `7.000` công ty phi tài chính niêm yết tại Mỹ (`1963–2004`) cho thấy tỷ suất lợi nhuận trên vốn đầu tư (`ROIC`, loại trừ `goodwill`) ở mức trung vị chỉ quanh **`10%/năm`**, xấp xỉ chi phí vốn dài hạn — nghĩa là công ty "trung bình" chỉ kiếm vừa đủ trả chi phí vốn.
- Chỉ những doanh nghiệp sở hữu **lợi thế cạnh tranh bền vững (`Economic Moat` — hào nước bảo vệ lâu đài)** mới duy trì được `ROIC` vượt chi phí vốn qua nhiều chu kỳ.

> Câu cần nhớ: **Đừng hỏi "năm nay công ty lãi bao nhiêu tỷ?"; hãy hỏi "mỗi 100 đồng vốn bỏ vào bộ máy kinh doanh sinh ra bao nhiêu đồng lợi nhuận (`ROIC`), con số đó có bền vững qua nhiều năm không, và hào nước nào ngăn đối thủ vào chia phần?"**

---

## Ôn bài cũ hoặc kiểm tra đầu vào

Hãy nối liền kiến thức từ 3 bài trước trong Nhánh 1:
1. **Từ [Bài N4: Giá trị thời gian của tiền và lợi suất](N4-time-value-returns.md):** Bạn đã biết sức mạnh của lãi kép $\text{FV} = \text{PV} \times (1 + r)^n$. Một doanh nghiệp chất lượng cao chính là một **"cỗ máy lãi kép nội tại"**: mỗi năm tạo ra lợi nhuận và tái đầu tư mở rộng ở tỷ suất sinh lời trên vốn (`ROIC`) cao, giúp giá trị doanh nghiệp tăng trưởng kép.
2. **Từ [Bài 002: Hiểu và tìm một cổ phiếu đang được định giá rẻ](002-finding-a-cheap-stock.md):** Bạn đã học 3 câu hỏi theo thứ tự (*Kiếm tiền bằng cách nào? → Doanh nghiệp có khỏe và chất lượng không? → Giá có rẻ không?*). Bài 003 cung cấp thước đo định lượng cho câu hỏi số 2.
3. **Từ [Bài N2: Đọc từng dòng ba báo cáo tài chính](N2-statement-line-items.md):** Nhớ lại số liệu cuối năm của **Quán cà phê Sao Biển** (dùng ở mục 2 bên dưới):
   - **Báo cáo kết quả kinh doanh:** Doanh thu thuần `= 1.200 triệu đồng`, Lợi nhuận hoạt động (`EBIT`) `= 150 triệu đồng`, Thuế suất `= 20%`, Lợi nhuận ròng (`Net Income`) `= 100 triệu đồng`.
   - **Bảng cân đối kế toán:** Tiền mặt `= 185 triệu`, Phải thu `= 40 triệu`, Tồn kho `= 35 triệu`, Tài sản cố định ròng `= 470 triệu` (**Tổng tài sản `= 730 triệu`**); Phải trả người bán `= 30 triệu` (không chịu lãi), Nợ vay ngân hàng `= 200 triệu`, Vốn chủ sở hữu `= 500 triệu`.

---

## 1. Lợi thế cạnh tranh bền vững (`Economic Moat`) là gì?

Thuật ngữ **Economic Moat** (hào nước kinh tế) mô tả những rào cản cấu trúc giúp doanh nghiệp bảo vệ thị phần và tỷ suất lợi nhuận trước đối thủ cạnh tranh.

`SỰ_THẬT` Theo tài liệu của **VanEck** mô tả phương pháp luận của **Morningstar**, có **5 nguồn tạo ra lợi thế cạnh tranh (`Five Sources of Moat`)**:

| Nguồn lợi thế cạnh tranh (`Moat`) | Trực giác đời thường | Ví dụ điển hình |
|---|---|---|
| **1. Tài sản vô hình (`Intangible Assets`)** | Thương hiệu mạnh khiến khách trả giá cao hơn, hoặc bằng sáng chế / giấy phép cấm đối thủ sao chép. | Starbucks, Eli Lilly |
| **2. Chi phí chuyển đổi (`Switching Costs`)** | Đổi sang đối thủ tốn nhiều thời gian đào tạo lại, chi phí tích hợp hoặc rủi ro đứt gãy vận hành. | Salesforce, Stryker |
| **3. Hiệu ứng mạng lưới (`Network Effect`)** | Càng nhiều người dùng, mạng lưới càng giá trị đối với người dùng mới. | Visa, Google |
| **4. Lợi thế chi phí (`Cost Advantage`)** | Nhờ quy mô, quy trình hoặc nguồn nguyên liệu rẻ, sản xuất với chi phí thấp hơn hẳn đối thủ. | Walmart, AB InBev |
| **5. Quy mô hiệu quả (`Efficient Scale`)** | Thị trường ngách chỉ đủ chỗ cho 1–2 doanh nghiệp có lãi; người thứ ba vào sẽ khiến cả ngành cùng lỗ. | Union Pacific, Dominion Energy |

### Lợi thế cạnh tranh phải được chứng minh bằng con số, không bằng lời tự khen

Báo cáo thường niên nào cũng viết *"Chúng tôi dẫn đầu thị trường"*. Đó chỉ là `Ý_KIẾN` của doanh nghiệp. Một `Moat` thật phải để lại **4 dấu vết định lượng lặp lại qua nhiều năm**:
1. **Biên lợi nhuận gộp và biên `EBIT`** cao hơn hẳn trung vị ngành và ổn định kể cả trong năm khó khăn.
2. **Quyền định giá (`Pricing Power`):** Tăng giá bán bù lạm phát mà sản lượng không giảm.
3. **Tỷ lệ giữ chân khách hàng (`Retention Rate`) cao kéo dài** và thị phần ổn định.
4. **Tỷ suất lợi nhuận trên vốn đầu tư (`ROIC`) cao hơn Chi phí vốn (`WACC`)** liên tục qua nhiều chu kỳ.

---

## 2. Giải phẫu từng bước `NOPAT`, `Vốn đầu tư (Invested Capital)` và `ROIC`

### 1. Vì sao cần `ROIC` bên cạnh `ROE` và `ROA`?

Ở [Bài N2](N2-statement-line-items.md), bạn đã biết `ROE = Lợi nhuận ròng / Vốn chủ sở hữu` và `ROA = Lợi nhuận ròng / Tổng tài sản`. Tuy nhiên:
- `ROE` bị khuếch đại mạnh bởi **đòn bẩy nợ vay** (hoặc mua lại cổ phiếu quỹ làm mỏng vốn chủ).
- `ROA` lại lệch pha giữa tử số và mẫu số: tử số (`Lợi nhuận ròng`) đã trừ lãi vay, còn mẫu số (`Tổng tài sản`) chứa cả tiền mặt nhàn rỗi và nợ phải trả người bán không tốn lãi. `SỰ_THẬT` **Damodaran (NYU Stern)** cảnh báo không dùng `ROA` để so với chi phí vốn (`WACC`).

Để đo chính xác **100 đồng vốn thực sự cắm vào bộ máy kinh doanh tạo ra bao nhiêu đồng lợi nhuận sau thuế cho cả chủ nợ lẫn cổ đông**, ta dùng **Tỷ suất lợi nhuận trên vốn đầu tư (`Return on Invested Capital — ROIC`)**.

### 2. Công thức chuẩn và 3 bước tính trên Quán cà phê Sao Biển

`SỰ_THẬT` Theo tài liệu của **Damodaran (NYU Stern)**, công thức chuẩn của `ROIC` là:

$$\text{ROIC} = \frac{\text{Lợi nhuận hoạt động sau thuế (NOPAT)}}{\text{Giá trị sổ sách của Vốn đầu tư (Invested Capital — IC)}}$$

Hãy tính từng bước cho **Quán cà phê Sao Biển**:

#### Bước 1: Tính tử số `NOPAT` (`Net Operating Profit After Tax` — Lợi nhuận hoạt động sau thuế)
Toàn bộ lợi nhuận hoạt động `EBIT = 150 triệu đồng` sau khi trừ thuế thu nhập doanh nghiệp (`thuế suất = 20%`) sẽ còn lại:
$$\text{NOPAT} = \text{EBIT} \times (1 - \text{Thuế suất}) = 150 \times (1 - 0,20) = 120 \text{ triệu đồng}$$
*(Lưu ý: Luôn nhân `EBIT` với `(1 − Thuế suất)` chứ không lấy thuế thực nộp trên báo cáo lãi lỗ, vì thuế thực nộp đã chứa lá chắn thuế của lãi vay — lấy sai sẽ tính trùng lợi ích thuế).*

#### Bước 2: Tính mẫu số `Vốn đầu tư (Invested Capital — IC)` bằng cả 2 cách đối chứng
Trong tổng tài sản `730 triệu đồng` của Quán Sao Biển, có `185 triệu` tiền mặt nằm trong két sắt và `30 triệu` được nhà cung cấp cho mua chịu miễn phí. Vậy **vốn thực sự mà chủ nợ và cổ đông đã bỏ vào vận hành quán** là bao nhiêu? Hai cách tính dưới đây luôn khớp nhau 100%:

- `PHÉP_TÍNH` **Cách 1 — Nhìn từ Nguồn vốn tài trợ (`Financing Approach`):**
  $$\text{Vốn đầu tư (IC)} = \text{Tổng nợ vay chịu lãi} + \text{Vốn chủ sở hữu} - \text{Tiền và tương đương tiền}$$
  $$\text{IC}_{\text{Sao Biển}} = 200 \text{ (Nợ vay)} + 500 \text{ (Vốn chủ)} - 185 \text{ (Tiền mặt)} = 515 \text{ triệu đồng}$$

- `PHÉP_TÍNH` **Cách 2 — Nhìn từ Tài sản vận hành (`Operating Asset Approach`):**
  Lấy Tài sản cố định ròng cộng Vốn lưu động phi tiền mặt (`Phải thu + Tồn kho − Nợ ngắn hạn không chịu lãi`):
  $$\text{Vốn lưu động phi tiền mặt} = (40 + 35) - 30 = 45 \text{ triệu đồng}$$
  $$\text{IC}_{\text{Sao Biển}} = 470 \text{ (Tài sản cố định ròng)} + 45 \text{ (Vốn lưu động phi tiền mặt)} = 515 \text{ triệu đồng}$$

Nhờ phương trình kế toán `Tài sản = Nợ phải trả + Vốn chủ sở hữu`, cả hai cách đều ra chính xác **`515 triệu đồng`**!

#### Bước 3: Chia `NOPAT` cho `Vốn đầu tư (IC)` để ra `ROIC`
Theo Damodaran, chuẩn nhất là dùng **Vốn đầu tư đầu kỳ** (hoặc bình quân đầu kỳ và cuối kỳ, miễn là nhất quán):
- `PHÉP_TÍNH` Trên vốn đầu tư cuối kỳ (`515 triệu`): $\text{ROIC} = \frac{120}{515} \approx 23,30\%/\text{năm}$. Trên vốn đầu tư đầu kỳ (`500 triệu`): $\text{ROIC} = \frac{120}{500} = 24,00\%/\text{năm}$.
- *(Cảnh báo: Không áp công thức `ROIC` này cho **ngân hàng và bảo hiểm** vì tiền gửi khách hàng là nguyên liệu kinh doanh — học riêng ở [Bài 013](013-banks-insurers.md)).*

---

## 3. So sánh `ROIC` với Chi phí vốn (`WACC`): Tạo hay phá hủy giá trị?

Ta so sánh `ROIC` với **Chi phí vốn (`Cost of Capital / WACC`)** — mức sinh lời tối thiểu mà chủ nợ và cổ đông đòi hỏi (học cách ước tính ở [Bài 010](010-cost-of-capital.md)). `SỰ_THẬT` Theo **Damodaran** và **McKinsey**, thước đo tạo giá trị cốt lõi là **Lợi suất vượt trội (`Excess Return = ROIC − WACC`)**:
- **Khi `ROIC > WACC`:** Mỗi đồng vốn mới tạo ra nhiều hơn chi phí huy động nó $\implies$ **Tăng trưởng tạo thêm giá trị.**
- **Khi `ROIC < WACC`:** Mỗi đồng vốn mới sinh ra ít hơn chi phí của nó $\implies$ **Càng mở rộng nhanh càng phá hủy giá trị**, dù lợi nhuận kế toán vẫn dương!
- `SỰ_THẬT` **McKinsey** (`Balancing ROIC and growth to build value`, 2006) chỉ ra: công ty có `ROIC > 20%` có khoảng `50%` xác suất duy trì mức đó sau 10 năm; còn công ty tăng trưởng nóng (`> 20%/năm`) có tới `56%` xác suất tụt xuống `< 5%/năm` sau một thập kỷ và chỉ `13%` giữ được đà tăng trưởng.

---

## 4. Tái đầu tư, Tăng trưởng (`g = Reinvestment Rate × ROIC`) và Phân rã DuPont

### 1. Phương trình nối giữa Tái đầu tư và Tăng trưởng lợi nhuận

`SỰ_THẬT` Theo **Damodaran**, khi `ROIC` ổn định, tốc độ tăng trưởng lợi nhuận hoạt động (`g`) bằng:

$$\text{Tốc độ tăng trưởng (g)} \approx \text{Tỷ lệ tái đầu tư} \times \text{ROIC} \implies \text{Tỷ lệ tái đầu tư cần thiết} = \frac{g}{\text{ROIC}}$$

với $\text{Tỷ lệ tái đầu tư} = \frac{(\text{CapEx} - \text{Khấu hao}) + \Delta\text{Vốn lưu động phi tiền mặt}}{\text{NOPAT}}$.

`KỊCH_BẢN` & `PHÉP_TÍNH` So sánh **Công ty A** và **Công ty B** cùng có doanh thu `1.000`, cùng muốn tăng trưởng **`g = 6%/năm`** (giả sử `WACC = 10%/năm`):

| Chỉ tiêu (1 năm) | Công ty A (Có Moat mạnh) | Công ty B (Không có Moat) |
|---|---:|---:|
| Doanh thu thuần / `NOPAT` / `IC` đầu kỳ | `1.000` / `150` / `500` | `1.000` / `60` / `1.200` |
| **`ROIC = NOPAT / IC`** | **`150 / 500 = 30,0%`** | **`60 / 1.200 = 5,0%`** |
| Tỷ lệ tái đầu tư cần thiết để tăng `g = 6%/năm` (`= g / ROIC`) | **`6% / 30% = 20%` NOPAT** (`= 30`) | **`6% / 5% = 120%` NOPAT** (`= 72`) |
| Dòng tiền tự do (`FCFF = NOPAT − Tái đầu tư`) còn lại | **`150 − 30 = +120`** (Dư tiền chia cổ tức!) | **`60 − 72 = −12`** (Thiếu tiền, phải vay thêm!) |

`SUY_LUẬN` Cùng tăng trưởng `6%/năm`, Công ty A (`ROIC = 30%`) chỉ cần giữ lại `20%` lợi nhuận và dư `120` tiền mặt tự do; còn Công ty B (`ROIC = 5%`) tiêu hết `100%` lợi nhuận vẫn thiếu `12`, phải vay nợ hoặc phát hành thêm cổ phiếu!

### 2. Phân rã `ROIC` theo trực giác DuPont: Biên lợi nhuận × Vòng quay vốn

`PHÉP_TÍNH` Nhân cả tử và mẫu của `ROIC` với `Doanh thu thuần`:

$$\text{ROIC} = \underbrace{\left(\frac{\text{NOPAT}}{\text{Doanh thu thuần}}\right)}_{\text{Biên NOPAT}} \times \underbrace{\left(\frac{\text{Doanh thu thuần}}{\text{Vốn đầu tư (IC)}}\right)}_{\text{Vòng quay vốn đầu tư}}$$

Công ty A đạt `15% × 2,0 vòng = 30%`; Công ty B chỉ đạt `6% × 0,83 vòng ≈ 5%`. Có hai con đường tạo `ROIC` cao: bán với **biên lợi nhuận dày** (thương hiệu, bằng sáng chế) hoặc **quay vòng vốn cực nhanh** (bán lẻ hiệu quả cao).

---

## 5. Phân biệt `Moat` thật với Đỉnh chu kỳ & Ba cờ đỏ quản trị

### 1. Vì sao lợi nhuận 1 năm ở đỉnh chu kỳ đánh lừa cả `P/E` lẫn `ROIC`?

`KỊCH_BẢN` & `PHÉP_TÍNH` **Công ty C** (ngành chu kỳ) có `50 triệu cổ phiếu`, giá `24` (Vốn hóa `= 1.200`). Chuỗi lợi nhuận 5 năm: **`20`, `25`, `22`, `100`, `30`** (năm thứ 4 vọt lên `100` do giá hàng hóa tăng đột biến):
- Nhìn đúng năm đỉnh (`100`): $\text{P/E} = \frac{1.200}{100} = 12,0 \text{ lần}$ (trông rẻ).
- Dùng **trung vị (`median`) 5 năm** (`25`): $\text{P/E} = \frac{1.200}{25} = 48,0 \text{ lần}$ (thực chất rất đắt!).
- Dùng **bình quân 5 năm** (`39,4`): $\text{P/E} = \frac{1.200}{39,4} \approx 30,5 \text{ lần}$; bỏ năm đỉnh (`97/4 = 24,25`) thì $\text{P/E} \approx 49,5 \text{ lần}$.

### 2. Ba cờ đỏ quản trị làm xói mòn chất lượng doanh nghiệp

1. **Pha loãng cổ phiếu (`Dilution`):** `SỰ_THẬT` Theo *Investor Bulletin: Investing in an IPO* của **SEC (`Investor.gov`)**, hồ sơ chào bán phải thuyết minh mục *Dilution* và rủi ro cấu trúc cổ phiếu hai lớp (`dual-class`). Phát hành ESOP/cổ phiếu giá rẻ liên tục làm EPS tăng chậm hơn lợi nhuận.
2. **Giao dịch bên liên quan (`Related-Party Transactions`):** `SỰ_THẬT` Theo **IAS 24 (IFRS Foundation)**, doanh nghiệp phải thuyết minh bản chất và giá trị giao dịch với bên liên quan (cá nhân/tổ chức kiểm soát, quản lý chủ chốt và gia đình) dù có tính giá hay không, để cổ đông kiểm tra nguy cơ rút ruột lợi nhuận.
3. **Thâu tóm (`M&A`) giá đắt tạo `Goodwill` lớn:** `SỰ_THẬT` Theo **IFRS 3 (IFRS Foundation)**, `Goodwill` là phần giá mua vượt giá trị hợp lý của tài sản thuần xác định được. Mua đắt làm phình mẫu số `IC` (gộp `Goodwill`) và kéo `ROIC` đi xuống.

---

## Ví dụ từ nguồn thật: Giải phẫu hiệu quả vốn của Apple Inc. (`Form 10-K FY2025`)

`SỰ_THẬT` Kiểm tra trên dữ liệu từ **[Apple Inc. — Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm)** (kết thúc `27/09/2025`, đơn vị: triệu USD) trong tệp [apple_fy2025_inputs.csv](../practice/models/apple_fy2025_inputs.csv) và mô hình [valuation.py](../practice/models/valuation.py):
- **Kết quả kinh doanh (`FY2025`):** Doanh thu thuần `= 416.161`; Lợi nhuận hoạt động (`EBIT`) `= 133.050`; Lợi nhuận trước thuế `= 132.729`; Thuế TNDN `= 20.719`; Lợi nhuận ròng `= 112.010`.
- **Bảng cân đối (`27/09/2025`):** Tiền mặt `= 35.934`; Chứng khoán khả mại `= 18.763 + 77.723 = 96.486` (Tổng thanh khoản `= 132.420`); Phải thu `= 39.777`; Tồn kho `= 5.718`; Phải trả người bán `= 69.860`; Tổng nợ vay `= 7.979 + 12.350 + 78.328 = 98.657`; Vốn chủ sở hữu `= 73.733`.

`PHÉP_TÍNH` Từng bước tính toán:
1. **Thuế suất hiệu dụng và `NOPAT`:**
   $$\text{Thuế suất hiệu dụng} = \frac{20.719}{132.729} \approx 15,610\% \implies \text{NOPAT} = 133.050 \times (1 - 0,15610) \approx 112.281 \text{ triệu USD (Biên NOPAT } \approx 26,98\%)$$
2. **Vốn lưu động thương mại và `ROIC`:**
   - Phải thu + Tồn kho (`45.495`) nhỏ hơn Phải trả người bán (`69.860`), tạo ra **vốn lưu động thương mại âm** (`−24.365 triệu USD`).
   - Nếu tính `IC` khi chỉ trừ `Cash` (`35.934`): $\text{IC} = 98.657 + 73.733 - 35.934 = 136.456 \text{ triệu USD} \implies \text{ROIC} = \frac{112.281}{136.456} \approx 82,28\%/\text{năm}$ (còn nếu trừ cả chứng khoán khả mại thì `IC = 39.970 triệu USD`, `ROIC > 280%`).
   - Hàm `residual_income()` trong [valuation.py](../practice/models/valuation.py) minh họa trực tiếp cách một doanh nghiệp có `ROE` / `ROIC` vượt xa chi phí vốn tạo ra thu nhập thặng dư lớn trên mỗi đồng vốn sổ sách.

---

## Bài tập

`KỊCH_BẢN` Tự giải từng bước 10 bài tập dưới đây trước khi mở Đáp án (Bài 9–10 dùng dữ liệu thật từ [apple_fy2025_inputs.csv](../practice/models/apple_fy2025_inputs.csv) và [valuation.py](../practice/models/valuation.py)):

1. **Tính `ROIC` nhiều năm:** Công ty T có chuỗi `NOPAT` và `IC đầu kỳ` qua 4 năm: Năm 1 (`80` / `800`); Năm 2 (`100` / `900`); Năm 3 (`108` / `1.200`); Năm 4 (`110` / `1.500`). Tính `ROIC` từng năm, nhận xét xu hướng và nêu 2 giả thuyết cần kiểm tra.
2. **Tuyên bố so với Bằng chứng `Moat`:** Phân loại 5 câu sau là **tuyên bố** hay **bằng chứng** và nêu dữ liệu cần kiểm tra: (a) *"Thương hiệu được yêu thích nhất ngành"*; (b) *"Tỷ lệ gia hạn hợp đồng đạt 95% trong 5 năm liên tiếp"*; (c) *"Hệ sinh thái không có đối thủ"*; (d) *"Biên gộp duy trì 45%–48% suốt 10 năm so với trung vị ngành 22%–25%"*; (e) *"Đổi nhà cung cấp tốn 6 tháng tích hợp lại hệ thống"*.
3. **Phân biệt `Moat` với Đỉnh chu kỳ:** Công ty V sản xuất hóa chất cơ bản có lợi nhuận tăng từ `40` lên `160` trong 1 năm nhờ giá hóa chất thế giới tăng `+60%` do đứt gãy nguồn cung. Đặt giả thuyết và nêu dữ liệu kiểm tra để phân biệt `Moat` với đỉnh chu kỳ.
4. **Tính `NOPAT`, `IC` theo 2 cách và `ROIC`:** Doanh nghiệp K có Doanh thu `= 2.000`, `EBIT = 250`, thuế suất `= 20%`. Đầu kỳ có: Tiền mặt `= 100`, Phải thu `= 150`, Tồn kho `= 200`, TSCĐ ròng `= 650` (Tổng tài sản `= 1.100`); Phải trả người bán (không chịu lãi) `= 100`, Vay ngân hàng `= 300`, Vốn chủ `= 700`. Tính `NOPAT`, `IC` theo 2 cách và `ROIC`.
5. **Phân rã DuPont của `ROIC`:** Chuỗi bán lẻ X và Thương hiệu Y cùng đạt `ROIC = 24%/năm`. Biết X có biên `NOPAT = 4%`, Y có biên `NOPAT = 16%`. Tính vòng quay vốn đầu tư của X và Y.
6. **Tỷ lệ tái đầu tư và `FCFF`:** Công ty M (`ROIC = 20%`) và N (`ROIC = 10%`) cùng có `NOPAT = 200 tỷ đồng` và cùng muốn tăng trưởng `g = 8%/năm`. Tính tỷ lệ tái đầu tư, số tiền tái đầu tư và `FCFF = NOPAT − Tái đầu tư` của M và N.
7. **Lợi nhuận kinh tế (`Economic Profit`):** Công ty A (`NOPAT = 150`, `IC = 500`, `ROIC = 30%`) và Công ty B (`NOPAT = 60`, `IC = 1.200`, `ROIC = 5%`), giả sử `WACC = 10%`. Tính `Economic Profit = NOPAT − IC × WACC` của A và B.
8. **Ảnh hưởng của `Goodwill` lên `ROIC`:** Tập đoàn G có `NOPAT = 180 tỷ`, tổng `IC = 1.800 tỷ` (trong đó `Goodwill` từ M&A là `1.000 tỷ`, tài sản hữu hình & vốn lưu động là `800 tỷ`). Tính `ROIC` gộp `Goodwill` và loại trừ `Goodwill`, giải thích ý nghĩa từng số.
9. **Dữ liệu thật Apple (`FY2025`):** Từ [apple_fy2025_inputs.csv](../practice/models/apple_fy2025_inputs.csv), mảng `Products` có doanh thu `307.003`, giá vốn `194.116`; mảng `Services` có doanh thu `109.158`, giá vốn `26.844` (triệu USD). Tính biên lợi nhuận gộp từng mảng và liên hệ với nguồn `Moat`.
10. **Thực hành `residual_income()` trong [valuation.py](../practice/models/valuation.py):** Với `B0 = 100`, `ke = 10%`, `payout = 50%`, `ROE = 20%` trong 2 năm đầu rồi hội tụ về `ke`, hãy tính `NI`, `RI = NI − ke × B` của Năm 1, Năm 2 và tổng giá trị `value = B0 + PV(RI)`.

---

## Đáp án

1. `PHÉP_TÍNH` Năm 1: `10,0%`; Năm 2: `11,1%`; Năm 3: `9,0%`; Năm 4: `7,3%`. `SUY_LUẬN` `NOPAT` tăng nhưng `ROIC` giảm vì vốn phình nhanh hơn lãi; cần kiểm tra `Goodwill` từ M&A, tiến độ nhà máy mới hoặc biên lợi nhuận bị ép.
2. `SUY_LUẬN` Câu (a), (c) là **tuyên bố**; câu (b), (d) là **bằng chứng định lượng**; câu (e) là **bán bằng chứng** (cần kiểm tra tỷ lệ rời bỏ thực tế).
3. `SUY_LUẬN` Kiểm tra chuỗi giá bán/biên lợi nhuận 5–10 năm qua cả năm đáy chu kỳ và dòng tiền `CFO` ([Bài 004](004-cash-flow-and-earnings-quality.md)); nếu giá hàng hóa hạ nhiệt mà lợi nhuận rơi về `40` thì đó là đỉnh chu kỳ.
4. `PHÉP_TÍNH` (a) $\text{NOPAT} = 250 \times 0,8 = 200 \text{ tỷ}$; (b) Nguồn vốn: $\text{IC} = 300 + 700 - 100 = 900 \text{ tỷ}$; Tài sản: $\text{IC} = 650 + (150 + 200 - 100) = 900 \text{ tỷ}$; (c) $\text{ROIC} = 200 / 900 \approx 22,22\%$.
5. `PHÉP_TÍNH` Vòng quay vốn của X $= 24\% / 4\% = 6,0 \text{ vòng/năm}$ (chi phí thấp, quay vòng nhanh); của Y $= 24\% / 16\% = 1,5 \text{ vòng/năm}$ (thương hiệu biên dày).
6. `PHÉP_TÍNH` M: tái đầu tư $8\% / 20\% = 40\%$ (`80 tỷ`) $\implies \text{FCFF}_M = 120 \text{ tỷ}$. N: tái đầu tư $8\% / 10\% = 80\%$ (`160 tỷ`) $\implies \text{FCFF}_N = 40 \text{ tỷ}$.
7. `PHÉP_TÍNH` Công ty A: $150 - 500 \times 10\% = +100$ (tạo giá trị). Công ty B: $60 - 1.200 \times 10\% = -60$ (phá hủy giá trị dù lãi kế toán dương).
8. `PHÉP_TÍNH` Gộp `Goodwill`: $180 / 1.800 = 10,0\%$ (đánh giá trách nhiệm M&A của ban lãnh đạo); Loại `Goodwill`: $180 / 800 = 22,5\%$ (đánh giá hiệu quả bộ máy vận hành hiện hữu).
9. `PHÉP_TÍNH` Biên gộp `Products` $= (307.003 - 194.116) / 307.003 \approx 36,77\%$; Biên gộp `Services` $= (109.158 - 26.844) / 109.158 \approx 75,41\%$ (cao gấp đôi nhờ chi phí chuyển đổi và hiệu ứng mạng lưới hệ sinh thái iOS).
10. `PHÉP_TÍNH` Năm 1: $\text{NI}_1 = 20, \text{RI}_1 = 20 - 10 = 10, B_1 = 110$. Năm 2: $\text{NI}_2 = 22, \text{RI}_2 = 22 - 11 = 11$. $\text{PV(RI)} = 10/1,1 + 11/1,21 = 18,1818 \implies \text{value} = 118,18$.

---

## Bài làm với dữ liệu thiếu hoặc lệch

Khi tính `ROIC` thực tế, bạn thường gặp 2 tình huống lệch dữ liệu:
1. **Các trang web hiển thị `ROIC` rất khác nhau cho cùng một công ty** do khác quy ước trừ tiền mặt (`Cash` so với `Marketable securities`) hoặc dùng vốn đầu kỳ/cuối kỳ.
2. **Vốn đầu tư (`IC`) âm hoặc sát `0`** ở các công ty phần mềm/dịch vụ giữ nhiều tiền mặt và thu tiền khách trả trước lớn.

**Quy trình xử lý chuẩn:**
- **Bước 1:** Luôn tự tính từ báo cáo gốc và ghi rõ quy ước tử số (`NOPAT`) cùng mẫu số (`IC` đầu kỳ hay bình quân, có gồm `Goodwill` không).
- **Bước 2:** Khi `IC ≤ 0` do tiền mặt và chiếm dụng vốn lớn, không chia máy móc ra `ROIC` âm mà đánh giá qua **Biên `NOPAT`** và **Tỷ lệ `FCF / Doanh thu`** ([Bài 004](004-cash-flow-and-earnings-quality.md)).

---

## Sai ở đâu

### Sai lầm 1: Đem `ROA` so sánh trực tiếp với `WACC`
- **Sai ở đâu:** Mẫu số `Tổng tài sản` của `ROA` chứa cả tiền mặt nhàn rỗi và nợ thương mại không tốn lãi, còn tử số đã trừ lãi vay.
- **Cách sửa:** Tính `NOPAT` và `Vốn đầu tư (IC)` để ra `ROIC` rồi mới so với `WACC`.

### Sai lầm 2: Tính `NOPAT` bằng cách lấy `EBIT` trừ thẳng dòng "Thuế TNDN thực nộp" của công ty vay nợ lớn
- **Sai ở đâu:** Thuế thực nộp đã giảm nhờ lá chắn thuế của lãi vay; trừ thẳng sẽ tính trùng lợi ích thuế của nợ vay (vốn đã nằm trong `WACC`).
- **Cách sửa:** Luôn tính $\text{NOPAT} = \text{EBIT} \times (1 - \text{Thuế suất})$.

### Sai lầm 3: Ca ngợi tăng trưởng lợi nhuận khi `ROIC < WACC`
- **Sai ở đâu:** Khi `ROIC < WACC`, mỗi đồng vốn mới bỏ thêm đều sinh lời thấp hơn chi phí huy động, làm cổ đông nghèo đi.
- **Cách sửa:** Luôn kiểm tra `ROIC − WACC` và dòng tiền tự do còn lại sau tái đầu tư.

---

## Kiểm tra chuyển bài

Trước khi chuyển sang **[Bài 004: Dòng tiền và chất lượng lợi nhuận](004-cash-flow-and-earnings-quality.md)** (Bước 10/23 Nhánh 1), hãy tự trả lời 3 câu hỏi sau:

1. Vì sao `Tổng nợ vay chịu lãi + Vốn chủ sở hữu − Tiền mặt` luôn khớp với `Tài sản cố định ròng + Vốn lưu động phi tiền mặt`?
2. Một công ty có `ROIC = 6%/năm` và `WACC = 10%/năm` giữ lại `100%` lợi nhuận để mở rộng gấp đôi quy mô: tốt hay xấu cho cổ đông?
3. **Bắc cầu sang [Bài 004](004-cash-flow-and-earnings-quality.md):** Nếu công ty báo cáo `NOPAT = 200 tỷ` và `ROIC = 25%` rất cao, nhưng toàn bộ lợi nhuận nằm ở **Phải thu khách hàng** và **Tồn kho** khiến két tiền trống rỗng (`CFO < 0`), làm sao phát hiện "lợi nhuận giấy" đó? Hãy sang ngay **[Bài 004: Dòng tiền và chất lượng lợi nhuận](004-cash-flow-and-earnings-quality.md)**!

---

## Ranh giới an toàn

- Bài học này là khung phân tích chất lượng doanh nghiệp, không phải khuyến nghị mua/bán/nắm giữ cổ phiếu.
- Không đặt lệnh đầu tư chỉ dựa trên một chỉ số `ROIC` cao hay lời tuyên bố "có moat".

## Nguồn Internet đã mở và nghiên cứu liên quan

Các nguồn dưới đây được mở trực tiếp ngày `2026-08-12` và đối chiếu lại ngày `2026-11-06`:

- [Return on Capital (ROC), Return on Invested Capital (ROIC) and Return on Equity (ROE) — Aswath Damodaran, NYU Stern (PDF)](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/returnmeasures.pdf) (`07/2007`) — Công thức `NOPAT`, 2 cách tính `IC`, `ROIC`, `Excess Return = ROIC − WACC`, `g = Reinvestment Rate × ROIC` và cảnh báo về `ROA`.
- [A long-term look at ROIC — McKinsey on Finance](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/a-long-term-look-at-roic) (`2006-02-01`) & [Balancing ROIC and growth to build value](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/balancing-roic-and-growth-to-build-value) (`2006-03-01`) — Trung vị `ROIC ~10%` trên `7.000` công ty Mỹ và độ bền của `ROIC > 20%`.
- [Five Sources of Moats Whitepaper — VanEck (mô tả phương pháp luận Morningstar)](https://www.vaneck.com/nl/en/moat-investing/five-sources-of-moats-whitepaper.pdf) — Nguồn thứ cấp mô tả 5 nguồn `Moat`.
- [IAS 24 — Related Party Disclosures](https://www.ifrs.org/issued-standards/list-of-standards/ias-24-related-party-disclosures/) & [IFRS 3 — Business Combinations](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-3-business-combinations/) (IFRS Foundation) — Giao dịch bên liên quan và `Goodwill`.
- [Investor Bulletin: Investing in an IPO — SEC Investor.gov](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-17) (`2022-10-14`) — Pha loãng cổ phiếu (`Dilution`).
- [Apple Inc. — Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) (`31/10/2025`) — Số liệu thực tế tại mục Ví dụ từ nguồn thật, Bài tập 9 và [apple_fy2025_inputs.csv](../practice/models/apple_fy2025_inputs.csv).
