# Bài M1 — Tiền tệ, lãi suất, tỷ giá và tín dụng Việt Nam

- Ngày: `2026-11-05`
- Chốt dữ liệu lúc: `2026-11-05 12:30 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Đọc đúng kỳ hạn, mẫu số và phạm vi của dữ liệu tín dụng – huy động – lãi suất – tỷ giá; phân tách cơ chế truyền dẫn từ công cụ của Ngân hàng Nhà nước (NHNN) sang thanh khoản liên ngân hàng, chi phí vốn huy động (`COF`), lãi vay doanh nghiệp và báo cáo tài chính thực tế.
- Bài trước liên quan: [008](008-macro-transmission.md), [N7](N7-data-probability-uncertainty.md), [A5](A5-international-investing-currency-tax.md), [F4](F4-vietnam-bank-analysis.md).
- Thời lượng: Ba phiên học có điểm dừng (mỗi phiên 45 phút) + thực hành trên mô hình [Bài F4](F4-vietnam-bank-analysis.md) và [insurance.py](../practice/models/insurance.py).
- Câu hỏi cốt lõi: **Khi đọc bản tin về lãi suất điều hành, tỷ giá hay tăng trưởng tín dụng, những mắt xích truyền dẫn nào phải xảy ra trước khi con số đó chạm tới dòng tiền và lợi nhuận của một doanh nghiệp cụ thể?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/M1-fact-check.md), [phản biện](../reviews/M1-risk-review.md).

---

## Hiểu bài trong một phút

Ngân hàng trung ương không ấn định trực tiếp lợi nhuận của từng công ty trên sàn chứng khoán. Tại Việt Nam, Ngân hàng Nhà nước (NHNN) điều tiết điều kiện tiền tệ qua bộ công cụ gồm lãi suất điều hành (tái cấp vốn, tái chiết khấu, trần lãi suất tiền gửi dưới 6 tháng), nghiệp vụ thị trường mở (`OMO`), giao dịch ngoại hối (tỷ giá trung tâm, biên độ giao dịch, hoán đổi ngoại tệ `FX swap`) và định hướng tăng trưởng tín dụng. Tuy nhiên, từ quyết định chính sách đến báo cáo kết quả kinh doanh của doanh nghiệp có ít nhất bốn lớp đệm: (1) thanh khoản hệ thống ngân hàng và chênh lệch tín dụng – huy động, (2) kỳ hạn tái định giá của hợp đồng vay (`repricing lag`), (3) cấu trúc thu – chi ngoại tệ tự nhiên (`natural hedge`) hoặc hợp đồng phòng hộ (`hedging`), và (4) khả năng chuyển chi phí vốn/tỷ giá tăng thêm sang giá bán. Một con số tăng trưởng tín dụng hay biến động tỷ giá đơn lẻ không bao giờ tự chứng minh quan hệ nhân quả hay dự báo giá cổ phiếu nếu chưa mở từng lớp đệm này.

---

## Ôn bài cũ

- Trong [Bài N4 — Giá trị thời gian của tiền, lạm phát và lợi suất](N4-time-value-returns.md) và [Bài 012 — Kịch bản và biên an toàn](012-scenarios-margin-of-safety.md), ta đã thấy lãi suất chi phối tỷ suất chiết khấu. Bài M1 mở đầu **Tầng M (Vĩ mô & Chu kỳ)** bằng cơ chế truyền dẫn chính sách tiền tệ, lãi suất, tỷ giá và tín dụng.

---

## Phiên 1 — Cơ chế truyền dẫn tiền tệ, lãi suất và cách đọc dữ liệu tín dụng đúng kỳ

### 1.1. Bốn tầng lãi suất trong nền kinh tế Việt Nam

Người mới học vĩ mô thường gộp chung "lãi suất" thành một con số duy nhất. Thực tế, khi phân tích tác động của chính sách tiền tệ lên doanh nghiệp và định chế tài chính (ngân hàng, bảo hiểm), bạn phải tách bạch bốn tầng lãi suất có chức năng và tốc độ phản ứng hoàn toàn khác nhau:

`SỰ_THẬT` Báo cáo thường niên [BIS — Monetary and fiscal policy: safeguarding stability and trust (2023)](https://www.bis.org/publications/aer-2023/monetary-fiscal-policy-safeguarding-stability-trust) mô tả cơ chế truyền dẫn chính sách tiền tệ chuẩn mực đi từ công cụ của ngân hàng trung ương qua thị trường tiền tệ ngắn hạn, cấu trúc kỳ hạn lợi suất, chi phí vay mượn của khu vực tư nhân, giá tài sản và tỷ giá hối đoái. Tại Việt Nam, cơ chế này vận hành qua hệ thống trung gian ngân hàng (`bank-based system`):

| Tầng lãi suất | Đại diện tiêu biểu tại Việt Nam | Ai giao dịch với ai? | Tốc độ biến động và ý nghĩa phân tích |
|---|---|---|---|
| **1. Lãi suất điều hành (`Policy rates`)** | Lãi suất tái cấp vốn, tái chiết khấu, trần lãi suất tiền gửi VND dưới 6 tháng | NHNN quy định hoặc giao dịch với các tổ chức tín dụng (TCTD) | Thay đổi theo quyết định hành chính của NHNN; đóng vai trò "neo kỳ vọng" và giới hạn biên độ chi phí vốn ngắn hạn. |
| **2. Lãi suất thị trường 2 (`Interbank & OMO`)** | Lãi suất liên ngân hàng VND qua đêm (`ON`), 1 tuần (`1W`); lãi suất `OMO` và tín phiếu NHNN (`SBV bills`) | NHNN với các ngân hàng thương mại (NHTM), và các NHTM vay mượn lẫn nhau | Biến động hàng ngày; phản ánh tức thời trạng thái thanh khoản VND và áp lực tỷ giá, nhưng **không phải** lãi vay của doanh nghiệp sản xuất. |
| **3. Lãi suất huy động thị trường 1 (`Deposit rates`)** | Lãi suất tiết kiệm kỳ hạn 1–36 tháng, chứng chỉ tiền gửi (`CD`) của dân cư và tổ chức | Các NHTM huy động vốn từ người dân và doanh nghiệp | Thay đổi theo cung – cầu vốn thực tế và `LDR`; quyết định trực tiếp chi phí vốn đầu vào (`COF`) của ngân hàng và lợi suất tiền gửi của công ty bảo hiểm ([F8](F8-vietnam-insurance-analysis.md)). |
| **4. Lãi suất cho vay thị trường 1 (`Lending rates`)** | Lãi vay vốn lưu động ngắn hạn (3–6 tháng) và lãi vay trung dài hạn (máy móc, dự án) | NHTM cho doanh nghiệp và hộ gia đình vay | Bằng lãi suất cơ sở/huy động cộng biên độ rủi ro (`credit spread`). Phản ứng có độ trễ 3–12 tháng tùy chu kỳ tái định giá (`repricing schedule`) trong hợp đồng. |

`SUY_LUẬN` Khi đọc tin "lãi suất liên ngân hàng qua đêm tăng từ 2%/năm lên 5%/năm trong tuần", điều đó cho biết thanh khoản ngắn hạn trên thị trường 2 đang căng thẳng (do mùa quyết toán cuối quý, Kho bạc Nhà nước thu thuế, hoặc NHNN phát hành tín phiếu nâng lãi suất VND thị trường 2 nhằm thu hẹp chênh lệch lãi suất VND–USD). Nó **chưa làm tăng ngay** chi phí lãi vay của công ty sản xuất nếu lãi suất huy động kỳ hạn 6–12 tháng trên thị trường 1 vẫn giữ nguyên. Chỉ khi căng thẳng kéo dài khiến các NHTM nâng biểu lãi suất huy động dân cư kỳ hạn 12 tháng, chi phí vốn đầu vào (`COF`) mới tăng lên và truyền sang lãi vay doanh nghiệp ở kỳ tái định giá tiếp theo.

### 1.2. Đọc đúng kỳ hạn và mẫu số của dữ liệu tín dụng – huy động

Một sai lầm kinh điển khi đọc báo cáo vĩ mô là nhầm lẫn giữa **tăng trưởng so với cuối năm trước (`YTD` — Year-to-Date)**, **tăng trưởng so với cùng kỳ năm trước (`YoY` — Year-on-Year)** và **quy mô dư nợ trên GDP (`Credit-to-GDP`)**.

`SỰ_THẬT` Theo [Cục Thống kê — Báo cáo tình hình kinh tế - xã hội Quý III và 9 tháng năm 2026](https://www.nso.gov.vn/bai-top/2026/10/bao-cao-tinh-hinh-kinh-te-xa-hoi-quy-iii-va-9-thang-nam-2026/), tính đến thời điểm `28/09/2026`, tăng trưởng tín dụng của nền kinh tế đạt `10,89%` và huy động vốn của các tổ chức tín dụng tăng `9,78%` so với cuối năm 2025.

Khi đưa hai con số `10,89%` và `9,78%` vào sổ nghiên cứu, cần kiểm tra 3 thuộc tính kỹ thuật:
1. **Gốc so sánh (`Base date`):** Mốc so sánh là `31/12/2025`, tức đây là mức tăng lũy kế gần 9 tháng đầu năm (`YTD`), **không phải** tốc độ tăng trưởng 12 tháng (`YoY`). Nếu quý IV năm trước tín dụng tăng mạnh, tốc độ 12 tháng (`YoY`) sẽ cao hơn đáng kể so với số `YTD`.
2. **Chênh lệch tốc độ tín dụng – huy động (`Credit–Deposit growth gap`):** Trong 9 tháng đầu năm 2026, tốc độ tăng tín dụng (`10,89%`) vượt tốc độ tăng huy động vốn (`9,78%`) là:
   $$\text{Chênh lệch tốc độ tăng (YTD)} = 10{,}89\% - 9{,}78\% = +1{,}11\text{ điểm phần trăm}$$
   `SUY_LUẬN` Khi tín dụng tăng nhanh hơn huy động, bộ đệm thanh khoản thu hẹp (tỷ lệ `LDR` nhích lên), thúc đẩy ngân hàng phát hành thêm giấy tờ có giá hoặc nâng lãi suất tiền gửi trung hạn để hút vốn.
3. **Cường độ và chất lượng phân bổ tín dụng:** Khi tỷ lệ tín dụng/GDP ở vùng cao (trên `130%–140%` GDP), mỗi `10%` tăng trưởng tín dụng tương đương lượng vốn vay mới bằng `13%–14%` GDP bơm vào nền kinh tế. Tuy nhiên, con số tổng hợp không tự nói lên tiền vay chảy vào sản xuất xuất khẩu hay đảo nợ tài sản.

### 1.3. Phép tính độ nhạy lãi suất thả nổi và độ trễ tái định giá (`Repricing lag`)

Để định lượng tác động lãi suất lên doanh nghiệp, bạn phải tách cấu trúc nợ thành: (a) nợ lãi suất cố định, (b) nợ vay ngắn hạn quay vòng, và (c) nợ trung dài hạn thả nổi theo mốc tái định giá.

`KỊCH_BẢN` Doanh nghiệp công nghiệp Alpha có tổng dư nợ vay tại ngày `01/01` là `1.200 tỷ VND` giữ nguyên trong năm, gồm:
- **Khoản A (Nợ dài hạn cố định):** `300 tỷ VND`, lãi suất cố định `8,0%/năm` trong 3 năm.
- **Khoản B (Nợ vốn lưu động quay vòng 3 tháng/lần):** `400 tỷ VND`, lãi suất đầu năm `6,5%/năm`.
- **Khoản C (Nợ trung hạn thả nổi):** `500 tỷ VND`, tái định giá định kỳ vào ngày `01/07` hàng năm.

Giả sử ngày `01/04` (đầu Quý II), mặt bằng lãi suất tham chiếu và lãi vay ngắn hạn đồng loạt tăng thêm `+1,5 điểm phần trăm/năm` (`+150 bps`) và giữ nguyên đến hết năm.

`PHÉP_TÍNH` Chi phí lãi vay tăng thêm (`Incremental interest expense`) trong năm hiện hành:
1. **Khoản A (`300 tỷ` cố định):** Không đổi (`0 tỷ VND`).
2. **Khoản B (`400 tỷ` quay vòng từ `01/04`, chịu lãi mới trong 9 tháng cuối năm = `9/12` năm):**
   $$\Delta \text{Lãi Khoản B} = 400 \times 1{,}5\% \times \frac{9}{12} = 4{,}50\text{ tỷ VND}$$
3. **Khoản C (`500 tỷ` thả nổi, tái định giá từ `01/07`, chịu lãi mới trong 6 tháng cuối năm = `6/12` năm):**
   $$\Delta \text{Lãi Khoản C} = 500 \times 1{,}5\% \times \frac{6}{12} = 3{,}75\text{ tỷ VND}$$
4. **Tổng chi phí lãi vay tăng thêm năm nay:** `0 + 4,50 + 3,75 = 8,25 tỷ VND` (thấp hơn nhiều so với phép nhân ngây thơ `1.200 × 1,5% = 18,00 tỷ VND`). Sang năm kế tiếp (khi Khoản B và C chịu đủ 12 tháng lãi mới), mức tăng cả năm mới đạt `(400 + 500) × 1,5% = 13,50 tỷ VND/năm`.

`SUY_LUẬN` Đây là lý do lợi nhuận của doanh nghiệp thâm dụng vốn thường chưa giảm ngay trong quý đầu tiên lãi suất nhích tăng, nhưng lại bị bào mòn mạnh vào 2–4 quý sau đó. Bạn có thể dùng [Bài F4](F4-vietnam-bank-analysis.md) để kiểm chứng mặt đối ứng của quá trình tái định giá này trên bảng cân đối của ngân hàng.

> **Điểm dừng phiên 1:** Mở thuyết minh "Vay và nợ thuê tài chính" của một doanh nghiệp sản xuất hoặc đối chiếu với [Bài F4](F4-vietnam-bank-analysis.md), ghi lại tỷ trọng nợ ngắn hạn và cơ chế lãi suất cố định/thả nổi.

---

## Phiên 2 — Tỷ giá hối đoái, thanh khoản liên ngân hàng và bảng cân đối ngoại tệ doanh nghiệp

### 2.1. Quy ước yết giá tỷ giá và liên kết với lãi suất thị trường 2

Tại Việt Nam, tỷ giá thông dụng được yết theo `VND/USD` (số VND cần để đổi lấy 1 USD). Khi `VND/USD` tăng từ `25.000` lên `25.500`:
- Phần trăm tăng giá của USD tính bằng VND là: $(25.500 - 25.000) / 25.000 = +2{,}00\%$.
- Phần trăm giảm giá của VND tính theo USD là: $(1/25.500 - 1/25.000) / (1/25.000) = -500 / 25.500 \approx -1{,}96\%$.

`SUY_LUẬN` Khi lãi suất USD quốc tế ở mức cao trong khi lãi suất VND qua đêm liên ngân hàng rơi xuống quá thấp, chênh lệch lãi suất `VND − USD` âm sâu sẽ khuyến khích nắm giữ USD ngắn hạn. Để giảm áp lực lên tỷ giá và dự trữ ngoại hối, NHNN có thể phát hành tín phiếu hoặc điều tiết `OMO` / `FX swap` để nâng lãi suất VND trên thị trường 2. Hiểu điều này giúp bạn không đánh đồng mọi nhịp điều tiết thanh khoản thị trường 2 với việc thắt chặt tiền tệ toàn diện trên thị trường 1, nhưng cũng nhận thức rõ giới hạn nới lỏng nếu áp lực tỷ giá kéo dài.

### 2.2. Hai kênh tác động của tỷ giá lên báo cáo tài chính doanh nghiệp

Tác động của tỷ giá đi vào báo cáo tài chính qua **hai kênh độc lập** cần tính riêng:
1. **Kênh dòng tiền hoạt động ròng (`Operating FX exposure`):**
   $$\text{Dòng ngoại tệ hoạt động ròng (USD)} = \text{Doanh thu USD} - \text{Chi phí hoạt động USD}$$
2. **Kênh đánh giá lại khoản mục tiền tệ có gốc ngoại tệ cuối kỳ (`Balance-sheet translation exposure`):**
   Theo Chuẩn mực kế toán Việt Nam (VAS 10 và Thông tư 200/2014/TT-BTC), tại ngày khóa sổ, doanh nghiệp phải đánh giá lại các khoản mục tiền tệ có gốc ngoại tệ (đặc biệt là **dư nợ vay bằng ngoại tệ**) theo tỷ giá cuối kỳ. Khoản lỗ chênh lệch tỷ giá đánh giá lại nợ gốc USD cuối kỳ phải hạch toán ngay vào **Chi phí tài chính** trên Báo cáo kết quả kinh doanh dù nợ gốc chưa đến hạn trả bằng tiền mặt!

`KỊCH_BẢN` Công ty Dệt may Beta trong năm có:
- **Doanh thu xuất khẩu bằng USD:** `80 triệu USD/năm`.
- **Chi phí nhập khẩu bông, sợi, hóa chất bằng USD:** `55 triệu USD/năm`.
- **Dư nợ vay dài hạn bằng USD (chưa đến hạn trả gốc):** `60 triệu USD`, lãi suất cố định `5,5%/năm` trả cuối năm.
- **Hợp đồng kỳ hạn (`FX Forward`):** Đã chốt bán kỳ hạn `10 triệu USD` ở tỷ giá `25.000 VND/USD`.
- **Biến động tỷ giá:** Tỷ giá đầu năm `25.000 VND/USD`; tỷ giá bình quân và cuối năm cùng tăng `+3,0%` lên `25.750 VND/USD` (`+750 VND/USD`). Sản lượng, giá bán USD và chi phí VND giữ nguyên.

`PHÉP_TÍNH` Tác động của mức tăng tỷ giá `+750 VND/USD`:
1. **Dòng ngoại tệ hoạt động ròng trước lãi vay:** `80 − 55 = +25,00 triệu USD`.
2. **Trừ lãi vay USD trả trong năm (`60 × 5,5% = 3,30 triệu USD`):** Dòng tiền USD ròng trước phòng hộ = `25,00 − 3,30 = +21,70 triệu USD`.
3. **Trừ phần đã chốt Forward (`10,00 triệu USD`):** Dòng tiền USD ròng hưởng lợi tỷ giá mới = `21,70 − 10,00 = +11,70 triệu USD`.
   $$\Delta \text{Dòng tiền thuần bằng VND trong năm} = +11{,}70\text{ triệu USD} \times 750 = +8{,}775\text{ tỷ VND}$$
4. **Bút toán đánh giá lại gốc nợ vay dài hạn `60 triệu USD` cuối năm (lỗ tỷ giá chưa thực hiện):**
   $$\Delta \text{Lỗ tỷ giá đánh giá lại nợ gốc} = -60\text{ triệu USD} \times 750 = -45{,}000\text{ tỷ VND}$$
5. **Tổng tác động ròng lên Lợi nhuận trước thuế (`EBT`) kế toán:**
   $$\Delta \text{EBT} = +8{,}775 - 45{,}000 = -36{,}225\text{ tỷ VND}$$

`SUY_LUẬN` Dù Beta là doanh nghiệp xuất khẩu ròng và **dòng tiền mặt thực tế tăng thêm `+8,775 tỷ VND`**, nhưng **lợi nhuận kế toán trước thuế (`EBT`) lại giảm `-36,225 tỷ VND`** do đánh giá lại nợ gốc USD dài hạn. Hơn nữa, nếu khách hàng nước ngoài ép giảm giá bán USD đi `1%–2%` khi thấy VND giảm giá, phần lợi ích dòng tiền hoạt động cũng sẽ thu hẹp.

> **Điểm dừng phiên 2:** Hãy tự tính lại `ΔEBT` của Công ty Beta nếu công ty vay hoàn toàn bằng VND thay vì vay `60 triệu USD`.

---

## Phiên 3 — Ma trận theo dõi vĩ mô và kết nối sang mô hình Ngân hàng – Bảo hiểm

| Biến số theo dõi | Câu hỏi bắt buộc về định nghĩa & kỳ đo | Nguồn gốc cần mở | Tác động có điều kiện lên Ngân hàng & Bảo hiểm | Điều chưa biết cần gắn nhãn `CHƯA_BIẾT` |
|---|---|---|---|---|
| **Tăng trưởng tín dụng** | Đo theo `YTD` (so cuối năm trước) hay `YoY` (so cùng kỳ 12 tháng)? | [Cục Thống kê](https://www.nso.gov.vn/bai-top/2026/10/bao-cao-tinh-hinh-kinh-te-xa-hoi-quy-iii-va-9-thang-nam-2026/), NHNN | Mở rộng tài sản sinh lời của ngân hàng ([Bài F4](F4-vietnam-bank-analysis.md)), nhưng nếu vượt xa huy động sẽ đẩy `LDR` và `COF` tăng. | Cơ cấu tín dụng theo ngành và tỷ lệ nợ cơ cấu lại nếu nguồn chỉ công bố số tổng. |
| **Tăng trưởng huy động vốn** | Có gồm giấy tờ có giá không? Biến động tỷ lệ `CASA` ra sao? | Cục Thống kê, NHNN, BCTC ngân hàng | Quyết định chi phí vốn đầu vào (`COF`) ngân hàng và lợi suất tiền gửi của công ty bảo hiểm ([insurance.py](../practice/models/insurance.py)). | Độ bền vững của tiền gửi tổ chức vào tuần cuối quý. |
| **Lãi suất điều hành & Thị trường 2** | Lãi suất tái cấp vốn, `OMO` hay qua đêm liên ngân hàng (`ON`)? | Thông cáo NHNN | Phản ánh chi phí thanh khoản ngắn hạn thị trường 2; chưa đồng nhất với lãi vay thị trường 1. | Độ trễ truyền dẫn thực tế sang biểu lãi suất tiết kiệm dân cư kỳ hạn 6–12 tháng. |
| **Lợi suất trái phiếu Chính phủ** | Kỳ hạn mấy năm (5Y, 10Y)? Sơ cấp hay thứ cấp? | HNX, Kho bạc Nhà nước | Neo lãi suất phi rủi ro (`R_f`) và quyết định lãi suất chiết khấu dự phòng toán học bảo hiểm nhân thọ. | Lượng cầu tái đầu tư thực tế trong các phiên đấu thầu tới. |
| **Tỷ giá hối đoái (`FX`)** | Tỷ giá trung tâm, tỷ giá mua/bán NHTM hay tỷ giá hạch toán cuối kỳ? | NHNN, biểu tỷ giá NHTM | Tác động hai chiều lên dòng tiền xuất nhập khẩu ròng và đánh giá lại nợ gốc ngoại tệ cuối kỳ. | Khối lượng hợp đồng kỳ hạn ngoại tệ (`FX forward/swap`) ngoại bảng nếu không thuyết minh. |

> **Điểm dừng phiên 3:** Tóm tắt vì sao cùng một đợt tăng lãi suất tiền gửi `+1,0%/năm` lại làm **tăng** thu nhập tài chính của công ty bảo hiểm phi nhân thọ nhiều tiền mặt ([insurance.py](../practice/models/insurance.py)), nhưng làm **giảm** lợi nhuận của doanh nghiệp sản xuất vay nợ thả nổi cao.

---

## Ví dụ từ nguồn thật

1. **Dữ liệu tín dụng và huy động vốn 9 tháng năm 2026 tại Việt Nam:**
   `SỰ_THẬT` Mở trực tiếp [Cục Thống kê — Báo cáo tình hình kinh tế - xã hội Quý III và 9 tháng năm 2026](https://www.nso.gov.vn/bai-top/2026/10/bao-cao-tinh-hinh-kinh-te-xa-hoi-quy-iii-va-9-thang-nam-2026/) (tháng 10/2026): Tính đến `28/09/2026`, tổng phương tiện thanh toán tăng `9,31%` so với cuối năm 2025; huy động vốn của các tổ chức tín dụng tăng `9,78%`; tăng trưởng tín dụng của nền kinh tế đạt `10,89%`. Khoảng cách `+1,11 điểm phần trăm` giữa tăng trưởng tín dụng (`10,89%`) và huy động (`9,78%`) là dữ kiện thực chứng cho thấy nhu cầu vốn tín dụng mở rộng nhanh hơn tốc độ tích lũy tiền gửi trong 9 tháng đầu năm 2026.
2. **Khung truyền dẫn chính sách tiền tệ quốc tế của BIS:**
   `SỰ_THẬT` Mở báo cáo [BIS — Annual Economic Report 2023: Monetary and fiscal policy: safeguarding stability and trust](https://www.bis.org/publications/aer-2023/monetary-fiscal-policy-safeguarding-stability-trust): BIS chỉ rõ hiệu lực truyền dẫn của lãi suất chính sách phụ thuộc chặt chẽ vào cấu trúc kỳ hạn nợ của khu vực tư nhân và tỷ số chi phí trả nợ (`debt service ratio`).

---

## Bài tập

Hãy tự giải 10 bài tập dưới đây trước khi mở phần Đáp án:

1. **Phân biệt điểm phần trăm và phần trăm thay đổi:** Lãi vay vốn lưu động tăng từ `6,0%/năm` lên `7,5%/năm`. Hỏi lãi suất đã tăng bao nhiêu **điểm phần trăm (`bps`)** và tăng bao nhiêu **phần trăm tương đối (`%`)** so với mức ban đầu?
2. **Đọc đúng kỳ dữ liệu tín dụng (`YTD` vs `YoY`):** Tại ngày `28/09/2026`, tín dụng nền kinh tế tăng `10,89%` so với `31/12/2025` ([Cục Thống kê](https://www.nso.gov.vn/bai-top/2026/10/bao-cao-tinh-hinh-kinh-te-xa-hoi-quy-iii-va-9-thang-nam-2026/)). Giả sử dư nợ tại `30/09/2025` là `100` đơn vị, trong Quý IV/2025 tín dụng tăng `5,0%` (lên `105` đơn vị tại `31/12/2025`). Hãy tính tốc độ tăng trưởng tín dụng 12 tháng (`YoY`) từ cuối tháng 9/2025 đến `28/09/2026` theo giả định này.
3. **Chênh lệch tăng trưởng tín dụng – huy động và `LDR`:** Một ngân hàng đầu năm có dư nợ cho vay `800.000 tỷ VND` và vốn huy động `1.000.000 tỷ VND` (`LDR` giản lược = `80,00%`). Sau 9 tháng, tín dụng tăng `10,89%` và huy động tăng `9,78%`. Hãy tính số dư cho vay mới, huy động mới và `LDR` giản lược cuối tháng 9.
4. **Tính chi phí lãi vay có độ trễ tái định giá (`Repricing lag`):** Công ty Gamma có tổng nợ vay `800 tỷ VND`, gồm `250 tỷ VND` trái phiếu cố định `8,5%/năm` và `550 tỷ VND` nợ vay ngân hàng thả nổi tái định giá vào ngày `01/05` và `01/11` hàng năm. Nếu lãi suất tham chiếu tăng thêm `+1,2 điểm phần trăm/năm` từ ngày `01/03` và giữ nguyên đến hết năm, chi phí lãi vay trong năm hiện hành (`01/01–31/12`) tăng thêm bao nhiêu tỷ VND?
5. **Quy đổi chiều tỷ giá `VND/USD` và `USD/VND`:** Tỷ giá đầu năm là `24.800 VND/USD`, cuối năm là `25.420 VND/USD`. Hãy tính: (a) mức thay đổi tuyệt đối, (b) phần trăm tăng giá của USD tính bằng VND, và (c) phần trăm giảm giá của VND tính bằng USD.
6. **Tác động tỷ giá lên nhà nhập khẩu có phòng hộ một phần:** Công ty nhập khẩu nhựa phải trả `15 triệu USD` trong quý tới, đã mua kỳ hạn (`FX Forward`) `6 triệu USD` ở tỷ giá `25.000 VND/USD`, phần `9 triệu USD` còn lại thả nổi. Nếu ngày thanh toán tỷ giá giao ngay lên `25.450 VND/USD`, tổng số tiền VND phải trả là bao nhiêu và tăng thêm bao nhiêu tỷ VND so với tỷ giá `25.000 VND/USD`?
7. **Tách dòng tiền hoạt động ngoại tệ và lỗ đánh giá lại nợ gốc:** Doanh nghiệp vận tải biển có doanh thu USD `40 triệu USD/năm`, chi phí vận hành USD `22 triệu USD/năm`, và nợ vay mua tàu bằng USD `50 triệu USD` (lãi suất `6,0%/năm` trả cuối năm, chưa đến hạn trả gốc). Nếu tỷ giá bình quân và cuối năm cùng tăng từ `25.000` lên `25.500 VND/USD` (`+500 VND/USD`), không phòng hộ, hãy tính: (a) biến động dòng tiền thuần bằng VND trong năm, và (b) biến động `EBT` kế toán sau khi đánh giá lại nợ gốc USD cuối năm.
8. **Độ nhạy giá bán USD khi tỷ giá tăng:** Doanh nghiệp xuất khẩu thủy sản thu `50 triệu USD/năm`, chi phí đầu vào mua trong nước bằng VND là `1.100 tỷ VND`. Khi tỷ giá tăng `+4,0%` từ `25.000` lên `26.000 VND/USD`, khách hàng nước ngoài yêu cầu giảm giá bán USD đi `3,0%` (sản lượng không đổi). Hỏi lợi nhuận gộp bằng VND thay đổi bao nhiêu tỷ VND?
9. **Hệ số khả năng trả lãi (`ICR`):** Doanh nghiệp có `EBIT` năm cơ sở `180 tỷ VND`, nợ vay thả nổi `1.500 tỷ VND` với lãi suất `8,0%/năm`. Sang năm bất lợi, `EBIT` giảm `15%` và lãi vay thả nổi tái định giá tăng thêm `+2,0 điểm phần trăm/năm` (lên `10,0%/năm`). Tính `ICR = EBIT / Chi phí lãi vay` ở năm cơ sở và năm bất lợi.
10. **Đối chiếu tác động bất đối xứng giữa Bảo hiểm và Doanh nghiệp vay nợ:** Khi lãi suất tiền gửi kỳ hạn 12 tháng tăng `+1,5 điểm phần trăm/năm`, vì sao một công ty bảo hiểm phi nhân thọ nắm giữ `8.000 tỷ VND` tiền gửi kỳ hạn 6–12 tháng và không vay nợ ([F8](F8-vietnam-insurance-analysis.md)) lại có hướng biến động lợi nhuận ngược hẳn với doanh nghiệp ở Bài tập 9?

---

## Đáp án

1. **Điểm phần trăm vs Phần trăm tương đối:**
   - `PHÉP_TÍNH` Tăng tuyệt đối: `7,5% − 6,0% = +1,5 điểm phần trăm/năm` (`+150 bps`).
   - `PHÉP_TÍNH` Tăng tương đối so với lãi suất gốc: `(7,5% − 6,0%) / 6,0% = +25,00%`.
2. **Tăng trưởng `YTD` vs `YoY`:**
   - `PHÉP_TÍNH` Chỉ số dư nợ tại `28/09/2026` (`30/09/2025 = 100`): `105 × (1 + 10,89%) = 116,4345`.
   - `PHÉP_TÍNH` Tăng trưởng 12 tháng (`YoY`): `(116,4345 − 100) / 100 = +16,43%`.
3. **Chênh lệch tín dụng – huy động và `LDR`:**
   - `PHÉP_TÍNH` Dư nợ mới: `800.000 × 1,1089 = 887.120 tỷ VND`. Huy động mới: `1.000.000 × 1,0978 = 1.097.800 tỷ VND`.
   - `PHÉP_TÍNH` `LDR` giản lược mới: `887.120 / 1.097.800 ≈ 80,81%` (tăng `+0,81 điểm phần trăm`).
4. **Chi phí lãi vay có độ trễ tái định giá (Công ty Gamma):**
   - `PHÉP_TÍNH` Trái phiếu cố định `250 tỷ`: tăng `0 tỷ`. Khoản thả nổi `550 tỷ` tái định giá từ `01/05` (chịu lãi mới 8 tháng cuối năm = `8/12` năm): `550 × 1,2% × (8/12) = 4,40 tỷ VND`.
5. **Quy đổi chiều tỷ giá:**
   - `PHÉP_TÍNH` (a) Thay đổi tuyệt đối: `25.420 − 24.800 = +620 VND/USD`. (b) USD tăng giá theo VND: `620 / 24.800 = +2,50%`. (c) VND giảm giá theo USD: `−620 / 25.420 ≈ −2,44%`.
6. **Nhà nhập khẩu có phòng hộ một phần:**
   - `PHÉP_TÍNH` Chi trả `6 triệu USD` Forward: `6 × 25.000 = 150,00 tỷ VND`. Chi trả `9 triệu USD` giao ngay: `9 × 25.450 = 229,05 tỷ VND`. Tổng chi: `379,05 tỷ VND` (tăng thêm `9 × 450 = +4,05 tỷ VND` so với tỷ giá `25.000`).
7. **Dòng tiền ngoại tệ vs Đánh giá lại nợ gốc:**
   - `PHÉP_TÍNH` Dòng USD hoạt động ròng trước lãi: `40 − 22 = +18,00 triệu USD`. Trừ lãi vay USD (`50 × 6% = 3,00 triệu USD`), dòng tiền USD ròng = `+15,00 triệu USD`.
   - `PHÉP_TÍNH` (a) Dòng tiền VND trong năm tăng: `+15,00 triệu × 500 = +7,50 tỷ VND`. (b) Lỗ đánh giá lại nợ gốc `50 triệu USD`: `−50 triệu × 500 = −25,00 tỷ VND` → `ΔEBT = +7,50 − 25,00 = −17,50 tỷ VND`.
8. **Độ nhạy giá bán USD khi tỷ giá tăng:**
   - `PHÉP_TÍNH` Lợi nhuận gộp ban đầu: `50 × 25.000 − 1.100 = 1.250 − 1.100 = 150,00 tỷ VND`.
   - `PHÉP_TÍNH` Doanh thu USD mới sau giảm giá `3%`: `50 × 0,97 = 48,50 triệu USD`. Quy đổi ở tỷ giá `26.000`: `48,50 × 26.000 = 1.261,00 tỷ VND`. Lợi nhuận gộp mới: `1.261 − 1.100 = 161,00 tỷ VND` (tăng `+11,00 tỷ VND`).
9. **Hệ số khả năng trả lãi (`ICR`):**
   - `PHÉP_TÍNH` Năm cơ sở: Lãi vay = `1.500 × 8,0% = 120 tỷ VND` → `ICR = 180 / 120 = 1,50 lần`.
   - `PHÉP_TÍNH` Năm bất lợi: `EBIT` mới = `180 × 0,85 = 153 tỷ VND`; Lãi vay mới = `1.500 × 10,0% = 150 tỷ VND` → `ICR = 153 / 150 = 1,02 lần`.
10. **Đối chiếu Bảo hiểm và Doanh nghiệp vay nợ:**
    - `SUY_LUẬN` Doanh nghiệp vay nợ thả nổi là người đi vay ròng (`net borrower`) nên lãi suất tăng làm tăng chi phí tài chính. Ngược lại, doanh nghiệp bảo hiểm phi nhân thọ là người gửi tiền ròng (`net depositor`) từ nguồn vốn nổi (`float`), nên khi `8.000 tỷ VND` tiền gửi tái tục ở lãi suất cao hơn `+1,5%/năm`, thu nhập tài chính tăng thêm khoảng `8.000 × 1,5% = +120 tỷ VND/năm`.

---

## Bài làm với dữ liệu thiếu hoặc lệch

Trong thực tế nghiên cứu tại Việt Nam, bạn thường gặp hai tình huống dữ liệu lệch hoặc khuyết:
1. **Khác biệt giữa tỷ giá trên báo chí và tỷ giá hạch toán trên Thuyết minh BCTC:** Báo chí dẫn tỷ giá trung tâm NHNN, còn doanh nghiệp quy đổi nợ ngoại tệ cuối kỳ theo tỷ giá bán chuyển khoản của ngân hàng thương mại nơi mở tài khoản (theo Thông tư 200/2014/TT-BTC).
2. **Doanh nghiệp không thuyết minh lịch tái định giá (`repricing schedule`) và tỷ lệ phòng hộ (`hedging ratio`):** BCTC quý thường chỉ liệt kê tổng dư nợ vay và số dư ngoại tệ cuối kỳ.

**Quy trình xử lý chuẩn Bậc S:**
- **Bước 1 — Ghi nhận tường minh `CHƯA_BIẾT`:** Không tự bịa "100% nợ đã phòng hộ". Ghi rõ: `CHƯA_BIẾT tỷ lệ phòng hộ kỳ hạn và lịch tái định giá chi tiết`.
- **Bước 2 — Ước lượng lãi suất hiệu dụng ẩn (`Implied Effective Interest Rate`):** Tính `Chi phí lãi vay trong kỳ / Dư nợ vay bình quân đầu – cuối kỳ`, lưu ý kiểm tra phần lãi vay vốn hóa vào xây dựng cơ bản dở dang.
- **Bước 3 — Lập ma trận độ nhạy 3 kịch bản (`Sensitivity Table`):** Tính `ΔEBT` theo 3 mức biến động lãi suất (`+50 bps`, `+100 bps`, `+200 bps`) và 3 tỷ lệ tái định giá giả định (`50%`, `75%`, `100%`).

---

## Sai ở đâu

### Sai lầm 1: Lấy lãi suất liên ngân hàng qua đêm làm lãi vay của doanh nghiệp sản xuất và bất động sản
- **Bối cảnh:** Thấy lãi suất VND qua đêm liên ngân hàng giảm từ `4,2%/năm` xuống `1,8%/năm` trong tuần, người viết kết luận doanh nghiệp sản xuất giảm ngay một nửa chi phí lãi vay.
- **Sai ở đâu:** Đánh đồng **lãi suất thị trường 2 (`Interbank rate`)** giữa các ngân hàng với **lãi vay thị trường 1 (`Customer lending rate`)** được định giá theo chi phí huy động dân cư kỳ hạn 6–12 tháng cộng biên độ rủi ro.
- **Cách sửa:** Kiểm tra biểu lãi suất huy động kỳ hạn 6–12 tháng thị trường 1 và thuyết minh lãi vay trên BCTC doanh nghiệp.

### Sai lầm 2: Kết luận doanh nghiệp xuất khẩu chắc chắn báo lãi lớn khi tỷ giá `VND/USD` tăng
- **Bối cảnh:** Thấy tỷ giá tăng `3,5%`, nhà đầu tư mua cổ phiếu công ty sợi xuất khẩu nhưng khi BCTC công bố, công ty lại báo lỗ nặng vì chi phí tài chính tăng vọt.
- **Sai ở đâu:** Bỏ qua tỷ trọng nhập khẩu bông bằng USD (`70%` giá vốn) và khoản lỗ tỷ giá đánh giá lại dư nợ vay USD dài hạn cuối quý.
- **Cách sửa:** Luôn tính đồng thời cả dòng tiền ngoại tệ hoạt động ròng và bút toán đánh giá lại nợ gốc ngoại tệ trên Bảng cân đối kế toán.

### Sai lầm 3: So sánh trực tiếp tăng trưởng tín dụng 9 tháng (`YTD`) với tăng trưởng cả năm (`12 tháng`)
- **Bối cảnh:** Lấy số tín dụng đến `28/09/2026` tăng `10,89%` ([Cục Thống kê](https://www.nso.gov.vn/bai-top/2026/10/bao-cao-tinh-hinh-kinh-te-xa-hoi-quy-iii-va-9-thang-nam-2026/)) so thẳng với số cả năm trước (`15%`) rồi kết luận tín dụng đang bị siết chặt.
- **Sai ở đâu:** So sánh hai kỳ đo có độ dài khác nhau (`9 tháng YTD` so với `12 tháng`), bỏ qua tính mùa vụ quý IV và tốc độ tăng huy động vốn (`9,78%`).
- **Cách sửa:** Quy về cùng hệ quy chiếu (`YTD` cùng kỳ hoặc `YoY` 12 tháng) và đặt cạnh tốc độ tăng huy động vốn.

---

## Kiểm tra chuyển bài

Trước khi chuyển sang bài [M2 — Chu kỳ tín dụng và bất động sản](M2-credit-real-estate-cycle.md), hãy trả lời 3 câu hỏi dưới đây:

1. **Chuyển giao sang Ngân hàng ([F4](F4-vietnam-bank-analysis.md)):** Khi tín dụng toàn hệ thống tăng `10,89%` nhưng huy động chỉ tăng `9,78%`, vì sao ngân hàng có tỷ lệ `CASA` cao lại bảo vệ được `NIM` tốt hơn ngân hàng phụ thuộc tiền gửi có kỳ hạn?
2. **Chuyển giao sang Bảo hiểm ([F8](F8-vietnam-insurance-analysis.md)):** Khi lãi suất tiền gửi 12 tháng và lợi suất trái phiếu Chính phủ 10 năm tăng `+100 bps`, hai chỉ tiêu nào trên BCTC công ty bảo hiểm sẽ phản ứng trực tiếp?
3. **Chuyển giao sang bài [M2](M2-credit-real-estate-cycle.md):** Khi lãi vay thả nổi tái định giá tăng `+2,0 điểm phần trăm/năm` sau thời gian ưu đãi, điều gì xảy ra đồng thời với dòng tiền trả nợ của người mua nhà và giá trị thanh lý của tài sản bảo đảm?

---

## Nguồn Internet đã mở

- Truy cập `2026-10-27` và kiểm tra đối chiếu `2026-11-05`:
  1. [Cục Thống kê — Báo cáo tình hình kinh tế - xã hội Quý III và 9 tháng năm 2026](https://www.nso.gov.vn/bai-top/2026/10/bao-cao-tinh-hinh-kinh-te-xa-hoi-quy-iii-va-9-thang-nam-2026/) — công bố tháng 10/2026; ghi nhận đến `28/09/2026` tăng trưởng tín dụng nền kinh tế đạt `10,89%`, huy động vốn tăng `9,78%` và tổng phương tiện thanh toán tăng `9,31%` so với cuối năm 2025.
  2. [BIS — Annual Economic Report 2023: Monetary and fiscal policy: safeguarding stability and trust](https://www.bis.org/publications/aer-2023/monetary-fiscal-policy-safeguarding-stability-trust) — xuất bản năm 2023; khung truyền dẫn chính sách tiền tệ, độ nhạy chi phí trả nợ và tương tác tiền tệ – tài khóa.
- Các kịch bản doanh nghiệp Alpha, Beta, Gamma được gắn nhãn `KỊCH_BẢN` để phục vụ rèn luyện tính toán.
