# Bài F4 — Đọc ngân hàng Việt Nam: Biên lãi ròng (NIM), Phân loại nợ xấu, Bộ đệm dự phòng và An toàn vốn (CAR)

- Ngày cập nhật: `2026-11-05`
- Chốt dữ liệu lúc: `2026-11-05 12:00 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Đọc thông suốt báo cáo tài chính và thuyết minh quản trị rủi ro của ngân hàng thương mại Việt Nam; tính chính xác `NIM`, `CASA`, `CIR`, tỷ lệ nợ xấu (`NPL` nhóm 3–5), tỷ lệ nợ cần chú ý (nhóm 2), tỷ lệ bao phủ nợ xấu (`LLR`) và cầu nối biến động dự phòng rủi ro tín dụng; hiểu cơ chế phân loại nợ theo Thông tư `31/2024/TT-NHNN` (sửa đổi bởi Thông tư `37/2025/TT-NHNN`) và định giá ngân hàng bằng `Justified P/B`.
- Thời lượng dự kiến: `3 buổi học (~270 phút)`
  - **Buổi 1 (90 phút):** Kinh tế học bảng cân đối ngân hàng (`CASA`, `IEA`, `NIM`, `CIR`).
  - **Buổi 2 (90 phút):** Phân loại 5 nhóm nợ, liên thông `CIC`, cầu nối dự phòng – xử lý nợ (`Write-off`) và lãi dự thu.
  - **Buổi 3 (90 phút):** Hồ sơ thực tế `VCB` và `TCB`, an toàn vốn (`CAR`), xử lý dữ liệu bẩn và 10 bài tập.
- Bài trước liên quan: [Bài F3 — Doanh nghiệp bất động sản Việt Nam](F3-vietnam-property-developers.md), [Bài 013 — Ngân hàng và bảo hiểm](013-banks-insurers.md), [Bài F2 — Định giá DDM, RI và SOTP](F2-valuation-ddm-residual-sotp.md).
- Học tiếp: [Bài F5 — Khung nghiên cứu sáu ngành Việt Nam](F5-vietnam-industry-research-framework.md).
- Mô hình thực hành và hồ sơ đi kèm: [`../practice/models/valuation.py`](../practice/models/valuation.py), [`../practice/models/earnings_quality.py`](../practice/models/earnings_quality.py) và hồ sơ thực chiến [`../../research/companies/VN/VCB/report.md`](../../research/companies/VN/VCB/report.md).
- Câu hỏi cốt lõi: Vì sao hai ngân hàng có cùng mức tăng trưởng tín dụng `15%/năm` và cùng báo cáo tỷ lệ nợ xấu `1,2%`, nhưng một ngân hàng tạo ra lợi nhuận bền vững với `P/B = 2,2x` còn ngân hàng kia thực chất đang ăn mòn vốn chủ sở hữu?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/F4-fact-check.md), [phản biện](../reviews/F4-risk-review.md).

---

## Hiểu bài trong một phút

Phân tích một ngân hàng thương mại Việt Nam trên sàn `HOSE` (`VCB`, `BID`, `CTG`, `TCB`, `MBB`, `ACB`) xoay quanh **4 trụ cột gắn với quy định của Ngân hàng Nhà nước (`NHNN`)**:
1. **Chi phí vốn huy động (`CASA` và `COF`):** Ngân hàng có tỷ lệ tiền gửi không kỳ hạn (`CASA`, lãi suất `0,1%–0,5%/năm`) cao sẽ có chi phí vốn thấp, giúp duy trì Biên lãi ròng (`NIM`) tốt mà không cần cho vay bất động sản rủi ro cao (`SUY_LUẬN`).
2. **Phân loại 5 nhóm nợ và liên thông `CIC`:** Theo Thông tư `31/2024/TT-NHNN` và Thông tư `37/2025/TT-NHNN`, nợ cho vay chia thành 5 nhóm; **Nợ xấu (`NPL`) là tổng Nhóm 3 + Nhóm 4 + Nhóm 5** (`SỰ_THẬT`). Nếu một doanh nghiệp bị nợ xấu Nhóm 4 tại Ngân hàng X, Trung tâm Thông tin Tín dụng Quốc gia (`CIC`) buộc Ngân hàng Y cũng phải hạ nhóm nợ của doanh nghiệp đó xuống Nhóm 4 (`SỰ_THẬT`).
3. **Cầu nối Dự phòng (`LLR` và `Write-off`):** Tỷ lệ nợ xấu cuối kỳ thấp có thể nhờ xóa nợ bằng dự phòng (`Write-off`) hoặc giữ nợ ở Nhóm 2. Phải đọc đồng thời Nợ nhóm 2, Nợ nhóm 3–5, tỷ lệ bao phủ nợ xấu (`LLR`) và cầu nối trích lập – xử lý nợ trên Thuyết minh BCTC (`SUY_LUẬN`).
4. **Cảnh báo sớm từ Lãi và phí phải thu (`Accrued Interest`):** Khi khách hàng chưa trả lãi bằng tiền mặt nhưng khoản vay còn ở Nhóm 1–2, ngân hàng vẫn ghi "lãi dự thu" vào Thu nhập lãi. Nếu `Lãi và phí phải thu` phình to nhanh hơn dư nợ, lợi nhuận đang chứa "lãi giấy" sẽ phải thoái thu khi nợ rơi xuống Nhóm 3 (`SUY_LUẬN`).

---

## Ôn bài cũ

- Trong [Bài F3 — Doanh nghiệp bất động sản Việt Nam](F3-vietnam-property-developers.md) và [Bài 013 — Ngân hàng và công ty bảo hiểm](013-banks-insurers.md), ta đã thấy mối liên hệ giữa chu kỳ tín dụng – bất động sản và bảng cân đối ngân hàng. Bài F4 đi sâu vào chuẩn phân loại nợ, dự phòng và định giá ngân hàng Việt Nam.

---

## Buổi 1 — Kinh tế học Bảng cân đối Ngân hàng Việt Nam: CASA, NIM, CIR và PPOP

### 1.1. Bóc tách Tài sản sinh lời (`IEA`) và Nguồn vốn chịu lãi (`IBL`)

Khác với doanh nghiệp sản xuất, "hàng tồn kho" của ngân hàng chính là tiền và các khoản tín dụng. Trên Bảng cân đối kế toán của một ngân hàng Việt Nam:
- **Tài sản sinh lời (`Interest-Earning Assets — IEA`)** gồm 4 cấu phần:
  1. Tiền gửi tại NHNN và tiền gửi, cho vay các tổ chức tín dụng khác (`Interbank Placement`);
  2. Chứng khoán kinh doanh và Chứng khoán đầu tư (Trái phiếu Chính phủ, trái phiếu TCTD, và **trái phiếu doanh nghiệp**);
  3. Cho vay khách hàng (`Customer Loans` — thường chiếm `65%–75%` tổng tài sản);
  4. Các công cụ phái sinh tiền tệ sinh lãi (nếu có).
- **Nguồn vốn chịu lãi (`Interest-Bearing Liabilities — IBL`)** gồm:
  1. Tiền gửi của khách hàng (tách làm Tiền gửi không kỳ hạn + Tiền gửi ký quỹ = `CASA`, và Tiền gửi có kỳ hạn + Tiết kiệm);
  2. Phát hành giấy tờ có giá (Chứng chỉ tiền gửi, trái phiếu ngân hàng);
  3. Vay NHNN và tiền gửi/vay các tổ chức tín dụng khác.

### 1.2. Công thức tính `CASA`, `NIM` và `CIR` chuẩn xác

1. **Tỷ lệ tiền gửi không kỳ hạn (`CASA Ratio`):**
   $$\text{CASA} = \frac{\text{Tiền gửi không kỳ hạn} + \text{Tiền gửi ký quỹ}}{\text{Tổng tiền gửi của khách hàng}}$$
   *Lưu ý thực hành:* Một số bản thuyết trình IR cộng cả "tiền gửi thanh toán có kỳ hạn ngắn đặc biệt" vào CASA; khi so sánh ngang giữa các ngân hàng (như `VCB`, `TCB`, `MBB`), phải mở **Thuyết minh Tiền gửi của khách hàng** trên BCTC kiểm toán và áp dụng đúng một công thức duy nhất (`SUY_LUẬN`).

2. **Biên lãi ròng (`Net Interest Margin — NIM`):**
   $$\text{NIM} = \frac{\text{Thu nhập lãi thuần (NII)}}{\text{Tài sản sinh lời bình quân (Average IEA)}} = \text{Lợi suất tài sản sinh lời (Asset Yield)} - \text{Chi phí vốn bình quân điều chỉnh}$$
   Trong đó: $\text{Thu nhập lãi thuần (NII)} = \text{Thu nhập lãi và các khoản tương tự} - \text{Chi phí lãi và các khoản tương tự}$.
   *Cảnh báo:* Nếu lấy dư nợ cuối kỳ thay vì số dư bình quân (trung bình cộng 5 quý hoặc trung bình đầu kỳ – cuối kỳ) trong một năm ngân hàng tăng trưởng tín dụng dồn dập vào tháng 12, mẫu số sẽ bị phóng đại và làm `NIM` tính ra thấp hơn thực tế (`SUY_LUẬN`).

3. **Tỷ lệ chi phí hoạt động trên thu nhập (`Cost-to-Income Ratio — CIR`) và Lợi nhuận trước dự phòng (`PPOP`):**
   $$\text{TOI (Tổng thu nhập hoạt động)} = \text{Thu nhập lãi thuần (NII)} + \text{Lãi thuần dịch vụ} + \text{Lãi thuần ngoại hối, chứng khoán, góp vốn, hoạt động khác}$$
   $$\text{CIR} = \frac{\text{Chi phí hoạt động (OPEX)}}{\text{Tổng thu nhập hoạt động (TOI)}}$$
   $$\text{PPOP (Lợi nhuận thuần từ HĐKD trước chi phí dự phòng)} = \text{TOI} - \text{OPEX} = \text{TOI} \times (1 - \text{CIR})$$
   $$\text{LNTT (EBT)} = \text{PPOP} - \text{Chi phí dự phòng rủi ro tín dụng trong kỳ}$$

Công thức cuối cùng cho thấy bản chất của ngân hàng: **`PPOP` là "sức kiếm tiền thô" của cỗ máy ngân hàng, còn `Chi phí dự phòng rủi ro tín dụng` là cái phanh quyết định bao nhiêu phần trăm `PPOP` còn sót lại thành lợi nhuận cho cổ đông** (`SUY_LUẬN`).

---

## Buổi 2 — Năm nhóm nợ, Dự phòng rủi ro tín dụng và Bẫy "Lãi dự thu"

### 2.1. Khung pháp lý phân loại nợ và trích lập dự phòng tại Việt Nam

`SỰ_THẬT`: Hoạt động phân loại tài sản có (cho vay khách hàng, trái phiếu doanh nghiệp chưa niêm yết...) của các tổ chức tín dụng tại Việt Nam được điều chỉnh bởi [Thông tư số 31/2024/TT-NHNN](https://vanban.chinhphu.vn/?classid=1&docid=210625&pageid=27160) (sửa đổi, bổ sung bởi [Thông tư số 37/2025/TT-NHNN](https://vanban.chinhphu.vn/?classid=1&docid=215867&pageid=27160&typegroupid=6)), kết hợp với quy định trích lập dự phòng rủi ro của Chính phủ (Nghị định `86/2024/NĐ-CP`).

Bảng tóm tắt 5 nhóm nợ và nguyên tắc trích lập dự phòng chuẩn mực trong phân tích ngân hàng Việt Nam:

| Nhóm nợ | Tên gọi trên Thuyết minh BCTC | Tiêu chuẩn quá hạn định lượng cơ bản (tham chiếu quy định NHNN) | Tỷ lệ trích lập Dự phòng cụ thể ($R_i$) trên phần dư nợ sau khi trừ giá trị khấu trừ của Tài sản đảm bảo ($C_i$) | Ý nghĩa phân tích |
|---|---|---|---:|---|
| **Nhóm 1** | Nợ đủ tiêu chuẩn (`Standard`) | Trong hạn hoặc quá hạn dưới 10 ngày | `0%` | Dư nợ lành mạnh; vẫn phải trích **Dự phòng chung = `0,75%`** tổng dư nợ từ Nhóm 1 đến Nhóm 4. |
| **Nhóm 2** | Nợ cần chú ý (`Special Mention`) | Quá hạn từ 10 đến 90 ngày (hoặc cơ cấu lại thời hạn trả nợ lần đầu trong hạn theo quy định) | `5%` | **Vùng đệm cảnh báo sớm!** Nếu Nhóm 2 tăng vọt, 1–2 quý sau nợ xấu Nhóm 3–5 thường tăng theo; nhưng ở Nhóm 2 ngân hàng vẫn chưa phải thoái thu toàn bộ lãi dự thu như Nhóm 3. |
| **Nhóm 3** | Nợ dưới tiêu chuẩn (`Substandard`) | Quá hạn từ 91 đến 180 ngày | `20%` | Bắt đầu tính vào **Nợ xấu (`NPL`)**. Ngân hàng bắt buộc phải **ngừng dự thu lãi** và **thoái thu (xuất toán ra ngoại bảng)** toàn bộ số lãi dự thu đã ghi nhận trước đó mà chưa thu được tiền! |
| **Nhóm 4** | Nợ nghi ngờ (`Doubtful`) | Quá hạn từ 181 đến 360 ngày | `50%` | Thuộc **Nợ xấu (`NPL`)**; áp lực trích lập dự phòng cụ thể tăng gấp rưỡi. |
| **Nhóm 5** | Nợ có khả năng mất vốn (`Loss`) | Quá hạn trên 360 ngày (hoặc nợ cơ cấu lại nhiều lần không trả được) | `100%` | Thuộc **Nợ xấu (`NPL`)**; phần dư nợ không được tài sản đảm bảo khấu trừ phải trích lập dự phòng đủ `100%`. |

Công thức tính **Dự phòng cụ thể (`Specific Provision`)** phải trích cho một khoản nợ $i$:

$$\text{Dự phòng cụ thể}_i = R_i \times \max(0,\; \text{Dư nợ gốc}_i - \text{Giá trị khấu trừ được phép của Tài sản đảm bảo}_i)$$

*Điểm mù sống còn (`SUY_LUẬN`):* Công thức trên giải thích vì sao một ngân hàng có nhiều nợ xấu Nhóm 5 được thế chấp bằng bất động sản định giá cao có thể trích lập dự phòng cụ thể rất thấp (do $\text{Dư nợ gốc} - \text{Giá trị khấu trừ TSĐB} \approx 0$)! Khi đó, dù nợ xấu Nhóm 5 tăng mạnh, ngân hàng vẫn báo cáo chi phí dự phòng thấp, dẫn tới tỷ lệ bao phủ nợ xấu (`LLR`) tụt xuống mức mỏng manh (`40%–60%`). Nếu thị trường bất động sản đóng băng không phát mãi được tài sản thế chấp, ngân hàng đó sẽ phải trích bù dự phòng đau đớn ở các năm sau.

### 2.2. Cầu nối Số dư Dự phòng, Chi phí trích lập trong kỳ và Xử lý nợ (`Write-off`)

Không bao giờ nhầm **Số dư dự phòng rủi ro cho vay khách hàng trên Bảng cân đối kế toán (`Balance Sheet Allowance`)** với **Chi phí dự phòng rủi ro tín dụng trong kỳ trên Báo cáo KQKD (`Income Statement Provision Expense`)**. Hai đại lượng này liên kết với nhau qua phương trình cầu nối bất biến:

$$\text{Số dư dự phòng cuối kỳ} = \text{Số dư dự phòng đầu kỳ} + \text{Chi phí trích lập ròng trong kỳ (trên KQKD)} - \text{Sử dụng dự phòng để xử lý nợ xấu trong kỳ (Write-off)} \pm \text{Chênh lệch tỷ giá/khác}$$

Từ phương trình này, ta rút ra công thức tính **Tổng nợ xấu hình thành mới thực chất trong kỳ (`New NPL Formation`)**:

$$\text{Nợ xấu hình thành ròng trong kỳ} = (\text{Nợ xấu cuối kỳ} - \text{Nợ xấu đầu kỳ}) + \text{Nợ xấu đã xóa bằng dự phòng trong kỳ (Write-off)}$$

Nếu một ngân hàng có Nợ xấu cuối kỳ giữ nguyên ở mức `10.000 tỷ VND` như đầu kỳ, nhưng trong năm đã dùng `8.000 tỷ VND` quỹ dự phòng để xóa nợ (`Write-off`), thì thực chất trong năm đó ngân hàng đã phát sinh thêm tới **`8.000 tỷ VND` nợ xấu mới** (`PHÉP_TÍNH`)!

### 2.3. Cảnh báo sớm từ Trái phiếu doanh nghiệp và Lãi dự thu

Tại Việt Nam, nhiều ngân hàng cấp tín dụng cho các chủ đầu tư bất động sản không chỉ qua mục **Cho vay khách hàng** mà còn qua mục **Chứng khoán đầu tư — Trái phiếu do các tổ chức kinh tế trong nước phát hành**. Vì vậy, khi kiểm tra rủi ro tín dụng, bạn bắt buộc phải:
1. Mở cả **Thuyết minh Cho vay khách hàng** lẫn **Thuyết minh Chứng khoán đầu tư** để cộng tổng dư nợ và dự phòng cụ thể của trái phiếu doanh nghiệp (như cách ta đã làm trong hồ sơ thực chiến [`../../research/companies/VN/VCB/report.md`](../../research/companies/VN/VCB/report.md)).
2. Tính tỷ số **Lãi và phí phải thu / Tổng tài sản sinh lời** (hoặc số ngày dự thu lãi bình quân = $\text{Lãi phải thu} / \text{Thu nhập lãi trong năm} \times 365$). Ngân hàng có chất lượng thu lãi bằng tiền mặt tốt (như `VCB`, `ACB`) thường có tỷ lệ lãi dự thu rất thấp (`< 1,0%` dư nợ); ngân hàng có lãi dự thu phình to lên `2,5%–4,0%` dư nợ là tín hiệu rủi ro nợ xấu tiềm ẩn cực lớn (`SUY_LUẬN`).

---

## 3. Ví dụ từ nguồn thật: Đối chiếu Vietcombank (Q3/9T 2026) và Techcombank (FY2025)

Chúng ta đối chiếu trực tiếp hai bộ dữ liệu ngân hàng thực tế đã được kiểm chứng trong kho nghiên cứu:

### 3.1. Vietcombank (`VCB`) — BCTC hợp nhất Quý 3 / 9 tháng năm 2026
Theo Báo cáo tài chính hợp nhất Quý 3/2026 của Ngân hàng TMCP Ngoại thương Việt Nam (`VCB`, ký ngày `30/10/2026`, lưu vết và kiểm nguồn độc lập tại [`../../research/companies/VN/VCB/report.md`](../../research/companies/VN/VCB/report.md) và [`../../research/companies/VN/VCB/fact-check.md`](../../research/companies/VN/VCB/fact-check.md)):
- **Dư nợ cho vay khách hàng và 5 nhóm nợ tại `30/09/2026` (`SỰ_THẬT`, Thuyết minh trang 27–28 BCTC):**
  - Tổng dư nợ cho vay khách hàng: `1.816.093.286 triệu VND` (`1.816.093,29 tỷ VND`).
  - Nợ nhóm 2 (Nợ cần chú ý): `7.129.365 triệu VND` (`7.129,37 tỷ VND`, chiếm `0,3926%` dư nợ).
  - Nợ nhóm 3 (Dưới tiêu chuẩn): `2.571.437 triệu VND` (`2.571,44 tỷ VND`).
  - Nợ nhóm 4 (Nghi ngờ): `1.657.212 triệu VND` (`1.657,21 tỷ VND`).
  - Nợ nhóm 5 (Có khả năng mất vốn): `8.588.936 triệu VND` (`8.588,94 tỷ VND`).
- **Phép tính tái lập chất lượng tài sản của `VCB` (`PHÉP_TÍNH`):**
  - Tổng nợ xấu nội bảng (`Nhóm 3 + Nhóm 4 + Nhóm 5`):
    $$\text{NPL}_{30/09/2026} = 2.571.437 + 1.657.212 + 8.588.936 = 12.817.585\text{ triệu VND}\; (12.817,59\text{ tỷ VND})$$
    (So với đầu kỳ trình bày lại là $761.291 + 301.991 + 8.650.658 = 9.713.940\text{ triệu VND}$).
  - Tỷ lệ nợ xấu (`NPL Ratio`):
    $$\text{NPL Ratio} = \frac{12.817,585}{1.816.093,286} = 0,7058\%\; (\approx 0,71\%)$$
  - Cầu nối quỹ dự phòng rủi ro cho vay khách hàng 9 tháng năm 2026:
    - Dự phòng chung: Đầu kỳ `12.422.952` + Trích lập `1.002.848` $-$ Khác `1.177` = **`13.424.623 triệu VND`**.
    - Dự phòng cụ thể: Đầu kỳ `12.557.439` + Trích lập `5.186.666` $-$ Khác `621` = **`17.743.484 triệu VND`** (dòng sử dụng dự phòng xử lý nợ để dấu gạch ngang).
    - Tổng số dư dự phòng cho vay khách hàng cuối kỳ:
      $$13.424.623 + 17.743.484 = 31.168.107\text{ triệu VND}\; (31.168,11\text{ tỷ VND})$$
  - Tỷ lệ bao phủ nợ xấu (`LLR — Loan Loss Reserve Coverage`):
    $$\text{LLR} = \frac{31.168,107}{12.817,585} = 243,17\%$$
- **Bài học đọc sâu Thuyết minh Chứng khoán đầu tư của `VCB` (`SỰ_THẬT` & `SUY_LUẬN`):**
  - Nếu chỉ nhìn bảng cho vay khách hàng (`NPL = 0,71%`, `LLR = 243,17%`), người đọc sẽ bỏ sót biến động tại mục **Chứng khoán đầu tư giữ đến ngày đáo hạn**: Số dư dự phòng cụ thể cho trái phiếu tổ chức kinh tế tăng từ `3.306,873 tỷ VND` đầu năm lên **`6.303,616 tỷ VND`** tại `30/09/2026` (tăng thêm **`+2.996,743 tỷ VND`**, tức `+90,62%`, trên danh mục trái phiếu tổ chức kinh tế nắm giữ đến đáo hạn `6.501,250 tỷ VND` — `PHÉP_TÍNH`). Điều này chứng minh quy tắc vàng: **Đọc ngân hàng Việt Nam bắt buộc phải cộng kiểm tra cả dự phòng trái phiếu doanh nghiệp trong mục Chứng khoán đầu tư!**

### 3.2. Techcombank (`TCB`) — Chênh lệch tỷ lệ nợ xấu trước và sau phân loại liên thông CIC
- `SỰ_THẬT`: Trong [Báo cáo kết quả kinh doanh năm 2025 của Techcombank](https://techcombank.com/content/dam/techcombank/public-site/documents/bao-cao-ket-qua-kinh-doanh-2025-ke-hoach-2026-eng.pdf) (công bố ngày `03/04/2026`), ngân hàng trình bày hai con số tỷ lệ nợ xấu cuối năm 2025:
  - Tỷ lệ nợ xấu **trước ảnh hưởng phân loại lại theo CIC**: **`0,98%`**;
  - Tỷ lệ nợ xấu **sau ảnh hưởng phân loại lại theo CIC**: **`1,13%`** (chênh lệch `+0,15 điểm phần trăm`, tương đương `+15 bps`).
- `SUY_LUẬN`: Khoản chênh lệch `0,15%` này chính là những khách hàng vẫn đang trả nợ bình thường tại Techcombank nhưng bị hạ nhóm nợ tại các ngân hàng khác trên hệ thống `CIC`, buộc Techcombank phải hạ nhóm nợ tương ứng theo quy định của NHNN. Khi so sánh hai ngân hàng, không bao giờ được lấy số "trước CIC" của ngân hàng này đi so với số "sau CIC" của ngân hàng kia!

---

## Buổi 3 — An toàn vốn (CAR), Định giá Ngân hàng (Justified P/B) và Xử lý dữ liệu bẩn

### 4.1. Tỷ lệ an toàn vốn (`CAR` — Capital Adequacy Ratio) và Đòn bẩy

$$\text{CAR} = \frac{\text{Vốn tự có hợp lệ (Vốn cấp 1 + Vốn cấp 2 - Các khoản giảm trừ)}}{\text{Tổng Tài sản có rủi ro tín dụng} + 12,5 \times (\text{Vốn yêu cầu cho rủi ro hoạt động} + \text{Vốn yêu cầu cho rủi ro thị trường})}$$

- **Không nhầm `Vốn chủ sở hữu / Tổng tài sản` với `CAR`:** Một ngân hàng có `Vốn chủ sở hữu / Tổng tài sản = 8%`, nhưng nếu danh mục tài sản nắm giữ nhiều Trái phiếu Chính phủ (hệ số rủi ro `0%`) và cho vay bán lẻ thế chấp nhà ở (hệ số rủi ro thấp hơn cho vay kinh doanh bất động sản thường có hệ số rủi ro `150%–200%`), thì `CAR` của ngân hàng đó có thể đạt `12%–15%`. Ngược lại, ngân hàng dồn vốn vào cho vay dự án bất động sản và trái phiếu doanh nghiệp sẽ bị đội mẫu số Tài sản có rủi ro (`RWA`) lên rất cao, làm `CAR` bị ép xuống (`SUY_LUẬN`).
- **Chất lượng Vốn cấp 1 (`Tier 1 Capital`) vs. Vốn cấp 2 (`Tier 2 Capital`):** Vốn cấp 1 (vốn điều lệ, thặng dư vốn, lợi nhuận giữ lại) là vốn tự có vĩnh viễn, không phải trả lãi. Vốn cấp 2 chủ yếu là trái phiếu thứ cấp dài hạn do ngân hàng phát hành — thực chất vẫn là nợ vay chịu lãi suất cao và sẽ bị khấuấu trừ dần trong 5 năm cuối trước khi đáo hạn. Một ngân hàng có `CAR = 11%` nhưng `Tier 1 = 10,5%` vững mạnh hơn nhiều so với ngân hàng có `CAR = 11%` nhưng `Tier 1` chỉ đạt `7,0%` và phải dựa vào `4,0%` trái phiếu cấp 2 (`SUY_LUẬN`).

### 4.2. Định giá ngân hàng bằng `Justified P/B` điều chỉnh chất lượng bộ đệm dự phòng

Tương tự Bài [013](013-banks-insurers.md) và mô-đun [`../practice/models/valuation.py`](../practice/models/valuation.py), bội số `P/B hợp lý` của ngân hàng được xác định bởi:

$$\left(\frac{P}{B}\right)_{\text{hợp lý}} = \frac{\text{ROE}_{\text{bền vững}} - g}{k_e - g}$$

Tuy nhiên, trước khi đưa Giá trị sổ sách (`Book Value — B_0`) và `ROE` vào công thức, nhà phân tích ngân hàng Việt Nam phải thực hiện **bước kiểm tra chất lượng sổ sách (`Adjusted Book Value`)**:
- Nếu Ngân hàng A có `LLR = 243%` (như `VCB`), bộ đệm dự phòng dư thừa đóng vai trò như một phần "vốn chủ sở hữu ẩn" bảo vệ `ROE` khỏi biến động chu kỳ.
- Ngược lại, nếu Ngân hàng B chỉ có `LLR = 45%`, nhiều nợ nhóm 2 và lãi dự thu treo cao, bạn phải thử kịch bản **trích bù dự phòng để đưa `LLR` lên mức an toàn (ví dụ `80%–100%`)** và **thoái thu phần lãi dự thu nghi ngờ**, rồi trừ phần thiếu hụt sau thuế đó khỏi Vốn chủ sở hữu $B_0$ trước khi nhân bội số `P/B` (`SUY_LUẬN`).

---

## 5. Bài làm với dữ liệu thiếu hoặc lệch (Dirty-Data Exercise)

### Tình huống dữ liệu bẩn
Ngân hàng TMCP H công bố Bản tin nhà đầu tư năm 2025 với thông điệp:
> *"Năm 2025, lợi nhuận trước thuế của Ngân hàng H tăng trưởng +25% đạt 8.000 tỷ VND, ROE đạt 18,5%, tỷ lệ nợ xấu nội bảng giảm từ 1,90% xuống chỉ còn 1,60% trên tổng dư nợ cho vay 400.000 tỷ VND. Cổ phiếu đang giao dịch ở P/B = 1,05 lần — quá rẻ cho một ngân hàng có ROE 18,5%!"*

Khi mở **Báo cáo tài chính hợp nhất kiểm toán năm 2025** của Ngân hàng H, bạn phát hiện 4 dữ kiện bị lược bỏ khỏi bản tin tóm tắt (`KỊCH_BẢN`):
1. Trong năm 2025, dù nợ xấu cuối kỳ là `6.400 tỷ VND` (`1,60%` của `400.000 tỷ`), nhưng tại Thuyết minh Dự phòng rủi ro cho vay khách hàng, ngân hàng chỉ trích lập dự phòng mới trên KQKD là `3.200 tỷ VND` trong khi đã **sử dụng `5.000 tỷ VND` quỹ dự phòng để xóa nợ xấu ngoại bảng (`Write-off`)**, làm tổng số dư quỹ dự phòng cuối kỳ sụt giảm từ `5.100 tỷ VND` xuống chỉ còn **`3.300 tỷ VND`** (`LLR` tụt xuống `51,56%`).
2. Nợ nhóm 2 (Nợ cần chú ý) tăng vọt từ `6.000 tỷ VND` (`1,8%` dư nợ đầu năm) lên **`18.000 tỷ VND`** (`4,50%` dư nợ cuối năm).
3. Khoản mục **Lãi và phí phải thu** trên Bảng cân đối kế toán tăng gấp đôi từ `4.800 tỷ VND` lên **`10.200 tỷ VND`** (tăng thêm `+5.400 tỷ VND`, tương đương `67,5%` toàn bộ Lợi nhuận trước thuế của cả năm!).
4. Tại Thuyết minh Chứng khoán đầu tư, ngân hàng nắm giữ `22.000 tỷ VND` trái phiếu doanh nghiệp bất động sản chưa niêm yết của các chủ đầu tư đang chậm tiến độ, nhưng mới chỉ trích lập dự phòng chung `0,75%` (`165 tỷ VND`) và chưa trích dự phòng cụ thể.

### Quy trình làm sạch và điều chỉnh định giá
1. **Tính lượng nợ xấu hình thành mới thực tế (`New NPL Formation`):**
   - Nợ xấu đầu năm (theo thông tin bản tin): $6.400 / 0,016 \text{ (dư nợ cuối)} \rightarrow$ giả sử nợ xấu đầu năm là `6.650 tỷ VND` (tương ứng `1,90%` trên dư nợ đầu năm `350.000 tỷ VND`).
   - Nợ xấu hình thành ròng trong năm 2025 = $(6.400 - 6.650) + 5.000\text{ (Write-off)} = +4.750\text{ tỷ VND}$ (`PHÉP_TÍNH`). Tỷ lệ nợ xấu giảm trên bề mặt chỉ là kết quả của việc xả quỹ dự phòng để xóa nợ (`LLR` rơi từ `76,69%` xuống `51,56%`)!
2. **Ước tính chi phí dự phòng bị thiếu hụt và lãi dự thu có nguy cơ thoái thu (`Bear Stress Test`):**
   - Để nâng bộ đệm `LLR` của mảng cho vay từ `51,56%` (`3.300 tỷ`) lên mức trung bình an toàn `100%` (`6.400 tỷ`), ngân hàng đang thiếu **`3.100 tỷ VND`** dự phòng.
   - Nếu `25%` khoản Lãi dự thu tăng đột biến (`+5.400 tỷ VND`) và `15%` danh mục Nợ nhóm 2 (`18.000 tỷ VND`) + Trái phiếu BĐS (`22.000 tỷ VND`) chuyển thành tổn thất cần trích lập/thoái thu thêm khoảng **`3.500 tỷ VND`**, thì tổng chi phí trước thuế chưa phản ánh hết lên tới `6.600 tỷ VND` (sau thuế TNDN `20%` là **`5.280 tỷ VND`**).
3. **Kết luận định giá:** Con số `ROE = 18,5%` là lợi nhuận kế toán đạt được nhờ chậm trích lập dự phòng và treo lãi dự thu. Sau khi trừ khoản đệm thiếu hụt ước tính `5.280 tỷ VND` khỏi Vốn chủ sở hữu, `P/B` thực chất của Ngân hàng H không hề rẻ ở mức `1,05x`, mà đang tiềm ẩn rủi ro pha loãng hoặc suy giảm lợi nhuận kéo dài 2–3 năm để dọn sạch bảng cân đối (`SUY_LUẬN`).

---

## 6. Sai ở đâu? (Bắt lỗi suy luận)

Hãy chỉ ra chỗ sai trong nhận định sau:

> *"Ngân hàng X có Tỷ lệ bao phủ nợ xấu (LLR) đạt 150%, nghĩa là cứ 100 đồng nợ xấu thì ngân hàng đã để sẵn 150 đồng tiền mặt trong két sắt để dự phòng. Nếu toàn bộ nợ xấu hiện tại mất trắng 100%, ngân hàng chẳng những không mất đồng nào mà còn lời ra 50 đồng tiền mặt!"*

### Phân tích chỗ sai
1. **Nhầm lẫn "Số dư Dự phòng rủi ro tín dụng" với "Két sắt tiền mặt":** Khoản mục `Dự phòng rủi ro cho vay khách hàng` (số âm nằm ngay dưới dòng `Cho vay khách hàng` bên phần Tài sản của Bảng cân đối kế toán) là một **tài khoản điều chỉnh giảm giá trị ghi sổ của khoản vay (`Contra-Asset Account`)**, hoàn toàn **không phải là một quỹ tiền mặt nằm riêng trong két sắt**! Khi ngân hàng trích lập dự phòng `150 đồng`, ngân hàng đã ghi nhận trước `150 đồng` chi phí lên Báo cáo KQKD ở các kỳ trước (làm giảm lợi nhuận giữ lại và giảm giá trị ghi sổ thuần của dư nợ cho vay đi `150 đồng`), còn tiền mặt thực tế của ngân hàng nằm ở mục Tiền mặt và Tiền gửi tại NHNN (`SỰ_THẬT`).
2. **Hiểu đúng ý nghĩa của `LLR = 150%`:** Nếu `100 đồng` nợ xấu hiện tại thực sự mất trắng và không thu hồi được đồng nào từ tài sản thế chấp, ngân hàng sẽ không nhận về thêm đồng tiền mặt nào cả; nhưng nhờ đã trích trước `150 đồng` chi phí vào các năm trước, **Báo cáo KQKD của năm hiện tại sẽ không bị lỗ thêm** (và nếu xóa sổ `100 đồng` nợ xấu đó, ngân hàng còn dư `50 đồng` bộ đệm kế toán để che chắn cho các khoản nợ nhóm 2 có thể chuyển thành nợ xấu mới trong tương lai) (`SUY_LUẬN`).

---

## 7. Bài tập (10 câu)

1. Một ngân hàng có Thu nhập lãi và các khoản tương tự trong năm là `68.000 tỷ VND`, Chi phí lãi và các khoản tương tự là `36.000 tỷ VND`. Tài sản sinh lời đầu năm là `760.000 tỷ VND` và cuối năm là `840.000 tỷ VND`. Tính Thu nhập lãi thuần (`NII`), Tài sản sinh lời bình quân (`Average IEA`), Lợi suất tài sản sinh lời (`Asset Yield`) và Biên lãi ròng (`NIM`).
2. Tiếp nối Câu 1: Trong năm, ngân hàng có Lãi thuần từ hoạt động dịch vụ `5.200 tỷ VND`, Lãi thuần từ kinh doanh ngoại hối và hoạt động khác `2.800 tỷ VND`, Chi phí hoạt động (`OPEX`) `13.600 tỷ VND`, và Chi phí dự phòng rủi ro tín dụng trong năm `8.400 tỷ VND`. Tính Tổng thu nhập hoạt động (`TOI`), Tỷ lệ `CIR`, Lợi nhuận thuần trước dự phòng (`PPOP`), Lợi nhuận trước thuế (`EBT`) và tỷ lệ `Chi phí dự phòng / PPOP`.
3. Cuối năm 2025, Ngân hàng M có cơ cấu Tiền gửi của khách hàng gồm: Tiền gửi không kỳ hạn `142.000 tỷ VND`, Tiền gửi có kỳ hạn và tiền gửi tiết kiệm `448.000 tỷ VND`, Tiền gửi ký quỹ `10.000 tỷ VND`. Tính Tổng tiền gửi khách hàng và tỷ lệ `CASA` của Ngân hàng M.
4. Theo số liệu thực tế của `Vietcombank (VCB)` tại ngày `30/09/2026` trong Mục 3.1: Tổng dư nợ cho vay là `1.816.093,286 tỷ VND`, Nợ nhóm 2 là `7.129,365 tỷ VND`, Nợ nhóm 3 là `2.571,437 tỷ VND`, Nợ nhóm 4 là `1.657,212 tỷ VND`, Nợ nhóm 5 là `8.588,936 tỷ VND`. Hãy tính lại: (a) Tổng nợ xấu (`NPL` nhóm 3–5); (b) Tỷ lệ nợ xấu (`NPL Ratio`); và (c) Tổng tỷ lệ nợ có vấn đề (`Nợ nhóm 2 + Nợ nhóm 3–5`) trên tổng dư nợ.
5. Vẫn với số liệu `VCB` tại ngày `30/09/2026`: Số dư dự phòng chung là `13.424,623 tỷ VND` và dự phòng cụ thể là `17.743,484 tỷ VND`. Tính tổng số dư quỹ dự phòng cho vay khách hàng, tỷ lệ bao phủ nợ xấu (`LLR = Tổng dự phòng / NPL nhóm 3–5`) và tỷ lệ bao phủ trên tổng nợ nhóm 2–5 (`Tổng dự phòng / (Nhóm 2 + Nhóm 3–5)`).
6. Ngân hàng K có số dư quỹ dự phòng rủi ro cho vay khách hàng đầu năm là `9.000 tỷ VND`. Trong năm, ngân hàng ghi nhận Chi phí dự phòng rủi ro cho vay trên Báo cáo KQKD là `6.500 tỷ VND` và đã sử dụng `4.800 tỷ VND` dự phòng để xóa nợ xấu đưa ra theo dõi ngoại bảng (`Write-off`). Tính số dư quỹ dự phòng rủi ro cho vay cuối năm (giả sử không có biến động tỷ giá).
7. Tiếp nối Câu 6: Biết số dư Nợ xấu nội bảng (`Nhóm 3–5`) của Ngân hàng K đầu năm là `7.200 tỷ VND` và cuối năm là `7.900 tỷ VND`. Hãy tính tổng lượng **Nợ xấu hình thành ròng trong năm (`New NPL Formation`)** của Ngân hàng K. Nếu người đọc chỉ nhìn mức tăng nợ xấu trên bảng cân đối (`7.900 - 7.200 = +700 tỷ VND`), họ đã bỏ sót bao nhiêu phần trăm nợ xấu mới thực tế phát sinh?
8. Một khoản vay doanh nghiệp có dư nợ gốc `200 tỷ VND` bị quá hạn 210 ngày và phân loại vào **Nhóm 4 (Nợ nghi ngờ, tỷ lệ trích lập cụ thể $R_4 = 50\%$)**. Tài sản đảm bảo của khoản vay được định giá và áp tỷ lệ khấu trừ hợp lệ theo quy định là `110 tỷ VND`. Tính số tiền Dự phòng cụ thể mà ngân hàng phải trích lập cho khoản vay này. Nếu sau đó khoản vay quá hạn trên 360 ngày chuyển sang **Nhóm 5 ($R_5 = 100\%$)** và giá trị khấu trừ tài sản đảm bảo giảm xuống còn `80 tỷ VND`, số tiền Dự phòng cụ thể phải trích tăng lên thành bao nhiêu?
9. Giải thích vì sao một ngân hàng có tỷ lệ `Vốn chủ sở hữu / Tổng tài sản = 9,5%` vẫn có thể có Tỷ lệ an toàn vốn (`CAR`) thấp hơn một ngân hàng có `Vốn chủ sở hữu / Tổng tài sản = 8,2%`.
10. Sử dụng hàm `justified_pb` trong mô-đun [`../practice/models/valuation.py`](../practice/models/valuation.py): Ngân hàng X có Giá trị sổ sách mỗi cổ phiếu (`BVPS`) = `28.000 VND/CP`, chi phí vốn chủ sở hữu $k_e = 12,0\%/\text{năm}$ và tốc độ tăng trưởng dài hạn $g = 6,0\%/\text{năm}$. Tính `P/B hợp lý` và giá trị hợp lý mỗi cổ phiếu trong hai kịch bản: (a) Kịch bản Cơ sở với $\text{ROE} = 18,0\%$; và (b) Kịch bản Bất lợi khi chi phí dự phòng tăng làm $\text{ROE}$ giảm xuống `10,5%`.

---

## 8. Đáp án chi tiết

1. **Tính `NII`, `Average IEA`, `Asset Yield` và `NIM`:**
   - $\text{NII} = 68.000 - 36.000 = 32.000\text{ tỷ VND}$.
   - $\text{Average IEA} = (760.000 + 840.000) / 2 = 800.000\text{ tỷ VND}$.
   - $\text{Asset Yield} = 68.000 / 800.000 = 8,50\%/\text{năm}$.
   - $\text{NIM} = 32.000 / 800.000 = 4,00\%/\text{năm}$ (`PHÉP_TÍNH`).
2. **Tính `TOI`, `CIR`, `PPOP`, `EBT` và gánh nặng dự phòng:**
   - $\text{TOI} = 32.000 + 5.200 + 2.800 = 40.000\text{ tỷ VND}$.
   - $\text{CIR} = 13.600 / 40.000 = 34,00\%$.
   - $\text{PPOP} = 40.000 - 13.600 = 26.400\text{ tỷ VND}$.
   - $\text{EBT} = 26.400 - 8.400 = 18.000\text{ tỷ VND}$.
   - Tỷ lệ `Chi phí dự phòng / PPOP` = $8.400 / 26.400 = 31,82\%$ (`PHÉP_TÍNH`).
3. **Tính Tổng tiền gửi và tỷ lệ `CASA`:**
   - Tổng tiền gửi khách hàng = $142.000 + 448.000 + 10.000 = 600.000\text{ tỷ VND}$.
   - Tổng `CASA` (Tiền gửi không kỳ hạn + Tiền gửi ký quỹ) = $142.000 + 10.000 = 152.000\text{ tỷ VND}$.
   - Tỷ lệ `CASA` = $152.000 / 600.000 = 25,33\%$ (`PHÉP_TÍNH`).
4. **Tính `NPL` và tỷ lệ nợ có vấn đề của `VCB` tại `30/09/2026`:**
   - (a) Tổng nợ xấu (`Nhóm 3–5`) = $2.571,437 + 1.657,212 + 8.588,936 = 12.817,585\text{ tỷ VND}$.
   - (b) Tỷ lệ nợ xấu (`NPL Ratio`) = $12.817,585 / 1.816.093,286 = 0,7058\%$ (`~0,71%`).
   - (c) Tổng nợ nhóm 2–5 = $7.129,365 + 12.817,585 = 19.946,950\text{ tỷ VND}$; Tỷ lệ trên tổng dư nợ = $19.946,950 / 1.816.093,286 = 1,0983\%$ (`~1,10%`) (`PHÉP_TÍNH`).
5. **Tính độ bao phủ dự phòng (`LLR`) của `VCB` tại `30/09/2026`:**
   - Tổng quỹ dự phòng cho vay khách hàng = $13.424,623 + 17.743,484 = 31.168,107\text{ tỷ VND}$.
   - `LLR` trên nợ xấu nhóm 3–5 = $31.168,107 / 12.817,585 = 243,17\%$.
   - Độ bao phủ trên tổng nợ nhóm 2–5 = $31.168,107 / 19.946,950 = 156,25\%$ — tức ngay cả khi cộng toàn bộ nợ nhóm 2 vào nợ xấu, quỹ dự phòng nội bảng của `VCB` vẫn bao phủ tới `156,25%` (`PHÉP_TÍNH`).
6. **Cầu nối quỹ dự phòng cuối năm của Ngân hàng K:**
   - $\text{Số dư dự phòng cuối năm} = 9.000 + 6.500 - 4.800 = 10.700\text{ tỷ VND}$ (`PHÉP_TÍNH`).
7. **Tính lượng Nợ xấu hình thành ròng (`New NPL Formation`) của Ngân hàng K:**
   - $\text{Nợ xấu hình thành ròng} = (7.900 - 7.200) + 4.800\text{ (Write-off)} = 700 + 4.800 = 5.500\text{ tỷ VND}$.
   - Nếu chỉ nhìn mức tăng `+700 tỷ VND` trên bảng cân đối, người đọc đã bỏ sót $4.800 / 5.500 = 87,27\%$ lượng nợ xấu mới thực tế phát sinh trong năm (`PHÉP_TÍNH`)!
8. **Tính Dự phòng cụ thể theo nhóm nợ và khấu trừ tài sản đảm bảo:**
   - Khi ở Nhóm 4 ($R_4 = 50\%$, khấu trừ TSĐB `110 tỷ`):
     $$\text{DP cụ thể}_{\text{Nhóm 4}} = 50\% \times (200 - 110) = 45\text{ tỷ VND}$$
   - Khi rơi xuống Nhóm 5 ($R_5 = 100\%$, khấu trừ TSĐB giảm còn `80 tỷ`):
     $$\text{DP cụ thể}_{\text{Nhóm 5}} = 100\% \times (200 - 80) = 120\text{ tỷ VND}$$
   - Ngân hàng phải trích lập bổ sung thêm $120 - 45 = 75\text{ tỷ VND}$ chi phí dự phòng (`PHÉP_TÍNH`).
9. **Vì sao `VCSH / Tổng tài sản` cao hơn nhưng `CAR` lại thấp hơn:**
   - Mẫu số của `CAR` là **Tài sản có điều chỉnh theo hệ số rủi ro (`RWA`)** cộng vốn yêu cầu cho rủi ro hoạt động và thị trường, còn tử số là Vốn tự có hợp lệ (đã trừ các khoản giảm trừ). Nếu ngân hàng có `VCSH / Tổng tài sản = 9,5%` nhưng cho vay tập trung vào các khoản tín dụng hệ số rủi ro cao (`150%–200%`) hoặc có các khoản đầu tư chéo phải trừ khỏi vốn tự có, thì `CAR` sẽ thấp hơn ngân hàng có `VCSH / Tổng tài sản = 8,2%` nhưng nắm nhiều Trái phiếu Chính phủ (`0%` rủi ro) và cho vay bán lẻ chuẩn mực (`SUY_LUẬN`).
10. **Định giá bằng hàm `justified_pb` (`BVPS = 28.000`, $k_e = 12,0\%$, $g = 6,0\%$):**
    - (a) Kịch bản Cơ sở ($\text{ROE} = 18,0\%$):
      $$(P/B)_{\text{Cơ sở}} = \frac{0,180 - 0,060}{0,120 - 0,060} = \frac{0,120}{0,060} = 2,00\text{ lần} \implies P_{\text{Cơ sở}} = 28.000 \times 2,00 = 56.000\text{ VND/CP}$$
    - (b) Kịch bản Bất lợi ($\text{ROE} = 10,5\% < k_e = 12,0\%$):
      $$(P/B)_{\text{Bất lợi}} = \frac{0,105 - 0,060}{0,120 - 0,060} = \frac{0,045}{0,060} = 0,75\text{ lần} \implies P_{\text{Bất lợi}} = 28.000 \times 0,75 = 21.000\text{ VND/CP}\quad (\text{PHÉP\_TÍNH})$$

---

## 9. Kiểm tra chuyển bài (Transfer Check)

Trước khi chuyển sang Bài [F8 — Phân tích doanh nghiệp bảo hiểm Việt Nam](F8-vietnam-insurance-analysis.md) hoặc Bài [F5 — Khung nghiên cứu sáu ngành Việt Nam](F5-vietnam-industry-research-framework.md), hãy tự kiểm tra 3 câu hỏi sau:
1. **Đối chiếu Ngân hàng (`F4`) với Bảo hiểm (`F8`):** Trong ngân hàng, nguồn vốn huy động chủ lực là Tiền gửi khách hàng (trong đó `CASA` có chi phí gần bằng `0%`); còn trong công ty bảo hiểm phi nhân thọ/nhân thọ (như `BVH`, `PVI`, `BIC`), nguồn vốn tương đương với `CASA` là gì và khi nào nguồn vốn đó có chi phí âm?
2. **Kiểm tra chéo liên thông Ngân hàng – Bảo hiểm (`Bancassurance`):** Khi đọc hồ sơ `BIC` (công ty con của ngân hàng `BIDV`), `BIC` gửi `4.428,50 tỷ VND` tiền gửi có kỳ hạn tại `BIDV`. Khoản tiền đó nằm ở mục nào trên BCTC của `BIC` và nằm ở mục nào trên BCTC riêng của `BIDV`?
3. **Kỷ luật đọc thuyết minh nợ xấu:** Bạn đã nhớ quy tắc bắt buộc phải mở đồng thời cả **Thuyết minh Cho vay khách hàng** lẫn **Thuyết minh Chứng khoán đầu tư (Trái phiếu tổ chức kinh tế)** và lập cầu nối `Write-off` trước khi tin vào con số tỷ lệ nợ xấu bề mặt chưa?

---

## 10. Lỗi thường gặp và ranh giới an toàn

- **Bốn lỗi phân tích phổ biến:** (1) So sánh `NIM` và `NPL` giữa hai ngân hàng mà không kiểm tra định nghĩa trước/sau phân loại `CIC`; (2) Nhìn tỷ lệ nợ xấu giảm mà quên cộng lượng nợ đã xóa bằng dự phòng (`Write-off`) và quên nhìn Nợ nhóm 2 + Lãi dự thu; (3) Bỏ qua danh mục Trái phiếu doanh nghiệp nằm trong mục Chứng khoán đầu tư; (4) Coi số dư quỹ dự phòng là tiền mặt nằm sẵn trong két.
- **Ranh giới an toàn:** Mọi số liệu của `Vietcombank (VCB)` và `Techcombank (TCB)` trong bài chỉ dùng làm tài liệu học tập cách đọc thuyết minh BCTC, tuyệt đối không phải khuyến nghị mua/bán cổ phiếu hay đánh giá tín nhiệm cá nhân hóa.

## Nguồn Internet đã mở

- Chốt kiểm tra trực tuyến lúc `2026-11-05 12:00 UTC+7`:
  1. [Cổng Thông tin điện tử Chính phủ — Thông tư số 31/2024/TT-NHNN](https://vanban.chinhphu.vn/?classid=1&docid=210625&pageid=27160) và [Thông tư số 37/2025/TT-NHNN](https://vanban.chinhphu.vn/?classid=1&docid=215867&pageid=27160&typegroupid=6) quy định về phân loại tài sản có trong hoạt động của tổ chức tín dụng.
  2. [Hồ sơ nghiên cứu đã kiểm duyệt — Ngân hàng TMCP Ngoại thương Việt Nam (VCB)](../../research/companies/VN/VCB/report.md) và [BCTC hợp nhất Quý 3/2026 của VCB](https://cdn.24hmoney.vn/upload/file/2026-4/2026-10-31/no-name-1793388232.pdf), ký ngày `30/10/2026`.
  3. [Techcombank — Báo cáo kết quả kinh doanh năm 2025](https://techcombank.com/content/dam/techcombank/public-site/documents/bao-cao-ket-qua-kinh-doanh-2025-ke-hoach-2026-eng.pdf), ngày `03/04/2026`.
