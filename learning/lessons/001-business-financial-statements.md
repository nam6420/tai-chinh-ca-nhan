# Bài 001: Một doanh nghiệp đi qua ba báo cáo tài chính

- Ngày cập nhật: `2026-11-06` (bản gốc `2026-08-10`, nâng cấp Bậc S `2026-11-06`)
- Chốt dữ liệu lúc: `2026-11-06 10:48 UTC+7 (Asia/Ho_Chi_Minh)`
- Bậc chiều sâu: `Bậc S`
- Lộ trình đọc: **Bài 3 / 23 của Nhánh 1 (Hiểu doanh nghiệp & Phân tích cổ phiếu)**.
  - **Bài trước liên quan:** **[Bài N1 — Thị trường chứng khoán vận hành thế nào?](N1-market-basics.md)** (Bước 1/23) và **[Bài N6 — Doanh nghiệp kiếm tiền thế nào?](N6-business-model-unit-economics.md)** (Bước 2/23).
  - **Học tiếp theo đúng thứ tự:** **[Bài N2 — Đọc từng dòng ba báo cáo tài chính](N2-statement-line-items.md)** (Bước 4/23), sau đó tới **[Bài N8 — Tìm và kiểm nguồn](N8-finding-verifying-sources.md)** (Bước 5/23).
- Mục tiêu: Phân biệt rõ doanh thu, lợi nhuận và tiền mặt; chỉ ra mỗi báo cáo trong ba báo cáo tài chính trả lời câu hỏi gì; tính được khoảng cách giữa dòng tiền hoạt động (`CFO`) và lợi nhuận sau thuế, dựng "cây cầu" đối chiếu và nêu giả thuyết kèm dữ liệu cần kiểm chứng.
- Thời lượng: Ba phiên học ngắn (30–35 phút/phiên) có điểm dừng; thực hành cùng [`practice/models/earnings_quality.py`](../practice/models/earnings_quality.py) và [`practice/models/apple_fy2025_inputs.csv`](../practice/models/apple_fy2025_inputs.csv).
- Câu hỏi cốt lõi: **Doanh nghiệp báo lãi lớn, nhưng tiền mặt thật đã về két chưa — và nếu chưa thì tiền đang nằm ở đâu?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

> Đây là bài học nền tảng, không phải khuyến nghị mua, bán hay nắm giữ chứng khoán. Các ví dụ số học về Quán Sao Biển là hư cấu (`KỊCH_BẢN`); ví dụ thực tế lấy từ báo cáo `Form 10-K FY2025` của Apple Inc. đã nộp cho SEC.

---

## Hiểu bài này trong 1 phút

Bài này giải quyết một nhầm lẫn phổ biến nhất của người mới: **bán được hàng (doanh thu), có lời trên sổ sách (lợi nhuận) và thu được tiền thật vào két (dòng tiền) KHÔNG phải lúc nào cũng xảy ra cùng một lúc.**

Hãy hình dung **ba báo cáo tài chính** như **ba góc máy quay** cùng gắn trong **Quán cà phê Sao Biển**:

| Tên báo cáo tài chính | Hình ảnh trực giác | Câu hỏi cốt lõi mà báo cáo này trả lời |
|---|---|---|
| **1. Báo cáo kết quả kinh doanh** (`Income Statement`) | **Cuốn phim quay suốt một kỳ** (1 quý hoặc 1 năm) | Trong kỳ đó, quán buôn bán **lời hay lỗ** bao nhiêu? |
| **2. Bảng cân đối kế toán** (`Balance Sheet` / Báo cáo tình hình tài chính) | **Bức ảnh chụp tĩnh tại một ngày khóa sổ** (ví dụ ngày 31/12) | Ngay tại thời điểm chụp ảnh, quán **có những tài sản gì**, **nợ ai bao nhiêu**, và **phần vốn thuộc về chủ còn lại bao nhiêu**? |
| **3. Báo cáo lưu chuyển tiền tệ** (`Cash Flow Statement`) | **Nhật ký két sắt tiền mặt suốt một kỳ** | Tiền mặt thật sự đã **chảy vào và chảy ra** qua 3 cánh cửa (kinh doanh hàng ngày, mua sắm đầu tư, và vay/trả nợ/chia cổ tức) như thế nào? |

Ví dụ cực ngắn: Tháng này Quán Sao Biển giao đơn hàng cà phê trị giá **`100 triệu đồng`** cho khách, nhưng khách mới chuyển khoản trả **`60 triệu đồng`**, còn **`40 triệu đồng`** hẹn tháng sau trả:
- **Doanh thu** trên Báo cáo kết quả kinh doanh được ghi nhận là **`100 triệu đồng`** (vì hàng đã giao xong).
- **Lợi nhuận** được tính bằng cách lấy `100 triệu đồng` doanh thu trừ đi các chi phí nguyên liệu, lương, thuê nhà của tháng đó.
- Nhưng **Tiền mặt thực thu từ khách** trên Báo cáo lưu chuyển tiền tệ mới chỉ là **`60 triệu đồng`**; còn **`40 triệu đồng`** chưa thu được đang nằm trên Bảng cân đối kế toán ở dòng **"Khoản phải thu khách hàng" (`Accounts Receivable`)**.

Chính vì vậy, một doanh nghiệp hoàn toàn có thể **báo lãi đẹp trên giấy nhưng trong két lại thiếu tiền mặt**!

---

## Ôn bài cũ hoặc kiểm tra đầu vào

Hãy nối lại câu chuyện bạn vừa học ở **[Bài N1](N1-market-basics.md)** và **[Bài N6](N6-business-model-unit-economics.md)** trước khi đi tiếp:

1. **Câu hỏi 1 (từ [Bài N6 — Doanh nghiệp kiếm tiền thế nào?](N6-business-model-unit-economics.md)):** Ở Phiên 3 của Bài N6, Quán Sao Biển bán `7.000 ly` cà phê (giá `50.000 đồng/ly`, biến phí `30.000 đồng/ly`, định phí `120 triệu đồng/tháng`), tính ra lãi `+20 triệu đồng`, nhưng có `2.000 ly` (`100 triệu đồng`) khách mua chịu sang tháng sau mới trả. Vì sao tháng đó két tiền của quán bị hụt `80 triệu đồng`?
   - **Đáp án:** Vì quán phải chi ngay tiền mặt `210 triệu` nguyên liệu và `120 triệu` định phí (tổng chi `330 triệu`), trong khi mới thu tiền mặt của `5.000 ly` bán lẻ (`250 triệu`). Khoản `100 triệu` bán chịu đã tính vào doanh thu để ra lãi `+20 triệu`, nhưng chưa biến thành tiền mặt trong két.
2. **Câu hỏi 2 (từ [Bài N1 — Thị trường chứng khoán vận hành thế nào?](N1-market-basics.md)):** Tiền khách trả khi mua cà phê và tiền cổ đông nộp vào khi công ty phát hành cổ phiếu mới khác nhau thế nào trên 3 báo cáo tài chính?
   - **Đáp án:** Tiền bán cà phê tạo ra **doanh thu** và **dòng tiền hoạt động kinh doanh**; còn tiền cổ đông góp thêm khi phát hành cổ phần mới đi vào **dòng tiền hoạt động tài chính** và làm tăng **vốn chủ sở hữu** trên Bảng cân đối kế toán, tuyệt đối không phải doanh thu hay lợi nhuận!

## Bài này làm gì và chưa làm gì

| Bài này làm | Bài này chưa làm |
|---|---|
| Giải thích vai trò của từng báo cáo trong 3 báo cáo tài chính bằng ví dụ đời thường | Chưa đi vào từng dòng chi tiết như `EBIT`, `EBITDA`, `EPS`, `ROA`, `ROE` (học ngay ở **[Bài N2 — Đọc từng dòng ba báo cáo tài chính](N2-statement-line-items.md)**) |
| Hướng dẫn tính khoảng cách giữa **Dòng tiền hoạt động (`CFO`)** và **Lợi nhuận sau thuế**, dựng "cây cầu" giải thích sự lệch pha đó | Chưa dạy mã số biểu mẫu báo cáo tài chính Việt Nam theo VAS (học ở **[Bài N3](N3-vietnam-vas-statements.md)**) |
| Dạy cách đặt giả thuyết kèm theo dữ liệu cần mở để kiểm chứng | Không kết luận một doanh nghiệp là "tốt" hay "xấu" chỉ từ một kỳ dòng tiền âm |

---

## Phiên 1 — Ba góc máy quay cùng nhìn vào một doanh nghiệp

### 1.1. Theo dõi một tháng của Quán cà phê Sao Biển qua 3 báo cáo

`KỊCH_BẢN` Trong tháng này tại Quán Sao Biển:
- Quán giao cà phê cho khách trị giá **`100 triệu đồng`**, khách mới trả tiền mặt **`60 triệu đồng`**, còn nợ lại **`40 triệu đồng`**.
- Giá vốn nguyên liệu của số hàng đã bán là **`50 triệu đồng`** (đã trả tiền mặt cho nhà cung cấp).
- Đầu tháng, quán bỏ **`20 triệu đồng`** tiền mặt mua một máy xay cà phê công nghiệp dùng trong **5 năm** (mỗi năm máy mòn đi `4 triệu đồng`, gọi là **khấu hao — `depreciation`**).

Hãy xem **3 báo cáo tài chính** ghi chép sự kiện này khác nhau thế nào (`SỰ_THẬT` theo [Beginners' Guide to Financial Statements — U.S. SEC](https://www.sec.gov/reportspubs/investor-publications/investorpubsbegfinstmtguide)):

1. **Góc máy 1 — Báo cáo kết quả kinh doanh (`Income Statement`):**
   - Dùng nguyên tắc **kế toán dồn tích (`accrual accounting`)**: ghi nhận doanh thu khi đã giao hàng (dù chưa thu đủ tiền) và ghép với đúng phần chi phí tạo ra doanh thu đó trong kỳ.
   - Báo cáo ghi: Doanh thu = `100 triệu đồng`; trừ Giá vốn nguyên liệu = `50 triệu đồng`; trừ phần nhỏ chi phí hao mòn máy xay trong kỳ (chứ **không trừ cả cục `20 triệu đồng`** tiền mua máy ngay tháng đầu, vì máy còn dùng suốt 5 năm!).
2. **Góc máy 2 — Bảng cân đối kế toán (`Balance Sheet`):**
   - Chụp ảnh tại ngày cuối tháng: quán có bao nhiêu **Tài sản (`Assets`)** (tiền mặt trong két, khoản `40 triệu đồng` khách còn nợ, giá trị còn lại của máy xay), bao nhiêu **Nợ phải trả (`Liabilities`)**, và phần còn lại thuộc về **Vốn chủ sở hữu (`Shareholders' Equity`)**.
3. **Góc máy 3 — Báo cáo lưu chuyển tiền tệ (`Cash Flow Statement`):**
   - Chỉ quan tâm: **tiền mặt thật sự đã vào két hay ra khỏi két chưa?** Báo cáo chia két sắt thành **3 cánh cửa**:
     - **Cửa 1 — Dòng tiền từ hoạt động kinh doanh (`Operating Cash Flow — CFO`):** Tiền thu thực tế từ khách mua cà phê (`+60 triệu`) trừ tiền trả thực tế cho nguyên liệu, lương, vận hành hàng ngày (`−50 triệu`).
     - **Cửa 2 — Dòng tiền từ hoạt động đầu tư (`Investing Cash Flow — CFI`):** Tiền chi mua tài sản dài hạn dùng nhiều năm — chính là khoản **`−20 triệu đồng`** mua máy xay cà phê! *(Nhớ kỹ: tiền mua máy móc dài hạn nằm ở cửa Đầu tư, không nằm ở cửa Hoạt động kinh doanh).*
     - **Cửa 3 — Dòng tiền từ hoạt động tài chính (`Financing Cash Flow — CFF`):** Tiền nhận thêm khi vay ngân hàng hoặc phát hành cổ phiếu mới, và tiền chi ra khi trả nợ gốc ngân hàng hoặc trả cổ tức.

### 1.2. Năm câu hỏi định hướng khi mở bộ 3 báo cáo

1. Doanh thu được tạo ra từ sản phẩm và nhóm khách hàng nào? (Nối từ **[Bài N6](N6-business-model-unit-economics.md)**).
2. Lợi nhuận trên Báo cáo kết quả kinh doanh có chuyển hóa thành **dòng tiền hoạt động (`CFO`)** trên Báo cáo lưu chuyển tiền tệ không?
3. Trên Bảng cân đối kế toán, **khoản phải thu khách hàng** và **hàng tồn kho** có phình to nhanh hơn tốc độ tăng doanh thu không?
4. Doanh nghiệp phải chi bao nhiêu tiền ở cửa Đầu tư (mua sắm máy móc, nhà xưởng — `CapEx`) để duy trì hoạt động?
5. Ở cửa Tài chính, doanh nghiệp có phải liên tục vay nợ mới hoặc in thêm cổ phiếu để bù đắp thiếu hụt tiền mặt không?

> **Điểm dừng Phiên 1:** Nếu công ty bỏ 100 tỷ đồng tiền mặt mua dây chuyền máy móc mới dùng trong 10 năm, khoản 100 tỷ tiền mặt chi ra đó nằm ở cánh cửa nào trên Báo cáo lưu chuyển tiền tệ? *(Đáp án: Cửa Đầu tư — không phải Cửa Hoạt động kinh doanh).*

---

## Phiên 2 — Dựng "cây cầu" nối từ Lợi nhuận sang Dòng tiền hoạt động

Hãy giải bài toán kinh điển: **Tại sao công ty báo lãi `+20` nhưng dòng tiền hoạt động lại âm `−10`?**

`KỊCH_BẢN` Một công ty công bố 3 con số trong cùng một kỳ (cùng đơn vị tiền):
- **Doanh thu thuần:** `200`
- **Lợi nhuận sau thuế (`Net Income`):** `+20`
- **Dòng tiền từ hoạt động kinh doanh (`Operating Cash Flow — CFO`):** `−10`

Hãy đi qua **6 bước tư duy chuẩn** để đọc 3 con số này mà không đoán mò:

### Bước 1: Tách rõ điều đã biết (`SỰ_THẬT`) và điều chưa biết (`CHƯA_BIẾT`)

- `SỰ_THẬT`: Doanh thu ghi nhận là `200` (quy mô hàng đã giao, **chưa cho biết** đã thu bao nhiêu tiền mặt); Lợi nhuận sau thuế là `+20` (theo kế toán dồn tích); Dòng tiền hoạt động `CFO` là `−10` (hoạt động kinh doanh hàng ngày đã **chi tiền mặt ra nhiều hơn thu vào 10 đơn vị**).
- `CHƯA_BIẾT`: Khoản phải thu khách hàng, hàng tồn kho, khoản phải trả người bán và khấu hao đã biến động cụ thể bao nhiêu.

### Bước 2: Tính "Khoảng cách tiền mặt" cần giải thích

`PHÉP_TÍNH` Lấy Dòng tiền hoạt động trừ Lợi nhuận sau thuế:
$$\text{Khoảng cách tiền mặt} = \text{CFO} - \text{Lợi nhuận sau thuế} = -10 - 20 = -30\text{ đơn vị}$$

Chia cả hai cho Doanh thu (`200`) (`PHÉP_TÍNH`):
- **Biên lợi nhuận sau thuế:** `20 / 200 = 10%` (cứ 100 đồng doanh thu có 10 đồng lãi trên sổ).
- **Biên dòng tiền hoạt động:** `−10 / 200 = −5%` (cứ 100 đồng doanh thu thì két tiền kinh doanh vơi đi 5 đồng).

Con số **`−30`** đặt ra câu hỏi chính xác: **Những khoản mục nào đã làm dòng tiền hoạt động thấp hơn lợi nhuận sau thuế 30 đơn vị?**

### Bước 3: Hiểu quy tắc dấu trên "Cây cầu" đối chiếu từ Lợi nhuận sang Tiền

`SỰ_THẬT` Theo chuẩn mực kế toán quốc tế [IAS 7 — Statement of Cash Flows](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/) và hướng dẫn của [SEC](https://www.sec.gov/reportspubs/investor-publications/investorpubsbegfinstmtguide), khi lập Báo cáo lưu chuyển tiền tệ theo **phương pháp gián tiếp (`indirect method`)**, kế toán đi từ **Lợi nhuận** rồi cộng/trừ các nhịp cầu điều chỉnh để tới **Dòng tiền hoạt động (`CFO`)**:

```text
Dòng tiền hoạt động (CFO)
= Lợi nhuận xuất phát
+ Chi phí phi tiền mặt (như Khấu hao máy móc: đã trừ khỏi lợi nhuận nhưng kỳ này không chi tiền mặt)
− Lãi/thu nhập phi tiền mặt hoặc thuộc cửa Đầu tư / Tài chính (như lãi bán đất, đánh giá lại tài sản)
− Phần TĂNG thêm của Tài sản hoạt động ngắn hạn (Phải thu khách hàng tăng, Hàng tồn kho tăng)
+ Phần TĂNG thêm của Nợ hoạt động ngắn hạn (Phải trả nhà cung cấp tăng, Thuế/chi phí phải trả tăng)
```

Bảng trực giác giúp bạn nhớ dấu cộng (`+`) và dấu trừ (`−`) ngay lập tức:

| Biến động trên Bảng cân đối | Dấu điều chỉnh khi tính `CFO` | Giải thích bằng trực giác đời thường |
|---|---|---|
| **Khoản phải thu khách hàng TĂNG** | **Trừ (`−`)** | Đã cộng vào doanh thu/lợi nhuận nhưng khách **chưa trả tiền mặt** (tiền kẹt ở chỗ khách). |
| **Khoản phải thu khách hàng GIẢM** | **Cộng (`+`)** | Kỳ này đòi được tiền nợ cũ của khách từ kỳ trước trả về két. |
| **Hàng tồn kho TĂNG** | **Trừ (`−`)** | Đã xuất tiền mua thêm hàng chất vào kho nhưng hàng chưa bán nên chưa trừ vào giá vốn. |
| **Hàng tồn kho GIẢM** | **Cộng (`+`)** | Lấy hàng trong kho cũ ra bán, kỳ này ghi giá vốn mà không tốn tiền mua hàng mới. |
| **Chi phí trả trước TĂNG** | **Trừ (`−`)** | Đã chi tiền mặt trả trước cho nhiều kỳ nhưng mới tính một phần vào chi phí kỳ này. |
| **Khoản phải trả người bán TĂNG** | **Cộng (`+`)** | Đã nhận nguyên liệu và tính chi phí, nhưng **chưa trả tiền mặt** cho nhà cung cấp (giữ lại được tiền). |
| **Khoản phải trả người bán GIẢM** | **Trừ (`−`)** | Phải xuất tiền mặt trong két ra trả bớt nợ cũ cho nhà cung cấp. |
| **Khấu hao tài sản cố định** | **Cộng (`+`)** | Tiền mua máy đã chi từ năm trước ở cửa Đầu tư; năm nay trừ khấu hao làm giảm lãi nhưng **không chi tiền mặt**, nên cộng trả lại. |

### Bước 4: Đặt giả thuyết kèm dữ liệu kiểm chứng

| Giả thuyết nguyên nhân (`SUY_LUẬN`) | Cơ chế làm tiền mặt thấp hơn lợi nhuận | Cần mở báo cáo & thuyết minh nào để kiểm tra? |
|---|---|---|
| **1. Khoản phải thu khách hàng tăng mạnh** | Bán chịu nhiều hơn hoặc khách trả chậm | Bảng cân đối (Phải thu đầu/cuối kỳ); Thuyết minh tuổi nợ quá hạn và dự phòng nợ khó đòi. |
| **2. Hàng tồn kho tăng mạnh** | Gom nguyên liệu hoặc hàng sản xuất ra chưa bán được | Bảng cân đối (Hàng tồn kho); Thuyết minh cơ cấu tồn kho và dự phòng giảm giá tồn kho. |
| **3. Khoản phải trả nhà cung cấp giảm** | Phải xuất tiền mặt trả nợ cũ cho nhà cung cấp nhanh hơn | Bảng cân đối (Phải trả người bán đầu/cuối kỳ) và điều khoản tín dụng thương mại. |
| **4. Lợi nhuận chứa khoản lãi một lần không tạo `CFO`** | Lãi đánh giá lại tài sản hoặc lãi bán đất/máy móc (tiền thu nằm ở cửa Đầu tư) | Báo cáo lưu chuyển tiền tệ (dòng điều chỉnh lãi/lỗ đầu tư) và Thuyết minh thu nhập khác. |

### Bước 5: Tự kiểm tra bằng một bảng cầu nối số học mẫu

`KỊCH_BẢN` Giả sử khi mở Báo cáo lưu chuyển tiền tệ chi tiết của công ty trên, ta thấy:

| Nhịp cầu nối từ Lợi nhuận sang Dòng tiền hoạt động | Số tiền | Giải thích từng bước |
|---|---:|---|
| **Điểm xuất phát: Lợi nhuận sau thuế** | **`+20`** | Số lãi ghi nhận trên Báo cáo kết quả kinh doanh |
| (+) Cộng lại: Chi phí khấu hao máy móc | `+5` | Chi phí phi tiền mặt (làm giảm lãi 5 nhưng không tốn tiền kỳ này) |
| (−) Trừ đi: Khoản phải thu khách hàng tăng thêm | `−20` | Bán hàng nhưng khách còn nợ thêm 20 chưa trả tiền |
| (−) Trừ đi: Hàng tồn kho tăng thêm | `−10` | Bỏ thêm 10 tiền mặt để nhập hàng dự trữ vào kho |
| (−) Trừ đi: Chi phí trả trước tăng thêm | `−3` | Trả trước tiền thuê dịch vụ cho các kỳ sau |
| (−) Trừ đi: Khoản phải trả nhà cung cấp giảm | `−2` | Xuất tiền mặt trả bớt nợ cũ cho nhà cung cấp |
| **= Điểm đích: Dòng tiền hoạt động (`CFO`)** | **`−10`** | `PHÉP_TÍNH`: `20 + 5 − 20 − 10 − 3 − 2 = −10` (Khớp!) |

### Bước 6: Phân biệt lệch pha tạm thời hay rủi ro kéo dài

Một kỳ `CFO` âm **`−10`** chưa tự động có nghĩa là công ty xấu:
- Nếu công ty đang nhập nguyên liệu làm hàng mùa cao điểm (như quý 3 tích trữ hàng Tết để quý 4 bán thu tiền), sang quý sau `CFO` sẽ dương lớn trở lại.
- Ngược lại, nếu 2–3 năm liền lợi nhuận dương nhưng `CFO` liên tục âm, phải thu quá hạn phình to và phải vay nợ mới để bù đắp, đó là **cờ đỏ cảnh báo chất lượng lợi nhuận thấp** (học sâu ở **[Bài 004](004-cash-flow-and-earnings-quality.md)** và **[Bài Q1](Q1-earnings-quality-toolkit.md)**).

---

## Ví dụ từ nguồn thật

Hãy mở báo cáo thường niên **Form 10-K năm tài chính 2025 (`FY2025`) của Apple Inc.** (kỳ kết thúc `27/09/2025`, nộp SEC `31/10/2025`, chuẩn `US GAAP`, đơn vị **triệu USD**) và đối chiếu với [`practice/models/apple_fy2025_inputs.csv`](../practice/models/apple_fy2025_inputs.csv) cùng [`practice/models/earnings_quality.py`](../practice/models/earnings_quality.py):

`SỰ_THẬT` Trên bộ 3 báo cáo tài chính hợp nhất của [Apple Inc. Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm):
1. **Báo cáo kết quả kinh doanh (`Consolidated Statements of Operations`):** Doanh thu thuần (`Total net sales`) = `416.161 triệu USD`; Lợi nhuận hoạt động (`Operating income`) = `133.050 triệu USD`; Lợi nhuận ròng sau thuế (`Net income`) = **`112.010 triệu USD`**.
2. **Bảng cân đối kế toán (`Consolidated Balance Sheets` tại `27/09/2025`):** Tổng tài sản (`Total assets`) = `359.241 triệu USD` (tiền và tương đương tiền `35.934`, phải thu thương mại ròng `39.777`, tồn kho `5.718`); Tổng nợ phải trả (`Total liabilities`) = `285.508 triệu USD`; Vốn chủ sở hữu (`Total shareholders' equity`) = `73.733 triệu USD` (`285.508 + 73.733 = 359.241 triệu USD`).
3. **Báo cáo lưu chuyển tiền tệ (`Consolidated Statements of Cash Flows`):**
   - **Dòng tiền từ hoạt động kinh doanh (`CFO`):** **`111.482 triệu USD`** (đã cộng lại Khấu hao và phân bổ `+11.698 triệu USD`, Chi phí thưởng cổ phiếu `+12.863 triệu USD` và điều chỉnh vốn lưu động).
   - **Cửa Đầu tư (`Investing activities`):** Chi mua sắm tài sản cố định (`CapEx`) = **`−12.715 triệu USD`**.

`PHÉP_TÍNH` **Kiểm tra khoảng cách lợi nhuận – tiền mặt của Apple FY2025:**
- Khoảng cách tuyệt đối: `CFO − Net income = 111.482 − 112.010 = −528 triệu USD` (chỉ lệch `-0,47%`).
- Tỷ lệ chuyển hóa lợi nhuận thành tiền hoạt động: `111.482 / 112.010 ≈ 99,53%` (cứ `100 USD` lợi nhuận ròng trên sổ thì có `99,53 USD` dòng tiền hoạt động thực chảy vào công ty).

---

## Năm câu hỏi khi đọc

1. Ba con số **Doanh thu**, **Lợi nhuận sau thuế** và **Dòng tiền hoạt động (`CFO`)** đang đi cùng chiều hay ngược chiều nhau?
2. Khoảng cách `CFO − Lợi nhuận sau thuế` bằng bao nhiêu đơn vị tiền, và bằng bao nhiêu % doanh thu?
3. Trong bảng đối chiếu dòng tiền gián tiếp, khoản mục nào tạo ra chênh lệch lớn nhất (phải thu tăng, tồn kho tăng, phải trả giảm, hay lãi một lần phi tiền mặt)?
4. Tiền chi mua sắm máy móc tài sản cố định (`CapEx`) ở cửa Đầu tư đang ngốn bao nhiêu phần của `CFO`?
5. Sự lệch pha giữa lợi nhuận và dòng tiền mới chỉ xuất hiện ở 1 quý do mùa vụ hay đã kéo dài nhiều năm liên tiếp?

---

## Bài tập — làm trước khi mở đáp án

1. Một công ty trong kỳ ghi nhận: **Doanh thu = `200`**, **Lợi nhuận sau thuế = `20`**, **Dòng tiền hoạt động (`CFO`) = `−10`** (cùng đơn vị tiền). Hãy tính **Khoảng cách tiền mặt (`CFO − Lợi nhuận sau thuế`)**, **Biên lợi nhuận sau thuế** và **Biên dòng tiền hoạt động**, rồi nêu ít nhất 3 nguyên nhân có thể giải thích khoảng cách đó kèm dữ liệu cần mở để kiểm tra.
2. Muốn tìm chính xác 5 thông tin sau, bạn phải mở báo cáo nào trong 3 báo cáo tài chính: (a) Số dư tiền mặt cuối năm; (b) Công ty lãi hay lỗ bao nhiêu trong năm; (c) Số tiền thực chi mua máy móc mới trong năm; (d) Khách hàng còn nợ công ty bao nhiêu vào cuối năm; (e) Số tiền mặt đã thực chi trả cổ tức trong năm?
3. Công ty H có **Lợi nhuận sau thuế = `50`**, **Chi phí khấu hao = `15`**, **Khoản phải thu khách hàng tăng = `30`**, **Hàng tồn kho giảm = `10`**, **Khoản phải trả người bán tăng = `5`** (không còn điều chỉnh nào khác). Hãy tính **Dòng tiền từ hoạt động kinh doanh (`CFO`)** từng bước.
4. Một người bạn nói: *"Năm nay công ty có lợi nhuận sau thuế là `40`, dòng tiền hoạt động là `60`, nhưng vì công ty chi `200` tiền mặt mua dây chuyền máy móc mới nên dòng tiền hoạt động thật ra là `60 − 200 = −140`."* Câu nói này sai ở đâu?
5. Một người khác khẳng định: *"Công ty báo lợi nhuận sau thuế năm nay là `30 tỷ đồng`, vậy số dư tiền mặt cuối năm chắc chắn tăng thêm đúng `30 tỷ đồng`."* Nêu 2 lý do vì sao khẳng định này sai.
6. Theo dõi Công ty M qua 2 năm liên tiếp:
   - **Năm 1:** Lợi nhuận sau thuế = `20`, `CFO` = `−10`, trong đó Khoản phải thu khách hàng tăng = `25`.
   - **Năm 2:** Lợi nhuận sau thuế = `25`, `CFO` = `+35`, trong đó Khoản phải thu khách hàng giảm = `10`.
   Hãy cộng gộp cả 2 năm để tính tổng lợi nhuận, tổng `CFO`, tổng khoảng cách tiền mặt 2 năm và cho biết biến động khoản phải thu giải thích được bao nhiêu phần của khoảng cách đó.
7. Công ty X báo lỗ ròng **`−15 tỷ đồng`** trong năm, nhưng **Dòng tiền hoạt động (`CFO`)** lại dương **`+25 tỷ đồng`**. Hãy dùng công thức cây cầu dòng tiền để giải thích và cho một tổ hợp số minh họa cụ thể.
8. Công ty B báo cáo **Lợi nhuận sau thuế = `80 tỷ đồng`**, trong đó có **`50 tỷ đồng`** là lãi một lần từ bán thanh lý một mảnh đất cũ (tiền bán đất nằm ở cửa Đầu tư). Nếu vốn lưu động không đổi và khấu hao bằng `10 tỷ đồng`, hãy tính **`CFO`** của Công ty B.
9. Trên `Form 10-K FY2025` của Apple (triệu USD): **Doanh thu thuần = `416.161`**, **Lợi nhuận ròng = `112.010`**, **`CFO` = `111.482`** và **`CapEx` = `12.715`**. Hãy tính: (a) Biên lợi nhuận ròng; (b) Biên dòng tiền hoạt động; (c) Dòng tiền còn lại `CFO − CapEx`.
10. Hai doanh nghiệp cùng có `Lợi nhuận sau thuế = 100 tỷ đồng` và `CFO = −40 tỷ đồng` trong quý 3: Doanh nghiệp 1 (bánh kẹo Tết) tăng tồn kho nguyên liệu `150 tỷ đồng` cuối quý 3 và lịch sử 5 năm qua quý 4 đều thu tiền dương mạnh; Doanh nghiệp 2 (xây dựng) tăng khoản phải thu quá hạn trên 2 năm thêm `150 tỷ đồng` và 3 năm liên tiếp `CFO` đều âm. Vì sao mức độ rủi ro của hai doanh nghiệp khác nhau?

## Đáp án và giải thích từng bước

<details>
<summary>Mở sau khi tự làm</summary>

1. **Câu 1 (`PHÉP_TÍNH` & `SUY_LUẬN`):** Khoảng cách tiền mặt = `−10 − 20 = −30`; Biên lợi nhuận sau thuế = `20 / 200 = 10%`; Biên `CFO` = `−10 / 200 = −5%`. Ba nguyên nhân cần kiểm tra: (1) Phải thu khách hàng tăng (kiểm tra số dư phải thu và tuổi nợ); (2) Hàng tồn kho tăng (kiểm tra tồn kho và dự phòng giảm giá); (3) Phải trả người bán giảm hoặc lợi nhuận có lãi phi tiền mặt.
2. **Câu 2 (`SỰ_THẬT`):** (a) Tiền mặt cuối năm: **Bảng cân đối kế toán** (hoặc dòng cuối Báo cáo lưu chuyển tiền tệ); (b) Lãi/lỗ trong năm: **Báo cáo kết quả kinh doanh**; (c) Tiền mua máy móc: **Báo cáo lưu chuyển tiền tệ — Cửa Đầu tư (`CFI`)**; (d) Khách còn nợ: **Bảng cân đối kế toán** (Phải thu khách hàng); (e) Tiền trả cổ tức: **Báo cáo lưu chuyển tiền tệ — Cửa Tài chính (`CFF`)** *(theo IAS 7 trước 2027 một số đơn vị có thể xếp vào `CFO`; từ kỳ `01/01/2027` theo IFRS 18 bắt buộc xếp vào `CFF`)*.
3. **Câu 3 (`PHÉP_TÍNH`):** `CFO = 50 (Lợi nhuận) + 15 (Khấu hao) − 30 (Phải thu tăng) + 10 (Tồn kho giảm) + 5 (Phải trả tăng) = +50`.
4. **Câu 4 (`SUY_LUẬN`):** Sai vì trộn **Cửa Đầu tư (`CFI`)** vào **Cửa Hoạt động kinh doanh (`CFO`)**. Tiền mua máy móc (`200`) thuộc `CFI`, nên `CFO` vẫn là **`+60`**. Con số `60 − 200 = −140` là dòng tiền sau đầu tư.
5. **Câu 5 (`SUY_LUẬN`):** Sai vì: (1) Lợi nhuận `30 tỷ` có thể đang nằm ở khoản khách nợ chưa trả hoặc hàng tồn kho; (2) Tiền mặt cuối năm còn tăng/giảm do Cửa Đầu tư (mua máy móc) và Cửa Tài chính (trả nợ vay, trả cổ tức).
6. **Câu 6 (`PHÉP_TÍNH` & `SUY_LUẬN`):** Tổng lợi nhuận 2 năm = `20 + 25 = 45`; Tổng `CFO` 2 năm = `−10 + 35 = +25`; Khoảng cách tiền mặt 2 năm = `25 − 45 = −20`. Khoản phải thu tăng ròng qua 2 năm = `25 − 10 = 15` (giải thích được `−15` trong `−20`), còn `−5` đơn vị cần mở tiếp dòng Tồn kho, Phải trả và Khấu hao để kiểm tra.
7. **Câu 7 (`PHÉP_TÍNH`):** Doanh nghiệp báo lỗ `−15 tỷ` vẫn có `CFO = +25 tỷ` khi có chi phí khấu hao lớn (phi tiền mặt) hoặc thu hồi công nợ/giảm tồn kho. Ví dụ: Lợi nhuận = `−15 tỷ`, Cộng khấu hao = `+30 tỷ`, Cộng hàng tồn kho giảm = `+10 tỷ` → `CFO = −15 + 30 + 10 = +25 tỷ đồng`.
8. **Câu 8 (`PHÉP_TÍNH`):** Lãi bán đất `50 tỷ` thuộc hoạt động đầu tư nên khi tính `CFO` gián tiếp phải trừ loại bỏ khỏi lợi nhuận: `CFO = 80 + 10 (Khấu hao) − 50 (Loại lãi bán đất) = +40 tỷ đồng`.
9. **Câu 9 (`PHÉP_TÍNH`):** (a) Biên lợi nhuận ròng = `112.010 / 416.161 ≈ 26,92%`; (b) Biên `CFO` = `111.482 / 416.161 ≈ 26,79%`; (c) `CFO − CapEx = 111.482 − 12.715 = 98.767 triệu USD`.
10. **Câu 10 (`SUY_LUẬN`):** Doanh nghiệp 1 âm `CFO` quý 3 do chu kỳ tích trữ hàng mùa vụ bình thường và quý 4 thu tiền về; Doanh nghiệp 2 âm `CFO` 3 năm liền kèm nợ quá hạn trên 2 năm là rủi ro mất vốn thực sự.

</details>

---

## Bài làm với dữ liệu thiếu hoặc lệch

`KỊCH_BẢN` Một bản tin viết về Công ty K: *"Năm 2025, Công ty K đạt lợi nhuận sau thuế `120 tỷ đồng`. Cuối năm 2025, khoản phải thu khách hàng trên Bảng cân đối là `300 tỷ đồng` so với đầu năm `180 tỷ đồng` (tăng `120 tỷ đồng`). Vậy toàn bộ `120 tỷ` lợi nhuận là lãi ảo và `CFO` chắc chắn bằng `0`!"*

**Cách phát hiện và xử lý chuẩn:**
1. **Dữ kiện bị thiếu:** Bản tin mới nhìn 3 con số lẻ mà **chưa mở Báo cáo lưu chuyển tiền tệ**!
2. **Vì sao không thể tự kết luận `CFO = 0`?** Công ty còn có **Khấu hao**, biến động **Tồn kho** và **Phải trả người bán** (ví dụ khấu hao `+50 tỷ`, phải trả tăng `+40 tỷ` thì `CFO` vẫn là `120 + 50 + 40 − 120 = +90 tỷ`). Ngoài ra phải thu trên Bảng cân đối có thể tăng do hợp nhất công ty con mới mua. Phải mở trực tiếp Báo cáo lưu chuyển tiền tệ và Thuyết minh tuổi nợ như quy trình trong [`practice/models/earnings_quality.py`](../practice/models/earnings_quality.py).

---

## Sai ở đâu

> *"Tôi chỉ cần đọc Báo cáo kết quả kinh doanh là đủ biết công ty giàu hay nghèo: nếu công ty có Lợi nhuận sau thuế dương 50 tỷ đồng suốt 3 năm liền (tổng lãi 150 tỷ đồng), thì công ty đó không bao giờ có thể mất khả năng thanh toán nợ!"*

**Phân tích lỗi sai:**
1. **Nhầm Lợi nhuận kế toán với Tiền mặt trả nợ:** Ngân hàng đòi nợ bằng **tiền mặt**, không nhận trả nợ bằng con số "Lợi nhuận sau thuế" trên giấy.
2. **Bỏ qua Bảng cân đối và Báo cáo lưu chuyển tiền tệ:** Nếu `150 tỷ` lãi nằm kẹt trong hàng tồn kho ế hoặc nợ xấu không đòi được (`CFO` âm), hoặc công ty rút hết tiền và vay nợ ngắn hạn đổ vào dự án dở dang (`CFI` âm nặng), thì khi nợ ngân hàng đến hạn, két sắt vẫn trống rỗng và công ty vẫn vỡ nợ (học sâu ở **[Bài 004](004-cash-flow-and-earnings-quality.md)** và **[Bài 005](005-debt-liquidity-survival.md)**).

---

## Kiểm tra chuyển bài

Trước khi chuyển sang **[Bài N2 — Đọc từng dòng ba báo cáo tài chính](N2-statement-line-items.md)**, hãy tự trả lời 3 câu hỏi sau:
1. Trong 3 báo cáo tài chính, báo cáo nào là "bức ảnh chụp tại một thời điểm", báo cáo nào là "cuốn phim quay trong một kỳ"?
2. Công ty có Lợi nhuận sau thuế `60 tỷ đồng`, Khấu hao `20 tỷ đồng`, Phải thu khách hàng tăng `35 tỷ đồng`, Hàng tồn kho tăng `15 tỷ đồng` và Phải trả người bán tăng `10 tỷ đồng`. Tính **`CFO`** và **Khoảng cách tiền mặt (`CFO − Lợi nhuận sau thuế`)**.
3. Khi công ty bỏ `400 triệu đồng` tiền mặt mua máy pha cà phê dùng trong `10 năm`, vì sao `400 triệu` đó không trừ hết ngay vào lợi nhuận năm đầu, và mỗi năm chi phí máy đó đi vào Báo cáo kết quả kinh doanh bằng cách nào?

- **Tiêu chí đạt:** Câu 1: Bảng cân đối kế toán là ảnh chụp; Báo cáo kết quả kinh doanh và Lưu chuyển tiền tệ là cuốn phim. Câu 2: `CFO = 60 + 20 − 35 − 15 + 10 = +40 tỷ đồng`; Khoảng cách = `40 − 60 = −20 tỷ đồng`. Câu 3: Lúc mua chỉ đổi Tiền mặt sang Tài sản máy móc (chi tiền ở cửa Đầu tư), sau đó mỗi năm trích **khấu hao** (`40 triệu/năm`) vào chi phí.
- **Điểm đến tiếp theo:** Mở ngay **[Bài N2 — Đọc từng dòng ba báo cáo tài chính](N2-statement-line-items.md)** (Bước 4/23 của Nhánh 1) để tự tay ghi 10 giao dịch của Quán Sao Biển vào từng dòng báo cáo!

---

## Đọc thêm: Từ kỳ báo cáo 2027, chuẩn quốc tế IFRS 18 thay đổi cách đọc báo cáo thế nào?

`SỰ_THẬT` Theo [IFRS Foundation — IFRS 18 Presentation and Disclosure in Financial Statements](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/) (ban hành `04/2024`, hiệu lực cho kỳ năm bắt đầu từ `01/01/2027`, thay thế IAS 1):
1. **Hai tiểu tổng bắt buộc mới trên Báo cáo kết quả kinh doanh:** Trình bày thống nhất **Lợi nhuận hoạt động (`Operating profit`)** và **Lợi nhuận trước tài chính và thuế thu nhập (`Profit before financing and income taxes`)**.
2. **Thuyết minh chỉ số tự định nghĩa (`MPM`):** Đưa các thước đo hiệu quả do ban điều hành tự định nghĩa (`Management-defined Performance Measures`) vào thuyết minh được kiểm toán (xem **[Bài 007](007-notes-and-accounting-red-flags.md)**).
3. **Chuẩn hóa điểm xuất phát và lãi vay/cổ tức trên Báo cáo lưu chuyển tiền tệ (sửa đổi IAS 7):** Phương pháp gián tiếp bắt đầu thống nhất từ **`Operating profit`**; với doanh nghiệp phi tài chính, **lãi vay đã trả** và **cổ tức đã trả** xếp cố định vào **Dòng tiền tài chính (`CFF`)**, còn **lãi và cổ tức thu được** xếp vào **Dòng tiền đầu tư (`CFI`)** ([KPMG — IFRS 18 changes to the statement of cash flows (01/06/2026)](https://kpmg.com/us/en/articles/2026/ifrs-18-changes-statement-cash-flows.html)). *(Quy định riêng của Việt Nam theo VAS và Thông tư `99/2025/TT-BTC` sẽ học tại **[Bài N3](N3-vietnam-vas-statements.md)**).*

---

## Ranh giới an toàn và Điều tôi vẫn chưa hiểu

- **Ranh giới an toàn:** Bài học này là khung đọc và kiểm tra tính nhất quán giữa 3 báo cáo tài chính, **không phải** khuyến nghị mua, bán hay nắm giữ chứng khoán.
- **Điều tôi vẫn chưa hiểu (dẫn sang Bài N2):** Vì sao phương trình `"Tổng Tài sản = Nợ phải trả + Vốn chủ sở hữu"` luôn cân bằng sau mỗi giao dịch, và các thuật ngữ `EBIT`, `EBITDA`, `EPS`, `ROA`, `ROE` được tính từng bước ra sao? *(Mở ngay **[Bài N2](N2-statement-line-items.md)**).*

## Nguồn Internet đã mở

| Nguồn | Kỳ / Phiên bản & Phạm vi | Nội dung xác minh dùng trong bài |
|---|---|---|
| [Beginners' Guide to Financial Statements — U.S. SEC](https://www.sec.gov/reportspubs/investor-publications/investorpubsbegfinstmtguide) | Hoa Kỳ; hướng dẫn chính thức của SEC (mở kiểm chứng `2026-11-06`, HTTP 200) | Vai trò của 3 báo cáo tài chính và cơ chế đối chiếu lợi nhuận với tiền mặt |
| [IAS 7 — Statement of Cash Flows, IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/) | Chuẩn mực quốc tế IFRS hiện hành | Ba dòng tiền (`CFO`, `CFI`, `CFF`) và phương pháp gián tiếp điều chỉnh vốn lưu động |
| [IFRS 18 — Presentation and Disclosure in Financial Statements, IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/) | Ban hành `04/2024`, hiệu lực từ `01/01/2027` | Thay thế IAS 1; bổ sung hai tiểu tổng bắt buộc và thuyết minh `MPM` |
| [KPMG — IFRS 18 changes to the statement of cash flows](https://kpmg.com/us/en/articles/2026/ifrs-18-changes-statement-cash-flows.html) | Nguồn thứ cấp chuyên môn; xuất bản `01/06/2026` | Sửa đổi IAS 7 theo IFRS 18: điểm xuất phát từ `Operating profit` và phân loại lãi vay, cổ tức |
| [Apple Inc. — Form 10-K FY2025 (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Năm tài chính kết thúc `27/09/2025`; nộp `31/10/2025`; `US GAAP`; triệu USD; mở kiểm chứng `2026-11-06` | Doanh thu thuần (`416.161`), Lợi nhuận ròng (`112.010`), `CFO` (`111.482`), Khấu hao (`11.698`), `CapEx` (`12.715`), Tổng tài sản (`359.241`), Nợ phải trả (`285.508`), Vốn chủ (`73.733`) |
