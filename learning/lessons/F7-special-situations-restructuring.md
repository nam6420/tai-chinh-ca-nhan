# Bài F7 — Tình huống đặc biệt: M&A, Tái cấu trúc, Phát hành pha loãng và Thủ tục Phục hồi – Phá sản

- Ngày cập nhật: `2026-11-05`
- Chốt dữ liệu lúc: `2026-11-05 12:05 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Phân tích các sự kiện doanh nghiệp đặc biệt (`Special Situations`) tại Việt Nam: mua bán và sáp nhập (`M&A`), kế toán hợp nhất kinh doanh và lợi thế thương mại (`Goodwill`), phát hành cổ phiếu tăng vốn / hoán đổi nợ (`Debt-to-Equity Swap`), phân biệt tác động pha loãng tỷ lệ biểu quyết với tác động tạo/hủy giá trị kinh tế trên mỗi cổ phiếu (`Accretion / Dilution`), và nắm vững ranh giới pháp lý giữa mất thanh khoản tạm thời, tái cơ cấu nợ tự nguyện với thủ tục phục hồi / phá sản theo Luật Phục hồi, phá sản số `142/2025/QH15`.
- Thời lượng dự kiến: `3 buổi học (~270 phút)`
  - **Buổi 1 (90 phút):** Vòng đời một thương vụ `M&A` và Tái cấu trúc tập đoàn — Từ Nghị quyết chủ trương đến Điều kiện tiên quyết (`Conditions Precedent`), hoàn tất giao dịch (`Closing`), kế toán mua lại (`Purchase Price Allocation — PPA`) và Lợi thế thương mại (`Goodwill`).
  - **Buổi 2 (90 phút):** Toán học về Phát hành cổ phiếu mới, Quyền mua cổ phần (`Rights Issue`), Hoán đổi nợ thành cổ phần (`Debt-to-Equity Swap`) và kiểm định khi nào phát hành thêm làm tăng (`Accretive`) hay làm giảm (`Dilutive`) giá trị nội tại mỗi cổ phần.
  - **Buổi 3 (90 phút):** Căng thẳng thanh khoản, tái cơ cấu nợ và Thứ tự ưu tiên thanh toán (`Absolute Priority Rule`) trong thủ tục phục hồi / phá sản theo Luật `142/2025/QH15`, kèm bài tập dữ liệu bẩn và 10 bài tập định lượng.
- Bài trước liên quan: [V3 — Hành động doanh nghiệp: cổ tức, thưởng, quyền mua, tách gộp](V3-corporate-actions.md), [F2 — Định giá DDM, Thu nhập thặng dư và SOTP](F2-valuation-ddm-residual-sotp.md), [F6 — Quản trị, bên liên quan và kiểm toán](F6-governance-related-party-audit.md), [005 — Nợ, thanh khoản và khả năng sống sót](005-debt-liquidity-survival.md).
- Mô hình thực hành và hồ sơ đi kèm: [`../practice/models/capital_return.py`](../practice/models/capital_return.py), [`../practice/models/valuation.py`](../practice/models/valuation.py) và hai hồ sơ thực chiến [`../../research/companies/VN/FPT/report.md`](../../research/companies/VN/FPT/report.md), [`../../research/companies/VN/BIC/report.md`](../../research/companies/VN/BIC/report.md).
- Câu hỏi cốt lõi: Khi một doanh nghiệp công bố nghị quyết "sáp nhập công ty con", "phát hành 100 triệu cổ phiếu tăng vốn" hoặc "hoán đổi 2.000 tỷ đồng nợ thành cổ phần", làm sao để bạn không bị cuốn theo tin đồn mà tính ra chính xác từng đồng giá trị trên mỗi cổ phần thay đổi thế nào?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/F7-fact-check.md), [phản biện](../reviews/F7-risk-review.md).

---

## Hiểu bài trong một phút

Khi phân tích các sự kiện doanh nghiệp đặc biệt (`M&A`, phát hành riêng lẻ, quyền mua, hoán đổi nợ, tái cấu trúc), nhà phân tích luôn áp dụng **3 nguyên tắc cốt lõi**:
1. **Tách bạch "Nghị quyết dự kiến" với "Giao dịch đã hoàn tất (`Closed`)":** Nghị quyết HĐQT/ĐHĐCĐ mới là bước phê duyệt nội bộ. Giao dịch chỉ làm thay đổi bảng cân đối và dòng tiền khi đã thỏa mãn điều kiện tiên quyết, được cơ quan quản lý chấp thuận, đã chuyển tiền/cổ phần và ghi nhận trên BCTC sau sự kiện (`SỰ_THẬT`).
2. **Tách bạch "Pha loãng tỷ lệ sở hữu (`Ownership Dilution`)" với "Pha loãng giá trị mỗi cổ phần (`Value Dilution`)":** Nếu bạn nắm `10%` một công ty có giá trị nội tại `1.000 tỷ VND` (`100 triệu CP`, tức `10.000 VND/CP`), rồi công ty phát hành thêm `25 triệu CP` cho đối tác mới, tỷ lệ sở hữu của bạn giảm từ `10%` xuống `8%` (`10/125`). Nhưng nếu đối tác mua giá `16.000 VND/CP` bằng tiền mặt, giá trị nội tại mỗi cổ phần của bạn **tăng lên `11.200 VND/CP`** (`Accretive`); ngược lại nếu họ mua riêng lẻ giá `6.000 VND/CP`, mỗi cổ phần của bạn bị **rút xuống còn `9.200 VND/CP`** (`Dilutive`) (`PHÉP_TÍNH`)!
3. **Địa vị cuối bảng của Cổ đông phổ thông khi Phá sản:** Theo Luật Phục hồi, phá sản số `142/2025/QH15`, tiền thu hồi tài sản luôn ưu tiên trả phí phá sản, nợ lương người lao động, nợ có bảo đảm, thuế và nợ không có bảo đảm trước; **cổ đông phổ thông đứng cuối cùng (`Residual Claimant`)** (`SỰ_THẬT`).

---

## Ôn bài cũ

- Trong [Bài F6 — Quản trị, bên liên quan và kiểm toán](F6-governance-related-party-audit.md) và [Bài F2 — Định giá DDM, Thu nhập thặng dư và SOTP](F2-valuation-ddm-residual-sotp.md), ta đã nắm cấu trúc tập đoàn và định giá tổng thành phần. Bài F7 giải phẫu các thương vụ mua bán sáp nhập (`M&A`), lợi thế thương mại (`Goodwill`), thoái vốn và tái cơ cấu nợ.

---

## Buổi 1 — Vòng đời thương vụ M&A, Kế toán Hợp nhất kinh doanh và Lợi thế thương mại (Goodwill)

### 1.1. Bốn giai đoạn của một sự kiện M&A / Tái cấu trúc và Tài liệu cần kiểm

Không bao giờ định giá một thương vụ chỉ qua một bản tin tóm tắt. Hãy xác định chính xác sự kiện đang nằm ở ô nào trong 4 giai đoạn sau:

| Giai đoạn | Văn bản công bố thông tin (`CBTT`) | Tác động lên BCTC tại thời điểm đó | Rủi ro / Điểm cần kiểm tra |
|---|---|---|---|
| **1. Chủ trương / Đề xuất (`Proposal`)** | Tờ trình HĐQT / ĐHĐCĐ, Biên bản ghi nhớ (`MOU` / `Term Sheet`). | **Chưa có tác động** (trừ khi đã chuyển tiền đặt cọc thực hiện giao dịch tại mục `Phải thu khác`). | Tỷ lệ thành công còn thấp; kiểm tra xem có khoản tiền đặt cọc lớn nào đã chảy ra khỏi công ty chưa. |
| **2. Phê duyệt nội bộ & Ký kết (`Approval & Signing`)** | Nghị quyết HĐQT / ĐHĐCĐ, Hợp đồng chuyển nhượng cổ phần (`SPA`) có kèm Điều kiện tiên quyết (`Conditions Precedent — CP`). | Chưa hợp nhất hoặc chưa xóa sổ công ty con cho đến khi ngày hoàn tất (`Closing Date`) diễn ra. | Đọc kỹ: Ai là bên mua, ai là bên bán (có phải bên liên quan theo Bài [F6](F6-governance-related-party-audit.md) không?), giá chuyển nhượng và nguồn tiền lấy từ đâu? |
| **3. Hoàn tất giao dịch (`Closing`)** | Công bố thông tin hoàn tất nhận/chuyển nhượng, Giấy chứng nhận đăng ký doanh nghiệp sửa đổi, chấp thuận của Bộ Tài chính / NHNN / UBCKNN. | Bắt đầu hợp nhất (hoặc ngừng hợp nhất) từ ngày kiểm soát thực tế chuyển giao. | Kiểm tra dòng tiền thực thu/thực chi trên Báo cáo lưu chuyển tiền tệ kỳ phát sinh giao dịch. |
| **4. Hậu kiểm sau hợp nhất (`Post-Merger Integration`)** | Thuyết minh Hợp nhất kinh doanh trên BCTC bán niên / năm đã kiểm toán sau sự kiện. | Ghi nhận Tài sản thuần theo giá trị hợp lý, **Lợi thế thương mại (`Goodwill`)**, Lợi ích cổ đông không kiểm soát (`NCI`) và chi phí phân bổ `Goodwill`. | Kiểm tra xem công ty mục tiêu có tạo ra dòng tiền đúng như kế hoạch khi mua hay làm phát sinh chi phí phân bổ `Goodwill` ăn mòn lợi nhuận hợp nhất. |

### 1.2. Công thức tính Lợi thế thương mại (`Goodwill`) và Phân bổ theo chuẩn VAS 11

Theo Chuẩn mực kế toán Việt Nam số 11 (`VAS 11 — Hợp nhất kinh doanh`) và Thông tư `202/2014/TT-BTC`, khi Công ty mẹ M mua tỷ lệ sở hữu $\theta$ (với $\theta > 50\%$ quyền biểu quyết) tại Công ty con S với tổng giá phí hợp nhất kinh doanh là $P_{\text{mua}}$:

$$\text{Goodwill (Lợi thế thương mại)} = P_{\text{mua}} - \theta \times \text{FV}_{\text{Tài sản thuần có thể xác định được của S tại ngày mua}}$$

Trong đó:
$$\text{FV}_{\text{Tài sản thuần}} = \text{Giá trị hợp lý của Tổng Tài sản xác định được} - \text{Giá trị hợp lý của Nợ phải trả (kể cả thuế TNDN hoãn lại phải trả)}$$

*Hai điểm khác biệt sống còn của chuẩn mực `VAS` tại Việt Nam cần nhớ (`SỰ_THẬT`):*
1. **Phân bổ đều tối đa không quá 10 năm:** Khác với chuẩn quốc tế (`IFRS 3` / `US GAAP`) giữ nguyên `Goodwill` và kiểm tra suy giảm giá trị (`Impairment Test`) hằng năm, theo Thông tư `202/2014/TT-BTC` tại Việt Nam, khoản `Goodwill` dương phát sinh khi mua công ty con phải được **phân bổ dần đều vào Chi phí quản lý doanh nghiệp trên Báo cáo KQKD hợp nhất trong thời gian tối đa không quá 10 năm** (`10%/năm`). Nghĩa là nếu một công ty chi vượt `1.000 tỷ VND` so với tài sản thuần để mua công ty con (`Goodwill = 1.000 tỷ VND`), thì suốt 10 năm tiếp theo, mỗi năm Lợi nhuận trước thuế hợp nhất sẽ tự động bị trừ đi **`100 tỷ VND` chi phí phân bổ lợi thế thương mại** (dù đây là chi phí phi tiền mặt)!
2. **Giao dịch mua bán thêm cổ phần của công ty con đã kiểm soát từ trước:** Nếu Công ty mẹ đã sở hữu `51%` Công ty con S (đã nắm quyền kiểm soát) và sau đó mua thêm `20%` từ cổ đông thiểu số để nâng lên `71%` (hoặc bán bớt `10%` xuống `41%` mà không mất quyền kiểm soát nếu vẫn giữ đa số biểu quyết, hoặc từ `70%` xuống `55%`), theo Thông tư `202/2014/TT-BTC`, phần chênh lệch giữa giá mua/bán thêm với giá trị sổ sách tài sản thuần tương ứng **không ghi nhận vào Báo cáo KQKD và không tạo thêm `Goodwill`**, mà được ghi tăng/giảm trực tiếp vào khoản mục **Lợi nhuận sau thuế chưa phân phối** trong Vốn chủ sở hữu trên Bảng cân đối kế toán hợp nhất (`SỰ_THẬT`)!

---

## Buổi 2 — Toán học về Phát hành cổ phiếu, Pha loãng và Hoán đổi Nợ thành Vốn

### 2.1. Công thức kiểm định Tạo giá trị (`Accretive`) hay Hủy giá trị (`Dilutive`) khi phát hành thêm

Giả sử trước sự kiện, doanh nghiệp có $N_0$ cổ phiếu đang lưu hành, tổng giá trị nội tại của vốn chủ sở hữu là $V_0$, tương ứng giá trị nội tại mỗi cổ phần trước phát hành là:

$$\text{IV}_0 = \frac{V_0}{N_0}$$

Doanh nghiệp phát hành thêm $\Delta N$ cổ phiếu mới (tương ứng tỷ lệ pha loãng số lượng cổ phần là $\Delta N / (N_0 + \Delta N)$) với giá thu ròng mỗi cổ phiếu mới (sau khi đã trừ phí tư vấn, bảo lãnh phát hành) là $P_{\text{ròng}}$, thu về tổng lượng tiền mặt mới (hoặc giảm được lượng nợ vay tương ứng) là $\Delta V = \Delta N \times P_{\text{ròng}}$ (giả sử số tiền đó được đầu tư ở mức sinh lời đúng bằng chi phí vốn $r = k_e$). Khi đó, giá trị nội tại mỗi cổ phần sau phát hành ($\text{IV}_1$) là:

$$\text{IV}_1 = \frac{V_0 + \Delta N \times P_{\text{ròng}}}{N_0 + \Delta N}$$

So sánh $\text{IV}_1$ với $\text{IV}_0$, ta có định lý bất biến cho cổ đông hiện hữu không được mua thêm (như trong phát hành riêng lẻ hoặc `ESOP`):
- Nếu $P_{\text{ròng}} > \text{IV}_0 \implies \text{IV}_1 > \text{IV}_0$: Đợt phát hành **tạo thêm giá trị trên mỗi cổ phần (`Value-Accretive`)** dù tỷ lệ biểu quyết của cổ đông cũ giảm xuống!
- Nếu $P_{\text{ròng}} < \text{IV}_0 \implies \text{IV}_1 < \text{IV}_0$: Đợt phát hành **hủy hoại/pha loãng giá trị trên mỗi cổ phần (`Value-Dilutive`)** — một phần tài sản của cổ đông cũ đã bị chuyển sang cho người mua cổ phiếu phát hành riêng lẻ giá rẻ!
- Nếu phát hành cho **tất cả cổ đông hiện hữu theo tỷ lệ sở hữu (`Rights Issue` hoặc thưởng cổ phiếu từ nguồn vốn chủ sở hữu)** và cổ đông thực hiện đầy đủ quyền mua: Tỷ lệ sở hữu của cổ đông không đổi, và tổng giá trị kinh tế cổ đông nắm giữ bằng đúng giá trị cũ cộng số tiền mặt cổ đông vừa nộp thêm vào công ty (`SUY_LUẬN`).

### 2.2. Hoán đổi Nợ thành Cổ phần (`Debt-to-Equity Swap`) trong tái cấu trúc

Khi một doanh nghiệp lâm vào cảnh nợ nần chồng chất không có tiền mặt trả gốc và lãi vay, doanh nghiệp có thể đàm phán với chủ nợ (ngân hàng hoặc trái chủ) để **chuyển đổi một khoản nợ có giá trị ghi sổ $D_{\text{hoán đổi}}$ thành $\Delta N_{\text{mới}}$ cổ phiếu phổ thông** theo mức giá quy đổi $P_{\text{hoán đổi}} = D_{\text{hoán đổi}} / \Delta N_{\text{mới}}$.

Ba câu hỏi bắt buộc phải tính khi phân tích một vụ hoán đổi nợ thành cổ phần:
1. **Chủ nợ chấp nhận xóa nợ hay nhận cổ phần giá rẻ?** Nếu thị giá cổ phiếu trên sàn đang là `6.000 VND/CP` nhưng hợp đồng tái cơ cấu hoán đổi nợ theo mệnh giá `10.000 VND/CP`, tức cứ `10.000 VND` nợ gốc đổi lấy `1 cổ phiếu` trị giá thị trường `6.000 VND`, thì thực chất chủ nợ đã chấp nhận chịu thiệt giá thị trường (`Haircut` kinh tế `40%`), còn bảng cân đối kế toán của doanh nghiệp giảm được `10.000 VND` nợ vay và tăng `10.000 VND` vốn chủ sở hữu trên mỗi cổ phiếu mới phát hành! Ngược lại, nếu hoán đổi ở giá thấp hơn giá trị thực của cổ phần, cổ đông hiện hữu sẽ bị pha loãng nặng nề (`SUY_LUẬN`).
2. **Chi phí lãi vay tiết kiệm được mỗi năm là bao nhiêu?** Khoản nợ $D_{\text{hoán đổi}}$ với lãi suất $i_d$ được xóa bỏ sẽ giúp doanh nghiệp tiết kiệm được $\Delta \text{Lãi vay} = D_{\text{hoán đổi}} \times i_d$ mỗi năm trên Báo cáo KQKD và Báo cáo lưu chuyển tiền tệ.
3. **Áp lực bán cổ phiếu sau thời gian hạn chế chuyển nhượng (`Overhang Risk`):** Chủ nợ (như ngân hàng hoặc nhà thầu xây dựng) bản chất không muốn làm cổ đông dài hạn; ngay khi hết thời hạn hạn chế chuyển nhượng (thường là 1 năm), lượng cổ phiếu $\Delta N_{\text{mới}}$ khổng lồ này có thể bị bán ra thị trường để thu hồi tiền mặt (`SUY_LUẬN`).

---

## Buổi 3 — Căng thẳng Thanh khoản và Thủ tục Phục hồi – Phá sản (Luật 142/2025/QH15)

### 3.1. Bốn trạng thái tài chính – pháp lý và Thứ tự ưu tiên thanh toán

Không gọi mọi doanh nghiệp thua lỗ hoặc chậm trả một kỳ lãi trái phiếu là "đã phá sản". Có 4 trạng thái khác nhau: (1) Thua lỗ kế toán nhưng dòng tiền dương; (2) Cơ cấu lại nợ tự nguyện ngoài tòa án (`Out-of-Court Workout` — gia hạn trái phiếu, hoán đổi tài sản); (3) Thủ tục Phục hồi hoạt động kinh doanh dưới sự giám sát của Tòa án, Quản tài viên và Hội nghị chủ nợ; và (4) Thủ tục tuyên bố Phá sản và Thanh lý tài sản.

`SỰ_THẬT`: [Luật Phục hồi, phá sản số 142/2025/QH15 trên Công báo Chính phủ](https://congbao.chinhphu.vn/van-ban/luat-so-142-2025-qh15-468702.htm) (hiệu lực từ `01/03/2026`) ưu tiên thủ tục phục hồi trước và quy định trình tự xử lý tài sản bảo đảm, phân chia tài sản khi thanh lý. Về mặt kinh tế tài chính (`Priority Waterfall`), thứ tự ưu tiên thanh toán khi thanh lý đi từ trên xuống dưới:
1. **Nhóm ưu tiên số 1:** Chi phí phục hồi/phá sản, nợ lương, trợ cấp thôi việc, bảo hiểm xã hội của người lao động và khoản nợ phát sinh nhằm phục hồi kinh doanh.
2. **Chủ nợ có bảo đảm (`Secured Creditors`):** Thanh toán bằng tài sản bảo đảm hợp lệ; nếu tài sản bảo đảm không đủ trả hết gốc/lãi, phần thiếu hụt chuyển xuống xếp chung với nợ không có bảo đảm (`SUY_LUẬN`).
3. **Nghĩa vụ thuế với Nhà nước và Chủ nợ không có bảo đảm (`Unsecured Creditors`):** Chia theo tỷ lệ (`Pro-rata`) trên phần tài sản còn lại.
4. **Cổ đông (`Equity Holders` — Cổ phần ưu đãi rồi đến Cổ phần phổ thông):** Chỉ nhận phần dư **sau khi tất cả chủ nợ ở 3 bậc trên đã nhận đủ `100%`**. Trong hầu hết các vụ thanh lý phá sản, khi tài sản phát mãi không đủ trả chủ nợ không có bảo đảm, giá trị thu hồi của cổ phần phổ thông bằng **`0 VND`** (`SUY_LUẬN`)!

---

## 4. Ví dụ từ nguồn thật: Thông báo sáp nhập công ty con Vingroup (11/2025) và Tăng vốn / M&A tại BIC (FY2025)

1. **Thông báo tái cấu trúc nội bộ của Tập đoàn Vingroup (`VIC` — Tháng 11/2025):**
   - `SỰ_THẬT`: [Vingroup — CBTT về việc sáp nhập công ty con ngày 06/11/2025](https://ircdn.vingroup.net/storage/Uploads/0_Quan%20he%20co%20dong/0_Vingroup_2025/T11/20251106%20-%20VIC%20-%20CBTT%20ve%20viec%20sap%20nhap%20cong%20ty%20con_E.pdf) công bố nghị quyết HĐQT về việc sáp nhập `VinApp` vào `VinSmart Future`.
   - `SUY_LUẬN`: Nghị quyết thể hiện quyết định tinh gọn pháp nhân nội bộ, không tự chứng minh giao dịch đã hoàn tất đăng ký kinh doanh hay tạo dòng tiền mới từ bên ngoài. Vì cả hai đều là công ty con hợp nhất, việc sáp nhập chủ yếu làm thay đổi tỷ lệ lợi ích giữa công ty mẹ và cổ đông không kiểm soát (`NCI`); cần kiểm tra Thuyết minh Danh sách công ty con trên BCTC hợp nhất kiểm toán.

2. **Mua công ty con (`M&A`) và Phát hành cổ phiếu tăng vốn `+72,30%` tại Bảo hiểm BIDV (`BIC` — FY2025):**
   - `SỰ_THẬT`: Theo BCTC hợp nhất kiểm toán năm 2025 của `BIC` ([`../../research/companies/VN/BIC/report.md`](../../research/companies/VN/BIC/report.md)):
     - **Phát hành cổ phiếu từ nguồn vốn chủ sở hữu (Thuyết minh 23, tr. 50 PDF):** `BIC` phát hành thêm **`84.790.162` cổ phiếu** trả cổ tức từ lợi nhuận sau thuế chưa phân phối, nâng tổng số cổ phiếu từ `117.276.895 CP` lên **`202.067.057 CP`** (vốn điều lệ tăng **`+72,30%`** từ `1.172,77 tỷ VND` lên `2.020,67 tỷ VND`). Vì phát hành theo tỷ lệ cho mọi cổ đông hiện hữu, tỷ lệ sở hữu của `BIDV` giữ nguyên **`51,00%`** và kết chuyển `847,90 tỷ VND` từ Lợi nhuận chưa phân phối sang Vốn góp chủ sở hữu (`SỰ_THẬT` & `PHÉP_TÍNH`).
     - **Mua `51%` công ty bảo hiểm tại Campuchia (`CVI`, Thuyết minh 1 & 4.1):** Ngày `01/07/2025`, `BIC` chi **`106,99 tỷ VND`** mua `51%` quyền biểu quyết tại `CVI`, hợp nhất `CVI` vào BCTC và ghi nhận Lợi ích cổ đông không kiểm soát (`NCI`) tăng từ `17,43 tỷ VND` lên **`133,04 tỷ VND`** cuối năm 2025 (`SỰ_THẬT`).

---

## 5. Bài làm với dữ liệu thiếu hoặc lệch (Dirty-Data Exercise)

### Tình huống dữ liệu bẩn
Công ty Q giao dịch ở giá `12.000 VND/CP` (`100 triệu CP`, vốn hóa `1.200 tỷ VND`), nhưng Giá trị sổ sách thuần đã kiểm toán (`NAV` thực) là **`20.000 VND/CP`** (`Vốn chủ sở hữu = 2.000 tỷ VND`). Công ty công bố:
> *"ĐHĐCĐ thông qua: (1) Phát hành riêng lẻ 100 triệu CP mới giá 10.000 VND/CP thu về 1.000 tỷ VND; và (2) Dùng ngay 1.000 tỷ VND đó mua 100% vốn Công ty S (có giá trị tài sản thuần hợp lý là 350 tỷ VND)."*

Hồ sơ chi tiết cho thấy bên mua phát hành riêng lẻ và bên bán Công ty S có liên hệ với nhóm cổ đông nội bộ (`KỊCH_BẢN`). Hãy định lượng mức thiệt hại trên mỗi cổ phần của cổ đông hiện hữu!

### Quy trình định lượng hủy giá trị kép (`Double Value Destruction`)
1. **Bước 1 — Hủy giá trị do phát hành riêng lẻ dưới `IV_0` (`Dilutive Private Placement`):**
   - Trước phát hành: $N_0 = 100\text{ triệu CP}$, $V_0 = 2.000\text{ tỷ VND} \implies \text{IV}_0 = 20.000\text{ VND/CP}$.
   - Phát hành riêng lẻ $\Delta N = 100\text{ triệu CP}$ giá $P = 10.000\text{ VND/CP}$ thu về `+1.000 tỷ VND` tiền mặt. Ngay sau Bước 1, tổng tài sản thuần là $2.000 + 1.000 = 3.000\text{ tỷ VND}$ trên `200 triệu CP`:
     $$\text{IV}_{\text{sau Bước 1}} = \frac{3.000\text{ tỷ VND}}{200\text{ triệu CP}} = 15.000\text{ VND/CP}\quad (\text{mất ngay }-5.000\text{ VND/CP hay }-25\%!)\quad (\text{PHÉP\_TÍNH})$$
2. **Bước 2 — Hủy giá trị lần hai do mua tài sản giá đắt (`Overpriced M&A`):**
   - Chi `1.000 tỷ VND` tiền mặt mua Công ty S chỉ có tài sản thuần hợp lý `350 tỷ VND`, trả đắt hơn thực tế $1.000 - 350 = 650\text{ tỷ VND}$ (biến thành `Goodwill` vô hình phải phân bổ chi phí `65 tỷ VND/năm` suốt 10 năm).
   - Tính theo tài sản thuần hữu hình (`Tangible Book Value`), sau Bước 2 tổng tài sản thuần hữu hình của Công ty Q chỉ còn $3.000 - 1.000 + 350 = 2.350\text{ tỷ VND}$ trên `200 triệu CP`:
     $$\text{IV}_{\text{hữu hình sau Bước 2}} = \frac{2.350\text{ tỷ VND}}{200\text{ triệu CP}} = 11.750\text{ VND/CP}\quad (\text{bốc hơi }-41,25\%\text{ từ }20.000\text{ VND/CP!})\quad (\text{PHÉP\_TÍNH})$$

---

## 6. Sai ở đâu? (Bắt lỗi suy luận)

Hãy chỉ ra chỗ sai khi bắt đáy cổ phiếu đang thanh lý phá sản:

> *"Công ty X đang làm thủ tục phá sản thanh lý tài sản. Trên BCTC gần nhất, Tổng tài sản ghi sổ là 5.000 tỷ VND, Tổng nợ phải trả là 4.200 tỷ VND, tức Vốn chủ sở hữu còn +800 tỷ VND (8.000 VND/CP trên 100 triệu CP). Giá cổ phiếu trên sàn chỉ 1.500 VND/CP — mua vào chờ tòa án bán tài sản trả nợ xong kiểu gì cổ đông cũng được chia 8.000 VND/CP!"*

### Phân tích chỗ sai
1. **Nhầm "Giá trị ghi sổ lúc hoạt động liên tục" với "Giá trị thanh lý cưỡng bức":** Khi thanh lý phá sản, chi phí trả trước/lợi thế thương mại bằng `0`, còn tài sản vật chất bán đấu giá cưỡng bức thường chỉ thu hồi được `40%–65%` giá trị ghi sổ. Giả sử `5.000 tỷ VND` tài sản bán đấu giá chỉ thu về `60%` = **`3.000 tỷ VND`** (`PHÉP_TÍNH`).
2. **Quy tắc ưu tiên tuyệt đối (`Absolute Priority Rule`):** Nợ phải trả `4.200 tỷ VND` cộng thêm chi phí phá sản, nợ lương và lãi phạt tăng lên `4.400 tỷ VND`. Với `3.000 tỷ VND` tiền thu đối mặt với `4.400 tỷ VND` nợ ưu tiên đứng trước, ngay cả chủ nợ không có bảo đảm cũng mất `1.400 tỷ VND`, còn phần tiền cho cổ đông phổ thông đứng cuối cùng bằng đúng **`0 VND/CP`** (`PHÉP_TÍNH`)!

---

## 7. Bài tập (10 câu)

1. Nêu 4 giai đoạn của một sự kiện `M&A` / tái cấu trúc doanh nghiệp và giải thích vì sao một Nghị quyết HĐQT thông qua chủ trương mua/sáp nhập chưa tự động làm thay đổi báo cáo tài chính hợp nhất.
2. Ngày `01/01/2026`, Công ty mẹ M chi `600 tỷ VND` tiền mặt để mua `80%` cổ phần có quyền biểu quyết của Công ty S. Tại ngày mua, Tổng tài sản có thể xác định được của Công ty S theo giá trị hợp lý là `900 tỷ VND` và Tổng nợ phải trả theo giá trị hợp lý là `400 tỷ VND`. Hãy tính: (a) Giá trị hợp lý tài sản thuần của Công ty S tại ngày mua; (b) Phần tài sản thuần thuộc về Công ty mẹ M (`80%`) và phần thuộc về Cổ đông không kiểm soát (`NCI = 20%`); (c) Giá trị Lợi thế thương mại (`Goodwill`) phát sinh từ thương vụ; và (d) Chi phí phân bổ `Goodwill` hằng năm trên Báo cáo KQKD hợp nhất nếu phân bổ đều trong 10 năm theo chuẩn `VAS`.
3. Trước khi phát hành thêm, Công ty A có `100 triệu` cổ phiếu lưu hành, cổ đông An nắm giữ `10 triệu` cổ phiếu. Giá trị nội tại hợp lý của vốn chủ sở hữu trước phát hành là `2.500 tỷ VND` (`25.000 VND/cổ phiếu`). Công ty phát hành riêng lẻ thêm `25 triệu` cổ phiếu mới cho một quỹ đầu tư (cổ đông An không được mua). Tính tỷ lệ sở hữu của cổ đông An sau phát hành và giá trị nội tại mỗi cổ phần sau phát hành ($\text{IV}_1$) trong hai trường hợp: (a) Quỹ đầu tư mua với giá thu ròng `32.000 VND/CP`; và (b) Quỹ đầu tư mua với giá thu ròng `15.000 VND/CP`.
4. Theo dữ liệu kiểm toán năm 2025 của Bảo hiểm BIDV (`BIC`) trong Mục 4.2: Trước đợt phát hành trả cổ tức từ nguồn vốn chủ sở hữu, `BIC` có `117.276.895` cổ phiếu; sau khi phát hành thêm `84.790.162` cổ phiếu cho cổ đông hiện hữu, tổng số cổ phiếu là `202.067.057` cổ phiếu. Biết tổng Vốn chủ sở hữu thuộc về cổ đông công ty mẹ cuối năm 2025 là `3.250,058 tỷ VND`. Hãy tính: (a) Tỷ lệ phát hành thêm cổ phiếu (`%`); (b) Giá trị sổ sách mỗi cổ phần (`BVPS`) cuối năm 2025 tính trên số lượng cổ phiếu mới; và (c) Giải thích vì sao đợt phát hành này không làm thay đổi tổng Vốn chủ sở hữu của `BIC`.
5. Một doanh nghiệp đang có `60 triệu` cổ phiếu lưu hành, Vốn chủ sở hữu `300 tỷ VND` (`BVPS = 5.000 VND/CP`) và đang gánh một khoản nợ vay quá hạn `400 tỷ VND` với lãi suất `11%/năm`. Trong phương án tái cấu trúc, chủ nợ đồng ý hoán đổi toàn bộ `400 tỷ VND` nợ gốc này thành cổ phiếu mới theo mức giá hoán đổi `10.000 VND/cổ phiếu`. Hãy tính: (a) Số lượng cổ phiếu mới phát hành cho chủ nợ; (b) Tỷ lệ sở hữu của chủ nợ và của nhóm cổ đông cũ sau hoán đổi; (c) Tổng Vốn chủ sở hữu và `BVPS` kế toán mới sau hoán đổi; và (d) Số tiền chi phí lãi vay trước thuế mà doanh nghiệp tiết kiệm được mỗi năm.
6. Công ty mẹ P đang sở hữu `60%` Công ty con K (đã hợp nhất báo cáo tài chính từ 3 năm trước). Năm nay, Công ty mẹ P chi `180 tỷ VND` mua thêm `15%` cổ phần của Công ty K từ các cổ đông thiểu số để nâng tỷ lệ sở hữu lên `75%`. Biết tại ngày mua thêm, giá trị sổ sách tài sản thuần của Công ty K là `1.000 tỷ VND`. Theo quy định hợp nhất báo cáo tài chính của Việt Nam (`Thông tư 202/2014/TT-BTC`), thương vụ mua thêm `15%` này có làm phát sinh thêm Lợi thế thương mại (`Goodwill`) mới không, và khoản chênh lệch giữa giá mua (`180 tỷ`) với phần tài sản thuần mua thêm ($15\% \times 1.000 = 150\text{ tỷ}$) được hạch toán vào đâu?
7. Một doanh nghiệp bất động sản mất khả năng thanh toán bị mở thủ tục thanh lý phá sản. Tổng giá trị tiền mặt thu được từ việc bán đấu giá toàn bộ tài sản của doanh nghiệp (sau khi đã trừ chi phí phá sản và trả hết nợ lương người lao động) là `1.800 tỷ VND`. Doanh nghiệp có 3 nhóm nghĩa vụ còn lại: (1) Nợ vay ngân hàng có tài sản bảo đảm hợp lệ `1.100 tỷ VND` (tài sản thế chấp của khoản vay này bán đấu giá thu được `1.100 tỷ VND` nằm trong tổng `1.800 tỷ VND`); (2) Thuế và các khoản nợ trái phiếu, nợ nhà thầu không có tài sản bảo đảm tổng cộng `1.400 tỷ VND`; và (3) Vốn góp của cổ đông phổ thông `1.000 tỷ VND`. Tính số tiền thu hồi và tỷ lệ thu hồi (`Recovery Rate`, `%`) của từng nhóm!
8. Giải thích sự khác nhau giữa **Chào bán cổ phiếu cho cổ đông hiện hữu theo tỷ lệ (`Rights Issue`)** với **Phát hành cổ phiếu riêng lẻ (`Private Placement`)** về quyền bảo vệ cổ đông thiểu số khỏi bị pha loãng tỷ lệ sở hữu và giá trị.
9. Khi một doanh nghiệp công bố nghị quyết *"Hội đồng Quản trị thông qua hạn mức vay tối đa 3.000 tỷ VND hoặc phát hành tối đa 50 triệu cổ phiếu"*, vì sao bạn không được lấy ngay con số `3.000 tỷ VND` hay `50 triệu cổ phiếu` cộng vào mô hình định giá?
10. Sử dụng mô-đun [`../practice/models/capital_return.py`](../practice/models/capital_return.py), giải thích vì sao việc một doanh nghiệp mua lại cổ phiếu quỹ (`Share Buyback`) khi thị giá $P < \text{IV}_0$ là nghiệp vụ ngược dấu hoàn toàn (làm tăng $\text{IV}_1$ cho cổ đông còn lại) so với việc phát hành riêng lẻ khi $P < \text{IV}_0$.

---

## 8. Đáp án chi tiết

1. **Bốn giai đoạn sự kiện và lý do Nghị quyết chưa làm đổi BCTC:**
   - Bốn giai đoạn: (1) Đề xuất / Chủ trương; (2) Phê duyệt nội bộ & Ký hợp đồng có điều kiện tiên quyết; (3) Hoàn tất giao dịch (`Closing`); (4) Hậu kiểm hợp nhất sau giao dịch. Nghị quyết HĐQT mới ở bước phê duyệt nội bộ; chừng nào chưa hoàn tất chuyển giao quyền kiểm soát thực tế và thanh toán thì chuẩn mực kế toán chưa cho phép hợp nhất (hoặc ngừng hợp nhất) trên BCTC (`SỰ_THẬT`).
2. **Kế toán mua `80%` Công ty S và tính `Goodwill` (`VAS 11`):**
   - (a) Giá trị hợp lý tài sản thuần của Công ty S = $900 - 400 = 500\text{ tỷ VND}$.
   - (b) Phần tài sản thuần thuộc Công ty mẹ M (`80%`) = $80\% \times 500 = 400\text{ tỷ VND}$; Phần thuộc Cổ đông không kiểm soát (`NCI = 20%`) = $20\% \times 500 = 100\text{ tỷ VND}$.
   - (c) Lợi thế thương mại (`Goodwill`) = $600 - 400 = 200\text{ tỷ VND}$.
   - (d) Chi phí phân bổ `Goodwill` mỗi năm (trong 10 năm) = $200 / 10 = 20\text{ tỷ VND/năm}$ ghi vào Chi phí quản lý doanh nghiệp hợp nhất (`PHÉP_TÍNH`).
3. **Kiểm định `Accretive` vs. `Dilutive` khi phát hành riêng lẻ `25 triệu CP`:**
   - Tỷ lệ sở hữu của cổ đông An giảm từ $10 / 100 = 10,0\%$ xuống $10 / (100 + 25) = 8,0\%$.
   - (a) Khi phát hành giá ròng $P_{\text{ròng}} = 32.000\text{ VND/CP} > \text{IV}_0 = 25.000\text{ VND/CP}$ (thu về `800 tỷ VND`):
     $$\text{IV}_1 = \frac{2.500 + 800}{125\text{ triệu CP}} = \frac{3.300}{125} = 26.400\text{ VND/CP}\quad (\text{Accretive: tăng }+1.400\text{ VND/CP!})$$
   - (b) Khi phát hành giá ròng $P_{\text{ròng}} = 15.000\text{ VND/CP} < \text{IV}_0 = 25.000\text{ VND/CP}$ (thu về `375 tỷ VND`):
     $$\text{IV}_1 = \frac{2.500 + 375}{125\text{ triệu CP}} = \frac{2.875}{125} = 23.000\text{ VND/CP}\quad (\text{Dilutive: mất }-2.000\text{ VND/CP!})\quad (\text{PHÉP\_TÍNH})$$
4. **Phân tích đợt phát hành tăng vốn `+72,30%` năm 2025 của `BIC`:**
   - (a) Tỷ lệ phát hành thêm = $84.790.162 / 117.276.895 = 72,30\%$.
   - (b) `BVPS` công ty mẹ cuối năm 2025 = $\frac{3.250,058\text{ tỷ VND}}{202,067057\text{ triệu CP}} = 16.084,05\text{ VND/CP}$.
   - (c) Tổng Vốn chủ sở hữu không đổi vì đây là bút toán kết chuyển nội bộ trong Vốn chủ sở hữu (giảm Lợi nhuận sau thuế chưa phân phối `847,90 tỷ VND` và tăng Vốn góp của chủ sở hữu thêm `847,90 tỷ VND`) (`PHÉP_TÍNH` & `SỰ_THẬT`).
5. **Hoán đổi `400 tỷ VND` nợ thành cổ phần ở giá `10.000 VND/CP`:**
   - (a) Số cổ phiếu mới phát hành cho chủ nợ = $400\text{ tỷ VND} / 10.000\text{ VND/CP} = 40\text{ triệu CP}$ (tổng số cổ phiếu sau hoán đổi = $60 + 40 = 100\text{ triệu CP}$).
   - (b) Tỷ lệ sở hữu sau hoán đổi: Chủ nợ nắm $40 / 100 = 40,0\%$; nhóm cổ đông cũ giảm từ `100%` xuống $60 / 100 = 60,0\%$.
   - (c) Tổng Vốn chủ sở hữu kế toán sau hoán đổi = $300 + 400 = 700\text{ tỷ VND} \implies \text{BVPS}_{\text{mới}} = 700\text{ tỷ} / 100\text{ triệu CP} = 7.000\text{ VND/CP}$ (tăng từ `5.000 VND/CP` lên `7.000 VND/CP` vì chủ nợ nhận quy đổi ở giá `10.000 VND/CP` cao hơn `BVPS` cũ!).
   - (d) Chi phí lãi vay trước thuế tiết kiệm được mỗi năm = $400 \times 11\% = 44\text{ tỷ VND/năm}$ (`PHÉP_TÍNH`).
6. **Mua thêm `15%` cổ phần của công ty con đã kiểm soát (`60% -> 75%`):**
   - Theo Thông tư `202/2014/TT-BTC`, vì Công ty mẹ P đã nắm quyền kiểm soát Công ty K từ trước (`60% > 50%`), việc mua thêm `15%` từ cổ đông không kiểm soát (`NCI`) là giao dịch giữa các chủ sở hữu với nhau, nên **không ghi nhận thêm `Goodwill` mới**. Khoản chênh lệch $180 - 150 = 30\text{ tỷ VND}$ được ghi **giảm trực tiếp vào Lợi nhuận sau thuế chưa phân phối** trên Bảng cân đối kế toán hợp nhất (`SỰ_THẬT` & `PHÉP_TÍNH`).
7. **Tính tỷ lệ thu hồi (`Recovery Rate`) khi thanh lý phá sản:**
   - (1) Chủ nợ có bảo đảm (`1.100 tỷ VND`): Thu hồi đủ **`1.100 tỷ VND`** từ tài sản thế chấp (`Recovery Rate = 100%`).
   - Phần tiền mặt còn lại cho các bậc dưới = $1.800 - 1.100 = 700\text{ tỷ VND}$.
   - (2) Thuế và Chủ nợ không có bảo đảm (`1.400 tỷ VND`): Được chia theo tỷ lệ từ `700 tỷ VND` còn lại, tức thu hồi **`700 tỷ VND`**, tương ứng `Recovery Rate` = $700 / 1.400 = 50,0\%$.
   - (3) Cổ đông phổ thông (`1.000 tỷ VND`): Vì bậc chủ nợ không có bảo đảm mới chỉ thu hồi được `50%` (thiếu `700 tỷ VND`), phần còn lại cho cổ đông phổ thông bằng **`0 tỷ VND`** (`Recovery Rate = 0%`) (`PHÉP_TÍNH`).
8. **Sự khác nhau giữa `Rights Issue` và `Private Placement`:**
   - Trong `Rights Issue`, mọi cổ đông hiện hữu đều được phân bổ quyền mua theo đúng tỷ lệ sở hữu (hoặc có thể bán quyền mua nếu giá chào bán thấp hơn thị giá), nên không bị tước đoạt tỷ lệ biểu quyết ngoài ý muốn. Trong `Private Placement`, cổ đông nhỏ lẻ không được quyền tham gia mua, nên nếu phát hành riêng lẻ ở mức giá $P_{\text{ròng}} < \text{IV}_0$, cổ đông nhỏ lẻ bị thiệt hại kép cả về quyền biểu quyết lẫn giá trị nội tại mỗi cổ phần (`SUY_LUẬN`).
9. **Hạn mức được duyệt khác với số thực hiện:**
   - Hạn mức tối đa chỉ là trần được phép trong một khoảng thời gian; doanh nghiệp có thể chỉ giải ngân một phần, hoãn hoặc hủy phương án nếu điều kiện thị trường không thuận lợi. Phải kiểm tra báo cáo kết quả đợt phát hành / số dư nợ thực tế trên BCTC (`SUY_LUẬN`).
10. **Đối xứng giữa Mua cổ phiếu quỹ (`Buyback`) và Phát hành riêng lẻ (`Private Placement`) khi $P < \text{IV}_0$:**
    - Khi thị giá $P < \text{IV}_0$: Nếu công ty **mua lại cổ phiếu quỹ** ở giá rẻ $P$, mỗi cổ phần mua lại giúp phần giá trị chiết khấu $(\text{IV}_0 - P)$ ở lại làm tăng $\text{IV}_1$ cho các cổ đông trung thành còn lại; ngược lại, nếu công ty **phát hành thêm cổ phiếu mới** cho người ngoài ở giá rẻ $P < \text{IV}_0$, các cổ đông hiện hữu bị mất phần $(\text{IV}_0 - P)$ sang cho người mới (`SUY_LUẬN`).

---

## 9. Kiểm tra chuyển bài (Transfer Check)

Bạn đã hoàn thành toàn bộ cụm bài học phân tích chuyên sâu doanh nghiệp và tình huống đặc biệt tại Việt Nam (`F3` đến `F8`). Trước khi bước sang Cụm Tài sản & Danh mục (`A1` đến `A4`), hãy tự kiểm tra 3 kỹ năng tổng hợp sau:
1. **Liên thông 6 bài `F3–F8`:** Khi đứng trước bất kỳ mã cổ phiếu nào trên sàn `HOSE` / `HNX`, bạn đã biết cách phân loại ngay doanh nghiệp đó thuộc mô hình kinh doanh nào (Bất động sản `F3`, Ngân hàng `F4`, Sản xuất/Chu kỳ/Bán lẻ/Chứng khoán `F5`, hay Bảo hiểm `F8`), rồi áp dụng bộ lọc Quản trị – Bên liên quan – Kiểm toán (`F6`) và kiểm tra các sự kiện Pha loãng / `M&A` (`F7`) chưa?
2. **Phản xạ với tin tức tăng vốn và `M&A`:** Khi đọc tin một công ty chuẩn bị phát hành riêng lẻ hoặc mua lại công ty con, bạn đã có phản xạ đặt bút tính ngay $\text{IV}_1$ so với $\text{IV}_0$ và kiểm tra lượng `Goodwill` phát sinh thay vì giao dịch theo tin đồn chưa?
3. **Hiểu vị trí của Cổ phần phổ thông trong cấu trúc vốn:** Bạn đã thấy rõ sự khác biệt về độ ưu tiên dòng tiền và rủi ro mất vốn giữa Tiền gửi / Trái phiếu (sẽ học sâu ở Bài [A1](A1-deposits-government-corporate-bonds.md)) với Cổ phần phổ thông trong kịch bản doanh nghiệp gặp khủng hoảng thanh khoản chưa?

---

## 10. Lỗi thường gặp và ranh giới an toàn

- **Bốn lỗi phân tích phổ biến:** (1) Coi thông báo chủ trương `M&A` là giao dịch đã hoàn tất; (2) Chỉ nhìn tốc độ tăng quy mô tổng tài sản/vốn điều lệ sau phát hành mà quên tính giá trị nội tại trên **mỗi cổ phần** (`IV per share`) bị pha loãng; (3) Quên trừ chi phí phân bổ Lợi thế thương mại (`Goodwill` tối đa 10 năm theo `VAS`) và quên kiểm tra xem bên bán công ty mục tiêu có phải là bên liên quan không; (4) Lấy giá trị sổ sách kế toán để bắt đáy cổ phiếu đang làm thủ tục phá sản mà bỏ qua chiết khấu thanh lý cưỡng bức và thứ tự ưu tiên chủ nợ.
- **Ranh giới an toàn:** Bài học cung cấp khung phân tích tài chính cho các sự kiện doanh nghiệp; không đưa ra tư vấn pháp lý về thủ tục phục hồi, phá sản hay khuyến nghị mua/bán bất kỳ mã chứng khoán nào.

## Nguồn Internet đã mở

- Chốt kiểm tra trực tuyến lúc `2026-11-05 12:05 UTC+7`:
  1. [Tập đoàn Vingroup — Công bố thông tin về việc sáp nhập công ty con](https://ircdn.vingroup.net/storage/Uploads/0_Quan%20he%20co%20dong/0_Vingroup_2025/T11/20251106%20-%20VIC%20-%20CBTT%20ve%20viec%20sap%20nhap%20cong%20ty%20con_E.pdf), ngày `06/11/2025`.
  2. [Công báo Chính phủ — Luật Phục hồi, phá sản số 142/2025/QH15](https://congbao.chinhphu.vn/van-ban/luat-so-142-2025-qh15-468702.htm), hiệu lực từ ngày `01/03/2026`.
  3. [Hồ sơ nghiên cứu đã kiểm duyệt — Tổng Công ty Bảo hiểm BIDV (BIC)](../../research/companies/VN/BIC/report.md) (Thuyết minh 1, 4.1 và 23 BCTC hợp nhất kiểm toán năm 2025 về mua công ty con `CVI` và phát hành cổ phiếu tăng vốn điều lệ `+72,30%`).
