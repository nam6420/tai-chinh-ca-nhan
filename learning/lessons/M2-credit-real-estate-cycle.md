# Bài M2 — Chu kỳ tín dụng và bất động sản

- Ngày: `2026-11-05`
- Chốt dữ liệu lúc: `2026-11-05 12:30 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Giải phẫu cơ chế khuếch đại hai chiều giữa tín dụng ngân hàng, giá trị tài sản bảo đảm (`collateral value`) và dòng tiền trả nợ trong chu kỳ bất động sản; đọc đúng các chỉ báo cảnh báo sớm (`early warning indicators`) của BIS và nhận diện ranh giới giữa tài sản bảo đảm trên sổ sách với dòng tiền thu hồi thực tế.
- Bài trước liên quan: [M1](M1-monetary-policy-rates-fx-credit.md), [005](005-debt-liquidity-survival.md), [A3](A3-gold-currency-property-crypto.md), [F3](F3-vietnam-property-developers.md), [F4](F4-vietnam-bank-analysis.md).
- Thời lượng: Ba phiên học có điểm dừng (mỗi phiên 45 phút) + thực hành đối chiếu trên mô hình [bank.py](../practice/models/bank.py) và [earnings_quality.py](../practice/models/earnings_quality.py).
- Câu hỏi cốt lõi: **Vì sao một khoản vay có tài sản bảo đảm là bất động sản định giá gấp rưỡi dư nợ gốc vẫn có thể biến thành nợ xấu làm tê liệt thanh khoản của cả chủ đầu tư lẫn ngân hàng khi chu kỳ đảo chiều?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/M2-fact-check.md), [phản biện](../reviews/M2-risk-review.md).

---

## Hiểu bài trong một phút

Bất động sản và hệ thống ngân hàng gắn chặt với nhau qua một vòng lặp phản hồi có điều kiện được gọi là **cơ chế gia tốc tài chính (`financial accelerator`)**. Ở pha đi lên, tín dụng mở rộng làm tăng sức mua và giá đất; giá đất tăng làm phình giá trị tài sản thế chấp (`collateral`), giúp chủ đầu tư và người mua nhà vay được nhiều tiền hơn nữa trên cùng một mảnh đất. Nhưng ở pha đi xuống — khi giá nhà vượt quá xa thu nhập thực tế của người mua ở thực, pháp lý dự án bị tắc nghẽn hoặc lãi suất thả nổi hết thời gian ưu đãi — dòng tiền bán hàng và tiền thuê ngừng chảy. Lúc này, nhà đầu tư nhận ra một sự thật cốt lõi: **Tài sản bảo đảm không tự sinh ra tiền mặt để trả lãi hàng tháng, và giá trị thẩm định lúc thị trường sốt nóng không bao giờ giữ nguyên khi nhiều con nợ buộc phải bán giải chấp cùng một lúc.** Hiểu cơ chế này giúp bạn đọc xuyên qua bảng cân đối kế toán của cả doanh nghiệp bất động sản ([F3](F3-vietnam-property-developers.md)) lẫn ngân hàng thương mại ([F4](F4-vietnam-bank-analysis.md)) mà không rơi vào bẫy dự báo khủng hoảng cực đoan.

---

## Phiên 1 — Cơ chế gia tốc tài chính (`Financial Accelerator`) và hai tầng tín dụng bất động sản

### 1.1. Vòng lặp phản hồi giữa Tín dụng – Giá tài sản – Tài sản bảo đảm

Trong kinh tế học vĩ mô và ngân hàng, bất động sản không chỉ là một ngành xây dựng – thương mại thông thường mà còn là **vật chứa tài sản thế chấp lớn nhất của hệ thống tín dụng**.

`SUY_LUẬN` Cơ chế khuếch đại hai chiều vận hành qua 5 mắt xích liên hoàn:

| Mắt xích | Pha mở rộng (`Upswing / Boom`) | Pha co hẹp / Đảo chiều (`Downswing / Crunch`) |
|---|---|---|
| **1. Điều kiện tín dụng & Lãi suất** | Lãi suất thấp, hạn mức tín dụng dồi dào, điều kiện phê duyệt khoản vay và phát hành trái phiếu nới lỏng. | Lãi suất thả nổi tái định giá tăng cao, đến hạn đáo hạn trái phiếu lớn hoặc kiểm soát chặt điều kiện giải ngân dự án. |
| **2. Cầu giao dịch & Tiến độ bán hàng (`Pre-sales`)** | Người mua ở thực và nhà đầu tư thứ cấp dùng đòn bẩy mua mạnh; tỷ lệ hấp thụ dự án mở bán mới đạt 70%–90%. | Khả năng chi trả (`affordability`) suy kiệt; nhà đầu tư thứ cấp ngừng xuống tiền; thanh khoản sơ cấp và thứ cấp đóng băng. |
| **3. Giá tài sản & Định giá thế chấp (`Collateral valuation`)** | Giá giao dịch thiết lập mặt bằng mới cao hơn; ngân hàng định giá lại quyền sử dụng đất cao hơn, làm giảm tỷ lệ `LTV` (`Loan-to-Value`) trên sổ sách. | Giá chào bán thực tế phải chiết khấu sâu mới có người mua; giá trị thanh lý thực tế giảm mạnh làm tỷ lệ `LTV` thực tế vượt ngưỡng an toàn. |
| **4. Khả năng vay mới & Tái cấp vốn (`Refinancing`)** | Cùng một quỹ đất có thể thế chấp vay thêm vốn lưu động hoặc phát hành lô trái phiếu mới để thâu tóm quỹ đất tiếp theo. | Không thể phát hành nợ mới để đảo nợ cũ (`rollover risk`); ngân hàng yêu cầu bổ sung tài sản thế chấp hoặc thu hồi nợ. |
| **5. Chất lượng tài sản ngân hàng & Thanh khoản** | Tỷ lệ nợ xấu (`NPL`) báo cáo cực thấp (nhờ tiền bán hàng mới hoặc vay mới); `NIM` ngân hàng mở rộng. | Nợ Nhóm 2 và nợ xấu (Nhóm 3–5) tăng; lãi dự thu phải thoái thu; ngân hàng siết khẩu vị rủi ro khiến tín dụng càng co hẹp. |

`SỰ_THẬT` Báo cáo [World Bank — Viet Nam Economic Update (tháng 05/2026)](https://documents1.worldbank.org/curated/en/099740005122628080/pdf/IDU-2ee874ce-e0c0-462b-9571-99e553ef83c9.pdf) phân tích mối liên hệ giữa tăng trưởng tín dụng bất động sản, khả năng chi trả nhà ở (`housing affordability`) của hộ gia đình và chất lượng tài sản của hệ thống ngân hàng Việt Nam. Đây là phân tích thực chứng dựa trên dữ liệu lịch sử của World Bank nhằm nhấn mạnh việc giám sát rủi ro tập trung tín dụng và sự lệch pha cung – cầu giữa phân khúc cao cấp với nhà ở vừa túi tiền, không phải dự báo giá nhà một địa phương cụ thể.

### 1.2. Hai tầng tín dụng bất động sản không được phép trộn lẫn

Khi đọc số liệu "tín dụng bất động sản", cần tách biệt hai nhóm khách hàng vay có dòng tiền trả nợ và rủi ro pháp lý rất khác nhau:
1. **Tín dụng kinh doanh bất động sản (`Developer loans & corporate bonds`):**
   - **Người vay:** Chủ đầu tư dự án, công ty thành viên (`SPV`) vay ngân hàng hoặc phát hành trái phiếu để giải phóng mặt bằng, nộp tiền sử dụng đất và xây dựng hạ tầng.
   - **Nguồn trả nợ:** Dòng tiền thu trước từ người mua nhà (`Cash pre-sales`) theo tiến độ hợp đồng.
   - **Điểm gãy chí mạng:** Rủi ro pháp lý (chậm phê duyệt quy hoạch 1/500, chậm tính tiền sử dụng đất, chưa đủ điều kiện ký Hợp đồng mua bán). Khi pháp lý đình trệ, chủ đầu tư **không được phép thu tiền theo tiến độ từ khách hàng**, trong khi lãi vay ngân hàng và trái phiếu vẫn tích tụ từng ngày.
2. **Tín dụng mua nhà của cá nhân (`Retail mortgage / homebuyer loans`):**
   - **Người vay:** Cá nhân, hộ gia đình vay mua căn hộ, nhà phố, đất nền.
   - **Điểm gãy chí mạng:** Tại Việt Nam, chủ đầu tư thường tung gói **"ân hạn nợ gốc và hỗ trợ lãi suất 0% trong 18–24 tháng đầu"** (chủ đầu tư trả hộ lãi vay và cộng chi phí đó vào giá bán sơ cấp). Khi hết 24 tháng ân hạn, người mua đột ngột phải tự trả cả nợ gốc lẫn lãi thả nổi (`10%–12%/năm`). Nếu dự án chưa bàn giao (chưa có dòng tiền cho thuê) hoặc giá thứ cấp sụt giảm, người mua dùng đòn bẩy cao sẽ mất khả năng thanh toán, biến rủi ro của chủ đầu tư thành rủi ro nợ xấu bán lẻ tại ngân hàng.

> **Điểm dừng phiên 1:** Liên hệ với bài [F3](F3-vietnam-property-developers.md): Vì sao trên BCTC chủ đầu tư, **"Người mua trả tiền trước ngắn hạn"** tăng kèm `CFO` dương lại là bằng chứng tốt hơn nhiều so với việc **"Phải thu hợp tác đầu tư (BCC)"** tăng mạnh?

---

## Phiên 2 — Toán học của Tài sản bảo đảm (`LTV`), Khả năng trả nợ (`DSCR`) và Thanh lý cưỡng chế (`Fire-sale Haircut`)

### 2.1. Ba công thức định lượng sức chịu đựng của khoản vay bất động sản

Để thẩm định khoản vay dự án hoặc đánh giá danh mục cho vay bất động sản của ngân hàng ([bank.py](../practice/models/bank.py)), người phân tích dùng 3 tỷ số:

1. **Tỷ lệ Dư nợ trên Giá trị tài sản bảo đảm (`Loan-to-Value — LTV`) và Giá trị thu hồi hiện tại ròng (`Net Present Recovery`):**
   $$\text{LTV} = \frac{\text{Dư nợ vay (Loan)}}{\text{Giá trị tài sản bảo đảm (Collateral Value)}}$$
   Khi phát mại tài sản (`forced liquidation`) với chiết khấu thanh khoản $h$, chi phí pháp lý $C_{\text{legal}}$ và thời gian chờ xử lý $t$ năm (chi phí vốn $r$):
   $$\text{PV}_{\text{Recovery}} = \frac{V_0 \times (1 - h) - C_{\text{legal}}}{(1 + r)^t}$$
2. **Hệ số khả năng trả nợ từ dòng tiền (`Debt Service Coverage Ratio — DSCR`):**
   $$\text{DSCR} = \frac{\text{Dòng tiền hoạt động ròng dùng để trả nợ trong kỳ (NOI hoặc Cash Pre-sales ròng)}}{\text{Nghĩa vụ trả lãi vay + Nợ gốc đến hạn trong kỳ (Total Debt Service)}}$$
   Khi `DSCR < 1,00x`, dòng tiền tự thân không đủ trả gốc và lãi đến hạn; doanh nghiệp buộc phải bán tài sản hoặc vay nợ mới trả nợ cũ (`Ponzi financing`).
3. **Gánh nặng trả nợ trên thu nhập hộ gia đình (`Debt-Service-to-Income — DSTI`):**
   $$\text{DSTI} = \frac{\text{Tiền trả gốc và lãi vay mua nhà hàng tháng}}{\text{Thu nhập khả dụng hàng tháng của hộ gia đình}}$$

### 2.2. Kịch bản định lượng: Từ "khoản vay thế chấp an toàn 60%" đến lỗ thu hồi vốn khi chu kỳ đảo chiều

`KỊCH_BẢN` Xét khoản vay dự án thương mại của Công ty Địa ốc Delta tại Ngân hàng X:
- **Giá trị thẩm định tài sản bảo đảm lúc giải ngân (`V_0`):** `500 tỷ VND`.
- **Dư nợ gốc giải ngân (`L_0`):** `300 tỷ VND` (`LTV` ban đầu = `300 / 500 = 60,0%` — tài sản gấp `1,67 lần` dư nợ).
- **Điều khoản trả nợ:** Lãi suất thả nổi Năm 1 là `9,5%/năm`, Năm 2 tái định giá lên `11,5%/năm`. Mỗi năm trả gốc định kỳ `30 tỷ VND` cộng lãi trên dư nợ đầu năm.
- **Dòng tiền cho thuê ròng (`NOI`):** Năm 1 đạt `60 tỷ VND`. Sang Năm 2, do dư cung mặt bằng, `NOI` giảm `40%` còn `36 tỷ VND`.

`PHÉP_TÍNH` Kiểm tra `DSCR` và giá trị thu hồi tài sản thế chấp:
1. **Năm 1 (`Dư nợ gốc = 300 tỷ`, `Lãi suất = 9,5%`):**
   - Lãi Năm 1 = `300 × 9,5% = 28,50 tỷ VND`; Gốc phải trả = `30,00 tỷ VND` → Tổng nghĩa vụ trả nợ Năm 1 = `58,50 tỷ VND`.
   - `DSCR` Năm 1 = `60,00 / 58,50 ≈ 1,0256 lần` (vừa đủ trả gốc và lãi; dư nợ gốc cuối Năm 1 giảm còn `270 tỷ VND`).
2. **Năm 2 (`Dư nợ gốc đầu Năm 2 = 270 tỷ`, `Lãi suất = 11,5%`, `NOI_2 = 36 tỷ`):**
   - Lãi Năm 2 = `270 × 11,5% = 31,05 tỷ VND`; Gốc đến hạn = `30,00 tỷ VND` → Tổng nghĩa vụ trả nợ Năm 2 = `61,05 tỷ VND`.
   - `DSCR` Năm 2 = `36,00 / 61,05 ≈ 0,5897 lần` (`0,59x`, thiếu hụt `25,05 tỷ VND` tiền mặt ngay trong Năm 2!).
3. **Xử lý phát mại tài sản bảo đảm cuối Năm 2:**
   Giả sử cuối Năm 2 Delta mất khả năng thanh toán trên dư nợ gốc `270 tỷ VND` cộng lãi Năm 2 `31,05 tỷ VND` (tổng nghĩa vụ `301,05 tỷ VND`). Ngân hàng X phát mại tài sản bị chiết khấu giá `h = 35%` so với `V_0 = 500 tỷ VND`, chi phí tòa án – đấu giá mất `12 tỷ VND`, và mất `2 năm` mới thu được tiền về (chi phí vốn `r = 8,0%/năm`):
   - Tiền thu ròng danh nghĩa sau 2 năm: `500 × (1 − 35%) − 12 = 325 − 12 = 313,00 tỷ VND`.
   - Giá trị hiện tại tại thời điểm cuối Năm 2:
     $$\text{PV}_{\text{Recovery}} = \frac{313{,}00}{(1 + 8{,}0\%)^2} = \frac{313{,}00}{1{,}1664} \approx 268{,}35\text{ tỷ VND}$$
   - Chênh lệch kinh tế so với tổng nghĩa vụ `301,05 tỷ VND`: `268,35 − 301,05 = −32,70 tỷ VND` (thậm chí thấp hơn cả dư nợ gốc `270 tỷ VND`!).

`SUY_LUẬN` Khi dòng tiền trả nợ (`DSCR`) gãy đổ, **chiết khấu giá bán cưỡng chế (`35%`) cộng thời gian xử lý kéo dài (`2 năm`)** xóa sạch lớp đệm `40%` của tỷ lệ `LTV` ban đầu.

> **Điểm dừng phiên 2:** Mở mô hình [bank.py](../practice/models/bank.py) và giải thích vì sao ngân hàng vẫn phải trích lập dự phòng rủi ro tín dụng (`LLR`) bằng tiền thật dù khoản nợ xấu có tài sản thế chấp là đất đai.

---

## Phiên 3 — Hệ thống chỉ báo cảnh báo sớm (`Early Warning Indicators`) và giới hạn phương pháp luận

`SỰ_THẬT` Nghiên cứu [BIS Quarterly Review — Early warning indicators for banking crises: expanding the family (03/2018)](https://www.bis.org/publications/qr-201803/early-warning-indicators-banking-crises-expanding-family) phân tích hiệu năng và giới hạn của các chỉ báo cảnh báo sớm trên toàn cầu. Không một biến số đơn lẻ nào ấn định được ngày khủng hoảng, mà phải kết hợp 4 nhóm chỉ báo:

| Nhóm chỉ báo | Chỉ tiêu đo lường cụ thể | Tín hiệu cảnh báo tích tụ rủi ro | Giới hạn phương pháp luận (vì sao có thể báo động giả?) |
|---|---|---|---|
| **1. Khoảng cách tín dụng/GDP (`Credit-to-GDP gap`)** | Độ lệch của tỷ lệ `Tín dụng tư nhân / GDP` so với xu hướng dài hạn. | Phản ánh nền kinh tế tăng trưởng dựa quá nặng vào đòn bẩy nợ trong nhiều năm. | Nền kinh tế đang tài chính hóa hợp thức (`financial deepening`) có thể có tín dụng/GDP tăng mà chưa xảy ra đổ vỡ ngay. |
| **2. Tỷ số chi phí trả nợ (`Debt Service Ratio — DSR`)** | Tỷ lệ thu nhập khu vực tư nhân phải trích ra để trả gốc và lãi vay định kỳ. | Khi `DSR` vượt ngưỡng lịch sử (nhất là khi lãi suất nhích tăng), báo hiệu dòng tiền bị vắt kiệt trong 1–2 năm tới. | Số tổng hợp cấp quốc gia có thể che khuất sự phân hóa giữa doanh nghiệp xuất khẩu ít vay nợ và nhóm bất động sản đòn bẩy cao. |
| **3. Giá nhà/Thu nhập & Lợi suất cho thuê (`Rental yield`)** | `Giá nhà / Thu nhập hộ gia đình`; `Lợi suất cho thuê` so với `Lãi vay mua nhà`. | Khi `Lợi suất cho thuê` (`2%–3%/năm`) thấp xa `Lãi vay` (`9%–11%/năm`), người mua chịu dòng tiền âm nặng (`negative carry`). | Giá nhà tại đô thị thiếu cung có thể neo cao kéo dài (thanh khoản đóng băng nhưng không giảm đồng loạt nếu ít dùng đòn bẩy). |
| **4. Chỉ báo vi mô trên BCTC Chủ đầu tư & Ngân hàng** | `Lãi phải thu / Tài sản sinh lời` ([bank.py](../practice/models/bank.py)); `Tồn kho dở dang + Phải thu BCC` và `CFO` ([earnings_quality.py](../practice/models/earnings_quality.py)). | Lãi dự thu ngân hàng phình to; chủ đầu tư báo lãi kế toán nhưng `CFO` âm liên tục và nợ ngắn hạn vượt tiền mặt. | Cơ chế cơ cấu lại thời hạn trả nợ có thể làm độ trễ ghi nhận nợ xấu trên báo cáo kéo dài 4–8 quý. |

`SỰ_THẬT` Tại [Cục Thống kê — Báo cáo Quý III và 9 tháng năm 2026](https://www.nso.gov.vn/bai-top/2026/10/bao-cao-tinh-hinh-kinh-te-xa-hoi-quy-iii-va-9-thang-nam-2026/), tín dụng toàn nền kinh tế đến `28/09/2026` tăng `10,89%` so với cuối năm 2025. `CHƯA_BIẾT` Chỉ tiêu tổng hợp này không tách riêng tín dụng kinh doanh bất động sản hay mua nhà cá nhân; muốn biết tốc độ thực tế của từng mảng phải mở thuyết minh "Cho vay khách hàng theo ngành kinh tế" trên BCTC từng ngân hàng ([F4](F4-vietnam-bank-analysis.md)).

> **Điểm dừng phiên 3:** Lập danh sách 4 chỉ tiêu trên BCTC bạn sẽ kiểm tra đầu tiên khi một công ty bất động sản tuyên bố "đã qua đáy chu kỳ".

---

## Ví dụ từ nguồn thật

1. **Phân tích của World Bank về tín dụng bất động sản và chất lượng tài sản ngân hàng Việt Nam:**
   `SỰ_THẬT` Mở trực tiếp [World Bank — Viet Nam Economic Update (05/2026)](https://documents1.worldbank.org/curated/en/099740005122628080/pdf/IDU-2ee874ce-e0c0-462b-9571-99e553ef83c9.pdf): Báo cáo chỉ ra sự mở rộng nhanh của tín dụng bất động sản đi kèm khoảng cách lớn giữa giá nhà và thu nhập hộ gia đình làm giảm khả năng hấp thụ thực tế ở phân khúc giá cao và tăng rủi ro tập trung tín dụng tại các ngân hàng thương mại.
2. **Nghiên cứu của BIS về các chỉ báo cảnh báo sớm (`Early Warning Indicators`):**
   `SỰ_THẬT` Mở bài nghiên cứu [BIS — Early warning indicators for banking crises: expanding the family (03/2018)](https://www.bis.org/publications/qr-201803/early-warning-indicators-banking-crises-expanding-family): BIS chứng minh chỉ báo `Credit-to-GDP gap` phát tín hiệu sớm về tích tụ đòn bẩy dài hạn, còn `Debt Service Ratio (DSR)` có độ chính xác cao trong khung 1–2 năm trước khi căng thẳng tín dụng bộc lộ.
3. **Dữ liệu tín dụng 9 tháng năm 2026 của Cục Thống kê:**
   `SỰ_THẬT` Mở [Cục Thống kê — Báo cáo Quý III và 9 tháng năm 2026](https://www.nso.gov.vn/bai-top/2026/10/bao-cao-tinh-hinh-kinh-te-xa-hoi-quy-iii-va-9-thang-nam-2026/): Tín dụng toàn nền kinh tế đến `28/09/2026` tăng `10,89%` và huy động vốn tăng `9,78%` so với cuối năm 2025.

---

## Bài tập

Hãy tự giải 10 bài tập dưới đây trước khi mở phần Đáp án:

1. **Tính `LTV` ban đầu và sau khi giá đất giảm:** Chủ đầu tư thế chấp lô đất định giá `400 tỷ VND` để vay `260 tỷ VND`. Tính `LTV` ban đầu. Nếu sau 1 năm giá thị trường lô đất giảm `25%` và dư nợ gốc giữ nguyên `260 tỷ VND`, tỷ lệ `LTV` mới là bao nhiêu?
2. **Tính giá trị thu hồi hiện tại ròng (`Net Present Recovery`):** Khoản nợ xấu có dư nợ gốc `180 tỷ VND` và lãi treo `20 tỷ VND`. Tài sản bảo đảm định giá ban đầu `300 tỷ VND`. Khi phát mại, giá bán thực tế bị chiết khấu `30%`, chi phí pháp lý `10 tỷ VND`, và mất `2 năm` mới thu được tiền về (chi phí vốn `10,0%/năm`). Tính giá trị hiện tại ròng của số tiền thu hồi và phần thiếu hụt so với dư nợ gốc `180 tỷ VND`.
3. **Chi phí trả nợ khi hết thời gian ân hạn/ưu đãi (`Teaser rate reset`):** Người mua nhà vay `4,0 tỷ VND` với gói lãi suất `0%/năm` trong 18 tháng đầu. Từ tháng 19, lãi suất thả nổi là `11,0%/năm` và phải trả gốc đều `200 triệu VND/năm`. Tính tổng tiền gốc và lãi phải trả trong 12 tháng đầu sau ưu đãi (theo năm và trung bình mỗi tháng, tính lãi đơn trên dư nợ đầu kỳ `4,0 tỷ VND`).
4. **Tính tỷ số gánh nặng trả nợ trên thu nhập (`DSTI`):** Tiếp nối Bài tập 3, nếu hộ gia đình có tổng thu nhập khả dụng `45 triệu VND/tháng` và căn hộ chưa bàn giao, tỷ lệ `DSTI` hàng tháng khi bước sang tháng 19 là bao nhiêu?
5. **Chênh lệch lợi suất cho thuê và lãi vay (`Negative Carry`):** Căn nhà phố giá `20 tỷ VND`, cho thuê thu ròng `480 triệu VND/năm`. Tính lợi suất cho thuê ròng (`Net Rental Yield`). Nếu vay `50%` giá trị căn nhà (`10 tỷ VND`) với lãi suất `10,5%/năm`, dòng tiền ròng hàng năm trước trả gốc (`Tiền thuê ròng − Tiền lãi vay`) âm hay dương bao nhiêu triệu VND?
6. **Tính hệ số `DSCR` của dự án bất động sản:** Dự án nhà xưởng cho thuê có doanh thu tiền mặt `150 tỷ VND/năm`, chi phí vận hành bằng tiền `35 tỷ VND/năm`, trả lãi vay `55 tỷ VND` và trả gốc đến hạn `40 tỷ VND`. Tính `NOI` và `DSCR`.
7. **Stress test `DSCR`:** Cùng dự án ở Bài tập 6 (`Dư nợ 550 tỷ VND`, lãi suất `10,0%/năm` tương ứng lãi `55 tỷ`, gốc đến hạn `40 tỷ`), nếu sang năm tới `NOI` giảm `20%` và lãi vay thả nổi tăng thêm `+2,0 điểm phần trăm/năm` (lên `12,0%/năm`), hệ số `DSCR` mới là bao nhiêu?
8. **Sai số Loại I và Loại II của chỉ báo cảnh báo sớm:** Theo [BIS (2018)](https://www.bis.org/publications/qr-201803/early-warning-indicators-banking-crises-expanding-family), nếu hạ ngưỡng cảnh báo của `Credit-to-GDP gap` xuống rất thấp để không bỏ sót khủng hoảng, loại sai số nào sẽ tăng lên và ảnh hưởng gì tới phân bổ vốn?
9. **Đọc xuyên qua tỷ lệ nợ xấu khi lãi dự thu tăng vọt:** Ngân hàng Y báo cáo `NPL` bất động sản giữ ở `1,8%`, nhưng khoản mục **"Các khoản lãi và phí phải thu"** tăng `65%` trong năm khi dư nợ chỉ tăng `12%` ([bank.py](../practice/models/bank.py)). Hiện tượng này cảnh báo điều gì?
10. **Đối chiếu chất lượng dòng tiền chủ đầu tư qua [earnings_quality.py](../practice/models/earnings_quality.py):** Chủ đầu tư Z báo lãi sau thuế `+1.200 tỷ VND` nhờ bán buôn dự án cho công ty liên kết, nhưng `CFO` âm `-2.800 tỷ VND` và phải thu ngắn hạn tăng `+3.500 tỷ VND`. Tính `CFO / LNST` và giải thích vì sao lợi nhuận này không dùng để trả gốc trái phiếu đến hạn được.

---

## Đáp án

1. **Tỷ lệ `LTV`:**
   - `PHÉP_TÍNH` `LTV` ban đầu: `260 / 400 = 65,00%`. Giá trị đất mới sau giảm `25%`: `400 × 0,75 = 300 tỷ VND` → `LTV` mới: `260 / 300 ≈ 86,67%`.
2. **Giá trị thu hồi hiện tại ròng (`Net Present Recovery`):**
   - `PHÉP_TÍNH` Tiền thu ròng danh nghĩa sau 2 năm: `300 × (1 − 30%) − 10 = 200,00 tỷ VND`.
   - `PHÉP_TÍNH` Giá trị hiện tại (`r = 10%`, `t = 2`): `200 / 1,10^2 = 200 / 1,21 ≈ 165,29 tỷ VND`. Thiếu hụt so với dư nợ gốc `180 tỷ`: `165,29 − 180,00 = −14,71 tỷ VND` (và mất thêm `20 tỷ` lãi treo).
3. **Chi phí trả nợ sau ưu đãi:**
   - `PHÉP_TÍNH` Lãi năm đầu sau ưu đãi: `4.000 × 11,0% = 440 triệu VND`. Cộng gốc `200 triệu VND` = `640 triệu VND/năm`, tương đương `640 / 12 ≈ 53,33 triệu VND/tháng`.
4. **Tỷ số `DSTI`:**
   - `PHÉP_TÍNH` `DSTI = 53,33 / 45,00 ≈ 118,52%` (vượt `100%` thu nhập khả dụng của gia đình).
5. **Lợi suất cho thuê vs Lãi vay (`Negative Carry`):**
   - `PHÉP_TÍNH` Lợi suất thuê ròng: `480 / 20.000 = 2,40%/năm`. Tiền lãi vay: `10.000 × 10,5% = 1.050 triệu VND/năm`. Dòng tiền ròng trước trả gốc: `480 − 1.050 = −570 triệu VND/năm`.
6. **Hệ số `DSCR` cơ sở:**
   - `PHÉP_TÍNH` `NOI = 150 − 35 = 115,00 tỷ VND`. Tổng nghĩa vụ trả nợ = `55 + 40 = 95,00 tỷ VND` → `DSCR = 115 / 95 ≈ 1,21 lần`.
7. **Stress test `DSCR`:**
   - `PHÉP_TÍNH` `NOI` mới: `115 × 0,80 = 92,00 tỷ VND`. Lãi vay mới: `550 × 12,0% = 66,00 tỷ VND` → Nghĩa vụ nợ mới: `66 + 40 = 106,00 tỷ VND` → `DSCR` mới = `92 / 106 ≈ 0,87 lần` (`< 1,0x`).
8. **Sai số Loại I và Loại II:**
   - `SUY_LUẬN` Hạ ngưỡng cảnh báo xuống quá thấp làm tăng mạnh **báo động giả (`Type I error`)**, khiến nhà đầu tư đứng ngoài thị trường quá sớm trong nhiều năm bình thường.
9. **Lãi dự thu tăng vọt:**
   - `SUY_LUẬN` Cho thấy khách hàng vay không trả được lãi bằng tiền mặt đúng hạn nhưng khoản vay vẫn được giữ ở Nhóm 1 nhờ ân hạn/cơ cấu nợ; báo hiệu chất lượng tài sản suy giảm trước khi `NPL` kịp tăng.
10. **Chất lượng dòng tiền chủ đầu tư:**
    - `PHÉP_TÍNH` `CFO / LNST = −2.800 / 1.200 ≈ −2,33 lần`.
    - `SUY_LUẬN` Lợi nhuận `+1.200 tỷ` nằm ở khoản phải thu (`+3.500 tỷ`), không phải tiền mặt nên không thể dùng trả gốc trái phiếu đến hạn.

---

## Bài làm với dữ liệu thiếu hoặc lệch

Khi phân tích chu kỳ tín dụng – bất động sản tại Việt Nam, bạn thường gặp hai khoảng trống dữ liệu:
1. **Giá chào bán sơ cấp khác xa giá giao dịch thực thu bằng tiền mặt:** Chủ đầu tư chào giá `80 triệu VND/m2` kèm gói hỗ trợ lãi suất 24 tháng và quà tặng, nhưng chiết khấu `18%` nếu thanh toán sớm bằng tiền mặt.
2. **Nợ ẩn ngoài dư nợ tín dụng ngân hàng:** Trái phiếu phát hành riêng lẻ và hợp đồng hợp tác đầu tư (`BCC`) có cam kết lợi nhuận cố định.

**Quy trình xử lý chuẩn Bậc S:**
- **Bước 1 — Tính giá hiệu dụng ròng (`Net Effective Price`):** Lấy giá chào sơ cấp trừ tỷ lệ chiết khấu thanh toán sớm (`80 × (1 − 18%) = 65,6 triệu VND/m2`) để biết giá trị thực của tài sản thế chấp.
- **Bước 2 — Kiểm chứng chéo 3 dòng trên BCTC qua [earnings_quality.py](../practice/models/earnings_quality.py):** Kiểm tra đồng thời `Tiền mặt`, `Người mua trả tiền trước ngắn hạn` và `CFO` thay vì tin vào tin đồn tỷ lệ hấp thụ.
- **Bước 3 — Cộng toàn bộ nghĩa vụ nợ ẩn vào mẫu số `DSCR`:** Đưa trái phiếu đến hạn và cam kết `BCC` vào nghĩa vụ trả nợ; gắn nhãn `CHƯA_BIẾT` nếu thiếu kỳ hạn chi tiết.

---

## Sai ở đâu

### Sai lầm 1: Tin rằng "Tài sản thế chấp là đất có sổ đỏ với LTV 60% thì ngân hàng không bao giờ mất vốn"
- **Bối cảnh:** Nhà đầu tư tin rằng dù chủ đầu tư dự án nghỉ dưỡng vỡ nợ, ngân hàng bán đất thế chấp (`LTV = 60%`) vẫn thu hồi đủ 100% gốc và lãi.
- **Sai ở đâu:** Nhầm giá thẩm định lúc đỉnh chu kỳ với **giá trị hiện tại của dòng tiền thu hồi khi phát mại (`Net Present Recovery`)** sau khi trừ chiết khấu thanh khoản (`30%–50%`) và `2–4 năm` chờ xử lý pháp lý.
- **Cách sửa:** Luôn đặt `DSCR` làm tuyến phòng thủ số 1 và áp chiết khấu thời gian + thanh khoản khi tính thu hồi tài sản thế chấp.

### Sai lầm 2: Dùng chỉ báo `Credit-to-GDP` cao để ấn định ngày sụp đổ của thị trường chứng khoán
- **Bối cảnh:** Thấy tín dụng/GDP cao liền tuyên bố thị trường chắc chắn sụp đổ ngay trong quý tới.
- **Sai ở đâu:** Biến **chỉ báo mức độ nhạy cảm cấu trúc (`vulnerability indicator`)** thành công cụ bấm giờ thị trườngngắn hạn, trái với cảnh báo của [BIS (2018)](https://www.bis.org/publications/qr-201803/early-warning-indicators-banking-crises-expanding-family).
- **Cách sửa:** Dùng chỉ báo để nâng tiêu chuẩn lọc bảng cân đối kế toán (tránh doanh nghiệp `DSCR < 1,0x`) thay vì đoán ngày giờ khủng hoảng.

### Sai lầm 3: Nhầm sức cầu đầu cơ nhờ gói "ân hạn gốc và lãi 0% trong 24 tháng" với sức mua ở thực bền vững
- **Bối cảnh:** Thấy dự án vùng ven bán nhanh nhờ chỉ cần đóng `15%` vốn tự có và ân hạn 24 tháng, người viết kết luận cầu ở thực rất khỏe.
- **Sai ở đâu:** Không nhận ra rủi ro thanh toán bị dồn nén toàn bộ sang tháng thứ 25 khi lãi suất thả nổi kích hoạt và `DSTI` vượt ngưỡng chịu đựng.
- **Cách sửa:** Tính lại `DSTI` của người mua tại thời điểm hết thời gian ân hạn.

---

## Kiểm tra chuyển bài

Trước khi chuyển sang bài [M3 — Dòng vốn, thương mại và địa chính trị](M3-capital-trade-geopolitics.md), hãy trả lời 3 câu hỏi dưới đây:

1. **Kết nối `M1` và `M2`:** Chuỗi truyền dẫn từ "tín dụng tăng nhanh hơn huy động (`M1`)" sang "tái định giá lãi vay thả nổi làm giảm `DSCR` của dự án bất động sản (`M2`)" diễn ra như thế nào?
2. **Kết nối `M2` với [F3](F3-vietnam-property-developers.md) và [F4](F4-vietnam-bank-analysis.md):** Khi chủ đầu tư gặp khó khăn thanh khoản, 2 khoản mục nào trên BCTC chủ đầu tư và 2 khoản mục nào trên BCTC ngân hàng cho vay sẽ phát tín hiệu sớm nhất?
3. **Chuẩn bị cho bài [M3](M3-capital-trade-geopolitics.md):** Vì sao dòng tiền của bất động sản khu công nghiệp lại gắn với **vốn FDI thực hiện và thương mại toàn cầu (`M3`)** nhiều hơn chu kỳ đất nền dân cư?

---

## Nguồn Internet đã mở

- Truy cập `2026-10-27` và kiểm tra đối chiếu `2026-11-05`:
  1. [World Bank — Viet Nam Economic Update (05/2026)](https://documents1.worldbank.org/curated/en/099740005122628080/pdf/IDU-2ee874ce-e0c0-462b-9571-99e553ef83c9.pdf) — phân tích tín dụng bất động sản, khả năng chi trả nhà ở và chất lượng tài sản ngân hàng Việt Nam.
  2. [BIS Quarterly Review — Early warning indicators for banking crises: expanding the family (03/2018)](https://www.bis.org/publications/qr-201803/early-warning-indicators-banking-crises-expanding-family) — khung định lượng và giới hạn của `Credit-to-GDP gap` và `Debt Service Ratio (DSR)`.
  3. [Cục Thống kê — Báo cáo tình hình kinh tế - xã hội Quý III và 9 tháng năm 2026](https://www.nso.gov.vn/bai-top/2026/10/bao-cao-tinh-hinh-kinh-te-xa-hoi-quy-iii-va-9-thang-nam-2026/) — số liệu tín dụng (`10,89%`) và huy động vốn (`9,78%`) đến ngày `28/09/2026`.
- Các ví dụ tính toán của Công ty Delta và bài tập định lượng được gắn nhãn `KỊCH_BẢN`.
