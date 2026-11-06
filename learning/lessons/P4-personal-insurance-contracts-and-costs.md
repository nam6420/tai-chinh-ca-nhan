# Bài P4 — Đọc hợp đồng bảo hiểm cá nhân: cấu trúc phí, điều khoản loại trừ và ranh giới giữa bảo vệ với đầu tư

- Ngày: `2026-11-05`
- Chốt dữ liệu lúc: `2026-11-05 10:35 UTC+7 (Asia/Ho_Chi_Minh)`
- Bậc chiều sâu: `Bậc S — 3 buổi học, 10 bài tập + mô hình Python`
- Mục tiêu: Đọc và bóc tách hợp đồng bảo hiểm nhân thọ/sức khỏe theo `Luật KDBH (31/VBHN-VPQH)`, `Nghị định 46/2023/NĐ-CP` và `VBHN 44/2026/VBHN-TT-BTC` (`29/09/2026`); phân biệt 5 dòng sản phẩm (`Term Life`, `Whole Life`, `Endowment`, `UL`, `ILP`); tự tính 6 lớp phí (`Mẫu 22-NT`, `Mẫu 23-NT`), Giá trị tài khoản (`Account Value`), Giá trị hoàn lại (`Surrender Value`) và so sánh 10 năm giữa **"Mua bảo hiểm liên kết đầu tư (`UL`)"** với **"Mua bảo hiểm tử kỳ + Tự đầu tư phần chênh lệch (`BTID`)"**.
- Bài trước liên quan: [P1](P1-budget-emergency-fund-insurance.md), [P2](P2-personal-debt.md), [013](013-banks-insurers.md), [F8](F8-vietnam-insurance-analysis.md).
- Thời lượng: `3 buổi học` + thực hành [`practice/models/insurance.py`](../practice/models/insurance.py).
- Câu hỏi cốt lõi: **Vì sao đóng `20–30 triệu đồng/năm` vào hợp đồng liên kết đầu tư (`UL`/`ILP`), sau 2 năm hủy hợp đồng chỉ nhận về vài triệu đồng, và làm sao thiết kế lớp bảo vệ tài chính đúng chuẩn cho gia đình mà không nhầm bảo hiểm với sổ tiết kiệm?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

---

## Hiểu bài này trong 1 phút

Hầu hết tranh chấp bảo hiểm nhân thọ tại Việt Nam bắt nguồn từ một sự nhầm lẫn cốt lõi: **người mua tưởng mình đang gửi tiết kiệm lãi cao được tặng kèm bảo hiểm miễn phí, trong khi thực chất đang ký hợp đồng mua dịch vụ bảo vệ rủi ro dài hạn có chi phí bán hàng và chi phí rủi ro khấu trừ rất nặng trong những năm đầu.**

Nhìn từ bảng cân đối kế toán ở **[Bài 013](013-banks-insurers.md)** và **[Bài F8](F8-vietnam-insurance-analysis.md)**:
1. Khi đóng phí năm đầu vào hợp đồng liên kết chung (`Universal Life — UL`), công ty bảo hiểm trả ngay hoa hồng đại lý (tối đa `30%` phí cơ bản năm đầu với `UL`/`ILP` từ `01/07/2024` và `40%` với `Term Life`/`Whole Life` theo `Điểm 3.2 Khoản 3 Điều 51 VBHN 44/2026/VBHN-TT-BTC`), cộng chi phí thẩm định và phát hành. Do đó hợp đồng trừ ngay **Phí ban đầu (`Initial Charge`)** tối đa **`50%`** phí cơ bản năm 1, **`30%`** năm 2, **`20%`** năm 3–5 theo trần `Điểm a Khoản 3 Điều 22 VBHN 44` (hợp đồng ký trước `Thông tư 67/2023/TT-BTC` trừ tới `60%–75%` năm đầu).
2. Phần tiền còn lại vào **Giá trị tài khoản (`Account Value`)** tiếp tục bị trừ hàng tháng **Phí bảo hiểm rủi ro (`COI`)** và **Phí quản lý hợp đồng (`Policy Admin Fee`)**.
3. Nếu hủy hợp đồng sớm trong 2–5 năm đầu, công ty trừ thêm **Phí chấm dứt hợp đồng trước hạn (`Surrender Charge`)**, khiến **Giá trị hoàn lại (`Surrender Value`)** năm 1–2 chỉ còn `8%–25%` tổng phí đã đóng.

Quy tắc vàng: **Bảo hiểm bảo vệ thu nhập của người trụ cột trước tai họa xác suất nhỏ nhưng hậu quả hủy diệt (tử vong sớm, thương tật toàn bộ vĩnh viễn, bệnh hiểm nghèo, viện phí lớn); còn tích lũy tài sản dài hạn là nhiệm vụ của danh mục đầu tư độc lập.**

> [!WARNING]
> **Cảnh báo an toàn trước khi quyết định dừng hoặc hủy hợp đồng bảo hiểm đang có hiệu lực:**
> Phân tích chi phí trong bài giúp bạn hiểu bản chất toán học trước khi ký hợp đồng mới hoặc tái cơ cấu hợp đồng cũ, **tuyệt đối không phải lời khuyên hủy ngay hợp đồng `UL`/`ILP` đang có**. Trước khi thay đổi hợp đồng nhân thọ, bắt buộc kiểm tra **3 điều kiện sống còn**:
> 1. **Tình trạng sức khỏe hiện tại (`Insurability`):** Nếu từ lúc ký hợp đồng cũ đến nay đã phát sinh bệnh nền mới (huyết áp, tiểu đường, tuyến giáp, u nang, tim mạch...), hủy hợp đồng cũ sẽ khiến hợp đồng mới bị **loại trừ bệnh có sẵn (`36 tháng`)**, tăng phí rủi ro hoặc bị từ chối bảo hiểm.
> 2. **Chi phí chìm (`Sunk Cost`) theo năm hợp đồng:** Nếu hợp đồng `UL`/`ILP` đã qua **Năm thứ 5–6 trở đi**, phần lớn **Phí ban đầu (`50%` năm 1, `30%` năm 2, `20%` năm 3–5)** đã trừ xong và **Phí hủy hợp đồng (`Surrender Charge`)** đã giảm về `0%–5%`. Hủy hợp đồng giai đoạn này để mua mới là tự mất phí ban đầu lần thứ hai.
> 3. **Quyền tái cấu trúc hợp đồng hiện hữu (`Policy Restructuring`):** Nếu áp lực dòng tiền nặng, thay vì hủy bỏ, hãy kiểm tra quyền **cắt giảm sản phẩm bổ trợ (`Riders`) trùng lặp**, **hạ Số tiền bảo hiểm về mức tối thiểu**, hoặc dùng **quyền tạm ngưng đóng phí / đóng phí tối thiểu duy trì hiệu lực** khi Giá trị tài khoản đủ trang trải `COI`.

---

## Ôn bài cũ và phạm vi bài học

- **Ôn bài cũ:** Bài [P1](P1-budget-emergency-fund-insurance.md) yêu cầu có **Quỹ dự phòng khẩn cấp (`Emergency Fund`)** `3–6 tháng` chi phí sinh hoạt và Bài [P2](P2-personal-debt.md)–[P3](P3-goals-risk-ips.md) xử lý nợ lãi cao trước khi mua bảo hiểm nhân thọ. Bài [013](013-banks-insurers.md) & [F8](F8-vietnam-insurance-analysis.md) giải thích dự phòng toán học và chi phí khai thác năm đầu trên BCTC DNBH.
- **Bài này làm gì:** Buổi 1 phân biệt 5 dòng sản phẩm (`Term Life`, `Whole Life`, `Endowment`, `UL`, `ILP`) và 6 lá chắn pháp lý (`Luật KDBH` & `VBHN 44/2026/VBHN-TT-BTC`); Buổi 2 giải phẫu 6 lớp phí (`Mẫu 22-NT`, `Mẫu 23-NT`, `Điều 22 & 29 VBHN 44`) và công thức $AV_t \to CSV_t$; Buổi 3 chạy mô hình 10 năm so sánh `UL` với `BTID`, tính `Sum Assured` tối ưu và hạn mức `200 triệu đồng` của **Quỹ bảo vệ người được bảo hiểm** (`Điều 95 Nghị định 46/2023/NĐ-CP`).
- **Bài này chưa làm gì:** Không tư vấn mua hay hủy sản phẩm cụ thể; không thay thế việc đọc Quy tắc và Điều khoản hợp đồng.

---

## Buổi 1 — Bản đồ 5 dòng sản phẩm nhân thọ và 6 lá chắn pháp lý bắt buộc phải biết

### 1.1. Phân biệt 5 dòng sản phẩm bảo hiểm nhân thọ

| Dòng sản phẩm | Bảo vệ | Tiết kiệm / Đầu tư | Ai chịu rủi ro đầu tư? | Phí/năm (`1 tỷ` bảo vệ) | Mục tiêu phù hợp |
|---|---|---|---|---|---|
| **1. Tử kỳ (`Term Life`)** | **100%** (10–20 năm) | **0%** (không hoàn phí) | Không có tài khoản đầu tư | **Rẻ nhất** (`8%–15%` phí HĐ tích lũy) | Người trụ cột cần bảo vệ lớn (`2–5 tỷ`) chi phí thấp để tự đầu tư phần chênh lệch (`BTID`) |
| **2. Trọn đời (`Whole Life`)** | Trọn đời (đến 99–100 tuổi) | Giá trị hoàn lại tăng chậm | Công ty bảo hiểm | Gấp `5–8 lần` `Term Life` | Để lại di sản thừa kế chắc chắn |
| **3. Hỗn hợp (`Endowment`)** | Kỳ hạn xác định (10–20 năm) | Cam kết trả tiền đáo hạn | Công ty bảo hiểm (`2%–4%/năm`) | Rất cao | Người ngại rủi ro, chấp nhận lợi suất thấp |
| **4. Liên kết chung (`UL`)** | Linh hoạt ($\ge 5$ lần phí cơ bản năm đầu, `Điều 20 VBHN 44`) | Hưởng lãi **Quỹ liên kết chung** (TPCP & tiền gửi) | Công ty **cam kết lãi tối thiểu** (`Điều 21 VBHN 44`) | Trung bình – Cao (`COI` tăng theo tuổi) | Bảo vệ dài hạn kèm tài khoản tích lũy có sàn lãi cam kết |
| **5. Liên kết đơn vị (`ILP`)** | Mệnh giá $\ge 5$ lần phí cơ bản năm đầu (`Điều 20 VBHN 44`) | Mua **Đơn vị quỹ (`Fund Units`)** CP/TP | **Khách hàng chịu 100% lãi/lỗ**, không cam kết lãi tối thiểu (`Khoản 2 Điều 21`) | Trung bình – Cao (phí ban đầu + phí quản lý quỹ) | Hiểu rõ cấu trúc phí kép và chấp nhận biến động chứng khoán |

### 1.2. Sáu lá chắn pháp lý bảo vệ người mua bảo hiểm tại Việt Nam

`SỰ_THẬT` Theo [Luật Kinh doanh bảo hiểm 31/VBHN-VPQH](https://vanban.chinhphu.vn/?pageid=27160&docid=215622) và [VBHN 44/2026/VBHN-TT-BTC ngày 29/09/2026](https://vanban.chinhphu.vn/?pageid=27160&docid=217205):

1. **Thời gian cân nhắc `21 ngày` (`Free-Look Period` — `Điều 35 Luật KDBH`):** Với hợp đồng trên `01 năm`, trong **`21 ngày`** từ ngày nhận hợp đồng, bên mua được từ chối tham gia và **nhận lại toàn bộ phí đã đóng** (trừ chi phí khám sức khỏe thực tế nếu có) nếu chưa xảy ra sự kiện bảo hiểm.
2. **Nghĩa vụ kê khai trung thực hai chiều (`Điều 21 & Điều 22 Luật KDBH`):** Bên mua **cố ý** kê khai gian dối bệnh nền thì DNBH được hủy hợp đồng và từ chối bồi thường (`Khoản 2 Điều 22`); ngược lại, nếu **DNBH** cố ý cung cấp thông tin sai sự thật, bên mua được hủy hợp đồng và đòi bồi thường thiệt hại (`Khoản 3 Điều 22`).
3. **Thời gian chờ (`Waiting Period`) và Bệnh có sẵn (`Khoản 2 & Khoản 3 Điều 12 VBHN 44`, tr. 9–10):** Tai nạn: **`0 ngày`** (`Điểm d Khoản 2 Điều 12`); Bệnh thường: $\le$ **`90 ngày`**; Thai sản: $\le$ **`270 ngày`** (sinh con) và **`90 ngày`** (biến chứng); Bệnh đặc biệt và Bệnh có sẵn: $\le$ **`365 ngày`**. *Bệnh có sẵn* chỉ tính bệnh đã được bác sĩ khám, chẩn đoán hoặc điều trị trước ngày hiệu lực/khôi phục **trong vòng `36 tháng` (`03 năm`) căn cứ theo hồ sơ y tế hoặc thông tin khách hàng tự kê khai** (`Điểm d Khoản 3 Điều 12`).
4. **Gia hạn đóng phí `60 ngày` và Khôi phục hiệu lực tối thiểu `24 tháng` (`Điều 37 Luật KDBH`; `Khoản 4, 6 Điều 12 & Điều 17 VBHN 44`, tr. 11, 13):** Hợp đồng giữ nguyên hiệu lực trong `60 ngày` gia hạn đóng phí; nếu mất hiệu lực tạm thời, được yêu cầu khôi phục trong tối thiểu `24 tháng`.
5. **Cấm ngân hàng bán kèm `UL` / `ILP` quanh ngày giải ngân vay và bắt buộc ghi âm (`Điều 53 VBHN 44`, tr. 69–71):** Cấm TCTD tư vấn, giới thiệu, chào bán, thu xếp giao kết hợp đồng `UL` / `ILP` **trong `60 ngày trước` và `60 ngày sau` ngày giải ngân toàn bộ khoản vay** (`Điểm c Khoản 3 Điều 53`, tr. 70); bắt buộc **ghi âm (`Audio Recording`)** toàn bộ nội dung tư vấn và lưu trữ tối thiểu **`05 năm`** (`Điểm đ Khoản 2 & Khoản 5 Điều 53`, tr. 69–71).

---

## Buổi 2 — Giải phẫu 6 lớp phí trong Bảng minh họa (`Mẫu 22-NT`, `Mẫu 23-NT`) và Công thức Giá trị hoàn lại

### 2.1. Sáu lớp phí và trần tối đa (`Khoản 3 Điều 22 VBHN 44/2026/VBHN-TT-BTC`, tr. 19–21)

1. **Phí ban đầu (`Initial Charge` — $c_t^{\text{init}}$, hàm `vn_ul_initial_fee_rate()` trong [`practice/models/insurance.py`](../practice/models/insurance.py)):** $\text{Tiền phân bổ}_t = P_t (1 - c_t^{\text{init}})$.
   - Theo **`Điểm a Khoản 3 Điều 22 VBHN 44` (tr. 20)**, trần Phí ban đầu tối đa trên phí cơ bản định kỳ: **Năm 1: `50%`; Năm 2: `30%`; Năm 3–5: `20%`; Năm 6–10: `2%`; Từ Năm 11: `0%`** (`Top-up` $\le$ **`1,5%`** trong 10 năm đầu; đóng 1 lần $\le$ `10%`).
   - Nguyên nhân kinh tế: **`Điểm 3.2 Khoản 3 Điều 51 VBHN 44` (tr. 65–66)** quy định trần hoa hồng đại lý năm 1 là **`30%`** với `UL`/`ILP` định kỳ (năm 2 tối đa `20%`, các năm sau `10%`), và **`40%`** với `Term Life`/`Whole Life`.
2. **Phí bảo hiểm rủi ro (`COI_t` — `Điểm b Khoản 3 Điều 22`):** Khấu trừ từ Giá trị tài khoản theo $\text{COI}_t = \frac{\text{coi\_rate}_t}{1.000} \times \text{NAR}_t$, với $\text{NAR}_t = \max(\text{SA} - AV_{\text{after contrib}, t},\; 0)$. Khi sang tuổi 60–75, tỷ lệ tử vong tăng theo hàm mũ; nếu tài khoản mỏng, `COI` ăn mòn hết tài khoản gây mất hiệu lực (`Policy Lapse`).
3. **Phí quản lý hợp đồng (`Policy Admin Fee — A_t` — `Điểm c Khoản 3 Điều 22`):** Khoảng `0,42–0,60 triệu đồng/năm`.
4. **Phí quản lý quỹ (`Fund Management Fee — m` — `Điểm d Khoản 3 Điều 22`, tr. 20):** $r_{\text{net}} = r_{\text{gross}} - m$. Trần tối đa: Quỹ `UL` $\le$ **`2,0%/năm`**; Quỹ `ILP` cổ phiếu/tăng trưởng $\le$ **`2,5%/năm`**, trái phiếu $\le$ **`1,5%/năm`**, tiền tệ/tiền gửi $\le$ **`1,0%/năm`**.
5. **Phí chấm dứt hợp đồng trước hạn (`Surrender Charge — s_t` — `Điểm đ Khoản 3 Điều 22`):** Khấu trừ `60%–80%` $AV_t$ nếu hủy những năm đầu.
6. **Phí chuyển đổi quỹ (`Switching Fee` — `Điểm e Khoản 3 Điều 22`, miễn phí lần đầu trong năm).**

### 2.2. Công thức Giá trị tài khoản (`AV_t`) và Giá trị hoàn lại (`CSV_t`)

Theo hàm `ul_vs_term_invest()` trong [`practice/models/insurance.py`](../practice/models/insurance.py):
$$AV_{\text{after contrib}, t} = AV_{t-1} + P_t^{\text{base}}(1 - c_t^{\text{init}}) + P_t^{\text{topup}}(1 - c_t^{\text{topup}}), \qquad \text{NAR}_t = \max\Big(0,\; \text{SA} - AV_{\text{after contrib}, t}\Big)$$
$$\text{COI}_t = \frac{\text{coi\_rate}_t}{1.000} \times \text{NAR}_t, \qquad AV_t = \max\Big(0,\; AV_{\text{after contrib}, t} - \text{COI}_t - A_t\Big) \times (1 + r_{\text{gross}} - m), \qquad CSV_t = AV_t \times (1 - s_t)$$

`SỰ_THẬT` Theo `Điều 29` và `Phụ lục VIII VBHN 44/2026/VBHN-TT-BTC` (tr. 29, 226–243), bảng minh họa `UL` (`Mẫu 22-NT`) trình bày lãi suất cam kết tối thiểu, mức thấp và mức cao; bảng minh họa `ILP` (`Mẫu 23-NT`) bắt buộc có cột **Tỷ suất đầu tư âm (lỗ)**.
- **Cơ chế "Cú đấm kép" ở `ILP` (`Double Whammy Lapse Risk`):** Khi chứng khoán giảm `-25%` đến `-30%` lúc người được bảo hiểm đã lớn tuổi (`55–70 tuổi`), hai lực ngược chiều xảy ra cùng lúc: (1) $AV_t$ sụt giảm theo giá đơn vị quỹ; và (2) vì $\text{NAR}_t = \text{SA} - AV_{\text{after contrib}, t}$, khi $AV$ thu hẹp thì `NAR` tự động **phình to ra**, buộc DNBH phải **bán giải chấp nhiều đơn vị quỹ hơn ở đúng vùng giá đáy** để thu đủ `COI` đang tăng theo tuổi, đẩy hợp đồng tới điểm gãy mất hiệu lực (`Lapse`) nhanh gấp bội.

---

## Buổi 3 — So sánh định lượng 10 năm (`UL` vs. `BTID`) và Giới hạn Quỹ bảo vệ người được bảo hiểm

### 3.1. Đối chiếu định lượng 10 năm: Hợp đồng `UL` vs. `BTID` (`Buy Term and Invest the Difference`)

Xét người trụ cột 32 tuổi cần mệnh giá bảo vệ **`1.000 triệu đồng` (`1 tỷ đồng`)** trong `10 năm` với ngân sách **`20,00 triệu đồng/năm`** (hàm `ul_vs_term_invest()` trong [`practice/models/insurance.py`](../practice/models/insurance.py)):
- **Phương án A (`UL` đóng phí cơ bản `20,00 tr/năm`):** Trần Phí ban đầu `Điểm a Khoản 3 Điều 22 VBHN 44`: $c^{\text{init}} = [50\%, 30\%, 20\%, 20\%, 20\%, 2\%, 2\%, 2\%, 2\%, 2\%]$; $\text{coi\_rates\_per\_1000} = [1,8; 1,9; 2,0; 2,1; 2,2; 2,4; 2,6; 2,8; 3,0; 3,3]\text{ ‰/năm}$; Phí QL HĐ $A_t = 0,42\text{ tr/năm}$; Lãi gộp `6,5%/năm` trừ trần phí quản lý quỹ `UL` `2,0%/năm` = ròng `4,5%/năm`; Phí hủy $s_t = [80\%, 60\%, 40\%, 25\%, 15\%, 5\%, 0\%, 0\%, 0\%, 0\%]$.
- **Phương án B (`BTID`):** Mua `Term Life` 10 năm mệnh giá `1.000 triệu đồng` phí `1,80 triệu đồng/năm`; phần chênh lệch **`18,20 triệu đồng/năm`** tự đầu tư vào quỹ chỉ số/trái phiếu có cùng lãi gộp `6,5%/năm` trừ phí ETF `0,5%/năm` (ròng `6,0%/năm`).

| Năm ($t$) | Tổng đóng (`20 tr/năm`) | **`UL`**: Phí ban đầu (`Điều 22`) | **`UL`**: `COI` + QL HĐ (`0,42 tr`) | **`UL`**: Giá trị tài khoản ($AV_t$) | **`UL`**: Giá trị hoàn lại ($CSV_t$) | **`BTID`**: Tự đầu tư (`18,2 tr/năm` @ `6,0%`) | Chênh lệch ($\text{BTID} - CSV_t$) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| **1** | `20,00` | `10,00` (`50%`) | `2,20` (`1,78 + 0,42`) | `8,15` | **`1,63`** | **`19,29`** | **`+17,66`** |
| **2** | `40,00` | `6,00` (`30%`) | `2,28` (`1,86 + 0,42`) | `20,77` | **`8,31`** | **`39,74`** | **`+31,44`** |
| **3** | `60,00` | `4,00` (`20%`) | `2,35` (`1,93 + 0,42`) | `35,97` | **`21,58`** | **`61,42`** | **`+39,84`** |
| **4** | `80,00` | `4,00` (`20%`) | `2,41` (`1,99 + 0,42`) | `51,79` | **`38,84`** | **`84,40`** | **`+45,56`** |
| **5** | `100,00` | `4,00` (`20%`) | `2,47` (`2,05 + 0,42`) | `68,26` | **`58,02`** | **`108,75`** | **`+50,73`** |
| **6** | `120,00` | `0,40` (`2%`) | `2,61` (`2,19 + 0,42`) | `89,08` | **`84,63`** | **`134,57`** | **`+49,94`** |
| **7** | `140,00` | `0,40` (`2%`) | `2,74` (`2,32 + 0,42`) | `110,71` | **`110,71`** | **`161,93`** | **`+51,22`** |
| **8** | `160,00` | `0,40` (`2%`) | `2,86` (`2,44 + 0,42`) | `133,19` | **`133,19`** | **`190,94`** | **`+57,75`** |
| **9** | `180,00` | `0,40` (`2%`) | `2,96` (`2,54 + 0,42`) | `156,57` | **`156,57`** | **`221,69`** | **`+65,12`** |
| **10** | `200,00` | `0,40` (`2%`) | `3,14` (`2,72 + 0,42`) | `180,82` | **`180,82`** | **`254,28`** | **`+73,46`** |

`SUY_LUẬN` Cuối Năm 1 và Năm 2, nếu hủy hợp đồng `UL`, khách hàng chỉ nhận **`1,63 triệu`** và **`8,31 triệu đồng`** (mất `79%–92%` tiền đã đóng). Sau 10 năm đóng `200,00 triệu đồng` (tổng Phí ban đầu `30,00 triệu`, tổng `COI` `21,82 triệu`), Giá trị hoàn lại của `UL` đạt **`180,82 triệu đồng`**, thấp hơn `BTID` (**`254,28 triệu đồng`**) tới **`-73,46 triệu đồng`**.
- **Bốn rủi ro thực tế và điều kiện biên khi áp dụng `BTID`:**
  1. **Rủi ro tái tục khi hết hạn `Term Life` (`Renewability & Insurability Risk`):** `Term Life` chỉ bảo vệ kỳ hạn cố định (`10–20 năm`). Nếu ở Năm 8–9 mắc bệnh hiểm nghèo/mãn tính nhưng chưa tử vong, khi `Term Life` 10 năm đáo hạn sẽ **không thể mua mới hoặc bị tăng phí rất đắt**, trong khi `UL`/`Whole Life` duy trì đến `85–99 tuổi` không thẩm định lại sức khỏe (miễn tài khoản đủ trừ `COI`). Khắc phục: mua `Term Life` đủ dài bao trọn thời gian nuôi con (`15–20 năm`) hoặc gói **đảm bảo gia hạn/chuyển đổi không thẩm định lại (`Guaranteed Renewable / Convertible Term`)**.
  2. **Rủi ro kỷ luật hành vi (`Behavioral Risk` — *"Buy Term and Spend the Difference"*):** `BTID` chỉ thắng nếu khoản chênh lệch `18,20 triệu/năm` được trích tự động (`Auto-invest`) ngay ngày nhận lương. Nếu tiêu xài hết phần chênh lệch, `UL` lại đóng vai trò "tiết kiệm cưỡng bức có phí cao".
  3. **Khác biệt Quyền lợi tử vong (`Level` vs. `Increasing Death Benefit`):** Với `BTID`, nếu tử vong Năm 10, gia đình nhận **`1.000 triệu`** bảo hiểm tử kỳ **cộng `254,28 triệu`** tự đầu tư (tổng **`1.254,28 triệu đồng`**), còn `UL` chọn *Quyền lợi cơ bản* chỉ trả $\max(1.000\text{ tr},\; AV_{10}) = 1.000\text{ triệu đồng}$ (chọn *Quyền lợi nâng cao* trả $1.000\text{ tr} + AV_t$ thì `COI` cao hơn nữa).
  4. **Rào cản phân phối:** Đại lý ít giới thiệu `Term Life` độc lập vì hoa hồng thấp (`1,8 triệu × 40% = 0,72 triệu đồng`), nên người mua phải chủ động tìm trên kênh số (`Digital Insurance`) hoặc quầy giao dịch doanh nghiệp.

### 3.2. Giới hạn `200 triệu đồng` của Quỹ bảo vệ người được bảo hiểm (`Điều 95 Nghị định 46/2023/NĐ-CP`)

`SỰ_THẬT` Nếu DNBH mất khả năng thanh toán hoặc phá sản mà chuyển giao danh mục hợp đồng (`Điều 92, 110 Luật KDBH`) và tài sản không đủ chi trả, **Quỹ bảo vệ người được bảo hiểm** chi trả theo **`Điều 95 Nghị định 46/2023/NĐ-CP`**: tối đa **`90%` mức trách nhiệm của DNBH nhân thọ, nhưng không quá `200.000.000 đồng` (`200 triệu đồng`)/người/hợp đồng** ([Nghị định 46/2023/NĐ-CP](https://vanban.chinhphu.vn/?pageid=27160&docid=208265)). (Từ `01/01/2023` theo `Khoản 2 Điều 156 Luật KDBH`, việc trích nộp mới vào Quỹ đã dừng và Bộ Tài chính quản lý số dư hiện có đến khi dùng hết). Với hợp đồng lớn (`1–5 tỷ đồng`), phải chọn DNBH có bảng cân đối và `CAR` vững mạnh.

---

## Ví dụ từ nguồn thật

`SỰ_THẬT` Nguồn: [Luật KDBH 31/VBHN-VPQH](https://vanban.chinhphu.vn/?pageid=27160&docid=215622), [Nghị định 46/2023/NĐ-CP](https://vanban.chinhphu.vn/?pageid=27160&docid=208265) và [VBHN 44/2026/VBHN-TT-BTC ngày 29/09/2026](https://vanban.chinhphu.vn/?pageid=27160&docid=217205):

| Quyền lợi / Nghĩa vụ / Trần giới hạn | Con số pháp định bắt buộc | Căn cứ điều khoản chính xác | Ý nghĩa thực chiến |
|---|---|---|---|
| 1. Thời gian cân nhắc (`Free-Look`) | **`21 ngày`** từ ngày nhận HĐ ($> 1$ năm) | `Điều 35 Luật KDBH (31/VBHN-VPQH)` | Nhận lại `100%` phí đã đóng (trừ phí khám sức khỏe thực tế) |
| 2. Gia hạn đóng phí (`Grace Period`) | **`60 ngày`** từ ngày đến hạn đóng phí | `Điều 37 Luật KDBH` & `Khoản 4 Điều 12, Điều 17 VBHN 44` | Giữ nguyên hiệu lực bảo vệ trong 60 ngày trễ hạn |
| 3. Thời hạn khôi phục hiệu lực HĐ | Tối thiểu **`24 tháng`** từ ngày mất hiệu lực | `Khoản 6 Điều 12 & Điều 17 VBHN 44` (tr. 11, 13) | Khôi phục HĐ cũ thay vì mua mới chịu lại phí ban đầu năm 1 |
| 4. Thời gian chờ bảo hiểm sức khỏe | Tai nạn: **`0 ngày`**; Bệnh thường: $\le$ **`90 ngày`**; Bệnh đặc biệt/có sẵn: $\le$ **`365 ngày`**; Thai sản: $\le$ **`270 ngày`** | `Khoản 2 Điều 12 VBHN 44/2026/VBHN-TT-BTC` (tr. 9) | Mọi điều khoản quy định thời gian chờ dài hơn trần này là trái thông tư |
| 5. Định nghĩa Bệnh có sẵn | Khám, chẩn đoán hoặc điều trị trong **`36 tháng`** trước ngày hiệu lực/khôi phục | `Điểm d Khoản 3 Điều 12 VBHN 44` (tr. 10) | Căn cứ hồ sơ y tế hoặc thông tin khách hàng tự kê khai |
| 6. Mệnh giá tối thiểu `UL` / `ILP` | Tối thiểu **`5 lần`** phí cơ bản năm đầu (định kỳ) hoặc **`125%`** phí đóng 1 lần | `Điều 20 VBHN 44/2026/VBHN-TT-BTC` (tr. 15–16) | Đảm bảo hợp đồng liên kết đầu tư có tính bảo vệ thực sự |
| 7. Trần Phí ban đầu `UL` / `ILP` định kỳ | Năm 1: **`50%`**; Năm 2: **`30%`**; Năm 3–5: **`20%`**; Năm 6–10: **`2%`**; Từ Năm 11: **`0%`** (`Top-up` $\le$ **`1,5%`**) | `Điểm a Khoản 3 Điều 22 VBHN 44` (tr. 20) | Khống chế mức khấu trừ phí ban đầu tối đa trên phí cơ bản định kỳ |
| 8. Trần hoa hồng đại lý năm 1 | `UL`/`ILP` định kỳ: **`30%`** (năm 2: `20%`); `Term Life`/`Whole Life`: **`40%`**; Hỗn hợp: **`15%–30%`** | `Điểm 3.2 Khoản 3 Điều 51 VBHN 44` (tr. 65–66) | Giảm động cơ đại lý ép khách mua `UL`/`ILP` vì hoa hồng năm đầu cao |
| 9. Cấm ngân hàng bán `UL`/`ILP` quanh giải ngân & ghi âm | Cấm bán `UL`/`ILP` **`60 ngày trước`** và **`60 ngày sau`** giải ngân; ghi âm lưu trữ $\ge$ **`05 năm`** | `Điểm đ Khoản 2, Điểm c Khoản 3 & Khoản 5 Điều 53 VBHN 44` (tr. 69–71) | Ngân hàng ép mua `UL`/`ILP` khi giải ngân vay hoặc không ghi âm là phạm luật |
| 10. Hạn mức Quỹ bảo vệ người được bảo hiểm | Tối đa **`90%`** trách nhiệm nhân thọ nhưng không quá **`200 triệu đồng`/người/HĐ** | `Điều 95 Nghị định 46/2023/NĐ-CP` | Quỹ chỉ bảo vệ tối đa `200 triệu đồng`; HĐ lớn phụ thuộc sức khỏe DNBH |

---

## Bài tập

Tự giải trước khi mở Đáp án; kiểm chứng bằng `python3 learning/practice/models/insurance.py`.

1. **(Quyền `21 ngày` cân nhắc theo `Điều 35 Luật KDBH`):** Ngày `05/03/2026`, chị Lan ký hồ sơ yêu cầu `UL` đóng `35.000.000 đồng` năm đầu; phí khám sức khỏe thực tế do công ty chỉ định là `1.200.000 đồng`. Ngày `12/03/2026`, chị nhận bộ hợp đồng. Ngày `28/03/2026`, chị nộp đơn từ chối tham gia (chưa phát sinh sự kiện bảo hiểm). Hỏi: (a) Yêu cầu còn trong hạn `21 ngày` không? (b) Số tiền công ty phải hoàn trả?
2. **(Tính $AV_1, CSV_1, AV_2, CSV_2$ của `UL` theo `ul_vs_term_invest()`):** Với thông số Phương án A (`UL`) ở Buổi 3 (`P = 20,00 tr/năm`, `SA = 1.000 tr`; Năm 1: `Phí ban đầu = 50%`, `coi_rate = 1,8‰`, `Phí QL HĐ = 0,42 tr`, `Phí hủy = 80%`; Năm 2: `Phí ban đầu = 30%`, `coi_rate = 1,9‰`, `Phí QL HĐ = 0,42 tr`, `Phí hủy = 60%`; lãi gộp `6,5%`, phí quản lý quỹ `2,0%`), tính từng bước $AV_1, CSV_1$ và $AV_2, CSV_2$.
3. **(Tìm năm hòa vốn tiền mặt danh nghĩa của `UL`):** Cuối Năm 10 khách hàng đã đóng `200,00 triệu đồng` và $AV_{10} = CSV_{10} = 180,82\text{ triệu đồng}$. Từ Năm 11 trở đi, đóng `20,00 triệu/năm` với `Phí ban đầu = 0%` (`Điểm a Khoản 3 Điều 22 VBHN 44`), `COI + Phí QL HĐ = 3,30 triệu/năm`, `Phí hủy = 0%`, lãi ròng `4,5%/năm`. Tính $CSV_{11}, CSV_{12}, CSV_{13}$ để xác định cuối năm thứ mấy hòa vốn tiền mặt danh nghĩa.
4. **(So sánh `BTID` ở lãi suất ròng `5,5%` và `8,0%`):** Với phần chênh lệch `18,20 triệu đồng/năm` đầu tư đầu mỗi năm trong 10 năm ($\text{FV}_{10} = \sum_{t=1}^{10} 18,20(1+r)^t$), tính tổng tài sản cuối Năm 10 khi: (a) tiết kiệm `r = 5,5%/năm`; (b) chứng chỉ quỹ `r = 8,0%/năm`, và so với $CSV_{10} = 180,82\text{ triệu}$ của `UL`.
5. **(Thời gian chờ và Bệnh có sẵn theo `Khoản 2 & 3 Điều 12 VBHN 44`):** Thẻ sức khỏe của anh Minh hiệu lực từ `01/04/2026` (áp dụng thời gian chờ tối đa). Xác định trách nhiệm chi trả 3 ca: (A) Ngày `15/04/2026` (`14 ngày`), gãy xương tay do tai nạn giao thông; (B) Ngày `20/05/2026` (`49 ngày`), viêm phế quản thông thường; (C) Ngày `10/11/2026` (`223 ngày`), mổ biến chứng sỏi thận đã chẩn đoán tháng `01/2025` (`14 tháng` trước ngày hiệu lực) nhưng không kê khai.
6. **(Vi phạm `Bancassurance` theo `Điều 53 VBHN 44`):** Ngày `10/06/2026`, anh Tuấn giải ngân vay mua nhà `2 tỷ đồng` tại Ngân hàng X. Nhân viên ngân hàng yêu cầu ký ngay hợp đồng `ILP` đóng `50 triệu đồng/năm` trong ngày giải ngân để duyệt lãi vay ưu đãi, nói miệng *"cam kết không bao giờ lỗ vốn"* và không ghi âm buổi tư vấn. Chỉ ra **3 vi phạm pháp luật**.
7. **(Bẫy tăng vọt `COI` ở tuổi 65 và `Policy Lapse`):** Hợp đồng `UL` có `SA = 2.000 triệu đồng` ($\text{NAR} = 2.000 - AV$). Năm 65 tuổi, $AV$ đầu năm còn `120 triệu đồng`, ngưng đóng phí ($P = 0$), $q_{65} = 2,45\%/\text{năm}$ (`24,5‰`) trên `NAR`, phí QL HĐ `0,60 triệu/năm`, lãi ròng `4,5%/năm`. Tính `NAR`, `COI` và $AV$ cuối năm 65 tuổi, rồi giải thích vì sao hợp đồng mất hiệu lực sau khoảng 2 năm nữa.
8. **(Tính `Sum Assured` tối ưu cho người trụ cột):** Anh Hùng (35 tuổi, 2 con nhỏ cần nuôi `15 năm`) đóng góp cho gia đình `240 triệu đồng/năm`, nợ vay mua nhà `1.200 triệu đồng`, có sẵn `300 triệu đồng` tiết kiệm. Với $r_{\text{real}} = 3,0\%/\text{năm}$, tính: (a) Hiện giá dòng thu nhập cần thay thế 15 năm; (b) Tổng `Sum Assured` tối ưu; (c) Vì sao với ngân sách `19,2 triệu đồng/năm` phải chọn `Term Life` thay vì `Endowment`?
9. **(Thế quyền đòi người thứ ba theo `Điều 54` vs. `Điều 68 Luật KDBH`):** Anh Nam bị xe tải đâm hỏng ô tô (sửa hết `150 triệu đồng`) và bị thương nằm viện. Chủ xe tải đã đền đủ `150 triệu đồng` sửa xe và `50 triệu đồng` sức khỏe. Hỏi: (a) Anh Nam có được nhận thêm `150 triệu đồng` từ bảo hiểm vật chất xe ô tô không? (b) Khoản `50 triệu đồng` chủ xe tải đền có làm mất quyền nhận tiền bảo hiểm nhân thọ/tai nạn con người không?
10. **(Hạn mức Quỹ bảo vệ người được bảo hiểm theo `Điều 95 Nghị định 46/2023/NĐ-CP`):** Khi DNBH nhân thọ phá sản và chi trả từ Quỹ bảo vệ người được bảo hiểm, tính số tiền tối đa Quỹ trả cho: (a) Hợp đồng A có mức trách nhiệm `180 triệu đồng`; (b) Hợp đồng B có mức trách nhiệm `1.500 triệu đồng`.

---

## Đáp án

<details>
<summary>Mở sau khi đã tự giải cả 10 bài tập</summary>

1. **`PHÉP_TÍNH` & `SỰ_THẬT`:** (a) Mốc `21 ngày` tính từ ngày nhận HĐ (`12/03/2026`); đến `28/03/2026` là `16 ngày` ($\le 21$) nên hợp lệ. (b) Hoàn lại: $35.000.000 - 1.200.000 = 33.800.000\text{ đồng}$.
2. **`PHÉP_TÍNH`:** $r_{\text{net}} = 6,5\% - 2,0\% = 4,5\%$.
   - Năm 1: Phân bổ $= 10,00\text{ tr}$; $\text{NAR}_1 = 990,00\text{ tr}$; $\text{COI}_1 = 1,782\text{ tr}$; $AV_{\text{before growth}, 1} = 10,00 - 1,782 - 0,42 = 7,798\text{ tr}$; $AV_1 = 8,1489 \approx 8,15\text{ tr}$; $CSV_1 = 8,1489 \times 20\% = 1,63\text{ triệu đồng}$.
   - Năm 2: Phân bổ $= 14,00\text{ tr}$; $AV_{\text{after contrib}, 2} = 22,1489\text{ tr}$; $\text{NAR}_2 = 977,8511\text{ tr}$; $\text{COI}_2 = 1,8579\text{ tr}$; $AV_{\text{before growth}, 2} = 19,8710\text{ tr}$; $AV_2 = 20,7652 \approx 20,77\text{ tr}$; $CSV_2 = 20,7652 \times 40\% = 8,31\text{ triệu đồng}$.
3. **`PHÉP_TÍNH`:** Năm 11 (`220 tr`): $CSV_{11} = (180,82 + 20 - 3,30) \times 1,045 = 206,41\text{ tr}$. Năm 12 (`240 tr`): $CSV_{12} = 233,15\text{ tr}$. Năm 13 (`260 tr`): $CSV_{13} = 261,09\text{ triệu đồng} > 260,00\text{ triệu đồng}$ (**cuối Năm 13** hòa vốn tiền mặt danh nghĩa).
4. **`PHÉP_TÍNH`:** (a) `r = 5,5%`: $\text{FV}_{10} = 247,22\text{ triệu đồng}$ (hơn `UL` `+66,40 triệu`). (b) `r = 8,0%`: $\text{FV}_{10} = 284,75\text{ triệu đồng}$ (hơn `UL` `+103,93 triệu`).
5. **`SỰ_THẬT`:** (A) Tai nạn chờ `0 ngày` (`Điểm d Khoản 2 Điều 12 VBHN 44`) $\implies$ **Được chi trả**. (B) Bệnh thường ngày thứ `49 < 90 ngày` $\implies$ **Từ chối hợp pháp** (trừ khi HĐ quy định ngắn hơn). (C) Sỏi thận chẩn đoán `14 tháng` trước (`< 36 tháng`) là **Bệnh có sẵn** (`Điểm d Khoản 3 Điều 12`), mới qua `223 < 365 ngày` và không kê khai $\implies$ **Từ chối hợp pháp**.
6. **`SỰ_THẬT`:** (1) Bán `ILP` trong ngày giải ngân vi phạm lệnh cấm `60 ngày trước và sau` giải ngân (`Điểm c Khoản 3 Điều 53 VBHN 44`); (2) Ép mua kèm khoản vay và nói `ILP` "không lỗ vốn" vi phạm `Khoản 5 Điều 9 Luật KDBH` & `Khoản 2 Điều 21 VBHN 44`; (3) Không ghi âm vi phạm `Điểm đ Khoản 2 & Khoản 5 Điều 53 VBHN 44`.
7. **`PHÉP_TÍNH`:** $\text{NAR}_{65} = 1.880\text{ tr}$; $\text{COI}_{65} = 46,06\text{ tr}$; $\text{Base}_{65} = 73,34\text{ tr}$; $AV_{65} = 76,64\text{ triệu đồng}$. Khi $AV$ giảm thì $\text{NAR}$ năm 66 tăng lên `1.923,36 tr` và $q_{66} > q_{65}$, làm `COI` vượt `50 tr/năm` và xóa sạch tài khoản năm 67 tuổi (`Lapse Spiral`).
8. **`PHÉP_TÍNH`:** (a) $PV_{\text{income}} = 240 \times \frac{1 - 1,03^{-15}}{0,03} = 2.865,11\text{ triệu đồng}$. (b) $\text{Optimal SA} = 2.865,11 + 1.200 - 300 = 3.765,11\text{ triệu đồng}$ (`~3,8 tỷ đồng`). (c) Với `19,2 triệu/năm`, `Endowment` chỉ bảo vệ `200–300 triệu`, còn `Term Life` 15 năm bảo vệ đủ `3,5–4,0 tỷ đồng`.
9. **`SỰ_THẬT`:** (a) Bảo hiểm tài sản áp dụng thế quyền (`Điều 54 Luật KDBH`) nên không nhận hai lần. (b) Nhân thọ và sức khỏe **không áp dụng thế quyền** (`Điều 68 Luật KDBH`), nên vẫn nhận đủ tiền bảo hiểm theo hợp đồng.
10. **`PHÉP_TÍNH` & `SỰ_THẬT`:** Theo `Điều 95 Nghị định 46/2023/NĐ-CP`, $\text{Payout} = \min(90\% \times \text{Mức trách nhiệm},\; 200\text{ triệu đồng})$. (a) HĐ A (`180 tr`): $162\text{ triệu đồng}$. (b) HĐ B (`1.500 tr`): Nhận tối đa **`200 triệu đồng`**.

</details>

---

## Bài làm với dữ liệu thiếu hoặc lệch

**Đề bài:** Tờ rơi viết tay chào gói `UL` đóng `30 triệu đồng/năm` trong `10 năm` (tổng `300 triệu`) chỉ ghi *"Lãi dự kiến `9,5%/năm` — sau 10 năm nhận `503 triệu`"*, bỏ trống Phí ban đầu tối đa (`50%`, `30%`, `20%`, `20%`, `20%`, `2%–2%` theo `Điểm a Khoản 3 Điều 22 VBHN 44`), bỏ trống `COI + Phí QL HĐ` (`4,0 triệu/năm`) và cắt cột *Giá trị hoàn lại* (phí hủy Năm 1 `90%`, Năm 2 `75%`, Năm 3 `50%`). Tính lại theo chuẩn Bộ Tài chính ($r_{\text{net}} = 5,0\%/\text{năm}$).

<details>
<summary>Xem cách sửa dữ liệu lệch và tính lại số thực nhận</summary>

1. **`SỰ_THẬT` (Bác bỏ lãi minh họa `9,5%/năm`):** `Điều 29` và `Mẫu 22-NT VBHN 44/2026/VBHN-TT-BTC` cấm minh họa `UL` vượt trần Bộ Tài chính và cấm tính lãi trên `100%` phí đóng khi chưa trừ Phí ban đầu (`Điểm a Khoản 3 Điều 22`) và `COI`.
2. **`PHÉP_TÍNH` (Tính lại $AV$ và $CSV$ Năm 1–3 và Năm 10 với $r_{\text{net}} = 5,0\%$):**
   - Năm 1 (`Phí ban đầu 50%`): Phân bổ $= 15,00\text{ tr}$; trừ `4,00 tr` còn `11,00 tr`; cộng lãi `5%` $\implies AV_1 = 11,55\text{ tr}$; trừ phí hủy `90%` $\implies CSV_1 = 1,15\text{ triệu đồng}$.
   - Năm 2 (`Phí ban đầu 30%`): Phân bổ $= 21,00\text{ tr}$; $\text{Base}_2 = 28,55\text{ tr}$; $AV_2 = 29,98\text{ tr}$; trừ phí hủy `75%` $\implies$ **$CSV_2 = 7,49\text{ triệu đồng}$** (trên `60 triệu` đã đóng).
   - Năm 3 (`Phí ban đầu 20%`): Phân bổ $= 24,00\text{ tr}$; $\text{Base}_3 = 49,98\text{ tr}$; $AV_3 = 52,48\text{ tr}$; trừ phí hủy `50%` $\implies$ **$CSV_3 = 26,24\text{ triệu đồng}$** (trên `90 triệu` đã đóng).
   - Cuối Năm 10: $CSV_{10} = 276,15\text{ triệu đồng}$ (thấp hơn `300 triệu` gốc đã đóng và thấp hơn tờ rơi `-226,85 triệu đồng`).

</details>

---

## Sai ở đâu

**Nhận định sai lầm:** *"Vợ chồng tôi thu nhập `25 triệu/tháng`, đang nợ mua nhà `800 triệu` và chưa có con. Hai vợ chồng trẻ khỏe nên không mua bảo hiểm cho mình mà dồn `48 triệu/năm` mua hợp đồng `ILP` đứng tên Người được bảo hiểm là cháu ruột 2 tuổi để tích lũy du học sau 16 năm, vì tiền đóng vào bảo hiểm nhân thọ được Nhà nước bảo lãnh 100% không bao giờ mất!"*

<details>
<summary>Mở sau khi tự tìm lỗi</summary>

1. **Mua ngược đối tượng:** Phải ưu tiên bảo vệ **người trụ cột tạo thu nhập (`25 triệu/tháng`) và gánh nợ (`800 triệu`)**, không phải mua cho trẻ em chưa tạo thu nhập.
2. **Vi phạm Quyền lợi có thể được bảo hiểm (`Điều 34 & 25 Luật KDBH`):** Nếu không phải người giám hộ/nuôi dưỡng hợp pháp của cháu ruột thì không có quyền lợi có thể được bảo hiểm, dẫn tới nguy cơ **hợp đồng vô hiệu** (`Điểm b Khoản 1 Điều 25 Luật KDBH`).
3. **Dùng `ILP` chịu phí kép để tích lũy:** `ILP` trừ phí ban đầu nặng 5 năm đầu (`50%/30%/20%/20%/20%`), phí quản lý quỹ ($\le 2,5\%/\text{năm}$) và khách hàng chịu 100% rủi ro lỗ chứng khoán (`Khoản 2 Điều 21 VBHN 44`).
4. **Ngộ nhận "Nhà nước bảo lãnh 100%":** Quỹ bảo vệ người được bảo hiểm chỉ trả tối đa `90%` nhưng không quá **`200 triệu đồng/người/HĐ`** (`Điều 95 Nghị định 46/2023/NĐ-CP`) và không bảo lãnh lỗ đầu tư `ILP`.

</details>

---

## Kiểm tra chuyển bài

1. Khoản *Phí ban đầu `50%` năm 1* và *Phí quản lý quỹ `2,0%/năm`* trừ khỏi tài khoản khách hàng ở Bài `P4` chảy vào những dòng nào trên BCKQKD của DNBH ở Bài `F8` và `CSM` ở Bài `013`?
2. Nêu công thức 3 bước để gia đình trẻ tự tính: (i) Quỹ dự phòng khẩn cấp; (ii) `Sum Assured` cần mua qua `Term Life`; và (iii) Ngân sách đầu tư định kỳ.
3. Trước khi ký hợp đồng nhân thọ 20 năm với một DNBH tại Việt Nam, cần kiểm tra 3 chỉ số nào trên BCTC kiểm toán của doanh nghiệp đó?

<details>
<summary>Mở sau khi tự trả lời</summary>

1. Phí ban đầu bù đắp hoa hồng đại lý (`Điểm 3.2 Khoản 3 Điều 51 VBHN 44`) và chi phí khai thác năm đầu trên BCKQKD (Bài `F8`), còn thặng dư phí rủi ro và phí quản lý quỹ tạo nên biên lợi nhuận dịch vụ (`CSM`) phân bổ dần theo `IFRS 17` (Bài `013`).
2. (i) Giữ `3–6 tháng` sinh hoạt phí ở tiền gửi thanh khoản cao; (ii) Tính $\text{SA} = PV(\text{Thu nhập thay thế}) + \text{Dư nợ vay} - \text{Tài sản thanh khoản}$ và mua qua `Term Life` + thẻ sức khỏe nội trú; (iii) Phần tiết kiệm còn lại đầu tư định kỳ vào quỹ chỉ số/trái phiếu chi phí thấp (`BTID`).
3. Kiểm tra: (1) Tỷ trọng TPCP và Tiền gửi trong danh mục đầu tư (`Điều 43 NĐ 46`); (2) Dự phòng toán học và Dự phòng lãi cam kết tối thiểu trên Bảng CĐKT; (3) VCSH cùng Tỷ lệ an toàn vốn (`CAR / RBC`).

</details>

---

## Ranh giới an toàn và điều tôi vẫn chưa hiểu

- **Ranh giới an toàn:** Bài giảng cung cấp công cụ toán học và căn cứ pháp lý tại Việt Nam để tự đọc hiểu hợp đồng bảo hiểm; không phải lời khuyên mua hay hủy hợp đồng cụ thể. Trước khi hủy hợp đồng cũ đang có hiệu lực, phải kiểm tra: (1) tình trạng sức khỏe hiện tại (nếu có bệnh nền mới thì mua mới bị loại trừ `36 tháng`); và (2) nếu hợp đồng cũ đã qua năm thứ 5–6 (đã trừ xong phí ban đầu `50%/30%/20%` và phí hủy về `0%–5%`), hủy hợp đồng cũ để mua mới sẽ mất phí ban đầu lần thứ hai.
- **Điều tôi vẫn chưa hiểu (`CHƯA_BIẾT`):** Biểu tỷ lệ phí rủi ro (`COI`) chi tiết từ tuổi `60` đến `99` của từng sản phẩm `UL`/`ILP` chỉ có trong Phụ lục hợp đồng cá nhân; cần yêu cầu chạy bảng minh họa đến năm `80 tuổi` ở lãi cam kết tối thiểu để kiểm tra điểm gãy `Lapse`.

---

## Nguồn Internet đã mở

| Nguồn pháp quy / Tài liệu chuẩn mực | Kỳ báo cáo / Phiên bản / Phạm vi | Ngày truy cập | Nội dung đối chiếu trong bài |
|---|---|---|---|
| [Văn bản hợp nhất Luật Kinh doanh bảo hiểm `31/VBHN-VPQH` (`22/08/2025`)](https://vanban.chinhphu.vn/?pageid=27160&docid=215622) | Quốc hội; Luật KDBH `08/2022/QH15` | `2026-11-05` | Nghĩa vụ thông tin (`Điều 21–22`), vô hiệu (`Điều 25`), quyền lợi được bảo hiểm (`Điều 34`), `21 ngày` cân nhắc (`Điều 35`), gia hạn phí (`Điều 37`), thế quyền (`Điều 54, 68`) |
| [Nghị định `46/2023/NĐ-CP` (`01/07/2023`)](https://vanban.chinhphu.vn/?pageid=27160&docid=208265) | Chính phủ Việt Nam | `2026-11-05` | Hạn mức chi trả `90%` và tối đa `200 triệu đồng/người/HĐ` của Quỹ bảo vệ người được bảo hiểm (`Điều 94–98`) |
| [Văn bản hợp nhất `44/2026/VBHN-TT-BTC` (`29/09/2026`)](https://vanban.chinhphu.vn/?pageid=27160&docid=217205) | Bộ Tài chính; hợp nhất `TT 67/2023` & `TT 96/2026` | `2026-11-05` | Thời gian chờ, bệnh có sẵn `36 tháng`, gia hạn `60 ngày`, khôi phục `24 tháng` (`Điều 12, 17`), mệnh giá tối thiểu (`Điều 20`), quyền lợi đầu tư (`Điều 21`), 6 loại phí & trần phí ban đầu `50%/30%/20%/2%/0%` (`Khoản 3 Điều 22`), bảng minh họa (`Điều 29`, `Mẫu 22-NT, 23-NT`), trần hoa hồng (`Điều 51`), cấm ngân hàng bán `UL/ILP` `60 ngày` quanh giải ngân & ghi âm `05 năm` (`Điều 53`) |
| [`learning/practice/models/insurance.py`](../practice/models/insurance.py) | Mô hình Python 3 của kho học tập | `2026-11-05` | Hàm `vn_ul_initial_fee_rate()` và `ul_vs_term_invest()` |
