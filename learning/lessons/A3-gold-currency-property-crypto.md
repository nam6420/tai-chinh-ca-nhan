# Bài A3 — Vàng, Ngoại tệ, Bất động sản cho thuê và Tài sản mã hóa: Quyền sở hữu, Dòng tiền, Chi phí ma sát và Khung pháp lý

- Ngày cập nhật: `2026-11-05`
- Chốt dữ liệu lúc: `2026-11-05 12:15 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Phân biệt bản chất kinh tế của tài sản tạo dòng tiền nội tại (`Cash-Flow Generating Assets` như bất động sản cho thuê, cổ phiếu, trái phiếu) với tài sản không tạo dòng tiền định kỳ (`Non-Yielding Assets` như vàng vật chất, ngoại tệ tiền mặt, tài sản mã hóa); tính chính xác điểm hòa vốn sau chênh lệch giá mua – bán (`Bid-Ask Spread`), tỷ suất vốn hóa bất động sản ròng (`Net Cap Rate`) và lợi suất vốn chủ sở hữu có đòn bẩy (`Cash-on-Cash Return`); nắm vững quy định quản lý kinh doanh vàng tại Việt Nam (`Nghị định 232/2025/NĐ-CP`, `Nghị định 390/2026/NĐ-CP`) và nghị quyết thí điểm tài sản mã hóa (`Nghị quyết 05/2025/NQ-CP`).
- Thời lượng dự kiến: `3 buổi học (~270 phút)`
  - **Buổi 1 (90 phút):** Vàng vật chất và Ngoại tệ — Bản chất không trả cổ tức/trái tức, toán học về chênh lệch giá mua – bán (`Bid-Ask Spread`), chênh lệch giá vàng nội địa so với thế giới quy đổi (`Domestic Gold Premium`) và quy định thanh toán không dùng tiền mặt từ `5 triệu VND/ngày` theo Nghị định `390/2026/NĐ-CP`.
  - **Buổi 2 (90 phút):** Kinh tế học Bất động sản cá nhân và cho thuê — Phân biệt Lợi suất cho thuê gộp (`Gross Rental Yield`) với Tỷ suất vốn hóa ròng (`Net Cap Rate`), chi phí bảo trì – trống phòng – thuế và sự nguy hiểm khi dùng đòn bẩy vay mua bất động sản lúc lãi suất thả nổi vượt `Net Cap Rate`.
  - **Buổi 3 (90 phút):** Tài sản mã hóa (`Crypto Assets`) — Rủi ro lưu ký (`Not your keys` vs. nền tảng mất thanh khoản), khung pháp lý thí điểm Nghị quyết `05/2025/NQ-CP`, cảnh báo của `SEC`, xử lý dữ liệu bẩn và giải 10 bài tập định lượng.
- Bài trước liên quan: [N4 — Giá trị thời gian của tiền và lợi suất](N4-time-value-returns.md), [P3 — Mục tiêu, khẩu vị rủi ro và IPS](P3-goals-risk-ips.md), [B3 — Bảo mật tài khoản và phòng chống lừa đảo](B3-account-security-scams.md), [A1 — Tiền gửi và trái phiếu](A1-deposits-government-corporate-bonds.md).
- Mô hình thực hành đi kèm: [`../practice/models/market_returns.py`](../practice/models/market_returns.py) và [`../practice/models/risk_performance.py`](../practice/models/risk_performance.py).
- Câu hỏi cốt lõi: Khi bạn bỏ 3 tỷ đồng mua vàng miếng, mua một căn hộ cho thuê hay nạp tiền vào một sàn giao dịch tài sản số, bạn đang thực sự sở hữu quyền pháp lý gì, ai đang giữ tài sản đó, và bạn mất bao nhiêu phần trăm chi phí ma sát ngay giây phút vừa giao dịch xong?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/A3-fact-check.md), [phản biện](../reviews/A3-risk-review.md).

---

## Hiểu bài trong một phút

Trước khi xuống tiền vào bất kỳ lớp tài sản nào ngoài cổ phiếu và trái phiếu, nhà đầu tư tỉnh táo phải đặt tài sản đó lên **bàn cân 3 chiều**:
1. **Chiều thứ nhất — Tài sản có tự sinh ra dòng tiền định kỳ (`Intrinsic Cash Flow`) hay không?**
   - Một căn nhà cho thuê tạo ra tiền thuê hằng tháng; một cổ phiếu chia cổ tức từ lợi nhuận nhà máy; một trái phiếu trả lãi cuống phiếu định kỳ.
   - Ngược lại, `1 lượng vàng vật chất` để trong két sắt hay `1 đồng tiền mã hóa` sau 10 năm vẫn chỉ là `1 lượng vàng` hay `1 đồng tiền mã hóa` — chúng **không tự đẻ ra tiền lãi hay dòng tiền kinh doanh** (`SỰ_THẬT`). Kết quả đầu tư phụ thuộc hoàn toàn vào việc người mua sau có chấp nhận trả giá cao hơn giá bạn đã mua (trừ đi chênh lệch giá mua – bán và chi phí cất giữ) hay không (`SUY_LUẬN`).
2. **Chiều thứ hai — Chi phí ma sát hai chiều (`Round-Trip Friction Cost`):** Giá niêm yết chiều bán ra của tiệm vàng hay giá chào bán nhà đất trên mạng không phải là số tiền mặt bạn cầm về nếu bán lại ngay lập tức. Khi tiệm vàng niêm yết giá mua vào $P_{\text{Bid}} = 96$ và giá bán ra cho khách $P_{\text{Ask}} = 100$, ngay giây phút bạn vừa mua xong bước ra khỏi cửa hàng, bạn đã lỗ ngay `-4,0%` và giá vàng phải tăng tối thiểu **`+4,17%`** ($100/96 - 1$) bạn mới hòa vốn (`PHÉP_TÍNH`)!
3. **Chiều thứ ba — Quyền sở hữu pháp lý và Rủi ro đối tác lưu ký (`Custody & Legal Risk`):** Giữ vàng vật chất hợp pháp khác với giao dịch "vàng tài khoản" trái phép; đứng tên Giấy chứng nhận quyền sử dụng đất (`Sổ hồng/Sổ đỏ`) khác với ký "hợp đồng góp vốn dự án chưa đủ pháp lý"; và việc Nghị quyết `05/2025/NQ-CP` triển khai thí điểm thị trường tài sản mã hóa không đồng nghĩa với việc mọi sàn giao dịch hay mọi đồng token trôi nổi đều được cấp phép hoặc có bảo hiểm tiền gửi (`SỰ_THẬT`).

---

## Buổi 1 — Vàng vật chất và Ngoại tệ: Toán học Giá quy đổi, Spread và Quy định Pháp lý

### 1.1. Bản chất kinh tế của Vàng và Công thức quy đổi Giá vàng Thế giới sang VND/lượng

Theo phân tích của [Hội đồng Vàng Thế giới (`World Gold Council — Risks and Challenges`)](https://www.gold.org/goldhub/research/relevance-of-gold-as-a-strategic-asset/risks-challenges), vàng đóng vai trò là tài sản dự trữ thanh khoản và phân tán rủi ro địa chính trị trong dài hạn, nhưng bản thân vàng không tạo ra dòng tiền định kỳ (`No Yield / Coupon`) và có độ biến động giá (`Volatility`) tương đương nhiều lớp tài sản rủi ro, nên không đảm bảo luôn tăng giá trong mọi khung thời gian ngắn hạn (`SỰ_THẬT`).

Tại Việt Nam, đơn vị đo lường vàng truyền thống là **1 lượng (cây) vàng = `37,5 gram` = `1,205653 troy ounce`** (vì `1 troy ounce` quốc tế $= 31,1034768\text{ gram}$, nên $37,5 / 31,1034768 = 1,205653\text{ oz}$ — `PHÉP_TÍNH`). Do đó, công thức quy đổi từ giá vàng giao ngay quốc tế ($P_{\text{XAU/USD}}$, tính bằng `USD/oz`) sang giá vàng quy đổi tương đương bằng `VND/lượng` (chưa tính thuế, phí vận chuyển, gia công) theo tỷ giá $\text{FX}_{\text{USD/VND}}$ là:

$$P_{\text{Quy đổi (VND/lượng)}} = P_{\text{XAU/USD}} \times 1,205653 \times \text{FX}_{\text{USD/VND}}$$

Khoảng cách giữa giá vàng miếng bán ra trong nước ($P_{\text{Nội địa}}$) và giá thế giới quy đổi gọi là **Mức phụ trội giá vàng nội địa (`Domestic Gold Premium`)**:

$$\text{Gold Premium (VND/lượng)} = P_{\text{Nội địa}} - P_{\text{Quy đổi}}, \qquad \text{Gold Premium (\%)} = \frac{P_{\text{Nội địa}} - P_{\text{Quy đổi}}}{P_{\text{Quy đổi}}}$$

*Hai rủi ro định lượng khi mua vàng vật chất ở vùng `Spread` và `Premium` cao (`SUY_LUẬN`):*
1. **Rào cản hòa vốn từ Chênh lệch giá Mua – Bán (`Bid-Ask Spread`):** Nếu đơn vị kinh doanh vàng niêm yết giá mua vào từ khách là $P_{\text{Bid}}$ và giá bán ra cho khách là $P_{\text{Ask}}$ ($P_{\text{Ask}} > P_{\text{Bid}}$), tỷ lệ tăng giá tối thiểu của $P_{\text{Bid}}$ để người mua hòa vốn là:
   $$R_{\text{Hòa vốn}} = \frac{P_{\text{Ask}} - P_{\text{Bid}}}{P_{\text{Bid}}} = \frac{P_{\text{Ask}}}{P_{\text{Bid}}} - 1$$
2. **Rủi ro thu hẹp `Domestic Gold Premium`:** Nếu bạn mua vàng trong nước khi $P_{\text{Nội địa}}$ đang cao hơn giá thế giới quy đổi `12 triệu VND/lượng`, sau đó cơ quan quản lý tăng cung hoặc sửa đổi cơ chế thị trường kéo chênh lệch thu hẹp về `2 triệu VND/lượng`, bạn vẫn lỗ `10 triệu VND/lượng` ngay cả khi giá vàng thế giới đi ngang!

### 1.2. Khung pháp lý quản lý hoạt động kinh doanh vàng và ngoại tệ tại Việt Nam

- `SỰ_THẬT`: Chính phủ đã ban hành [Nghị định số 232/2025/NĐ-CP](https://xaydungchinhsach.chinhphu.vn/toan-van-nghi-dinh-so-232-2025-nd-cp-sua-doi-bo-sung-nghi-dinh-24-2012-nd-cp-ve-quan-ly-hoat-dong-kinh-doanh-vang-119250829100240562.htm) (hiệu lực từ `10/10/2025`) và tiếp tục ban hành [Nghị định số 390/2026/NĐ-CP](https://xaydungchinhsach.chinhphu.vn/nghi-dinh-so-390-2026-nd-cp-sua-doi-bo-sung-quy-dinh-quan-ly-hoat-dong-kinh-doanh-vang-119261017180443142.htm) (hiệu lực từ `16/10/2026`) sửa đổi, bổ sung quy định về quản lý hoạt động kinh doanh vàng. Đáng chú ý, theo quy định được công bố trên Cổng thông tin Chính phủ, các giao dịch mua, bán vàng có giá trị từ **`5 triệu đồng` trong ngày trở lên phải thực hiện thanh toán qua tài khoản (không dùng tiền mặt)** và có hóa đơn điện tử minh bạch.
- **Đối với Ngoại tệ:** Việc mua, bán, nắm giữ ngoại tệ tiền mặt của cá nhân tại Việt Nam chịu sự điều chỉnh nghiêm ngặt của Pháp lệnh Ngoại hối; đồng thời lãi suất tiền gửi tiết kiệm bằng `USD` tại ngân hàng thương mại Việt Nam hiện áp trần `0%/năm` và tiền gửi ngoại tệ không thuộc phạm vi Bảo hiểm tiền gửi Việt Nam (như đã học ở Bài [A1](A1-deposits-government-corporate-bonds.md)). Tuyệt đối không nhầm việc nắm giữ ngoại tệ hợp pháp phục vụ nhu cầu du học/công tác với việc nạp tiền vào các sàn giao dịch ngoại hối ký quỹ (`Forex Margin`) không phép!

---

## Buổi 2 — Kinh tế học Bất động sản Cá nhân: Net Cap Rate và Đòn bẩy Tài chính

### 2.1. Phân biệt Lợi suất cho thuê gộp (`Gross Yield`) và Tỷ suất vốn hóa ròng (`Net Cap Rate`)

Khi môi giới chào bán một căn hộ hoặc nhà phố giá $P_{\text{Mua}}$ (cộng thuế trước bạ, phí công chứng, sửa chữa nội thất ban đầu thành **Tổng vốn đầu tư ban đầu $I_{\text{Tổng}}$**), họ thường lấy tiền thuê 1 tháng lúc có khách nhân với 12 tháng rồi chia cho giá mua để quảng cáo "Lợi suất cho thuê `5%/năm`". Phép tính đó bỏ sót hoàn toàn 4 khoản hao hụt thực tế trong năm:
1. **Tỷ lệ thời gian trống khách (`Vacancy Rate` — $v$):** Giữa hai người thuê nhà thường mất 1–2 tháng trống phòng tìm khách mới (ví dụ trống 1 tháng/năm tương đương $v = 1/12 = 8,33\%$).
2. **Phí môi giới cho thuê và Phí quản lý vận hành/bảo trì định kỳ (`OPEX`):** Thường mất thêm 1 tháng tiền thuê cho môi giới mỗi hợp đồng, cộng chi phí sửa chữa điện nước, sơn sửa hao mòn nội thất (`Khấu hao nội thất`).
3. **Thuế cho thuê tài sản:** Tại Việt Nam, cá nhân có doanh thu cho thuê tài sản trên ngưỡng quy định phải nộp thuế GTGT và thuế TNCN tính trên doanh thu cho thuê.

Do đó, công thức chuẩn để tính **Thu nhập hoạt động ròng hằng năm (`Net Operating Income — NOI`)** và **Tỷ suất vốn hóa ròng (`Net Capitalization Rate — Net Cap Rate`)** khi mua đứt 100% bằng vốn tự có là:

$$\text{NOI} = \text{Tiền thuê lý thuyết 12 tháng} \times (1 - v) - \text{Chi phí bảo trì, môi giới, quản lý} - \text{Thuế cho thuê tài sản}$$

$$\text{Net Cap Rate} = \frac{\text{NOI}}{I_{\text{Tổng (Giá mua + Thuế phí + Nội thất)}}}$$

### 2.2. Đòn bẩy vay mua bất động sản: Khi nào Đòn bẩy giúp tăng ROE, khi nào Đòn bẩy "cắn ngược"?

Giả sử bạn đầu tư tổng cộng $I_{\text{Tổng}} = E_0 + D_0$, trong đó vốn tự có bỏ ra là $E_0$ và vay ngân hàng $D_0$ với lãi suất vay $i_d/\text{năm}$ (chi phí lãi vay hằng năm là $D_0 \times i_d$). Khi đó, dòng tiền ròng trước trả nợ gốc trên vốn tự có (**Tỷ suất tiền mặt trên vốn chủ — `Levered Yield / Cash-on-Cash Return`**) là:

$$\text{ROE}_{\text{Dòng tiền cho thuê}} = \frac{\text{NOI} - D_0 \times i_d}{E_0} = \text{Net Cap Rate} + \frac{D_0}{E_0} \times \left(\text{Net Cap Rate} - i_d\right)$$

Nhìn vào phương trình đòn bẩy kinh điển trên, bạn thấy ngay sự thật lạnh lùng tại thị trường Việt Nam (`SUY_LUẬN`):
- Thông thường tại Hà Nội và TP.HCM, `Net Cap Rate` của căn hộ/nhà phố cho thuê chỉ đạt từ **`2,5%` đến `4,0%/năm`**, trong khi lãi suất vay mua nhà sau khi hết ưu đãi 12 tháng đầu thường thả nổi ở mức **`9,0%` đến `11,0%/năm`** ($\text{Net Cap Rate} \ll i_d$).
- Vì $(\text{Net Cap Rate} - i_d) < 0$ (ví dụ $3,5\% - 10,0\% = -6,5\%$), nên **dòng tiền cho thuê âm nặng sau khi trả lãi vay (`Negative Carry`)**! Người vay mua bất động sản thực chất phải lấy tiền lương hằng tháng bù vào khoảng chênh lệch `-6,5%/năm` trên số nợ vay đó và đặt cược rằng giá bán căn nhà sẽ tăng mạnh hơn mức bù lãi. Nếu giá bất động sản đi ngang hoặc giảm trong 3 năm trong khi lãi suất thả nổi giữ ở mức `10%/năm`, đòn bẩy sẽ bào mòn vốn tự có cực nhanh (`PHÉP_TÍNH`).

---

## Buổi 3 — Tài sản Mã hóa (Crypto Assets): Lưu ký, Khung pháp lý Thí điểm và Cảnh báo Rủi ro

### 3.1. Phân biệt Rủi ro Biến động giá với Rủi ro Đối tác / Nền tảng Lưu ký

- `SỰ_THẬT`: Tại Việt Nam, Chính phủ đã ban hành [Nghị quyết số 05/2025/NQ-CP](https://vanban.chinhphu.vn/?classid=0&docid=215249&pageid=27160) về việc triển khai thí điểm thị trường tài sản mã hóa. Việc tồn tại cơ chế thí điểm có kiểm soát nhằm thiết lập khung quản lý nhà nước, phòng chống rửa tiền và bảo vệ trật tự tài chính; hoàn toàn **không đồng nghĩa** với việc mọi sàn giao dịch quốc tế, mọi ứng dụng kêu gọi đầu tư hay mọi đồng token đều được pháp luật bảo hộ hoặc có bảo hiểm tiền gửi (`SỰ_THẬT`).
- `SỰ_THẬT`: Theo tài liệu cảnh báo chính thức của [SEC Hoa Kỳ — Crypto Asset Securities Investor Alert (`23/03/2023`)](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-alerts/crypto-asset-securities), bên cạnh rủi ro biến động giá cực đoan và thiếu dòng tiền nội tại, nhà đầu tư cá nhân đối mặt với 4 rủi ro cấu trúc đặc thù:
  1. **Rủi ro nền tảng lưu ký tập trung (`Custodial Platform Insolvency`):** Khi bạn để tài sản trên một sàn giao dịch hoặc nền tảng cho vay tài sản mã hóa, bạn không trực tiếp giữ khóa riêng tư (`Private Key`) mà chỉ là một **chủ nợ không có bảo đảm** của sàn đó. Khi sàn bị tấn công mạng (`Hack`), trộn lẫn tiền khách hàng (`Commingling of Customer Funds`) hoặc đóng băng lệnh rút tiền (`Freeze Withdrawals`), con số hiển thị trên màn hình ứng dụng không thể rút ra thành tiền thật.
  2. **Rủi ro thao túng thị trường (`Wash Trading`, `Pump-and-Dump`):** Khối lượng giao dịch ảo tự mua tự bán để đẩy giá rồi xả cho người đến sau.
  3. **Rủi ro cam kết lãi suất cố định ảo (`Fake Staking / Yield Farming`):** Chào mời gửi token nhận lãi cố định `15%–30%/năm` mà không có nguồn thu kinh tế thực chất.
  4. **Chi phí ẩn và Trượt giá thanh khoản (`Slippage` & `Gas Fees`).**

---

## 4. Ví dụ từ nguồn thật: Định lượng Giá vàng quy đổi theo Nghị định 232/2025 & 390/2026 và Bất động sản cho thuê

1. **Thực hành quy đổi giá vàng quốc tế và tính điểm hòa vốn `Spread`:**
   - `SỰ_THẬT`: Theo [Nghị định 232/2025/NĐ-CP](https://xaydungchinhsach.chinhphu.vn/toan-van-nghi-dinh-so-232-2025-nd-cp-sua-doi-bo-sung-nghi-dinh-24-2012-nd-cp-ve-quan-ly-hoat-dong-kinh-doanh-vang-119250829100240562.htm) và [Nghị định 390/2026/NĐ-CP](https://xaydungchinhsach.chinhphu.vn/nghi-dinh-so-390-2026-nd-cp-sua-doi-bo-sung-quy-dinh-quan-ly-hoat-dong-kinh-doanh-vang-119261017180443142.htm), giao dịch mua bán vàng từ `5 triệu đồng/ngày` trở lên phải thanh toán không dùng tiền mặt qua tài khoản ngân hàng.
   - `KỊCH_BẢN` & `PHÉP_TÍNH`: Giả sử tại một ngày giao dịch, giá vàng giao ngay thế giới là $P_{\text{XAU/USD}} = 2.750\text{ USD/oz}$ và tỷ giá quy đổi là $\text{FX} = 25.400\text{ VND/USD}$. Một đơn vị kinh doanh vàng được cấp phép trong nước niêm yết giá mua vào từ khách là $P_{\text{Bid}} = 87,00\text{ triệu VND/lượng}$ và giá bán ra cho khách là $P_{\text{Ask}} = 89,00\text{ triệu VND/lượng}$:
     - Giá vàng thế giới quy đổi sang `VND/lượng` ($1\text{ lượng} = 1,205653\text{ oz}$):
       $$P_{\text{Quy đổi}} = 2.750 \times 1,205653 \times 25.400 = 84.214.862\text{ VND/lượng}\; (\approx 84,21\text{ triệu VND/lượng})$$
     - Mức phụ trội (`Domestic Gold Premium`) tại giá khách mua vào ($P_{\text{Ask}} = 89,00\text{ triệu}$):
       $$\text{Gold Premium} = 89,00 - 84,21 = +4,79\text{ triệu VND/lượng}\; (+5,69\%)$$
     - Tỷ lệ tăng giá tối thiểu của chiều mua lại ($P_{\text{Bid}}$) để người mua tại giá `89,00 triệu` hòa vốn:
       $$R_{\text{Hòa vốn}} = \frac{89,00 - 87,00}{87,00} = \frac{2,00}{87,00} = +2,2989\%\; (\approx +2,30\%)$$

2. **Thực hành tính `Net Cap Rate` và Đòn bẩy căn hộ cho thuê:**
   - `KỊCH_BẢN` & `PHÉP_TÍNH`: Một căn hộ có tổng vốn đầu tư ban đầu (giá mua + thuế phí + nội thất) là $I_{\text{Tổng}} = 4.000\text{ triệu VND}$ (`4,0 tỷ VND`). Giá cho thuê là `16 triệu VND/tháng` (`192 triệu VND/năm`), nhưng bình quân mỗi năm trống khách 1 tháng ($v = 1/12$, tức thực thu 11 tháng = `176 triệu VND/năm`), chi phí môi giới + bảo trì nội thất + thuế cho thuê là `36 triệu VND/năm`:
     - Thu nhập hoạt động ròng hằng năm: $\text{NOI} = 176 - 36 = 140\text{ triệu VND/năm}$.
     - Tỷ suất vốn hóa ròng: $\text{Net Cap Rate} = 140 / 4.000 = 3,50\%/\text{năm}$ (thấp hơn nhiều so với con số lợi suất gộp quảng cáo $192 / 4.000 = 4,80\%/\text{năm}$).

---

## 5. Bài làm với dữ liệu thiếu hoặc lệch (Dirty-Data Exercise)

### Tình huống dữ liệu bẩn
Một môi giới bất động sản gửi cho bạn bảng tính mua một căn nhà phố thương mại (`Shophouse`) trị giá `10,0 tỷ VND`:
> *"Chỉ cần bỏ ra 3,0 tỷ VND vốn tự có, ngân hàng cho vay 7,0 tỷ VND với lãi suất ưu đãi năm đầu 6,0%/năm! Căn Shophouse này đang có hợp đồng cam kết thuê lại 500 triệu VND/năm (tương đương lợi suất 5,0%/năm). Năm đầu tiên bạn thu 500 triệu tiền thuê, trả lãi ngân hàng 7,0 tỷ × 6% = 420 triệu, vẫn dư ra +80 triệu VND tiền mặt bỏ túi!"*

Khi đọc kỹ **Hợp đồng tín dụng ngân hàng** và **Hợp đồng thuê mặt bằng**, bạn phát hiện 4 dữ kiện bị giấu đi (`KỊCH_BẢN`):
1. Ngoài `10,0 tỷ VND` giá mua căn nhà ở trạng thái xây thô, bạn phải tự bỏ thêm **`800 triệu VND`** tiền mặt để hoàn thiện nội thất và nộp thuế trước bạ mới có thể bàn giao cho người thuê (tức tổng vốn đầu tư thực tế $I_{\text{Tổng}} = 10,8\text{ tỷ VND}$, và vốn tự có thực bỏ ra là $E_0 = 3,8\text{ tỷ VND}$).
2. Mức tiền thuê `500 triệu VND/năm` chỉ là chương trình "hỗ trợ tiền thuê năm đầu" của chủ đầu tư (thực chất trích từ chính giá bán căn nhà trả lại cho bạn). Từ Năm thứ 2 trở đi, giá thuê thị trường thực tế của khu vực đó chỉ đạt `300 triệu VND/năm`, và sau khi trừ thời gian trống khách, bảo trì, thuế cho thuê còn lại $\text{NOI}_{\text{thực}} = 240\text{ triệu VND/năm}$ (`Net Cap Rate` thực chỉ đạt $240 / 10.800 = 2,22\%/\text{năm}$!).
3. Từ Năm thứ 2 trở đi, lãi suất vay ngân hàng `7,0 tỷ VND` hết ưu đãi chuyển sang thả nổi ở mức **`10,5%/năm`**, tức chỉ riêng tiền lãi vay mỗi năm đã vọt lên $7.000 \times 10,5\% = 735\text{ triệu VND/năm}$!
4. Ngoài tiền lãi vay, hợp đồng tín dụng 15 năm yêu cầu bạn phải **trả nợ gốc đều đặn mỗi năm** $7.000 / 15 = 466,67\text{ triệu VND/năm}$ bằng tiền mặt.

### Quy trình làm sạch dòng tiền từ Năm thứ 2 trở đi
- **Dòng tiền ròng trước trả nợ gốc từ Năm 2 (`Cash-on-Cash Return`):**
  $$\text{CF}_{\text{trước trả gốc}} = \text{NOI}_{\text{thực}} - \text{Lãi vay thả nổi} = 240 - 735 = -495\text{ triệu VND/năm}\quad (\text{PHÉP\_TÍNH})$$
  Tỷ suất dòng tiền trên `3,8 tỷ VND` vốn tự có là $-495 / 3.800 = -13,03\%/\text{năm}$!
- **Tổng dòng tiền mặt phải bù thêm mỗi năm (tính cả trả nợ gốc `466,67 triệu VND`):**
  $$\text{Tiền mặt thực thiếu hụt mỗi năm} = 240 - (735 + 466,67) = -961,67\text{ triệu VND/năm}\quad (\approx -80,1\text{ triệu VND/tháng!})$$
  Nếu người mua không có thu nhập ngoài ổn định trên `100 triệu VND/tháng` để bù khoản thiếu hụt `-80,1 triệu VND/tháng` này từ Năm thứ 2, họ sẽ buộc phải bán tháo căn nhà trong thế bị ép giá (`Forced Liquidation`) (`SUY_LUẬN`).

---

## 6. Sai ở đâu? (Bắt lỗi suy luận)

Hãy chỉ ra chỗ sai trong suy nghĩ sau:

> *"Hôm nay tiệm vàng niêm yết giá Mua vào là 86,0 triệu đồng/lượng và giá Bán ra là 90,0 triệu đồng/lượng (chênh lệch 4,0 triệu đồng trên giá mua của tôi là 4 / 90 = 4,44%). Vậy ngày mai giá vàng chỉ cần tăng đúng +4,44% là tôi đem ra tiệm bán lại sẽ hòa vốn!"*

### Phân tích chỗ sai
1. **Nhầm mẫu số khi tính phần trăm tăng giá để hòa vốn sau `Bid-Ask Spread`:**
   - Khi bạn mua vàng từ tiệm, bạn phải trả theo giá **Bán ra của tiệm ($P_{\text{Ask}} = 90,0\text{ triệu VND}$)**.
   - Nhưng khi bạn đem vàng ra bán lại cho tiệm, tiệm trả tiền cho bạn theo giá **Mua vào của tiệm ($P_{\text{Bid}}$, hiện đang ở mốc `86,0 triệu VND`)**!
2. **Phép tính đúng:** Để giá Mua vào của tiệm ($P_{\text{Bid}}$) tăng từ `86,0 triệu VND` lên chạm mức giá vốn `90,0 triệu VND` của bạn, giá mua vào của tiệm phải tăng một tỷ lệ tính trên mẫu số `86,0 triệu VND` (chứ không phải `90,0 triệu VND`):
   $$R_{\text{Hòa vốn}} = \frac{90,0 - 86,0}{86,0} = \frac{4,0}{86,0} = +4,651\%\; (> 4,444\%)\quad (\text{PHÉP\_TÍNH})$$
   Mọi phép tính tỷ suất hòa vốn sau khi chịu một mức chiết khấu hay `Spread` $s$ đều tuân theo công thức bất đối xứng $\frac{1}{1 - s} - 1 > s$ (giống như giảm `-50%` thì phải tăng `+100%` mới về bờ!).

---

## 7. Bài tập (10 câu)

1. Phân loại 6 tài sản sau thành hai nhóm **Tài sản tạo dòng tiền nội tại (`Cash-Flow Generating`)** và **Tài sản không tạo dòng tiền định kỳ (`Non-Yielding`)**: (a) Cổ phiếu ngành điện trả cổ tức; (b) Vàng miếng vật chất; (c) Trái phiếu Chính phủ; (d) Ngoại tệ tiền mặt (`USD`); (e) Căn hộ chung cư cho thuê; (f) Đồng tiền mã hóa không có doanh thu thực.
2. Tại một thời điểm, giá vàng giao ngay quốc tế là $P_{\text{XAU/USD}} = 2.680\text{ USD/oz}$ và tỷ giá $\text{FX}_{\text{USD/VND}} = 25.300\text{ VND/USD}$. Biết `1 lượng = 37,5 gram = 1,205653 troy ounce`. Tính giá vàng thế giới quy đổi sang `VND/lượng`. Nếu giá vàng miếng bán ra trong nước đang là `86,50 triệu VND/lượng`, mức phụ trội (`Domestic Gold Premium`) đang là bao nhiêu triệu VND/lượng và bao nhiêu phần trăm?
3. Một cửa hàng kinh doanh vàng hợp pháp niêm yết giá mua vào từ khách là $P_{\text{Bid}} = 84,50\text{ triệu VND/lượng}$ và giá bán ra cho khách là $P_{\text{Ask}} = 87,20\text{ triệu VND/lượng}$. Nếu bạn mua `2 lượng` vàng tại giá `87,20 triệu VND/lượng`: (a) Tổng số tiền bạn phải thanh toán (và theo Nghị định `390/2026/NĐ-CP`, giao dịch này phải thanh toán bằng hình thức nào?); (b) Nếu bán lại ngay lập tức bạn lỗ bao nhiêu triệu VND; và (c) Giá mua vào của cửa hàng ($P_{\text{Bid}}$) phải tăng tối thiểu bao nhiêu phần trăm để bạn hòa vốn?
4. Một căn nhà cho thuê có giá mua ban đầu cùng toàn bộ thuế phí, nội thất là $I_{\text{Tổng}} = 5.000\text{ triệu VND}$ (`5,0 tỷ VND`). Giá cho thuê mỗi tháng là `20 triệu VND/tháng` (`240 triệu VND/năm`). Trung bình mỗi năm nhà bị trống khách 1,5 tháng (tức chỉ thu được tiền thuê của `10,5 tháng`), chi phí bảo trì sửa chữa là `18 triệu VND/năm` và thuế cho thuê tài sản cùng phí môi giới là `22 triệu VND/năm`. Tính: (a) Lợi suất cho thuê gộp lý thuyết (`Gross Rental Yield`); (b) Thu nhập hoạt động ròng (`NOI`); và (c) Tỷ suất vốn hóa ròng (`Net Cap Rate`).
5. Tiếp nối Câu 4: Giả sử để mua căn nhà `5,0 tỷ VND` trên, nhà đầu tư dùng $E_0 = 2.500\text{ triệu VND}$ vốn tự có và vay ngân hàng $D_0 = 2.500\text{ triệu VND}$ ($D/E = 1,0\text{ lần}$). Tính dòng tiền ròng sau lãi vay ($\text{NOI} - D_0 \times i_d$) và tỷ suất dòng tiền trên vốn tự có (`ROE dòng tiền`) trong hai kịch bản lãi suất vay: (a) Lãi suất vay ưu đãi cực thấp giả định $i_d = 2,5\%/\text{năm}$; và (b) Lãi suất vay thả nổi thực tế $i_d = 9,5\%/\text{năm}$.
6. Giải thích sự khác biệt về bản chất pháp lý và rủi ro giữa: (a) Mua và nắm giữ ngoại tệ tiền mặt hợp pháp hoặc gửi ngoại tệ tại ngân hàng thương mại; với (b) Nạp tiền vào một ứng dụng giao dịch phái sinh tỷ giá có đòn bẩy (`Forex Margin 1:100`) không được cấp phép tại Việt Nam.
7. Theo [Nghị quyết số 05/2025/NQ-CP](https://vanban.chinhphu.vn/?classid=0&docid=215249&pageid=27160) về thí điểm thị trường tài sản mã hóa tại Việt Nam, vì sao người học không được phép suy diễn từ sự tồn tại của nghị quyết thí điểm rằng mọi sàn giao dịch tài sản mã hóa trên Internet đều hợp pháp và được bảo đảm an toàn vốn?
8. Một nhà đầu tư mua một tài sản số trên một nền tảng giao dịch với giá `100 triệu VND`. Khi mua chịu phí giao dịch `0,5%` và trượt giá khớp lệnh (`Slippage`) `1,5%`; khi bán ra cũng chịu phí và trượt giá tổng cộng `2,0%`; đồng thời phí rút tiền khỏi nền tảng là `500.000 VND`. Nếu giá niêm yết trên màn hình không đổi, sau một vòng mua vào rồi bán rút tiền ra ngay, nhà đầu tư còn lại bao nhiêu tiền mặt và đã mất bao nhiêu phần trăm vì chi phí ma sát?
9. Nêu 4 giấy tờ và điều kiện pháp lý bắt buộc phải kiểm tra trực tiếp trước khi đặt cọc mua một bất động sản nhà ở tại Việt Nam.
10. Sử dụng hàm `max_drawdown` và `annualized_volatility` trong mô-đun [`../practice/models/risk_performance.py`](../practice/models/risk_performance.py): Nếu một tài sản không tạo dòng tiền rơi từ mức đỉnh `100` xuống đáy `35` trước khi hồi lên `70`, mức sụt giảm tối đa từ đỉnh (`Maximum Drawdown`) là bao nhiêu phần trăm, và từ đáy `35` tài sản đó phải tăng bao nhiêu phần trăm mới quay lại được mức đỉnh `100`?

---

## 8. Đáp án chi tiết

1. **Phân loại tài sản theo dòng tiền nội tại:**
   - **Tạo dòng tiền nội tại (`Cash-Flow Generating`):** (a) Cổ phiếu ngành điện trả cổ tức; (c) Trái phiếu Chính phủ; (e) Căn hộ chung cư cho thuê.
   - **Không tạo dòng tiền định kỳ (`Non-Yielding`):** (b) Vàng miếng vật chất; (d) Ngoại tệ tiền mặt (`USD`); (f) Đồng tiền mã hóa không có doanh thu thực (`SỰ_THẬT`).
2. **Quy đổi giá vàng thế giới và tính `Domestic Gold Premium`:**
   - $P_{\text{Quy đổi}} = 2.680 \times 1,205653 \times 25.300 = 81.747.962\text{ VND/lượng}$ (`~81,75 triệu VND/lượng`).
   - `Gold Premium` = $86,50 - 81,75 = +4,75\text{ triệu VND/lượng}$, tương đương $+4,75 / 81,75 = +5,81\%$ (`PHÉP_TÍNH`).
3. **Chi phí `Bid-Ask Spread` và quy định thanh toán vàng:**
   - (a) Tổng số tiền thanh toán cho `2 lượng` = $2 \times 87,20 = 174,40\text{ triệu VND}$. Vì giá trị giao dịch $\ge 5\text{ triệu VND/ngày}$, theo Nghị định `390/2026/NĐ-CP`, giao dịch bắt buộc phải **thanh toán không dùng tiền mặt (chuyển khoản qua tài khoản ngân hàng)**.
   - (b) Nếu bán lại ngay tại $P_{\text{Bid}} = 84,50\text{ triệu/lượng}$, lỗ ngay $2 \times (87,20 - 84,50) = 5,40\text{ triệu VND}$.
   - (c) Tỷ lệ tăng tối thiểu của $P_{\text{Bid}}$ để hòa vốn = $\frac{87,20 - 84,50}{84,50} = \frac{2,70}{84,50} = +3,195\%$ (`PHÉP_TÍNH`).
4. **Tính `Gross Rental Yield`, `NOI` và `Net Cap Rate` của căn nhà `5,0 tỷ VND`:**
   - (a) `Gross Rental Yield` lý thuyết = $240 / 5.000 = 4,80\%/\text{năm}$.
   - (b) Tiền thuê thực thu (`10,5 tháng`) = $10,5 \times 20 = 210\text{ triệu VND/năm} \implies \text{NOI} = 210 - 18 - 22 = 170\text{ triệu VND/năm}$.
   - (c) `Net Cap Rate` = $170 / 5.000 = 3,40\%/\text{năm}$ (`PHÉP_TÍNH`).
5. **Tác động của Đòn bẩy vay `2,5 tỷ VND` lên `ROE dòng tiền` ($\text{NOI} = 170\text{ triệu}$, $\text{Net Cap Rate} = 3,40\%$):**
   - (a) Khi $i_d = 2,5\% < 3,40\%$: Lãi vay = $2.500 \times 2,5\% = 62,5\text{ triệu} \implies \text{CF ròng} = 170 - 62,5 = +107,5\text{ triệu VND/năm} \implies \text{ROE dòng tiền} = 107,5 / 2.500 = +4,30\%/\text{năm}$ (đòn bẩy khuếch đại dương).
   - (b) Khi $i_d = 9,5\% > 3,40\%$: Lãi vay = $2.500 \times 9,5\% = 237,5\text{ triệu} \implies \text{CF ròng} = 170 - 237,5 = -67,5\text{ triệu VND/năm} \implies \text{ROE dòng tiền} = -67,5 / 2.500 = -2,70\%/\text{năm}$ (đòn bẩy ăn mòn vốn tự có!) (`PHÉP_TÍNH`).
6. **Phân biệt nắm giữ ngoại tệ hợp pháp và sàn `Forex Margin` trái phép:**
   - Giữ ngoại tệ hợp pháp là nắm tài sản tiền tệ không có đòn bẩy; còn nạp tiền vào ứng dụng `Forex Margin 1:100` không phép là đánh cược phái sinh đòn bẩy gấp 100 lần (chỉ cần tỷ giá ngược chiều `1%` là cháy `100%` tài khoản) tại các tổ chức không được pháp luật Việt Nam cấp phép, kèm rủi ro bị chiếm đoạt tiền nạp (xem thêm Bài [B3](B3-account-security-scams.md)).
7. **Giới hạn của Nghị quyết `05/2025/NQ-CP`:**
   - Nghị quyết thí điểm chỉ áp dụng cho phạm vi, tổ chức và điều kiện được cơ quan nhà nước có thẩm quyền phê duyệt trong khuôn khổ thí điểm; không hợp thức hóa các sàn giao dịch tự phát hay bảo đảm giá trị cho bất kỳ đồng token nào (`SỰ_THẬT`).
8. **Tính hao hụt chi phí ma sát hai chiều (`100 triệu VND`):**
   - Giá trị tài sản thực nhận sau khi mua (trừ `2,0%` phí + trượt giá chiều mua) = $100.000.000 \times (1 - 2,0\%) = 98.000.000\text{ VND}$.
   - Giá trị thu về khi bán ra (trừ tiếp `2,0%` chiều bán) = $98.000.000 \times (1 - 2,0\%) = 96.040.000\text{ VND}$.
   - Trừ tiếp `500.000 VND` phí rút tiền: còn lại **`95.540.000 VND`**, tức mất ngay **`-4,46%`** vốn gốc dù giá thị trường không hề giảm (`PHÉP_TÍNH`)!
9. **Bốn giấy tờ/điều kiện pháp lý cần kiểm khi mua nhà đất:**
   - (1) Bản gốc Giấy chứng nhận quyền sử dụng đất, quyền sở hữu tài sản gắn liền với đất (`Sổ đỏ/Sổ hồng`) và danh tính chính chủ; (2) Tình trạng thế chấp ngân hàng, kê biên thi hành án hoặc tranh chấp đồng sở hữu; (3) Thông tin quy hoạch sử dụng đất, lộ giới tại cơ quan chức năng địa phương; (4) Điều khoản thanh toán qua ngân hàng và nghĩa vụ thuế TNCN, lệ phí trước bạ trong hợp đồng công chứng.
10. **Tính `Maximum Drawdown` và tỷ lệ tăng hồi phục từ đáy (`100 -> 35 -> 70`):**
    - `Maximum Drawdown` = $\frac{35 - 100}{100} = -65,0\%$ (hoặc độ lớn `65,0%`).
    - Từ đáy `35`, để quay lại mức đỉnh `100`, tài sản đó phải tăng: $\frac{100 - 35}{35} = \frac{65}{35} = +185,71\%$ (gần gấp 3 lần giá trị ở đáy!) (`PHÉP_TÍNH`).

---

## 9. Kiểm tra chuyển bài (Transfer Check)

Trước khi chuyển sang Bài [A4 — Phân bổ tài sản, tương quan và tái cân bằng](A4-allocation-correlation-rebalancing.md), hãy tự kiểm tra 3 kỹ năng sau:
1. **Ghép các lớp tài sản (`A1 + A2 + A3`) thành một Danh mục (`A4`):** Sau khi đã hiểu rõ Tiền gửi & Trái phiếu (`A1`), Quỹ mở & `ETF` cổ phiếu (`A2`), và Vàng / Bất động sản (`A3`), ở Bài [A4](A4-allocation-correlation-rebalancing.md) bạn sẽ học cách kết hợp chúng theo hệ số tương quan ($\rho$) và kỷ luật tái cân bằng (`Rebalancing`). Bạn đã phân biệt được vai trò tạo dòng tiền của Cổ phiếu/Trái phiếu với vai trò phòng thủ của Tiền gửi/Vàng trong danh mục chưa?
2. **Phản xạ kiểm tra `Net Cap Rate` vs. Lãi suất vay ($i_d$):** Khi ai đó rủ bạn vay ngân hàng mua bất động sản cho thuê, bạn đã nhớ đặt bút tính ngay xem $\text{Net Cap Rate} - i_d$ là số dương hay số âm chưa?
3. **Kỷ luật pháp lý và lưu ký:** Bạn đã nắm vững quy định thanh toán không dùng tiền mặt từ `5 triệu VND/ngày` khi giao dịch vàng theo Nghị định `390/2026/NĐ-CP` và nguyên tắc kiểm tra pháp lý nền tảng lưu ký chưa?

---

## 10. Lỗi thường gặp và ranh giới an toàn

- **Bốn lỗi phân tích phổ biến:** (1) Tin rằng vàng hay bất động sản "chỉ có tăng chứ không bao giờ lỗ" mà bỏ qua chênh lệch giá mua – bán (`Spread`), phụ trội giá nội địa (`Premium`) và chi phí cơ hội không có dòng tiền; (2) Lấy tiền thuê gộp 12 tháng chia giá mua làm lợi suất ròng mà quên trừ thời gian trống khách, bảo trì, thuế và lãi vay thả nổi; (3) Coi con số hiển thị trên các ứng dụng tài sản số không phép là tiền mặt chắc chắn rút về được; (4) Dùng vốn vay (`Margin`) hoặc quỹ khẩn cấp của gia đình để đầu cơ tài sản biến động mạnh.
- **Ranh giới an toàn:** Bài học cung cấp kiến thức kinh tế và khung pháp lý công khai về các lớp tài sản; không đưa ra khuyến nghị mua/bán vàng, ngoại tệ, bất động sản hay tài sản mã hóa.

## Nguồn Internet đã mở

- Chốt kiểm tra trực tuyến lúc `2026-11-05 12:15 UTC+7`:
  1. [Cổng Thông tin Chính phủ — Toàn văn Nghị định số 232/2025/NĐ-CP](https://xaydungchinhsach.chinhphu.vn/toan-van-nghi-dinh-so-232-2025-nd-cp-sua-doi-bo-sung-nghi-dinh-24-2012-nd-cp-ve-quan-ly-hoat-dong-kinh-doanh-vang-119250829100240562.htm) (`10/10/2025`) và [Nghị định số 390/2026/NĐ-CP](https://xaydungchinhsach.chinhphu.vn/nghi-dinh-so-390-2026-nd-cp-sua-doi-bo-sung-quy-dinh-quan-ly-hoat-dong-kinh-doanh-vang-119261017180443142.htm) (`16/10/2026`) về quản lý hoạt động kinh doanh vàng.
  2. [Cổng Thông tin điện tử Chính phủ — Nghị quyết số 05/2025/NQ-CP](https://vanban.chinhphu.vn/?classid=0&docid=215249&pageid=27160) về thí điểm thị trường tài sản mã hóa.
  3. [World Gold Council — Risks and Challenges of Gold](https://www.gold.org/goldhub/research/relevance-of-gold-as-a-strategic-asset/risks-challenges) (`04/02/2026`) và [SEC Investor Alert — Crypto Asset Securities (`23/03/2023`)](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-alerts/crypto-asset-securities).
