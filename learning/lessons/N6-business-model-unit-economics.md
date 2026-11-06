# Bài N6 — Doanh nghiệp kiếm tiền thế nào? Mô hình kinh doanh, kinh tế đơn vị và điểm hòa vốn

- Ngày cập nhật: `2026-11-06`
- Chốt dữ liệu lúc: `2026-11-06 10:05 UTC+7 (Asia/Ho_Chi_Minh)`
- Bậc chiều sâu: `Bậc S`
- Lộ trình đọc: **Bài 2 / 23 của Nhánh 1 (Hiểu doanh nghiệp & Phân tích cổ phiếu)**.
  - **Bài trước liên quan:** **[Bài N1 — Thị trường chứng khoán vận hành thế nào?](N1-market-basics.md)** (Bước 1/23).
  - **Học tiếp theo đúng thứ tự:** **[Bài 001 — Một doanh nghiệp đi qua ba báo cáo tài chính](001-business-financial-statements.md)** (Bước 3/23).
- Mục tiêu: Trả lời được 6 câu hỏi giải phẫu một mô hình kinh doanh; tách bạch chi phí biến đổi theo từng sản phẩm (**biến phí**) với chi phí cố định hàng tháng (**định phí**); tính từng bước **phần đóng góp (`contribution margin`)** và **điểm hòa vốn (`break-even point`)**; hiểu vì sao giảm giá bán 10% có thể làm lợi nhuận sụt giảm mạnh hơn rất nhiều, và vì sao quán đông khách có lãi trên giấy nhưng trong két vẫn cạn tiền mặt.
- Thời lượng: Ba phiên học ngắn (khoảng 30–35 phút/phiên) có điểm dừng; thực hành cùng [`practice/models/market_returns.py`](../practice/models/market_returns.py).
- Câu hỏi cốt lõi: **Khi một cửa hàng bán thêm được một sản phẩm, cửa hàng đó thực sự bỏ túi thêm bao nhiêu đồng để bù tiền thuê mặt bằng — và cần bán bao nhiêu sản phẩm thì bắt đầu có lãi?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

---

## Hiểu bài này trong 1 phút

Đi ngang qua một quán cà phê thấy khách ngồi chật kín bàn, nhiều người vội kết luận: *"Quán này chắc chắn lãi to!"* Nhưng thực tế, **đông khách chưa chắc đã có lãi, và có lãi trên sổ sách cũng chưa chắc đã có tiền mặt trong két.**

Muốn biết **Quán cà phê Sao Biển** kiếm tiền thật hay đang "lấy công làm lời", bạn phải nhìn qua 3 lớp kính:
1. **Lớp 1 — Trên từng ly cà phê lẻ (Kinh tế đơn vị — `Unit Economics`):** Bán 1 ly thu `50.000 đồng`, mất ngay `30.000 đồng` tiền hạt cà phê, sữa, đá, ly nhựa. Mỗi ly chỉ để lại **`20.000 đồng`** (**phần đóng góp**) để phụ trả tiền thuê nhà và lương nhân viên.
2. **Lớp 2 — Trên cả tháng vận hành (Điểm hòa vốn — `Break-even Point`):** Nếu tiền thuê mặt bằng và lương cố định là `120 triệu đồng/tháng`, quán phải bán đủ `120.000.000 / 20.000 = 6.000 ly` mới vừa đủ bù định phí. Từ ly thứ `6.001` trở đi mới bắt đầu có lãi.
3. **Lớp 3 — Thời điểm thu tiền mặt:** Dù tháng này bán `7.000 ly` (lãi `20 triệu đồng` trên giấy), nhưng nếu khách đặt tiệc hẹn tháng sau mới trả tiền trong khi tiền sữa và tiền thuê nhà phải trả ngay hôm nay, thì két tiền của quán vẫn trống rỗng!

---

## Ôn bài cũ hoặc kiểm tra đầu vào

Ôn lại 2 điểm cốt lõi từ **[Bài N1 — Thị trường chứng khoán vận hành thế nào?](N1-market-basics.md)**:
1. **Câu hỏi 1 (từ [Bài N1](N1-market-basics.md)):** Khi chị Lan mua lại 100 cổ phần cũ của Quán Sao Biển từ anh Minh trên sàn, anh Minh nhận tiền, còn Quán Sao Biển không nhận đồng nào. Ngay cả khi quán phát hành cổ phần mới nhận 2 tỷ đồng, thì đó là **vốn góp của chủ sở hữu**, khác hoàn toàn với **doanh thu bán cà phê**.
2. **Câu hỏi 2 (cầu nối sang Bài N6):** Một sản phẩm ngon chưa tự động tạo ra doanh nghiệp kiếm tiền tốt — muốn kiểm tra, ta phải bước vào bếp và quầy thu ngân để tính **kinh tế đơn vị** và **điểm hòa vốn**.

## Bài này làm gì và chưa làm gì

| Bài này làm | Bài này chưa làm |
|---|---|
| Đặt 6 câu hỏi nền tảng để hiểu doanh nghiệp kiếm tiền bằng cách nào | Chưa dạy lập 3 báo cáo tài chính (học ngay ở [Bài 001](001-business-financial-statements.md)) |
| Tách biến phí, định phí, tính phần đóng góp và điểm hòa vốn từng bước | Chưa đi vào chu kỳ công suất ngành nặng ([Bài 014](014-industry-capital-cycle.md), [Bài F5](F5-vietnam-industry-research-framework.md)) |
| Chỉ ra độ nhạy khi giảm giá bán và sự khác biệt giữa lãi với tiền mặt | Không coi công thức một sản phẩm là khuôn mẫu cứng nhắc cho tập đoàn đa ngành |

---

## Phiên 1 — Giải phẫu một ly cà phê: Biến phí, Định phí và Điểm hòa vốn

### 1.1. Sáu câu hỏi để hiểu một mô hình kinh doanh

`Ý_KIẾN` Trước khi nhìn vào bất kỳ bảng số liệu hay tỷ số tài chính phức tạp nào, hãy tập thói quen lấy một tờ giấy trắng và trả lời 6 câu hỏi đời thường sau về doanh nghiệp bạn đang tìm hiểu:
1. **Khách hàng là ai?** (Người đi làm mua cà phê sáng mang đi, sinh viên ngồi học cả buổi, hay các công ty đặt đồ uống theo hợp đồng tháng?)
2. **Họ trả tiền để giải quyết việc gì?** (Cần tỉnh táo nhanh trong 2 phút trên đường đi làm, hay cần một chỗ ngồi mát mẻ có Wi-Fi?)
3. **Sản phẩm / Dịch vụ cụ thể là gì và cách thu tiền ra sao?** (Thu tiền theo từng ly lẻ, bán thẻ thành viên trả trước theo tháng, hay nhượng quyền thương hiệu thu phí phần trăm?)
4. **Những chi phí nào tăng giảm trực tiếp theo từng đơn hàng bán ra?** (Gọi là **Biến phí**).
5. **Những chi phí nào vẫn phải trả đều đặn mỗi tháng dù quán vắng khách?** (Gọi là **Định phí**).
6. **Khách trả tiền lúc nào và mình phải trả tiền cho nhà cung cấp lúc nào?** (Thu tiền mặt ngay tại quầy hay bán chịu? Mua nguyên liệu phải trả tiền ngay hay được nợ 30 ngày?).

Nếu chưa trả lời rõ ràng được 6 câu này bằng lời giản dị, bạn chưa thực sự hiểu doanh nghiệp đó kiếm tiền bằng cách nào.

### 1.2. Tách hai giỏ chi phí: Biến phí (`Variable Cost`) và Định phí (`Fixed Cost`)

Hãy tiếp tục câu chuyện của **Quán cà phê Sao Biển** (từ **[Bài N1](N1-market-basics.md)**). Giả sử để dễ theo dõi, quán chỉ bán một dòng sản phẩm đồng giá là **Cà phê sữa đặc biệt** với giá bán **`50.000 đồng/ly`**.

Mọi khoản chi tiêu hàng tháng của quán được chia vào hai giỏ có tính chất hoàn toàn khác nhau:
- **Giỏ 1 — Biến phí trên mỗi đơn vị (`Variable Cost per unit`):** Là những chi phí **chỉ phát sinh khi làm ra thêm 1 ly cà phê** (gồm hạt cà phê rang xay, sữa tươi, đá viên, ly nhựa, ống hút, nắp đậy).
  - Nếu quán không bán được ly nào: biến phí bằng `0 đồng`.
  - Cứ bán thêm 1 ly: tốn thêm đúng **`30.000 đồng`**. Bán 100 ly thì tốn `100 × 30.000 = 3.000.000 đồng`.
- **Giỏ 2 — Định phí hàng tháng (`Fixed Costs`):** Là những chi phí **cố định mỗi tháng để duy trì cửa hàng mở cửa** trong một phạm vi công suất nhất định, bất kể tháng đó bán được 100 ly hay 10.000 ly (gồm tiền thuê mặt bằng, lương nhân viên cố định theo tháng, tiền mạng Internet, chi phí bảo trì định kỳ).
  - Tại Quán Sao Biển, tổng định phí mỗi tháng là **`120.000.000 đồng`** (`120 triệu đồng/tháng`).

### 1.3. Tính từng bước: Phần đóng góp (`Contribution Margin`) và Điểm hòa vốn (`Break-even Point`)

`KỊCH_BẢN` Với giá bán `50.000 đồng/ly`, biến phí `30.000 đồng/ly` và định phí `120 triệu đồng/tháng` (giả định chưa xét thuế, lãi vay hay mua sắm máy móc mới, và công suất quán đáp ứng đủ lượng khách):

- **Bước 1 — Tính Phần đóng góp trên mỗi ly (`Contribution Margin per unit`):**
  Khi khách trả `50.000 đồng` cho 1 ly cà phê, quán phải trích ngay `30.000 đồng` để bù tiền hạt cà phê, sữa và cốc nhựa của chính ly đó. Số tiền còn dư lại của mỗi ly là:
  $$\text{Phần đóng góp mỗi ly} = \text{Giá bán 1 ly} - \text{Biến phí 1 ly} = 50.000 - 30.000 = 20.000\text{ đồng/ly}$$
  *Tại sao gọi là "Phần đóng góp" mà không gọi ngay là "Tiền lãi ròng mỗi ly"?*
  Vì `20.000 đồng` này **chưa phải là tiền lãi bỏ túi chủ quán ngay từ ly đầu tiên!** Nó mới chỉ là phần tiền mà mỗi ly cà phê "đóng góp" vào cái hũ chung để góp nhau trả khoản tiền thuê nhà và lương nhân viên cố định `120 triệu đồng` của tháng đó.

- **Bước 2 — Tính Tỷ lệ phần đóng góp trên doanh thu (`Contribution Margin Ratio`):**
  `PHÉP_TÍNH` Trên mỗi `50.000 đồng` doanh thu, quán giữ lại được `20.000 đồng` phần đóng góp:
  $$\text{Tỷ lệ phần đóng góp} = \frac{20.000\text{ đồng}}{50.000\text{ đồng}} = 0,40 = 40\%$$
  Nghĩa là cứ thu được `100 đồng` tiền bán cà phê thì có `60 đồng` đi trả tiền nguyên liệu và `40 đồng` được bỏ vào hũ trả định phí.

- **Bước 3 — Tính Sản lượng hòa vốn (`Break-even Volume`):**
  `PHÉP_TÍNH` Mỗi tháng cái hũ định phí cần đúng `120.000.000 đồng` để trả tiền thuê nhà và lương cứng. Vì mỗi ly cà phê đóng góp được `20.000 đồng` vào hũ, số ly cà phê cần bán để lấp đầy cái hũ đó là:
  $$\text{Sản lượng hòa vốn} = \frac{\text{Tổng định phí}}{\text{Phần đóng góp mỗi ly}} = \frac{120.000.000\text{ đồng}}{20.000\text{ đồng/ly}} = 6.000\text{ ly/tháng}$$
  Và **Doanh thu hòa vốn (`Break-even Revenue`)** tương ứng là:
  $$\text{Doanh thu hòa vốn} = 6.000\text{ ly} \times 50.000\text{ đồng/ly} = 300.000.000\text{ đồng/tháng}\text{ (300 triệu đồng)}$$
  *(Hoặc tính bằng công thức tỷ lệ: `120 triệu / 40% = 300 triệu đồng`).*

- **Bước 4 — Điều gì xảy ra trước và sau mốc 6.000 ly?**
  - Nếu tháng này quán chỉ bán được **`5.000 ly`** (tức vẫn thiếu `1.000 ly` so với mốc hòa vốn):
    $$\text{Kết quả hoạt động} = (5.000\text{ ly} \times 20.000\text{ đồng}) - 120.000.000\text{ đồng} = 100\text{ triệu} - 120\text{ triệu} = -20\text{ triệu đồng (Lỗ 20 triệu)}$$
  - Nếu tháng này quán bán được đúng **`6.000 ly`**:
    $$\text{Kết quả hoạt động} = (6.000\text{ ly} \times 20.000\text{ đồng}) - 120.000.000\text{ đồng} = 0\text{ đồng (Hòa vốn)}$$
  - Nếu tháng này quán bán được **`7.000 ly`** (vượt mốc hòa vốn `1.000 ly`):
    Vì `6.000 ly` đầu tiên đã trả xong toàn bộ `120 triệu đồng` tiền thuê nhà và lương cứng, nên `1.000 ly` vượt thêm đó không phải gánh thêm đồng định phí nào nữa! Toàn bộ `20.000 đồng` phần đóng góp của mỗi ly vượt thêm biến thẳng thành lợi nhuận hoạt động:
    $$\text{Lợi nhuận hoạt động giản lược} = (7.000 \times 20.000) - 120.000.000 = 140\text{ triệu} - 120\text{ triệu} = +20\text{ triệu đồng}$$

`SỰ_THẬT` Công thức và điều kiện tính điểm hòa vốn đơn sản phẩm này được Cơ quan Quản lý Doanh nghiệp Nhỏ Hoa Kỳ ([U.S. Small Business Administration — SBA: Calculate Your Break-Even Point](https://legacy.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs/break-even-point)) hướng dẫn làm bước kiểm tra cơ bản trước khi vận hành kinh doanh. Lưu ý toán học quan trọng: nếu **phần đóng góp mỗi đơn vị nhỏ hơn hoặc bằng 0** (tức giá bán thấp hơn hoặc bằng biến phí nguyên liệu mỗi ly: bán 1 ly giá 28.000 đồng trong khi nguyên liệu tốn 30.000 đồng), thì khi định phí dương, **không tồn tại điểm hòa vốn hữu hạn** — càng bán nhiều ly thì quán càng lỗ nặng hơn!

> **Điểm dừng Phiên 1:** Hãy tự nhẩm: nếu Quán Sao Biển bán được `6.500 ly` trong tháng này (vượt mốc hòa vốn `500 ly`), bạn có cần tính lại từ đầu doanh thu và tổng chi phí không, hay có thể lấy ngay `500 ly vượt thêm × 20.000 đồng = 10 triệu đồng` tiền lãi? Hãy thử cả hai cách để thấy chúng ra cùng một đáp số!

---

## Phiên 2 — Bẫy giảm giá, Đa sản phẩm và Định phí nhảy bậc

### 2.1. Tại sao giảm giá bán 10% lại có thể đánh sập lợi nhuận?

Người mới kinh doanh hoặc mới phân tích cổ phiếu thường nghĩ đơn giản: *"Giảm giá bán 10% thì lợi nhuận cùng lắm chỉ giảm 10%, lại còn hút thêm được khách!"* Hãy làm phép tính từng bước để thấy vì sao suy nghĩ đó cực kỳ nguy hiểm:

`KỊCH_BẢN` Quán Sao Biển đang bán `7.000 ly/tháng` ở giá `50.000 đồng/ly` (biến phí nguyên liệu vẫn là `30.000 đồng/ly`, định phí vẫn là `120 triệu đồng/tháng`). Như ta vừa tính ở Phiên 1, quán đang **lãi `+20 triệu đồng/tháng`**.
Bây giờ, chủ quán quyết định **giảm giá bán 10%** (tức giảm `5.000 đồng/ly`, giá bán mới còn **`45.000 đồng/ly`**). Giả sử lượng bán vẫn giữ ở mức `7.000 ly/tháng`:
- **Bước 1 — Phần đóng góp mỗi ly bị co lại bao nhiêu?**
  Giá bán giảm `5.000 đồng`, nhưng tiền hạt cà phê và sữa tươi (`30.000 đồng/ly`) có giảm theo đâu! Do đó, toàn bộ `5.000 đồng` giảm giá ăn thẳng vào phần đóng góp:
  $$\text{Phần đóng góp mới mỗi ly} = 45.000 - 30.000 = 15.000\text{ đồng/ly}$$
  `PHÉP_TÍNH` Hãy nhìn tỷ lệ sụt giảm: giá bán chỉ giảm `5.000 / 50.000 = 10%`, nhưng phần đóng góp mỗi ly đã tụt từ `20.000 đồng` xuống `15.000 đồng`, tức **sụt giảm tới `25%`**!
- **Bước 2 — Điểm hòa vốn mới vọt lên bao nhiêu?**
  $$\text{Sản lượng hòa vốn mới} = \frac{120.000.000\text{ đồng}}{15.000\text{ đồng/ly}} = 8.000\text{ ly/tháng}$$
  Trước khi giảm giá, chỉ cần bán `6.000 ly` là hòa vốn; sau khi giảm giá 10%, quán phải bán tới **`8.000 ly`** (tăng thêm `33,3%` sản lượng!) mới chỉ vừa đủ hòa vốn!
- **Bước 3 — Kết quả khi vẫn bán 7.000 ly ở mức giá 45.000 đồng:**
  $$\text{Kết quả mới} = (7.000\text{ ly} \times 15.000\text{ đồng}) - 120.000.000\text{ đồng} = 105\text{ triệu} - 120\text{ triệu} = -15\text{ triệu đồng (Lỗ 15 triệu!)}$$
  Chỉ vì giảm giá 10% mà không tăng được mạnh sản lượng, quán đã chuyển từ **lãi `+20 triệu đồng`** sang **lỗ `−15 triệu đồng`**! Ngược lại, nếu một doanh nghiệp có thương hiệu mạnh (như ta sẽ học về **quyền định giá — `pricing power`** ở **[Bài 003](003-business-quality-moat-and-roic.md)**) có thể tăng giá bán 10% (lên `55.000 đồng/ly`) mà khách vẫn mua đều `7.000 ly`, phần đóng góp mỗi ly tăng từ `20.000` lên `25.000 đồng`, giúp lợi nhuận vọt từ `+20 triệu` lên `7.000 × 25.000 − 120 triệu = +55 triệu đồng` (tăng gấp `2,75 lần`!).

### 2.2. Khi cửa hàng bán nhiều sản phẩm khác nhau (`Product Mix`)

Ngoài đời thực, Quán Sao Biển không chỉ bán một loại cà phê mà còn bán thêm **Bánh ngọt** và **Trà trái cây**:
- Giả sử **Cà phê** có phần đóng góp `20.000 đồng/món`, nhưng **Nước suối đóng chai** bán kèm chỉ có phần đóng góp `5.000 đồng/chai`.
- Nếu tháng này tổng số món bán ra vẫn là `6.000 món`, nhưng khách chuyển sang mua toàn nước suối thay vì cà phê, thì tổng phần đóng góp thu về sẽ thấp hơn rất nhiều so với `120 triệu đồng`, và quán sẽ bị lỗ!
- `SUY_LUẬN` Vì vậy, khi một doanh nghiệp bán nhiều dòng sản phẩm có độ lời dày mỏng khác nhau, điểm hòa vốn phụ thuộc chặt chẽ vào **cơ cấu bán hàng (`product mix` / `sales mix` — tỷ trọng từng mặt hàng trong tổng lượng bán)**. Không được lấy tổng số lượng sản phẩm đủ loại cộng gộp lại rồi nhân với phần đóng góp của mặt hàng lời nhất!

### 2.3. Định phí không đứng yên mãi mãi: Chi phí nhảy bậc (`Step-Fixed Costs`)

Trong ví dụ ở Phiên 1, ta giả định định phí giữ nguyên ở mức `120 triệu đồng/tháng`. Nhưng giả định đó chỉ đúng **trong phạm vi công suất hiện tại của 1 cửa hàng** (ví dụ tối đa phục vụ được `9.000 ly/tháng`).
- Nếu chủ quán muốn bán `15.000 ly/tháng`, một mặt bằng và một dàn máy pha hiện tại không thể làm xuể. Quán bắt buộc phải thuê thêm mặt bằng thứ hai, mua thêm máy pha và tuyển thêm một đội nhân viên mới — làm định phí hàng tháng **nhảy vọt thành bậc thang** (ví dụ từ `120 triệu` nhảy lên `240 triệu đồng/tháng`).
- Nếu cửa hàng thứ hai mới mở mới chỉ bán được thêm `2.000 ly/tháng` (đóng góp thêm `40 triệu`), trong khi định phí nhảy thêm `120 triệu`, thì tổng lợi nhuận của cả chuỗi sẽ bị kéo tụt xuống trong giai đoạn đầu mở rộng.

---

## Phiên 3 — Có lãi trên giấy nhưng két tiền trống rỗng (Cầu nối sang Bài 001)

`KỊCH_BẢN` Hãy xét tình huống thực tế sau tại Quán Sao Biển trong tháng 10:
- Quán bán được **`7.000 ly`** cà phê giá `50.000 đồng/ly` (tổng doanh thu **`350 triệu đồng`**).
- Trong đó:
  - `5.000 ly` bán lẻ tại quầy thu tiền mặt ngay: thu được **`250 triệu đồng` tiền mặt**.
  - `2.000 ly` còn lại là đơn hàng phục vụ hội nghị cho một công ty đối tác (`2.000 × 50.000 = 100 triệu đồng`). Công ty đối tác đã ký biên bản nhận hàng trong tháng 10 nhưng theo hợp đồng **hẹn ngày 15 tháng 11 mới chuyển khoản thanh toán**.
- Trong khi đó, ngay trong tháng 10, Quán Sao Biển phải trả bằng tiền mặt ngay lập tức:
  - Tiền nguyên liệu cho cả `7.000 ly`: `7.000 × 30.000 = 210 triệu đồng`.
  - Tiền thuê mặt bằng và lương nhân viên tháng 10: `120 triệu đồng`.
  - Tổng tiền mặt phải chi ra ngay trong tháng 10: `210 + 120 = 330 triệu đồng`.

Hãy đặt hai con số của tháng 10 cạnh nhau (`PHÉP_TÍNH`):
1. **Tính theo Lợi nhuận kinh doanh trong tháng 10:**
   $$\text{Doanh thu } (350\text{ triệu}) - \text{Tổng chi phí } (210 + 120 = 330\text{ triệu}) = \mathbf{+20\text{ triệu đồng (Có lãi!)}}.$$
2. **Tính theo Dòng tiền mặt thực thu – thực chi trong tháng 10:**
   $$\text{Tiền mặt thực thu } (250\text{ triệu}) - \text{Tiền mặt thực chi } (330\text{ triệu}) = \mathbf{-80\text{ triệu đồng (Thiếu hụt 80 triệu tiền mặt!)}}.$$

Tại sao cùng một quán cà phê trong cùng một tháng, tính lời lỗ thì báo **lãi `+20 triệu`**, nhưng mở két tiền ra thì lại **âm `−80 triệu`** (nếu đầu tháng trong két không có sẵn tiền dự trữ thì chủ quán không đủ tiền trả lương nhân viên)?
- Bởi vì **`100 triệu đồng`** doanh thu của đơn hàng công ty đang nằm dưới dạng **"Khoản phải thu khách hàng"** (lời hứa trả tiền trên giấy), chứ chưa biến thành tiền mặt!
- Именно để theo dõi đồng thời cả 3 mặt: **(1) Làm ăn lời hay lỗ**, **(2) Đang có tài sản gì, ai đang nợ mình và mình đang nợ ai**, và **(3) Tiền mặt thực sự vào/ra két bao nhiêu**, ngành kế toán mới sinh ra **Ba báo cáo tài chính** mà bạn sẽ học ngay ở bài kế tiếp: **[Bài 001 — Một doanh nghiệp đi qua ba báo cáo tài chính](001-business-financial-statements.md)**!

> **Điểm dừng Phiên 3:** Hãy tự giải thích bằng lời: vì sao một doanh nghiệp đang tăng trưởng đơn hàng rất nhanh (bán chịu cho nhiều khách hàng lớn) lại có thể rơi vào cảnh hết sạch tiền mặt để trả nợ ngắn hạn?

---

## Ví dụ từ nguồn thật

Khi đọc báo cáo tài chính của một chuỗi cà phê thật trên thế giới, tại sao chúng ta không được lấy "Tổng doanh thu" chia cho "Tổng số cửa hàng" để tính doanh thu trung bình một quán? Hãy mở **Form 10-K năm tài chính 2025 (`FY2025`) của Starbucks Corporation** nộp cho Ủy ban Chứng khoán Hoa Kỳ (`SEC`):

- `SỰ_THẬT` Theo [Starbucks Corporation Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm) (kỳ năm tài chính kết thúc ngày `28/09/2025`, nộp ngày `14/11/2025`, Hoa Kỳ, chuẩn kế toán `US GAAP`, các bảng báo cáo tài chính hợp nhất tính bằng đơn vị **triệu USD**), tổng doanh thu thuần (`Total net revenues`) của Starbucks đạt **`37.184,4 triệu USD`** (`37,18 tỷ USD`).
- Tuy nhiên, trên ngay mặt Báo cáo kết quả kinh doanh hợp nhất (`Consolidated Statements of Earnings`), Starbucks bắt buộc phải tách riêng doanh thu từ hai mô hình cửa hàng có kinh tế đơn vị hoàn toàn khác nhau:
  1. **Cửa hàng tự vận hành (`Company-operated stores`):** Đạt doanh thu **`30.744,8 triệu USD`** (chiếm khoảng `82,7%` tổng doanh thu). Với các cửa hàng này, Starbucks trực tiếp thu tiền bán từng ly cà phê từ khách hàng lẻ và trực tiếp trả tiền nguyên liệu, tiền thuê mặt bằng, tiền lương nhân viên pha chế tại cửa hàng.
  2. **Cửa hàng cấp phép (`Licensed stores`):** Đạt doanh thu **`4.350,4 triệu USD`** (chiếm khoảng `11,7%` tổng doanh thu; phần còn lại đến từ mảng khác). Với cửa hàng cấp phép, đối tác bên ngoài bỏ vốn thuê mặt bằng và trả lương nhân viên; Starbucks chủ yếu bán nguyên liệu cà phê, si-rô và thu phí bản quyền thương hiệu (`royalties`) từ đối tác.
- **Bài học thực chiến từ nguồn thật:** Hai mô hình trên nằm dưới cùng một thương hiệu Starbucks nhưng có cấu trúc doanh thu, biến phí và định phí khác hẳn nhau. Nếu người phân tích cộng gộp tổng số cửa hàng tự vận hành với cửa hàng cấp phép rồi lấy tổng doanh thu chia đều, con số "doanh thu mỗi cửa hàng" tính ra sẽ hoàn toàn sai bản chất kinh tế!

---

## Năm câu hỏi khi đọc

Khi tìm hiểu mô hình kinh doanh của bất kỳ công ty nào, hãy luôn đặt 5 câu hỏi kiểm tra:
1. **Đơn vị kinh tế (`Unit`):** Đơn vị bán hàng cốt lõi để tính lời lỗ của doanh nghiệp này là gì (một ly cà phê, một tấn thép, một thuê bao tháng, hay một dự án xây dựng)?
2. **Phần đóng góp:** Mỗi đơn vị bán thêm mang lại bao nhiêu đồng sau khi trừ chi phí biến đổi trực tiếp đi kèm đơn vị đó?
3. **Gánh nặng định phí:** Chi phí cố định hàng tháng/hàng năm (thuê mặt bằng, khấu hao nhà máy, lương bộ máy) lớn cỡ nào? Doanh nghiệp phải vận hành ở mức sản lượng bao nhiêu để vượt điểm hòa vốn?
4. **Quyền giữ giá và cơ cấu sản phẩm:** Doanh nghiệp đang bán thêm được hàng nhờ giữ nguyên giá hay phải giảm giá mạnh (bào mòn phần đóng góp)? Cơ cấu mặt hàng lời cao và lời thấp có thay đổi không?
5. **Chuyển hóa thành tiền mặt:** Khi ghi nhận doanh thu và lãi trên đơn hàng, khách hàng đã trả tiền mặt ngay chưa hay đang nợ lại?

---

## Bài tập — làm trước khi mở đáp án

Câu 1–4 rèn luyện kỹ năng tính phần đóng góp và điểm hòa vốn; câu 5–7 kiểm tra độ nhạy khi thay đổi giá/chi phí và dòng tiền; câu 8–10 yêu cầu giải quyết tình huống nhiều bước. Hãy tự tính trước khi mở đáp án.

1. Quán cà phê bán một loại đồ uống giá `50.000 đồng/ly`, chi phí nguyên liệu và cốc nhựa đi theo mỗi ly (biến phí) là `30.000 đồng/ly`. Tính **phần đóng góp mỗi ly** (bằng tiền) và **tỷ lệ phần đóng góp trên doanh thu** (bằng %).
2. Với phần đóng góp vừa tính ở câu 1, nếu tổng định phí mỗi tháng (tiền thuê nhà và lương nhân viên cố định) là `120.000.000 đồng`, quán cần bán bao nhiêu ly mỗi tháng để đạt **điểm hòa vốn**? Doanh thu hòa vốn tương ứng là bao nhiêu triệu đồng?
3. Nếu quán bán được `7.000 ly/tháng` nhưng quyết định **giảm giá bán xuống còn `45.000 đồng/ly`** (biến phí vẫn là `30.000 đồng/ly`, định phí vẫn là `120 triệu đồng`), kết quả hoạt động giản lược trong tháng là lãi hay lỗ bao nhiêu tiền?
4. Giả sử giá bán giữ nguyên `50.000 đồng/ly`, nhưng do giá sữa và hạt cà phê tăng nên biến phí tăng từ `30.000 đồng` lên `35.000 đồng/ly` (định phí vẫn `120 triệu đồng`). Tính sản lượng hòa vốn mới của quán.
5. Trong tháng, Quán Sao Biển tính ra lợi nhuận hoạt động là `+20 triệu đồng`, nhưng có một khách hàng doanh nghiệp mua chịu `50 triệu đồng` tiền cà phê chưa thanh toán. Chỉ với hai con số này, bạn đã biết chắc chắn số tiền mặt cuối tháng trong két của quán tăng hay giảm bao nhiêu chưa? Cần biết thêm những gì?
6. Một cửa hàng bán hai mặt hàng: **Cà phê** (phần đóng góp `20.000 đồng/ly`) và **Bánh quy đóng gói** (phần đóng góp `5.000 đồng/gói`). Vì sao không thể chỉ nói chung chung *"Cửa hàng cần bán 6.000 món mỗi tháng để hòa vốn"* mà bắt buộc phải hỏi cơ cấu bán hàng giữa hai món?
7. Giả sử Quán Sao Biển đang bán `7.000 ly/tháng` ở giá `50.000 đồng/ly` (biến phí `30.000 đồng`, định phí `120 triệu đồng`, đang lãi `20 triệu đồng`). Nếu quán giảm giá xuống `45.000 đồng/ly`, quán phải bán được **bao nhiêu ly mỗi tháng** để vẫn giữ được mức lãi `+20 triệu đồng` như cũ?
8. Một cửa hàng bán `60%` số lượng là Món A (giá `50.000 đồng`, biến phí `30.000 đồng`) và `40%` số lượng là Món B (giá `30.000 đồng`, biến phí `20.000 đồng`). Định phí hàng tháng là `160 triệu đồng`. Hãy tính **phần đóng góp bình quân gia quyền trên 1 món bán ra** theo cơ cấu này và tổng số món cần bán để hòa vốn.
9. Một quán hiện tại có công suất tối đa `8.000 ly/tháng` với định phí `120 triệu đồng/tháng` (giá bán `50.000 đồng`, biến phí `30.000 đồng`). Để bán được `9.500 ly/tháng`, chủ quán phải thuê thêm mặt bằng sát bên cạnh và tuyển thêm ca nhân viên, làm tổng định phí nhảy bậc từ `120 triệu` lên `190 triệu đồng/tháng`. Hãy tính lợi nhuận ở mức `8.000 ly` (1 mặt bằng) so với ở mức `9.500 ly` (2 mặt bằng) và rút ra nhận xét.
10. Trên báo cáo `Form 10-K FY2025` của Starbucks, doanh thu cửa hàng tự vận hành là `30.744,8 triệu USD` và doanh thu cửa hàng cấp phép là `4.350,4 triệu USD` trên tổng doanh thu thuần `37.184,4 triệu USD`. Hãy tính tỷ trọng đóng góp doanh thu của từng mảng trong tổng doanh thu thuần và giải thích vì sao không được gộp chung số lượng cửa hàng của hai mảng này khi tính doanh thu bình quân trên một cửa hàng.

## Đáp án và giải thích từng bước

<details>
<summary>Mở sau khi tự làm</summary>

1. **Đáp án câu 1 (`PHÉP_TÍNH`):**
   - Phần đóng góp mỗi ly = `50.000 − 30.000 = 20.000 đồng/ly`.
   - Tỷ lệ phần đóng góp = `20.000 / 50.000 = 40%`.
2. **Đáp án câu 2 (`PHÉP_TÍNH`):**
   - Sản lượng hòa vốn = `120.000.000 / 20.000 = 6.000 ly/tháng`.
   - Doanh thu hòa vốn = `6.000 ly × 50.000 đồng = 300.000.000 đồng` (`300 triệu đồng`).
3. **Đáp án câu 3 (`PHÉP_TÍNH`):**
   - Phần đóng góp mới mỗi ly = `45.000 − 30.000 = 15.000 đồng/ly`.
   - Tổng phần đóng góp của 7.000 ly = `7.000 × 15.000 = 105.000.000 đồng` (`105 triệu đồng`).
   - Kết quả hoạt động = `105 triệu − 120 triệu (định phí) = −15 triệu đồng` (**Lỗ 15 triệu đồng**).
4. **Đáp án câu 4 (`PHÉP_TÍNH`):**
   - Phần đóng góp mới mỗi ly khi biến phí tăng lên 35.000 đồng = `50.000 − 35.000 = 15.000 đồng/ly`.
   - Sản lượng hòa vốn mới = `120.000.000 / 15.000 = 8.000 ly/tháng`.
5. **Đáp án câu 5 (`SUY_LUẬN`):**
   - **Chưa đủ dữ kiện để biết tiền mặt cuối tháng.** Lợi nhuận `+20 triệu` được tính theo doanh thu và chi phí ghi nhận trong kỳ, nhưng có `50 triệu` khách còn nợ chưa trả tiền. Muốn biết tiền mặt cuối tháng, ta cần biết: số dư tiền đầu tháng, tổng tiền thực thu từ khách, tổng tiền thực trả cho nhà cung cấp và nhân viên, tiền mua sắm thiết bị và tiền vay/trả nợ (đây chính là nội dung sẽ học ngay ở **[Bài 001](001-business-financial-statements.md)**).
6. **Đáp án câu 6 (`SUY_LUẬN`):**
   - Vì mỗi ly cà phê đóng góp `20.000 đồng` để trả định phí, gấp 4 lần một gói bánh quy (`5.000 đồng`). Nếu bán 6.000 gói bánh quy thì chỉ thu được `6.000 × 5.000 = 30 triệu đồng` phần đóng góp (vẫn lỗ `90 triệu đồng` so với định phí `120 triệu`). Khi có nhiều sản phẩm, điểm hòa vốn phụ thuộc trực tiếp vào tỷ trọng số lượng bán của từng sản phẩm.
7. **Đáp án câu 7 (`PHÉP_TÍNH`):**
   - Để đạt mức lãi mục tiêu `+20 triệu đồng` khi định phí là `120 triệu đồng`, tổng phần đóng góp cần thu về trong tháng là: `120 triệu + 20 triệu = 140 triệu đồng`.
   - Ở giá bán `45.000 đồng/ly`, mỗi ly đóng góp `15.000 đồng`. Vậy số ly cần bán là:
     $$\frac{140.000.000\text{ đồng}}{15.000\text{ đồng/ly}} \approx 9.334\text{ ly/tháng}$$
   - Nghĩa là giảm giá 10% thì sản lượng bán phải tăng từ `7.000 ly` lên `9.334 ly` (tăng thêm **33,3%**) mới giữ nguyên được số tiền lãi 20 triệu đồng!
8. **Đáp án câu 8 (`PHÉP_TÍNH`):**
   - Phần đóng góp Món A = `50.000 − 30.000 = 20.000 đồng`.
   - Phần đóng góp Món B = `30.000 − 20.000 = 10.000 đồng`.
   - Phần đóng góp bình quân gia quyền trên 1 món (theo cơ cấu 60% A : 40% B) là:
     $$(0,60 \times 20.000) + (0,40 \times 10.000) = 12.000 + 4.000 = 16.000\text{ đồng/món}$$
   - Tổng số món cần bán để hòa vốn (với giả định cơ cấu 60:40 không đổi):
     $$\frac{160.000.000\text{ đồng}}{16.000\text{ đồng/món}} = 10.000\text{ món/tháng}\text{ (gồm 6.000 món A và 4.000 món B)}$$
9. **Đáp án câu 9 (`PHÉP_TÍNH` & `SUY_LUẬN`):**
   - Ở mức `8.000 ly` (1 mặt bằng, định phí `120 triệu`):
     $$\text{Lợi nhuận} = (8.000 \times 20.000) - 120.000.000 = 160\text{ triệu} - 120\text{ triệu} = +40\text{ triệu đồng}$$
   - Ở mức `9.500 ly` (2 mặt bằng, định phí nhảy lên `190 triệu`):
     $$\text{Lợi nhuận} = (9.500 \times 20.000) - 190.000.000 = 190\text{ triệu} - 190\text{ triệu} = 0\text{ đồng (Hòa vốn!)}$$
   - **Nhận xét:** Bán thêm `1.500 ly` chỉ tạo thêm `1.500 × 20.000 = 30 triệu đồng` phần đóng góp, trong khi định phí nhảy bậc tăng thêm tới `70 triệu đồng` (`190 − 120`), khiến tổng lợi nhuận giảm từ `+40 triệu` về `0 đồng`. Khi mở rộng quy mô làm định phí nhảy bậc, sản lượng phải vượt qua ngưỡng hòa vốn mới (`190 triệu / 20.000 = 9.500 ly`) và tiến lên trên `11.500 ly` mới có lãi cao hơn lúc chưa mở rộng.
10. **Đáp án câu 10 (`PHÉP_TÍNH` & `SUY_LUẬN`):**
    - Tỷ trọng cửa hàng tự vận hành: `30.744,8 / 37.184,4 ≈ 82,68%`.
    - Tỷ trọng cửa hàng cấp phép: `4.350,4 / 37.184,4 ≈ 11,70%`.
    - Không được gộp chung số lượng cửa hàng của hai mảng vì ở cửa hàng tự vận hành, Starbucks ghi nhận 100% doanh thu bán lẻ từng ly đồ uống; còn ở cửa hàng cấp phép, Starbucks chỉ ghi nhận doanh thu bán nguyên liệu và tiền phí bản quyền thu từ đối tác.

</details>

---

## Bài làm với dữ liệu thiếu hoặc lệch

`KỊCH_BẢN` Một bản giới thiệu nhượng quyền quán trà sữa viết:
> *"Giá bán trung bình mỗi ly là `40.000 đồng`, tiền cốt trà và trân châu chỉ tốn `12.000 đồng/ly`, vậy mỗi ly bạn lãi ròng `28.000 đồng` (tỷ suất lợi nhuận 70%!). Chỉ cần bán `200 ly/ngày` là mỗi năm bạn bỏ túi hơn `2 tỷ đồng` tiền lãi!"*

Khi kiểm tra kỹ bảng chi tiết đính kèm, bạn phát hiện:
- Bản giới thiệu **chưa hề trừ** phí chiết khấu `25%` trên giá bán cho các ứng dụng giao đồ ăn (trong khi 60% đơn hàng của quán bán qua ứng dụng giao hàng);
- Chưa tính tiền ly nhựa, màng dập nắp, túi mang đi (`3.000 đồng/ly`);
- Tiền thuê mặt bằng (`35 triệu đồng/tháng`), lương 4 nhân viên (`28 triệu đồng/tháng`), điện nước (`7 triệu đồng/tháng`) và chi phí đầu tư ban đầu `500 triệu đồng` đang bị bỏ quên hoàn toàn khỏi phép tính "lãi 28.000 đồng/ly"!

**Cách phát hiện và xử lý chuẩn:**
1. **Bóc lỗi nhầm "Chênh lệch giá bán – cốt nguyên liệu" với "Lãi ròng":** Con số `28.000 đồng` thậm chí còn chưa phải là phần đóng góp đúng, vì đã bỏ sót biến phí bao bì (`3.000 đồng/ly`) và phí hoa hồng ứng dụng giao hàng (`60% × 25% × 40.000 = 6.000 đồng/ly` tính bình quân).
2. **Tính lại từng bước với dữ liệu đã làm sạch (`PHÉP_TÍNH`):**
   - Biến phí thực tế bình quân mỗi ly = `12.000 (cốt trà) + 3.000 (bao bì) + 6.000 (phí ứng dụng bình quân) = 21.000 đồng/ly`.
   - Phần đóng góp thực tế mỗi ly = `40.000 − 21.000 = 19.000 đồng/ly` (chứ không phải `28.000 đồng`).
   - Tổng định phí hàng tháng (chưa tính khấu hao 500 triệu vốn đầu tư ban đầu) = `35 + 28 + 7 = 70 triệu đồng/tháng`.
   - Sản lượng hòa vốn mỗi tháng = `70.000.000 / 19.000 ≈ 3.685 ly/tháng` (khoảng `123 ly/ngày` chỉ để trả tiền thuê nhà, lương và điện nước).
   - Nếu bán `200 ly/ngày` (`6.000 ly/tháng` trong tháng 30 ngày), lợi nhuận trước khấu hao và thuế chỉ là `(6.000 × 19.000) − 70.000.000 = 114 triệu − 70 triệu = 44 triệu đồng/tháng` (tức `528 triệu đồng/năm` trước khi thu hồi `500 triệu` vốn mở quán ban đầu — thấp xa con số quảng cáo "hơn 2 tỷ đồng/năm"!).

---

## Sai ở đâu

Hãy đọc lập luận sau của một nhà phân tích mới và chỉ ra chỗ sai:

> *"Công ty A đang bán 10.000 sản phẩm/tháng với giá 100.000 đồng/sản phẩm, biến phí 60.000 đồng/sản phẩm, định phí 300 triệu đồng/tháng, lợi nhuận đang là 100 triệu đồng/tháng. Năm tới Công ty A dự kiến mở thêm nhà máy mới gấp đôi công suất để bán 14.000 sản phẩm/tháng. Vì phần đóng góp mỗi sản phẩm là 40.000 đồng và định phí là cố định 300 triệu đồng, nên lợi nhuận năm tới chắc chắn là `14.000 × 40.000 − 300 triệu = 260 triệu đồng/tháng`!"*

**Phân tích lỗi sai:**
1. **Lỗi thứ nhất — Quên rằng định phí chỉ cố định trong phạm vi công suất hiện tại (bỏ qua định phí nhảy bậc):** Khi xây thêm nhà máy mới gấp đôi công suất, chi phí khấu hao máy móc mới, lương quản lý nhà máy mới, bảo hiểm và bảo trì cố định sẽ tăng vọt lên một bậc mới, chứ không thể giữ nguyên ở mức `300 triệu đồng/tháng` của nhà máy cũ.
2. **Lỗi thứ hai — Giả định bán tăng thêm 40% sản lượng mà không cần giảm giá bán hoặc tăng chi phí bán hàng:** Để đẩy lượng hàng tiêu thụ từ `10.000` lên `14.000 sản phẩm`, doanh nghiệp có thể phải chiết khấu thêm cho đại lý hoặc chi thêm hoa hồng tiếp thị, làm phần đóng góp mỗi sản phẩm thấp hơn mức `40.000 đồng` cũ.

---

## Kiểm tra chuyển bài

Trước khi chuyển sang **[Bài 001 — Một doanh nghiệp đi qua ba báo cáo tài chính](001-business-financial-statements.md)**, hãy tự làm 3 câu kiểm tra sau:

1. Một sản phẩm có giá bán `80.000 đồng`, biến phí `50.000 đồng/sản phẩm`, tổng định phí `90 triệu đồng/tháng`. Tính **phần đóng góp mỗi sản phẩm**, **sản lượng hòa vốn** và **doanh thu hòa vốn** hàng tháng.
2. Nếu giảm giá bán 10% (xuống `72.000 đồng/sản phẩm`) khi biến phí và định phí không đổi, thì phần đóng góp mỗi sản phẩm giảm bao nhiêu % và sản lượng hòa vốn mới là bao nhiêu?
3. Cửa hàng bán `4.000 sản phẩm` (giá `80.000 đồng`), tính ra lãi `+30 triệu đồng`, nhưng khách mới trả tiền mặt một nửa. Vì sao chủ cửa hàng cần đọc cùng lúc cả **Báo cáo kết quả kinh doanh**, **Bảng cân đối kế toán** và **Báo cáo lưu chuyển tiền tệ**?

- **Tiêu chí đạt:** (1) Phần đóng góp `= 30.000đ`, Sản lượng hòa vốn `= 3.000 sp`, Doanh thu hòa vốn `= 240 triệu`; (2) Phần đóng góp mới `= 22.000đ` (giảm `26,67%`), hòa vốn mới `≈ 4.091 sp`; (3) Báo cáo kết quả kinh doanh chỉ báo lãi `+30 triệu` chứ không cho biết tiền mặt thực thu và khoản khách còn nợ.
- **Điểm đến tiếp theo:** Mở ngay **[Bài 001 — Một doanh nghiệp đi qua ba báo cáo tài chính](001-business-financial-statements.md)** (Bước 3/23 của Nhánh 1)!

---

## Mô hình thực hành

Thực hành tính toán cùng [`practice/models/market_returns.py`](../practice/models/market_returns.py) và [`practice/research-and-model-worksheets.md`](../practice/research-and-model-worksheets.md). Luôn giữ thống nhất đơn vị tiền tệ trước khi chia điểm hòa vốn.

## Ranh giới an toàn

- Bài học này cung cấp khung phân tích mô hình kinh doanh, **không phải** khuyến nghị mua, bán hay nắm giữ cổ phiếu Starbucks hay bất kỳ doanh nghiệp nào.
- Mọi con số của Quán Sao Biển và quán trà sữa được gắn nhãn `KỊCH_BẢN` để minh họa toán học.

## Nguồn Internet đã mở

Các nguồn dưới đây đã được tìm kiếm và mở kiểm chứng trực tiếp (cập nhật ngày `2026-11-06`):

| Nguồn | Kỳ / Phiên bản & Phạm vi | Nội dung xác minh dùng trong bài |
|---|---|---|
| [U.S. Small Business Administration (SBA) — Calculate Your Break-Even Point](https://legacy.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs/break-even-point) | Hoa Kỳ; hướng dẫn chính thức của SBA | Công thức tính điểm hòa vốn theo sản lượng và doanh thu; định phí, biến phí và phần đóng góp |
| [Starbucks Corporation — Form 10-K FY2025 (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm) | Năm tài chính kết thúc `28/09/2025`; nộp `14/11/2025`; `US GAAP`; triệu USD (`2026-11-06`) | Tách doanh thu cửa hàng tự vận hành (`30.744,8 triệu USD`) và cửa hàng cấp phép (`4.350,4 triệu USD`) trên tổng doanh thu (`37.184,4 triệu USD`) |
