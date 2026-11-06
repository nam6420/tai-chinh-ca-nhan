# Bài F3 — Phân tích doanh nghiệp bất động sản Việt Nam: Vòng đời dự án, Tiền khách trả trước, Tồn kho, Trái phiếu và NAV

- Ngày cập nhật: `2026-11-05`
- Chốt dữ liệu lúc: `2026-11-05 12:00 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Đọc thông suốt báo cáo tài chính của doanh nghiệp phát triển bất động sản nhà ở và khu đô thị tại Việt Nam; phân biệt rạch ròi 4 đại lượng (`Doanh số mở bán / Pre-sales`, `Người mua trả tiền trước ngắn hạn`, `Hàng tồn kho bất động sản dở dang`, và `Doanh thu bàn giao ghi nhận trên Báo cáo kết quả kinh doanh`); kiểm tra cấu trúc nợ vay – trái phiếu theo lô và tự tay dựng mô hình Giá trị Tài sản Ròng (`RNAV` / `NAV`) chiết khấu theo tiến độ pháp lý.
- Thời lượng dự kiến: `3 buổi học (~270 phút)`
  - **Buổi 1 (90 phút):** Chuỗi giá trị dự án bất động sản Việt Nam và nghịch lý kế toán giữa dòng tiền thu trước của khách hàng (`Customer Advances`) với thời điểm ghi nhận doanh thu bàn giao theo chuẩn mực kế toán Việt Nam (`VAS`).
  - **Buổi 2 (90 phút):** Giải phẫu mục Hàng tồn kho bất động sản dở dang, chi phí lãi vay vốn hóa (`Capitalized Interest`), cấu trúc hợp tác kinh doanh (`BCC`) và lịch đáo hạn trái phiếu doanh nghiệp.
  - **Buổi 3 (90 phút):** Dựng mô hình định giá `RNAV` (`Revalued Net Asset Value`) từng dự án có trọng số rủi ro pháp lý, thực hành xử lý dữ liệu bẩn và làm 10 bài tập định lượng.
- Bài trước liên quan: [004 — Dòng tiền và chất lượng lợi nhuận](004-cash-flow-and-earnings-quality.md), [005 — Nợ, thanh khoản và khả năng sống sót](005-debt-liquidity-survival.md), [F1 — Mô hình ba báo cáo tài chính](F1-three-statement-model-sensitivity.md), [F2 — Định giá DDM, Thu nhập thặng dư và SOTP](F2-valuation-ddm-residual-sotp.md).
- Mô hình thực hành đi kèm: [`../practice/models/valuation.py`](../practice/models/valuation.py) và [`../practice/models/earnings_quality.py`](../practice/models/earnings_quality.py).
- Câu hỏi cốt lõi: Khi một chủ đầu tư công bố bán hết hàng chục nghìn tỷ đồng sản phẩm nhưng lợi nhuận quý đó lại sụt giảm (hoặc ngược lại: lợi nhuận kỷ lục nhưng dòng tiền kinh doanh âm nặng), con số nào trên bảng cân đối kế toán nói cho bạn biết sự thật?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/F3-fact-check.md), [phản biện](../reviews/F3-risk-review.md).

---

## Hiểu bài trong một phút

Một dự án bất động sản tại Việt Nam kéo dài từ **3 đến 7 năm** qua 5 bước tách biệt: (1) Xin chấp thuận chủ trương đầu tư, quy hoạch 1/500, đền bù giải phóng mặt bằng và nộp tiền sử dụng đất; (2) Xây dựng hạ tầng/móng và được Sở Xây dựng xác nhận đủ điều kiện bán nhà ở hình thành trong tương lai; (3) Mở bán, ký Hợp đồng mua bán (`HĐMB`) và thu tiền trả góp theo tiến độ; (4) Thi công hoàn thiện; và (5) Bàn giao nhà thực tế cho người mua.

Theo chuẩn mực kế toán Việt Nam (`VAS 14`, Thông tư `200/2014/TT-BTC`, kế thừa tại Thông tư `99/2025/TT-BTC`), doanh nghiệp **không được ghi nhận doanh thu và lợi nhuận khi mới ký hợp đồng hay thu tiền theo tiến độ**, mà chỉ ghi nhận khi đã **hoàn thành và bàn giao phần lớn rủi ro, lợi ích gắn liền với bất động sản cho người mua** (`SỰ_THẬT`). Vì vậy:
- Tiền khách đóng theo tiến độ trong 2–3 năm xây dựng nằm bên **Nợ phải trả** tại khoản mục **Người mua trả tiền trước ngắn hạn** (`Mã 312`). Đó là "kho lương thực" sẽ kết chuyển thành doanh thu và lợi nhuận khi dự án bàn giao (`SUY_LUẬN`).
- Tiền đền bù đất, tiền sử dụng đất, chi phí xây dựng và **chi phí lãi vay phát sinh trong giai đoạn xây dựng** được gom vào mục **Hàng tồn kho — Bất động sản để bán đang xây dựng** (`Mã 140`). Nếu dự án vướng pháp lý dừng thi công, lãi vay không còn được vốn hóa vào tồn kho mà phải hạch toán thẳng vào chi phí tài chính trong kỳ (`SỰ_THẬT`).

---

## Ôn bài cũ

- Trong [Bài F2 — Định giá DDM, Thu nhập thặng dư và SOTP](F2-valuation-ddm-residual-sotp.md) và [Bài N3 — Đặc thù báo cáo tài chính Việt Nam](N3-vietnam-vas-statements.md), ta đã nắm công cụ định giá từng phần (`SOTP` / `RNAV`) và khoản mục người mua trả tiền trước. Bài F3 áp dụng trực tiếp vào doanh nghiệp bất động sản Việt Nam.

---

## Buổi 1 — Chuỗi giá trị dự án và Bốn con số không bao giờ được cộng gộp

### 1.1. Bốn khái niệm cốt lõi trên báo cáo bất động sản

Khi đọc báo cáo thường niên hoặc bản tin nhà đầu tư của một công ty bất động sản (như Vinhomes, Khang Điền, Nam Long), người mới thường bị choáng ngợp bởi bốn con số khác nhau hoàn toàn về bản chất kế toán:

| Chỉ tiêu | Bản chất kinh tế | Vị trí trên Báo cáo tài chính (`VAS`) | Ý nghĩa đối với nhà phân tích |
|---|---|---|---|
| **1. Doanh số bán hàng mới (`Pre-sales` / `Contracted Sales`)** | Tổng giá trị hợp đồng mua bán (`HĐMB`) hoặc văn bản thỏa thuận mới ký với khách hàng trong kỳ. | **Không nằm trên BCTC** (chỉ thuyết minh trong Bản tin IR hoặc Báo cáo thường niên). | Đo sức hấp thụ thực tế của thị trường ở thời điểm hiện tại. Nếu `Pre-sales` rơi tự do, dòng tiền thu từ khách trong 4–8 quý tới sẽ cạn. |
| **2. Doanh số chưa ghi nhận (`Unbilled Bookings` / `Backlog`)** | Phần giá trị hợp đồng đã ký với khách hàng nhưng chưa bàn giao nhà nên chưa đủ điều kiện hạch toán doanh thu. | Ngoại bảng (thuyết minh quản trị). | Đo tổng quy mô doanh thu tiềm năng đang chờ bàn giao trong 1–3 năm tới. |
| **3. Người mua trả tiền trước ngắn hạn (`Customer Advances`, Mã 312)** | Số tiền mặt thực tế khách hàng đã nộp cho chủ đầu tư theo tiến độ thanh toán của hợp đồng mua bán (thường từ `30%` đến `70%` giá trị căn nhà trước khi nhận bàn giao). | **Bảng cân đối kế toán — Nợ ngắn hạn (`Mã 312`)** (hoặc `Phải trả ngắn hạn khác — Mã 319` nếu mới là tiền đặt cọc theo thỏa thuận giữ chỗ chưa lên HĐMB). | Là nguồn vốn **không phải trả lãi vay** tốt nhất của chủ đầu tư. Khi bàn giao nhà, khoản nợ này giảm xuống và chuyển hóa trực tiếp thành Doanh thu thuần. |
| **4. Doanh thu thuần bàn giao BĐS (`Recognized Revenue`, Mã 10)** | Giá trị hợp đồng của những căn hộ/biệt thự đã hoàn thiện và ký biên bản bàn giao thực tế cho khách trong kỳ. | **Báo cáo kết quả kinh doanh (`Mã 10`)**. | Là kết quả của hoạt động bán hàng từ **2–3 năm trước**, không phản ánh sức mua của thị trường ngay trong quý hiện tại. |

`Ý_KIẾN` Sai lầm phổ biến nhất của người mới là cộng `Doanh số ký hợp đồng` với `Người mua trả tiền trước` và `Doanh thu đã ghi nhận` lại với nhau, dẫn tới đếm trùng một căn nhà tới ba lần!

### 1.2. Cầu nối kế toán từ Lúc thu tiền đến Lúc bàn giao

Hãy theo dõi một căn nhà phố có giá bán chưa gồm thuế GTGT là `10,0 tỷ VND`, giá vốn đất và xây dựng là `6,0 tỷ VND` (`KỊCH_BẢN`):
- **Năm 1 (Ký HĐMB, khách đóng 30% = 3,0 tỷ VND, chủ đầu tư đã chi 2,5 tỷ VND làm hạ tầng):**
  - Tiền mặt (`Mã 110`) tăng `+3,0 tỷ` (nhưng chi `-2,5 tỷ` xây dựng nên tiền ròng giữ lại `+0,5 tỷ`).
  - Hàng tồn kho BĐS dở dang (`Mã 140`) tăng `+2,5 tỷ`.
  - Người mua trả tiền trước ngắn hạn (`Mã 312`) tăng `+3,0 tỷ`.
  - **Doanh thu = `0`**, **Lợi nhuận gộp = `0`** (`PHÉP_TÍNH`).
- **Năm 2 (Khách đóng tiếp 40% = 4,0 tỷ VND, chủ đầu tư chi nốt 3,5 tỷ VND hoàn thiện):**
  - Lũy kế Hàng tồn kho (`Mã 140`) đạt `2,5 + 3,5 = 6,0 tỷ VND`.
  - Lũy kế Người mua trả tiền trước (`Mã 312`) đạt `3,0 + 4,0 = 7,0 tỷ VND`.
  - **Doanh thu = `0`**, **Lợi nhuận gộp = `0`**, dù chủ đầu tư đã thu về `7,0 tỷ VND` tiền mặt (`PHÉP_TÍNH`)!
- **Năm 3 (Bàn giao nhà, khách đóng nốt 30% = 3,0 tỷ VND):**
  - Khoản `Người mua trả tiền trước (7,0 tỷ)` được xóa sổ khỏi Nợ phải trả, cộng với `3,0 tỷ` thu nốt để ghi nhận **Doanh thu thuần = `10,0 tỷ VND`** trên Báo cáo KQKD.
  - Khoản `Hàng tồn kho (6,0 tỷ)` được xóa sổ khỏi Tài sản để ghi nhận **Giá vốn hàng bán = `6,0 tỷ VND`**.
  - **Lợi nhuận gộp = `10,0 - 6,0 = 4,0 tỷ VND`** (`Biên lãi gộp = 40,0%`), nhưng dòng tiền mặt thực thu thêm trong Năm 3 chỉ còn `3,0 tỷ VND` (`PHÉP_TÍNH`).

Cơ chế này giải thích vì sao ở đỉnh điểm bàn giao dự án (như Năm 3), Báo cáo KQKD của doanh nghiệp bất động sản trông cực kỳ rực rỡ (`P/E` tampak rất rẻ, chỉ `5x–7x`), nhưng nếu trong Năm 3 họ không mở bán được dự án gối đầu mới (`Người mua trả tiền trước` sụt giảm mạnh), thì Năm 4 và Năm 5 doanh thu sẽ rơi xuống vực thẳm (`SUY_LUẬN`).

---

## Buổi 2 — Giải phẫu Hàng tồn kho, Vốn hóa lãi vay, Hợp tác BCC và Trái phiếu

### 2.1. Hàng tồn kho BĐS dở dang: Sổ sách khác xa giá thị trường

Trên BCTC của doanh nghiệp bất động sản, Hàng tồn kho (`Mã 140`) thường chiếm từ `40%` đến `70%` tổng tài sản. Khi mở Thuyết minh Hàng tồn kho, bạn bắt buộc phải tách làm 3 nhóm chất lượng:
1. **Nhóm A — Dự án đã có quy hoạch 1/500, đã nộp tiền sử dụng đất, đang thi công và mở bán:** Tồn kho này có tính thanh khoản cao, đi kèm với số dư `Người mua trả tiền trước` lớn ở bên phần Nguồn vốn.
2. **Nhóm B — Quỹ đất đang đền bù dở dang ("đất da báo") hoặc chờ tính tiền sử dụng đất:** Dù giá đất thị trường xung quanh có thể đã tăng gấp đôi so với giá gốc ghi sổ, nhưng chừng nào chưa đền bù xong 100% diện tích và chưa nộp tiền sử dụng đất theo bảng giá đất mới, dự án chưa thể khởi công hay mở bán. Tồn kho này là **vốn chết tạm thời** (`SUY_LUẬN`).
3. **Nhóm C — Bất động sản hàng hóa đã xây xong nhưng tồn đọng nhiều năm không bán được:** Rủi ro phải trích lập dự phòng giảm giá hàng tồn kho hoặc đang bị thế chấp toàn bộ tại ngân hàng để vay nợ.

### 2.2. Bẫy "Vốn hóa chi phí lãi vay" (`Capitalized Interest` — Chuẩn mực VAS 16)

Theo Chuẩn mực kế toán Việt Nam số 16 (`VAS 16 — Chi phí đi vay`), chi phí lãi vay phục vụ trực tiếp cho việc đầu tư xây dựng tài sản dở dang được **vốn hóa (cộng thẳng) vào giá trị Hàng tồn kho** thay vì ghi vào Chi phí tài chính trên Báo cáo KQKD (`SỰ_THẬT`).

Hãy xem điều gì xảy ra khi một chủ đầu tư vay `5.000 tỷ VND` với lãi suất `11%/năm` (tức phải trả `550 tỷ VND` tiền lãi mỗi năm) để làm dự án (`KỊCH_BẢN`):
- **Khi dự án đang thi công bình thường:** Công ty vốn hóa `450 tỷ VND` lãi vay vào Hàng tồn kho (`Mã 140`) và chỉ ghi `100 tỷ VND` vào Chi phí tài chính (`Mã 23`). Báo cáo KQKD vẫn báo lãi đẹp, trong khi trên Báo cáo lưu chuyển tiền tệ, tiền lãi thực trả vẫn rút ra `-550 tỷ VND`!
- **Khi dự án bị đình trệ thi công do vướng pháp lý:** Theo `VAS 16`, việc vốn hóa lãi vay phải **tạm ngừng** trong giai đoạn dự án ngừng triển khai xây dựng. Lập tức, cả `550 tỷ VND` lãi vay đập thẳng vào Báo cáo KQKD, làm công ty chuyển từ lãi sang lỗ nặng; đồng thời giá vốn tồn kho đội lên làm biên lãi gộp lúc bàn giao sau này bị bào mòn (`PHÉP_TÍNH`).

Để kiểm tra chất lượng lợi nhuận và mức độ vốn hóa, bạn có thể dùng hàm đối chiếu tỷ số chất lượng lợi nhuận và đòn bẩy trong [`../practice/models/earnings_quality.py`](../practice/models/earnings_quality.py).

### 2.3. Phải thu Hợp tác kinh doanh (`BCC`) và Lịch đáo hạn Trái phiếu

Nhiều doanh nghiệp đẩy hàng chục nghìn tỷ đồng sang **Phải thu ngắn hạn/dài hạn khác (`Mã 136 / Mã 216`)** dưới dạng tiền đặt cọc M&A hoặc vốn góp Hợp đồng Hợp tác Kinh doanh (`BCC`). `SUY_LUẬN` Khi tiền nằm ở `Phải thu BCC` kéo dài nhiều năm không chuyển thành Hàng tồn kho dự án, phải kiểm tra xem đó là quỹ đất thật hay kênh rút tiền cho các công ty sân sau vay không tài sản đảm bảo. Đồng thời, khi phân tích thanh khoản (Bài [005](005-debt-liquidity-survival.md)), phải dựng **lịch đáo hạn nợ vay và trái phiếu 12–24 tháng tới** đối chiếu với tiền mặt tự do (trừ tiền gửi bị phong tỏa) và dòng tiền thu tiếp từ khách hàng.

---

## 3. Ví dụ từ nguồn thật: Trái phiếu VHM12501 trên VSDC và Thông tư 99/2025/TT-BTC

1. **Nguồn pháp lý kế toán (`Thông tư 99/2025/TT-BTC`):**
   - `SỰ_THẬT`: [Thông tư số 99/2025/TT-BTC trên Công báo Chính phủ](https://congbao.chinhphu.vn/van-ban/thong-tu-so-99-2025-tt-btc-46529.htm) quy định chế độ kế toán doanh nghiệp hiệu lực từ `01/01/2026`.
   - `SUY_LUẬN`: Nhà phân tích phải mở trực tiếp Thuyết minh Chính sách kế toán của doanh nghiệp để kiểm tra thời điểm ghi nhận doanh thu bàn giao, nguyên tắc phân bổ giá vốn đất và vốn hóa lãi vay, không suy đoán thu tiền ứng trước tự động là doanh thu.

2. **Nguồn lưu ký chứng khoán (`VSDC` — Mã trái phiếu `VHM12501`):**
   - `SỰ_THẬT`: Theo [VSDC — Thông báo mã VHM12501](https://vsdc.vn/en/ad/186503) (`22/08/2025`), mã trái phiếu `VHM12501` có số lượng đăng ký `80.000` trái phiếu, mệnh giá `100.000.000 VND/trái phiếu` (`100 triệu VND`).
   - `PHÉP_TÍNH`: Tổng mệnh giá đăng ký = $80.000 \times 100.000.000\text{ VND} = 8.000\text{ tỷ VND}$.
   - `SỰ_THẬT`: [VSDC — Thông báo chốt danh sách thanh toán lãi kỳ thứ 5](https://vsdc.vn/en/ad/201471) (`19/10/2026`) công bố ngày đăng ký cuối cùng và lịch trả lãi dự kiến kỳ thứ 5.
   - **Bài học kiểm chứng (`SUY_LUẬN` & `CHƯA_BIẾT`):** Thông báo đăng ký lưu ký và chốt quyền trả lãi trên VSDC chỉ xác nhận thông số đăng ký và lịch thực hiện quyền, **không tự chứng minh** dư nợ gốc đang lưu hành sau các đợt mua lại trước hạn hay năng lực dòng tiền trả gốc khi đáo hạn. Muốn biết dư nợ gốc còn lại và tài sản thế chấp, phải mở **Thuyết minh Vay và nợ thuê tài chính** trên BCTC kiểm toán kết hợp công bố trên `CBonds HNX`.

---

## Buổi 3 — Dựng mô hình định giá RNAV (Revalued Net Asset Value) có điều kiện

### 4.1. Vì sao P/E và P/B truyền thống dễ đánh lừa trong ngành bất động sản?

- **`P/E` bị méo theo điểm rơi bàn giao:** Một công ty sở hữu quỹ đất sạch 100 ha đang xây dựng rầm rộ có thể có `P/E = 50x` (vì chưa bàn giao nên lợi nhuận thấp), nhưng năm sau khi bàn giao đồng loạt thì `P/E` tụt xuống `4x`. Ngược lại, một công ty vừa bàn giao hết dự án cuối cùng và không còn quỹ đất mới sẽ có `P/E = 4x` ngay tại đỉnh chu kỳ lợi nhuận!
- **`P/B` bị méo theo tuổi của quỹ đất:** Quỹ đất mua từ 10 năm trước được ghi nhận theo giá gốc lịch sử thấp hơn nhiều lần giá thị trường hiện hành; nhưng quỹ đất vừa mua lại ở đỉnh sốt đất bằng nợ vay lại có giá sổ sách sát (hoặc cao hơn) giá trị thực.

Vì vậy, phương pháp chuẩn mực nhất để định giá doanh nghiệp phát triển bất động sản là **Giá trị Tài sản Ròng đánh giá lại (`RNAV` — Revalued Net Asset Value)**, một nhánh chuyên biệt của định giá Tổng các thành phần (`SOTP` trong Bài [F2](F2-valuation-ddm-residual-sotp.md) và mô-đun [`../practice/models/valuation.py`](../practice/models/valuation.py)).

### 4.2. Công thức 5 bước tính RNAV và Kịch bản chiết khấu pháp lý

Với mỗi dự án $i$ trong danh mục của doanh nghiệp, giá trị dòng tiền ròng thuộc về chủ đầu tư được ước tính qua 5 bước:

$$\text{CF}_{i, t} = \text{Tiền thu bán hàng}_{i, t} - \text{Tiền sử dụng đất còn phải nộp}_{i, t} - \text{Chi phí xây dựng & hạ tầng}_{i, t} - \text{Chi phí bán hàng & quản lý}_{i, t} - \text{Thuế TNDN}_{i, t}$$

Giá trị hiện tại ròng của dự án $i$ thuộc về cổ đông công ty mẹ là:

$$\text{NPV}_i = \theta_i \times w_{\text{pháp lý}, i} \times \sum_{t=1}^{T_i} \frac{\text{CF}_{i, t}}{(1 + r)^t}$$

Trong đó:
- $\theta_i$: Tỷ lệ lợi ích kinh tế thực tế của công ty mẹ tại dự án $i$ (ví dụ: công ty con sở hữu `70%` thì $\theta_i = 0,70$; không bao giờ cộng 100% dự án liên doanh khi chỉ nắm `50%`!).
- $r$: Chi phí vốn chiết khấu của dự án (thường bằng `WACC` từ `11%` đến `15%/năm` tùy rủi ro thực thi).
- $w_{\text{pháp lý}, i}$: Trọng số điều chỉnh xác suất/tiến độ pháp lý (hoặc thể hiện qua việc lùi thời điểm bắt đầu có dòng tiền $t$ thêm 2–4 năm đối với dự án chưa có quy hoạch 1/500 hay chưa tính xong tiền sử dụng đất).

Sau khi cộng tổng giá trị các dự án, ta cầu nối sang `RNAV` vốn chủ sở hữu:

$$\text{RNAV}_{\text{Vốn chủ}} = \sum_{i=1}^{N} \text{NPV}_i + \text{Tài sản vận hành tạo dòng tiền (Khu công nghiệp, TTTM, Văn phòng)} + \text{Tiền mặt & tương đương tiền tự do} - \text{Tổng nợ vay (Ngân hàng + Trái phiếu)}$$

### 4.3. Ví dụ tính toán tái lập bằng mô hình

Giả sử Công ty Bất động sản X có `100 triệu` cổ phiếu đang lưu hành, tiền mặt tự do `300 tỷ VND`, tổng nợ vay ngân hàng và trái phiếu `1.200 tỷ VND`, và danh mục gồm 2 dự án (`KỊCH_BẢN`):
- **Dự án A (Đã có GPXD, đang mở bán, sở hữu $\theta_A = 100\%$):** Dự kiến bàn giao và thu ròng sau khi trừ chi phí xây dựng, bán hàng, thuế trong 2 năm tới lần lượt là `CF_1 = 900 tỷ VND` và `CF_2 = 1.100 tỷ VND`. Với suất chiết khấu $r = 12\%/\text{năm}$:
  $$\text{NPV}_A = \frac{900}{1,12^1} + \frac{1.100}{1,12^2} = 803,57 + 876,91 = 1.680,48\text{ tỷ VND}\quad (\text{PHÉP\_TÍNH})$$
- **Dự án B (Đang hoàn thiện pháp lý, sở hữu liên doanh $\theta_B = 60\%$):** Tổng dòng tiền ròng toàn dự án (100%) nếu làm xong ước đạt giá trị hiện tại `1.500 tỷ VND`, nhưng vì mới xong quy hoạch 1/500 và đang chờ định giá tiền sử dụng đất nên áp hệ số thận trọng $w_{\text{pháp lý}, B} = 0,75$:
  $$\text{NPV}_B = 0,60 \times 0,75 \times 1.500 = 675,00\text{ tỷ VND}\quad (\text{PHÉP\_TÍNH})$$
- **Tổng `RNAV` vốn chủ sở hữu của Công ty X:**
  $$\text{RNAV} = 1.680,48 + 675,00 + 300,00 - 1.200,00 = 1.455,48\text{ tỷ VND}\quad (\text{PHÉP\_TÍNH})$$
  $$\text{RNAV mỗi cổ phiếu} = \frac{1.455,48\text{ tỷ VND}}{100\text{ triệu CP}} = 14.555\text{ VND/cổ phiếu}$$
- Trên thị trường chứng khoán Việt Nam, cổ phiếu bất động sản thường giao dịch ở một mức **chiết khấu so với `RNAV` (`Discount to RNAV`) từ `15%` đến `40%`** tùy thuộc vào uy tín bàn giao của ban lãnh đạo, tính minh bạch của giao dịch bên liên quan và áp lực đáo hạn trái phiếu ngắn hạn (`SUY_LUẬN`).

---

## 5. Bài làm với dữ liệu thiếu hoặc lệch (Dirty-Data Exercise)

### Tình huống dữ liệu bẩn
Bạn đang phân tích Công ty Bất động sản Y cuối năm 2025. Bản trình chiếu gặp gỡ nhà đầu tư (`IR Presentation`) quảng cáo:
> *"Năm 2025, Công ty đạt tổng doanh số ký hợp đồng (`Pre-sales`) 4.500 tỷ VND, tồn kho quỹ đất theo giá thị trường ước đạt 12.000 tỷ VND, trong khi vốn hóa thị trường chỉ có 3.600 tỷ VND — cổ phiếu đang rẻ hơn 70% giá trị thực!"*

Tuy nhiên, khi mở **Báo cáo tài chính hợp nhất kiểm toán năm 2025** của Công ty Y, bạn phát hiện 4 sự thật bị ẩn giấu sau lớp ngôn từ quảng cáo (`KỊCH_BẢN`):
1. Trong `4.500 tỷ VND` doanh số công bố, khoản mục **Người mua trả tiền trước ngắn hạn (`Mã 312`)** trên Bảng cân đối kế toán chỉ tăng thêm đúng `+180 tỷ VND`; phần còn lại nằm ở "phiếu đăng ký nguyện vọng" của các sàn môi giới liên kết và chưa hề thu được tiền thật vào tài khoản công ty.
2. Mục **Hàng tồn kho (`Mã 140`)** trên BCTC ghi nhận theo giá gốc là `4.200 tỷ VND`, nhưng Thuyết minh Hàng tồn kho cho biết `3.100 tỷ VND` trong số đó thuộc Dự án Khu đô thị M đang tạm dừng thi công từ năm 2023 để chờ điều chỉnh quy hoạch và xác định lại tiền sử dụng đất; toàn bộ quyền phát triển dự án đã thế chấp cho lô trái phiếu `2.500 tỷ VND` đáo hạn vào tháng 09/2026.
3. Trong năm 2025, Công ty Y vẫn tiếp tục **vốn hóa `240 tỷ VND` chi phí lãi vay** của Dự án M vào Hàng tồn kho thay vì ghi vào chi phí tài chính, nhờ đó Báo cáo KQKD báo lãi trước thuế `+90 tỷ VND`. Kiểm toán viên đã đưa ra **Ý kiến kiểm toán ngoại trừ** đối với khoản lãi vay vốn hóa `240 tỷ VND` này.
4. Tiền và tương đương tiền cuối năm là `410 tỷ VND`, nhưng Thuyết minh Tiền cho biết `360 tỷ VND` là tiền gửi có kỳ hạn đang bị ngân hàng phong tỏa để bảo lãnh nghĩa vụ trái phiếu.

### Quy trình bóc tách và làm sạch dữ liệu
1. **Loại bỏ ảo giác `Pre-sales`:** Không dùng con số `4.500 tỷ VND` tự công bố để dự phóng doanh thu; chỉ ghi nhận dòng tiền khách hàng thực nộp tăng thêm `+180 tỷ VND` tại `Mã 312` (`SUY_LUẬN`).
2. **Điều chỉnh lại Lợi nhuận trước thuế theo ý kiến kiểm toán ngoại trừ:** Vì Dự án M đã dừng thi công từ năm 2023, theo `VAS 16`, khoản lãi vay `240 tỷ VND` không được phép vốn hóa vào tồn kho. Nếu hạch toán đúng vào chi phí tài chính, Lợi nhuận trước thuế thực chất của Công ty Y năm 2025 là:
   $$\text{EBT}_{\text{điều chỉnh}} = 90 - 240 = -150\text{ tỷ VND (Lỗ trước thuế)}\quad (\text{PHÉP\_TÍNH})$$
   Đồng thời giá trị Hàng tồn kho thực tế phải giảm đi `240 tỷ VND` phần lãi vay treo sai quy định.
3. **Đánh giá bức tường thanh khoản tháng 09/2026:** Tiền mặt tự do thực sự chỉ còn $410 - 360 = 50\text{ tỷ VND}$ (`PHÉP_TÍNH`), trong khi dòng tiền thu từ khách hàng mới chỉ đạt `180 tỷ VND` và lô trái phiếu `2.500 tỷ VND` sắp đáo hạn trong 9 tháng tới. Rủi ro mất thanh khoản / tái cơ cấu nợ bắt buộc là **rất cao**, làm cho con số "quỹ đất theo giá thị trường 12.000 tỷ VND" không thể hiện thực hóa cho cổ đông phổ thông nếu dự án bị xử lý tài sản đảm bảo.

---

## 6. Sai ở đâu? (Bắt lỗi suy luận)

Hãy chỉ ra chỗ sai trong câu nói sau của một nhà đầu tư cá nhân:

> *"Tôi vừa mở Bảng cân đối kế toán Quý 4 của Công ty Bất động sản Z thấy mục Nợ phải trả tăng vọt thêm 6.000 tỷ VND chỉ trong một năm, làm tỷ lệ Tổng Nợ phải trả / Vốn chủ sở hữu tăng từ 1,2 lần lên 2,1 lần. Một công ty bất động sản mà nợ phình to nhanh như vậy chắc chắn đang vay nợ quá đà và sắp gặp nguy hiểm!"*

### Phân tích chỗ sai
1. **Nhầm lẫn "Nợ phải trả chiếm dụng từ khách hàng" với "Nợ vay chịu lãi":** Trên Bảng cân đối kế toán của doanh nghiệp bất động sản, **Tổng Nợ phải trả (`Mã 300`)** bao gồm hai thành phần đối lập hoàn toàn về rủi ro:
   - **Nợ vay tài chính chịu lãi (`Mã 320 + Mã 338`):** Vay ngân hàng và phát hành trái phiếu — đây mới là khoản nợ bắt buộc phải trả bằng tiền mặt kèm lãi vay định kỳ.
   - **Người mua trả tiền trước ngắn hạn (`Mã 312`):** Tiền khách hàng đã đóng khi mua nhà hình thành trong tương lai — đây là khoản nợ **không chịu lãi vay** và sẽ được thanh toán bằng cách **bàn giao căn nhà** (chuyển thành Doanh thu và Lợi nhuận), chứ không phải trả lại tiền mặt!
2. **Cách kiểm tra đúng:** Phải mở chi tiết cấu trúc `6.000 tỷ VND` nợ tăng thêm. Nếu `5.500 tỷ VND` trong số đó là `Người mua trả tiền trước (Mã 312)` tăng lên nhờ mở bán thành công dự án mới, còn nợ vay ngân hàng và trái phiếu giảm `-500 tỷ VND`, thì sức khỏe tài chính của Công ty Z thực chất đang **tốt lên vượt bậc**, chứ không phải xấu đi (`SUY_LUẬN`)! Luôn dùng tỷ số **Nợ vay ròng chịu lãi / Vốn chủ sở hữu (`Net Debt / Equity`)** thay vì `Tổng Nợ phải trả / Vốn chủ sở hữu`.

---

## 7. Bài tập (10 câu)

1. Phân biệt thời điểm phát sinh của 4 chỉ tiêu: `Doanh số mở bán (Pre-sales)`, `Người mua trả tiền trước (Mã 312)`, `Hàng tồn kho BĐS dở dang (Mã 140)` và `Doanh thu thuần bàn giao BĐS (Mã 10)`.
2. Một dự án căn hộ ký hợp đồng bán 500 căn với tổng giá trị (chưa gồm VAT) là `2.000 tỷ VND`. Trong năm 2025, khách hàng đã đóng `40%` tiến độ (`800 tỷ VND`), chủ đầu tư đã chi `650 tỷ VND` xây dựng phần thô nhưng dự án dự kiến cuối năm 2026 mới bàn giao. Hỏi trong năm 2025, doanh thu thuần và lợi nhuận gộp ghi nhận trên Báo cáo KQKD của dự án này là bao nhiêu? Số dư `Mã 312` và `Mã 140` thay đổi thế nào?
3. Tiếp nối Câu 2: Sang năm 2026, chủ đầu tư chi thêm `550 tỷ VND` để hoàn thiện (tổng giá vốn xây dựng và đất hoàn chỉnh là `1.200 tỷ VND`), bàn giao toàn bộ 500 căn cho khách và thu nốt `60%` tiền còn lại (`1.200 tỷ VND`). Tính Doanh thu thuần, Giá vốn hàng bán, Lợi nhuận gộp và biên lợi nhuận gộp ghi nhận trong năm 2026.
4. Một doanh nghiệp bất động sản có tổng dư nợ vay ngân hàng và trái phiếu là `4.000 tỷ VND` với lãi suất bình quân `10,5%/năm`. Trong năm, công ty vốn hóa `320 tỷ VND` lãi vay vào Hàng tồn kho và chỉ hạch toán phần còn lại vào Chi phí tài chính trên Báo cáo KQKD. Tính số tiền lãi vay hạch toán vào Chi phí tài chính và tổng tiền lãi vay thực phát sinh trong năm.
5. Nếu dự án trong Câu 4 bị cơ quan chức năng yêu cầu dừng thi công trọn năm sau để rà soát pháp lý, theo Chuẩn mực kế toán `VAS 16`, chi phí tài chính trên Báo cáo KQKD năm sau sẽ thay đổi thế nào (giả sử dư nợ và lãi suất không đổi)?
6. Một dự án khu dân cư dự kiến thu bán hàng `1.500 tỷ VND`, chi phí hoàn thiện và bán hàng còn lại `850 tỷ VND`, thuế và phí phải nộp `90 tỷ VND`. Dự án do Công ty con thực hiện, trong đó Công ty mẹ sở hữu `60%` vốn cổ phần, và tại cấp công ty dự án đang có khoản vay ngân hàng `160 tỷ VND` (tiền mặt dự án bằng `0`). Tính `NAV` tĩnh của toàn dự án (100%) và phần `NAV` tĩnh thuộc về cổ đông Công ty mẹ (bỏ qua chiết khấu thời gian).
7. Theo thông báo đăng ký mã trái phiếu `VHM12501` trên VSDC, nếu một lô trái phiếu có `80.000` trái phiếu với mệnh giá `100 triệu VND/trái phiếu` và lãi suất danh nghĩa giả định `12%/năm` trả lãi 6 tháng/lần, hãy tính tổng mệnh giá đăng ký của lô trái phiếu và tổng số tiền lãi phải trả cho mỗi kỳ 6 tháng (giả sử chưa mua lại trước hạn và tính tròn nửa năm).
8. Một chủ đầu tư có Tổng tài sản `20.000 tỷ VND`, Vốn chủ sở hữu `6.000 tỷ VND`, Tổng nợ phải trả `14.000 tỷ VND`. Trong Tổng nợ phải trả có `5.200 tỷ VND` Người mua trả tiền trước ngắn hạn, `1.800 tỷ VND` Phải trả nhà thầu và thuế, phần còn lại là Vay ngắn hạn và dài hạn chịu lãi. Tiền và tương đương tiền không bị phong tỏa là `1.000 tỷ VND`. Tính tổng nợ vay chịu lãi, nợ vay ròng (`Net Debt`) và tỷ lệ `Net Debt / Equity`.
9. Dự án K dự kiến tạo dòng tiền ròng sau thuế thuộc về công ty mẹ trong 3 năm tới lần lượt là `CF_1 = 400 tỷ VND`, `CF_2 = 700 tỷ VND`, `CF_3 = 900 tỷ VND`. Tính giá trị hiện tại ròng (`NPV`) của dự án với chi phí vốn $r = 13\%/\text{năm}$. Nếu dự án bị chậm pháp lý lùi toàn bộ dòng tiền lại đúng 1 năm (`CF_1 = 0`, `CF_2 = 400`, `CF_3 = 700`, `CF_4 = 900`), `NPV` bị sụt giảm bao nhiêu tỷ VND và bao nhiêu phần trăm?
10. Mở mô-đun [`../practice/models/valuation.py`](../practice/models/valuation.py), trình bày cách sử dụng hàm định giá tổng các thành phần (`sotp_equity_value`) để tổng hợp `RNAV` của một tập đoàn bất động sản gồm 3 dự án nhà ở, 1 mảng cho thuê khu công nghiệp và trừ đi nợ vay ròng cấp tập đoàn.

---

## 8. Đáp án chi tiết

1. **Bốn chỉ tiêu khác nhau hoàn toàn về mốc thời gian:**
   - `Pre-sales`: Phát sinh ngay khi ký HĐMB/thỏa thuận với khách (ngoại bảng).
   - `Người mua trả tiền trước (Mã 312)`: Phát sinh khi khách nộp tiền theo từng đợt tiến độ (nằm ở Nợ ngắn hạn).
   - `Hàng tồn kho BĐS dở dang (Mã 140)`: Tích lũy toàn bộ chi phí đất, xây dựng, lãi vay vốn hóa trong suốt quá trình làm dự án (nằm ở Tài sản ngắn hạn).
   - `Doanh thu thuần (Mã 10)`: Chỉ được ghi nhận tại thời điểm hoàn thành và bàn giao nhà thực tế cho khách hàng (`SỰ_THẬT`).
2. **Năm 2025 (Chưa bàn giao):**
   - Doanh thu thuần ghi nhận trên KQKD = **`0 tỷ VND`**; Lợi nhuận gộp = **`0 tỷ VND`**.
   - Trên Bảng cân đối kế toán: `Người mua trả tiền trước (Mã 312)` tăng **`+800 tỷ VND`**; `Hàng tồn kho (Mã 140)` tăng **`+650 tỷ VND`** (`PHÉP_TÍNH`).
3. **Năm 2026 (Bàn giao toàn bộ 500 căn):**
   - Doanh thu thuần ghi nhận = **`2.000 tỷ VND`** (`800 tỷ` kết chuyển từ `Mã 312` + `1.200 tỷ` thu nốt).
   - Giá vốn hàng bán = **`1.200 tỷ VND`** (`650 + 550 tỷ` kết chuyển từ `Mã 140`).
   - Lợi nhuận gộp = `2.000 - 1.200 = 800 tỷ VND`; Biên lợi nhuận gộp = `800 / 2.000 = 40,0%` (`PHÉP_TÍNH`).
4. **Chi phí lãi vay và vốn hóa:**
   - Tổng tiền lãi vay phát sinh trong năm = $4.000 \times 10,5\% = 420\text{ tỷ VND}$.
   - Phần vốn hóa vào Hàng tồn kho = `320 tỷ VND`.
   - Phần ghi nhận vào Chi phí tài chính trên Báo cáo KQKD = $420 - 320 = 100\text{ tỷ VND}$ (`PHÉP_TÍNH`).
5. **Khi dự án dừng thi công trọn năm sau:** Theo `VAS 16`, công ty không được phép vốn hóa lãi vay trong thời gian ngừng thi công kéo dài. Toàn bộ **`420 tỷ VND`** lãi vay phải hạch toán thẳng vào Chi phí tài chính trên Báo cáo KQKD (tăng thêm `+320 tỷ VND` chi phí so với năm trước), làm lợi nhuận trước thuế sụt giảm tương ứng `320 tỷ VND` (`PHÉP_TÍNH`).
6. **Tính `NAV` tĩnh dự án liên doanh (`60%`):**
   - `NAV` tĩnh toàn dự án (100%) = $1.500 - 850 - 90 - 160 = 400\text{ tỷ VND}$.
   - Phần `NAV` tĩnh thuộc về cổ đông Công ty mẹ (`60%`) = $400 \times 60\% = 240\text{ tỷ VND}$ (`PHÉP_TÍNH`). (Tuyệt đối không lấy 100% là `400 tỷ VND` cộng vào vốn chủ công ty mẹ).
7. **Tính quy mô và lãi kỳ 6 tháng của lô trái phiếu:**
   - Tổng mệnh giá đăng ký = $80.000 \times 100\text{ triệu VND} = 8.000\text{ tỷ VND}$.
   - Tiền lãi mỗi kỳ 6 tháng (giả định tròn `0,5` năm trên mệnh giá `8.000 tỷ VND`) = $8.000 \times 12\% \times 0,5 = 480\text{ tỷ VND}$ (`PHÉP_TÍNH`).
8. **Bóc tách Nợ vay chịu lãi và `Net Debt / Equity`:**
   - Tổng nợ vay chịu lãi = $14.000 - 5.200 - 1.800 = 7.000\text{ tỷ VND}$.
   - Nợ vay ròng (`Net Debt`) = $7.000 - 1.000\text{ (tiền tự do)} = 6.000\text{ tỷ VND}$.
   - Tỷ lệ `Net Debt / Equity` = $6.000 / 6.000 = 1,00\text{ lần}$ (`100%`), thấp hơn rất nhiều so với tỷ lệ `Tổng nợ phải trả / VCSH` là $14.000 / 6.000 = 2,33\text{ lần}$ (`PHÉP_TÍNH`).
9. **Tác động của việc chậm pháp lý 1 năm lên `NPV` ($r = 13\%$):**
   - Khi đúng tiến độ:
     $$\text{NPV}_{\text{gốc}} = \frac{400}{1,13^1} + \frac{700}{1,13^2} + \frac{900}{1,13^3} = 353,98 + 548,20 + 623,75 = 1.525,93\text{ tỷ VND}$$
   - Khi bị lùi tiến độ đúng 1 năm (`NPV` mới bằng $\text{NPV}_{\text{gốc}} / 1,13$):
     $$\text{NPV}_{\text{trễ 1 năm}} = \frac{1.525,93}{1,13} = 1.350,38\text{ tỷ VND}$$
   - Giá trị dự án bốc hơi: $1.525,93 - 1.350,38 = 175,55\text{ tỷ VND}$ (giảm đúng `-11,50%`, tức $1 - 1/1,13$) chỉ vì chậm pháp lý 1 năm (`PHÉP_TÍNH`)!
10. **Ứng dụng `sotp_equity_value` trong [`../practice/models/valuation.py`](../practice/models/valuation.py):**
    - Truyền danh sách giá trị hiện tại ròng đã nhân tỷ lệ sở hữu $\theta_i$ của 3 dự án nhà ở cùng giá trị mảng Khu công nghiệp vào tham số `segment_values`, cộng `cash` (tiền mặt tự do không bị phong tỏa) và trừ `debt` (tổng nợ vay ngân hàng + trái phiếu cấp tập đoàn) để thu được `RNAV` vốn chủ sở hữu hợp nhất một cách minh bạch, tái lập được bằng kiểm thử tự động.

---

## 9. Kiểm tra chuyển bài (Transfer Check)

Trước khi chuyển sang Bài [F4 — Đọc ngân hàng Việt Nam: biên lãi, nợ xấu và vốn](F4-vietnam-bank-analysis.md), hãy tự kiểm tra 3 kỹ năng liên thông sau:
1. **Chuyển từ Bất động sản sang Ngân hàng (`F3 -> F4`):** Khi một dự án bất động sản bị vướng pháp lý dừng thi công như trong Buổi 2, chủ đầu tư không thu được tiền khách hàng trả tiếp và không trả được lãi trái phiếu/khoản vay ngân hàng. Hãy giải thích khoản vay của chủ đầu tư đó và khoản vay mua nhà của người dân tại dự án đó sẽ dịch chuyển như thế nào giữa 5 nhóm nợ trên báo cáo tài chính của Ngân hàng ở Bài [F4](F4-vietnam-bank-analysis.md)?
2. **Kiểm tra dòng tiền chất lượng cao:** Khi nhìn vào hai doanh nghiệp bất động sản có cùng vốn hóa `10.000 tỷ VND`, một bên có `Người mua trả tiền trước = 6.500 tỷ VND` và `Nợ vay ròng = 800 tỷ VND`, bên kia có `Người mua trả tiền trước = 300 tỷ VND` và `Nợ vay ròng = 7.200 tỷ VND`, bạn đã phân biệt được ngay bên nào có doanh thu bàn giao chắc chắn trong 2 năm tới chưa?
3. **Kỷ luật tra cứu nguồn gốc:** Bạn đã nắm vững cách đối chiếu chéo giữa Thông báo lưu ký trái phiếu trên `VSDC` / `CBonds HNX` với Thuyết minh Vay và nợ thuê tài chính trên BCTC kiểm toán chưa?

---

## 10. Lỗi thường gặp và ranh giới an toàn

- **Ba lỗi phân tích chí mạng:** (1) Nhầm doanh số ký hợp đồng (`Pre-sales`) với doanh thu kế toán đã ghi nhận; (2) Lấy giá trị Hàng tồn kho trên sổ sách cộng ngang làm `NAV` mà không kiểm tra tình trạng pháp lý, thế chấp và chi phí lãi vay vốn hóa; (3) Đọc thông báo mệnh giá đăng ký trái phiếu cũ rồi kết luận ngay đó là dư nợ hiện hành mà không kiểm tra các đợt mua lại trước hạn hoặc gia hạn kỳ hạn.
- **Ranh giới an toàn:** Bài học cung cấp khung kế toán và mô hình định giá `RNAV` có điều kiện để phục vụ học tập; mọi con số về mã trái phiếu `VHM12501` chỉ minh họa kỹ năng đọc văn bản lưu ký gốc, tuyệt đối không phải dự báo tiến độ dự án hay khuyến nghị mua/bán cổ phiếu, trái phiếu.

## Nguồn Internet đã mở

- Chốt kiểm tra trực tuyến lúc `2026-11-05 12:00 UTC+7`:
  1. [Công báo Chính phủ — Thông tư số 99/2025/TT-BTC](https://congbao.chinhphu.vn/van-ban/thong-tu-so-99-2025-tt-btc-46529.htm), ban hành chế độ kế toán doanh nghiệp hiệu lực từ `01/01/2026`.
  2. [Tổng công ty Lưu ký và Bù trừ chứng khoán Việt Nam (VSDC) — Thông báo đăng ký mã trái phiếu VHM12501](https://vsdc.vn/en/ad/186503), ngày `22/08/2025` (`80.000` trái phiếu, mệnh giá `100 triệu VND/trái phiếu`).
  3. [VSDC — Thông báo ngày đăng ký cuối cùng thanh toán lãi kỳ thứ 5 mã VHM12501](https://vsdc.vn/en/ad/201471), ngày `19/10/2026`.
