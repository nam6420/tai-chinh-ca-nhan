# Bài N2: Đọc từng dòng ba báo cáo tài chính

- Ngày cập nhật: `2026-11-06`
- Chốt dữ liệu lúc: `2026-11-06 10:10 UTC+7 (Asia/Ho_Chi_Minh)`
- Bậc chiều sâu: `Bậc S`
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Lộ trình đọc: **Bài 4 / 23 của Nhánh 1 (Hiểu doanh nghiệp & Phân tích cổ phiếu)**.
  - **Bài trước liên quan:** [Bài 001](001-business-financial-statements.md) (Bước 3/23), [Bài N6](N6-business-model-unit-economics.md) (Bước 2/23) và [Bài N1](N1-market-basics.md) (Bước 1/23).
  - **Học tiếp theo đúng thứ tự:** [Bài N8 — Tìm và kiểm nguồn](N8-finding-verifying-sources.md) (Bước 5/23), rồi tới [Bài N3 (Phần A) — Tìm đường trên báo cáo Việt Nam](N3-vietnam-vas-statements.md#phần-a--tìm-đường-trên-báo-cáo-sau-n2) (Bước 6/23) và [Bài 002](002-finding-a-cheap-stock.md) (Bước 7/23).
- Mục tiêu: Viết phương trình kế toán và giải thích vì sao luôn cân; ghi một giao dịch vào hai chỗ (bút toán kép); kể đúng thứ tự các tầng lợi nhuận từ doanh thu tới `EPS`; tính từng bước `EBIT`, `EBITDA`, biên lợi nhuận gộp/hoạt động/ròng, `ROA`, `ROE` và tách `ROE` theo DuPont; nhận diện khi nào `ROE` cao chỉ do vốn chủ mỏng hoặc không dùng được.
- Thời lượng: Ba phiên A/B/C + thực hành trên [`practice/models/earnings_quality.py`](../practice/models/earnings_quality.py).
- Câu hỏi cốt lõi: **Mỗi con số trên báo cáo tài chính nằm ở tầng nào, đến từ giao dịch nào, và `EBIT`, `EBITDA`, `EPS`, `ROA`, `ROE` thực chất đo cái gì?**

> Đây là bài học nền tảng, không phải khuyến nghị mua, bán hay nắm giữ chứng khoán. Ví dụ Quán cà phê Sao Biển là hư cấu (`KỊCH_BẢN`); ví dụ Apple ở mục 5 lấy từ báo cáo `10-K FY2025` gốc.

## Hiểu bài này trong 1 phút

Hãy hình dung sổ ghi chép hàng ngày của **Quán cà phê Sao Biển** (nối tiếp từ [Bài N1](N1-market-basics.md), [Bài N6](N6-business-model-unit-economics.md) và [Bài 001](001-business-financial-statements.md)). Ba báo cáo tài chính là ba cách **xếp lại** cùng một cuốn sổ gốc:

- **Bảng cân đối kế toán**: chụp ảnh tại một ngày — quán có tài sản gì, nợ ai, và phần vốn còn lại thuộc về chủ là bao nhiêu.
- **Báo cáo kết quả kinh doanh**: quay phim một kỳ — từ doanh thu bán cà phê, trừ dần nguyên liệu, lương, khấu hao, lãi vay và thuế để xem cuối cùng còn lại bao nhiêu lãi.
- **Báo cáo lưu chuyển tiền tệ**: chỉ theo dõi **tiền mặt trong két** vào/ra từ đâu (kiểm chứng tại [`practice/models/earnings_quality.py`](../practice/models/earnings_quality.py)).

> Câu cần nhớ: **Mỗi giao dịch luôn chạm ít nhất hai chỗ trong sổ sách nên Bảng cân đối luôn cân bằng; còn Lợi nhuận cuối kỳ chảy vào Vốn chủ sở hữu trên Bảng cân đối.**

## Ôn bài cũ và Chia ba phiên học

Ôn lại 3 câu hỏi từ [Bài 001 — Một doanh nghiệp đi qua ba báo cáo tài chính](001-business-financial-statements.md) (đáp án ở mục 9 cuối bài):
1. Quán Sao Biển giao đơn hàng `100 triệu đồng`, khách mới trả tiền mặt `60 triệu đồng`. Doanh thu kỳ này là bao nhiêu, và `40 triệu đồng` chưa thu nằm ở dòng nào trên báo cáo nào?
2. Báo cáo nào là "ảnh chụp tại một ngày", báo cáo nào là "cuốn phim quay suốt một kỳ"?
3. Vì sao chi tiền mua máy pha cà phê dùng 10 năm **không** làm dòng tiền hoạt động (`CFO`) bị âm?

`Ý_KIẾN` Chia bài học làm 3 phiên ngắn:

| Phiên | Phần học chính | Tự kiểm trước khi chuyển tiếp |
|---|---|---|
| **Phiên A — Ghi hai chỗ** | Mục 1–2; Bài tập 1–2 | Chủ góp 20 triệu tiền mặt: chỉ ra hai dòng cùng tăng 20 triệu để phương trình cân |
| **Phiên B — Cầu thang lợi nhuận** | Mục 3; Bài tập 3 và 6 | Giải thích `EBIT`, `EBITDA`, `EPS` và vì sao mua máy không trừ hết ngay vào lợi nhuận |
| **Phiên C — Sáu tỷ số & DuPont** | Mục 4–5; Bài tập 4–5, 7–10 | Tính `ROA`, `ROE`, tách `ROE` thành 3 phần và nêu trường hợp `ROE` cao gây hiểu sai |

## Bài này làm gì và chưa làm gì

| Bài này làm | Bài này chưa làm |
|---|---|
| Dạy phương trình kế toán và nguyên tắc "ghi hai chỗ" bằng trực giác | Không dạy định khoản Nợ/Có theo số hiệu tài khoản kế toán |
| Giải thích từng bậc thang lợi nhuận và ý nghĩa `EBIT`, `EBITDA`, `EPS` | Chưa dạy tra cứu hồ sơ gốc ([Bài N8](N8-finding-verifying-sources.md)) và mã số báo cáo Việt Nam ([Bài N3](N3-vietnam-vas-statements.md)) |
| Hướng dẫn tính 6 tỷ số cơ bản và phân rã `ROE` theo DuPont | Chưa dạy `ROIC` ([Bài 003](003-business-quality-moat-and-roic.md)), dòng tiền tự do ([Bài 004](004-cash-flow-and-earnings-quality.md)) hay bội số ([Bài 009](009-valuation-multiples.md)) |
| Thực hành đọc báo cáo thật của Apple (`Form 10-K FY2025`) | Không áp cho ngân hàng và bảo hiểm ([Bài 013](013-banks-insurers.md), [Bài F4](F4-vietnam-bank-analysis.md), [Bài F8](F8-vietnam-insurance-analysis.md)) |

## 1. Bảng cân đối: phương trình luôn cân

`SỰ_THẬT` Theo *Beginners' Guide to Financial Statements* của SEC (Mỹ), bảng cân đối tuân theo phương trình:

```text
Tài sản = Nợ phải trả + Vốn chủ sở hữu
```

- **Tài sản**: thứ doanh nghiệp kiểm soát và có thể đem lại lợi ích kinh tế — tiền, khoản khách còn nợ, hàng tồn kho, máy móc. `SỰ_THẬT` Khung khái niệm IFRS bản 2018 định nghĩa tài sản là "nguồn lực kinh tế hiện tại do doanh nghiệp kiểm soát, phát sinh từ sự kiện trong quá khứ", và nguồn lực kinh tế là "một quyền có tiềm năng tạo ra lợi ích kinh tế" (dẫn qua bài kỹ thuật của ACCA — nguồn thứ cấp).
- **Nợ phải trả**: nghĩa vụ phải trả cho người khác — vay ngân hàng, tiền còn nợ nhà cung cấp, thuế còn phải nộp. `SỰ_THẬT` Khung khái niệm 2018: "nghĩa vụ hiện tại phải chuyển giao một nguồn lực kinh tế, phát sinh từ sự kiện trong quá khứ".
- **Vốn chủ sở hữu**: phần còn lại. `PHÉP_TÍNH` Từ phương trình: `Vốn chủ = Tài sản − Nợ phải trả`. Đó là theo **giá trị sổ sách**, không phải giá bán thật.

Vốn chủ sở hữu có hai nguồn chính: **vốn chủ góp** (tiền cổ đông bỏ vào, gồm cả thặng dư vốn) và **lợi nhuận giữ lại** (lợi nhuận tích lũy chưa chia). Mua lại cổ phiếu và trả cổ tức làm vốn chủ **giảm**. Lợi nhuận mỗi kỳ chảy vào lợi nhuận giữ lại — đó là sợi dây nối báo cáo kết quả kinh doanh với bảng cân đối.

**Ngắn hạn và dài hạn**: tài sản và nợ được xếp thành ngắn hạn (dự kiến thu hồi/trả trong khoảng 12 tháng hoặc một chu kỳ kinh doanh) và dài hạn. Nợ ngắn hạn gồm cả nợ vay ngắn hạn, phải trả người bán và thuế phải nộp (xem Bài 005).

## 2. Bút toán kép: mỗi giao dịch chạm hai chỗ

Quy tắc cốt lõi: **mỗi giao dịch làm thay đổi ít nhất hai dòng, sao cho phương trình luôn cân**.

`KỊCH_BẢN` Quán cà phê hư cấu, năm đầu tiên, đơn vị: triệu đồng, thuế suất 20%.

| # | Giao dịch | Chỗ thứ nhất | Chỗ thứ hai |
|---|---|---|---|
| 1 | Chủ góp vốn 500 tiền mặt | Tiền **+500** | Vốn góp **+500** |
| 2 | Vay ngân hàng 300 | Tiền **+300** | Nợ vay **+300** |
| 3 | Mua máy pha 400, trả tiền | Máy móc **+400** | Tiền **−400** |
| 4 | Mua nguyên liệu 100, nợ nhà cung cấp | Tồn kho **+100** | Phải trả người bán **+100** |
| 5 | Bán hàng 250: thu 200, khách nợ 50 | Tiền **+200**, Phải thu **+50** | Doanh thu 250 → lợi nhuận giữ lại **+250** |
| 6 | Nguyên liệu đã dùng cho số hàng bán: 80 | Tồn kho **−80** | Giá vốn 80 → lợi nhuận giữ lại **−80** |
| 7 | Trả lương 60 | Tiền **−60** | Chi phí lương → lợi nhuận giữ lại **−60** |
| 8 | Khấu hao máy 40 (máy dùng 10 năm) | Máy móc **−40** | Chi phí khấu hao → lợi nhuận giữ lại **−40** |
| 9 | Trả lãi vay 10 | Tiền **−10** | Chi phí lãi → lợi nhuận giữ lại **−10** |
| 10 | Thuế thu nhập 12, chưa nộp | Thuế phải nộp **+12** | Chi phí thuế → lợi nhuận giữ lại **−12** |

`PHÉP_TÍNH` Trước khi lắp vào Bảng cân đối cuối năm, hãy cộng nhẩm từng dòng theo đúng 10 giao dịch trên để thấy mọi con số đều từ các phép cộng trừ đơn giản mà ra:
- **Tiền mặt trong két cuối năm:** Bắt đầu `0` + Chủ góp vốn `500` (GD 1) + Vay ngân hàng `300` (GD 2) − Mua máy pha cà phê `400` (GD 3) + Tiền mặt thu từ khách mua cà phê `200` (GD 5) − Trả lương nhân viên `60` (GD 7) − Trả lãi vay ngân hàng `10` (GD 9) = **`530 triệu đồng`**.
- **Khoản phải thu khách hàng:** Khách mua cà phê còn nợ lại **`50 triệu đồng`** (GD 5).
- **Hàng tồn kho nguyên liệu:** Nhập về `100` (GD 4) − Đã đem pha chế hết `80` (GD 6) = Còn trong kho **`20 triệu đồng`**.
- **Máy móc thiết bị (giá trị còn lại):** Mua ban đầu `400` (GD 3) − Hao mòn năm đầu `40` (GD 8) = Còn **`360 triệu đồng`**.
- **Lợi nhuận giữ lại tích lũy cuối năm:** Doanh thu bán hàng `+250` (GD 5) − Giá vốn nguyên liệu `80` (GD 6) − Chi phí lương `60` (GD 7) − Chi phí khấu hao máy `40` (GD 8) − Chi phí lãi vay `10` (GD 9) − Thuế thu nhập `12` (GD 10) = **`+48 triệu đồng`**.

Bảng cân đối kế toán cuối năm của Quán cà phê Sao Biển:

| Tài sản (Quán đang có gì?) | Số tiền | Nợ phải trả và Vốn chủ sở hữu (Nguồn tiền từ đâu?) | Số tiền |
|---|---:|---|---:|
| Tiền mặt (`500 + 300 − 400 + 200 − 60 − 10`) | 530 | Nợ vay ngân hàng (GD 2) | 300 |
| Phải thu khách hàng (GD 5) | 50 | Phải trả người bán nguyên liệu (GD 4) | 100 |
| Hàng tồn kho (`100 − 80`) | 20 | Thuế thu nhập còn phải nộp (GD 10) | 12 |
| Máy móc thiết bị (`400 − 40`) | 360 | **Tổng Nợ phải trả (`300 + 100 + 12`)** | **412** |
| | | Vốn góp ban đầu của chủ (GD 1) | 500 |
| | | Lợi nhuận giữ lại (`250 − 80 − 60 − 40 − 10 − 12`) | 48 |
| | | **Tổng Vốn chủ sở hữu (`500 + 48`)** | **548** |
| **Tổng Tài sản (`530 + 50 + 20 + 360`)** | **960** | **Tổng Nợ phải trả + Vốn chủ (`412 + 548`)** | **960** |

Ba điều đáng chú ý nhất từ bảng trên:
1. **Giao dịch 3 (mua máy pha cà phê 400 triệu) không làm giảm lợi nhuận ngay lúc mua:** Lúc mới mua, nó chỉ đổi 400 triệu từ dòng "Tiền mặt" sang dòng "Máy móc" (tổng tài sản vẫn không đổi). Chi phí của chiếc máy đi vào lợi nhuận từ từ mỗi năm `40 triệu` thông qua **khấu hao** (Giao dịch 8).
2. **Giao dịch 8 (khấu hao 40 triệu) làm giảm lợi nhuận nhưng không làm vơi tiền mặt trong năm đó:** Vì tiền mua máy đã trả từ lúc đầu năm rồi!
3. **Giao dịch 4 (mua chịu nguyên liệu 100 triệu) và Giao dịch 10 (thuế 12 triệu chưa nộp) tạo ra nghĩa vụ nợ mà chưa xuất tiền mặt ngay:** Đó là lý do Tiền mặt cuối năm (`530 triệu`) khác hoàn toàn với Lợi nhuận sau thuế (`48 triệu`).

## 3. Báo cáo kết quả kinh doanh: Đi xuống từng bậc cầu thang lợi nhuận

`SỰ_THẬT` Theo hướng dẫn của [SEC](https://www.sec.gov/reportspubs/investor-publications/investorpubsbegfinstmtguide), Báo cáo kết quả kinh doanh giống như một **cầu thang đi từ trên đỉnh xuống dưới chân**: bắt đầu từ tổng tiền bán hàng trên cùng, mỗi bước đi xuống lại trừ bớt một loại chi phí để ra một tầng lợi nhuận hẹp hơn:
1. **Doanh thu thuần (`Net Revenue / Net Sales`):** Tổng giá trị hàng bán ra sau khi đã trừ chiết khấu, hàng trả lại.
2. Trừ **Giá vốn hàng bán (`Cost of Goods Sold — COGS`)** (chi phí nguyên liệu, sản xuất trực tiếp ra món hàng đó) $\to$ còn lại **Lợi nhuận gộp (`Gross Profit`)**.
3. Trừ tiếp **Chi phí hoạt động (`Operating Expenses`)** (như lương nhân viên bán hàng, quản lý, thuê mặt bằng, nghiên cứu phát triển và khấu hao máy móc) $\to$ còn lại **Lợi nhuận hoạt động (`Operating Income`)**, thường xấp xỉ với chỉ số **`EBIT`** (*Earnings Before Interest and Taxes* — **Lợi nhuận trước lãi vay và thuế**).
4. Cộng/trừ thu nhập và **Chi phí lãi vay ngân hàng (`Interest Expense`)** $\to$ còn lại **Lợi nhuận trước thuế (`Earnings Before Taxes — EBT`)**.
5. Trừ **Thuế thu nhập doanh nghiệp (`Income Tax`)** $\to$ còn lại dòng cuối cùng là **Lợi nhuận sau thuế / Lợi nhuận ròng (`Net Income`)**.

`PHÉP_TÍNH` Áp đúng cầu thang này vào Quán cà phê Sao Biển (đơn vị: triệu đồng):

```text
  Doanh thu thuần (Giao dịch 5)                    250
− Giá vốn nguyên liệu đã dùng (Giao dịch 6)        (80)
──────────────────────────────────────────────────────
= TẦNG 1: Lợi nhuận gộp (Gross Profit)             170   (Biên gộp = 170 / 250 = 68,0%)
− Chi phí lương nhân viên (Giao dịch 7)            (60)
− Chi phí khấu hao máy pha cà phê (Giao dịch 8)    (40)
──────────────────────────────────────────────────────
= TẦNG 2: Lợi nhuận hoạt động (≈ EBIT)              70   (Biên hoạt động = 70 / 250 = 28,0%)
− Chi phí lãi vay ngân hàng (Giao dịch 9)          (10)
──────────────────────────────────────────────────────
= TẦNG 3: Lợi nhuận trước thuế (EBT)                60
− Thuế thu nhập doanh nghiệp 20% (Giao dịch 10)    (12)
──────────────────────────────────────────────────────
= TẦNG 4: Lợi nhuận sau thuế (Net Income)           48   (Biên ròng = 48 / 250 = 19,2%)
```

Hãy giải nghĩa 4 thuật ngữ viết tắt bạn sẽ gặp suốt khóa học:

| Thuật ngữ viết tắt | Tên đầy đủ và ý nghĩa bình dân | Số của Quán Sao Biển |
|---|---|---:|
| **`EBIT`** (*Earnings Before Interest and Taxes*) | **Lợi nhuận trước lãi vay và thuế:** Đo sức kiếm lời của bản thân hoạt động kinh doanh trước khi chia tiền lãi cho ngân hàng và nộp thuế cho Nhà nước. | **`70`** |
| **`EBITDA`** (*Earnings Before Interest, Taxes, Depreciation, and Amortization*) | **Lợi nhuận trước lãi vay, thuế, khấu hao và phân bổ:** Lấy `EBIT` cộng ngược lại chi phí khấu hao tài sản hữu hình (`Depreciation`) và phân bổ tài sản vô hình (`Amortization`). | `70 + 40 =` **`110`** |
| **Lợi nhuận thuộc cổ đông công ty mẹ** | Nếu một tập đoàn có các công ty con mà tập đoàn chỉ nắm 70%–80% vốn, phần lợi nhuận thuộc về 20%–30% cổ đông bên ngoài (gọi là **cổ đông không kiểm soát — `NCI`**) phải được tách riêng ra. | *(Không áp dụng vì quán chưa có công ty con)* |
| **`EPS`** (*Earnings Per Share*) | **Lãi cơ bản trên mỗi cổ phiếu:** Lấy phần lợi nhuận ròng dành cho cổ đông phổ thông chia cho số lượng cổ phiếu phổ thông đang lưu hành bình quân trong kỳ. `SỰ_THẬT` Tại Việt Nam, tử số tính `EPS` thường phải trừ thêm khoản trích **quỹ khen thưởng, phúc lợi** (ví dụ: Vinamilk năm 2025 trừ `992,8 tỷ đồng` quỹ khen thưởng phúc lợi khỏi `9.410,2 tỷ đồng` lợi nhuận thuộc công ty mẹ rồi mới chia cho `2.089.955.445` cổ phiếu để ra `EPS = 4.028 đồng/cp`; nếu quên trừ sẽ tính nhầm thành `4.503 đồng/cp` — sẽ học kỹ ở **[Bài N3](N3-vietnam-vas-statements.md)**). | — |

`SỰ_THẬT` EBITDA **không** phải chỉ tiêu do chuẩn mực quy định. Điều chỉnh thêm bất cứ khoản nào ngoài lãi vay, thuế, khấu hao, phân bổ thì đó là "EBITDA điều chỉnh", không còn là EBITDA.

Ba lưu ý tránh nhầm:
- "Lợi nhuận hoạt động" trên báo cáo **không mặc nhiên bằng** EBIT tự tính.
- **Với báo cáo Việt Nam**: dòng "lợi nhuận thuần từ hoạt động kinh doanh" (mã 30) **đã trừ lãi vay và cộng doanh thu tài chính**, nên **không phải EBIT** ([Bài N3](N3-vietnam-vas-statements.md)).
- EBITDA cộng lại khấu hao, nhưng máy móc vẫn phải mua bằng tiền thật nên EBITDA không phải tiền mặt.

## 4. Sáu tỷ số cơ bản và phân rã ROE

`PHÉP_TÍNH` Công thức và kết quả cho quán cà phê:

| Tỷ số | Công thức | Quán cà phê | Trả lời câu hỏi |
|---|---|---:|---|
| Biên gộp | Lợi nhuận gộp / Doanh thu | `170/250 = 68,0%` | Mỗi đồng doanh thu còn bao nhiêu sau giá vốn |
| Biên hoạt động | Lợi nhuận hoạt động / Doanh thu | `70/250 = 28,0%` | Sau mọi chi phí vận hành |
| Biên ròng | Lợi nhuận sau thuế / Doanh thu | `48/250 = 19,2%` | Sau lãi vay và thuế |
| Vòng quay tài sản | Doanh thu / Tổng tài sản | `250/960 = 0,26` lần | Mỗi đồng tài sản tạo bao nhiêu doanh thu |
| ROA | Lợi nhuận sau thuế / Tổng tài sản | `48/960 = 5,0%` | Lợi nhuận trên toàn bộ tài sản |
| ROE | Lợi nhuận sau thuế / Vốn chủ sở hữu | `48/548 = 8,8%` | Lợi nhuận trên phần vốn của chủ |

`SỰ_THẬT` Biên hoạt động theo SEC là lợi nhuận hoạt động chia doanh thu thuần. `SỰ_THẬT` Damodaran (NYU Stern) định nghĩa ROE kế toán là **lợi nhuận ròng năm t chia giá trị sổ sách vốn chủ đầu kỳ (t−1)**. Với doanh nghiệp đang hoạt động, hãy dùng **đầu kỳ** hoặc **bình quân**, và ghi rõ đã dùng cách nào.

`PHÉP_TÍNH` **Phân rã ROE (DuPont)**:

```text
ROE = (Lợi nhuận / Doanh thu) × (Doanh thu / Tài sản) × (Tài sản / Vốn chủ)
    =       Biên ròng        ×    Vòng quay tài sản   ×  Hệ số nhân vốn chủ
```

Quán cà phê: `19,2% × 0,2604 × (960/548 = 1,7518) = 8,76%` — khớp. Cùng một ROE có thể đến từ biên dày (thương hiệu), vòng quay nhanh (siêu thị), hoặc **hệ số nhân vốn chủ** lớn (vốn chủ mỏng so với tài sản). Lưu ý: tổng nợ phải trả gồm cả các khoản **không chịu lãi** như phải trả người bán, người mua trả trước, thuế phải nộp.

**ROE cho tập đoàn:** ROE của cổ đông công ty mẹ = lợi nhuận thuộc công ty mẹ / (vốn chủ − lợi ích cổ đông không kiểm soát); trên báo cáo Việt Nam là mã 61 / (mã 400 − mã 429) ([Bài N3](N3-vietnam-vas-statements.md)).

**Khi ROE không dùng được:** `SỰ_THẬT` McDonald's tại 31/12/2024 có tổng vốn chủ **âm 3.797** triệu USD dù lợi nhuận ròng 2024 là **8.223** triệu USD (10-K FY2024: bảng cân đối R7 và báo cáo kết quả R3). `PHÉP_TÍNH` ROE = `8.223 / (−3.797) ≈ −216,6%` — một con số vô nghĩa cho doanh nghiệp đang lãi lớn.

## 5. Ví dụ doanh nghiệp thật: Apple FY2025 theo từng tầng

`SỰ_THẬT` Số dưới đây lấy từ báo cáo kết quả hoạt động và bảng cân đối hợp nhất trong **10-K FY2025 của Apple** nộp SEC (mở ngày `2026-10-26`), đơn vị **triệu USD**, năm tài chính kết thúc 27/09/2025, chuẩn **US GAAP**.

| Tầng | FY2025 | FY2024 |
|---|---:|---:|
| Doanh thu thuần (Total net sales) | 416.161 | 391.035 |
| Giá vốn (Total cost of sales) | 220.960 | 210.352 |
| Lợi nhuận gộp (Gross margin) | 195.201 | 180.683 |
| Chi phí R&D | 34.550 | 31.370 |
| Chi phí bán hàng và quản lý (SG&A) | 27.601 | 26.097 |
| Lợi nhuận hoạt động (Operating income) | 133.050 | 123.216 |
| Thu nhập/(chi phí) khác, ròng | (321) | 269 |
| Lợi nhuận trước thuế | 132.729 | 123.485 |
| Thuế thu nhập | 20.719 | 29.749 |
| Lợi nhuận ròng | 112.010 | 93.736 |
| EPS pha loãng (USD) | 7,46 | 6,08 |
| Tổng tài sản (cuối kỳ) | 359.241 | 364.980 |
| Tổng nợ phải trả (cuối kỳ) | 285.508 | 308.030 |
| Vốn chủ sở hữu (cuối kỳ) | 73.733 | 56.950 |

`PHÉP_TÍNH` Tự kiểm các tầng FY2025: `416.161 − 220.960 = 195.201`; `195.201 − 34.550 − 27.601 = 133.050`; `133.050 − 321 = 132.729`; `132.729 − 20.719 = 112.010`. Phương trình kế toán: `285.508 + 73.733 = 359.241`.

`PHÉP_TÍNH` Tỷ số FY2025 (mẫu số đầu kỳ tại 28/09/2024):
- Biên gộp `195.201 / 416.161 = 46,9%`; biên hoạt động `133.050 / 416.161 = 32,0%`; biên ròng `112.010 / 416.161 = 26,9%`.
- EBITDA xấp xỉ từ lợi nhuận hoạt động: `133.050 + 11.698` (khấu hao và phân bổ trên báo cáo dòng tiền) = `144.748`.
- ROA = `112.010 / 364.980 = 30,7%`.
- ROE đầu kỳ = `112.010 / 56.950 = 196,7%` (phân rã DuPont: `26,9% × 1,14 × 6,41 = 196,7%`). Dùng vốn chủ **bình quân** `(56.950 + 73.733)/2` cho ROE = `171,4%`; dùng **cuối kỳ** cho `151,9%`.

Ba bài học từ Apple FY2025:
1. **ROE gần 200% là do hệ số nhân vốn chủ 6,41 (vốn chủ mỏng do mua lại cổ phiếu nhiều năm)**, không có nghĩa Apple vay nợ ròng nặng. `SỰ_THẬT` Tại 27/09/2025, tổng nợ vay (`7.979 + 12.350 + 78.328`) là **98.657**, trong khi tiền và chứng khoán đầu tư (`35.934 + 18.763 + 77.723`) là **132.420** triệu USD → `PHÉP_TÍNH` Apple có **tiền ròng khoảng 33.763 triệu USD**; nợ vay chỉ chiếm `34,6%` tổng nợ phải trả (phần còn lại là phải trả người bán `69.860` và các khoản không chịu lãi). Theo bảng thay đổi vốn chủ FY2025, Apple mua lại cổ phiếu **90.052** và công bố cổ tức **15.413** triệu USD (`56.950 + 112.010 + 1.601 + 13.246 + 1.498 − 4.452 − 1.655 − 90.052 − 15.413 = 73.733`).
2. **Ba quy ước mẫu số cho ba mức ROE khác hẳn nhau** (`151,9% / 171,4% / 196,7%`), nên khi so sánh phải dùng cùng quy ước.
3. **Thuế suất hiệu dụng thay đổi mạnh:** `PHÉP_TÍNH` `20.719 / 132.729 = 15,6%` ở FY2025 so với `29.749 / 123.485 = 24,1%` ở FY2024 do quý IV FY2024 có khoản chi phí thuế một lần **10,2 tỷ USD** liên quan quyết định State Aid của EU với Ireland.

## 6. Năm câu hỏi khi đọc từng dòng

1. Doanh thu thuần đã trừ các khoản giảm trừ chưa? Xu hướng biên lợi nhuận gộp 3–5 năm ra sao?
2. Giữa lợi nhuận gộp và lợi nhuận hoạt động có khoản nào lặp lại, khoản nào bất thường một lần?
3. Lãi vay và thuế chiếm bao nhiêu phần trăm lợi nhuận hoạt động; thuế suất hiệu dụng có ổn định không?
4. Vốn chủ đến từ vốn góp hay lợi nhuận giữ lại, và đã mua lại cổ phiếu/trả cổ tức bao nhiêu?
5. ROE cao do biên ròng, vòng quay tài sản hay hệ số nhân vốn chủ — và vốn chủ có âm hoặc quá mỏng không?

## 7. Bài tập

`KỊCH_BẢN` Số liệu hư cấu, đơn vị: triệu đồng, thuế suất 20% nếu không nói khác. Hãy tự giải toàn bộ 10 bài trước khi mở Đáp án:

1. **Phương trình kế toán:** Một doanh nghiệp có tiền 120, phải thu 80, tồn kho 100, máy móc 300; nợ vay 200, phải trả người bán 90. Tính tổng tài sản, tổng nợ phải trả và vốn chủ sở hữu.
2. **Ghi hai chỗ (Bút toán kép):** Với mỗi giao dịch, nêu hai dòng thay đổi và chiều tăng/giảm: (a) trả nợ vay 50 bằng tiền; (b) bán hàng 70, khách nợ toàn bộ; (c) thu 30 tiền từ khách đã nợ; (d) mua tồn kho 40 bằng tiền.
3. **Dựng các tầng lợi nhuận:** Doanh thu thuần 1.000; giá vốn 600; chi phí bán hàng 120; chi phí quản lý 80; khấu hao (đã nằm trong các chi phí trên) 50; chi phí lãi vay 40. Tính lợi nhuận gộp, EBIT, EBITDA, lợi nhuận trước thuế, lợi nhuận sau thuế.
4. **Sáu tỷ số và DuPont:** Dùng kết quả Bài 3. Biết tổng tài sản đầu kỳ 1.600, vốn chủ đầu kỳ 400. Tính biên gộp, biên hoạt động, biên ròng, ROA, ROE (đầu kỳ) và kiểm bằng phân rã DuPont.
5. **Cùng ROE, khác chất lượng:** Hai doanh nghiệp cùng ROE 20%. X: biên ròng 20%, vòng quay 0,5, hệ số nhân vốn chủ 2. Y: biên ròng 2%, vòng quay 2,0, hệ số nhân vốn chủ 5. Kiểm ROE của cả hai. Giả sử tỷ trọng chi phí cố định trong tổng chi phí của hai bên như nhau: nếu doanh thu cả hai giảm 10%, doanh nghiệp nào nguy hiểm hơn và vì sao?
6. **Cầu nối Lợi nhuận sang Dòng tiền hoạt động (`CFO`):** Dùng bảng giao dịch quán cà phê ở mục 2. Dựng dòng tiền hoạt động theo phương pháp gián tiếp từ lợi nhuận sau thuế 48 (coi lãi vay đã trả là dòng tiền hoạt động) và kiểm với tiền thực thu, thực chi.
7. **Phát hiện lỗi ROE và EBITDA:** "Công ty Z có ROE 45%, cao gấp ba ngành, chứng tỏ ban điều hành giỏi gấp ba. EBITDA 500 nghĩa là công ty có 500 tiền để trả nợ." Chỉ ra **hai** lỗi và cách kiểm.
8. **Đọc chênh lệch giữa các tầng báo cáo:** Một doanh nghiệp có lợi nhuận hoạt động tăng 10%, lợi nhuận sau thuế giảm 15%, vốn chủ giảm 30% trong khi lợi nhuận vẫn dương. Nêu **ba** giả thuyết giải thích và dòng báo cáo cần mở để kiểm.
9. **Tác động của Quỹ khen thưởng, phúc lợi lên EPS tại Việt Nam:** Tập đoàn M có lợi nhuận sau thuế thuộc cổ đông công ty mẹ là `1.200 tỷ đồng`, trích quỹ khen thưởng phúc lợi `150 tỷ đồng`, số cổ phiếu phổ thông lưu hành bình quân là `300 triệu cổ phiếu`. Tính EPS cơ bản trước và sau khi trừ quỹ khen thưởng phúc lợi.
10. **Đối chiếu chất lượng lợi nhuận qua [earnings_quality.py](../practice/models/earnings_quality.py):** Công ty K báo cáo lợi nhuận sau thuế năm nay tăng từ `100` lên `180` triệu đồng, nhưng khoản phải thu khách hàng tăng thêm `+140` triệu đồng, hàng tồn kho tăng thêm `+60` triệu đồng, phải trả người bán không đổi, khấu hao `30` triệu đồng. Hãy tính `CFO` theo phương pháp gián tiếp và tỷ lệ chuyển hóa tiền mặt (`CFO / LNST`).

## 8. Đáp án

1. **Phương trình kế toán:** `PHÉP_TÍNH` Tổng tài sản `120 + 80 + 100 + 300 = 600`; nợ phải trả `200 + 90 = 290`; vốn chủ `600 − 290 = 310`.
2. **Ghi hai chỗ:** (a) Tiền **−50**, nợ vay **−50** (lợi nhuận không đổi); (b) Phải thu **+70**, doanh thu 70 → lợi nhuận giữ lại **+70** (tiền không đổi); (c) Tiền **+30**, phải thu **−30** (đổi dạng tài sản, lợi nhuận không đổi); (d) Tồn kho **+40**, tiền **−40** (lợi nhuận không đổi cho đến khi bán).
3. **Các tầng lợi nhuận:** `PHÉP_TÍNH` Lợi nhuận gộp `1.000 − 600 = 400`; EBIT `400 − 120 − 80 = 200`; EBITDA `200 + 50 = 250` (khấu hao đã nằm trong chi phí hoạt động nên chỉ cộng lại khi tính EBITDA); lợi nhuận trước thuế `200 − 40 = 160`; lợi nhuận sau thuế `160 × 0,8 = 128`.
4. **Sáu tỷ số và DuPont:** `PHÉP_TÍNH` Biên gộp `400/1.000 = 40,0%`; biên hoạt động `200/1.000 = 20,0%`; biên ròng `128/1.000 = 12,8%`; ROA `128/1.600 = 8,0%`; ROE `128/400 = 32,0%`. DuPont: `12,8% × (1.000/1.600 = 0,625) × (1.600/400 = 4,0) = 32,0%` — khớp.
5. **Cùng ROE, khác chất lượng:** `PHÉP_TÍNH` X: `20% × 0,5 × 2 = 20%`; Y: `2% × 2,0 × 5 = 20%`. `SUY_LUẬN` Với cùng tỷ trọng định phí, Y nguy hiểm hơn vì biên ròng chỉ 2% dễ bị xóa sạch khi doanh thu giảm, và hệ số nhân vốn chủ 5 phóng đại khoản lỗ trên vốn chủ. (Nếu bỏ giả định cùng tỷ trọng định phí thì phải đọc cơ cấu định phí/biến phí trước khi kết luận).
6. **Cầu nối `CFO`:** `PHÉP_TÍNH` `48 + 40 (khấu hao) − 50 (phải thu tăng) − 20 (tồn kho tăng) + 100 (phải trả người bán tăng) + 12 (thuế phải nộp tăng) = 130`. Kiểm bằng tiền thực: thu từ khách `200 − lương 60 − lãi 10 = 130` — khớp. (`SỰ_THẬT` Khi IFRS 18 có hiệu lực từ `2027-01-01`, doanh nghiệp không cung cấp tài chính như hoạt động chính xếp lãi vay đã trả vào dòng tiền tài chính, khi đó `CFO = 140` và dòng tiền tài chính `= 790`).
7. **Phát hiện lỗi ROE và EBITDA:** `SUY_LUẬN` Lỗi 1: ROE cao có thể do hệ số nhân vốn chủ lớn hoặc mua lại cổ phiếu làm mỏng vốn chủ (như Apple), thậm chí vô nghĩa khi vốn chủ âm (như McDonald's). Cách kiểm: phân rã DuPont, xem ROA và ROIC. Lỗi 2: EBITDA chưa trừ thuế, chưa trừ `CapEx` và biến động vốn lưu động nên không phải tiền mặt trả nợ.
8. **Chênh lệch các tầng báo cáo:** `SUY_LUẬN` Ba giả thuyết giữa lợi nhuận hoạt động và sau thuế: (1) chi phí lãi vay tăng; (2) thuế suất hiệu dụng tăng hoặc có thuế một lần; (3) lỗ tỷ giá/chi phí khác. Vốn chủ giảm 30% dù lãi dương: trả cổ tức hoặc mua lại cổ phiếu lớn hơn lợi nhuận ròng — mở bảng thay đổi vốn chủ sở hữu.
9. **EPS và Quỹ khen thưởng phúc lợi:** `PHÉP_TÍNH` EPS trước trích quỹ = `1.200 / 300 = 4.000 đồng/cp`. EPS sau trích quỹ = `(1.200 − 150) / 300 = 1.050 / 300 = 3.500 đồng/cp` (thấp hơn `12,5%`).
10. **Chất lượng lợi nhuận qua [earnings_quality.py](../practice/models/earnings_quality.py):** `PHÉP_TÍNH` `CFO = 180 + 30 (khấu hao) − 140 (phải thu tăng) − 60 (tồn kho tăng) = +10 triệu đồng`. Tỷ lệ chuyển hóa tiền mặt `CFO / LNST = 10 / 180 ≈ 5,56%` (lợi nhuận tăng mạnh nhưng nằm gần hết ở khoản phải thu và tồn kho).

## 9. Đáp án phần ôn bài cũ

1. Doanh thu có thể là 100 nếu đã đủ điều kiện ghi nhận; 40 còn lại là **phải thu khách hàng** trên bảng cân đối.
2. Bảng cân đối là ảnh chụp tại một ngày; báo cáo kết quả kinh doanh và lưu chuyển tiền tệ là phim trong một kỳ.
3. Vì mua tài sản dài hạn được xếp vào **dòng tiền đầu tư**, không phải dòng tiền hoạt động.

## Bài làm với dữ liệu thiếu hoặc lệch

Khi đọc báo cáo thực tế để tính tỷ số ở bài `N2`, bạn thường gặp hai tình huống dữ liệu lệch hoặc thiếu:
1. **Khấu hao nằm ẩn trong Giá vốn và Chi phí hoạt động:** Báo cáo kết quả kinh doanh (cả US GAAP như Apple lẫn VAS ở Việt Nam) thường không tách dòng riêng "Chi phí khấu hao" trên mặt bảng kết quả kinh doanh.
2. **Lệch mẫu số Vốn chủ (`Đầu kỳ`, `Cuối kỳ`, `Bình quân`) và Lợi ích cổ đông không kiểm soát (`NCI`):** Các trang web tự động tính `ROE` bằng nhiều công thức khác nhau mà không ghi chú.

**Quy trình xử lý chuẩn:**
- **Bước 1 — Lấy Khấu hao & Phân bổ (`D&A`) từ Báo cáo lưu chuyển tiền tệ (phương pháp gián tiếp) hoặc Thuyết minh chi phí theo yếu tố:** Như với Apple FY2025 (`11.698 triệu USD` trên báo cáo dòng tiền), luôn mở Báo cáo dòng tiền phần điều chỉnh khấu hao để cộng vào `EBIT`. Nếu thiếu thuyết minh, gắn nhãn `CHƯA_BIẾT` đối với `EBITDA`.
- **Bước 2 — Chuẩn hóa mẫu số và kiểm tra chất lượng thu nhập qua [earnings_quality.py](../practice/models/earnings_quality.py):** Ghi rõ quy ước mẫu số (`ROE đầu kỳ` hay `bình quân`), tách `NCI` khỏi vốn chủ cổ đông công ty mẹ, và kiểm tra `CFO / Lợi nhuận ròng`.

## Sai ở đâu

### Sai lầm 1: Lọc cổ phiếu theo "ROE cao nhất sàn" mà không phân rã DuPont
- **Sai ở đâu:** Bỏ qua `Hệ số nhân vốn chủ = Tài sản / Vốn chủ`. Doanh nghiệp có vốn chủ mỏng dính do lỗ lũy kế hoặc vay nợ cao chỉ cần lãi nhẹ là `ROE` vọt lên `50%–100%`; ngược lại, công ty mua lại cổ phiếu mạnh như McDonald's có vốn chủ âm (`-3.797 triệu USD`) có `ROE` âm (`-216,6%`).
- **Cách sửa:** Luôn phân rã `ROE = Biên ròng × Vòng quay tài sản × Hệ số nhân vốn chủ` và kết hợp với `ROA`, `ROIC`.

### Sai lầm 2: Trừ khấu hao hai lần khi tính `EBIT` hoặc coi `EBITDA` là tiền mặt trả nợ
- **Sai ở đâu:** (1) Khấu hao đã nằm sẵn trong Giá vốn, Chi phí bán hàng và Quản lý nên trừ thêm là tính trùng; (2) `EBITDA` chưa trừ thuế, biến động vốn lưu động và `CapEx`.
- **Cách sửa:** Kiểm tra cầu nối từ Lợi nhuận sang `CFO` và `FCF` bằng [earnings_quality.py](../practice/models/earnings_quality.py).

### Sai lầm 3: Áp dụng Biên lợi nhuận gộp và `EBITDA` của bài `N2` cho Ngân hàng và Bảo hiểm
- **Sai ở đâu:** Với ngân hàng, lãi vay là chi phí đầu vào để tạo thu nhập lãi thuần (`NII`), không tồn tại khái niệm `EBITDA`.
- **Cách sửa:** Với ngân hàng và bảo hiểm, dùng khung riêng tại [Bài 013](013-banks-insurers.md), [Bài F4](F4-vietnam-bank-analysis.md) và [Bài F8](F8-vietnam-insurance-analysis.md).

## Kiểm tra chuyển bài

Trước khi chuyển sang [Bài N8 — Tìm và kiểm nguồn](N8-finding-verifying-sources.md) (Bước 5/23) và [Bài N3 (Phần A) — Tìm đường trên báo cáo Việt Nam](N3-vietnam-vas-statements.md#phần-a--tìm-đường-trên-báo-cáo-sau-n2) (Bước 6/23), hãy trả lời 3 câu hỏi sau:

1. **Chuyển giao sang [Bài N8](N8-finding-verifying-sources.md) & [Bài N3](N3-vietnam-vas-statements.md):** Vì sao trên Báo cáo kết quả kinh doanh Việt Nam bạn **không được** lấy dòng "Lợi nhuận thuần từ hoạt động kinh doanh" (mã 30) làm `EBIT`?
2. **Chuyển giao sang [Bài 003](003-business-quality-moat-and-roic.md):** Qua ví dụ Apple FY2025 (`ROE đầu kỳ = 196,7%`), vì sao cần học thêm chỉ số `ROIC` ở Bài 003?
3. **Chuyển giao sang [`practice/models/earnings_quality.py`](../practice/models/earnings_quality.py):** Nếu lợi nhuận tăng vọt nhờ bán chịu (`Phải thu khách hàng` tăng), dòng nào trên Báo cáo lưu chuyển tiền tệ gián tiếp sẽ phơi bày việc chưa thu được tiền mặt?

## 11. Ranh giới an toàn và Điều chưa hiểu

- Bài này là khung đọc báo cáo, **không** phải khuyến nghị mua/bán/nắm giữ. Số liệu Apple là dữ liệu lịch sử FY2025 tại ngày chốt; không tỷ số nào trong bài chứa **giá cổ phiếu**, nên không thể nói đắt hay rẻ (xem Bài 002, 009).
- `SỰ_THẬT` Góp ý của nhân viên SEC ngày 22/12/2023 (trích trong thư phản hồi của KBR ngày 02/01/2024): nếu điều chỉnh lợi nhuận ròng bằng bất cứ khoản nào **ngoài** lãi vay, thuế, khấu hao và phân bổ thì không được gọi thước đo đó là EBITDA (dẫn C&DI 103.01; `CHƯA_BIẾT` trang C&DI gốc trả HTTP 404).

## 13. Nguồn Internet đã mở

Tất cả mở ngày `2026-10-26` và kiểm tra đối chiếu `2026-11-05`:

| Nguồn | Trạng thái | Ngày xuất bản / kỳ | Dùng cho |
|---|---|---|---|
| [Beginners' Guide to Financial Statements — U.S. SEC](https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements) | Mở được | Đăng 2014-01-12; cập nhật 2017-02-06 | Phương trình kế toán; định nghĩa tài sản/nợ/vốn chủ; các tầng lợi nhuận; EPS; biên hoạt động |
| [Extreme makeover — ACCA](https://www.accaglobal.com/uk/en/student/exam-support-resources/fundamentals-exams-study-resources/f7/technical-articles/extreme-makeover.html) | Mở được; nguồn thứ cấp | Mô tả Khung khái niệm IASB bản 03/2018 | Định nghĩa tài sản, nguồn lực kinh tế, nợ phải trả theo Khung khái niệm 2018 |
| [Conceptual Framework — IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/conceptual-framework/) | Mở được | Ban hành 03/2018 | Xác nhận Khung 2018 đặt định nghĩa tài sản, nợ, vốn chủ, thu nhập, chi phí |
| [Thư phản hồi của KBR gửi SEC (CORRESP)](https://www.sec.gov/Archives/edgar/data/1357615/000135761524000002/filename1.htm) | Mở được | 2024-01-02 (trích góp ý SEC 2023-12-22) | Quy tắc chỉ gọi là EBITDA khi chỉ điều chỉnh lãi vay, thuế, khấu hao, phân bổ |
| [Damodaran — Return on Capital, ROIC and ROE (PDF, NYU Stern)](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/returnmeasures.pdf) | Mở được | Bản 2007 | Định nghĩa ROE = lợi nhuận ròng năm t / vốn chủ sổ sách đầu kỳ |
| [Apple Inc. Form 10-K FY2025 — SEC EDGAR](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Nguồn **gốc** | FY kết thúc 2025-09-27; triệu USD; US GAAP | Báo cáo kết quả hoạt động, bảng cân đối, khấu hao, mua lại cổ phiếu, cổ tức, thuế một lần FY2024 |
| [Vinamilk — BCTC hợp nhất kiểm toán 2025](https://d8um25gjecm9v.cloudfront.net/cms/20260227_BCTC_KIEM_TOAN_2025_HOP_NHAT_VN_94f1e76e45.pdf) | Nguồn **gốc** | Ngày ký 27/02/2026; đồng; VAS | Thuyết minh VI.11 (EPS sau trích quỹ khen thưởng, phúc lợi) |
| [McDonald's Form 10-K FY2024 — R7](https://www.sec.gov/Archives/edgar/data/63908/000006390825000012/R7.htm) & [R3](https://www.sec.gov/Archives/edgar/data/63908/000006390825000012/R3.htm) | Nguồn **gốc** | Ngày 31/12/2024; triệu USD; US GAAP | Vốn chủ âm −3.797 (R7); lợi nhuận ròng 8.223 (R3) |
| [KPMG — IFRS 18 changes to the statement of cash flows](https://kpmg.com/us/en/articles/2026/ifrs-18-changes-statement-cash-flows.html) | Nguồn thứ cấp | 2026-06-01 | Phân loại lãi vay và điểm xuất phát phương pháp gián tiếp theo IFRS 18 |
