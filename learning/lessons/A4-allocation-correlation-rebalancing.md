# Bài A4 — Phân bổ Tài sản, Ma trận Tương quan, Phương sai Danh mục và Kỷ luật Tái cân bằng (Rebalancing & DCA)

- Ngày cập nhật: `2026-11-05`
- Chốt dữ liệu lúc: `2026-11-05 12:15 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Hiểu và tính toán trực tiếp lợi suất kỳ vọng, phương sai và độ lệch chuẩn của danh mục gồm hai hay nhiều tài sản theo hệ số tương quan tuyến tính Pearson ($\rho_{AB}$); đo lường hiện tượng trôi tỷ trọng (`Weight Drift`) và thực hiện tái cân bằng (`Rebalancing`) bằng hai phương pháp (bán tài sản tăng / mua tài sản giảm hoặc dùng dòng tiền góp mới); tính đúng giá vốn bình quân điều hòa (`Harmonic Mean`) của chiến lược góp vốn định kỳ (`DCA`) và nhận diện rủi ro "tương quan hội tụ về +1 trong khủng hoảng thanh khoản".
- Thời lượng dự kiến: `3 buổi học (~270 phút)`
  - **Buổi 1 (90 phút):** Toán học Đa dạng hóa (`Diversification`) — Công thức lợi suất và độ lệch chuẩn danh mục 2 tài sản ($\sigma_p$), vai trò của hệ số tương quan $\rho \in [-1, +1]$ và nghịch lý "10 mã cổ phiếu cùng ngành bất động sản không phải là đa dạng hóa".
  - **Buổi 2 (90 phút):** Trôi tỷ trọng (`Weight Drift`) và Kỷ luật Tái cân bằng (`Calendar vs. Corridor Rebalancing`) — Phân biệt tái cân bằng nội bộ không dòng tiền mới với tái cân bằng bằng dòng tiền góp thêm, tính toán chi phí giao dịch và thuế khi tái cân bằng.
  - **Buổi 3 (90 phút):** Toán học về Góp vốn đều đặn (`Dollar-Cost Averaging — DCA` vs. `Lump-Sum`), thực hành kiểm thử với [`../practice/models/risk_performance.py`](../practice/models/risk_performance.py), xử lý dữ liệu bẩn và làm 10 bài tập định lượng.
- Bài trước liên quan: [N4 — Giá trị thời gian của tiền và lợi suất](N4-time-value-returns.md), [N5 — Danh mục và đầu tư chỉ số](N5-portfolio-index-investing.md), [N7 — Dữ liệu, xác suất và độ không chắc chắn](N7-data-probability-uncertainty.md), [P3 — Mục tiêu, khẩu vị rủi ro và IPS](P3-goals-risk-ips.md), [A1–A3](A1-deposits-government-corporate-bonds.md).
- Mô hình thực hành đi kèm: [`../practice/models/risk_performance.py`](../practice/models/risk_performance.py) và [`../practice/models/market_returns.py`](../practice/models/market_returns.py).
- Câu hỏi cốt lõi: Vì sao việc kết hợp hai tài sản có độ biến động cao nhưng không tương quan hoàn hảo ($\rho < 1$) lại giảm được độ rung lắc của toàn bộ danh mục mà không làm giảm lợi suất kỳ vọng bình quân, và khi nào công thức đó bị gãy trong thực tế?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/A4-fact-check.md), [phản biện](../reviews/A4-risk-review.md).

---

## Hiểu bài trong một phút

Phân bổ tài sản (`Asset Allocation`) — tức quyết định chia bao nhiêu phần trăm vốn vào Cổ phiếu, bao nhiêu vào Trái phiếu/Tiền gửi và bao nhiêu vào Vàng/Tiền mặt theo Tuyên bố Chính sách Đầu tư (`IPS` ở Bài [P3](P3-goals-risk-ips.md)) — là quyết định chi phối phần lớn độ biến động của tài sản gia đình qua các chu kỳ kinh tế:
1. **Đa dạng hóa thực sự phụ thuộc vào Hệ số tương quan ($\rho$), không phụ thuộc vào số lượng cái tên trong danh mục:** Lợi suất kỳ vọng của danh mục luôn bằng trung bình cộng có trọng số của các tài sản thành phần ($R_p = w_A R_A + w_B R_B$), nhưng độ lệch chuẩn (rủi ro biến động) của danh mục **nhỏ hơn trung bình cộng độ lệch chuẩn** của từng tài sản bất cứ khi nào hệ số tương quan $\rho_{AB} < +1,0$ (`SỰ_THẬT`).
2. **Tái cân bằng (`Rebalancing`) là cơ chế tự động "chốt lời một phần tài sản đã tăng nóng để mua thêm tài sản đang rẻ đi" nhằm giữ nguyên mức rủi ro mục tiêu:** Nếu bạn đặt mục tiêu `60% Cổ phiếu / 40% Trái phiếu & Tiền gửi`, sau một năm thị trường chứng khoán tăng mạnh làm tỷ trọng trôi lên `75% Cổ phiếu / 25% Trái phiếu`, nếu không tái cân bằng, danh mục của bạn đã tự động biến thành danh mục rủi ro cao ngay ở vùng đỉnh thị trường (`SUY_LUẬN`).
3. **Góp vốn định kỳ (`DCA`) cho giá vốn bình quân điều hòa (`Harmonic Mean`) thấp hơn trung bình cộng giá, nhưng không loại bỏ rủi ro thua lỗ:** Khi bạn góp cùng một số tiền cố định $C$ mỗi tháng, lúc giá thấp bạn tự động mua được nhiều đơn vị hơn, lúc giá cao mua ít đơn vị hơn; tuy nhiên nếu tài sản cơ sở suy giảm giá trị nội tại dài hạn, `DCA` vào một tài sản tồi vẫn dẫn đến thua lỗ (`SỰ_THẬT` & `SUY_LUẬN`).

---

## Ôn bài cũ

- Sau khi nắm đặc tính từng lớp tài sản qua [Bài A1](A1-deposits-government-corporate-bonds.md), [Bài A2](A2-mutual-funds-etfs-fees.md) và [Bài A3 — Vàng, ngoại tệ, bất động sản và tài sản mã hóa](A3-gold-currency-property-crypto.md), Bài A4 ghép chúng thành một danh mục đa tài sản bằng ma trận tương quan và kỷ luật tái cân bằng.

---

## Buổi 1 — Toán học Đa dạng hóa: Hệ số Tương quan Pearson và Phương sai Danh mục

### 1.1. Định nghĩa Hệ số tương quan tuyến tính Pearson ($\rho_{AB}$)

Theo tài liệu thống kê toán học của [Viện Tiêu chuẩn và Công nghệ Quốc gia Hoa Kỳ (`NIST — Correlation Coefficient`)](https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/correlat.htm), hệ số tương quan mẫu Pearson ($\rho_{AB}$) giữa hai chuỗi lợi suất $R_{A, t}$ và $R_{B, t}$ đo lường mức độ quan hệ tuyến tính giữa hai tài sản và luôn nằm trong đoạn $[-1, +1]$:

$$\rho_{AB} = \frac{\text{Cov}(R_A, R_B)}{\sigma_A \sigma_B} = \frac{\sum_{t=1}^{n} (R_{A, t} - \bar{R}_A)(R_{B, t} - \bar{R}_B)}{\sqrt{\sum_{t=1}^{n} (R_{A, t} - \bar{R}_A)^2} \sqrt{\sum_{t=1}^{n} (R_{B, t} - \bar{R}_B)^2}}$$

- $\rho_{AB} = +1,0$: Hai tài sản biến động tuyến tính cùng chiều hoàn hảo — ghép chúng lại **không tạo ra bất kỳ lợi ích giảm rủi ro nào**.
- $0 < \rho_{AB} < +1,0$: Hai tài sản có xu hướng cùng chiều nhưng không trùng khớp hoàn toàn — đã bắt đầu có lợi ích giảm phương sai danh mục.
- $\rho_{AB} = 0$: Hai tài sản không có tương quan tuyến tính trong mẫu quan sát.
- $\rho_{AB} < 0$: Khi tài sản A giảm thì tài sản B có xu hướng tăng (như Cổ phiếu và Trái phiếu Chính phủ chất lượng cao trong các cuộc suy thoái cầu tiêu dùng thông thường) — tạo ra **lợi ích giảm rủi ro mạnh nhất** (`SUY_LUẬN`).

### 1.2. Công thức Lợi suất và Độ lệch chuẩn của Danh mục 2 Tài sản

Giả sử bạn phân bổ tỷ trọng $w_A$ vào Tài sản A (có lợi suất kỳ vọng $E[R_A]$, độ lệch chuẩn $\sigma_A$) và tỷ trọng $w_B = 1 - w_A$ vào Tài sản B (có lợi suất kỳ vọng $E[R_B]$, độ lệch chuẩn $\sigma_B$). Khi đó:

$$E[R_p] = w_A E[R_A] + w_B E[R_B]$$

$$\sigma_p = \sqrt{w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \sigma_A \sigma_B \rho_{AB}}$$

**Ví dụ định lượng trực quan (`PHÉP_TÍNH`):**
Giả sử Tài sản A (Quỹ `ETF` Cổ phiếu) có $\sigma_A = 20,0\%/\text{năm}$, Tài sản B (Quỹ Trái phiếu / Vàng) có $\sigma_B = 10,0\%/\text{năm}$, và bạn chia tỷ trọng $w_A = 50\%, w_B = 50\%$. Trung bình cộng độ lệch chuẩn của hai tài sản là $0,5 \times 20\% + 0,5 \times 10\% = 15,0\%/\text{năm}$. Hãy xem độ lệch chuẩn thực tế của danh mục ($\sigma_p$) thay đổi thế nào theo $\rho_{AB}$:
1. Nếu $\rho_{AB} = +1,0$:
   $$\sigma_p = \sqrt{0,5^2 (20\%)^2 + 0,5^2 (10\%)^2 + 2(0,5)(0,5)(20\%)(10\%)(+1,0)} = \sqrt{100 + 25 + 100}\% = \sqrt{225}\% = 15,00\%/\text{năm}$$
2. Nếu $\rho_{AB} = 0,0$:
   $$\sigma_p = \sqrt{100 + 25 + 0}\% = \sqrt{125}\% = 11,18\%/\text{năm}\quad (\text{giảm được }3,82\text{ điểm phần trăm độ biến động!})$$
3. Nếu $\rho_{AB} = -0,40$:
   $$\sigma_p = \sqrt{100 + 25 + 100(-0,40)}\% = \sqrt{85}\% = 9,22\%/\text{năm}\quad (\text{thấp hơn cả độ biến động }10\%\text{ của tài sản an toàn hơn!})$$

### 1.3. Cảnh báo: Hiện tượng "Tương quan hội tụ về +1 trong Khủng hoảng Thanh khoản" (`Correlation Breakdown`)

Một cạm bẫy lớn trong quản trị rủi ro là coi hệ số tương quan quá khứ ($\rho_{AB}$) là một hằng số bất biến. Trong thực tế:
- Ở điều kiện thị trường bình thường, Cổ phiếu, Bất động sản, Vàng và Trái phiếu doanh nghiệp có thể có tương quan thấp (`0,1` đến `0,3`).
- Nhưng khi xảy ra **cú sốc lãi suất tăng vọt kèm khủng hoảng thanh khoản (`Margin Call` diện rộng)** — như năm 2008 trên toàn cầu hoặc cuối năm 2022 tại Việt Nam — các nhà đầu tư bị giải chấp buộc phải bán **tất cả mọi tài sản có thanh khoản** để lấy tiền mặt trả nợ, làm hệ số tương quan giữa Cổ phiếu, Bất động sản và Trái phiếu doanh nghiệp đồng loạt nhảy vọt về **`+0,8` đến `+0,95`** (`SUY_LUẬN`). Chỉ có Tiền gửi ngân hàng ngắn hạn / Trái phiếu Chính phủ kỳ hạn ngắn (Tín phiếu kho bạc) mới giữ vững vai trò neo thanh khoản trong những tuần lễ hoảng loạn đó.

---

## Buổi 2 — Hiện tượng Trôi tỷ trọng (Weight Drift) và Hai phương pháp Tái cân bằng

### 2.1. Công thức tính Tỷ trọng trôi (`Drifted Weights`) và Số tiền cần Tái cân bằng

Theo hướng dẫn của [SEC Hoa Kỳ — Beginner's Guide to Asset Allocation, Diversification, and Rebalancing](https://www.investor.gov/additional-resources/general-resources/publications-research/info-sheets/beginners-guide-asset), giả sử đầu kỳ danh mục có tổng giá trị $V_0$, phân bổ theo tỷ trọng mục tiêu $(w_A^*, w_B^*)$ tương ứng số tiền $(V_{A, 0}, V_{B, 0})$. Sau 1 năm, Tài sản A tăng trưởng với lợi suất $r_A$ đạt $V_{A, 1} = V_{A, 0}(1 + r_A)$ và Tài sản B đạt $V_{B, 1} = V_{B, 0}(1 + r_B)$, tổng danh mục cuối kỳ là $V_1 = V_{A, 1} + V_{B, 1}$.

Tỷ trọng thực tế cuối kỳ đã bị trôi (`Drifted Weights`) thành:

$$w_{A, 1} = \frac{V_{A, 1}}{V_1}, \qquad w_{B, 1} = \frac{V_{B, 1}}{V_1}$$

Để đưa danh mục quay về đúng tỷ trọng mục tiêu $(w_A^*, w_B^*)$, bạn có **2 cách hoàn toàn khác nhau về dòng tiền và thuế/phí**:

1. **Cách 1 — Tái cân bằng nội bộ không thêm tiền mới (`Internal Buy/Sell Rebalancing`):**
   - Giá trị đích của mỗi tài sản tính trên tổng vốn hiện có $V_1$ là: $V_{A, \text{đích}} = w_A^* \times V_1$ và $V_{B, \text{đích}} = w_B^* \times V_1$.
   - Giao dịch cần thực hiện: Bán bớt một lượng $\Delta_{\text{chuyển}} = V_{A, 1} - w_A^* V_1$ ở tài sản đang vượt tỷ trọng và dùng đúng số tiền đó mua thêm tài sản đang thiếu tỷ trọng (trong thực tế phải trừ đi phí giao dịch và thuế bán chứng khoán).
2. **Cách 2 — Tái cân bằng bằng dòng tiền góp mới (`Cash-Flow Rebalancing`):**
   - Nếu bạn đang trong giai đoạn tích sản có tiền lương tiết kiệm mới hằng quý/năm và **không muốn bán tài sản A** (để không phải chịu thuế bán `0,1%` và phí môi giới), bạn giữ nguyên $V_{A, 1}$ và tính số tiền mặt mới $\Delta C_{\text{góp vào B}}$ cần nạp thêm vào Tài sản B sao cho sau khi nạp, tỷ trọng của A giảm về đúng $w_A^*$:
     $$\frac{V_{A, 1}}{V_1 + \Delta C_{\text{góp vào B}}} = w_A^* \implies \Delta C_{\text{góp vào B}} = \frac{V_{A, 1}}{w_A^*} - V_1$$

### 2.2. Lịch tái cân bằng định kỳ (`Calendar`) vs. Tái cân bằng theo Dải biên độ (`Corridor / Tolerance Band`)

- Nếu tái cân bằng quá dày (ví dụ mỗi tuần hoặc mỗi tháng), bạn sẽ tốn rất nhiều phí giao dịch và thuế, đồng thời cắt cụt đà tăng (`Momentum`) của tài sản đang dẫn dắt.
- Trong thực tiễn quản lý danh mục cá nhân chuẩn mực, nhà đầu tư thường kết hợp **kiểm tra định kỳ mỗi 6 hoặc 12 tháng** với **ngưỡng lệch biên độ tuyệt đối $\pm 5\%$** (ví dụ mục tiêu Cổ phiếu là `60%`, chỉ thực hiện lệnh tái cân bằng khi tỷ trọng Cổ phiếu vượt quá `65%` hoặc tụt xuống dưới `55%`) (`SUY_LUẬN`).

---

## Buổi 3 — Toán học Góp vốn Định kỳ (DCA): Trung bình Điều hòa (Harmonic Mean)

### 3.1. Vì sao Giá vốn bình quân của DCA luôn thấp hơn Giá trung bình cộng?

Theo định nghĩa của [SEC Hoa Kỳ — Dollar-Cost Averaging (`DCA`)](https://www.investor.gov/introduction-investing/investing-basics/glossary/dollar-cost-averaging), khi bạn đầu tư một **số tiền bằng nhau $C$** vào mỗi kỳ $t = 1, 2, \dots, K$ tại các mức giá đơn vị $P_1, P_2, \dots, P_K$:
- Số lượng đơn vị mua được ở kỳ $t$ là $q_t = \frac{C}{P_t}$.
- Tổng số tiền đã góp sau $K$ kỳ là $K \times C$, và tổng số lượng đơn vị tích lũy được là $\sum_{t=1}^{K} \frac{C}{P_t}$.
- Do đó, **Giá vốn bình quân mỗi đơn vị (`Average Cost per Unit` — $\bar{P}_{\text{DCA}}$)** chính là **Trung bình điều hòa (`Harmonic Mean`)** của chuỗi giá:

$$\bar{P}_{\text{DCA}} = \frac{\text{Tổng tiền đã góp}}{\text{Tổng số đơn vị mua được}} = \frac{K \times C}{\sum_{t=1}^{K} \frac{C}{P_t}} = \frac{K}{\sum_{t=1}^{K} \frac{1}{P_t}}$$

Theo bất đẳng thức Cauchy – Schwarz giữa Trung bình cộng (`Arithmetic Mean` — $\bar{P}_{\text{Số học}} = \frac{1}{K}\sum P_t$) và Trung bình điều hòa (`Harmonic Mean`), khi các mức giá $P_t$ có sự biến động khác nhau ($P_1 \neq P_2 \dots$), ta luôn có bất đẳng thức toán học tuyệt đối:

$$\bar{P}_{\text{DCA (Điều hòa)}} < \bar{P}_{\text{Số học}}$$

*Giới hạn của `DCA` cần nhớ (`SUY_LUẬN`):*
1. `DCA` rất phù hợp với người đi làm nhận lương hằng tháng (đầu tư ngay khi có dòng tiền thu nhập mới) hoặc giúp giảm nỗi sợ tâm lý khi giải ngân một khoản tiền lớn vào thị trường biến động.
2. Tuy nhiên, nếu bạn đã có sẵn một cục tiền mặt lớn từ đầu (`Lump-Sum`) và thị trường đang trong xu hướng tăng dài hạn, việc giữ tiền mặt đứng ngoài để chia nhỏ giải ngân dần trong 2–3 năm sẽ chịu chi phí cơ hội của phần tiền mặt chưa được đầu tư.
3. Trong thực tế tại sàn `HOSE`, cổ phiếu giao dịch theo lô chẵn `100 cổ phiếu/lô`, nên với số tiền nhỏ mỗi tháng (như `2–5 triệu VND`), nhà đầu tư thường thực hiện `DCA` qua **Quỹ mở** (cho phép mua lẻ đến `0,01` đơn vị quỹ) hoặc gom đủ lô `100` chứng chỉ quỹ `ETF` (`SUY_LUẬN`).

---

## 4. Ví dụ từ nguồn thật: Thực hành Chuẩn mực SEC / NIST với Mô-đun `risk_performance.py`

1. **Đối chiếu nguồn chuẩn mực (`SEC` & `NIST`):**
   - `SỰ_THẬT`: Tài liệu của [SEC Hoa Kỳ](https://www.investor.gov/additional-resources/general-resources/publications-research/info-sheets/beginners-guide-asset) và [NIST](https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/correlat.htm) xác lập khung toán học chuẩn cho hệ số tương quan mẫu Pearson, phân bổ tỷ trọng và tái cân bằng danh mục.
2. **Ví dụ tính toán tái lập bằng mô-đun [`../practice/models/risk_performance.py`](../practice/models/risk_performance.py):**
   - Giả sử một nhà đầu tư Việt Nam thiết lập danh mục khởi đầu `200 triệu VND` theo tỷ trọng mục tiêu **`60% Quỹ ETF Cổ phiếu (A = 120 triệu VND)`** và **`40% Quỹ Trái phiếu / Tiền gửi (B = 80 triệu VND)`** (`KỊCH_BẢN`).
   - Kết thúc Năm 1, Quỹ `ETF` Cổ phiếu tăng $+25,0\%$ lên $V_{A, 1} = 120 \times 1,25 = 150,0\text{ triệu VND}$, còn Quỹ Trái phiếu tăng $+5,0\%$ lên $V_{B, 1} = 80 \times 1,05 = 84,0\text{ triệu VND}$.
   - **Phép tính tái lập (`PHÉP_TÍNH`):**
     - Tổng giá trị danh mục cuối Năm 1: $V_1 = 150,0 + 84,0 = 234,0\text{ triệu VND}$ (tổng lợi suất danh mục $= 234 / 200 - 1 = +17,0\%$, đúng bằng $0,6 \times 25\% + 0,4 \times 5\%$).
     - Tỷ trọng thực tế cuối Năm 1 đã trôi thành:
       $$w_{A, 1} = \frac{150,0}{234,0} = 64,10\%, \qquad w_{B, 1} = \frac{84,0}{234,0} = 35,90\%$$
     - **Nếu tái cân bằng nội bộ không thêm tiền mới (Cách 1):**
       - Giá trị đích của A (`60%`) = $0,60 \times 234,0 = 140,4\text{ triệu VND}$; Giá trị đích của B (`40%`) = $0,40 \times 234,0 = 93,6\text{ triệu VND}$.
       - Cần **bán `9,6 triệu VND` Quỹ Cổ phiếu A** ($150,0 - 140,4$) và dùng `9,6 triệu VND` đó **mua thêm Quỹ Trái phiếu B** ($84,0 + 9,6 = 93,6$).
     - **Nếu tái cân bằng bằng tiền thưởng Tết góp mới mà không bán A (Cách 2):**
       - Giữ nguyên $V_{A, 1} = 150,0\text{ triệu VND}$ làm `60%` của tổng danh mục mới $\implies \text{Tổng danh mục mới} = 150,0 / 0,60 = 250,0\text{ triệu VND}$.
       - Số tiền mới cần góp thẳng vào Quỹ Trái phiếu B = $250,0 - 234,0 = 16,0\text{ triệu VND}$ (nâng B từ `84,0` lên `100,0 triệu VND`, ứng với đúng $100 / 250 = 40,0\%$!).

---

## 5. Bài làm với dữ liệu thiếu hoặc lệch (Dirty-Data Exercise)

### Tình huống dữ liệu bẩn
Một nhà đầu tư cá nhân khoe danh mục "đa dạng hóa tuyệt đối 5 tài sản" trị giá `1,0 tỷ VND` vào đầu năm:
- `200 triệu VND` Cổ phiếu Công ty Bất động sản Vinhomes (`VHM`);
- `200 triệu VND` Cổ phiếu Công ty Bất động sản Khang Điền (`KDH`);
- `200 triệu VND` Cổ phiếu Công ty Xây dựng dân dụng Z (nhà thầu chính của các dự án BĐS);
- `200 triệu VND` Trái phiếu doanh nghiệp của một tập đoàn bất động sản chưa niêm yết;
- `200 triệu VND` Tiền đặt cọc mua một lô đất nền vùng ven.

Nhà đầu tư này tự tin tuyên bố:
> *"Tôi đã chia đều tiền vào 5 khoản đầu tư khác nhau (3 mã cổ phiếu, 1 trái phiếu và 1 lô đất), mỗi khoản chỉ chiếm 20% vốn theo đúng nguyên tắc không bỏ hết trứng vào một giỏ!"*

Hãy chỉ ra vì sao đây là một **danh mục "đa dạng hóa giả tạo" (`Diworsification / Pseudo-Diversification`)** và định lượng rủi ro thực tế của danh mục này!

### Quy trình bóc tách rủi ro tập trung ẩn (`Hidden Factor Concentration`)
1. **Phơi nhiễm 100% vào một nhân tố vĩ mô duy nhất (`Single Macro Factor — Chu kỳ Tín dụng & Bất động sản`):**
   - Dù mang 5 cái tên và 3 hình thức pháp lý khác nhau (cổ phiếu, trái phiếu, đất nền), cả 5 khoản đầu tư này đều phụ thuộc sống còn vào cùng một biến số: **Lãi suất vay mua nhà và Thanh khoản thị trường bất động sản Việt Nam**!
   - Khi lãi suất tăng và tín dụng bất động sản thắt chặt: (a) Cổ phiếu `VHM`, `KDH` và nhà thầu xây dựng Z cùng sụt giảm (`tương quan thực tế trong pha suy thoái` $\rho \approx +0,85$); (b) Trái phiếu doanh nghiệp bất động sản chưa niêm yết đối mặt rủi ro chậm trả gốc/lãi và mất thanh khoản; và (c) Lô đất nền vùng ven đóng băng không thể bán ra tiền mặt để tái cân bằng (`SUY_LUẬN`).
2. **Tính lại độ lệch chuẩn danh mục khi tương quan thực tế $\rho = +0,85$:**
   - Giả sử mỗi khoản có độ lệch chuẩn $\sigma_i = 30\%/\text{năm}$. Nếu nhà đầu tư tưởng nhầm 5 khoản này độc lập với nhau ($\rho = 0$), họ ước tính nhầm độ lệch chuẩn danh mục chỉ là $\sigma_p = \frac{30\%}{\sqrt{5}} = 13,42\%/\text{năm}$.
   - Nhưng vì hệ số tương quan thực tế giữa 5 khoản cùng ngành là $\rho = +0,85$, phương sai thực tế của danh mục đều 5 tài sản ($\sigma_p = \sigma \sqrt{\frac{1}{5} + \frac{4}{5}\rho}$) là:
     $$\sigma_{p, \text{thực}} = 30\% \times \sqrt{0,20 + 0,80 \times 0,85} = 30\% \times \sqrt{0,88} = 28,14\%/\text{năm}\quad (\text{PHÉP\_TÍNH})$$
   - Độ biến động thực tế (`28,14%/năm`) cao hơn gấp đôi con số ảo tưởng (`13,42%/năm`), và danh mục hoàn toàn không có bất kỳ lớp tài sản thanh khoản ngược pha nào (như Tiền gửi ngân hàng hay Trái phiếu Chính phủ) để đỡ đòn khi thị trường bất động sản đóng băng!

---

## 6. Sai ở đâu? (Bắt lỗi suy luận)

Hãy chỉ ra chỗ sai trong quyết định "tái cân bằng ngược" sau đây:

> *"Tôi thiết lập danh mục 50% Cổ phiếu / 50% Tiền gửi tiết kiệm (mỗi bên 100 triệu đồng). Sau một đợt thị trường chứng khoán sụt giảm mạnh -40%, phần Cổ phiếu của tôi chỉ còn 60 triệu đồng trong khi Tiền gửi tăng lên 105 triệu đồng. Vì thấy Cổ phiếu đang lỗ nặng quá nguy hiểm, tôi quyết định bán nốt 27,5 triệu đồng Cổ phiếu chuyển sang Tiền gửi để đưa tỷ trọng Cổ phiếu xuống còn 20% cho an toàn!"*

### Phân tích chỗ sai
1. **Nhầm lẫn "Hoảng loạn bán đáy theo cảm xúc (`Panic Selling`)" với "Tái cân bằng (`Rebalancing`)":**
   - Khi Cổ phiếu giảm còn `60 triệu VND` và Tiền gửi là `105 triệu VND` (tổng danh mục = `165 triệu VND`), tỷ trọng Cổ phiếu đã tự tụt xuống $60 / 165 = 36,36\%$ (thấp hơn mức mục tiêu `50%` ứng với $0,50 \times 165 = 82,5\text{ triệu VND}$).
   - Theo đúng kỷ luật tái cân bằng về đích `50/50`, tại thời điểm thị trường chứng khoán đã chiết khấu `-40%` (định giá `P/E`, `P/B` toàn thị trường đã rẻ đi rất nhiều), nhà đầu tư phải làm **ngược lại**: rút **`22,5 triệu VND` từ Tiền gửi** ($105 - 82,5$) để **mua thêm Cổ phiếu ở vùng giá thấp** ($60 + 22,5 = 82,5\text{ triệu VND}$) (`PHÉP_TÍNH`)!
2. **Hậu quả của việc bán ở đáy:** Việc bán bớt cổ phiếu sau khi đã giảm `-40%` để hạ tỷ trọng xuống `20%` chính là hành vi **khóa chặt khoản lỗ ở đáy** và khiến danh mục không thể phục hồi về vốn gốc khi thị trường chứng khoán tăng trở lại (`SUY_LUẬN`). Nếu khẩu vị rủi ro thực sự của bạn không chịu nổi mức giảm của danh mục `50/50`, bạn phải thiết kế tỷ trọng thấp hơn ngay từ đầu trong bản `IPS` (Bài [P3](P3-goals-risk-ips.md)), chứ không phải đợi thị trường sập xong mới bán tháo.

---

## 7. Bài tập (10 câu)

1. Danh mục của bạn gồm Tài sản A trị giá `180 triệu VND`, Tài sản B trị giá `90 triệu VND` và Tài sản C trị giá `30 triệu VND`. Tính tổng giá trị danh mục và tỷ trọng phần trăm ($w_A, w_B, w_C$) của từng tài sản.
2. Cho hai tài sản: Tài sản A (Quỹ Cổ phiếu) có lợi suất kỳ vọng $E[R_A] = 14,0\%/\text{năm}$, độ lệch chuẩn $\sigma_A = 22,0\%/\text{năm}$; Tài sản B (Quỹ Trái phiếu) có lợi suất kỳ vọng $E[R_B] = 6,0\%/\text{năm}$, độ lệch chuẩn $\sigma_B = 6,0\%/\text{năm}$. Bạn phân bổ tỷ trọng $w_A = 60\%$ và $w_B = 40\%$. Hãy tính: (a) Lợi suất kỳ vọng của danh mục ($E[R_p]$); và (b) Độ lệch chuẩn của danh mục ($\sigma_p$) trong hai trường hợp hệ số tương quan $\rho_{AB} = +0,20$ và $\rho_{AB} = -0,30$.
3. Đầu năm, bạn có danh mục `400 triệu VND` chia theo tỷ trọng mục tiêu `50% Cổ phiếu (A = 200 triệu VND)` và `50% Trái phiếu/Tiền gửi (B = 200 triệu VND)`. Cuối năm, phần Cổ phiếu A giảm `-20%` xuống còn `160 triệu VND`, trong khi phần B tăng `+6%` lên `212 triệu VND`. Tính tổng giá trị danh mục cuối năm, tỷ trọng trôi ($w_{A, 1}, w_{B, 1}$), và cho biết nếu tái cân bằng nội bộ không thêm tiền mới (bỏ qua phí), bạn phải chuyển bao nhiêu tiền từ tài sản nào sang tài sản nào?
4. Ngược lại với Câu 3: Đầu năm A = `200 triệu VND`, B = `200 triệu VND` (mục tiêu `50/50`). Cuối năm, A tăng vọt `+40%` lên `280 triệu VND`, còn B giữ nguyên `200 triệu VND` (tổng = `480 triệu VND`). Hãy tính: (a) Nếu tái cân bằng nội bộ không thêm tiền mới, cần bán bao nhiêu triệu VND ở A để mua B? (b) Nếu bạn **không muốn bán A** mà dùng tiền tiết kiệm mới nạp thêm vào B để đưa tỷ trọng về lại `50/50`, bạn cần góp thêm bao nhiêu triệu VND vào B?
5. Một nhà đầu tư thực hiện góp vốn đều đặn (`DCA`) vào một Quỹ mở với số tiền cố định $C = 3.000.000\text{ VND/tháng}$ trong 3 tháng liên tiếp. Giá `NAV/đơn vị` của 3 tháng lần lượt là: Tháng 1 = `15.000 VND`, Tháng 2 = `12.000 VND`, Tháng 3 = `20.000 VND` (bỏ qua phí phát hành). Tính: (a) Số đơn vị quỹ mua được ở từng tháng và tổng số đơn vị sau 3 tháng; (b) Giá trung bình cộng số học của 3 mức giá; và (c) Giá vốn bình quân thực tế mỗi đơn vị ($\bar{P}_{\text{DCA}}$ — trung bình điều hòa).
6. Tiếp nối Câu 5: Tại cuối Tháng 3 (khi `NAV/đơn vị` đang ở mức `20.000 VND`), tổng giá trị thị trường của số đơn vị quỹ mà nhà đầu tư đang nắm giữ là bao nhiêu, và nhà đầu tư đang lãi bao nhiêu triệu VND / bao nhiêu phần trăm trên tổng số vốn `9.000.000 VND` đã góp?
7. Giả sử khi tái cân bằng nội bộ ở Câu 4a (bán một lượng chứng chỉ `ETF` Cổ phiếu A để mua Quỹ Trái phiếu B), nhà đầu tư phải chịu phí môi giới cộng thuế bán chứng khoán tổng cộng là `0,25%` ở chiều bán A và phí mua `0,15%` ở chiều mua B. Nếu số tiền chuyển là `40 triệu VND`, tổng chi phí ma sát trực tiếp của lần tái cân bằng này là bao nhiêu VND?
8. Giải thích vì sao hai tài sản có hệ số tương quan mẫu Pearson bằng `0` ($\rho_{AB} = 0$) trong 3 năm thị trường bình thường vẫn có thể cùng sụt giảm `-25%` trong một tháng xảy ra khủng hoảng thanh khoản toàn cầu.
9. Phân biệt hai phương pháp thiết lập quy tắc tái cân bằng trong Tuyên bố Chính sách Đầu tư (`IPS`): **Tái cân bằng theo lịch cố định (`Calendar Rebalancing`)** và **Tái cân bằng theo dải biên độ (`Corridor / Tolerance-Band Rebalancing`)**.
10. Mở mô-đun [`../practice/models/risk_performance.py`](../practice/models/risk_performance.py), nêu cách sử dụng hàm `sharpe_ratio` và `sortino_ratio` để so sánh hiệu quả điều chỉnh theo rủi ro của một danh mục có tái cân bằng (`60/40`) so với danh mục giữ nguyên `100%` cổ phiếu.

---

## 8. Đáp án chi tiết

1. **Tính tỷ trọng danh mục 3 tài sản (`180`, `90`, `30 triệu VND`):**
   - Tổng giá trị danh mục = $180 + 90 + 30 = 300\text{ triệu VND}$.
   - Tỷ trọng: $w_A = 180 / 300 = 60,0\%$; $w_B = 90 / 300 = 30,0\%$; $w_C = 30 / 300 = 10,0\%$ (`PHÉP_TÍNH`).
2. **Tính lợi suất kỳ vọng và độ lệch chuẩn danh mục `60/40`:**
   - (a) Lợi suất kỳ vọng: $E[R_p] = 0,60 \times 14,0\% + 0,40 \times 6,0\% = 8,40\% + 2,40\% = 10,80\%/\text{năm}$.
   - (b) Độ lệch chuẩn ($\sigma_A = 22\%, \sigma_B = 6\%$):
     - Hạng tử $w_A^2 \sigma_A^2 = 0,36 \times 484 = 174,24\%^2$; Hạng tử $w_B^2 \sigma_B^2 = 0,16 \times 36 = 5,76\%^2$; Hạng tử tích $2 w_A w_B \sigma_A \sigma_B = 2(0,6)(0,4)(22)(6) = 63,36\%^2$.
     - Khi $\rho_{AB} = +0,20$: $\sigma_p = \sqrt{174,24 + 5,76 + 63,36(0,20)}\% = \sqrt{192,672}\% = 13,88\%/\text{năm}$.
     - Khi $\rho_{AB} = -0,30$: $\sigma_p = \sqrt{174,24 + 5,76 + 63,36(-0,30)}\% = \sqrt{160,992}\% = 12,69\%/\text{năm}$ (`PHÉP_TÍNH`).
3. **Tái cân bằng khi Cổ phiếu A giảm (`160 triệu`) và Trái phiếu B tăng (`212 triệu`):**
   - Tổng giá trị danh mục cuối năm = $160 + 212 = 372\text{ triệu VND}$.
   - Tỷ trọng trôi: $w_{A, 1} = 160 / 372 = 43,01\%$; $w_{B, 1} = 212 / 372 = 56,99\%$.
   - Giá trị đích `50/50` mỗi bên = $372 / 2 = 186\text{ triệu VND}$. Cần **chuyển `26 triệu VND` từ Trái phiếu/Tiền gửi B sang mua thêm Cổ phiếu A** ($160 + 26 = 186\text{ triệu VND}$) (`PHÉP_TÍNH`).
4. **Phân biệt Tái cân bằng nội bộ và Tái cân bằng bằng tiền mới (`A = 280 triệu`, `B = 200 triệu`):**
   - (a) Tái cân bằng nội bộ (tổng giữ nguyên `480 triệu VND`, đích mỗi bên `240 triệu VND`): Bán **`40 triệu VND`** ở A chuyển sang mua B.
   - (b) Tái cân bằng bằng tiền mới (giữ nguyên A = `280 triệu VND` làm `50%` danh mục): Cần góp thêm **`80 triệu VND` tiền mới vào B** để B cũng đạt `280 triệu VND` (tổng danh mục sau góp mới = `560 triệu VND`) (`PHÉP_TÍNH`).
5. **Tính số đơn vị và Giá vốn bình quân điều hòa (`DCA` 3 tháng, `3 triệu VND/tháng`):**
   - (a) Số đơn vị mua mỗi tháng: Tháng 1 = $3.000.000 / 15.000 = 200\text{ đơn vị}$; Tháng 2 = $3.000.000 / 12.000 = 250\text{ đơn vị}$; Tháng 3 = $3.000.000 / 20.000 = 150\text{ đơn vị}$. Tổng cộng = $200 + 250 + 150 = 600\text{ đơn vị}$.
   - (b) Giá trung bình cộng số học = $(15.000 + 12.000 + 20.000) / 3 = 15.667\text{ VND/đơn vị}$.
   - (c) Giá vốn bình quân thực tế ($\bar{P}_{\text{DCA}}$) = $\frac{9.000.000\text{ VND}}{600\text{ đơn vị}} = 15.000\text{ VND/đơn vị}$ (thấp hơn giá trung bình cộng `15.667 VND`!) (`PHÉP_TÍNH`).
6. **Tính giá trị danh mục và lãi sau 3 tháng `DCA` (`600 đơn vị` tại giá `20.000 VND`):**
   - Tổng giá trị thị trường cuối Tháng 3 = $600 \times 20.000 = 12.000.000\text{ VND}$ (`12,0 triệu VND`).
   - Lãi tuyệt đối = $12.000.000 - 9.000.000 = +3.000.000\text{ VND}$ (`+3,0 triệu VND`), tương ứng tỷ suất $+3,0 / 9,0 = +33,33\%$ trên tổng vốn đã góp (`PHÉP_TÍNH`).
7. **Tính chi phí ma sát khi tái cân bằng `40 triệu VND`:**
   - Phí + thuế chiều bán A (`0,25%`) = $40.000.000 \times 0,25\% = 100.000\text{ VND}$.
   - Phí chiều mua B (`0,15%` trên `39,9 triệu VND` còn lại, hoặc xấp xỉ trên `40 triệu`) $\approx 40.000.000 \times 0,15\% = 60.000\text{ VND}$ (chính xác là $39.900.000 \times 0,15\% = 59.850\text{ VND}$). Tổng chi phí ma sát $\approx 160.000\text{ VND}$ (`PHÉP_TÍNH`).
8. **Vì sao $\rho = 0$ trong quá khứ không bảo đảm tránh lỗ trong khủng hoảng:**
   - Hệ số tương quan Pearson chỉ đo quan hệ tuyến tính trong mẫu lịch sử quá khứ; khi xảy ra cú sốc thanh khoản hoặc lãi suất vĩ mô, áp lực bán giải chấp chung (`Forced De-leveraging`) làm các tài sản rủi ro cùng sụt giảm đồng thời (`SUY_LUẬN`).
9. **Phân biệt `Calendar Rebalancing` và `Corridor Rebalancing`:**
   - `Calendar Rebalancing`: Tái cân bằng theo mốc thời gian cố định (ví dụ mỗi ngày 30/06 và 31/12 hằng năm) bất kể tỷ trọng lệch ít hay nhiều.
   - `Corridor Rebalancing`: Đặt dải biên độ cho phép (ví dụ `60% ± 5%`, tức từ `55%` đến `65%`); chỉ giao dịch tái cân bằng khi tỷ trọng chạm hoặc vượt ra ngoài biên độ đó, giúp giảm giao dịch không cần thiết khi thị trường chỉ dao động nhẹ (`SUY_LUẬN`).
10. **Ứng dụng `sharpe_ratio` và `sortino_ratio` trong [`../practice/models/risk_performance.py`](../practice/models/risk_performance.py):**
    - Truyền chuỗi lợi suất định kỳ của danh mục `60/40` và lãi suất phi rủi ro vào `sharpe_ratio` (chia cho tổng độ lệch chuẩn $\sigma_p$) và `sortino_ratio` (chỉ chia cho độ lệch chuẩn các kỳ âm `Downside Deviation`) để định lượng hiệu quả giảm rủi ro đuôi của việc phân bổ tài sản.

---

## 9. Kiểm tra chuyển bài (Transfer Check)

Bạn đã hoàn thành toàn bộ Cụm Tài sản & Danh mục (`A1` đến `A4`). Trước khi bước sang Cụm Vĩ mô & Chu kỳ vốn (`M1`, `M2`, `M3`, `014`), hãy tự kiểm tra 3 kỹ năng liên thông sau:
1. **Chuyển từ Danh mục (`A4`) sang Truyền dẫn Vĩ mô (`M1`):** Ở Buổi 1, bạn thấy rằng đôi khi Cổ phiếu và Trái phiếu biến động ngược chiều ($\rho < 0$, giúp danh mục `60/40` rất êm), nhưng đôi khi cả Cổ phiếu lẫn Trái phiếu lại cùng sụt giảm ($\rho > 0$). Biến số vĩ mô nào quyết định chế độ tương quan đó? (Gợi ý: Khi cú sốc đến từ **Lạm phát và Ngân hàng Trung ương tăng lãi suất**, cả giá Trái phiếu lẫn định giá Cổ phiếu đều bị chiết khấu nặng — bạn sẽ học cơ chế này ngay tại Bài [M1](M1-monetary-policy-rates-fx-credit.md)!)
2. **Kỷ luật phân biệt "Đa dạng hóa thật" và "Đa dạng hóa giả":** Khi nhìn vào danh mục hiện tại của mình, bạn đã kiểm tra xem các khoản đầu tư có đang phụ thuộc trùng lắp vào cùng một nhân tố vĩ mô (như chu kỳ đất đai/tín dụng) không?
3. **Thực hành Python:** Bạn đã chạy thử mô-đun [`../practice/models/risk_performance.py`](../practice/models/risk_performance.py) để tính độ lệch chuẩn, `Max Drawdown` và `Sharpe Ratio` cho danh mục mẫu chưa?

---

## 10. Lỗi thường gặp và ranh giới an toàn

- **Bốn lỗi phân tích phổ biến:** (1) Nhầm việc mua nhiều mã cổ phiếu cùng ngành hoặc nhiều sản phẩm cùng phụ thuộc vào chu kỳ bất động sản là đã đa dạng hóa danh mục; (2) Nhầm việc góp thêm tiền mới (`20 triệu`) để cân bằng tỷ trọng với việc bán bớt tài sản cũ chuyển sang (`10 triệu`); (3) Hoảng loạn bán tháo tài sản rủi ro sau khi nó đã sụt giảm mạnh (làm ngược hoàn toàn với nguyên lý tái cân bằng); (4) Tin rằng góp đều (`DCA`) hoặc tái cân bằng có thể biến một tài sản rác thành có lãi.
- **Ranh giới an toàn:** Mọi tỷ trọng (`50/50`, `60/40`) trong bài chỉ phục vụ mục đích minh họa toán học danh mục; việc phân bổ thực tế của từng cá nhân phải dựa trên quỹ khẩn cấp, thời hạn mục tiêu và khả năng chịu đựng sụt giảm trong `IPS` riêng.

## Nguồn Internet đã mở

- Chốt kiểm tra trực tuyến lúc `2026-11-05 12:15 UTC+7`:
  1. [SEC Investor.gov — Beginner's Guide to Asset Allocation, Diversification, and Rebalancing](https://www.investor.gov/additional-resources/general-resources/publications-research/info-sheets/beginners-guide-asset) và [Dollar-Cost Averaging (DCA)](https://www.investor.gov/introduction-investing/investing-basics/glossary/dollar-cost-averaging).
  2. [NIST Engineering Statistics Handbook — Correlation Coefficient](https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/correlat.htm).
