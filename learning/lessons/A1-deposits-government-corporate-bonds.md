# Bài A1 — Tiền gửi, Trái phiếu Chính phủ và Trái phiếu Doanh nghiệp: Định giá, Kỳ hạn Macaulay/Modified và Rủi ro Tín dụng

- Ngày cập nhật: `2026-11-05`
- Chốt dữ liệu lúc: `2026-11-05 12:15 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Phân biệt bản chất pháp lý – kinh tế của Tiền gửi ngân hàng (có Bảo hiểm tiền gửi), Trái phiếu Chính phủ (`TPCP`) và Trái phiếu doanh nghiệp (`TPDN`); tính chính xác giá trái phiếu nhiều kỳ, lợi suất đáo hạn (`YTM`), thời lượng `Macaulay Duration` và `Modified Duration`; đánh giá rủi ro tín dụng, tài sản bảo đảm và bẫy "ngân hàng phân phối không phải là người bảo lãnh thanh toán".
- Thời lượng dự kiến: `3 buổi học (~270 phút)`
  - **Buổi 1 (90 phút):** Tiền gửi ngân hàng, cách tính lãi thực nhận, quy tắc Bảo hiểm tiền gửi Việt Nam (`hạn mức 350 triệu VND` theo Thông tư `05/2026/TT-NHNN`) và sự khác biệt căn bản giữa người gửi tiền với trái chủ.
  - **Buổi 2 (90 phút):** Toán học thu nhập cố định (`Fixed Income`) — Định giá trái phiếu trả lãi định kỳ (`Coupon Bond`), mối quan hệ nghịch biến giữa Lãi suất thị trường (`YTM`) và Giá trái phiếu, Thời lượng `Duration` và Độ lồi (`Convexity`).
  - **Buổi 3 (90 phút):** Giải phẫu Trái phiếu doanh nghiệp tại Việt Nam — Đọc bản công bố thông tin phát hành, kiểm định dòng tiền trả nợ (`Interest Coverage`, `Net Debt / EBITDA`), tài sản đảm bảo thực chất, xử lý dữ liệu bẩn và làm 10 bài tập định lượng.
- Bài trước liên quan: [N4 — Giá trị thời gian của tiền và lợi suất](N4-time-value-returns.md), [P1 — Ngân sách, quỹ khẩn cấp và bảo hiểm](P1-budget-emergency-fund-insurance.md), [005 — Nợ, thanh khoản và khả năng sống sót](005-debt-liquidity-survival.md), [F3 — Phân tích doanh nghiệp bất động sản Việt Nam](F3-vietnam-property-developers.md).
- Mô hình thực hành đi kèm: [`../practice/models/market_returns.py`](../practice/models/market_returns.py), [`../practice/models/insurance.py`](../practice/models/insurance.py) và [`../practice/models/valuation.py`](../practice/models/valuation.py).
- Câu hỏi cốt lõi: Khi một nhân viên tại quầy ngân hàng giới thiệu cho bạn một sản phẩm "tiết kiệm linh hoạt hưởng lãi suất cao hơn 3%/năm so với gửi tiết kiệm thông thường", làm sao bạn phân biệt ngay đó là tiền gửi được bảo hiểm hay là trái phiếu doanh nghiệp có nguy cơ mất vốn gốc?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/A1-fact-check.md), [phản biện](../reviews/A1-risk-review.md).

---

## Hiểu bài trong một phút

Các công cụ thu nhập cố định (`Fixed Income`) thường được gọi chung là "kênh đầu tư an toàn", nhưng thực chất chúng nằm trên một **phổ rủi ro trải dài từ gần như không có rủi ro vỡ nợ nội tệ cho đến rủi ro mất trắng 100% vốn gốc**:
1. **Tiền gửi ngân hàng bằng VND (`Bank Deposits`):** Là nghĩa vụ nợ trực tiếp của ngân hàng thương mại nhận tiền gửi và thuộc đối tượng được bảo vệ bởi **Bảo hiểm tiền gửi Việt Nam (`DIV`)** với hạn mức chi trả tối đa **`350 triệu VND`** (gộp cả gốc và lãi của một cá nhân tại một tổ chức tham gia bảo hiểm tiền gửi theo Thông tư `05/2026/TT-NHNN` — `SỰ_THẬT`).
2. **Trái phiếu Chính phủ (`Government Bonds`):** Là nghĩa vụ nợ trực tiếp của Chính phủ (Bộ Tài chính / Kho bạc Nhà nước phát hành). Trái phiếu Chính phủ bằng đồng nội tệ được coi là tài sản có rủi ro vỡ nợ tín dụng thấp nhất trong nền kinh tế (được các tập đoàn bảo hiểm như `Bảo Việt — BVH` nắm giữ tới `109.104,67 tỷ VND` làm trụ cột dự phòng toán học — `SỰ_THẬT`), nhưng nếu bạn bán trước ngày đáo hạn khi lãi suất thị trường tăng vọt, bạn vẫn chịu **rủi ro giảm giá thị trường (`Interest Rate / Duration Risk`)** (`SUY_LUẬN`).
3. **Trái phiếu doanh nghiệp (`Corporate Bonds`):** Là giấy nhận nợ do một công ty cổ phần hoặc công ty TNHH phát hành để vay tiền. Trái phiếu doanh nghiệp **tuyệt đối không phải là tiền gửi ngân hàng và không được Bảo hiểm tiền gửi Việt Nam bảo vệ** (`SỰ_THẬT`). Ngân hàng hay công ty chứng khoán đứng ra giới thiệu, phân phối trái phiếu chỉ hưởng phí dịch vụ trung gian, chứ không mặc nhiên có nghĩa vụ bỏ tiền ra trả nợ thay khi doanh nghiệp phát hành vỡ nợ (`SỰ_THẬT`).

---

## Buổi 1 — Tiền gửi Ngân hàng, Quy ước tính lãi và Bảo hiểm tiền gửi Việt Nam

### 1.1. Công thức tính lãi tiền gửi có kỳ hạn, lãi kép và rút trước hạn

Khi gửi một khoản tiền gốc $P_0$ tại ngân hàng với lãi suất danh nghĩa niêm yết $r_{\text{năm}}$ (tính theo tỷ lệ phần trăm/năm):
- **Nếu giữ đúng hạn theo lãi đơn (`Simple Interest`) cho số ngày thực gửi $d$ (quy ước cơ sở 365 ngày/năm tại Việt Nam):**
  $$\text{Tiền lãi đúng hạn} = P_0 \times r_{\text{năm}} \times \frac{d}{365}$$
- **Nếu tái tục cả gốc lẫn lãi qua $m$ kỳ ghép lãi trong năm trong $n$ năm (`Compound Interest`):**
  $$\text{Giá trị thu về } FV = P_0 \times \left(1 + \frac{r_{\text{năm}}}{m}\right)^{m \times n} \implies \text{Lãi suất hiệu dụng năm (EAR)} = \left(1 + \frac{r_{\text{năm}}}{m}\right)^m - 1$$
- **Rủi ro rút trước hạn (`Early Withdrawal Penalty`):** Trong hầu hết hợp đồng tiền gửi có kỳ hạn thông thường, nếu người gửi rút toàn bộ số tiền trước ngày đáo hạn chỉ vài ngày, toàn bộ số ngày đã gửi chỉ được hưởng **lãi suất không kỳ hạn** (thường chỉ `0,1%–0,5%/năm` thay vì `5%–6%/năm`)! Để tránh mất lãi khi có nhu cầu thanh khoản đột xuất, người gửi tiền cá nhân thường chia khoản tiền tiết kiệm thành nhiều sổ/hợp đồng tiền gửi trực tuyến nhỏ có kỳ hạn lệch nhau (`Deposit Laddering`) (`SUY_LUẬN`).

### 1.2. Phạm vi và Hạn mức Bảo hiểm tiền gửi Việt Nam

- `SỰ_THẬT`: Theo công bố của [Bảo hiểm tiền gửi Việt Nam (`DIV`)](https://www.div.gov.vn/bao-hiem-tien-gui-chi-ap-dung-doi-voi-tien-gui-cua-ca-nhan-bang-dong-viet-nam), bảo hiểm tiền gửi chỉ áp dụng đối với **tiền gửi bằng đồng Việt Nam (`VND`) của cá nhân** gửi tại tổ chức tham gia bảo hiểm tiền gửi dưới hình thức tiền gửi có kỳ hạn, tiền gửi không kỳ hạn, tiền gửi tiết kiệm, chứng chỉ tiền gửi, kỳ phiếu, tín phiếu. Tiền gửi bằng ngoại tệ (`USD`, `EUR`...), tiền gửi của tổ chức kinh tế (như khoản tiền gửi `326,60 tỷ VND` gốc quá hạn của `Bảo Việt` tại công ty cho thuê tài chính `ALCII`), hoặc tiền mua trái phiếu doanh nghiệp **không thuộc phạm vi chi trả của Bảo hiểm tiền gửi** (`SỰ_THẬT`).
- `SỰ_THẬT`: Theo [Thông tư số 05/2026/TT-NHNN](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/05-nhnn.pdf), hạn mức trả tiền bảo hiểm là **`350 triệu VND`**, tính cho **tổng tất cả các khoản tiền gửi được bảo hiểm (gồm cả gốc và lãi) của một cá nhân tại một tổ chức tham gia bảo hiểm tiền gửi** khi phát sinh nghĩa vụ trả tiền bảo hiểm.
- *Lưu ý thực hành (`SUY_LUẬN`):* Hạn mức `350 triệu VND` tính theo **từng cá nhân tại một ngân hàng**, chứ không phải tính riêng cho từng cuốn sổ tiết kiệm! Nếu một cá nhân mở 5 sổ tiết kiệm `200 triệu VND/sổ` (tổng gốc `1.000 triệu VND`) tại cùng một ngân hàng X, thì tổng mức bảo hiểm tiền gửi tối đa tại ngân hàng X vẫn là `350 triệu VND` (phần vượt hạn mức sẽ được thanh toán trong quá trình thanh lý tài sản của tổ chức tín dụng theo quy định pháp luật).

---

## Buổi 2 — Định giá Trái phiếu, Lợi suất đáo hạn (YTM) và Độ nhạy Lãi suất (Duration)

### 2.1. Công thức định giá Trái phiếu nhiều kỳ (`Coupon Bond Valuation`)

Theo định nghĩa chuẩn quốc tế của [Ủy ban Chứng khoán và Giao dịch Hoa Kỳ (`SEC — Bonds`)](https://www.investor.gov/introduction-investing/investing-basics/investment-products/bonds-or-fixed-income-products/bonds), trái phiếu là chứng khoán nợ trong đó tổ chức phát hành cam kết thanh toán tiền lãi định kỳ (`Coupon` — $C = F \times c$) và hoàn trả mệnh giá gốc ($F$, tại Việt Nam thường là `100.000 VND` hoặc `100.000.000 VND`) vào ngày đáo hạn $T$.

Khi thị trường yêu cầu mức lợi suất chiết khấu (Lợi suất đáo hạn — `Yield to Maturity`, ký hiệu $y$) cho một trái phiếu còn $T$ kỳ trả lãi đều đặn, giá hợp lý hiện tại ($P$) của trái phiếu bằng tổng giá trị hiện tại của toàn bộ dòng tiền tương lai:

$$P(y) = \sum_{t=1}^{T} \frac{C}{(1 + y)^t} + \frac{F}{(1 + y)^T} = C \times \left[\frac{1 - (1 + y)^{-T}}{y}\right] + \frac{F}{(1 + y)^T}$$

Ba định luật toán học bất biến từ phương trình định giá trái phiếu (được giải thích trực quan tại [SEC — Interest Rate Risk on Bonds](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-86)):
1. **Khi $y = c$ (Lợi suất yêu cầu bằng lãi suất cuống phiếu):** Giá trái phiếu bằng đúng mệnh giá ($P = F$, giao dịch ngang giá — `At Par`).
2. **Khi $y > c$ (Lãi suất thị trường tăng cao hơn lãi suất cuống phiếu):** Giá trái phiếu giảm xuống thấp hơn mệnh giá ($P < F$, giao dịch chiết khấu — `At a Discount`).
3. **Khi $y < c$ (Lãi suất thị trường giảm thấp hơn lãi suất cuống phiếu):** Giá trái phiếu tăng lên cao hơn mệnh giá ($P > F$, giao dịch phụ trội — `At a Premium`).

### 2.2. Thời lượng `Macaulay Duration` và `Modified Duration`: Đo rủi ro lãi suất

Vì sao cùng khi lãi suất thị trường tăng thêm `+1,0%/năm` (`+100 bps`), một trái phiếu kỳ hạn 1 năm chỉ giảm giá khoảng `-0,94%`, trong khi một trái phiếu kỳ hạn 15 năm lại sụt giá tới `-10%` đến `-12%`? Câu trả lời nằm ở **Thời lượng (`Duration`)** — chỉ số đã được cài đặt sẵn trong mô-đun [`../practice/models/market_returns.py`](../practice/models/market_returns.py) và [`../practice/models/insurance.py`](../practice/models/insurance.py):

1. **Thời lượng Macaulay (`Macaulay Duration` — $D_{\text{Mac}}$):** Là thời gian bình quân gia quyền (tính bằng năm) để nhà đầu tư thu hồi lại giá trị hiện tại của các dòng tiền từ trái phiếu:
   $$D_{\text{Mac}} = \frac{1}{P} \sum_{t=1}^{T} t \times \frac{\text{CF}_t}{(1 + y)^t}$$
2. **Thời lượng điều chỉnh (`Modified Duration` — $D_{\text{Mod}}$):** Đo trực tiếp độ nhạy phần trăm của giá trái phiếu khi lợi suất đáo hạn $y$ dịch chuyển một lượng $\Delta y$:
   $$D_{\text{Mod}} = \frac{D_{\text{Mac}}}{1 + y} \implies \frac{\Delta P}{P} \approx - D_{\text{Mod}} \times \Delta y$$

**Ví dụ tính toán tái lập (`PHÉP_TÍNH`):**
Xét một Trái phiếu có mệnh giá $F = 100\text{ triệu VND}$, kỳ hạn còn lại $T = 3\text{ năm}$, trả lãi cuống phiếu $c = 6,0\%/\text{năm}$ (`6,0 triệu VND` cuối mỗi năm), đang được định giá ở mức lợi suất đáo hạn $y = 6,0\%/\text{năm}$ ($P = 100,00\text{ triệu VND}$):
- Giá trị hiện tại của 3 dòng tiền tại $y = 6,0\%$:
  - Năm 1 ($t = 1$): $\text{PV}_1 = 6,0 / 1,06^1 = 5,6604\text{ triệu VND}$;
  - Năm 2 ($t = 2$): $\text{PV}_2 = 6,0 / 1,06^2 = 5,3400\text{ triệu VND}$;
  - Năm 3 ($t = 3$): $\text{PV}_3 = 106,0 / 1,06^3 = 88,9996\text{ triệu VND}$ (Tổng $P = 100,0000\text{ triệu VND}$).
- Thời lượng `Macaulay Duration`:
  $$D_{\text{Mac}} = \frac{1 \times 5,6604 + 2 \times 5,3400 + 3 \times 88,9996}{100,0000} = \frac{283,3392}{100,0000} = 2,8334\text{ năm}$$
- Thời lượng điều chỉnh `Modified Duration`:
  $$D_{\text{Mod}} = \frac{2,8334}{1,06} = 2,6730\text{ năm}$$
- Nếu lãi suất thị trường đột ngột tăng thêm $\Delta y = +2,0\%/\text{năm}$ (từ `6,0%` lên `8,0%`), giá thị trường của trái phiếu này sẽ sụt giảm xấp xỉ:
  $$\frac{\Delta P}{P} \approx -2,6730 \times (+0,02) = -5,346\%\quad (\text{tức giá rơi xuống khoảng }94,65\text{ triệu VND!})$$
  (Giá chính xác khi chiết khấu ở $y = 8,0\%$ là $6/1,08 + 6/1,08^2 + 106/1,08^3 = 94,8458\text{ triệu VND}$, giảm `-5,154%`; chênh lệch nhỏ `+0,19%` có lợi cho trái chủ chính là nhờ hiệu ứng **Độ lồi `Convexity`** — `PHÉP_TÍNH`).

---

## Buổi 3 — Giải phẫu Trái phiếu Doanh nghiệp tại Việt Nam và Kiểm định Rủi ro Tín dụng

### 3.1. Chênh lệch lợi suất tín dụng (`Credit Spread`) và 5 câu hỏi thẩm định TPDN

Vì sao một doanh nghiệp phải phát hành trái phiếu với lãi suất `11%–13%/năm` trong khi Trái phiếu Chính phủ cùng kỳ hạn 5 năm chỉ có lợi suất `2,8%–3,0%/năm`? Khoản chênh lệch `8%–10%/năm` đó chính là **Phần bù rủi ro tín dụng và thanh khoản (`Credit & Liquidity Spread`)**:

$$y_{\text{TPDN}} = y_{\text{TPCP cùng kỳ hạn}} + \text{Credit Spread (Bù đắp xác suất vỡ nợ } PD \times LGD) + \text{Liquidity Spread}$$

`SỰ_THẬT`: Trong thông cáo [Bộ Tài chính khuyến cáo các chủ thể tham gia thị trường trái phiếu doanh nghiệp](https://xaydungchinhsach.chinhphu.vn/nong-bo-tai-chinh-khuyen-cao-cac-chu-the-tham-gia-thi-truong-trai-phieu-doanh-nghiep-119221114165946867.htm), cơ quan quản lý nhấn mạnh hai nguyên tắc sống còn: (1) Lãi suất cao luôn đi kèm rủi ro cao, nhà đầu tư bắt buộc phải tự đánh giá tình hình tài chính của doanh nghiệp phát hành; và (2) **Các ngân hàng thương mại, công ty chứng khoán phân phối trái phiếu chỉ là tổ chức cung cấp dịch vụ, không mặc nhiên là chủ thể bảo lãnh thanh toán gốc và lãi trái phiếu** (trừ khi có hợp đồng bảo lãnh thanh toán vô điều kiện và không hủy ngang của tổ chức tín dụng theo đúng quy định pháp luật).

Trước khi mua bất kỳ một trái phiếu doanh nghiệp nào (hoặc khi đánh giá danh mục TPDN trên bảng cân đối của ngân hàng/công ty bảo hiểm), bạn phải kiểm tra **5 chỉ tiêu sống còn** (kết nối với Bài [005](005-debt-liquidity-survival.md)):
1. **Tổ chức phát hành là công ty vận hành thật hay công ty vỏ bọc dự án (`SPV`)?** Nếu bên phát hành là một công ty TNHH mới thành lập vài tháng chưa có doanh thu, vốn chủ sở hữu mỏng và không có dòng tiền hoạt động kinh doanh (`CFO < 0`), rủi ro mất vốn là cực đại.
2. **Hệ số khả năng trả lãi (`Interest Coverage Ratio = EBIT / Chi phí lãi vay`) và `Net Debt / EBITDA`:** Doanh nghiệp phát hành có tạo ra dòng tiền kinh doanh đủ trả lãi vay ít nhất `2,5–3,0 lần` không?
3. **Chất lượng thực của Tài sản bảo đảm (`Collateral Quality`):**
   - Tài sản bảo đảm là **Quyền sử dụng đất đã có sổ đỏ sạch / bảo lãnh thanh toán của ngân hàng**, hay chỉ là **cổ phiếu chưa niêm yết / quyền phát triển dự án bất động sản chưa xong pháp lý**?
   - Nếu doanh nghiệp vỡ nợ, giá cổ phiếu của chính doanh nghiệp đó sẽ lao dốc về gần `0`, khiến tài sản bảo đảm bằng cổ phiếu biến thành tờ giấy lộn (`Wrong-Way Risk` — rủi ro ngược chiều)!
4. **Mục đích sử dụng vốn và Bậc ưu tiên trả nợ (`Seniority`):** Tiền thu từ phát hành dùng để hoàn thiện dự án sắp bàn giao hay dùng để đảo nợ cũ cho các bên liên quan?
5. **Xếp hạng tín nhiệm độc lập (`Credit Rating`):** Lô trái phiếu đã được một tổ chức xếp hạng tín nhiệm được Bộ Tài chính cấp phép xếp hạng chưa, và bậc tín nhiệm nằm ở nhóm Đầu tư (`AAA` đến `BBB`) hay nhóm Đầu cơ rủi ro cao (`BB`, `B`, `C`)?

---

## 4. Ví dụ từ nguồn thật: Đối chiếu Trái phiếu Chính phủ tại Bảo Việt (BVH) và Nợ quá hạn Trái phiếu Sông Đà Thăng Long tại PVI (FY2025)

1. **Danh mục Trái phiếu Chính phủ và Tiền gửi tại Tập đoàn Bảo Việt (`BVH` — BCTC kiểm toán FY2025):**
   - `SỰ_THẬT`: Theo Thuyết minh 7 (trang 38–42) BCTC hợp nhất kiểm toán năm 2025 của Tập đoàn Bảo Việt (`BVH`, lưu vết tại [`../../research/companies/VN/BVH/report.md`](../../research/companies/VN/BVH/report.md)), trong tổng danh mục đầu tư tài chính `266.535,57 tỷ VND`, `BVH` phân bổ:
     - **Tiền gửi có kỳ hạn:** `119.500,82 tỷ VND` (`44,83%` danh mục đầu tư);
     - **Trái phiếu Chính phủ (`TPCP`) nắm giữ đến ngày đáo hạn (`HTM`):** **`109.104,67 tỷ VND`** (`40,93%` danh mục đầu tư);
     - **Trái phiếu doanh nghiệp và trái phiếu TCTD nắm giữ đến ngày đáo hạn:** `37.424,15 tỷ VND` (`14,04%` danh mục đầu tư).
   - `SUY_LUẬN`: Vì sao một định chế bảo hiểm nhân thọ quản lý gần `300.000 tỷ VND` tài sản lại giữ hơn `85%` danh mục ở Tiền gửi ngân hàng và Trái phiếu Chính phủ dù lợi suất bình quân năm 2025 chỉ đạt `4,47%/năm`? Bởi vì nghĩa vụ nợ của bảo hiểm nhân thọ là nghĩa vụ chi trả dài hạn 15–20 năm cho hàng triệu gia đình; họ cần các trái phiếu Chính phủ kỳ hạn dài (có `Duration` lớn và rủi ro vỡ nợ nội tệ gần bằng `0`) để khớp kỳ hạn (`Asset-Liability Matching`) và bảo toàn vốn gốc tuyệt đối.

2. **Bài học thực tế về rủi ro vỡ nợ Trái phiếu doanh nghiệp tồn đọng hơn 10 năm — Khoản trái phiếu CTCP Sông Đà Thăng Long tại `PVI` (BCTC kiểm toán FY2025):**
   - `SỰ_THẬT`: Theo **Thuyết minh 6a và Thuyết minh 7 (trang 33–34)** BCTC hợp nhất kiểm toán năm 2025 của Công ty Cổ phần PVI (`PVI`, được PwC Việt Nam kiểm toán ngày `11/03/2026`, lưu vết tại [`../../research/companies/VN/PVI/report.md`](../../research/companies/VN/PVI/report.md)), trong danh mục nợ xấu/phải thu quá hạn có ghi nhận khoản **phải thu gốc trái phiếu quá hạn của Công ty Cổ phần Sông Đà Thăng Long với giá gốc `180,77 tỷ VND`**.
   - `SỰ_THẬT`: Khoản trái phiếu doanh nghiệp bất động sản này đã quá hạn thanh toán từ năm 2013; suốt hơn một thập kỷ qua, dù có tài sản thế chấp và phán quyết đòi nợ, doanh nghiệp vẫn chưa thu hồi dứt điểm được tiền gốc và `PVI` đã phải **trích lập dự phòng phải thu khó đòi đủ `100%` (`180,77 tỷ VND`)**.
   - **Bài học xương máu (`SUY_LUẬN`):** Ví dụ thực tế trên BCTC kiểm toán của `PVI` chứng minh đanh thép rằng: ngay cả với một định chế tài chính chuyên nghiệp có bộ phận pháp chế hùng hậu, khi mua phải trái phiếu của một doanh nghiệp bất động sản mất khả năng thanh toán, quá trình xử lý tài sản thế chấp có thể kéo dài hơn 10 năm và phải trích lập mất vốn `100%` trên sổ sách!

---

## 5. Bài làm với dữ liệu thiếu hoặc lệch (Dirty-Data Exercise)

### Tình huống dữ liệu bẩn
Một nhà đầu tư cá nhân 60 tuổi có `2,0 tỷ VND` tiền tích lũy hưu trí đến ngân hàng gửi tiết kiệm. Nhân viên tư vấn đưa ra một tờ rơi quảng cáo:
> *"Sản phẩm Chứng chỉ Đầu tư Trái phiếu An Tâm Thịnh Vượng kỳ hạn 3 năm, lãi suất cố định 11,5%/năm (cao hơn gửi tiết kiệm 12 tháng tới 6,0%/năm!). Sản phẩm được Ngân hàng TMCP X làm đại lý quản lý tài sản bảo đảm, tài sản bảo đảm là 50 triệu cổ phiếu của chính Công ty Bất động sản Phát hành P (định giá 150% mệnh giá trái phiếu), và Công ty Chứng khoán X (công ty con của ngân hàng) cam kết hỗ trợ tìm kiếm khách mua lại khi nhà đầu tư cần tiền trước hạn!"*

Khi yêu cầu xem **Bản công bố thông tin chào bán trái phiếu** và **BCTC của Công ty Phát hành P**, bạn phát hiện 4 dữ kiện bị tờ rơi quảng cáo đánh tráo khái niệm (`KỊCH_BẢN`):
1. Không hề có sản phẩm nào tên là "Chứng chỉ Đầu tư được bảo hiểm tiền gửi"; hợp đồng thực tế bạn phải ký là **Hợp đồng mua Trái phiếu doanh nghiệp phát hành riêng lẻ** của Công ty P, kèm một giấy xác nhận nhà đầu tư chứng khoán chuyên nghiệp.
2. Ngân hàng X chỉ ký hợp đồng làm "Đại lý quản lý tài sản bảo đảm" (thu phí dịch vụ giữ giấy tờ), hoàn toàn **không ký hợp đồng bảo lãnh thanh toán vô điều kiện** cho lô trái phiếu.
3. Công ty Chứng khoán X chỉ ghi điều khoản *"nỗ lực tối đa hỗ trợ kết nối người mua thứ cấp theo điều kiện thị trường"*, không phải cam kết mua lại bằng tiền của công ty chứng khoán.
4. Trên BCTC của Công ty P, dòng tiền từ hoạt động kinh doanh (`CFO`) âm `-850 tỷ VND` suốt 2 năm liên tiếp, hệ số `EBIT / Lãi vay = 0,4 lần`, và mục đích phát hành lô trái phiếu mới này là để trả nợ cho lô trái phiếu cũ sắp đáo hạn.

### Quy trình bóc tách rủi ro
1. **Bóc trần 3 lớp ảo giác an toàn:**
   - **Ảo giác 1 (Bảo hiểm tiền gửi):** Khoản `2,0 tỷ VND` mua trái phiếu Công ty P có mức bảo hiểm tiền gửi bằng **`0 VND`** (nếu gửi tiết kiệm tại ngân hàng, khoản tiền gửi được bảo vệ theo quy định ngân hàng và có hạn mức bảo hiểm tiền gửi `350 triệu VND`).
   - **Ảo giác 2 (Tài sản bảo đảm bằng cổ phiếu chính tổ chức phát hành):** Đây là rủi ro ngược chiều (`Wrong-Way Risk`) nguy hiểm nhất. Vì Công ty P đang có `EBIT / Lãi vay = 0,4x` và `CFO < 0`, ngay khi Công ty P tuyên bố chậm trả lãi trái phiếu, giá cổ phiếu P sẽ mất thanh khoản và giảm `70%–90%`, làm giá trị tài sản bảo đảm bốc hơi cùng lúc với sự kiện vỡ nợ (`SUY_LUẬN`).
   - **Ảo giác 3 (Thanh khoản trước hạn):** Lời hứa "nỗ lực hỗ trợ tìm người mua" không có giá trị pháp lý bắt buộc mua lại; khi tổ chức phát hành gặp khó khăn, thanh khoản thứ cấp đóng băng hoàn toàn.
2. **Định lượng phần bù rủi ro không tương xứng:** Đổi lấy phần chênh lệch lãi suất `+6,0%/năm` (`120 triệu VND/năm` trước thuế TNCN `5%` trên lãi nhận được), nhà đầu tư hưu trí đang đánh cược toàn bộ **`2.000 triệu VND` vốn gốc** vào một doanh nghiệp không đủ tiền trả lãi vay (`EBIT / Lãi vay = 0,4x`)!

---

## 6. Sai ở đâu? (Bắt lỗi suy luận)

Hãy chỉ ra chỗ sai trong câu nói sau:

> *"Trái phiếu Chính phủ Việt Nam kỳ hạn 10 năm do Kho bạc Nhà nước phát hành hoàn toàn không có rủi ro vỡ nợ, nên giá của Trái phiếu Chính phủ không bao giờ có thể bị giảm. Mua quỹ trái phiếu nắm giữ Trái phiếu Chính phủ kỳ hạn 10 năm thì bất kỳ lúc nào rút tiền ra cũng chỉ có lãi chứ không thể lỗ!"*

### Phân tích chỗ sai
1. **Nhầm lẫn "Không có rủi ro vỡ nợ tín dụng (`Zero Credit Default Risk`)" với "Không có rủi ro biến động giá theo lãi suất (`Zero Interest Rate / Duration Risk`)":**
   - Đúng là nếu bạn giữ Trái phiếu Chính phủ kỳ hạn 10 năm cho đến tận **ngày đáo hạn cuối cùng sau 10 năm**, Kho bạc Nhà nước sẽ trả đủ `100%` mệnh giá gốc và các kỳ lãi cuống phiếu đã hứa (`SỰ_THẬT`).
   - Nhưng trong suốt 10 năm trước khi đáo hạn, giá thị trường mỗi ngày của trái phiếu đó biến động **ngược chiều với lợi suất thị trường (`YTM`)** theo công thức $\Delta P / P \approx -D_{\text{Mod}} \times \Delta y$!
2. **Ví dụ định lượng:** Một Trái phiếu Chính phủ kỳ hạn 10 năm có lãi suất cuống phiếu `2,8%/năm` thường có `Modified Duration` khoảng **`8,4 năm`**. Nếu lạm phát tăng khiến lợi suất Trái phiếu Chính phủ 10 năm trên thị trường thứ cấp tăng từ `2,8%/năm` lên `4,8%/năm` ($\Delta y = +2,0\%$), thì giá thị trường của trái phiếu đó lập tức **sụt giảm khoảng $-8,4 \times 2,0\% = -16,8\%$** (`PHÉP_TÍNH`)! Nếu bạn rút tiền khỏi quỹ trái phiếu kỳ hạn dài ngay lúc lãi suất tăng đó, bạn vẫn bị lỗ vốn thực tế như thường.

---

## 7. Bài tập (10 câu)

1. Một cá nhân gửi tiết kiệm có kỳ hạn `400 triệu VND` tại Ngân hàng A với lãi suất đơn `5,4%/năm` trong kỳ hạn 6 tháng (`182 ngày`, tính trên cơ sở 365 ngày/năm). Tính số tiền lãi và tổng gốc + lãi thu về khi đáo hạn. Nếu cá nhân đó cần tiền đột xuất và rút toàn bộ sổ tiết kiệm ở ngày thứ 170 (lãi suất không kỳ hạn áp dụng khi rút trước hạn là `0,2%/năm`), số tiền lãi thực nhận chỉ còn bao nhiêu?
2. Ông Bình có 3 cuốn sổ tiết kiệm bằng `VND` đứng tên mình tại cùng một Ngân hàng thương mại X, mỗi sổ có gốc và lãi cộng dồn là `180 triệu VND` (tổng cộng `540 triệu VND` tại Ngân hàng X), và 1 sổ tiết kiệm `250 triệu VND` tại Ngân hàng thương mại Y. Theo quy định về hạn mức trả tiền bảo hiểm `350 triệu VND` tại Thông tư `05/2026/TT-NHNN`, tổng số tiền gửi được thuộc hạn mức chi trả tối đa của Bảo hiểm tiền gửi Việt Nam cho Ông Bình tại Ngân hàng X và tại Ngân hàng Y lần lượt là bao nhiêu?
3. Phân biệt 3 khái niệm pháp lý trong một đợt phát hành trái phiếu doanh nghiệp: (a) **Tổ chức phát hành (`Issuer`)**; (b) **Tổ chức tư vấn, đại lý phát hành / phân phối (`Distributor`)**; và (c) **Tổ chức bảo lãnh thanh toán (`Payment Guarantor`)**.
4. Một trái phiếu có mệnh giá $F = 100.000.000\text{ VND}$ (`100 triệu VND`), trả lãi cuống phiếu cố định $c = 8,0\%/\text{năm}$ (`8 triệu VND` vào cuối mỗi năm) và còn đúng $T = 2\text{ năm}$ nữa là đáo hạn. Hãy tính giá hợp lý của trái phiếu này trong 3 trường hợp lợi suất đáo hạn thị trường yêu cầu ($y$) lần lượt là: (a) $y = 8,0\%/\text{năm}$; (b) $y = 10,0\%/\text{năm}$; và (c) $y = 6,0\%/\text{năm}$.
5. Với trái phiếu 2 năm trả lãi cuống phiếu $c = 8,0\%/\text{năm}$ ở Câu 4 đang giao dịch tại mức lợi suất đáo hạn $y = 8,0\%/\text{năm}$ (giá $P = 100\text{ triệu VND}$), hãy sử dụng công thức trong mô-đun [`../practice/models/market_returns.py`](../practice/models/market_returns.py) để tính: (a) Thời lượng `Macaulay Duration` ($D_{\text{Mac}}$); và (b) Thời lượng điều chỉnh `Modified Duration` ($D_{\text{Mod}}$).
6. Một danh mục Trái phiếu Chính phủ của công ty bảo hiểm có tổng giá trị thị trường là `10.000 tỷ VND` và có `Modified Duration` bình quân là $D_{\text{Mod}} = 7,5\text{ năm}$. Nếu mặt bằng lợi suất Trái phiếu Chính phủ trên thị trường tăng thêm `+1,20%/năm` (`+120 bps`), giá trị thị trường của danh mục trái phiếu này ước tính giảm bao nhiêu phần trăm và giảm bao nhiêu tỷ VND (theo xấp xỉ bậc nhất của `Duration`)?
7. Một trái phiếu doanh nghiệp niêm yết có mệnh giá `100.000 VND`, lãi suất cuống phiếu `10,0%/năm` trả lãi hằng năm. Lưu ý rằng tại Việt Nam, khi cá nhân nhận tiền lãi trái phiếu doanh nghiệp hoặc bán chuyển nhượng trái phiếu, cá nhân phải chịu thuế thu nhập cá nhân theo quy định (giả sử thuế TNCN khấu trừ tại nguồn đối với tiền lãi đầu tư vốn là `5%` trên số tiền lãi nhận được). Nếu nhà đầu tư mua trái phiếu ở đúng mệnh giá `100.000 VND` và giữ đến đáo hạn 1 năm, số tiền lãi ròng sau thuế `5%` và lợi suất ròng sau thuế là bao nhiêu?
8. Trái phiếu Chính phủ kỳ hạn 5 năm đang có lợi suất $y_{\text{TPCP}} = 2,90\%/\text{năm}$. Trái phiếu của Doanh nghiệp Bất động sản M cùng kỳ hạn 5 năm đang được chào bán với lợi suất $y_{\text{TPDN}} = 11,40\%/\text{năm}$. Tính mức chênh lệch lợi suất (`Credit & Liquidity Spread`) của trái phiếu Doanh nghiệp M so với Trái phiếu Chính phủ. Nếu xác suất vỡ nợ hằng năm của Doanh nghiệp M ước tính là $PD = 12\%/\text{năm}$ và tỷ lệ mất vốn khi vỡ nợ là $LGD = 75\%$, mức tổn thất kỳ vọng hằng năm ($EL = PD \times LGD$) là bao nhiêu và phần bù `Spread` có đủ bù đắp tổn thất kỳ vọng không?
9. Giải thích vì sao một lô trái phiếu doanh nghiệp được đảm bảo bằng **"quyền tài sản phát sinh từ dự án bất động sản hình thành trong tương lai chưa có Giấy phép xây dựng"** lại có khả năng thu hồi nợ rất thấp khi chủ đầu tư mất thanh khoản (tham chiếu ví dụ Sông Đà Thăng Long tại `PVI` trong Mục 4.2).
10. Mở mô-đun [`../practice/models/insurance.py`](../practice/models/insurance.py), giải thích cách hàm `alm_duration_gap` kết hợp `Modified Duration` của danh mục trái phiếu (Bài `A1`) với `Modified Duration` của dự phòng toán học bảo hiểm (Bài `F8`) để đo rủi ro bảng cân đối kế toán khi lãi suất thay đổi.

---

## 8. Đáp án chi tiết

1. **Tính lãi tiền gửi đúng hạn (182 ngày) so với rút trước hạn (170 ngày):**
   - Lãi đúng hạn 182 ngày ($5,4\%/\text{năm}$): $400.000.000 \times 5,4\% \times \frac{182}{365} = 10.770.411\text{ VND}$ (Tổng thu về = `410.770.411 VND`).
   - Nếu rút trước hạn ở ngày thứ 170 (chỉ hưởng lãi không kỳ hạn $0,2\%/\text{năm}$):
     $$\text{Tiền lãi rút trước hạn} = 400.000.000 \times 0,2\% \times \frac{170}{365} = 372.603\text{ VND}\quad (\text{mất hơn }10,39\text{ triệu VND tiền lãi!})\quad (\text{PHÉP\_TÍNH})$$
2. **Hạn mức Bảo hiểm tiền gửi theo Thông tư `05/2026/TT-NHNN` (`350 triệu VND/người/tổ chức`):**
   - Tại Ngân hàng X: Tổng tiền gửi gốc và lãi của Ông Bình là `540 triệu VND`, vượt hạn mức `350 triệu VND`, nên số tiền thuộc hạn mức chi trả tối đa của Bảo hiểm tiền gửi tại Ngân hàng X là **`350 triệu VND`** (chứ không phải $3 \times 180 = 540\text{ triệu VND}$).
   - Tại Ngân hàng Y: Tổng tiền gửi là `250 triệu VND` ($\le 350\text{ triệu VND}$), nên được bảo hiểm toàn bộ **`250 triệu VND`** (`PHÉP_TÍNH` & `SỰ_THẬT`).
3. **Phân biệt 3 chủ thể trong phát hành TPDN:**
   - (a) `Tổ chức phát hành`: Doanh nghiệp đi vay tiền và là người chịu trách nhiệm pháp lý trả gốc, lãi.
   - (b) `Tổ chức phân phối / đại lý`: Ngân hàng hoặc CTCK làm trung gian giới thiệu, thu phí dịch vụ; **không có nghĩa vụ trả nợ thay** khi tổ chức phát hành vỡ nợ.
   - (c) `Tổ chức bảo lãnh thanh toán`: Chỉ khi một ngân hàng/tổ chức tài chính ký cam kết bảo lãnh thanh toán rõ ràng trong hợp đồng phát hành thì họ mới có nghĩa vụ trả gốc/lãi thay khi tổ chức phát hành không trả được (`SỰ_THẬT`).
4. **Định giá trái phiếu 2 năm ($F = 100\text{ triệu}$, $C = 8\text{ triệu/năm}$):**
   - (a) Khi $y = 8,0\%$: $P = \frac{8}{1,08} + \frac{108}{1,08^2} = 7,4074 + 92,5926 = 100,0000\text{ triệu VND}$ (`At Par`).
   - (b) Khi $y = 10,0\%$: $P = \frac{8}{1,10} + \frac{108}{1,10^2} = 7,2727 + 89,2562 = 96,5289\text{ triệu VND}$ (`Discount`).
   - (c) Khi $y = 6,0\%$: $P = \frac{8}{1,06} + \frac{108}{1,06^2} = 7,5472 + 96,1196 = 103,6668\text{ triệu VND}$ (`Premium`) (`PHÉP_TÍNH`).
5. **Tính `Macaulay Duration` và `Modified Duration` ($T = 2$, $c = 8\%$, $y = 8\%$, $P = 100$):**
   - (a) $D_{\text{Mac}} = \frac{1 \times 7,4074 + 2 \times 92,5926}{100,0000} = \frac{192,5926}{100,0000} = 1,9259\text{ năm}$.
   - (b) $D_{\text{Mod}} = \frac{1,9259}{1,08} = 1,7833\text{ năm}$ (`PHÉP_TÍNH`).
6. **Ước tính mức sụt giảm giá trị danh mục TPCP (`10.000 tỷ VND`, $D_{\text{Mod}} = 7,5\text{ năm}$, $\Delta y = +1,20\%$):**
   - Phần trăm biến động giá ước tính: $\frac{\Delta P}{P} \approx -7,5 \times (+1,20\%) = -9,00\%$.
   - Mức sụt giảm giá trị thị trường: $-9,00\% \times 10.000\text{ tỷ VND} = -900\text{ tỷ VND}$ (`PHÉP_TÍNH`).
7. **Tính lãi ròng và lợi suất sau thuế TNCN `5%` trên lãi trái phiếu:**
   - Tiền lãi gộp trước thuế = $100.000 \times 10,0\% = 10.000\text{ VND}$.
   - Thuế TNCN khấu trừ `5%` trên tiền lãi = $10.000 \times 5\% = 500\text{ VND}$.
   - Tiền lãi ròng thực nhận = $10.000 - 500 = 9.500\text{ VND} \implies \text{Lợi suất ròng sau thuế} = 9.500 / 100.000 = 9,50\%/\text{năm}$ (`PHÉP_TÍNH`).
8. **Kiểm định `Credit Spread` so với Tổn thất kỳ vọng ($EL = PD \times LGD$):**
   - `Spread` = $11,40\% - 2,90\% = 8,50\%/\text{năm}$ (`850 bps`).
   - Tổn thất kỳ vọng hằng năm ($EL$) = $PD \times LGD = 12\% \times 75\% = 9,00\%/\text{năm}$ (`900 bps`).
   - Vì `Spread` (`8,50%/năm`) **thấp hơn** mức tổn thất kỳ vọng (`9,00%/năm`), chưa kể phần bù thanh khoản và thuế, nên lợi suất kỳ vọng điều chỉnh rủi ro của trái phiếu Doanh nghiệp M thực chất còn thấp hơn cả Trái phiếu Chính phủ (`PHÉP_TÍNH` & `SUY_LUẬN`)!
9. **Vì sao quyền tài sản dự án chưa có GPXD có khả năng thu hồi thấp:**
   - Khi dự án chưa hoàn tất pháp lý và chưa có Giấy phép xây dựng, dự án không đủ điều kiện chuyển nhượng thương mại hoặc mở bán ngay để thu tiền mặt; quá trình hoàn thiện pháp lý và xử lý tài sản thế chấp khi chủ đầu tư vỡ nợ thường bị đình trệ nhiều năm (như trường hợp Sông Đà Thăng Long tại `PVI`).
10. **Liên kết `alm_duration_gap` trong [`../practice/models/insurance.py`](../practice/models/insurance.py):**
    - Hàm `alm_duration_gap` lấy `Modified Duration` của Tài sản trái phiếu trừ đi `Modified Duration` của Nợ dự phòng toán học (có điều chỉnh quy mô $L/A$) để đo mức thay đổi Vốn chủ sở hữu kinh tế khi lãi suất thị trường dịch chuyển $\Delta y$.

---

## 9. Kiểm tra chuyển bài (Transfer Check)

Trước khi chuyển sang Bài [A2 — Quỹ mở, ETF, chi phí và sai lệch theo dõi](A2-mutual-funds-etfs-fees.md), hãy tự kiểm tra 3 kỹ năng sau:
1. **Chuyển từ Trái phiếu đơn lẻ (`A1`) sang Quỹ Trái phiếu / ETF (`A2`):** Thay vì tự mua lẻ một lô trái phiếu doanh nghiệp, nhiều nhà đầu tư mua chứng chỉ **Quỹ mở trái phiếu (`Bond Mutual Fund`)**. Bạn đã sẵn sàng dùng công thức `NAV/đơn vị`, `Duration` bình quân danh mục và biểu phí quản lý ở Bài [A2](A2-mutual-funds-etfs-fees.md) để kiểm tra xem bên trong quỹ trái phiếu đó đang giữ Trái phiếu Chính phủ/Tiền gửi hay đang giữ Trái phiếu doanh nghiệp bất động sản chưa?
2. **Phản xạ bảo vệ tiền gia đình:** Khi người thân trong gia đình được mời chào gửi tiền hưởng lãi suất cao bất thường, bạn đã nhớ 3 câu hỏi kiểm tra ngay lập tức: (1) Hợp đồng ghi tên sản phẩm là "Tiền gửi tiết kiệm" hay "Hợp đồng mua bán trái phiếu"? (2) Tổ chức phát hành là ai? và (3) Khoản tiền đó có thuộc diện Bảo hiểm tiền gửi `350 triệu VND` không?
3. **Thực hành Python:** Bạn đã chạy thử hàm `bond_price`, `macaulay_duration` và `modified_duration` trong [`../practice/models/market_returns.py`](../practice/models/market_returns.py) chưa?

---

## 10. Lỗi thường gặp và ranh giới an toàn

- **Bốn lỗi phân tích phổ biến:** (1) Nhầm trái phiếu doanh nghiệp được bán tại quầy ngân hàng với tiền gửi tiết kiệm có bảo hiểm; (2) Nhầm ngân hàng làm đại lý quản lý tài sản bảo đảm với ngân hàng bảo lãnh thanh toán vô điều kiện; (3) Tưởng hạn mức bảo hiểm tiền gửi `350 triệu VND` được nhân lên theo số lượng cuốn sổ tiết kiệm mở tại cùng một ngân hàng; (4) Tưởng Trái phiếu Chính phủ không có rủi ro giảm giá thị trường khi lãi suất tăng.
- **Ranh giới an toàn:** Bài học cung cấp kiến thức tài chính và công thức định giá thu nhập cố định; không đưa ra báo giá hay khuyến nghị mua/bán bất kỳ sản phẩm tiền gửi hay trái phiếu cụ thể nào.

## Nguồn Internet đã mở

- Chốt kiểm tra trực tuyến lúc `2026-11-05 12:15 UTC+7`:
  1. [Bảo hiểm tiền gửi Việt Nam (DIV) — Phạm vi bảo hiểm tiền gửi cá nhân bằng VND](https://www.div.gov.vn/bao-hiem-tien-gui-chi-ap-dung-doi-voi-tien-gui-cua-ca-nhan-bang-dong-viet-nam) và [Thông tư số 05/2026/TT-NHNN](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/05-nhnn.pdf) quy định hạn mức trả tiền bảo hiểm `350 triệu VND`.
  2. [Cổng Thông tin Chính phủ — Bộ Tài chính khuyến cáo các chủ thể tham gia thị trường trái phiếu doanh nghiệp](https://xaydungchinhsach.chinhphu.vn/nong-bo-tai-chinh-khuyen-cao-cac-chu-the-tham-gia-thi-truong-trai-phieu-doanh-nghiep-119221114165946867.htm).
  3. [SEC Investor.gov — Bonds](https://www.investor.gov/introduction-investing/investing-basics/investment-products/bonds-or-fixed-income-products/bonds) và [Interest Rate Risk — When Interest Rates Go Up, Prices of Fixed-Rate Bonds Fall](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-86).
  4. Hồ sơ đã kiểm duyệt: [`../../research/companies/VN/BVH/report.md`](../../research/companies/VN/BVH/report.md) (Thuyết minh 7 danh mục TPCP) và [`../../research/companies/VN/PVI/report.md`](../../research/companies/VN/PVI/report.md) (Thuyết minh 6a & 7 trái phiếu quá hạn Sông Đà Thăng Long).
