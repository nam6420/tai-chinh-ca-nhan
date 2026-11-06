# Bài 002: Hiểu và tìm một cổ phiếu đang được định giá rẻ

- Ngày: `2026-11-06`
- Chốt dữ liệu lúc: `2026-11-06 10:30 UTC+7 (Asia/Ho_Chi_Minh)`
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Mục tiêu: Phân biệt "thị giá một cổ phiếu thấp" với "doanh nghiệp đang được định giá rẻ"; hiểu trực giác và tính từng bước **Vốn hóa thị trường (`Market Cap`)**, **Giá trị doanh nghiệp (`Enterprise Value — EV`)**, **Hệ số giá trên thu nhập (`P/E`)** và **Hệ số giá trên giá trị sổ sách (`P/B`)**; nhận diện **bẫy giá rẻ (`value trap`)** khi lợi nhuận chứa khoản đột biến một lần hoặc đang ở đỉnh chu kỳ; xây dựng quy trình sàng lọc an toàn cho người mới.
- Thời lượng: Ba phiên học ngắn + thực hành với [valuation.py](../practice/models/valuation.py).
- Bài trước liên quan: Thứ tự đọc 7/23 của Nhánh 1 — học ngay sau [Bài N3 (Phần A): Tìm đường trên báo cáo tài chính Việt Nam](N3-vietnam-vas-statements.md#phần-a--tìm-đường-trên-báo-cáo-sau-n2) (kế thừa [Bài N1](N1-market-basics.md), [Bài N6](N6-business-model-unit-economics.md), [Bài 001](001-business-financial-statements.md), [Bài N2](N2-statement-line-items.md) và [Bài N8](N8-finding-verifying-sources.md)). Học tiếp: [Bài N4: Giá trị thời gian của tiền và lợi suất](N4-time-value-returns.md), sau đó sang [Bài 003: Chất lượng doanh nghiệp — lợi thế cạnh tranh, ROIC và khả năng tái đầu tư](003-business-quality-moat-and-roic.md).
- Câu hỏi cốt lõi: **Làm sao biết một cổ phiếu đang thực sự "rẻ" so với những gì doanh nghiệp tạo ra, thay vì chỉ có con số giá trên màn hình trông nhỏ hoặc lợi nhuận đang phình to tạm thời?**

> Đây là bài học nền tảng toàn cầu, không phải khuyến nghị mua, bán hay nắm giữ chứng khoán. Các ví dụ số học về Quán cà phê Sao Biển và các công ty X, Y là hư cấu; phần thực hành dùng số liệu thật từ báo cáo `Form 10-K FY2025` của Apple Inc.

---

## Hiểu bài này trong 1 phút

`SUY_LUẬN` Bài học này giải quyết nhầm lẫn phổ biến nhất của người mới: **thấy giá một cổ phiếu là `8.000 đồng` liền nghĩ nó "rẻ" hơn cổ phiếu giá `80.000 đồng`, hoặc thấy tỷ số `P/E = 6 lần` liền nghĩ là món hời chắc thắng.**

Hình dung bạn đi mua bánh pizza: một miếng bánh cắt nhỏ giá `20.000 đồng` chưa chắc đã rẻ hơn cả chiếc bánh lớn giá `100.000 đồng`. Muốn biết bên nào rẻ hơn, bạn phải biết chiếc bánh được cắt làm **bao nhiêu miếng**, nhân bánh **nhiều hay ít**, và tiệm bánh có bắt người mua gánh thêm **khoản nợ nào** không.

Với cổ phiếu cũng vậy: không bao giờ nhìn thị giá 1 cổ phần đơn lẻ, mà phải đặt **tổng số tiền phải trả để sở hữu doanh nghiệp** bên cạnh **khả năng tạo lợi nhuận và tiền mặt bền vững**, **sức khỏe bảng cân đối (tiền mặt và nợ vay)** cùng **rủi ro phía trước**.

### Ba câu hỏi bắt buộc phải trả lời theo đúng thứ tự

| Thứ tự | Câu hỏi cốt lõi | Dùng kiến thức từ bài nào? | Nếu chưa trả lời được thì sao? |
|---:|---|---|---|
| **1** | **Doanh nghiệp kiếm tiền bằng cách nào?** | [Bài N6](N6-business-model-unit-economics.md) (Mô hình kinh doanh & Kinh tế đơn vị) | Chưa hiểu mô hình kinh doanh thì chưa nên định giá. |
| **2** | **Doanh nghiệp có khỏe và lợi nhuận có đáng tin không?** | [Bài 001](001-business-financial-statements.md), [Bài N2](N2-statement-line-items.md), [Bài N8](N8-finding-verifying-sources.md), [Bài N3 (Phần A)](N3-vietnam-vas-statements.md#phần-a--tìm-đường-trên-báo-cáo-sau-n2) | Phải đọc báo cáo tài chính, dòng tiền, nợ vay và thuyết minh trước. |
| **3** | **Giá thị trường có thấp hơn đáng kể so với khoảng giá trị hợp lý không?** | Bài 002 này và đào sâu ở [Bài N4](N4-time-value-returns.md), [Bài 003](003-business-quality-moat-and-roic.md)–[Bài 012](012-scenarios-margin-of-safety.md) | Chưa thể gọi cổ phiếu là "rẻ" hay "đắt". |

> Câu cần nhớ: **Đừng hỏi “giá 1 cổ phiếu trên bảng điện có thấp không?”; hãy hỏi “tổng giá mua cả doanh nghiệp có thấp so với dòng tiền bền vững mà nó tạo ra sau khi đã tính đủ nợ vay và rủi ro không?”**

---

## Ôn bài cũ hoặc kiểm tra đầu vào

Hãy nối lại hành trình của **Quán cà phê Sao Biển** qua 6 bài bạn vừa học trong Nhánh 1:
1. **[Bài N1](N1-market-basics.md) & [Bài N6](N6-business-model-unit-economics.md):** Quán chia vốn chủ sở hữu thành `100.000 cổ phần`; bán mỗi ly cà phê giá `40.000 đồng`, lãi góp `25.000 đồng/ly`, hòa vốn ở `2.000 ly/tháng`.
2. **[Bài 001](001-business-financial-statements.md) & [Bài N2](N2-statement-line-items.md):** Trong năm đầu tiên, Quán Sao Biển đạt Doanh thu thuần `1.200 triệu đồng`, `EBIT = 150 triệu đồng`, Lợi nhuận sau thuế `= 100 triệu đồng` (`EPS = 1.000 đồng/cp`), `CFO = +115 triệu đồng`. Cuối năm quán có Tiền mặt `185 triệu đồng`, Tổng tài sản `730 triệu đồng`, Nợ vay ngân hàng `200 triệu đồng` (cùng `30 triệu` phải trả người bán) và **Vốn chủ sở hữu (`Book Value`)** `= 500 triệu đồng` (`5.000 đồng/cp`).
3. **[Bài N8](N8-finding-verifying-sources.md) & [Bài N3 (Phần A)](N3-vietnam-vas-statements.md#phần-a--tìm-đường-trên-báo-cáo-sau-n2):** Bạn đã biết mở tệp PDF báo cáo gốc và tra cứu các dòng trên biểu mẫu `B01-DN`, `B02-DN`, `B03-DN`.

Bây giờ, giả sử cổ phiếu của **Quán cà phê Sao Biển** lên sàn giao dịch. Làm sao biết mức giá trên bảng điện là món hời hay cái bẫy?

---

## Phiên 1 — Thị giá 1 cổ phiếu, Vốn hóa (`Market Cap`) và Giá mua đứt cả doanh nghiệp (`EV`)

### 1. Vì sao cổ phiếu giá `1.000 đồng` có thể đắt gấp đôi cổ phiếu giá `10.000 đồng`?

Thị giá 1 cổ phiếu (`Share Price`) chỉ là giá của **một lát cắt**, chưa cho biết cả chiếc bánh đắt hay rẻ nếu chưa nhân với **tổng số cổ phiếu đang lưu hành (`Shares Outstanding`)**.

`SỰ_THẬT` Tổng giá trị thị trường của toàn bộ vốn chủ sở hữu được gọi là **Vốn hóa thị trường (`Market Capitalization — Market Cap`)**:

$$\text{Vốn hóa thị trường (Market Cap)} = \text{Giá thị trường 1 cổ phiếu} \times \text{Số cổ phiếu đang lưu hành}$$

`PHÉP_TÍNH` So sánh hai quán cà phê có quy mô và lợi nhuận y hệt nhau (cùng lãi ròng `100 triệu đồng/năm`), chỉ khác số lượng cổ phần chia nhỏ:
- **Quán Sao Biển A:** Chia làm `100.000 cổ phiếu`, giá mỗi cổ phiếu **`10.000 đồng`** $\implies \text{Vốn hóa A} = 10.000 \times 100.000 = 1.000 \text{ triệu đồng (1 tỷ đồng)}$.
- **Quán Sao Biển B:** Chia làm `2.000.000 cổ phiếu`, giá mỗi cổ phiếu chỉ **`1.000 đồng`** $\implies \text{Vốn hóa B} = 1.000 \times 2.000.000 = 2.000 \text{ triệu đồng (2 tỷ đồng)}$.

`SUY_LUẬN` Cổ phiếu Quán B có thị giá (`1.000đ`) chỉ bằng **một phần mười** Quán A (`10.000đ`), nhưng tổng giá thị trường đòi bạn trả cho 100% vốn chủ của Quán B (`2 tỷ đồng`) lại **đắt gấp đôi** Quán A (`1 tỷ đồng`)! Vì vậy, lọc "cổ phiếu dưới 10.000 đồng vì nghĩ nó rẻ" là sai lầm số học.

### 2. Từ Vốn hóa (`Market Cap`) đến Giá trị doanh nghiệp (`Enterprise Value — EV`): Cái giá thực sự khi mua cả quán

Giả sử bạn bỏ `1.000 triệu đồng` mua đứt 100% cổ phần của Quán Sao Biển ([Bài N2](N2-statement-line-items.md)). Khi nhận chìa khóa quán:
- Mở két sắt của quán ra, bạn lấy được ngay **`185 triệu đồng` tiền mặt** có sẵn (`Cash`) — coi như được hoàn lại `185 triệu`!
- Nhưng đồng thời, bạn phải gánh khoản **nợ vay ngân hàng `200 triệu đồng`** (`Total Debt`) mà quán đang nợ.

Vậy **tổng số tiền thực chất (ròng)** bạn phải bỏ ra để sở hữu toàn bộ bộ máy kinh doanh của quán trong trạng thái sạch nợ vay là:
$$\text{Giá mua thực chất (EV)} = 1.000 \text{ (Vốn hóa)} + 200 \text{ (Nợ vay)} - 185 \text{ (Tiền mặt)} = 1.015 \text{ triệu đồng}$$

Đó chính là **Giá trị doanh nghiệp (`Enterprise Value — EV`)**:

$$\text{Giá trị doanh nghiệp (EV)} \approx \text{Vốn hóa thị trường (Market Cap)} + \text{Tổng nợ vay chịu lãi (Total Debt)} - \text{Tiền và tương đương tiền (Cash)}$$

*(Lưu ý: Phần "Tiền" tính cả tiền gửi có kỳ hạn/chứng khoán khả mại thanh khoản cao; công thức `EV` chỉ dùng cho **doanh nghiệp phi tài chính**, không áp dụng cho ngân hàng và bảo hiểm).*

`PHÉP_TÍNH` Hãy xem hai công ty C và D cùng có Vốn hóa `= 1.000 tỷ đồng`:
- **Công ty C (Không nợ, nhiều tiền):** Vốn hóa `1.000 tỷ`, Nợ vay `0`, Tiền mặt `400 tỷ` $\implies \text{EV}_C = 1.000 + 0 - 400 = 600 \text{ tỷ đồng}$.
- **Công ty D (Nợ vay lớn):** Vốn hóa `1.000 tỷ`, Nợ vay `800 tỷ`, Tiền mặt `50 tỷ` $\implies \text{EV}_D = 1.000 + 800 - 50 = 1.750 \text{ tỷ đồng}$ (đắt gần gấp 3 lần C!).

---

## Phiên 2 — Bốn thước đo khởi đầu và giải phẫu "Bẫy P/E thấp" (`Value Trap`)

### 1. Bốn tỷ số định giá khởi đầu (Học sâu ở [Bài 009](009-valuation-multiples.md))

| Tên tỷ số | Công thức tính | Minh họa tại Quán Sao Biển (Giá `10.000đ`, Vốn hóa `1.000 triệu`, `EV = 1.015 triệu`) | Khi nào hữu ích nhất? |
|---|---|---|---|
| **1. `P/E`** (`Price-to-Earnings`) | $$\frac{\text{Giá 1 cp}}{\text{EPS}} = \frac{\text{Vốn hóa}}{\text{LNST thuộc CĐ thường}}$$ | Lãi ròng `100 triệu` (`EPS = 1.000đ`) $\implies \text{P/E} = \frac{10.000}{1.000} = 10,0 \text{ lần}$ (trả 10 đồng cho 1 đồng lãi ròng hàng năm). | Khi lợi nhuận dương, ổn định và không có khoản lãi đột biến một lần. |
| **2. `P/B`** (`Price-to-Book`) | $$\frac{\text{Giá 1 cp}}{\text{BVPS}} = \frac{\text{Vốn hóa}}{\text{Vốn chủ sở hữu}}$$ | Vốn chủ sổ sách `500 triệu` (`BVPS = 5.000đ`) $\implies \text{P/B} = \frac{1.000}{500} = 2,0 \text{ lần}$. | Ngành nhiều tài sản hữu hình (phải đi kèm `ROIC` / `ROE` ở [Bài 003](003-business-quality-moat-and-roic.md)). |
| **3. `EV/EBIT`** | $$\frac{\text{Giá trị doanh nghiệp (EV)}}{\text{Lợi nhuận hoạt động (EBIT)}}$$ | `EV = 1.015 triệu`, `EBIT = 150 triệu` $\implies \text{EV/EBIT} = \frac{1.015}{150} \approx 6,77 \text{ lần}$. | So sánh các công ty cùng ngành nhưng có mức vay nợ khác nhau. |
| **4. `FCF Yield`** (Tỷ suất dòng tiền tự do) | $$\frac{\text{Dòng tiền tự do (FCF)}}{\text{Vốn hóa thị trường}}$$ | Giả sử năm ổn định `FCF = 90 triệu` $\implies \text{FCF Yield} = \frac{90}{1.000} = 9,0\%/\text{năm}$. | Đo lượng tiền mặt tự do thực sự tạo ra trên mỗi 100 đồng vốn hóa ([Bài 004](004-cash-flow-and-earnings-quality.md)). |

### 2. Vì sao `P/E = 10 lần` thực chất có thể là `P/E = 20 lần`?

Trong phân số $\text{P/E} = \frac{P}{E}$, tỷ số thấp có thể không phải vì giá $P$ rẻ, mà vì **mẫu số thu nhập $E$ năm vừa rồi phình to bất thường**!

`PHÉP_TÍNH` Một công ty hư cấu có thị giá **`80.000 đồng/cổ phiếu`**, báo cáo `EPS = 8.000 đồng/cp` $\implies \text{P/E báo cáo} = \frac{80.000}{8.000} = 10,0 \text{ lần}$.
Nhưng khi đọc Thuyết minh ([Bài N2](N2-statement-line-items.md), [Bài N3](N3-vietnam-vas-statements.md)), bạn phát hiện `4.000 đồng/cp` đến từ **lãi bán đất một lần**, còn thu nhập cốt lõi trong kịch bản bất lợi chỉ đạt **`4.000 đồng/cp`**:
$$\text{P/E trên EPS bất lợi} = \frac{80.000}{4.000} = 20,0 \text{ lần}$$

Khi lập bảng kịch bản (`KỊCH_BẢN` minh họa số học):

| Kịch bản | `EPS` bền vững giả định (nghìn đồng) | `P/E` hợp lý giả định (lần) | Kết quả `EPS × P/E` (nghìn đồng) | Nhận xét so với thị giá `80 nghìn đồng` |
|---|---:|---:|---:|---|
| **Stress (Vỡ nợ / Đứt thanh khoản)** | `≤ 0` | Không dùng được | Vốn chủ có thể về gần `0` | Cổ đông có thể mất gần toàn bộ vốn |
| **Bất lợi (`Bear`)** | `4,0` | `10,0` | `40,0` | Đang đắt gấp đôi (`-50%`), và `40` không phải giá sàn cố định |
| **Cơ sở (`Base`)** | `6,0` | `12,0` | `72,0` | Thị giá `80` vẫn cao hơn mức cơ sở `72` |
| **Thuận lợi (`Bull`)** | `8,0` | `14,0` | `112,0` | Chỉ có lời nếu kịch bản thuận lợi thực sự diễn ra |

---

## Phiên 3 — Ví dụ từ nguồn thật và Quy trình sàng lọc 6 bước

## Ví dụ từ nguồn thật: Kiểm tra Vốn hóa, Tiền mặt ròng (`Net Cash`), `EV` và `P/E` trên báo cáo Apple Inc. (`FY2025`)

`SỰ_THẬT` Trích xuất từ báo cáo **[Apple Inc. — Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm)** (kết thúc `27/09/2025`, nộp SEC ngày `31/10/2025`, đơn vị: triệu USD) trong tệp [apple_fy2025_inputs.csv](../practice/models/apple_fy2025_inputs.csv) và mô hình [valuation.py](../practice/models/valuation.py):
- **Kết quả kinh doanh:** Doanh thu thuần `= 416.161`; Lợi nhuận hoạt động (`EBIT`) `= 133.050`; Lợi nhuận ròng `= 112.010`; Cổ phiếu pha loãng bình quân `= 15.004,697 triệu cp`; Cổ phiếu lưu hành tại bìa báo cáo (`17/10/2025`) `= 14.776,353 triệu cp`.
- **Bảng cân đối (`27/09/2025`):** Tổng tiền và chứng khoán khả mại (`Cash + Marketable securities`) `= 35.934 + 18.763 + 77.723 = 132.420 triệu USD`; Tổng nợ vay chịu lãi (`Commercial paper + Term debt`) `= 7.979 + 12.350 + 78.328 = 98.657 triệu USD`; Vốn chủ sở hữu `= 73.733 triệu USD`.

`PHÉP_TÍNH` Thực hiện từng bước (đối chiếu với hàm `load_apple()` và `per_share()` trong [valuation.py](../practice/models/valuation.py)):
1. **Tính `Diluted EPS` và `BVPS`:**
   $$\text{Diluted EPS} = \frac{112.010}{15.004,697} \approx 7,46 \text{ USD/cp}; \quad \text{BVPS} = \frac{73.733}{14.776,353} \approx 4,99 \text{ USD/cp}$$
2. **Tính Tiền mặt ròng (`Net Cash`):**
   $$\text{Net Cash} = 132.420 \text{ (Tổng tiền & CK khả mại)} - 98.657 \text{ (Tổng nợ vay)} = +33.763 \text{ triệu USD}$$
3. **Với thị giá giả định minh họa (`KỊCH_BẢN` `230,00 USD/cp`):**
   - **Vốn hóa (`Market Cap`):** $230,00 \times 14.776,353 \approx 3.398.561 \text{ triệu USD}$.
   - **Giá trị doanh nghiệp (`EV`):** $3.398.561 + 98.657 - 132.420 = 3.364.798 \text{ triệu USD}$ (thấp hơn Vốn hóa `33.763 triệu USD` nhờ có tiền mặt ròng!).
   - **Bội số:** $\text{P/E} = \frac{230}{7,46} \approx 30,8 \text{ lần}$; $\text{P/B} = \frac{230}{4,99} \approx 46,1 \text{ lần}$.

### Quy trình sàng lọc 6 bước và Thứ tự học tiếp trong Nhánh 1

Bộ lọc (`screener`) chỉ tạo **danh sách chờ nghiên cứu**, không phải tín hiệu mua:
1. Chọn doanh nghiệp phi tài chính có mô hình kinh doanh dễ hiểu ([Bài N6](N6-business-model-unit-economics.md)).
2. Thu thập 3–5 năm dữ liệu từ báo cáo gốc ([Bài N8](N8-finding-verifying-sources.md) & [Bài N3](N3-vietnam-vas-statements.md)).
3. Kiểm tra lợi thế cạnh tranh (`Moat`) và tỷ suất sinh lời trên vốn `ROIC` ([Bài 003](003-business-quality-moat-and-roic.md)).
4. Kiểm tra dòng tiền (`CFO`, `FCF`), nợ vay, phân bổ vốn, thuyết minh và vĩ mô ([Bài 004](004-cash-flow-and-earnings-quality.md)–[Bài 008](008-macro-transmission.md)).
5. Quy đổi dòng tiền theo giá trị thời gian ([Bài N4](N4-time-value-returns.md)) và định giá theo 3 kịch bản ([Bài 009](009-valuation-multiples.md)–[Bài 012](012-scenarios-margin-of-safety.md)).
6. Viết rõ bằng chứng trái chiều và điều kiện làm luận điểm mất hiệu lực.

---

## Bài tập

`KỊCH_BẢN` Tự giải từng bước 10 bài tập dưới đây trước khi mở Đáp án (Bài 9–10 dùng dữ liệu thật của Apple `FY2025` từ [valuation.py](../practice/models/valuation.py) / [apple_fy2025_inputs.csv](../practice/models/apple_fy2025_inputs.csv)):

1. **Thị giá thấp so với Vốn hóa:** Cổ phiếu X giá `8.000 đồng/cp` có `2 tỷ cổ phiếu`. Cổ phiếu Y giá `80.000 đồng/cp` có `100 triệu cổ phiếu`. Tính Vốn hóa của X và Y; công ty nào lớn hơn và gấp mấy lần?
2. **Tính `EV` của Quán Sao Biển:** Quán có `100.000 cổ phiếu` giá `12.000 đồng/cp`, tiền mặt `185 triệu đồng`, nợ vay ngân hàng `200 triệu đồng`, phải trả người bán (không chịu lãi) `30 triệu đồng`. Tính Vốn hóa và `EV`. Vì sao `30 triệu` phải trả người bán không cộng vào `EV`?
3. **Cùng Vốn hóa, khác nợ vay:** Công ty M và N cùng có `EBIT = 200 tỷ đồng` và Vốn hóa `= 1.200 tỷ đồng`. M có `300 tỷ` tiền mặt, `0` nợ vay; N có `50 tỷ` tiền mặt, `650 tỷ` nợ vay. Tính `EV` và `EV/EBIT` của M và N.
4. **Bẫy `P/E` thấp do lãi một lần:** Công ty P có `50 triệu cp`, giá `30.000 đồng/cp`, LNST năm qua là `250 tỷ đồng` (trong đó có `150 tỷ` lãi bán tòa nhà một lần). Tính `EPS`, `P/E` báo cáo và `EPS`, `P/E` cốt lõi.
5. **Tác động của pha loãng (`Dilution`):** Năm 2024, Công ty Q lãi `100 tỷ` trên `50 triệu cp`. Năm 2025, Q lãi `120 tỷ` (`+20%`) nhưng số cổ phiếu tăng lên `80 triệu cp`. Tính `EPS` hai năm và giải thích.
6. **Định giá 3 kịch bản (`Bear / Base / Bull`):** Cổ phiếu R có thị giá `45.000 đồng/cp`. Ước tính: Bất lợi (`EPS = 3.000đ`, `P/E = 10x`); Cơ sở (`EPS = 4.500đ`, `P/E = 12x`); Thuận lợi (`EPS = 6.000đ`, `P/E = 14x`). Tính giá trị ước tính mỗi kịch bản và `%` lệch so với thị giá.
7. **Cảnh báo từ Dòng tiền:** Doanh nghiệp có LNST tăng 3 năm (`50 → 80 → 120 tỷ`), `P/E = 7x`, nhưng `CFO` âm cả 3 năm (`-10 → -25 → -40 tỷ`) và Phải thu tăng gấp 4 lần. Nêu 2 giả thuyết cần xác minh.
8. **Bẫy `P/B < 1`:** Công ty H có Vốn hóa `600 tỷ`, Vốn chủ sổ sách `800 tỷ`, nhưng mỗi năm chỉ lãi `16 tỷ` (`ROE = 2%/năm`). Tính `P/B` và giải thích vì sao `P/B = 0,75x` chưa chắc là rẻ.
9. **Dữ liệu thật Apple (`FY2025`) — `Net Cash` và `per_share`:** Từ [apple_fy2025_inputs.csv](../practice/models/apple_fy2025_inputs.csv), kiểm tra lại Tổng tiền & CK khả mại (`132.420`), Tổng nợ vay (`98.657`) và `Net Cash` (`+33.763 triệu USD`). Nếu hàm `dcf()` trong [valuation.py](../practice/models/valuation.py) ra `EV = 2.458.651 triệu USD`, hãy tính `per_share` với `14.776,353 triệu cp`.
10. **Dữ liệu thật Apple (`FY2025`) — `FCF` và `SBC`:** Với `CFO = 111.482`, `CapEx = 12.715` và thưởng cổ phiếu `SBC = 12.863` (triệu USD), hãy tính `FCF = CFO − CapEx` và `fcf0 = CFO − CapEx − SBC` như trong [valuation.py](../practice/models/valuation.py).

---

## Đáp án

1. `PHÉP_TÍNH` Vốn hóa X $= 8.000 \times 2 \text{ tỷ} = 16.000 \text{ tỷ đồng}$; Vốn hóa Y $= 80.000 \times 100 \text{ triệu} = 8.000 \text{ tỷ đồng}$. X có vốn hóa gấp đôi Y.
2. `PHÉP_TÍNH` Vốn hóa $= 1.200 \text{ triệu}$; $\text{EV} = 1.200 + 200 - 185 = 1.215 \text{ triệu đồng}$. Phải trả người bán `30 triệu` là nợ thương mại không chịu lãi (nằm trong vốn lưu động), không cộng vào Tổng nợ vay.
3. `PHÉP_TÍNH` $\text{EV}_M = 1.200 + 0 - 300 = 900 \text{ tỷ} \implies \text{EV/EBIT}_M = 4,5\text{x}$; $\text{EV}_N = 1.200 + 650 - 50 = 1.800 \text{ tỷ} \implies \text{EV/EBIT}_N = 9,0\text{x}$ (M rẻ bằng một nửa N).
4. `PHÉP_TÍNH` Báo cáo: $\text{EPS} = 5.000\text{đ}, \text{P/E} = 6,0\text{x}$. Cốt lõi (loại `150 tỷ` lãi bán nhà, còn `100 tỷ`): $\text{EPS} = 2.000\text{đ}, \text{P/E} = 15,0\text{x}$.
5. `PHÉP_TÍNH` $\text{EPS}_{2024} = 100 / 50 = 2.000\text{đ}$; $\text{EPS}_{2025} = 120 / 80 = 1.500\text{đ}$ (giảm `-25%` do số cổ phiếu tăng `+60%`).
6. `PHÉP_TÍNH` Bear: `30.000đ` (`-33,3%`); Base: `54.000đ` (`+20,0%`); Bull: `84.000đ` (`+86,7%`).
7. `SUY_LUẬN` Giả thuyết 1: Nới lỏng bán chịu/ghi nhận doanh thu sớm chưa thu được tiền; Giả thuyết 2: Nguy cơ trích lập dự phòng nợ xấu và thiếu tiền mặt trả nợ.
8. `PHÉP_TÍNH` $\text{P/B} = 600 / 800 = 0,75\text{x}$. Không tự động rẻ vì tài sản lạc hậu chỉ sinh lời `ROE = 2%/năm` (phá hủy giá trị so với chi phí vốn — [Bài 003](003-business-quality-moat-and-roic.md)).
9. `PHÉP_TÍNH` $\text{per\_share} = \frac{2.458.651 + 33.763}{14.776,353} = \frac{2.492.414}{14.776,353} \approx 168,68 \text{ USD/cp}$ (khớp `valuation.py`).
10. `PHÉP_TÍNH` $\text{FCF} = 111.482 - 12.715 = 98.767 \text{ triệu USD}$; $\text{fcf0} = 98.767 - 12.863 = 85.904 \text{ triệu USD}$ (trừ `SBC` để phản ánh chi phí pha loãng cổ phần thưởng).

---

## Bài làm với dữ liệu thiếu hoặc lệch

Khi tính Vốn hóa, `EV` và `P/E` thực tế, bạn thường gặp 2 lệch pha dữ liệu:
1. **Lệch số cổ phiếu giữa trang bìa (`14.776,353 triệu cp`) và số bình quân pha loãng (`15.004,697 triệu cp`):** Dùng số cổ phiếu lưu hành tại thời điểm hiện tại để tính Vốn hóa, và dùng số bình quân pha loãng để kiểm tra `Diluted EPS`.
2. **Bộ lọc tự động bỏ sót Tiền gửi có kỳ hạn (Mã `123` trên báo cáo Việt Nam hoặc `Marketable securities` trên báo cáo Mỹ) và lãi đột biến một lần:** Luôn mở Bảng cân đối và Thuyết minh để cộng đủ thanh khoản và loại lãi bất thường trước khi tính `EV` và `P/E`.

---

## Sai ở đâu

### Sai lầm 1: Lọc mua cổ phiếu "dưới 10.000 đồng/cp" vì nghĩ mệnh giá nhỏ là rẻ
- **Sai ở đâu:** Nhầm thị giá 1 lát cắt với quy mô cả doanh nghiệp (`Market Cap` và `EV`).
- **Cách sửa:** Nhân thị giá với tổng số cổ phiếu lưu hành và cộng nợ vay ròng để tính `EV`.

### Sai lầm 2: Mua cổ phiếu chu kỳ hoặc có lãi bán tài sản một lần chỉ vì `P/E = 5–6 lần`
- **Sai ở đâu:** Mẫu số `E` đang phình to tạm thời ở đỉnh chu kỳ hoặc nhờ thu nhập một lần.
- **Cách sửa:** Chuẩn hóa lợi nhuận qua nhiều năm và loại bỏ khoản lãi một lần.

### Sai lầm 3: Chỉ nhìn `P/E` mà bỏ qua `EV` khi so sánh hai công ty có nợ vay trái ngược
- **Sai ở đâu:** `P/E` không phản ánh trực tiếp khối nợ gốc trên bảng cân đối kế toán.
- **Cách sửa:** Luôn đặt `EV/EBIT` (hoặc `EV/EBITDA`) bên cạnh `P/E`.

---

## Kiểm tra chuyển bài

Trước khi chuyển sang **[Bài N4: Giá trị thời gian của tiền và lợi suất](N4-time-value-returns.md)** (Bước 8/23 Nhánh 1), hãy trả lời 3 câu hỏi sau:

1. Một công ty có `200 triệu cp` giá `25.000 đồng/cp`, tiền mặt `800 tỷ đồng`, tổng nợ vay `1.300 tỷ đồng`. Tính **Vốn hóa** và **`EV`**. *(Đáp án: Vốn hóa `= 5.000 tỷ`; `EV = 5.500 tỷ đồng`).*
2. Vì sao không được định giá cổ phiếu khi chưa trả lời được doanh nghiệp kiếm tiền bằng cách nào và lợi nhuận có thành tiền mặt không?
3. **Bắc cầu sang [Bài N4](N4-time-value-returns.md):** Nếu Quán Sao Biển hứa mang về `150 triệu đồng` sau `3 năm` nữa, vì sao khoản tiền đó không bằng `150 triệu đồng` cầm trên tay hôm nay — và làm sao quy đổi nó về hiện tại (`PV`)? Hãy bước sang **[Bài N4: Giá trị thời gian của tiền và lợi suất](N4-time-value-returns.md)**!

---

## Ranh giới an toàn

- Bài học này không phải khuyến nghị mua, bán hay nắm giữ chứng khoán; không đặt lệnh bằng tiền thật chỉ dựa trên bộ lọc tỷ số và không dùng đòn bẩy (`margin`).

## Nguồn Internet đã mở và nghiên cứu liên quan

Các nguồn được mở trực tiếp ngày `2026-08-10` và đối chiếu lại ngày `2026-11-06`:

- [FINRA — Evaluating Stocks](https://www.finra.org/investors/investing/investment-products/stocks/evaluating-stocks), [FINRA — Value Investing](https://www.finra.org/investors/insights/value-investing) (`2025-07-01`) & [FINRA — Defining the Value of an Investment](https://www.finra.org/investors/insights/defining-value-investment) (`2025-11-12`) — Định nghĩa `Market Cap`, `EPS`, `P/E`, `P/B`, giá trị nội tại và bẫy giá rẻ (`value trap`).
- [SEC Investor.gov — How to Read a 10-K](https://www.investor.gov/introduction-investing/getting-started/researching-investments/how-read-10-k) & [Beginners’ Guide to Asset Allocation, Diversification, and Rebalancing](https://www.investor.gov/additional-resources/general-resources/publications-research/info-sheets/beginners-guide-asset) — Quy trình đọc báo cáo gốc và ranh giới đa dạng hóa.
- [Apple Inc. — Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) (`31/10/2025`) — Số liệu thực tế tại Phiên 3, Bài tập 9–10 và tệp [apple_fy2025_inputs.csv](../practice/models/apple_fy2025_inputs.csv) dùng trong [valuation.py](../practice/models/valuation.py).
