# Bài A2 — Quỹ mở (Mutual Funds), Quỹ hoán đổi danh mục (ETF), Cấu trúc Chi phí và Sai lệch Theo dõi Chỉ số

- Ngày cập nhật: `2026-11-05`
- Chốt dữ liệu lúc: `2026-11-05 12:15 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Phân biệt cơ chế tạo lập – giao dịch của Quỹ mở (`Open-End Mutual Fund`) và Quỹ hoán đổi danh mục (`Exchange-Traded Fund — ETF`); tính chính xác Giá trị tài sản ròng trên một đơn vị quỹ (`NAV/CCQ`), chênh lệch giá khớp lệnh trên sàn so với `iNAV` (`Premium / Discount`); bóc tách phí ẩn trong `NAV` (`TER`) với phí giao dịch trả riêng; và tính toán thành thạo hai thước đo bám sát chỉ số là `Tracking Difference (TD)` và `Tracking Error (TE)`.
- Thời lượng dự kiến: `3 buổi học (~270 phút)`
  - **Buổi 1 (90 phút):** Cơ chế vận hành của Quỹ mở và `ETF` — Cách tính `NAV/đơn vị`, thị trường sơ cấp (`AP` và lô hoán đổi `Creation/Redemption Basket`) và thị trường thứ cấp trên sàn chứng khoán (`Premium / Discount`).
  - **Buổi 2 (90 phút):** Giải phẫu toàn bộ các tầng chi phí của quỹ đầu tư — Phí quản lý thường niên (`Management Fee` / `TER`) ăn mòn lãi kép như thế nào so với Phí phát hành (`Front-end Load`), Phí mua lại (`Redemption Fee`), chênh lệch giá mua-bán (`Bid-Ask Spread`) và thuế.
  - **Buổi 3 (90 phút):** Toán học về Độ lệch theo dõi chỉ số (`Tracking Difference` vs. `Tracking Error`), đọc Bản cáo bạch và Điều lệ quỹ tại Việt Nam, xử lý dữ liệu bẩn và giải 10 bài tập định lượng.
- Bài trước liên quan: [N5 — Danh mục và đầu tư chỉ số](N5-portfolio-index-investing.md), [B1 — Phí môi giới, lưu ký và thuế giao dịch](B1-broker-fees-custody.md), [A1 — Tiền gửi và trái phiếu](A1-deposits-government-corporate-bonds.md), [P4 — Hợp đồng bảo hiểm cá nhân và chi phí](P4-personal-insurance-contracts-and-costs.md).
- Mô hình thực hành đi kèm: [`../practice/models/market_returns.py`](../practice/models/market_returns.py) và [`../practice/models/risk_performance.py`](../practice/models/risk_performance.py).
- Câu hỏi cốt lõi: Vì sao một quỹ đầu tư quảng cáo "lợi nhuận danh mục đạt 12%/năm", nhưng sau khi trừ phí quản lý 2%/năm, phí mua/bán chứng chỉ quỹ và độ lệch theo dõi, số tiền thực tế nằm lại trong tài khoản của bạn sau 15 năm lại hụt mất hơn một phần tư?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/A2-fact-check.md), [phản biện](../reviews/A2-risk-review.md).

---

## Hiểu bài trong một phút

Quỹ đầu tư đại chúng là phương tiện gom vốn của nhiều nhà đầu tư để nắm giữ một danh mục cổ phiếu, trái phiếu hoặc tiền gửi dưới sự giám sát của Ngân hàng giám sát độc lập. Tuy nhiên, không phải mọi chứng chỉ quỹ đều giao dịch giống nhau và không phải mọi khoản phí đều hiển thị trên hóa đơn mua bán:
1. **Quỹ mở (`Mutual Fund`) giao dịch trực tiếp với Công ty quản lý quỹ tại mức giá `NAV/đơn vị` cuối ngày định giá**, trong khi **Quỹ `ETF` giao dịch liên tục trong phiên trên Sở Giao dịch Chứng khoán như một cổ phiếu thông thường** tại mức giá thị trường có thể cao hơn (`Premium`) hoặc thấp hơn (`Discount`) so với `NAV/đơn vị` (`SỰ_THẬT`).
2. **Có hai nhóm chi phí tuyệt đối không được nhầm lẫn hoặc cộng trùng:**
   - **Chi phí hoạt động nội tại của quỹ (`Total Expense Ratio — TER`):** Gồm phí quản lý quỹ, phí ngân hàng giám sát, phí lưu ký, phí kiểm toán. Khoản này được **trích trừ tự động mỗi ngày trực tiếp vào tài sản quỹ trước khi công bố `NAV/đơn vị`**. Do đó, lợi suất tăng trưởng `NAV/đơn vị` mà quỹ công bố đã trừ sẵn `TER` rồi (`SỰ_THẬT`).
   - **Chi phí giao dịch bên ngoài của nhà đầu tư:** Gồm phí phát hành (khi mua quỹ mở), phí mua lại (khi bán quỹ mở), hoặc phí môi giới + thuế bán `0,1%` + chênh lệch giá đặt mua/bán (`Bid-Ask Spread`) khi giao dịch `ETF` trên sàn (`SỰ_THẬT`).
3. **Phân biệt `Tracking Difference (TD)` và `Tracking Error (TE)`:** `Tracking Difference` là mức chênh lệch lợi suất cộng dồn giữa quỹ và chỉ số tham chiếu trong một kỳ ($R_{\text{Quỹ}} - R_{\text{Chỉ số}}$), còn `Tracking Error` là **độ lệch chuẩn quy đổi theo năm của chuỗi chênh lệch lợi suất định kỳ**, đo độ rung lắc/thiếu ổn định của việc bám sát chỉ số (`SỰ_THẬT`).

---

## Buổi 1 — Cơ chế vận hành Quỹ mở vs. ETF và Công thức NAV, Premium/Discount

### 1.1. Giá trị tài sản ròng trên một đơn vị quỹ (`NAV per Unit`)

Theo định nghĩa của [SEC Hoa Kỳ — Net Asset Value](https://www.investor.gov/introduction-investing/investing-basics/glossary/net-asset-value), tại mỗi kỳ định giá, Giá trị tài sản ròng của quỹ (`Total NAV`) và `NAV` trên mỗi đơn vị chứng chỉ quỹ (`NAV/CCQ`) được xác định bằng:

$$\text{Total NAV} = \text{Tổng giá trị tài sản của quỹ (Cổ phiếu + Trái phiếu + Tiền gửi + Cổ tức/Lãi dự thu)} - \text{Tổng nợ phải trả của quỹ (Phí quản lý, phí giám sát, phải trả mua chứng khoán)}$$

$$\text{NAV/đơn vị} = \frac{\text{Total NAV}}{\text{Tổng số đơn vị chứng chỉ quỹ đang lưu hành}}$$

### 1.2. Sự khác biệt cấu trúc giữa Quỹ mở và ETF (`AP` & Cơ chế Kinh doanh chênh lệch giá)

Theo tài liệu [SEC — Characteristics of Mutual Funds and Exchange-Traded Funds](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/characteristics-mutual-funds-exchange-traded-funds):

| Tiêu chí | Quỹ mở (`Open-End Mutual Fund`) | Quỹ hoán đổi danh mục (`ETF`) |
|---|---|---|
| **Cách nhà đầu tư cá nhân mua/bán** | Đặt lệnh mua (`Subscription`) hoặc bán lại (`Redemption`) trực tiếp với Công ty quản lý quỹ / đại lý phân phối trước giờ đóng sổ lệnh (`Cut-off time`). | Đặt lệnh mua/bán khớp lệnh liên tục trong phiên trên sàn chứng khoán (`HOSE`) thông qua tài khoản chứng khoán cá nhân. |
| **Giá khớp lệnh** | Luôn khớp theo đúng một mức giá **`NAV/đơn vị`** tính vào cuối ngày giao dịch (`Forward Pricing` — lúc đặt lệnh bạn chưa biết chính xác `NAV` cuối ngày là bao nhiêu) cộng/trừ phí phát hành/mua lại. | Khớp theo **giá thị trường trên bảng điện ($P_{\text{ETF}}$)** tại thời điểm đặt lệnh. Trong phiên, sàn công bố giá trị tài sản ròng tham chiếu theo thời gian thực gọi là `iNAV`. |
| **Cơ chế tạo lập đơn vị quỹ mới** | Khi bạn nộp tiền mặt vào mua, quỹ phát hành thêm đơn vị quỹ mới; khi bạn bán rút tiền, quỹ hủy đơn vị quỹ đó (nếu rút ròng lớn, quỹ phải bán bớt cổ phiếu trong danh mục để lấy tiền mặt trả cho bạn). | Trên thị trường sơ cấp, chỉ các **Thành viên lập quỹ (`Authorized Participants — AP`, thường là các CTCK lớn)** mới được đem một "rổ cổ phiếu cơ sở" (`Creation Basket`, ví dụ 1 lô = `100.000` chứng chỉ ETF) đổi lấy chứng chỉ ETF mới hoặc ngược lại. |

### 1.3. Chênh lệch giá thị trường ETF so với NAV (`Premium` và `Discount`)

Tỷ lệ phụ trội (`Premium`) hoặc chiết khấu (`Discount`) của thị giá `ETF` ($P_{\text{ETF}}$) so với `NAV/đơn vị` được tính bằng:

$$\text{Premium / Discount (\%)} = \frac{P_{\text{ETF}} - \text{NAV/đơn vị}}{\text{NAV/đơn vị}}$$

- Khi $P_{\text{ETF}} > \text{NAV/đơn vị}$ (ví dụ `NAV = 20.000 VND`, giá trên sàn `20.400 VND`, tức `Premium = +2,0%`): Nếu mức `Premium` này lớn hơn chi phí giao dịch hoán đổi, các Thành viên lập quỹ (`AP`) sẽ mua rổ cổ phiếu cơ sở ngoài thị trường với giá `20.000 VND`, đem hoán đổi lấy chứng chỉ ETF mới rồi bán ra sàn thu `20.400 VND`, qua đó kéo giá `ETF` lùi về sát `NAV` (`SUY_LUẬN`).
- *Cảnh báo thanh khoản ([SEC — ETF Investor Bulletin](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-24)):* Với các `ETF` có thanh khoản thưa thớt, biên độ dao động thị trường căng cứng (cổ phiếu cơ sở tăng trần/giảm sàn mất thanh khoản) hoặc bị giới hạn tỷ lệ sở hữu nước ngoài (`Foreign Room` tại Việt Nam), cơ chế kinh doanh chênh lệch giá của `AP` có thể bị nghẽn, làm `Premium` hoặc `Discount` giãn rộng bất thường. Nhà đầu tư cá nhân mua ở đỉnh `Premium +3%` và bán ra lúc `Discount -2%` sẽ mất oan `5%` ngay cả khi `NAV` không đổi (`PHÉP_TÍNH` & `SUY_LUẬN`)!

---

## Buổi 2 — Giải phẫu Các tầng Chi phí và Sức tàn phá Lãi kép của Phí Quản lý

### 2.1. Bảng phân tách Chi phí lấy từ Tài sản Quỹ vs. Chi phí thu trực tiếp từ Nhà đầu tư

Theo hướng dẫn của [SEC — Mutual Fund and ETF Fees and Expenses (`23/07/2025`)](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/mutual-fund-and-etf-fees-and-expenses-investor-bulletin), khi đánh giá một quỹ đầu tư, bạn phải kiểm tra 2 bảng phí tách biệt:

1. **Nhóm 1 — Phí giao dịch trả một lần khi Mua / Bán (`Transaction Fees`):**
   - Với **Quỹ mở**: Phí phát hành (`Front-end Load` — trừ ngay vào số tiền nộp vào mua) và Phí mua lại/rút vốn (`Back-end Load / Redemption Fee` — thường giảm dần theo thời gian nắm giữ, ví dụ giữ dưới 6 tháng thu `1,5%–2,0%`, giữ trên 24 tháng thu `0%`).
   - Với **ETF**: Phí môi giới trả cho công ty chứng khoán (`0,1%–0,25%`), chênh lệch giá đặt mua – đặt bán trên bảng điện (`Bid-Ask Spread`), và thuế thu nhập cá nhân khi bán chứng chỉ quỹ trên sàn (`0,1%` trên giá trị bán tại Việt Nam).
2. **Nhóm 2 — Chi phí hoạt động thường niên trừ ngầm vào NAV (`Ongoing Operating Expenses — TER`):**
   - Gồm Phí quản lý quỹ (`Management Fee`: quỹ ETF thụ động thường thu `0,5%–0,8%/năm`; quỹ mở cổ phiếu chủ động tại Việt Nam thường thu `1,5%–2,0%/năm`), cộng phí giám sát, lưu ký, quản trị quỹ và kiểm toán.
   - Ngoài ra còn có **Chi phí giao dịch danh mục bên trong quỹ (`Portfolio Turnover Cost`)**: Một quỹ chủ động mua đi bán lại cổ phiếu liên tục (vòng quay danh mục `200%–300%/năm`) sẽ tốn thêm một khoản phí môi giới và thuế bán từ `0,3%–0,6%/năm` trừ thẳng vào tài sản quỹ mà không nằm trong con số phí quản lý niêm yết (`SUY_LUẬN`)!

### 2.2. Công thức định lượng tác động của Phí lên Giá trị tài sản cuối kỳ

Giả sử bạn đầu tư số tiền ban đầu $V_0$, chịu phí mua ban đầu $f_{\text{mua}}$, danh mục tài sản gốc trước phí sinh lời bình quân $r_{\text{gộp}}/\text{năm}$, tỷ lệ chi phí hoạt động thường niên của quỹ là $\text{TER}/\text{năm}$ (nên lợi suất tăng trưởng `NAV` ròng mỗi năm là $r_{\text{NAV}} \approx r_{\text{gộp}} - \text{TER}$), giữ trong $n$ năm và chịu phí bán lại cuối kỳ $f_{\text{bán}}$. Giá trị tiền mặt thực thu về cuối kỳ ($V_n$) là:

$$V_n = V_0 \times (1 - f_{\text{mua}}) \times \left(1 + r_{\text{gộp}} - \text{TER}\right)^n \times (1 - f_{\text{bán}})$$

Khoản chênh lệch $\text{TER}$ nhìn có vẻ nhỏ (`1,5%/năm` so với `0,5%/năm`) nhưng vì nó nằm ở **số mũ $n$ của hàm lũy thừa**, sau 15–20 năm nó sẽ ăn mòn hàng chục phần trăm tổng tài sản cuối kỳ (tương tự cơ chế trong mô-đun [`../practice/models/market_returns.py`](../practice/models/market_returns.py)).

---

## Buổi 3 — Hai thước đo Bám sát Chỉ số: Tracking Difference (TD) và Tracking Error (TE)

### 3.1. Công thức chuẩn quốc tế phân biệt `Tracking Difference` và `Tracking Error`

Theo tài liệu phương pháp của [Sở Giao dịch Chứng khoán Quốc gia Ấn Độ (`NSE — Tracking Error`)](https://www.nseindia.com/static/products-services/indices-tracking-error) và quy định của [Ủy ban Chứng khoán và Giao dịch Ấn Độ (`SEBI — Circular on Passive Funds`, Mục V)](https://www.sebi.gov.in/sebi_data/attachdocs/may-2022/1653307308174.pdf), đối với một quỹ mô phỏng chỉ số (`Index Fund` hoặc `ETF`):

1. **Chênh lệch theo dõi (`Tracking Difference — TD`):** Là hiệu số đơn giản giữa lợi suất của `NAV` quỹ ($R_{p, t}$) và lợi suất của chỉ số tham chiếu ($R_{b, t}$) trong một kỳ xác định (ví dụ 1 năm):
   $$\text{TD}_t = R_{p, t} - R_{b, t}$$
   Trong điều kiện lý tưởng nếu quỹ nắm giữ đúng y hệt tỷ trọng chỉ số, `TD` trong 1 năm sẽ âm và xấp xỉ bằng trừ đi tổng chi phí hoạt động của quỹ ($\text{TD} \approx -\text{TER}$), hoặc có thể đỡ âm hơn một chút nếu chỉ số tham chiếu là chỉ số giá (`Price Index` chưa cộng cổ tức tiền mặt) trong khi quỹ được nhận cổ tức tiền mặt từ các cổ phiếu trong rổ (`SUY_LUẬN`).

2. **Sai số theo dõi (`Tracking Error — TE`):** Là **độ lệch chuẩn mẫu (`Sample Standard Deviation`) quy đổi theo năm của chuỗi chênh lệch lợi suất định kỳ** $d_t = R_{p, t} - R_{b, t}$ qua $M$ kỳ quan sát (với $k$ là số kỳ trong một năm: $k = 250$ nếu tính theo ngày giao dịch, $k = 52$ theo tuần, $k = 12$ theo tháng, $k = 4$ theo quý):
   $$\bar{d} = \frac{1}{M} \sum_{t=1}^{M} d_t, \qquad \text{TE}_{\text{năm}} = \sqrt{k} \times \sqrt{\frac{1}{M - 1} \sum_{t=1}^{M} (d_t - \bar{d})^2}$$

*Quy tắc kiểm chứng bắt buộc (`SỰ_THẬT`):* **Tuyệt đối không bao giờ lấy chênh lệch lợi suất của một kỳ đơn lẻ ($\text{TD}_t$) rồi gọi đó là `Tracking Error`!** Để tính `Tracking Error`, bắt buộc phải có một chuỗi thời gian nhiều kỳ quan sát ($M \ge 2$) để tính độ lệch chuẩn.

---

## 4. Ví dụ từ nguồn thật: Đối chiếu Chuẩn mực SEC Hoa Kỳ, Quy định SEBI/NSE và Tính toán Tái lập

1. **Đối chiếu nguồn chuẩn mực quốc tế (`SEC`, `NSE`, `SEBI`):**
   - `SỰ_THẬT`: Các ấn phẩm giáo dục nhà đầu tư chính thức của [SEC Hoa Kỳ (`23/07/2025`)](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/mutual-fund-and-etf-fees-and-expenses-investor-bulletin) và quy định về quỹ thụ động của [SEBI (`23/05/2022`)](https://www.sebi.gov.in/sebi_data/attachdocs/may-2022/1653307308174.pdf) yêu cầu tách bạch minh bạch giữa: (a) độ trôi trung bình do chi phí (`Tracking Difference`) và (b) độ biến động của sai lệch cấu trúc danh mục (`Tracking Error`).

2. **Ví dụ tính toán tái lập `Tracking Difference` và `Tracking Error` theo 4 quý:**
   Giả sử trong 4 quý của năm 2025 ($M = 4, k = 4$), một quỹ `ETF` mô phỏng chỉ số có lợi suất `NAV` theo quý ($R_{p, t}$) và lợi suất chỉ số tham chiếu ($R_{b, t}$) như sau (`KỊCH_BẢN`):
   - Quý 1: $R_{p, 1} = +5,80\%$, $R_{b, 1} = +6,00\% \implies d_1 = -0,20\%$;
   - Quý 2: $R_{p, 2} = -3,30\%$, $R_{b, 2} = -3,00\% \implies d_2 = -0,30\%$;
   - Quý 3: $R_{p, 3} = +8,10\%$, $R_{b, 3} = +8,20\% \implies d_3 = -0,10\%$;
   - Quý 4: $R_{p, 4} = +1,80\%$, $R_{b, 4} = +2,00\% \implies d_4 = -0,20\%$.
   - **Phép tính tái lập (`PHÉP_TÍNH`):**
     - Trung bình chênh lệch theo quý:
       $$\bar{d} = \frac{-0,20\% + (-0,30\%) + (-0,10\%) + (-0,20\%)}{4} = -0,20\%/\text{quý}$$
     - Phương sai mẫu của chênh lệch theo quý ($M - 1 = 3$):
       $$s_d^2 = \frac{(0)^2 + (-0,10\%)^2 + (+0,10\%)^2 + (0)^2}{3} = \frac{0,02\%^2}{3} = 0,006667\%^2 \implies s_d = 0,08165\%/\text{quý}$$
     - **Sai số theo dõi quy đổi theo năm (`Annualized Tracking Error`):**
       $$\text{TE}_{\text{năm}} = \sqrt{4} \times 0,08165\% = 2 \times 0,08165\% = 0,1633\%/\text{năm}\; (\approx 16,3\text{ bps/năm})$$
   - Bạn có thể kiểm chứng trực tiếp phép tính độ lệch chuẩn và lợi suất chuỗi thời gian này bằng các hàm trong [`../practice/models/risk_performance.py`](../practice/models/risk_performance.py) và [`../practice/models/market_returns.py`](../practice/models/market_returns.py).

---

## 5. Bài làm với dữ liệu thiếu hoặc lệch (Dirty-Data Exercise)

### Tình huống dữ liệu bẩn
Một nhân viên môi giới gửi cho bạn bảng so sánh giữa **Quỹ mở Cổ phiếu Chủ động A** và **Quỹ ETF Chỉ số B** để thuyết phục bạn mua Quỹ mở A:
> *"Trong năm 2025, danh mục cổ phiếu của Quỹ mở A đạt lợi nhuận gộp trước phí quản lý là +14,5%, cao hơn mức tăng +13,2% của Quỹ ETF B (NAV/đơn vị của ETF B đã công bố). Phí quản lý của Quỹ mở A chỉ có 2,0%/năm, phí phát hành lúc mua là 1,5% và phí mua lại khi rút sau 1 năm là 1,0%. Hơn nữa, tuần trước có phiên giá ETF B trên sàn giảm -2,5% trong khi chỉ số chỉ giảm -1,8%, tức ETF B có Tracking Error lên tới 0,7% chỉ trong 1 ngày!"*

Hãy bóc tách **3 lỗi dữ liệu bẩn và đánh tráo khái niệm** trong lời tư vấn trên!

### Quy trình làm sạch và tính lại lợi nhuận thực nhận (`Apples-to-Apples Comparison`)
1. **Lỗi 1 — So sánh "Lợi nhuận gộp trước phí quản lý" của Quỹ A với "Lợi nhuận `NAV` đã trừ phí" của Quỹ B:**
   - Lợi suất tăng trưởng `NAV/đơn vị` công bố của Quỹ `ETF B` (`+13,2%`) **đã trừ sẵn toàn bộ phí quản lý và chi phí vận hành nội tại (`TER`)** của `ETF B`.
   - Trong khi đó, con số `+14,5%` của Quỹ mở A là lợi nhuận gộp trước khi trừ `TER` (`2,0%/năm` phí quản lý + khoảng `0,2%/năm` phí giám sát/lưu ký = `2,2%/năm`). Sau khi trừ `TER`, mức tăng `NAV/đơn vị` của Quỹ mở A chỉ còn khoảng $14,5\% - 2,2\% = +12,3\%$, **thấp hơn mức `+13,2%` của `ETF B`** (`PHÉP_TÍNH`)!
2. **Lỗi 2 — Bỏ quên tác động bào mòn của Phí phát hành (`1,5%`) và Phí mua lại (`1,0%`) sau 1 năm nắm giữ:**
   - Nếu bạn bỏ `100 triệu VND` vào Quỹ mở A trong 1 năm:
     $$\text{Tiền thu về từ Quỹ A} = 100 \times (1 - 1,5\%) \times (1 + 12,3\%) \times (1 - 1,0\%) = 98,5 \times 1,123 \times 0,99 = 109,51\text{ triệu VND}\; (\text{lãi ròng }+9,51\%)$$
   - Trong khi nếu mua `ETF B` trên sàn (giả sử mua/bán sát `NAV`, tổng phí môi giới 2 chiều và thuế bán `0,1%` là `0,35%`):
     $$\text{Tiền thu về từ ETF B} \approx 100 \times (1 - 0,125\%) \times (1 + 13,2\%) \times (1 - 0,225\%) = 112,80\text{ triệu VND}\; (\text{lãi ròng }+12,80\%)$$
   - Thực chất, sau 1 năm nhà đầu tư vào Quỹ mở A thu về kém hơn `ETF B` tới **`3,29 triệu VND`** trên mỗi `100 triệu VND` vốn gốc (`PHÉP_TÍNH`)!
3. **Lỗi 3 — Nhầm chênh lệch giá thị trường 1 phiên (`Premium/Discount change`) với `Tracking Error`:**
   - Chênh lệch giữa biến động **giá khớp lệnh trên sàn** của `ETF` với chỉ số trong 1 phiên là biến động của `Premium/Discount` thứ cấp, hoàn toàn **không phải `Tracking Error`** (vốn phải tính bằng độ lệch chuẩn qua nhiều kỳ của chênh lệch giữa **`NAV/đơn vị`** và chỉ số).

---

## 6. Sai ở đâu? (Bắt lỗi suy luận)

Hãy chỉ ra chỗ sai trong phép tính sau của một người mới học:

> *"Báo cáo của Quỹ mở X công bố: ngày 31/12/2024 NAV/đơn vị là 20.000 VND, ngày 31/12/2025 NAV/đơn vị là 22.400 VND (tăng +12,0%). Trong Bản cáo bạch ghi phí quản lý quỹ là 1,8%/năm và phí giám sát là 0,2%/năm (tổng TER = 2,0%/năm). Vậy nếu tôi giữ chứng chỉ quỹ này suốt năm 2025 và chưa bán ra, lợi suất tài sản ròng của tôi chỉ còn 12,0% - 2,0% = 10,0%!"*

### Phân tích chỗ sai
- **Trừ hai lần (`Double Counting`) chi phí hoạt động nội tại của quỹ:**
  - Theo quy định kế toán quỹ đầu tư ([SEC — Mutual Fund Fees](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/mutual-fund-and-etf-fees-and-expenses-investor-bulletin)), phí quản lý (`1,8%/năm`) và phí giám sát (`0,2%/năm`) đã được kế toán quỹ **trích lập và trừ dần mỗi ngày vào Tổng tài sản thuần trước khi chia cho số lượng đơn vị quỹ để công bố con số `NAV/đơn vị = 22.400 VND`** (`SỰ_THẬT`).
  - Nghĩa là danh mục cổ phiếu gốc bên trong quỹ đã tăng khoảng `+14,0%`, sau khi trừ `2,0%` chi phí nội tại thì `NAV/đơn vị` mới tăng đúng **`+12,0%`** (lên `22.400 VND`). Nếu bạn lấy `+12,0%` trừ thêm `2,0%` một lần nữa thành `10,0%`, bạn đã trừ phí quản lý tới hai lần (`SUY_LUẬN`)!

---

## 7. Bài tập (10 câu)

1. Tại ngày định giá cuối tuần, một Quỹ mở có Tổng giá trị thị trường của cổ phiếu và tiền gửi là `1.860 tỷ VND`, cổ tức và lãi tiền gửi dự thu hợp lệ là `15 tỷ VND`, tổng các khoản nợ phải trả (phí quản lý phải trả, tiền mua chứng khoán chờ thanh toán) là `25 tỷ VND`, và tổng số lượng chứng chỉ quỹ đang lưu hành là `74.000.000` đơn vị. Tính Tổng `NAV` của quỹ và `NAV/đơn vị`.
2. Trên sàn `HOSE`, tại lúc 10h30 sáng, một chứng chỉ quỹ `ETF` có giá trị tài sản ròng tham chiếu trong phiên (`iNAV`) là `24.500 VND/CCQ`, trong khi giá đang khớp lệnh trên bảng điện là `24.892 VND/CCQ`. Chứng chỉ `ETF` này đang giao dịch ở trạng thái Phụ trội (`Premium`) hay Chiết khấu (`Discount`), với tỷ lệ bao nhiêu phần trăm?
3. Tiếp nối Câu 2: Giải thích một Thành viên lập quỹ (`AP`) sẽ thực hiện nghiệp vụ hoán đổi như thế nào giữa rổ cổ phiếu cơ sở và chứng chỉ `ETF` để kiếm lời chênh lệch giá (`Arbitrage`) và kéo giá `ETF` về sát `iNAV` (giả sử tổng chi phí hoán đổi và giao dịch thấp hơn mức chênh lệch)?
4. Một nhà đầu tư nộp `50.000.000 VND` (`50 triệu VND`) để mua chứng chỉ một Quỹ mở tại kỳ định giá có `NAV/đơn vị = 25.000 VND`. Biểu phí của quỹ quy định mức phí phát hành (phí mua) là `1,0%` tính trên tổng số tiền đăng ký mua. Tính số tiền phí phát hành bị trừ, số tiền thực tế được dùng để phân bổ chứng chỉ quỹ, và số lượng đơn vị chứng chỉ quỹ mà nhà đầu tư nhận được.
5. Giả sử nhà đầu tư ở Câu 4 nắm giữ số chứng chỉ quỹ đó trong 2 năm. Khi bán lại toàn bộ cho quỹ, `NAV/đơn vị` đã tăng lên `30.000 VND` và mức phí mua lại (phí bán) áp dụng cho thời gian nắm giữ 2 năm là `0,5%` trên giá trị bán lại (bỏ qua thuế). Tính giá trị bán lại trước phí, số tiền phí mua lại và số tiền mặt ròng nhà đầu tư thu về.
6. Hai quỹ đầu tư cùng nắm giữ một rổ cổ phiếu tạo ra tỷ suất sinh lời gộp trước chi phí là $r_{\text{gộp}} = 12,0\%/\text{năm}$ trong suốt $n = 20\text{ năm}$ (giả sử phí mua và phí bán đầu/cuối kỳ đều bằng `0%`). Quỹ Chỉ số Thụ động X có tổng chi phí hoạt động $\text{TER}_X = 0,6\%/\text{năm}$ ($r_{\text{NAV}, X} = 11,4\%/\text{năm}$), trong khi Quỹ Chủ động Y có $\text{TER}_Y = 2,1\%/\text{năm}$ ($r_{\text{NAV}, Y} = 9,9\%/\text{năm}$). Nếu đầu tư `500 triệu VND` ban đầu vào mỗi quỹ, sau 20 năm giá trị tài sản của Quỹ X và Quỹ Y lần lượt là bao nhiêu, và chênh lệch phí `1,5%/năm` đã lấy mất của nhà đầu tư ở Quỹ Y bao nhiêu triệu VND?
7. Trong năm 2025, `NAV/đơn vị` của Quỹ Chỉ số M tăng `+14,20%`, trong khi chỉ số tham chiếu tăng `+15,05%`. Tính `Tracking Difference (TD)` của Quỹ M trong năm 2025. Vì sao bạn không được gọi con số `-0,85%` này là `Tracking Error`?
8. Cho chuỗi chênh lệch lợi suất theo quý ($d_t = R_{p, t} - R_{b, t}$) của một quỹ `ETF` trong 4 quý liên tiếp là: $d_1 = -0,15\%$, $d_2 = -0,25\%$, $d_3 = +0,05\%$, $d_4 = -0,25\%$. Hãy tính: (a) Chênh lệch trung bình theo quý ($\bar{d}$); (b) Độ lệch chuẩn mẫu theo quý ($s_d$); và (c) `Tracking Error` quy đổi theo năm ($\text{TE}_{\text{năm}} = \sqrt{4} \times s_d$).
9. Khi đọc **Bản cáo bạch và Điều lệ của một Quỹ mở Trái phiếu** tại Việt Nam, bạn cần kiểm tra những giới hạn đầu tư nào để biết quỹ đó thực sự an toàn hay đang dồn tiền vào trái phiếu doanh nghiệp bất động sản chưa niêm yết?
10. Mở mô-đun [`../practice/models/market_returns.py`](../practice/models/market_returns.py) và [`../practice/models/risk_performance.py`](../practice/models/risk_performance.py), nêu cách kết hợp hàm tính lợi suất sau phí với hàm tính độ lệch chuẩn để giám sát định kỳ một danh mục quỹ `ETF`.

---

## 8. Đáp án chi tiết

1. **Tính Tổng `NAV` và `NAV/đơn vị`:**
   - $\text{Total NAV} = 1.860 + 15 - 25 = 1.850\text{ tỷ VND}$ (`1.850.000.000.000 VND`).
   - $\text{NAV/đơn vị} = \frac{1.850.000.000.000\text{ VND}}{74.000.000\text{ đơn vị}} = 25.000\text{ VND/đơn vị}$ (`PHÉP_TÍNH`).
2. **Tính `Premium / Discount` của `ETF` trên sàn:**
   - Vì $P_{\text{ETF}} = 24.892 > \text{iNAV} = 24.500$, chứng chỉ `ETF` đang giao dịch ở trạng thái **Phụ trội (`Premium`)**:
     $$\text{Premium} = \frac{24.892 - 24.500}{24.500} = \frac{392}{24.500} = +1,60\%\quad (\text{PHÉP\_TÍNH})$$
3. **Cơ chế `Arbitrage` của Thành viên lập quỹ (`AP`) khi `ETF` có `Premium +1,60%`:**
   - `AP` mua rổ cổ phiếu cơ sở trên thị trường với giá trị `24.500 VND/đơn vị tương đương`, đem nộp cho Quỹ `ETF` trên thị trường sơ cấp để tạo lập (`Creation`) các lô chứng chỉ `ETF` mới, đồng thời bán các chứng chỉ `ETF` đó trên sàn `HOSE` ở giá `24.892 VND`, thu lợi nhuận chênh lệch và tăng nguồn cung giúp kéo giá `ETF` trên sàn giảm về sát `iNAV` (`SUY_LUẬN`).
4. **Tính phí phát hành và số đơn vị Quỹ mở mua được:**
   - Phí phát hành (`1,0%`) = $50.000.000 \times 1,0\% = 500.000\text{ VND}$.
   - Số tiền thực phân bổ mua quỹ = $50.000.000 - 500.000 = 49.500.000\text{ VND}$.
   - Số đơn vị chứng chỉ quỹ nhận được = $49.500.000 / 25.000 = 1.980\text{ đơn vị}$ (`PHÉP_TÍNH`).
5. **Tính giá trị bán lại và tiền ròng sau 2 năm (`1.980 đơn vị`, `NAV = 30.000 VND`, phí bán `0,5%`):**
   - Giá trị bán lại trước phí = $1.980 \times 30.000 = 59.400.000\text{ VND}$.
   - Phí mua lại (`0,5%`) = $59.400.000 \times 0,5\% = 297.000\text{ VND}$.
   - Tiền mặt ròng thu về = $59.400.000 - 297.000 = 59.103.000\text{ VND}$ (`PHÉP_TÍNH`).
6. **Sức tàn phá lãi kép của chênh lệch phí `1,5%/năm` sau 20 năm (`V_0 = 500 triệu VND`):**
   - Quỹ Chỉ số Thụ động X ($r_{\text{NAV}, X} = 11,4\%/\text{năm}$):
     $$V_{20, X} = 500 \times (1,114)^{20} = 500 \times 8,6607 = 4.330,35\text{ triệu VND}\; (4,330\text{ tỷ VND})$$
   - Quỹ Chủ động Y ($r_{\text{NAV}, Y} = 9,9\%/\text{năm}$):
     $$V_{20, Y} = 500 \times (1,099)^{20} = 500 \times 6,6006 = 3.300,30\text{ triệu VND}\; (3,300\text{ tỷ VND})$$
   - Chênh lệch phí `1,5%/năm` đã lấy mất của nhà đầu tư ở Quỹ Y tới **$4.330,35 - 3.300,30 = 1.030,05\text{ triệu VND}$** (hơn **`1,03 tỷ VND`**, gấp đôi số vốn gốc ban đầu!) (`PHÉP_TÍNH`).
7. **Tính `Tracking Difference` năm 2025:**
   - $\text{TD}_{2025} = 14,20\% - 15,05\% = -0,85\%$ (`-85 bps`). Không gọi đây là `Tracking Error` vì `TD` chỉ là hiệu số lợi suất của 1 kỳ, trong khi `TE` là độ lệch chuẩn của chuỗi chênh lệch lợi suất qua nhiều kỳ (`PHÉP_TÍNH` & `SỰ_THẬT`).
8. **Tính `Tracking Error` quy đổi theo năm từ 4 quý ($d = [-0,15\%, -0,25\%, +0,05\%, -0,25\%]$):**
   - (a) Trung bình $\bar{d} = \frac{-0,15\% - 0,25\% + 0,05\% - 0,25\%}{4} = -0,15\%/\text{quý}$.
   - (b) Phương sai mẫu $s_d^2 = \frac{(0)^2 + (-0,10\%)^2 + (+0,20\%)^2 + (-0,10\%)^2}{4 - 1} = \frac{0,06\%^2}{3} = 0,02\%^2 \implies s_d = \sqrt{0,02}\% = 0,1414\%/\text{quý}$.
   - (c) $\text{TE}_{\text{năm}} = \sqrt{4} \times 0,1414\% = 2 \times 0,1414\% = 0,2828\%/\text{năm}$ (`~28,3 bps/năm`) (`PHÉP_TÍNH`).
9. **Kiểm tra Bản cáo bạch Quỹ mở Trái phiếu:**
   - Phải kiểm tra: (1) Tỷ trọng tối thiểu phân bổ vào Tiền gửi ngân hàng và Trái phiếu Chính phủ so với Trái phiếu doanh nghiệp; (2) Quỹ có được phép mua trái phiếu phát hành riêng lẻ hoặc trái phiếu chưa niêm yết không; (3) Giới hạn tỷ trọng tối đa đầu tư vào một tổ chức phát hành đơn lẻ; và (4) Báo cáo danh mục tài sản lớn nhất (`Top Holdings`) hằng tháng của quỹ (`SUY_LUẬN`).
10. **Ứng dụng mô-đun Python:**
    - Dùng các hàm trong [`../practice/models/market_returns.py`](../practice/models/market_returns.py) để tính lợi suất `CAGR` sau phí và dùng [`../practice/models/risk_performance.py`](../practice/models/risk_performance.py) để tính độ lệch chuẩn chuỗi chênh lệch lợi suất (`Tracking Error`) tự động.

---

## 9. Kiểm tra chuyển bài (Transfer Check)

Trước khi chuyển sang Bài [A3 — Vàng, ngoại tệ, bất động sản và tài sản mã hóa](A3-gold-currency-property-crypto.md), hãy tự kiểm tra 3 kỹ năng sau:
1. **Đối chiếu Quỹ đầu tư thuần túy (`A2`) với Bảo hiểm liên kết đơn vị (`Unit-Linked` ở Bài `P4` / `F8`):** Khi bạn mua một Quỹ mở hay `ETF` ở Bài `A2`, phí phát hành chỉ từ `0%–1,5%`; còn khi bạn mua một hợp đồng Bảo hiểm liên kết đơn vị (`Unit-Linked`), phí ban đầu năm thứ nhất bị khấu trừ bao nhiêu phần trăm? Bạn đã hiểu vì sao quy tắc vàng là *"Tách riêng bảo hiểm rủi ro tử kỳ và đầu tư trực tiếp qua Quỹ mở/ETF chi phí thấp"* chưa?
2. **Phản xạ trước khi đặt lệnh mua `ETF` trên sàn:** Bạn đã nhớ kiểm tra `iNAV` và độ rộng chênh lệch giá đặt mua – đặt bán (`Bid-Ask Spread`) để tránh đặt lệnh thị trường (`MP/ATO/ATC`) mua hớ ở mức `Premium` cao chưa?
3. **Kỷ luật đọc bảng phí:** Bạn đã phân biệt được khoản phí nào đã trừ trong `NAV` (`TER`) và khoản phí nào sẽ bị trừ thêm khi bạn nạp/rút tiền chưa?

---

## 10. Lỗi thường gặp và ranh giới an toàn

- **Bốn lỗi phân tích phổ biến:** (1) Nhầm giá khớp lệnh của `ETF` trên sàn luôn bằng đúng `NAV/đơn vị`; (2) Nhầm `Tracking Difference` của một kỳ với `Tracking Error`; (3) Trừ lặp một lần nữa phí quản lý thường niên vào mức tăng trưởng `NAV/đơn vị` đã công bố; (4) Xem nhẹ chênh lệch phí quản lý `1,5%/năm` trong đầu tư tích sản dài hạn 15–20 năm.
- **Ranh giới an toàn:** Bài học giải thích cơ chế tài chính và toán học chi phí của quỹ mở và `ETF`; không đề xuất hay khuyến nghị mua/bán bất kỳ chứng chỉ quỹ cụ thể nào.

## Nguồn Internet đã mở

- Chốt kiểm tra trực tuyến lúc `2026-11-05 12:15 UTC+7`:
  1. [SEC Investor.gov — Characteristics of Mutual Funds and Exchange-Traded Funds](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/characteristics-mutual-funds-exchange-traded-funds) và [Net Asset Value (NAV)](https://www.investor.gov/introduction-investing/investing-basics/glossary/net-asset-value).
  2. [SEC Investor Bulletin — Mutual Fund and ETF Fees and Expenses (`23/07/2025`)](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/mutual-fund-and-etf-fees-and-expenses-investor-bulletin) và [Exchange-Traded Funds (`23/02/2023`)](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-24).
  3. [NSE India — Tracking Error Methodology](https://www.nseindia.com/static/products-services/indices-tracking-error) và [SEBI Circular on Development of Passive Funds (`23/05/2022`)](https://www.sebi.gov.in/sebi_data/attachdocs/may-2022/1653307308174.pdf).
