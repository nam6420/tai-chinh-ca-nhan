# Bài 014 — Kinh tế ngành và chu kỳ vốn

- Ngày: `2026-11-05`
- Chốt dữ liệu lúc: `2026-11-05 12:30 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Tách biệt bốn biến số kinh tế ngành gồm Giá bán (`Price`), Sản lượng (`Volume`), Chi phí biến đổi/cố định (`Variable/Fixed Cost`) và Công suất (`Capacity`); tính điểm hòa vốn khai thác và đòn bẩy hoạt động (`DOL`); giải phẫu cơ chế Chu kỳ vốn (`Capital Cycle`) với độ trễ đầu tư tài sản cố định (`CapEx lag`) và tránh bẫy định giá đỉnh chu kỳ (`Peak-earnings P/E trap`).
- Bài trước liên quan: [N6](N6-business-model-unit-economics.md), [003](003-business-quality-moat-and-roic.md), [008](008-macro-transmission.md), [Q3](Q3-normalizing-earnings-cyclical.md), [F5](F5-vietnam-industry-research-framework.md).
- Thời lượng: Ba phiên học có điểm dừng (mỗi phiên 45 phút) + thực hành chạy kiểm chứng trên mô hình [cyclical.py](../practice/models/cyclical.py) và dữ liệu [hpg_cycle_inputs.csv](../practice/models/hpg_cycle_inputs.csv).
- Câu hỏi cốt lõi: **Khi lợi nhuận của một doanh nghiệp tăng gấp đôi trong một năm, làm sao phân biệt được đó là nhờ lợi thế cạnh tranh bền vững (`Moat`) hay chỉ là pha thuận lợi tạm thời của chu kỳ công suất và giá nguyên liệu đầu vào?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/014-fact-check.md), [phản biện](../reviews/014-risk-review.md).

---

## Hiểu bài trong một phút

Trong các ngành thâm dụng vốn như thép, hàng không, vận tải biển, hóa chất hay xi măng, **nhu cầu của khách hàng có thể thay đổi theo từng quý, nhưng việc xây dựng một nhà máy luyện gang thép lò cao hay nhận bàn giao đội tàu bay mới lại mất từ 3 đến 5 năm**. Sự lệch pha thời gian giữa *cầu ngắn hạn* và *cung dài hạn* này sinh ra **Chu kỳ vốn (`Capital Cycle`)**:
1. Khi cầu tăng mà công suất toàn ngành chưa mở rộng kịp, tỷ lệ lấp đầy công suất vượt ngưỡng, biên lợi nhuận (`spread`) và `ROIC` tăng vọt.
2. Lợi nhuận kỷ lục kích thích các công ty trong ngành đồng loạt vay tiền mở rộng nhà máy (`CapEx boom`).
3. Ba năm sau, khi công suất mới đồng loạt đi vào vận hành thì nhu cầu đã hạ nhiệt; nguồn cung dư thừa ép giá bán rơi xuống sát biến phí, trong khi định phí khấu hao và lãi vay của nhà máy mới đè nặng lên báo cáo kết quả kinh doanh.
Nhà đầu tư không hiểu chu kỳ vốn sẽ mắc sai lầm kinh điển: **Mua cổ phiếu chu kỳ khi `P/E` nhìn có vẻ cực rẻ (`5x–6x`) ngay tại đỉnh lợi nhuận chu kỳ, và bán tháo khi `P/E` vọt lên `25x–30x` (do mẫu số lợi nhuận co lại) ngay tại đáy chu kỳ.**

---

## Ôn bài cũ

- Trong [Bài 003 — Lợi thế cạnh tranh và ROIC](003-business-quality-moat-and-roic.md) và [Bài 012 — Kịch bản và biên an toàn](012-scenarios-margin-of-safety.md), ta đã phân tích cấu trúc ngành và tâm lý chu kỳ; nếu vừa đọc [Bài 013 — Ngân hàng và công ty bảo hiểm](013-banks-insurers.md), bạn đã tách riêng nhóm tài chính. Bài 014 đi sâu vào **chu kỳ vốn (`Capital Cycle`)** của các ngành sản xuất thâm dụng tài sản cố định.

---

## Phiên 1 — Bốn lớp kinh tế đơn vị của ngành thâm dụng vốn: Giá – Lượng – Chi phí – Công suất

### 1.1. Tách bốn động lực lợi nhuận trước khi nhìn vào bội số định giá

Khi thấy doanh nghiệp báo cáo lợi nhuận hoạt động (`EBIT`) tăng mạnh, người phân tích phải mổ xẻ phương trình lợi nhuận hoạt động theo công suất:

$$\text{Sản lượng khai thác } (Q) = \text{Công suất thiết kế } (K) \times \text{Tỷ lệ lấp đầy } (u)$$
$$\text{EBIT} = Q \times (P - v) - F = (K \times u) \times \underbrace{(P - v)}_{\text{Unit Contribution / Spread}} - \underbrace{F}_{\text{Fixed Operating Costs}}$$

Trong đó: $K$ là công suất thiết kế khả dụng; $u = Q/K$ là tỷ lệ lấp đầy công suất (`Capacity Utilization / Load Factor`); $P$ là giá bán bình quân đơn vị; $v$ là chi phí biến đổi đơn vị; $c = P - v$ là phần đóng góp đơn vị (`Spread`); và $F$ là định phí vận hành trong kỳ (khấu hao, nhân sự cơ hữu, bảo dưỡng định kỳ).

Từ đó, **Điểm hòa vốn hoạt động (`Operating Breakeven`)** và **Độ bẩy hoạt động (`DOL`)** là:
$$Q_{\text{BE}} = \frac{F}{P - v}, \qquad u_{\text{BE}} = \frac{Q_{\text{BE}}}{K} = \frac{F}{K \times (P - v)}, \qquad \text{DOL} = \frac{Q \times (P - v)}{Q \times (P - v) - F} = \frac{\text{Tổng phần đóng góp}}{\text{EBIT}}$$
Khi doanh nghiệp hoạt động gần điểm hòa vốn, mẫu số `EBIT` rất nhỏ nên `DOL` cực lớn: sản lượng hoặc giá bán chỉ cần giảm `10%–15%` là lợi nhuận đổi dấu thành lỗ!

### 1.2. Kịch bản định lượng ngành Hàng không: Chuyến bay đông khách chưa chắc đã có lãi

`KỊCH_BẢN` Xét một chuyến bay thương mại có công suất $K = 180\text{ ghế}$, giá vé bình quân $P = 120\text{ USD/khách}$, biến phí $v = 40\text{ USD/khách}$ và định phí chuyến bay $F = 10.000\text{ USD/chuyến}$ (trước lãi vay và thuế).

`PHÉP_TÍNH` Ta tính điểm hòa vốn và 4 kịch bản khai thác:
- **Phần đóng góp đơn vị:** $c = 120 - 40 = 80\text{ USD/khách}$.
- **Điểm hòa vốn:** $Q_{\text{BE}} = 10.000 / 80 = 125\text{ khách}$, tương ứng hệ số lấp đầy hòa vốn $u_{\text{BE}} = 125 / 180 \approx 69{,}44\%$.

| Kịch bản | Số khách ($Q$) & Lấp đầy ($u$) | Doanh thu ($Q \times P$) | Tổng đóng góp ($Q \times c$) | Định phí ($F$) | Lợi nhuận ($\text{EBIT}$) | Nhận định phân tích |
|---|---|---|---|---|---|---|
| **Cơ sở (`Base`)** | `144 khách` ($u = 80{,}0\%$) | `17.280 USD` | `11.520 USD` | `10.000 USD` | **`+1.520 USD`** | Độ bẩy hoạt động $\text{DOL} = 11.520 / 1.520 \approx 7{,}58\text{ lần}$! |
| **Bất lợi lượng (`Volume -25%`)** | `108 khách` ($u = 60{,}0\%$) | `12.960 USD` | `8.640 USD` | `10.000 USD` | **`-1.360 USD`** | Khách giảm `25%`, nhưng `EBIT` giảm `189,5%` (đổi từ lãi sang lỗ). |
| **Thuận lợi lượng (`Volume +12,5%`)** | `162 khách` ($u = 90{,}0\%$) | `19.440 USD` | `12.960 USD` | `10.000 USD` | **`+2.960 USD`** | Khách chỉ tăng `12,5%`, nhưng `EBIT` tăng vọt `+94,74%`. |
| **Bẫy giảm giá vé (`Price -10%` ở `144 khách`)** | `144 khách` ($u = 80{,}0\%$), $P = 108\text{ USD}$ | `15.552 USD` | $144 \times 68 = 9.792\text{ USD}$ | `10.000 USD` | **`-208 USD`** | Máy bay vẫn kín `80%` ghế nhưng giảm giá vé `10%` đẩy hòa vốn lên `147,1 khách` (`81,7%`), làm chuyến bay bị lỗ! |

### 1.3. Bằng chứng thực tế từ IATA và Delta Air Lines: Lợi nhuận tăng do cầu hay do nhiên liệu rẻ?

1. `SỰ_THẬT` Theo [IATA — Strong 2025 Passenger Demand Growth Continues into 2026 (29/01/2026)](https://www.iata.org/en/pressroom/2026-releases/2026-01-29-02/), hệ số lấp đầy hành khách toàn cầu (`PLF`) năm 2025 đạt kỷ lục `83,6%`, đi kèm nút thắt giao nhận máy bay mới và bảo dưỡng làm hạn chế tốc độ tăng công suất ghế.
2. `SỰ_THẬT` Mở báo cáo [Delta Air Lines — FY2025 Form 10-K (nộp SEC ngày 11/02/2026)](https://www.sec.gov/Archives/edgar/data/27904/000002790426000013/dal-20251231.htm): Trong năm tài chính 2025, chi phí nhiên liệu máy bay của Delta giảm xuống dù tổng lượng nhiên liệu tiêu thụ tăng lên, nhờ giá nhiên liệu bình quân mỗi gallon hạ nhiệt.

`SUY_LUẬN` Hai nguồn gốc này cho thấy: (a) con số `83,6%` của IATA là mức khai thác ghế bình quân ngành, không phải điểm hòa vốn của từng hãng; và (b) khi lợi nhuận tăng nhờ **chi phí đầu vào ($v$) giảm**, đó là **lợi ích chu kỳ nguyên liệu (`input cost windfall`)** chứ không phải bằng chứng về "con hào kinh tế (`moat`)" giúp tăng quyền định giá ($P$).

> **Điểm dừng phiên 1:** Viết một dữ kiện trên BCTC giúp bác bỏ giả thuyết *"biên lợi nhuận gộp của công ty thép/nhựa tăng trong năm qua là nhờ thương hiệu mạnh hơn đối thủ"*.

---

## Phiên 2 — Cơ chế Chu kỳ vốn (`Capital Cycle`) và Nghiên cứu thực chứng Tập đoàn Hòa Phát (`HPG`)

### 2.1. Năm giai đoạn của một Chu kỳ vốn (`Capital Cycle`)

Khung phân tích **Chu kỳ vốn (`Capital Cycle`)** tập trung vào **phản ứng đầu tư công suất (`supply-side CapEx response`)** của các doanh nghiệp trong ngành qua 5 pha:
1. **Pha 1 — Hậu thanh lọc & Hạn chế nguồn cung:** Sau suy thoái, các công ty yếu dừng lò, ngân hàng siết cho vay, không có nhà máy mới khởi công. Công suất toàn ngành ($K$) đi ngang.
2. **Pha 2 — Cầu phục hồi trên nền cung cứng (`Sweet Spot`):** Nhu cầu nhích tăng trong khi chưa có nhà máy mới hoàn thành; tỷ lệ lấp đầy ($u$) vọt lên `85%–95%`, biên đóng góp (`spread`) và `ROIC` lập đỉnh.
3. **Pha 3 — Cơn sốt đầu tư mở rộng (`CapEx Boom`):** Thấy `ROIC` vượt xa `WACC`, cả ngành đồng loạt vay nợ khởi công nhà máy mới. Cổ phiếu có `P/E` trượt nhìn rất thấp (`5x–7x`).
4. **Pha 4 — Độ trễ hoàn thành & Dư cung (`Supply Glut`):** Sau 2–4 năm xây dựng, công suất mới ập vào thị trường đúng lúc cầu chững lại. Giá bán ($P$) giảm mạnh trong khi chi phí khấu hao và lãi vay (hết thời gian vốn hóa!) tăng vọt.
5. **Pha 5 — Đáy chu kỳ & Tái cân bằng (`Trough`):** Các nhà sản xuất chi phí cao (`high-cost producers`) thua lỗ tiền mặt phải đóng cửa công suất; doanh nghiệp có **chi phí sản xuất thấp nhất trên đường cong chi phí (`lowest-cost producer`)** sống sót và giành thị phần.

### 2.2. Thực hành định lượng Chu kỳ vốn trên dữ liệu thực của Hòa Phát (`HPG` 2019–2024)

Đối chiếu mô hình [cyclical.py](../practice/models/cyclical.py) và tệp dữ liệu [hpg_cycle_inputs.csv](../practice/models/hpg_cycle_inputs.csv) (từ BCTC hợp nhất kiểm toán 2019–2024 của CTCP Tập đoàn Hòa Phát):

| Năm | Pha chu kỳ | Doanh thu (`tỷ VND`) | Biên gộp (`%`) | Biên `EBIT` (`%`) | `LNST` (`tỷ VND`) | `CFO` (`tỷ VND`) | `CapEx` (`tỷ VND`) | `FCF` (`tỷ VND`) | `ROE` (`%`) |
|---|---|---|---|---|---|---|---|---|---|
| **2019** | Giữa chu kỳ (Xây Dung Quất 1) | `63.658` | `17,6%` | `15,1%` | `7.578` | `7.742` | `20.916` | `-13.174` | `17,1%` |
| **2020** | Mở rộng (Dung Quất 1 vận hành) | `90.119` | `21,0%` | `18,4%` | `13.506` | `11.531` | `11.737` | `-206` | `25,2%` |
| **2021** | **Đỉnh chu kỳ (`Peak`)** | `149.680` | **`27,5%`** | **`25,2%`** | **`34.521`** | `26.716` | `12.423` | **`+14.293`** | **`46,1%`** |
| **2022** | Suy giảm (Giá thép giảm, than/FX tăng) | `141.409` | `11,9%` | `8,8%` | `8.444` | `10.912` | `17.904` | `-6.992` | `9,1%` |
| **2023** | **Đáy chu kỳ (`Trough`, xây Dung Quất 2)** | `118.953` | **`10,9%`** | **`8,4%`** | **`6.800`** | `13.105` | `17.376` | `-4.271` | **`6,8%`** |
| **2024** | Phục hồi bước đầu | `138.855` | `13,3%` | `10,8%` | `12.020` | `6.988` | `35.172` | `-28.184` | `11,1%` |

`PHÉP_TÍNH` Kết quả chuẩn hóa xuyên chu kỳ 6 năm (`2019–2024`) từ [cyclical.py](../practice/models/cyclical.py):
- **Biên độ Đỉnh – Đáy:** `LNST` rơi từ đỉnh `34.521 tỷ VND` (2021) xuống đáy `6.800 tỷ VND` (2023), tức giảm `80,30%`!
- **Trung bình xuyên chu kỳ 6 năm:** Biên gộp bình quân = `17,03%`; Biên `EBIT` bình quân = `14,45%`; `LNST` bình quân 6 năm = `13.811,50 tỷ VND/năm`.
- **Lợi nhuận chuẩn hóa giữa chu kỳ (`Normalized mid-cycle net income`):** Áp biên lợi nhuận ròng trung bình 6 năm (`11,22%`) lên doanh thu năm 2024 (`138.855 tỷ VND`) cho mức thu nhập chuẩn hóa **`15.581,98 tỷ VND/năm`**.

> **Điểm dừng phiên 2:** Nếu lấy lợi nhuận đỉnh năm 2021 (`34.521 tỷ VND`) làm dòng tiền vĩnh viễn trong mô hình DCF, bạn đã phóng đại thu nhập chuẩn hóa (`15.582 tỷ VND`) lên gấp bao nhiêu lần?

---

## Phiên 3 — Bẫy `P/E` ngược của cổ phiếu chu kỳ và Cách chọn nhóm so sánh (`Peer Group`)

### 3.1. Giải mã nghịch lý `P/E` đỉnh và đáy chu kỳ

`PHÉP_TÍNH` Với số liệu của `HPG` trong [cyclical.py](../practice/models/cyclical.py) tại mức **Vốn hóa thị trường giả định `180.000 tỷ VND`**:
1. **`P/E` tính trên lợi nhuận Đỉnh (`2021: 34.521 tỷ VND`):** `180.000 / 34.521 ≈ 5,21 lần` (nhìn cực rẻ nhưng mẫu số `E` đang ở đỉnh siêu chu kỳ).
2. **`P/E` tính trên lợi nhuận Đáy (`2023: 6.800 tỷ VND`):** `180.000 / 6.800 ≈ 26,47 lần` (nhìn rất đắt nhưng mẫu số `E` đang bị nén ở đáy biên lợi nhuận `8,4%`).
3. **`P/E` tính trên Lợi nhuận chuẩn hóa (`15.581,98 tỷ VND`):** `180.000 / 15.581,98 ≈ 11,55 lần`.

`SUY_LUẬN` Quy tắc định giá doanh nghiệp chu kỳ ([012](012-scenarios-margin-of-safety.md) và [Q3](Q3-normalizing-earnings-cyclical.md)): **Không bao giờ nhân bội số trung bình ngành với lợi nhuận năm đỉnh (`Peak E`) hay năm đáy (`Trough E`).** Luôn định giá trên **Lợi nhuận chuẩn hóa giữa chu kỳ (`Normalized Mid-Cycle Earnings`)**.

### 3.2. Năm tiêu chí lọc Nhóm so sánh (`Peer Group`)

Trước khi lấy trung bình bội số một ngành, phải kiểm tra 5 lớp tương đồng kinh tế:

| Tiêu chí lọc `Peer Group` | Sai lầm khi gom chung | Cách tách đúng theo Kinh tế ngành |
|---|---|---|
| **1. Vị trí chuỗi giá trị & Công nghệ** | Gom công ty luyện thép lò cao từ quặng (`BF/BOF` như HPG) chung với công ty chỉ nhập `HRC` về cán/mạ tôn (HSG, NKG). | Lò cao phụ thuộc `Spread = Thép − (Quặng + Than cốc)`; công ty tôn mạ phụ thuộc `Tôn − HRC` và đầu cơ tồn kho `HRC`. |
| **2. Vị thế trên Đường cong chi phí (`Cost Curve`)** | Coi nhà máy nhỏ tiêu hao năng lượng cao ngang với tổ hợp lớn có cảng nước sâu và tự chủ điện nhiệt dư. | Ở đáy chu kỳ, nhà sản xuất chi phí thấp nhất (`1st quartile`) vẫn có `EBITDA` dương, còn phân vị chi phí cao nhất (`4th quartile`) lỗ tiền mặt. |
| **3. Pha đầu tư `CapEx`** | So trực tiếp `FCF` của công ty đang dồn `35.172 tỷ VND CapEx` xây nhà máy mới với công ty không đầu tư mới. | Tách riêng `Maintenance CapEx` và `Expansion CapEx`; cộng công suất mới khi dự án đi vào vận hành. |
| **4. Cơ cấu hợp đồng (`Spot` vs `Time Charter`)** | So hãng tàu chạy giá giao ngay (`Spot`) với hãng ký hợp đồng định hạn dài hạn (`Time Charter`). | Hãng chạy `Spot` biến động lợi nhuận tức thời; hãng `Time Charter` có độ trễ tái ký hợp đồng. |
| **5. Đòn bẩy tài chính** | Chỉ nhìn `P/E` mà bỏ qua chênh lệch nợ vay ròng. | Ưu tiên dùng `EV/Normalized EBITDA` hoặc `EV/Installed Capacity` thay vì chỉ dùng `P/E`. |

> **Điểm dừng phiên 3:** Mở [cyclical.py](../practice/models/cyclical.py): Vì sao năm 2024 `LNST` của HPG đạt `12.020 tỷ VND` nhưng `FCF` lại âm `-28.184 tỷ VND`?

---

## Ví dụ từ nguồn thật

1. **Dữ liệu công suất và hệ số lấp đầy ngành hàng không toàn cầu của IATA:**
   `SỰ_THẬT` Mở [IATA — Strong 2025 Passenger Demand Growth Continues into 2026 (29/01/2026)](https://www.iata.org/en/pressroom/2026-releases/2026-01-29-02/): Hệ số lấp đầy hành khách toàn cầu (`PLF`) năm 2025 đạt `83,6%` trong bối cảnh nguồn cung tàu bay mới bị hạn chế bởi chuỗi cung ứng sản xuất và bảo dưỡng.
2. **Báo cáo thường niên Form 10-K năm 2025 của Delta Air Lines:**
   `SỰ_THẬT` Mở [Delta Air Lines — FY2025 Form 10-K (11/02/2026)](https://www.sec.gov/Archives/edgar/data/27904/000002790426000013/dal-20251231.htm): Chi phí nhiên liệu năm 2025 giảm dù lượng tiêu thụ tăng, chứng minh lợi nhuận một năm có thể cải thiện nhờ giá đầu vào hạ nhiệt thay vì tăng sức mạnh định giá.
3. **Dữ liệu chu kỳ 2019–2024 của Tập đoàn Hòa Phát (`HPG`):**
   `SỰ_THẬT` Đối chiếu [cyclical.py](../practice/models/cyclical.py) và [hpg_cycle_inputs.csv](../practice/models/hpg_cycle_inputs.csv): Biên gộp HPG dao động từ đỉnh `27,5%` (2021) xuống đáy `10,9%` (2023) và phục hồi lên `13,3%` (2024).

---

## Bài tập

Hãy tự giải 10 bài tập dưới đây trước khi mở phần Đáp án:

1. **Tính điểm hòa vốn và tỷ lệ lấp đầy hòa vốn của chuyến bay:** Chuyến bay `180 ghế`, giá vé `120 USD/khách`, biến phí `40 USD/khách`, định phí `10.000 USD`. Tính: (a) phần đóng góp đơn vị (`c`), (b) số khách hòa vốn (`Q_BE`), và (c) hệ số lấp đầy hòa vốn (`u_BE`).
2. **Đòn bẩy hoạt động (`DOL`):** Tiếp nối Bài tập 1, tính `EBIT` ở mức `144 khách` (`80%` ghế) và `108 khách` (`60%` ghế), cùng độ bẩy hoạt động `DOL` tại mức `144 khách`.
3. **Độ nhạy giá bán (`Price -10%`):** Giữ nguyên `144 khách`, biến phí `40 USD`, định phí `10.000 USD`, nhưng giảm giá vé `10%` (xuống `108 USD/khách`). Tính `EBIT` mới và số khách hòa vốn mới.
4. **Hiệu ứng chi phí đầu vào giảm (`Input cost windfall`):** Giữ `144 khách`, giá vé `120 USD`, định phí `10.000 USD`, nhưng biến phí giảm từ `40` xuống `30 USD/khách`. Tính `EBIT` mới và giải thích vì sao mức tăng này không chứng minh lợi thế thương hiệu bền vững.
5. **Kinh tế đơn vị và điểm hòa vốn nhà máy thép lò cao:** Liên hợp thép có công suất $K = 5{,}0\text{ triệu tấn/năm}$, định phí $F = 6.000\text{ tỷ VND/năm}$, giá bán $P = 15{,}0\text{ triệu VND/tấn}$, biến phí $v = 12{,}6\text{ triệu VND/tấn}$. Tính: (a) biên đóng góp `spread` (triệu VND/tấn), (b) sản lượng hòa vốn $Q_{\text{BE}}$ và tỷ lệ vận hành hòa vốn $u_{\text{BE}}$, (c) `EBIT` khi chạy `90%` công suất ($Q = 4{,}5\text{ triệu tấn}$).
6. **Cú sốc kép thu hẹp `Spread` và giảm công suất thép:** Tiếp nối Bài tập 5, sang năm suy thoái, giá thép giảm còn `13,8 triệu VND/tấn`, biến phí giảm nhẹ còn `12,3 triệu VND/tấn` (`spread = 1,5 triệu VND/tấn`), sản lượng giảm còn `3,6 triệu tấn` ($u = 72\%$), định phí `6.000 tỷ VND`. Tính `EBIT` mới và tỷ lệ công suất hòa vốn mới.
7. **Biên lợi nhuận xuyên chu kỳ của `HPG` (`2019–2024`):** Từ biên `EBIT` 6 năm của `HPG` (`15,1%`, `18,4%`, `25,2%`, `8,8%`, `8,4%`, `10,8%`), tính biên `EBIT` trung bình 6 năm và độ lệch của năm đỉnh `2021` và năm đáy `2023` so với mức trung bình.
8. **Tránh bẫy `P/E` đỉnh và đáy chu kỳ:** Công ty hóa chất có vốn hóa `24.000 tỷ VND`, lợi nhuận đỉnh năm ngoái `4.800 tỷ VND`, lợi nhuận đáy năm nay `800 tỷ VND`, và lợi nhuận chuẩn hóa giữa chu kỳ `2.000 tỷ VND/năm`. Tính `P/E` đỉnh, `P/E` đáy và `P/E` chuẩn hóa.
9. **Độ trễ đầu tư công suất (`CapEx lag`):** Ngành vật liệu có công suất `100 triệu tấn/năm`, cầu `92 triệu tấn/năm` (`u = 92%`). Có 5 công ty đồng loạt xây nhà máy mới (mỗi nhà máy `6 triệu tấn/năm`, tổng thêm `30 triệu tấn/năm`), mất `3 năm` hoàn thành. Nếu sau 3 năm tổng cầu chỉ tăng `+10%` (lên `101,2 triệu tấn`), tỷ lệ lấp đầy toàn ngành sẽ rơi từ `92%` xuống bao nhiêu?
10. **Vị thế trên Đường cong chi phí (`Cost Curve`) ở đáy chu kỳ:** Công ty A có tổng chi phí `420 USD/tấn` (biến phí tiền mặt `340 USD`, khấu hao `80 USD`). Công ty B có tổng chi phí `510 USD/tấn` (biến phí tiền mặt `460 USD`, khấu hao `50 USD`). Khi giá bán rơi xuống `440 USD/tấn`, tính `EBIT/tấn` và `EBITDA/tấn` của A và B, giải thích vì sao B phải đóng cửa lò trước.

---

## Đáp án

1. **Hòa vốn chuyến bay:**
   - `PHÉP_TÍNH` (a) `c = 120 − 40 = 80 USD/khách`. (b) `Q_BE = 10.000 / 80 = 125 khách`. (c) `u_BE = 125 / 180 ≈ 69,44%`.
2. **Đòn bẩy hoạt động (`DOL`):**
   - `PHÉP_TÍNH` Tại `144 khách`: `EBIT = 144 × 80 − 10.000 = +1.520 USD`; `DOL = 11.520 / 1.520 ≈ 7,58 lần`. Tại `108 khách`: `EBIT = 108 × 80 − 10.000 = −1.360 USD`.
3. **Độ nhạy giá bán (`Price -10%`):**
   - `PHÉP_TÍNH` `c' = 108 − 40 = 68 USD/khách` → `EBIT` mới = `144 × 68 − 10.000 = −208 USD`. Hòa vốn mới = `10.000 / 68 ≈ 147,06 khách` (`148 khách`, tức `82,22%` ghế).
4. **Hiệu ứng chi phí đầu vào giảm:**
   - `PHÉP_TÍNH` `c' = 120 − 30 = 90 USD/khách` → `EBIT` mới = `144 × 90 − 10.000 = +2.960 USD`. Mức tăng đến từ giá nhiên liệu giảm chung cho toàn ngành, không phải do quyền định giá vé cao hơn.
5. **Nhà máy thép (năm cơ sở):**
   - `PHÉP_TÍNH` (a) `Spread = 15,0 − 12,6 = 2,40 triệu VND/tấn`. (b) `Q_BE = 6.000 / 2,40 = 2,50 triệu tấn` (`u_BE = 50,00%`). (c) `EBIT` tại `4,5 triệu tấn`: `4,5 × 2.400 − 6.000 = +4.800 tỷ VND`.
6. **Cú sốc kép ngành thép:**
   - `PHÉP_TÍNH` `Spread` mới = `1,50 triệu VND/tấn` → `EBIT` tại `3,6 triệu tấn` = `3,6 × 1.500 − 6.000 = −600 tỷ VND`. Công suất hòa vốn mới = `6.000 / 1.500 = 4,00 triệu tấn` (`u_BE = 80,00%`).
7. **Biên `EBIT` xuyên chu kỳ `HPG`:**
   - `PHÉP_TÍNH` Trung bình 6 năm: `(15,1 + 18,4 + 25,2 + 8,8 + 8,4 + 10,8) / 6 = 14,45%` (khớp [cyclical.py](../practice/models/cyclical.py)). Năm đỉnh `2021` lệch `+10,75 điểm %`; năm đáy `2023` lệch `−6,05 điểm %`.
8. **Bẫy `P/E` đỉnh/đáy và `P/E` chuẩn hóa:**
   - `PHÉP_TÍNH` `P/E` đỉnh = `24.000 / 4.800 = 5,00x`; `P/E` đáy = `24.000 / 800 = 30,00x`; `P/E` chuẩn hóa = `24.000 / 2.000 = 12,00x`.
9. **Độ trễ đầu tư công suất (`CapEx lag`):**
   - `PHÉP_TÍNH` Công suất mới sau 3 năm = `100 + 30 = 130 triệu tấn`. Tỷ lệ lấp đầy mới = `101,2 / 130 ≈ 77,85%` (dư cung `28,8 triệu tấn`).
10. **Đường cong chi phí (`Cost Curve`):**
    - `PHÉP_TÍNH` Tại giá `440 USD/tấn`: Công ty A có `EBIT = +20 USD/tấn`, `EBITDA = +100 USD/tấn`. Công ty B có `EBIT = −70 USD/tấn`, và **`EBITDA = 440 − 460 = −20 USD/tấn`** (lỗ tiền mặt trực tiếp trên mỗi tấn sản xuất nên buộc phải đóng cửa lò trước).

---

## Bài làm với dữ liệu thiếu hoặc lệch

Khi phân tích kinh tế ngành tại Việt Nam, bạn thường gặp hai khoảng trống dữ liệu:
1. **Báo cáo kết quả kinh doanh gộp chung biến phí và định phí vào "Giá vốn hàng bán (`COGS`)"**: Không tách sẵn $v$ và $F$ trên mặt bảng chính.
2. **Công suất khả dụng thực tế khác công suất thiết kế trên giấy phép** do thời gian dừng lò bảo dưỡng hoặc nút thắt nguyên liệu.

**Quy trình xử lý chuẩn Bậc S:**
- **Bước 1 — Mở Thuyết minh "Chi phí sản xuất, kinh doanh theo yếu tố":** Dùng dòng "Chi phí nguyên liệu, vật liệu" làm hạt nhân ước lượng biến phí ($v$), và dòng "Chi phí khấu hao TSCĐ" cộng nhân công quản lý làm hạt nhân ước lượng định phí ($F$).
- **Bước 2 — Chuẩn hóa biên lợi nhuận đa niên bằng [cyclical.py](../practice/models/cyclical.py):** Lấy chuỗi 5–7 năm bao trùm cả đỉnh và đáy chu kỳ (như [hpg_cycle_inputs.csv](../practice/models/hpg_cycle_inputs.csv)) để tính biên lợi nhuận giữa chu kỳ (`Mid-cycle margin`).
- **Bước 3 — Gắn nhãn `CHƯA_BIẾT` với tốc độ lấp đầy dự án mới (`Ramp-up`):** Theo dõi tiến độ kết chuyển từ "Xây dựng cơ bản dở dang" sang "Tài sản cố định hữu hình" và lập kịch bản tỷ lệ vận hành năm đầu tiên.

---

## Sai ở đâu

### Sai lầm 1: Nhân bội số `P/E = 10x–12x` vào lợi nhuận năm đỉnh chu kỳ (`Peak Earnings`)
- **Bối cảnh:** Giữa năm 2021, nhiều người lấy `EPS` đỉnh lịch sử của ngành thép/phân bón nhân với `P/E = 10x` vì tưởng `P/E = 5x–6x` lúc đó là rẻ.
- **Sai ở đâu:** Đồng nhất **lợi nhuận đỉnh chu kỳ (`Peak EBIT margin = 25,2%`)** với thu nhập bền vững vĩnh viễn.
- **Cách sửa:** Định giá trên **Lợi nhuận chuẩn hóa xuyên chu kỳ (`Normalized Mid-Cycle Earnings`)** qua [cyclical.py](../practice/models/cyclical.py).

### Sai lầm 2: Nhầm lợi nhuận tăng nhờ giá nguyên liệu đầu vào giảm với "lợi thế cạnh tranh bền vững (`Moat`)"
- **Bối cảnh:** Thấy biên gộp tăng trong năm giá dầu/nhựa/nhiên liệu giảm liền trả bội số định giá cao hơn vĩnh viễn.
- **Sai ở đâu:** Không tách biến động chi phí đầu vào ($v$) với quyền định giá ($P$) như đã chứng minh ở [Delta Form 10-K (2026)](https://www.sec.gov/Archives/edgar/data/27904/000002790426000013/dal-20251231.htm).
- **Cách sửa:** Kiểm tra khả năng giữ biên lợi nhuận trên mỗi tấn sản phẩm khi giá nguyên liệu đầu vào tăng ngược trở lại.

### Sai lầm 3: Lấy hệ số lấp đầy toàn ngành áp thẳng làm điểm hòa vốn của một công ty đơn lẻ
- **Bối cảnh:** Thấy `PLF` toàn cầu đạt `83,6%` ([IATA, 2026](https://www.iata.org/en/pressroom/2026-releases/2026-01-29-02/)) liền suy ra mọi hãng bay lấp đầy trên `80%` đều có lãi lớn.
- **Sai ở đâu:** Bỏ qua sự khác biệt về giá vé bình quân ($P$) và định phí thuê tàu bay/lãi vay ($F$) giữa từng hãng.
- **Cách sửa:** Tính riêng $u_{\text{BE}} = F / [K \times (P - v)]$ cho từng doanh nghiệp.

---

## Kiểm tra chuyển bài

Trước khi chuyển sang bài [012](012-scenarios-margin-of-safety.md), [016](016-company-research-capstone.md) và [N2](N2-statement-line-items.md), hãy trả lời 3 câu hỏi dưới đây:

1. **Chuyển giao sang Định giá kịch bản ([012](012-scenarios-margin-of-safety.md)):** Khi lập 3 kịch bản cho doanh nghiệp chu kỳ như `HPG`, vì sao phải cho cả tỷ lệ vận hành công suất ($u$) và biên đóng góp ($P - v$) biến động đồng thời?
2. **Chuyển giao sang Kế toán TSCĐ & Lãi vay ([N2](N2-statement-line-items.md), [N3](N3-vietnam-vas-statements.md)):** Khi tổ hợp nhà máy mới chuyển từ "Xây dựng cơ bản dở dang" sang vận hành thương mại năm đầu với tỷ lệ lấp đầy `50%`, điều gì xảy ra ngay với **Chi phí khấu hao** và **Chi phí lãi vay** trên Báo cáo kết quả kinh doanh?
3. **Kết nối với bài [M3](M3-capital-trade-geopolitics.md):** Khi ngành thép/hóa chất nước láng giềng dư thừa công suất (`014`) và xuất khẩu giá rẻ sang Đông Nam Á, chính sách Phòng vệ thương mại (`M3`) đóng vai trò gì trong việc bảo vệ biên lợi nhuận nội địa?

---

## Nguồn Internet đã mở

- Truy cập `2026-10-26` và kiểm tra đối chiếu `2026-11-05`:
  1. [IATA — Strong 2025 Passenger Demand Growth Continues into 2026 (29/01/2026)](https://www.iata.org/en/pressroom/2026-releases/2026-01-29-02/) — công bố hệ số lấp đầy hành khách toàn cầu năm 2025 đạt `83,6%` kèm hạn chế chuỗi cung ứng tàu bay.
  2. [Delta Air Lines — FY2025 Form 10-K (11/02/2026)](https://www.sec.gov/Archives/edgar/data/27904/000002790426000013/dal-20251231.htm) — BCTC kiểm toán kỳ `31/12/2025` theo US GAAP; phản chứng lợi nhuận cải thiện nhờ chi phí nhiên liệu giảm.
  3. Chuỗi dữ liệu chu kỳ `HPG` (2019–2024) lưu tại [hpg_cycle_inputs.csv](../practice/models/hpg_cycle_inputs.csv) và mô hình [cyclical.py](../practice/models/cyclical.py).
- Các thông số chuyến bay 180 ghế và nhà máy thép 5 triệu tấn được gắn nhãn `KỊCH_BẢN`.
