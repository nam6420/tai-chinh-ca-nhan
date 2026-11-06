# Bài N4 — Giá trị thời gian của tiền và lợi suất

- Ngày: `2026-11-06`
- Chốt dữ liệu lúc: `2026-11-06 10:35 UTC+7 (Asia/Ho_Chi_Minh)`
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Mục tiêu: Hiểu vì sao một đồng nhận hôm nay khác một đồng nhận trong tương lai; tính từng bước **Giá trị tương lai (`FV` — lãi kép)**, **Giá trị hiện tại (`PV` — chiết khấu)**, **Lãi suất danh nghĩa so với Lãi suất hiệu dụng năm (`EAR`)**, **Lợi suất thực sau lạm phát (`Real Return`)**, **Tốc độ tăng trưởng kép hàng năm (`CAGR`)** và **Bài toán góp tiền định kỳ hàng tháng**; nhận biết giới hạn khi có dòng tiền góp/rút giữa kỳ.
- Thời lượng: Ba phiên học ngắn (Phiên 1: Đi xuôi bằng lãi kép `FV` và đi ngược bằng chiết khấu `PV`; Phiên 2: Tần suất ghép lãi, lạm phát và sức mua thực; Phiên 3: `CAGR` trên dữ liệu thật Apple FY2025 và góp đều hàng tháng) + thực hành với [market_returns.py](../practice/models/market_returns.py).
- Bài trước liên quan:
  - **Nhánh 1 (Phân tích doanh nghiệp — Thứ tự đọc 8/23):** Học ngay sau [Bài 002: Hiểu và tìm một cổ phiếu đang được định giá rẻ](002-finding-a-cheap-stock.md). Học tiếp: [Bài 003: Chất lượng doanh nghiệp — lợi thế cạnh tranh, ROIC và khả năng tái đầu tư](003-business-quality-moat-and-roic.md).
  - **Nhánh 2 (Nhà đầu tư cá nhân và quỹ chỉ số):** Học sau [Bài N1: Thị trường vốn](N1-market-basics.md) và [Bài N5 (Phần A): Đầu tư quỹ chỉ số](N5-portfolio-index-investing.md). Học tiếp: [Bài N5 (Phần B)](N5-portfolio-index-investing.md) hoặc [Bài N7: Dữ liệu, xác suất và bất định](N7-data-probability-uncertainty.md).
- Câu hỏi cốt lõi: **Một khoản tiền hứa trả trong tương lai tương đương bao nhiêu tiền mặt cầm trên tay ngày hôm nay — và làm sao đo đúng lợi suất khi có lạm phát hoặc góp thêm tiền?**

> Đây là bài học nền tảng toàn cầu, không phải khuyến nghị mua, bán hay nắm giữ chứng khoán. Các mức lãi suất và tỷ suất sinh lời trong bài chỉ là giả định toán học để luyện tư duy, không phải mức sinh lời được cam kết trên thị trường.

---

## Hiểu bài này trong 1 phút

Hãy tự hỏi: Nếu ai đó cho bạn chọn nhận **`100 triệu đồng` ngay hôm nay** hoặc nhận **`100 triệu đồng` sau `3 năm` nữa**, bạn chọn bên nào?

Mọi người đều chọn nhận `100 triệu đồng` ngay hôm nay vì ba lý do rất đời thường:
1. **Chi phí cơ hội sử dụng tiền (`Opportunity Cost`):** Có `100 triệu` hôm nay, bạn có thể đem gửi tiết kiệm hoặc đầu tư vào Quán cà phê Sao Biển để sinh ra tiền lãi trong suốt 3 năm đó.
2. **Lạm phát (`Inflation`):** Sau 3 năm, giá bát phở hay ly cà phê có thể đã tăng lên; `100 triệu` của 3 năm sau mua được ít hàng hóa hơn `100 triệu` hôm nay.
3. **Rủi ro (`Risk`):** Lời hứa trả tiền sau 3 năm luôn có xác suất bị trễ hẹn hoặc không trả đủ.

Vì tiền ở các thời điểm khác nhau không có giá trị bằng nhau, bạn không được phép lấy tiền của năm 2028 cộng thẳng với tiền của năm 2026 như cộng hai quả táo cùng rổ. Muốn so sánh hoặc cộng chúng lại, ta cần hai phép quy đổi ngược chiều nhau:
- **Đi xuôi từ hiện tại tới tương lai — Lãi kép (`Compounding`):** Nhân vốn ban đầu (`PV`) với hệ số sinh lời qua từng kỳ để tìm số tiền trong tương lai (`FV`).
- **Đi ngược từ tương lai về hiện tại — Chiết khấu (`Discounting`):** Chia khoản tiền tương lai (`FV`) cho hệ số đó để biết nó tương đương bao nhiêu tiền ngày hôm nay (`PV`).

> Câu cần nhớ: **Lãi kép đưa tiền hôm nay tới tương lai bằng phép nhân; chiết khấu kéo tiền tương lai về hôm nay bằng phép chia. Trước khi cộng hay so sánh hai khoản tiền, bắt buộc phải đưa chúng về cùng một mốc thời gian và cùng một đơn vị sức mua.**

---

## Ôn bài cũ hoặc kiểm tra đầu vào

- **Nối từ [Bài 002](002-finding-a-cheap-stock.md) (Nhánh 1):** Ở cuối Bài 002, chúng ta đã biết một cổ phiếu chỉ thực sự "rẻ" khi tổng giá mua doanh nghiệp (`Market Cap` / `EV`) thấp hơn giá trị của những dòng tiền mà doanh nghiệp tạo ra trong tương lai. Nhưng dòng tiền của Quán cà phê Sao Biển hay của Apple lại chảy về rải rác ở năm thứ 1, năm thứ 2, năm thứ 5... Bài `N4` này chính là chiếc cầu toán học giúp bạn quy đổi các khoản tiền tương lai đó về hiện tại (`PV`) trước khi học sâu về hiệu quả vốn `ROIC` ([Bài 003](003-business-quality-moat-and-roic.md)) và mô hình chiết khấu dòng tiền `DCF` ([Bài 010](010-cost-of-capital.md)–[Bài 011](011-dcf-reverse-dcf.md)).
- **Nối từ [Bài N1](N1-market-basics.md) và [Bài N5](N5-portfolio-index-investing.md) (Nhánh 2):** Nếu bạn đang đi theo lộ trình quỹ chỉ số (chưa học kế toán doanh nghiệp), bạn chỉ cần nắm 3 con số đầu vào: **Số tiền ban đầu**, **Số tiền cuối kỳ (hoặc góp thêm)** và **Số kỳ thời gian** để đo đúng tốc độ tăng trưởng tài sản cá nhân.

### Bài này làm gì và chưa làm gì?
- **Bài này làm:** Dạy cách tính `FV`, `PV`, đổi lãi suất giữa năm và tháng, tính lợi suất thực sau lạm phát, tính `CAGR` và mô phỏng góp tiền đều đặn hàng tháng.
- **Bài này chưa làm:** Chưa dạy cách chọn tỷ lệ chiết khấu (`WACC` hay `k_e`) phù hợp với mức độ rủi ro của từng cổ phiếu cụ thể — việc đó sẽ học ở [Bài 010: Chi phí vốn](010-cost-of-capital.md).

---

## Phiên 1 — Tiền đẻ ra tiền: Lãi kép (`FV`) và phép đi ngược thời gian (`PV`)

### 1. Lãi kép (`Compounding`): Vì sao 2 năm lãi `10%/năm` lại tăng `21%` chứ không phải `20%`?

`SỰ_THẬT` Tài liệu giáo dục của [California State Board of Equalization (BOE — Lesson 1)](https://www.boe.ca.gov/info/tvm/lesson1.html) trình bày nguyên lý cơ bản của giá trị thời gian của tiền: với lãi kép, tiền lãi của kỳ trước được cộng gộp vào vốn gốc để cùng sinh lãi trong kỳ tiếp theo (`lãi mẹ đẻ lãi con`).

`KỊCH_BẢN` Giả sử Quán cà phê Sao Biển có `100 triệu đồng` tiền nhàn rỗi (`PV = 100`), gửi vào một khoản đầu tư sinh lời cố định `r = 10%/năm` (`0,10`) trong `n = 2 năm`, không rút tiền lãi ra giữa chừng và chưa tính thuế/phí. Hãy tính từng bước:
- `PHÉP_TÍNH` **Cuối năm thứ 1:** Tiền gốc `100 triệu` sinh ra `100 × 10% = 10 triệu` tiền lãi. Tổng số dư cuối năm 1 là:
  $$\text{FV}_1 = 100 \times (1 + 0,10) = 110 \text{ triệu đồng}$$
- `PHÉP_TÍNH` **Cuối năm thứ 2:** Toàn bộ `110 triệu` (gồm `100 triệu` gốc ban đầu và `10 triệu` lãi năm 1) tiếp tục sinh lời `10%`:
  $$\text{FV}_2 = 110 \times (1 + 0,10) = 100 \times (1,10)^2 = 121 \text{ triệu đồng}$$

Bạn thấy tổng mức tăng sau 2 năm là `21 triệu đồng` (tức **`+21%`**), lớn hơn con số `20 triệu` của lãi đơn (`10% × 2`). Phần chênh thêm `1 triệu đồng` chính là **`10%` lãi sinh ra trên `10 triệu` tiền lãi của năm đầu tiên**!

Tổng quát cho một khoản đầu tư đơn lẻ sau $n$ kỳ với tỷ lệ sinh lời cố định $r$ mỗi kỳ (không góp thêm hay rút bớt giữa kỳ):

$$\text{FV} = \text{PV} \times (1 + r)^n$$

*(Lưu ý: Nếu tỷ lệ sinh lời thay đổi qua từng năm là $r_1, r_2, \dots, r_n$, ta nhân nối tiếp $\text{FV} = \text{PV} \times (1 + r_1) \times (1 + r_2) \cdots (1 + r_n)$).*

### 2. Đi ngược thời gian — Chiết khấu (`Discounting`): Tìm Giá trị hiện tại (`PV`)

Bây giờ hãy lật ngược câu hỏi: Giả sử một đối tác hứa trả cho Quán cà phê Sao Biển **`121 triệu đồng` sau `2 năm` nữa** (`FV = 121`, `n = 2`). Nếu bạn đòi hỏi mức sinh lời `r = 10%/năm`, thì lời hứa `121 triệu` đó đáng giá bao nhiêu tiền ngay hôm nay (`PV`)?

Chỉ cần chia ngược phương trình lãi kép cho $(1 + r)^n$:

$$\text{PV} = \frac{\text{FV}}{(1 + r)^n}$$

- `PHÉP_TÍNH` Với $r = 10\%/\text{năm}$ (`0,10`):
  $$\text{PV} = \frac{121}{(1 + 0,10)^2} = \frac{121}{1,21} = 100 \text{ triệu đồng}$$
- `PHÉP_TÍNH` Điều gì xảy ra nếu bạn thấy đối tác này rủi ro hơn (hoặc lãi suất ngoài thị trường tăng lên), nên bạn đòi hỏi tỷ lệ chiết khấu cao hơn là **`r = 12%/năm`** (`0,12`) cho cùng khoản tiền `121 triệu` sau 2 năm?
  $$\text{PV (ở mức } r = 12\%) = \frac{121}{(1 + 0,12)^2} = \frac{121}{1,2544} \approx 96,46 \text{ triệu đồng}$$

`SUY_LUẬN` Quy luật ngược chiều cực kỳ quan trọng của định giá: **Khi giữ nguyên khoản tiền tương lai dương (`FV`), tỷ lệ chiết khấu `r` càng cao (hoặc thời gian chờ `n` càng dài) thì Giá trị hiện tại (`PV`) càng thấp!**

### 3. Kiểm tra bằng phép tính ngược trên trục thời gian 3 năm

`KỊCH_BẢN` Một hợp đồng hứa trả `150 triệu đồng` sau `3 năm` (`FV = 150`, `n = 3`). Giả sử để luyện toán ta dùng tỷ lệ chiết khấu `r = 8%/năm` (`0,08`):
- `PHÉP_TÍNH` Bước 1 — Tính mẫu số lũy thừa: $(1 + 0,08)^3 = 1,08^3 = 1,259712$.
- `PHÉP_TÍNH` Bước 2 — Chia để tìm `PV`:
  $$\text{PV} = \frac{150}{1,259712} \approx 119,0748 \text{ triệu đồng (làm tròn } 119,07 \text{ triệu đồng)}$$
- `PHÉP_TÍNH` Bước 3 — Kiểm ngược lại `FV` (dùng số chưa làm tròn như hàm `present_value` và `future_value` trong [market_returns.py](../practice/models/market_returns.py)):
  $$119,0748 \times 1,08^3 = 150,00 \text{ triệu đồng}$$
- Nếu đổi tỷ lệ chiết khấu lên `10%/năm`, mẫu số tăng lên $1,10^3 = 1,331$, kéo `PV` giảm xuống còn $150 / 1,331 \approx 112,70 \text{ triệu đồng}$.

> **Điểm dừng Phiên 1:** Hãy vẽ một trục thời gian từ mốc `0 → 1 → 2 → 3`. Đặt `150 triệu` ở mốc `3` và `119,07 triệu` ở mốc `0`. Hãy nhớ: một phép tính `PV` đúng công thức vẫn sẽ sai về mặt kinh tế nếu con số `150 triệu` chỉ là "doanh thu dự kiến" (chưa trừ chi phí) hoặc đối tác có nguy cơ vỡ nợ không trả được tiền!

---

## Phiên 2 — Tỷ lệ sinh lời mỗi kỳ, Tần suất ghép lãi và Sức mua thực sau lạm phát

### 1. Lợi suất một kỳ, lợi suất nhiều kỳ và lợi suất thực (`Real Return`)

`PHÉP_TÍNH` Khi không có tiền góp thêm hay rút ra giữa kỳ:
1. **Lợi suất tổng cộng 1 kỳ (`Total Return` — gồm cả cổ tức tiền mặt nhận được trong kỳ và giữ riêng không tái đầu tư):**
   $$\text{Lợi suất 1 kỳ} = \frac{\text{Giá cuối kỳ} - \text{Giá đầu kỳ} + \text{Cổ tức tiền mặt}}{\text{Giá đầu kỳ}}$$
   *Ví dụ:* Mua cổ phiếu giá `50`, cuối năm giá lên `52` và nhận cổ tức `3` (cùng đơn vị) $\implies \text{Lợi suất} = \frac{52 - 50 + 3}{50} = \frac{5}{50} = 10\%$.
2. **Tốc độ tăng trưởng kép theo năm (`CAGR`) khi đi qua nhiều năm:**
   Từ `100 triệu` lên `121 triệu` sau `2 năm`, tốc độ tăng kép mỗi năm là:
   $$\text{CAGR} = \left(\frac{121}{100}\right)^{\frac{1}{2}} - 1 = \sqrt{1,21} - 1 = 1,10 - 1 = 10\%/\text{năm}$$
   *(Tuyệt đối không lấy tổng mức tăng `21%` chia `2` để nói lợi suất là `10,5%/năm`!).*
3. **Lợi suất thực sau khi trừ lạm phát (`Real Return`):**
   `SỰ_THẬT` Theo [Cục Thống kê Lao động Hoa Kỳ (BLS — CPI FAQ)](https://www.bls.gov/cpi/questions-and-answers.htm), chỉ số giá tiêu dùng (`CPI`) đo mức thay đổi giá của một rổ hàng hóa và dịch vụ đại diện. Nếu tài khoản của bạn tăng danh nghĩa $r_{\text{danh nghĩa}}$ nhưng giá rổ hàng hóa tăng theo tỷ lệ lạm phát $i$, thì **sức mua thực tế** tăng theo công thức Fisher:
   $$\text{Lợi suất thực} = \frac{1 + r_{\text{danh nghĩa}}}{1 + i} - 1$$
   - `PHÉP_TÍNH` *Ví dụ 1:* Lợi suất danh nghĩa `10%/năm` (`0,10`), lạm phát `5%/năm` (`0,05`) $\implies \text{Lợi suất thực} = \frac{1,10}{1,05} - 1 \approx 4,76\%$ (không phải phép trừ thô `10% − 5% = 5%`!).
   - `PHÉP_TÍNH` *Ví dụ 2:* Tài khoản tăng `8%` (`0,08`), lạm phát rổ chi tiêu là `4%` (`0,04`) $\implies \text{Lợi suất thực} = \frac{1,08}{1,04} - 1 \approx 3,85\%$. Nhưng nếu lạm phát vọt lên `10%`, sức mua của bạn bị **âm**: $\frac{1,08}{1,10} - 1 \approx -1,82\%$ dù số tiền danh nghĩa trong tài khoản vẫn tăng!

### 2. Phân biệt Lãi suất danh nghĩa niêm yết (`Nominal Rate`) và Lãi suất hiệu dụng năm (`Effective Annual Rate — EAR`)

`SỰ_THẬT` [California BOE — Lesson 9](https://www.boe.ca.gov/info/tvm/lesson9.html) giải thích rất rõ sự khác biệt khi tiền lãi được nhập gốc nhiều lần trong một năm (ví dụ ghép lãi hàng tháng hoặc hàng quý):

- **Trường hợp A — Cho lãi suất danh nghĩa năm $j = 12\%/\text{năm}$, ghép lãi hàng tháng ($m = 12$ lần/năm):**
  Theo quy ước hợp đồng danh nghĩa, lãi suất mỗi tháng là $\frac{j}{m} = \frac{12\%}{12} = 1\%/\text{tháng}$ (`0,01`). Sau 12 tháng nhập gốc liên tiếp, `1 đồng` vốn biến thành $(1 + 0,01)^{12} \approx 1,126825 \text{ đồng}$. Như vậy, **lãi suất hiệu dụng năm (`EAR`)** thực tế là:
  $$\text{EAR} = \left(1 + \frac{j}{m}\right)^m - 1 = (1 + 0,01)^{12} - 1 \approx 12,6825\%/\text{năm}$$
- **Trường hợp B — Cho sẵn lãi suất hiệu dụng năm $\text{EAR} = 12\%/\text{năm}$, muốn tìm tỷ lệ sinh lời mỗi tháng tương đương:**
  Lúc này bạn **không được chia thẳng cho 12**, mà phải lấy căn bậc 12 (như hàm `equivalent_period_rate(0.12, 12)` trong [market_returns.py](../practice/models/market_returns.py)):
  $$r_{\text{tháng}} = (1 + 0,12)^{\frac{1}{12}} - 1 \approx 0,9489\%/\text{tháng}$$
  *(Kiểm lại: $(1 + 0,009489)^{12} - 1 = 12,00\%/\text{năm}$!).*

Hãy nhớ thêm: Nếu ngân hàng "trả lãi hàng tháng vào tài khoản thanh toán và bạn rút ra tiêu hết" chứ không nhập vào gốc, thì tiền lãi đó không tiếp tục sinh lãi kép `1%/tháng` nữa!

> **Điểm dừng Phiên 2:** Trước khi sang Phiên 3, hãy phân biệt nhanh 3 con số: (1) `12%/năm danh nghĩa ghép lãi tháng` (chia 12 ra `1%/tháng`, cả năm thành `12,6825%`); (2) `12%/năm hiệu dụng` (lấy căn bậc 12 ra `0,9489%/tháng`); (3) `4% lạm phát năm` (dùng ở mẫu số `1,04` để tính sức mua thực).

---

## Phiên 3 — Lợi suất tổng cộng trên nguồn thật và Bài toán góp tiền định kỳ

### 1. Cùng một `CAGR` nhưng đường đi và nỗi đau sụt giảm (`Drawdown`) rất khác nhau

`PHÉP_TÍNH` Giả sử Quỹ A tăng đều `10%/năm` suốt 2 năm: từ `100` lên `110` rồi lên `121` (`CAGR = 10%/năm`).
Quỹ B năm đầu tăng nóng `+40%` (từ `100` lên `140`), nhưng năm thứ hai sụt giảm `-13,57%` ($140 \times (1 - 0,135714) = 121$).
Cả hai quỹ đều đi từ `100` lên `121` sau 2 năm và có cùng **`CAGR = 10%/năm`**, nhưng người giữ Quỹ B phải chịu cú rơi từ `140` xuống `121`. Vì vậy, `CAGR` chỉ là **tốc độ tăng đều tương đương nối giữa điểm đầu và điểm cuối**, không có nghĩa là năm nào tài sản cũng tăng đều đặn như vậy!

## Ví dụ từ nguồn thật: Kiểm chứng `CAGR` 5 năm trên báo cáo Apple Inc. (`Form 10-K FY2025`)

`SỰ_THẬT` Trong báo cáo **[Apple Inc. — Form 10-K cho năm tài chính kết thúc ngày 27/09/2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm)** (nộp SEC ngày `31/10/2025`, mục *Item 5 — Company Stock Performance*), bảng so sánh hiệu quả cổ phiếu giả định nhà đầu tư bỏ ra **`100 USD`** tại giá đóng cửa ngày `25/09/2020` và **tái đầu tư toàn bộ cổ tức (`reinvestment of dividends`)** suốt 5 năm. Tại mốc kết thúc tháng `09/2025`, khoản `100 USD` ban đầu trở thành:
- **Cổ phiếu Apple (`AAPL`):** **`234 USD`** (tổng mức tăng toàn kỳ `+134%`).
- **Chỉ số `S&P 500`:** **`217 USD`** (tổng mức tăng toàn kỳ `+117%`).

`PHÉP_TÍNH` Áp dụng công thức `CAGR` cho cửa sổ $n = 5 \text{ năm}$ (đối chiếu trực tiếp với hàm `cagr(100, 234, 5)` trong [market_returns.py](../practice/models/market_returns.py)):
$$\text{CAGR}_{\text{Apple}} = \left(\frac{234}{100}\right)^{\frac{1}{5}} - 1 = (2,34)^{0,2} - 1 \approx 18,53\%/\text{năm}$$
$$\text{CAGR}_{\text{S\&P 500}} = \left(\frac{217}{100}\right)^{\frac{1}{5}} - 1 = (2,17)^{0,2} - 1 \approx 16,76\%/\text{năm}$$

Ba quy tắc bắt buộc khi đọc bảng nguồn thật này:
1. **Không lấy `134% / 5 = 26,8%/năm`:** Chia trung bình cộng sẽ bỏ qua hiệu ứng lãi kép và thổi phồng tốc độ tăng trưởng hàng năm.
2. **Không cộng thêm cổ tức một lần nữa vào con số `234 USD`:** Vì chuỗi chỉ số tổng lợi suất (`Total Return Index`) trong bảng đã tự động dùng cổ tức mua thêm cổ phiếu qua từng quý.
3. **Hiểu rõ giới hạn:** Con số `18,53%/năm` tính bằng đồng `USD` trước thuế/phí giao dịch cá nhân, chưa quy đổi tỷ giá `USD/VND` hay lạm phát tại Việt Nam, và tuyệt đối không phải cam kết cho 5 năm tiếp theo.

### 2. Bài toán góp đều hàng tháng: Vì sao tiền góp mới không phải là "tiền lãi"?

`KỊCH_BẢN` Bạn bắt đầu với vốn ban đầu **`10 triệu đồng`** và đều đặn góp thêm **`2 triệu đồng` vào cuối mỗi tháng** trong suốt **`36 tháng`** (3 năm). Giả sử tài khoản sinh lời cố định theo mức danh nghĩa `6%/năm` ghép lãi hàng tháng, tức **`0,5%/tháng` (`0,005`)**, chưa tính thuế/phí.

`PHÉP_TÍNH` Hãy tách làm 2 phần rõ ràng (khớp với hàm `monthly_contributions(10, 2, 0.005, 36)` trong [market_returns.py](../practice/models/market_returns.py)):
1. **Phần 1 — Vốn gốc ban đầu `10 triệu đồng` nằm nguyên suốt 36 tháng:**
   $$\text{FV}_{\text{vốn đầu}} = 10 \times (1 + 0,005)^{36} \approx 11,9668 \text{ triệu đồng (làm tròn } 11,97 \text{ triệu đồng)}$$
2. **Phần 2 — 36 khoản góp `2 triệu đồng` vào cuối mỗi tháng:**
   Khoản góp cuối tháng 1 còn 35 tháng sinh lời; khoản góp cuối tháng 12 còn 24 tháng sinh lời; khoản góp cuối tháng 36 vừa nộp vào ngày cuối cùng nên có `0` tháng sinh lời. Tổng của 36 khoản khác tuổi này là:
   $$\text{FV}_{\text{góp đều cuối tháng}} = 2 \times \frac{(1 + 0,005)^{36} - 1}{0,005} \approx 78,6722 \text{ triệu đồng (làm tròn } 78,67 \text{ triệu đồng)}$$
3. **Tổng số dư cuối tháng 36:**
   $$\text{Tổng số dư} = 11,9668 + 78,6722 \approx 90,6390 \text{ triệu đồng (làm tròn } 90,64 \text{ triệu đồng)}$$
4. **Tách bạch Vốn tự nộp và Phần lãi sinh ra:**
   - **Tổng vốn tự nộp từ túi bạn:** $10 + (36 \times 2) = 82,00 \text{ triệu đồng}$.
   - **Phần tăng thêm do đầu tư (tiền lãi):** $90,64 - 82,00 = 8,64 \text{ triệu đồng}$ *(tuyệt đối không lấy `90,64 − 10 = 80,64 triệu` rồi khoe mình lãi 800%, vì `72 triệu` là tiền mồ hôi bạn nộp thêm vào!)*.
   - Nếu đổi sang **góp vào đầu mỗi tháng**, mỗi khoản `2 triệu` được hưởng thêm 1 tháng sinh lời (`× 1,005`), giúp phần góp đều tăng lên $78,6722 \times 1,005 \approx 79,0656 \text{ triệu}$ (tổng số dư tăng thêm khoảng `0,39 triệu đồng` lên `91,03 triệu đồng`).

*(Khi các khoản góp/rút không đều đặn, muốn đo chính xác hiệu quả của người quản lý hay của tài khoản cá nhân, bạn sẽ học hai thước đo chuyên biệt là `TWR` và `MWR/IRR` ở [Bài H4](H4-twr-mwr-benchmark.md)).*

---

## Năm câu hỏi kiểm tra mỗi khi gặp bài toán thời gian và lợi suất

1. Khoản tiền được nhận hoặc nộp vào **mốc thời gian nào** (đầu kỳ, giữa kỳ hay cuối kỳ)?
2. Lãi suất `r` và số kỳ `n` đã quy về **cùng một đơn vị thời gian** (cùng theo tháng hoặc cùng theo năm) chưa?
3. Con số lãi suất đầu vào là **danh nghĩa niêm yết (`j`)** hay **hiệu dụng năm (`EAR`)**?
4. Dòng tiền và lợi suất đang tính theo **danh nghĩa** hay đã điều chỉnh **lạm phát (`Real`)** và **tỷ giá tiền tệ**?
5. Biến động số dư tài khoản có chứa **tiền nộp thêm / rút ra** hay **cổ tức tái đầu tư** chưa được tách riêng không?

---

## Bài tập — làm trước khi mở đáp án

Hãy tự giải từng bước cả 10 câu hỏi dưới đây trước khi đối chiếu với phần Đáp án:

1. Khoản đầu tư `100 triệu đồng` tăng trưởng kép `10%/năm` trong `2 năm` (không góp/rút) sẽ thành bao nhiêu tiền?
2. Một khoản tiền `121 triệu đồng` nhận sau `2 năm` được quy đổi về ngày hôm nay (`PV`) ở mức chiết khấu `10%/năm` là bao nhiêu?
3. Tài sản tăng từ `100` lên `121` sau `2 năm`: tốc độ tăng trưởng kép theo năm (`CAGR`) là `21%` hay `10%`? Vì sao?
4. Cổ phiếu tăng giá từ `50` lên `52` trong 1 năm và trả cổ tức tiền mặt là `3` (cùng đơn vị, giữ tiền mặt không tái đầu tư trong kỳ): lợi suất tổng cộng của kỳ đó là bao nhiêu?
5. Lợi suất danh nghĩa đạt `8%/năm`, tỷ lệ lạm phát cùng kỳ là `4%/năm`: lợi suất thực (`Real Return`) chính xác là bao nhiêu phần trăm?
6. Tài khoản đầu năm có `100 triệu`, trong năm không rút tiền, ngay ngày cuối cùng của năm bạn nộp thêm `50 triệu` tiền lương làm số dư cuối năm báo `160 triệu`. Hãy tính phần lợi nhuận thực sự do đầu tư tạo ra và lợi suất 1 năm của khoản vốn đầu kỳ.
7. Bạn cần có `150 triệu đồng` sau `3 năm`, giả sử tỷ lệ sinh lời là `8%/năm`. Hãy tính `PV` hôm nay rồi nhân ngược lại để kiểm chứng `FV`. Nếu đổi tỷ lệ chiết khấu lên `10%/năm` thì `PV` tăng hay giảm, và bằng bao nhiêu?
8. Hãy phân biệt `12%/năm danh nghĩa ghép lãi hàng tháng` với `12%/năm hiệu dụng (EAR)`: tính tỷ lệ lãi mỗi tháng và lãi suất hiệu dụng cả năm của từng loại.
9. Từ bảng dữ liệu thật trong `Form 10-K FY2025` của Apple (`100 USD` thành `234 USD` sau `5 năm`), hãy tính `CAGR`, nêu 2 điều không được suy diễn từ con số này, và giải thích vì sao không cộng thêm cổ tức vào `234 USD`.
10. Với vốn ban đầu `10 triệu đồng`, góp thêm `2 triệu đồng` vào **cuối mỗi tháng** trong `36 tháng` ở mức lãi `0,5%/tháng`: hãy tính tổng vốn đã nộp, số dư cuối kỳ và phần tiền lãi tăng thêm. Nếu đề bài chỉ nói "góp 2 triệu mỗi tháng" mà không nói đầu tháng hay cuối tháng thì bạn còn thiếu dữ kiện gì?

---

## Đáp án và điều cần hiểu

1. `PHÉP_TÍNH` $\text{FV} = 100 \times (1 + 0,10)^2 = 121 \text{ triệu đồng}$.
2. `PHÉP_TÍNH` $\text{PV} = \frac{121}{(1 + 0,10)^2} = 100 \text{ triệu đồng}$ (phép chiết khấu ngược chiều với Câu 1).
3. `PHÉP_TÍNH` Lợi suất kép theo năm (`CAGR`) là **`10%/năm`** vì $(121/100)^{1/2} - 1 = 10\%$; còn `21%` là tổng mức tăng của cả 2 năm gộp lại.
4. `PHÉP_TÍNH` $\text{Lợi suất 1 kỳ} = \frac{52 - 50 + 3}{50} = \frac{5}{50} = 10,0\%$.
5. `PHÉP_TÍNH` $\text{Lợi suất thực} = \frac{1 + 0,08}{1 + 0,04} - 1 = \frac{1,08}{1,04} - 1 \approx 3,846\% \text{ (làm tròn } 3,85\%)$.
6. `PHÉP_TÍNH` Lợi nhuận do đầu tư tạo ra $= 160 - 100 - 50 \text{ (vốn nộp thêm)} = 10 \text{ triệu đồng}$. Vì `50 triệu` nộp vào ngay thời khắc cuối kỳ (chưa tham gia sinh lời trong năm) nên vốn sinh lời trong năm là `100 triệu` $\implies \text{Lợi suất} = \frac{10}{100} = 10,0\%$.
7. `PHÉP_TÍNH` Ở mức `8%/năm`: $\text{PV} = \frac{150}{1,08^3} = \frac{150}{1,259712} \approx 119,07 \text{ triệu đồng}$ (nhân ngược $119,0748 \times 1,08^3 = 150$). Khi tăng tỷ lệ chiết khấu lên `10%/năm`, mẫu số lớn hơn nên `PV` **giảm** xuống còn $\frac{150}{1,10^3} \approx 112,70 \text{ triệu đồng}$.
8. `PHÉP_TÍNH`
   - Loại 1 (`12%/năm danh nghĩa ghép tháng`): Tỷ lệ tháng $= \frac{12\%}{12} = 1,0\%/\text{tháng}$; Lãi suất hiệu dụng năm $\text{EAR} = (1,01)^{12} - 1 \approx 12,6825\%/\text{năm}$.
   - Loại 2 (`12%/năm hiệu dụng EAR`): Tỷ lệ tháng tương đương $= (1,12)^{1/12} - 1 \approx 0,9489\%/\text{tháng}$ (không chia thẳng cho 12!).
9. `PHÉP_TÍNH` $\text{CAGR} = (234 / 100)^{1/5} - 1 \approx 18,53\%/\text{năm}$. Hai điều không suy ra được: (1) Không có nghĩa mỗi năm đơn lẻ đều tăng `18,53%`; (2) Không đảm bảo 5 năm tới lặp lại mức này. Không cộng thêm cổ tức vì con số `234 USD` trong bảng `10-K` đã tính theo giả định tái đầu tư toàn bộ cổ tức.
10. `PHÉP_TÍNH` Tổng vốn tự nộp $= 10 + 36 \times 2 = 82 \text{ triệu đồng}$; Số dư cuối kỳ $\approx 90,64 \text{ triệu đồng}$; Phần lãi tăng thêm $\approx 8,64 \text{ triệu đồng}$. Nếu không biết nộp đầu tháng hay cuối tháng thì chưa khóa được số kỳ sinh lời của từng khoản góp (lệch nhau 1 kỳ lãi `× 1,005`).

---

## Bài làm với dữ liệu thiếu hoặc lệch

`KỊCH_BẢN` Một bảng sao kê tóm tắt chỉ ghi vỏn vẹn 3 dòng: **"Số dư đầu năm: `100 triệu đồng`; Tổng tiền nộp thêm trong năm: `20 triệu đồng`; Số dư cuối năm: `132 triệu đồng`"** — rồi người viết kết luận luôn: *"Tài khoản năm nay lãi `32%`!"*

Khi gặp dữ liệu thiếu ngày tháng như vậy, bạn xử lý theo 3 bước chuẩn Bậc S:
1. **Bước 1 — Bác bỏ ngay con số `32%`:** Chênh lệch số dư cuối năm và đầu năm là `132 − 100 = 32 triệu`, nhưng trong đó có **`20 triệu` là vốn mới nộp thêm**. Nếu không có khoản rút tiền hay phí ẩn nào khác, phần tiền lãi thực sự do đầu tư tạo ra chỉ là:
   $$\text{Lãi đầu tư} = 132 - 100 - 20 = 12 \text{ triệu đồng}$$
2. **Bước 2 — Chỉ ra dữ kiện còn thiếu (`CHƯA_BIẾT` ngày nộp tiền):** Với cùng `12 triệu` tiền lãi, thời điểm nộp `20 triệu` làm thay đổi hoàn toàn tỷ suất sinh lời:
   - Nếu `20 triệu` được nộp **ngay ngày đầu năm**, tổng vốn làm việc suốt cả năm là `100 + 20 = 120 triệu` $\implies \text{Lợi suất} = \frac{12}{120} = 10,0\%$.
   - Nếu `20 triệu` được nộp **ngay ngày cuối năm**, vốn làm việc suốt năm chỉ là `100 triệu` $\implies \text{Lợi suất trước khi nộp} = \frac{12}{100} = 12,0\%$.
3. **Bước 3 — Yêu cầu bảng dòng tiền kèm ngày tháng cụ thể** (và thông tin thuế/phí đã trừ) trước khi chốt tỷ suất sinh lời.

---

## Sai ở đâu

Hãy tìm tất cả các lỗi trong lời quảng cáo sau đây:
> *"Gửi 100 triệu đồng với lãi suất 12%/năm trả lãi hàng tháng, sau 2 năm thành 125,44 triệu; năm thứ hai bạn chỉ cần bỏ thêm 20 triệu vào là tổng tiền lãi vọt lên 45,44 triệu! Với lạm phát 4%/năm thì bạn cầm chắc lãi thực 8%/năm!"*

Đoạn quảng cáo ngắn trên mắc tới **4 lỗi nghiêm trọng**:
1. **Lỗi 1 — Nhầm kỳ ghép lãi:** Lấy $100 \times (1,12)^2 = 125,44 \text{ triệu}$ là công thức ghép lãi **theo năm**; trong khi "trả lãi hàng tháng" nếu không tái đầu tư thì là lãi đơn, còn nếu ghép lãi hàng tháng (`1%/tháng` trong `24 tháng`) thì phải là $100 \times (1,01)^{24} \approx 126,97 \text{ triệu}$.
2. **Lỗi 2 — Biến tiền vốn nộp thêm thành tiền lãi:** Khoản `20 triệu` nộp thêm là tiền túi của bạn, không được cộng vào tiền lãi (và cũng chưa cho biết nộp vào ngày nào của năm thứ hai).
3. **Lỗi 3 — Tính sai công thức lợi suất thực:** Lợi suất thực phải tính bằng phép chia $\frac{1 + r}{1 + i} - 1$ trên lãi suất hiệu dụng cùng kỳ, không phải lấy `12% − 4% = 8%`.
4. **Lỗi 4 — Bỏ qua thuế, phí và rủi ro:** Gọi một mức lãi giả định là "cầm chắc" mà không nêu điều kiện hợp đồng hay thuế/phí.

---

## Kiểm tra chuyển bài

Trước khi chuyển sang **[Bài 003: Chất lượng doanh nghiệp — lợi thế cạnh tranh, ROIC và khả năng tái đầu tư](003-business-quality-moat-and-roic.md)** (Bước 9/23 Nhánh 1) hoặc [Bài N7](N7-data-probability-uncertainty.md), hãy tự giải 3 câu hỏi kiểm tra đầu ra sau:

1. Khoản vốn `25 triệu đồng` tăng trưởng với lãi suất hiệu dụng `6%/năm` trong `4 năm`: hãy tính `FV` rồi chiết khấu ngược về `PV`.
2. Một tài khoản có hai khoản nộp tiền vào giữa năm nhưng không ghi ngày cụ thể: hãy liệt kê các dữ kiện bắt buộc phải hỏi thêm trước khi tính lợi suất.
3. Một khoản đầu tư tính bằng `USD` tăng `+9%` trong năm, nhưng cùng năm đó đồng `USD` giảm giá `-5%` so với `VND`, và lạm phát tính theo `VND` là `4%`: hãy mô tả thứ tự quy đổi và tính lợi suất thực theo sức mua `VND`.

**Tiêu chí đạt:**
- Câu 1: `PHÉP_TÍNH` $\text{FV} = 25 \times (1,06)^4 \approx 31,56 \text{ triệu đồng}$; chiết khấu ngược $\frac{31,5619}{1,06^4} = 25,00 \text{ triệu đồng}$.
- Câu 2: Phải yêu cầu ngày nộp/rút cụ thể, số tiền từng lần và giá trị tài khoản tại các mốc đó.
- Câu 3: `PHÉP_TÍNH` Bước 1 — Quy đổi sang lợi suất danh nghĩa bằng `VND` (như hàm `currency_return(0.09, -0.05)` trong [market_returns.py](../practice/models/market_returns.py)): $1,09 \times (1 - 0,05) - 1 = 1,09 \times 0,95 - 1 = 3,55\%$. Bước 2 — Chia cho lạm phát `VND` (`4%`): $\frac{1,0355}{1,04} - 1 \approx -0,43\%$ (sức mua thực tính bằng `VND` giảm nhẹ `-0,43%`, hoàn toàn không phải lấy `9% − 5% − 4% = 0%`!).

---

## Mô hình thực hành

Tệp [market_returns.py](../practice/models/market_returns.py) cài đặt sẵn các hàm chuẩn hóa cho bài học này: `future_value()`, `present_value()`, `cagr()`, `real_return()`, `currency_return()`, `effective_annual_rate()`, `equivalent_period_rate()` và `monthly_contributions()`. Bạn có thể chạy trực tiếp và kiểm tra bộ test tự động bằng lệnh `python3 -m unittest tests/test_market_returns.py`.

## Ranh giới an toàn

- Đây là bài học toán tài chính nền tảng, không phải khuyến nghị đầu tư cá nhân hóa.
- Mọi con số lãi suất giả định được gắn nhãn `KỊCH_BẢN`; công thức lãi kép không phải lời hứa làm giàu tự động hay cam kết lợi nhuận cố định trên thị trường chứng khoán.

## Nguồn Internet đã mở

Nguồn được mở kiểm chứng ngày `2026-11-02` và đối chiếu lại ngày `2026-11-06`:

| Nguồn | Kỳ / Phiên bản & Phạm vi | Dùng cho phần nào |
|---|---|---|
| [California BOE — Time Value of Money (Lesson 1)](https://www.boe.ca.gov/info/tvm/lesson1.html) | Hoa Kỳ; tài liệu giáo dục chính thức (`CHƯA_BIẾT` ngày xuất bản gốc) | Nguyên lý lãi kép (`FV`) và chiết khấu (`PV`) |
| [California BOE — Time Value of Money (Lesson 9)](https://www.boe.ca.gov/info/tvm/lesson9.html) | Hoa Kỳ; tài liệu giáo dục chính thức (`CHƯA_BIẾT` ngày xuất bản gốc) | Tần suất ghép lãi (`m` lần/năm) và lãi suất hiệu dụng |
| [SEC Investor.gov — Compound Interest Calculator](https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator) | Hoa Kỳ; công cụ giáo dục nhà đầu tư hiện hành | Đầu vào bài toán góp đều định kỳ và giới hạn giả định |
| [BLS — Consumer Price Index FAQ](https://www.bls.gov/cpi/questions-and-answers.htm) | Cục Thống kê Lao động Hoa Kỳ; trang hiện hành | Ý nghĩa rổ hàng hóa `CPI` và giới hạn khi đo sức mua từng hộ gia đình |
| [Apple Inc. — Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Năm tài chính kết thúc `27/09/2025`, nộp SEC ngày `31/10/2025` (USD, `US GAAP`) | Bảng *Company Stock Performance* 5 năm (`100 USD → 234 USD`) có tái đầu tư cổ tức |

Biên bản kiểm duyệt độc lập: [kiểm nguồn](../reviews/N4-fact-check.md), [phản biện rủi ro](../reviews/N4-risk-review.md).
