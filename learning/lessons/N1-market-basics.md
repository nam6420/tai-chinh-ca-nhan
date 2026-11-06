# Bài N1 — Thị trường chứng khoán vận hành thế nào?

- Ngày cập nhật: `2026-11-06`
- Chốt dữ liệu lúc: `2026-11-06 10:48 UTC+7 (Asia/Ho_Chi_Minh)`
- Bậc chiều sâu: `Bậc S`
- Lộ trình đọc: **Bài 1 (Mở đầu Nhánh 1 & Nhánh 2)**.
  - **Bài trước liên quan:** Không yêu cầu kiến thức tài chính (nếu muốn chuẩn bị ngân sách cá nhân và nhận diện lừa đảo trước khi mở tài khoản, hãy đọc [Bài P1 — Ngân sách, quỹ khẩn cấp và bảo hiểm](P1-budget-emergency-fund-insurance.md) và [Bài B3 — Bảo mật tài khoản và lừa đảo](B3-account-security-scams.md)).
  - **Học tiếp theo đúng thứ tự:**
    - **Nhánh 1 (Hiểu doanh nghiệp & Phân tích cổ phiếu):** Đọc tiếp **[Bài N6 — Doanh nghiệp kiếm tiền thế nào?](N6-business-model-unit-economics.md)** (Bước 2/23).
    - **Nhánh 2 (Danh mục & Quỹ chỉ số):** Đọc tiếp **[Bài N5 (Phần A) — Danh mục và đầu tư theo chỉ số](N5-portfolio-index-investing.md)**.
    - **Nhánh 3 (Thị trường Việt Nam):** Đọc tiếp **[Bài V1 — Cấu trúc thị trường chứng khoán Việt Nam](V1-vietnam-market-structure.md)**.
- Mục tiêu: Phân biệt rõ góp vốn làm chủ (cổ đông) với cho vay (chủ nợ); chỉ ra chính xác tiền chảy về đâu khi công ty phát hành cổ phần mới so với khi nhà đầu tư mua bán lại cổ phần cũ trên sàn; đọc đúng bảng giá (giá chào mua, giá chào bán, giá khớp) và hiểu vì sao giá 1 cổ phiếu thấp không có nghĩa là công ty rẻ.
- Thời lượng: Ba phiên học ngắn (30–40 phút/phiên) có điểm dừng tự kiểm; thực hành trên [`practice/models/market_returns.py`](../practice/models/market_returns.py).
- Câu hỏi cốt lõi: **Khi tôi bỏ tiền mua một cổ phiếu trên sàn chứng khoán, tôi thực sự sở hữu cái gì và số tiền tôi vừa trả chảy vào túi ai?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

---

## Hiểu bài này trong 1 phút

Hãy tưởng tượng một người bạn mở **Quán cà phê Sao Biển** cần vốn. Nếu bạn góp tiền để nắm 1% quyền làm chủ quán, phần quyền làm chủ đó chính là **cổ phần** (hay **cổ phiếu**).

Có ba điều người mới thường hiểu lầm nhất khi bước vào thị trường chứng khoán:
1. **Tiền mua cổ phiếu trên sàn hàng ngày không chảy vào két công ty:** Khi bạn lên ứng dụng mua lại 1% phần vốn Quán Sao Biển từ anh Minh (một chủ cũ muốn nhượng lại), tiền của bạn chuyển thẳng vào túi anh Minh. Quán Sao Biển chỉ nhận được tiền mới khi chính quán in thêm cổ phần mới để gọi vốn mở chi nhánh.
2. **Làm chủ 1% công ty không có nghĩa là được tự ý mở két lấy 1% tiền mặt của công ty:** Tiền trong tài khoản của quán thuộc về pháp nhân công ty để mua nguyên liệu, trả lương và trả nợ. Cổ đông chỉ nhận được tiền mặt khi công ty làm ăn có lãi và quyết định trích lãi chia cho chủ sở hữu (gọi là **cổ tức**).
3. **Giá hiển thị trên màn hình không phải là "giá trị thật" của doanh nghiệp:** Con số `20.000 đồng/cổ phiếu` trên bảng điện chỉ là mức giá hai người vừa đồng ý trao đổi cho một mảnh nhỏ của công ty. Muốn biết toàn bộ công ty đang được định giá bao nhiêu, bạn phải nhân giá 1 cổ phần với tổng số cổ phần của cả công ty.

---

## Ôn bài cũ hoặc kiểm tra đầu vào

Đây là **bài đầu tiên** của lộ trình cốt lõi nên bạn chưa cần biết công thức tài chính nào (nếu muốn kiểm tra ngân sách cá nhân và bảo mật tài khoản trước khi mở tài khoản, có thể xem thêm [Bài P1](P1-budget-emergency-fund-insurance.md) và [Bài B3](B3-account-security-scams.md)). Hãy bắt đầu bằng một tình huống đời thường:

- **Tình huống đầu vào:** Bạn có `50 triệu đồng` nhàn rỗi. Quán cà phê Sao Biển cần tiền mua máy pha cà phê mới và đưa cho bạn hai lựa chọn:
  - **Lựa chọn A (Cho vay):** Bạn cho quán vay `50 triệu đồng` trong 1 năm; hợp đồng vay ghi rõ cuối năm quán phải trả gốc `50 triệu` cộng `5 triệu` tiền lãi, bất kể quán đông khách hay vắng khách.
  - **Lựa chọn B (Góp vốn làm chủ):** Bạn góp `50 triệu đồng` để sở hữu `10%` quán. Quán không hứa trả lãi cố định; nếu quán ăn nên làm ra, phần 10% của bạn ngày càng có giá và được chia lời lớn; nếu quán thua lỗ đóng cửa, bạn cùng chịu lỗ.
- **Điểm cần nắm trước khi đọc tiếp:** Lựa chọn A là vị thế **chủ nợ** (trái chủ / người cho vay) — hưởng quyền đòi nợ theo hợp đồng. Lựa chọn B là vị thế **chủ sở hữu** (cổ đông) — hưởng thành quả khi doanh nghiệp thịnh vượng nhưng chịu rủi ro sau cùng khi doanh nghiệp thất bại.

## Bài này làm gì và chưa làm gì

| Bài này làm | Bài này chưa làm |
|---|---|
| Giải thích bản chất cổ phiếu, trái phiếu, dòng chảy của tiền và cơ chế khớp lệnh bằng ví dụ đời thường | Chưa dạy cách xem Quán Sao Biển bán mỗi ly cà phê lãi bao nhiêu (học ngay ở **[Bài N6](N6-business-model-unit-economics.md)**) |
| Hướng dẫn tính từng bước tỷ lệ sở hữu, vốn hóa thị trường và giá trị doanh nghiệp giản lược | Chưa dạy bước giá, biên độ, chu kỳ thanh toán riêng của sàn Việt Nam (xem **[Bài V1](V1-vietnam-market-structure.md)** và **[Bài V2](V2-vietnam-trading-rules.md)**) |
| Chỉ ra bẫy nhầm "giá 1 cổ phiếu thấp" với "công ty đang rẻ" | Chưa dạy cách đọc 3 báo cáo tài chính (xem **[Bài 001](001-business-financial-statements.md)** và **[Bài N2](N2-statement-line-items.md)**) |

---

## Phiên 1 — Góp vốn làm chủ khác cho vay ở đâu?

### 1.1. Hai chiếc ghế quanh cùng một doanh nghiệp: Cổ đông và Chủ nợ

Khi Quán cà phê Sao Biển lớn dần và chuyển thành công ty cổ phần, công ty vẫn chỉ có hai cách chính để huy động vốn từ bên ngoài:
1. **Phát hành cổ phiếu (`Stocks / Shares / Equity`):** Chia quyền làm chủ công ty thành nhiều phần bằng nhau (**cổ phần**). Người mua trở thành **cổ đông (`shareholder`)** — đồng chủ sở hữu công ty.
2. **Vay nợ hoặc phát hành trái phiếu (`Bonds / Debt`):** Công ty ký hợp đồng vay tiền (với ngân hàng, hoặc chia khoản vay thành nhiều giấy nhận nợ gọi là **trái phiếu** để vay từ công chúng). Người mua trái phiếu là **trái chủ (`bondholder`)** — chủ nợ của công ty.

`SỰ_THẬT` Theo trang giáo dục nhà đầu tư của Ủy ban Chứng khoán Hoa Kỳ ([SEC — Investor.gov: Stocks](https://www.investor.gov/introduction-investing/investing-basics/investment-products/stocks) và [Bonds](https://www.investor.gov/introduction-investing/investing-basics/investment-products/bonds-or-fixed-income-products/bonds)), cổ phiếu đại diện cho một phần quyền sở hữu công ty và khoản tiền chia từ lợi nhuận (**cổ tức — `dividend`**) chỉ phát sinh khi hội đồng quản trị công bố chia, hoàn toàn không được bảo đảm trước. Ngược lại, trái phiếu là khoản vay có cam kết trả lãi và hoàn gốc theo lịch hợp đồng.

| Người nắm giữ | Bản chất kinh tế | Câu hỏi đầu tiên cần hỏi | Điều tuyệt đối không được tự giả định |
|---|---|---|---|
| **Cổ đông** (giữ cổ phiếu) | Đồng chủ sở hữu doanh nghiệp | Cổ phần này cho quyền biểu quyết và hưởng lợi nhuận ra sao? | "Nắm 1% cổ phiếu là được rút 1% tiền trong két công ty hoặc năm nào cũng chắc chắn có cổ tức." |
| **Trái chủ** (giữ trái phiếu) | Chủ nợ cho doanh nghiệp vay | Ai nợ tôi, ngày nào trả gốc và lãi, có tài sản gì bảo đảm không? | "Cứ gọi là trái phiếu thì an toàn như tiền gửi tiết kiệm ngân hàng." |
| **Người giữ chứng chỉ quỹ** (`Fund unit`) | Góp tiền vào một giỏ chung để quỹ mua nhiều cổ phiếu/trái phiếu | Quỹ đang giữ những tài sản gì, thu phí quản lý bao nhiêu % mỗi năm? | "Mua quỹ thì không bao giờ lỗ." (Quỹ vẫn tăng giảm theo giá tài sản trong giỏ). |

### 1.2. Thứ tự ưu tiên khi doanh nghiệp gặp nạn

Tại sao cổ đông hưởng trọn phần lời khi công ty phát đạt nhưng chịu rủi ro cao hơn chủ nợ?
- Hàng tháng, Quán Sao Biển phải trả tiền nguyên liệu cho nhà cung cấp, trả lương nhân viên, trả lãi và gốc vay cho ngân hàng/trái chủ, rồi nộp thuế. Phần lợi nhuận còn lại sau cùng mới thuộc về cổ đông.
- `SỰ_THẬT` Theo [SEC — Investor.gov: Stocks](https://www.investor.gov/introduction-investing/investing-basics/investment-products/stocks), nếu công ty thất bại và phải thanh lý tài sản để trả nợ, chủ nợ có bảo đảm và trái chủ được ưu tiên nhận tiền trước; **cổ đông phổ thông (`common shareholders`) đứng ở hàng cuối cùng** và có thể mất toàn bộ vốn góp nếu tài sản bán đi chỉ vừa đủ trả nợ. *(Thứ tự ưu tiên cụ thể tại từng quốc gia tuân theo Luật Doanh nghiệp, Luật Phá sản và điều lệ công ty tại thị trường đó).*

### 1.3. Ba câu hỏi hoàn toàn khác nhau: Sản phẩm tốt, Công ty tốt và Giá mua hợp lý

`SUY_LUẬN` Người mới rất dễ đánh đồng: *"Quán Sao Biển cà phê ngon và đông khách → mua cổ phiếu Sao Biển giá nào cũng thắng!"* Thực tế, đây là **ba câu hỏi tách biệt**:
1. **Sản phẩm có tốt không?** (Khách có thích cà phê Sao Biển không?)
2. **Doanh nghiệp kiếm tiền và giữ tiền có tốt không?** (Trừ hết tiền thuê mặt bằng và lương nhân viên, quán có còn lãi và có tiền thật trong két không? — Học ở **[Bài N6](N6-business-model-unit-economics.md)** và **[Bài 001](001-business-financial-statements.md)**).
3. **Giá cổ phiếu đang mua có hợp lý không?** (Nếu cả quán chỉ đáng giá 10 tỷ đồng nhưng người bán đòi mức giá cổ phần tương đương 50 tỷ đồng cho cả quán, bạn mua vào vẫn thua lỗ — Học ở **[Bài 002](002-finding-a-cheap-stock.md)**).

> **Điểm dừng Phiên 1:** Hãy tự giải thích bằng lời của bạn: (1) Điểm khác nhau lớn nhất giữa người mua cổ phiếu và người cho công ty vay tiền là gì? (2) Vì sao một công ty đang có lãi nhưng năm nay không chia cổ tức tiền mặt chưa chắc là công ty xấu?

---

## Phiên 2 — Phát hành mới và Mua bán lại: Tiền chảy đi đâu?

Khi bạn bỏ 2 triệu đồng mua 100 cổ phiếu Quán Sao Biển trên ứng dụng chứng khoán, **Quán Sao Biển có nhận được 2 triệu đồng đó để mua thêm máy pha cà phê không?** Câu trả lời là: **Hầu như mọi giao dịch bấm nút mua/bán hàng ngày trên sàn đều KHÔNG chuyển tiền vào công ty!** Hãy tách rõ hai chặng đường của một cổ phiếu:

### 2.1. Chặng 1 (Thị trường sơ cấp) và Chặng 2 (Thị trường thứ cấp)

`SỰ_THẬT` Theo từ điển của [SEC — Investor.gov Glossary (“Primary Market” và “Secondary Market”)](https://www.investor.gov/introduction-investing/investing-basics/glossary) và [SIFMA Capital Markets Primer (09/2024)](https://www.sifma.org/wp-content/uploads/2024/09/SIFMA-Insights-Primer_Capital-Markets_FINAL.pdf):
- **Thị trường sơ cấp (`Primary Market` — Chặng phát hành mới):** Là nơi công ty tạo ra cổ phần mới và bán lần đầu cho nhà đầu tư để huy động vốn. **Ở chặng này, tiền của người mua chảy vào két của công ty phát hành** (sau khi trừ chi phí phát hành).
- **Thị trường thứ cấp (`Secondary Market` — Chặng mua đi bán lại trên sàn):** Là nơi các nhà đầu tư mua bán lại những cổ phần **đã phát hành từ trước** với nhau (như trên HOSE, HNX, NYSE, Nasdaq). **Ở chặng này, tiền chảy từ túi người mua sang túi người bán; công ty không nhận thêm đồng vốn nào** và tổng số cổ phần của công ty giữ nguyên.

### 2.2. Đi từng bước qua ví dụ Công ty Sao Biển

`KỊCH_BẢN` Hãy theo dõi từng bước số cổ phần và dòng tiền của **Công ty Cà phê Sao Biển**:
- **Trạng thái ban đầu:** Công ty Sao Biển có tổng cộng **`1.000.000 cổ phần`**. Bạn đang nắm giữ `10.000 cổ phần`.
  - **Bước 1 — Tính tỷ lệ sở hữu ban đầu của bạn:**
    $$\text{Tỷ lệ sở hữu ban đầu} = \frac{10.000\text{ cổ phần}}{1.000.000\text{ cổ phần}} = 0,01 = 1\%$$
- **Sự kiện 1 (Phát hành cổ phần mới — Thị trường sơ cấp):** Để mở chi nhánh mới, Công ty Sao Biển phát hành thêm **`100.000 cổ phần mới`** giá **`20.000 đồng/cổ phần`** (giả sử chi phí phát hành bằng 0). Bạn không mua thêm trong đợt này, còn các nhà đầu tư khác mua hết `100.000 cổ phần mới`.
  - **Bước 2 — Tiền đi về đâu?** `PHÉP_TÍNH` Vì đây là cổ phần mới do công ty phát hành, **két tiền của Công ty Sao Biển nhận thêm**:
    $$\text{Tiền vào công ty} = 100.000\text{ cổ phần} \times 20.000\text{ đồng/cổ phần} = 2.000.000.000\text{ đồng}\text{ (2 tỷ đồng)}$$
  - **Bước 3 — Tổng số cổ phần và tỷ lệ sở hữu thay đổi thế nào?** Tổng số cổ phần của công ty tăng lên:
    $$\text{Tổng số cổ phần mới} = 1.000.000 + 100.000 = 1.100.000\text{ cổ phần}$$
    Vì bạn vẫn giữ `10.000 cổ phần` trên một chiếc bánh có nhiều phần hơn, tỷ lệ sở hữu của bạn trở thành:
    $$\text{Tỷ lệ sở hữu mới} = \frac{10.000}{1.100.000} \approx 0,00909 \text{ (khoảng } 0,909\%\text{)}$$
    Việc tỷ lệ sở hữu giảm từ `1%` xuống `0,909%` khi công ty phát hành thêm cổ phần mới mà bạn không mua thêm gọi là **pha loãng tỷ lệ sở hữu (`ownership dilution`)**.
  - *Trực giác quan trọng (`SUY_LUẬN`):* Tỷ lệ sở hữu giảm từ `1%` xuống `0,909%` **không có nghĩa là bạn tự động mất tiền!** Đổi lại, két của Công ty Sao Biển có thêm **2 tỷ đồng tiền mặt mới**. Trước phát hành, bạn sở hữu `1%` công ty cũ; sau phát hành, bạn sở hữu `0,909%` của một công ty lớn hơn (công ty cũ + 2 tỷ đồng tiền mặt mới). Bạn chỉ thiệt nếu công ty bán cổ phần mới giá quá rẻ hoặc đem 2 tỷ đó đi đầu tư thua lỗ (học ở **[Bài 006](006-capital-allocation-governance.md)** và **[Bài Q2](Q2-sbc-dilution-buybacks-dividends.md)**).

- **Sự kiện 2 (Mua bán lại trên sàn — Thị trường thứ cấp):** Hôm sau, chị Lan lên sàn đặt lệnh mua lại **`100 cổ phần`** đã phát hành từ anh Minh (cổ đông cũ) với giá **`20.000 đồng/cổ phần`**.
  - **Bước 4 — Tiền đi về đâu?** `PHÉP_TÍNH` Chị Lan trả `100 × 20.000 = 2.000.000 đồng` (`2 triệu đồng`). Số tiền này (trừ phí môi giới nhỏ) **chảy vào tài khoản cá nhân của anh Minh**. Công ty Sao Biển nhận **`0 đồng`**, và tổng số cổ phần của công ty vẫn là `1.100.000 cổ phần` (chỉ đổi tên chủ của 100 cổ phần từ Minh sang Lan).

### 2.3. Khi một đợt chào bán có cả cổ phần mới lẫn cổ phần cũ

`SỰ_THẬT` Theo hướng dẫn về chào bán cổ phiếu lần đầu ra công chúng (IPO) của [SEC — Investor Bulletin: Investing in an IPO (14/10/2022)](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-17), một đợt chào bán có thể gồm cả cổ phần mới do công ty phát hành và cổ phần cũ do cổ đông hiện hữu bán bớt; công ty không nhận tiền từ phần cổ phần do cổ đông hiện hữu bán ra.

`KỊCH_BẢN` Trong một đợt chào bán giá **`10.000 đồng/cổ phần`**:
- Công ty phát hành **`200.000 cổ phần mới`** để huy động vốn;
- Một cổ đông sáng lập bán bớt **`50.000 cổ phần cũ`** của cá nhân mình.
- Chi phí tổ chức phát hành do công ty chịu là **`100.000.000 đồng`** (`100 triệu đồng`), người bán cổ phần cũ giả sử không chịu phí.

Hãy tính từng bước:
- **Bước 1 — Tổng tiền người mua bỏ ra:** `(200.000 + 50.000) × 10.000 = 2.500.000.000 đồng` (`2,5 tỷ đồng`).
- **Bước 2 — Tiền vào túi cổ đông cũ bán bớt cổ phần:** `50.000 × 10.000 = 500.000.000 đồng` (`0,5 tỷ đồng`).
- **Bước 3 — Tiền ròng thực tế chảy vào két công ty:**
  $$\text{Tiền gộp từ cổ phần mới} = 200.000 \times 10.000 = 2.000.000.000\text{ đồng (2,0 tỷ đồng)}$$
  $$\text{Tiền ròng công ty thực nhận} = 2.000.000.000 - 100.000.000 = 1.900.000.000\text{ đồng (1,9 tỷ đồng)}$$
- **Bước 4 — Số cổ phần tăng thêm của công ty:** Chỉ tăng thêm đúng **`200.000 cổ phần mới`**.

> **Điểm dừng Phiên 2:** Trong 2,5 tỷ đồng người mua trả ở ví dụ trên, bao nhiêu tiền vào két công ty, bao nhiêu vào túi cổ đông cũ, và bao nhiêu trả chi phí phát hành?

---

## Phiên 3 — Đọc bảng giá, Sổ lệnh và Quy mô thực của doanh nghiệp

### 3.1. Ba con số trên bảng giá: Giá chào mua, Giá chào bán và Giá khớp gần nhất

Khi đi chợ mua cam, có 3 mức giá khác nhau:
1. **Giá người bán đang đòi** (ví dụ `20.100 đồng/kg`): Trên sàn gọi là **Giá chào bán (`Ask / Offer price`)** — mức giá thấp nhất mà người có cổ phiếu sẵn sàng bán ra ngay lúc đó.
2. **Giá người mua đang trả** (ví dụ `19.900 đồng/kg`): Trên sàn gọi là **Giá chào mua (`Bid price`)** — mức giá cao nhất mà người muốn mua sẵn sàng trả ngay lúc đó.
3. **Giá giao dịch vừa xong trước đó 5 phút** (`20.000 đồng/kg`): Trên sàn gọi là **Giá khớp gần nhất (`Last price`)**.

`SỰ_THẬT` Theo hướng dẫn của [SEC — Investor.gov: Types of Orders](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders) và [Bid/Ask Glossary](https://www.investor.gov/introduction-investing/investing-basics/glossary/ask-price):
- Khoảng cách giữa giá chào bán thấp nhất và giá chào mua cao nhất gọi là **chênh lệch giá mua–bán (`Bid-Ask Spread`)** (`20.100 − 19.900 = 200 đồng`).
- **Giá khớp gần nhất (`20.000 đồng`) là chuyện của quá khứ**, không bảo đảm lệnh mua tiếp theo sẽ khớp ở giá `20.000 đồng`.
- Hai loại lệnh cơ bản:
  - **Lệnh thị trường (`Market Order`):** Ra lệnh *"Mua/bán ngay theo các mức giá đang chào tốt nhất trên sàn"*. Ưu điểm là khớp nhanh, nhưng **không kiểm soát được giá khớp** nếu sổ lệnh mỏng.
  - **Lệnh giới hạn (`Limit Order`):** Ra lệnh *"Chỉ mua với giá tối đa là X (hoặc chỉ bán với giá tối thiểu là Y)"*. Ưu điểm là **kiểm soát chặt mức giá**, nhưng **không bảo đảm khớp hết khối lượng** nếu không có người đối ứng ở giá đó.

### 3.2. Tính từng bước trên một Sổ lệnh (`Order Book`)

`KỊCH_BẢN` Tại thời điểm bạn nhìn màn hình, sổ lệnh chờ của cổ phiếu Sao Biển như sau:
- **Bên chào mua (`Bid`):** Cao nhất đang chờ mua `500 cổ phần` giá `19.900 đồng`.
- **Bên chào bán (`Ask`):**
  - Mức bán 1 (rẻ nhất đang chờ bán): **`300 cổ phần`** ở giá **`20.100 đồng`**.
  - Mức bán 2 (kế tiếp): **`100 cổ phần`** ở giá **`20.300 đồng`**.
- **Giá khớp gần nhất** trên màn hình: `20.000 đồng`.

Bạn cần mua ngay **`400 cổ phần`** (giả sử chưa có lệnh mới chen vào):
- **Trường hợp 1 — Đặt lệnh mua quét hết 400 cổ phần đang chào bán:**
  - **Bước 1:** Lấy hết `300 cổ phần` ở mức rẻ nhất `20.100 đồng` → `300 × 20.100 = 6.030.000 đồng`.
  - **Bước 2:** Còn thiếu `400 − 300 = 100 cổ phần`, lệnh leo lên mức bán kế tiếp `20.300 đồng` → `100 × 20.300 = 2.030.000 đồng`.
  - **Bước 3 — Tổng tiền và Giá mua bình quân (`PHÉP_TÍNH`):**
    $$\text{Tổng tiền mua} = 6.030.000 + 2.030.000 = 8.060.000\text{ đồng}$$
    $$\text{Giá mua bình quân} = \frac{8.060.000\text{ đồng}}{400\text{ cổ phần}} = 20.150\text{ đồng/cổ phần}$$
    `SỰ_THẬT` Khả năng mua/bán nhanh một lượng chứng khoán mà không làm giá biến động mạnh gọi là **thanh khoản (`liquidity`)** ([SEC — Liquidity](https://www.investor.gov/introduction-investing/investing-basics/glossary/liquidity-or-marketability)).
- **Trường hợp 2 — Đặt Lệnh giới hạn (`Limit Order`) mua 400 cổ phần giá tối đa `20.100 đồng`:**
  - Chỉ khớp được **`300 cổ phần`** ở giá `20.100 đồng`, còn **`100 cổ phần` chưa khớp** nằm chờ (vì hệ thống không được vượt trần `20.100 đồng` bạn đã đặt).

### 3.3. Từ giá 1 cổ phiếu đến Vốn hóa thị trường và Giá trị doanh nghiệp (`EV`)

Khi mua bánh pizza, quán A bán 1 miếng `12.500 đồng` (cắt bánh thành 80 miếng nhỏ) và quán B bán 1 miếng `100.000 đồng` (cắt bánh thành 8 miếng lớn). Muốn so giá cả chiếc bánh, phải nhân giá 1 miếng với tổng số miếng!

1. **Vốn hóa thị trường (`Market Capitalization` — Giá mua toàn bộ phần vốn chủ sở hữu):**
   $$\text{Vốn hóa thị trường} = \text{Giá thị trường của 1 cổ phần} \times \text{Tổng số cổ phần đang lưu hành}$$
   - `KỊCH_BẢN` **Công ty Mộc** có **`80.000.000 cổ phần`** (`80 triệu cổ phần`) đang lưu hành, thị giá **`12.500 đồng/cổ phần`**.
   - `PHÉP_TÍNH` Vốn hóa thị trường của Công ty Mộc = `80.000.000 × 12.500 = 1.000.000.000.000 đồng` (**`1.000 tỷ đồng`**).
   - Nếu ngày mai thị giá tăng lên `15.000 đồng`, vốn hóa tăng lên `1.200 tỷ đồng`. Khoản tăng `200 tỷ đồng` này là mức định giá trên sàn giữa các nhà đầu tư, **không phải 200 tỷ đồng tiền mặt mới chảy vào két Công ty Mộc**.

2. **Giá trị doanh nghiệp giản lược (`Enterprise Value — EV` — Tổng giá tiền thực sự để mua đứt cả công ty):**
   Nếu bạn mua đứt 100% Công ty Mộc: ngoài việc trả **`1.000 tỷ đồng`** cho các cổ đông (Vốn hóa), bạn phải **gánh luôn khoản nợ vay `400 tỷ đồng`** của công ty (`+ Nợ vay`), nhưng đồng thời **được nhận luôn `150 tỷ đồng` tiền mặt** có sẵn trong két công ty (`− Tiền mặt`).
   - `PHÉP_TÍNH` Số tiền ròng thực sự để mua toàn bộ hoạt động kinh doanh của Công ty Mộc trong mô hình 3 thành phần giản lược là:
     $$\text{EV giản lược} = \text{Vốn hóa thị trường} + \text{Nợ vay} - \text{Tiền mặt} = 1.000 + 400 - 150 = 1.250\text{ tỷ đồng}$$
   - `SỰ_THẬT` Theo Viện CFA ([CFA Institute — Market-based Valuation](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/market-based-valuation-price-enterprise-value-multiples)), công thức `EV` đầy đủ còn cộng thêm cổ phiếu ưu đãi, lợi ích cổ đông không kiểm soát và xử lý nghĩa vụ nợ thuê, tiền mặt hạn chế sử dụng (học ở **[Bài 009](009-valuation-multiples.md)**).

> **Điểm dừng Phiên 3:** Công ty X có giá cổ phiếu `5.000 đồng` với `1 tỷ cổ phần` (`Vốn hóa = 5.000 tỷ`); Công ty Y có giá cổ phiếu `100.000 đồng` với `10 triệu cổ phần` (`Vốn hóa = 1.000 tỷ`). Công ty nào đang được thị trường định giá tổng vốn chủ cao gấp 5 lần công ty kia?

---

## Ví dụ từ nguồn thật

Hãy mở trang bìa báo cáo thường niên **Form 10-K năm tài chính 2025 (`FY2025`) của Apple Inc.** nộp cho Ủy ban Chứng khoán Hoa Kỳ (`SEC`):
- `SỰ_THẬT` Trên trang bìa [Apple Inc. Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) (kỳ năm tài chính kết thúc ngày `27/09/2025`, nộp ngày `31/10/2025`, chuẩn `US GAAP`, đơn vị `USD`), Apple công bố: tính đến ngày **`17/10/2025`**, công ty có **`14.776.353.000` cổ phần phổ thông** đã phát hành và đang lưu hành (`issued and outstanding`).
- **Chú ý hai ngày khác nhau:** Kỳ kế toán `FY2025` kết thúc ngày `27/09/2025`, nhưng số cổ phần đang lưu hành trên trang bìa được chốt tại ngày `17/10/2025`.
- `KỊCH_BẢN` Đặt mức giá giả định để luyện tính là **`250 USD/cổ phần`** (số giả định phục vụ bài học, không phải giá đóng cửa đã xác minh ngày 17/10/2025).
- `PHÉP_TÍNH` Nhân giá 1 cổ phần với tổng số cổ phần đang lưu hành:
  $$\text{Vốn hóa giả định} = 250\text{ USD} \times 14.776.353.000\text{ cổ phần} = 3.694.088.250.000\text{ USD}\text{ (xấp xỉ } 3.694,1\text{ tỷ USD)}$$
- **Quy tắc thực hành:** Khi tính vốn hóa tại một ngày, luôn lấy **số cổ phần đang lưu hành tại thời điểm đó**, không lấy "số cổ phần bình quân trong kỳ" (vốn dùng để tính `EPS` ở **[Bài N2](N2-statement-line-items.md)**).

---

## Năm câu hỏi khi đọc

1. **Vị thế pháp lý:** Tôi đang góp vốn làm đồng chủ sở hữu (cổ đông) hay đang cho vay theo hợp đồng (chủ nợ)?
2. **Đường đi của tiền:** Tiền tôi bỏ ra chảy vào két doanh nghiệp (phát hành mới) hay chảy vào túi người bán lại trên sàn (thứ cấp)?
3. **Tổng số cổ phần:** Tổng số cổ phần công ty có tăng thêm làm pha loãng tỷ lệ sở hữu không, và công ty dùng tiền mới vào việc gì?
4. **Bảng giá và sổ lệnh:** Con số đang nhìn là giá khớp cũ, giá chào mua hay giá chào bán, và khối lượng chờ có đủ cho lệnh của tôi không?
5. **Quy mô toàn doanh nghiệp:** Tổng vốn hóa thị trường và nợ vay của doanh nghiệp là bao nhiêu, thay vì chỉ nhìn thị giá 1 cổ phiếu lẻ?

---

## Bài tập — làm trước khi mở đáp án

1. Công ty phát hành `200.000 cổ phần mới` với giá `10.000 đồng/cổ phần`. Hỏi công ty nhận được bao nhiêu tiền trước khi trừ chi phí phát hành?
2. Chị Lan bán `200 cổ phần cũ` (đã phát hành từ năm trước) cho anh Bình với giá `15.000 đồng/cổ phần`. Ai nhận số tiền `3.000.000 đồng` này (trước phí giao dịch), và công ty nhận được bao nhiêu?
3. Trên màn hình hiện "Giá khớp gần nhất: `20.000 đồng`". Con số này có bảo đảm lệnh mua tiếp theo của bạn chắc chắn mua được ở giá `20.000 đồng` không? Vì sao?
4. Bạn đang nắm `10.000 cổ phần` trên tổng số `1.000.000 cổ phần`. Công ty phát hành thêm `1.000.000 cổ phần mới` và bạn không mua thêm. Tỷ lệ sở hữu của bạn thay đổi từ bao nhiêu % xuống bao nhiêu %?
5. Một công ty năm nay thông báo **không chia cổ tức tiền mặt**. Điều đó có tự động chứng minh công ty đang thua lỗ hoặc sắp phá sản không?
6. Vì sao một cổ phiếu có giá `5.000 đồng/cổ phần` chưa chắc đã "rẻ hơn" một cổ phiếu có giá `100.000 đồng/cổ phần`?
7. Công ty Mộc có `80 triệu cổ phần` đang lưu hành, thị giá `12.500 đồng/cổ phần`, tổng nợ vay `400 tỷ đồng`, tiền mặt `150 tỷ đồng`. Hãy tính từng bước **Vốn hóa thị trường** và **Giá trị doanh nghiệp giản lược (`EV`)** theo đơn vị tỷ đồng, đồng thời nêu các khoản mục chưa xét tới trong công thức giản lược này.
8. Trong một đợt chào bán giá `10.000 đồng/cổ phần`, công ty phát hành `200.000 cổ phần mới` và một cổ đông lớn bán ra `50.000 cổ phần cũ`. Chi phí phát hành do công ty chịu là `100 triệu đồng` (người bán cổ phần cũ không chịu phí). Tính tổng tiền người mua trả, tiền ròng vào công ty và tiền vào cổ đông cũ.
9. Sổ lệnh bên bán đang có `300 cổ phần` chào giá `20.100 đồng` và `100 cổ phần` chào giá `20.300 đồng`. Nếu bạn đặt lệnh mua ngay `400 cổ phần` (giả định sổ lệnh không đổi), tổng tiền phải trả và giá mua bình quân mỗi cổ phần là bao nhiêu? Nếu bạn đặt **lệnh giới hạn mua** ở mức `20.100 đồng` cho `400 cổ phần` thì sao?
10. Một trang web lấy `47 triệu cổ phần bình quân pha loãng` trong năm, trang khác lấy `50 triệu cổ phần đang lưu hành` cuối quý, rồi nhân với giá `20.000 đồng` (không ghi ngày của giá) để công bố vốn hóa. Hãy chỉ ra những dữ kiện nào đang thiếu hoặc ghép sai quy tắc.

## Đáp án và giải thích từng bước

<details>
<summary>Mở sau khi tự làm</summary>

1. **Câu 1 (`PHÉP_TÍNH`):** Phát hành mới trên thị trường sơ cấp nên tiền vào công ty: `200.000 × 10.000 = 2.000.000.000 đồng` (`2 tỷ đồng`).
2. **Câu 2 (`SỰ_THẬT`):** Giao dịch thứ cấp giữa hai nhà đầu tư: chị Lan nhận `200 × 15.000 = 3.000.000 đồng` (trước phí/thuế); công ty nhận **`0 đồng`**.
3. **Câu 3 (`SỰ_THẬT`):** **Không bảo đảm.** Giá khớp `20.000 đồng` là giao dịch đã xong trong quá khứ. Lệnh mua mới phụ thuộc vào giá chào bán (`Ask`) và khối lượng đang chờ trên sổ lệnh hiện tại.
4. **Câu 4 (`PHÉP_TÍNH`):** Tỷ lệ ban đầu = `10.000 / 1.000.000 = 1,0%`. Sau khi phát hành thêm 1 triệu cổ phần mới, tổng số cổ phần là `2.000.000`, nên tỷ lệ sở hữu mới = `10.000 / 2.000.000 = 0,5%`.
5. **Câu 5 (`SUY_LUẬN`):** **Không.** Cổ tức không phải nghĩa vụ bắt buộc hàng năm. Công ty có lãi cao vẫn có thể giữ lại lợi nhuận để tái đầu tư mở rộng kinh doanh. Muốn biết công ty khỏe hay yếu phải đọc báo cáo tài chính ở **[Bài 001](001-business-financial-statements.md)**.
6. **Câu 6 (`SUY_LUẬN`):** Giá 1 cổ phần chỉ là giá của một lát cắt. Nếu công ty giá `5.000 đồng` có `1 tỷ cổ phần` thì vốn hóa là `5.000 tỷ đồng`; công ty giá `100.000 đồng` có `10 triệu cổ phần` thì vốn hóa chỉ là `1.000 tỷ đồng`. Đắt hay rẻ còn phụ thuộc vào lợi nhuận, dòng tiền và nợ vay (học ở **[Bài 002](002-finding-a-cheap-stock.md)**).
7. **Câu 7 (`PHÉP_TÍNH`):**
   - **Vốn hóa thị trường:** `80.000.000 × 12.500 = 1.000.000.000.000 đồng = 1.000 tỷ đồng`.
   - **Giá trị doanh nghiệp giản lược (`EV`):** `1.000 + 400 − 150 = 1.250 tỷ đồng`.
   - **Khoản chưa xét tới:** Cổ phiếu ưu đãi, lợi ích cổ đông không kiểm soát, nghĩa vụ nợ thuê tài sản, tiền mặt bị phong tỏa/hạn chế sử dụng.
8. **Câu 8 (`PHÉP_TÍNH`):**
   - Tổng tiền người mua trả: `(200.000 + 50.000) × 10.000 = 2,5 tỷ đồng`.
   - Tiền vào túi cổ đông cũ: `50.000 × 10.000 = 0,5 tỷ đồng`.
   - Tiền ròng vào két công ty: `(200.000 × 10.000) − 100.000.000 = 2,0 tỷ − 0,1 tỷ = 1,9 tỷ đồng`.
9. **Câu 9 (`PHÉP_TÍNH`):**
   - Mua khớp hết 400 cổ phần: Tổng tiền = `(300 × 20.100) + (100 × 20.300) = 6.030.000 + 2.030.000 = 8.060.000 đồng`; Giá mua bình quân = `8.060.000 / 400 = 20.150 đồng/cổ phần`.
   - Đặt **lệnh giới hạn mua giá `20.100 đồng`**: khớp được **`300 cổ phần`** (`6.030.000 đồng`), còn **`100 cổ phần` chưa khớp** nằm chờ vì lô bán kế tiếp (`20.300 đồng`) vượt trần giá giới hạn.
10. **Câu 10 (`SUY_LUẬN`):** Ba lỗi cần sửa: (1) Không dùng "cổ phần bình quân pha loãng trong kỳ" (`47 triệu`) để tính vốn hóa tại một thời điểm; (2) Giá `20.000 đồng` thiếu ngày chốt nên không rõ có cùng thời điểm với số cổ phần không; (3) Cần kiểm tra xem giữa ngày khóa sổ quý và ngày lấy giá có đợt phát hành/mua cổ phiếu quỹ nào không.

</details>

---

## Bài làm với dữ liệu thiếu hoặc lệch

`KỊCH_BẢN` Bạn thấy ảnh chụp màn hình ghi giá cổ phiếu `20.000 đồng` (bị cắt mất ngày giờ). Báo cáo quý gần nhất ghi công ty có `100 triệu cổ phần` đang lưu hành cuối quý, kèm thông báo "Dự kiến phát hành thêm `5 triệu cổ phần mới`" nhưng không ghi ngày hoàn tất. Người A lấy `105 triệu × 20.000 = 2.100 tỷ đồng`; người B lấy `100 triệu × 20.000 = 2.000 tỷ đồng`.

**Cách phát hiện và xử lý chuẩn:**
1. **Chỉ ra dữ kiện đang thiếu:** Ngày của mức giá `20.000 đồng` là `CHƯA_BIẾT`; đợt phát hành `5 triệu cổ phần` đã hoàn tất lưu hành tại ngày lấy giá hay mới là kế hoạch cũng là `CHƯA_BIẾT`.
2. **Cách xử lý đúng quy tắc nghiên cứu:** Không đoán mò. Phải mở thông báo kết quả đợt phát hành và tra giá đóng cửa tại đúng ngày xác định. Khi chưa đủ dữ kiện, chỉ ghi hai kịch bản có điều kiện: *"Với giá giả định 20.000 đồng, vốn hóa trên 100 triệu cổ phần trước phát hành là 2.000 tỷ đồng; trên 105 triệu cổ phần sau phát hành là 2.100 tỷ đồng (chênh lệch 100 tỷ đồng do mẫu số cổ phần)."*

---

## Sai ở đâu

> *"Hôm nay giá cổ phiếu Công ty Mộc tăng 20%, giúp vốn hóa tăng thêm 200 tỷ đồng, vậy là Công ty Mộc vừa có thêm 200 tỷ đồng tiền mặt trong két để trả nợ ngân hàng! Hơn nữa, chiều nay tôi vừa mua 1.000 cổ phiếu Mộc từ chị Lan trên sàn, tức là tôi vừa góp thêm vốn mới giúp công ty mở rộng nhà máy."*

**Phân tích lỗi sai:**
1. **Nhầm biến động vốn hóa trên sàn với tiền mặt trong két công ty:** Giá cổ phiếu tăng làm tổng giá trị thị trường của các cổ phần tăng thêm 200 tỷ đồng, nhưng đó là đánh giá giữa các nhà đầu tư trên sàn. Công ty Mộc **không nhận thêm đồng tiền mặt nào** từ biến động giá thứ cấp để đem đi trả nợ.
2. **Nhầm giao dịch thứ cấp với phát hành sơ cấp:** Mua 1.000 cổ phiếu từ chị Lan trên sàn thì tiền chảy vào tài khoản chị Lan. Công ty Mộc chỉ nhận vốn mới khi phát hành cổ phiếu mới (sơ cấp).

---

## Kiểm tra chuyển bài

Trước khi chuyển sang bài kế tiếp, hãy tự trả lời 3 câu hỏi sau:
1. Một đợt chào bán gồm `500.000 cổ phần mới` do công ty phát hành và `25.000 cổ phần cũ` do cổ đông hiện hữu bán ra, cùng giá `8.000 đồng/cổ phần`. Trước khi trừ chi phí, công ty nhận bao nhiêu tiền và cổ đông bán nhận bao nhiêu tiền?
2. Một công ty có vốn hóa thị trường `4.000 tỷ đồng`, tổng nợ vay `900 tỷ đồng` và tiền mặt `600 tỷ đồng`. Hãy tính `EV giản lược` và nêu hai khoản mục có thể còn thiếu nếu phân tích sâu hơn.
3. Bạn đặt **lệnh mua giới hạn (`Limit Order`)** `100 cổ phần` giá tối đa `15.000 đồng/cổ phần`, nhưng sổ lệnh chỉ có `40 cổ phần` đang chào bán ở giá `15.000 đồng` (các lô còn lại chào `15.200 đồng`). Vì sao `60 cổ phần` còn lại chưa khớp?

- **Tiêu chí đạt:** Câu 1: Công ty nhận `4 tỷ đồng`, cổ đông bán nhận `200 triệu đồng`. Câu 2: `EV giản lược = 4.000 + 900 − 600 = 4.300 tỷ đồng` (thiếu cổ phiếu ưu đãi, lợi ích cổ đông không kiểm soát, nợ thuê, tiền mặt hạn chế sử dụng). Câu 3: Lệnh giới hạn khóa trần mua ở `15.000 đồng` nên không mua lô `15.200 đồng`.
- **Điểm đến tiếp theo:** Mở ngay **[Bài N6 — Doanh nghiệp kiếm tiền thế nào?](N6-business-model-unit-economics.md)** (Bước 2/23 của Nhánh 1) để xem Quán cà phê Sao Biển kiếm lời từ mỗi ly cà phê ra sao!

---

## Mô hình thực hành

Chạy và kiểm tra toàn bộ phép tính trong bài bằng [`practice/models/market_returns.py`](../practice/models/market_returns.py) (các hàm `issuance`, `ownership`, `market_cap`, `enterprise_value`, `book_fill`):
- Chạy mô hình: `python3 learning/practice/models/market_returns.py`
- Kiểm thử: `python3 -m unittest tests/test_market_returns.py`

## Lỗi thường gặp

- Tưởng rằng bấm nút mua cổ phiếu trên sàn là tiền của mình chảy vào két công ty.
- Tưởng cổ tức là tiền lãi cố định bắt buộc phải trả hàng năm như tiết kiệm ngân hàng.
- Nhìn "giá khớp gần nhất" rồi đinh ninh lệnh mua số lượng lớn tiếp theo cũng khớp đúng giá đó.
- Nhìn giá 1 cổ phiếu `5.000 đồng` rồi khen "rẻ" mà không nhân với tổng số cổ phần và cộng nợ vay ròng.

## Ranh giới an toàn

- Bài học cung cấp kiến thức nền tảng về vận hành thị trường, **không phải** khuyến nghị mua, bán hay nắm giữ chứng khoán.
- Mọi con số của Quán Sao Biển, Công ty Mộc và giá giả định 250 USD của Apple được gắn nhãn `KỊCH_BẢN` để rèn kỹ năng tính toán, không phải dữ liệu giá thị trường hiện hành.

## Điều tôi vẫn chưa hiểu

- Cổ phần phổ thông khác cổ phần ưu đãi ở những quyền lợi cụ thể nào trên báo cáo thực tế?
- Khi doanh nghiệp đã có vốn, doanh nghiệp bán hàng mỗi ngày thế nào để tạo ra lợi nhuận và tiền mặt? *(Xem ngay **[Bài N6 — Doanh nghiệp kiếm tiền thế nào?](N6-business-model-unit-economics.md)**).*

## Nguồn Internet đã mở

| Nguồn | Kỳ / Phiên bản & Phạm vi | Nội dung xác minh dùng trong bài |
|---|---|---|
| [Investor.gov (SEC) — Stocks](https://www.investor.gov/introduction-investing/investing-basics/investment-products/stocks) | Hoa Kỳ; trang chính thức của SEC, mở kiểm chứng `2026-11-06` | Cổ phiếu là quyền sở hữu một phần công ty; cổ tức không được bảo đảm; cổ đông nhận tài sản sau chủ nợ khi thanh lý |
| [Investor.gov (SEC) — Bonds](https://www.investor.gov/introduction-investing/investing-basics/investment-products/bonds-or-fixed-income-products/bonds) | Hoa Kỳ; trang chính thức của SEC, mở kiểm chứng `2026-11-06` | Trái phiếu là khoản vay nợ, nghĩa vụ trả lãi/gốc và rủi ro vỡ nợ |
| [Investor.gov (SEC) — Glossary (Primary Market, Secondary Market, Ask Price, Liquidity)](https://www.investor.gov/introduction-investing/investing-basics/glossary) | Hoa Kỳ; trang chính thức của SEC, mở kiểm chứng `2026-11-06` | Phân biệt thị trường sơ cấp và thứ cấp; giá chào mua/bán và thanh khoản |
| [Investor.gov (SEC) — Types of Orders](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders) | Hoa Kỳ; trang chính thức của SEC, mở kiểm chứng `2026-11-06` | Cơ chế lệnh thị trường (`Market Order`) và lệnh giới hạn (`Limit Order`) |
| [Investor.gov (SEC) — Investor Bulletin: Investing in an IPO](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-17) | Xuất bản `14/10/2022`; Hoa Kỳ; mở kiểm chứng `2026-11-06` | Phân biệt tiền thu từ cổ phần mới phát hành và cổ phần do cổ đông hiện hữu bán ra |
| [SIFMA — Capital Markets Primer (PDF)](https://www.sifma.org/wp-content/uploads/2024/09/SIFMA-Insights-Primer_Capital-Markets_FINAL.pdf) | Tháng `09/2024`; thị trường vốn Hoa Kỳ | Vai trò huy động vốn của thị trường sơ cấp và thanh khoản của thị trường thứ cấp |
| [CFA Institute — Market-based Valuation: Price and Enterprise Value Multiples](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/market-based-valuation-price-enterprise-value-multiples) | Khung phân tích toàn cầu, truy cập `02/11/2026` | Thành phần đầy đủ của Giá trị doanh nghiệp (`Enterprise Value — EV`) |
| [Apple Inc. — Form 10-K FY2025 (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Năm tài chính kết thúc `27/09/2025`; nộp `31/10/2025`; `USD`; `US GAAP`; mở kiểm chứng `2026-11-06` | Trang bìa: `14.776.353.000` cổ phần phổ thông đang lưu hành tại ngày `17/10/2025` |
