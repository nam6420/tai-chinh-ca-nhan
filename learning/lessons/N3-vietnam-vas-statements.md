# Bài N3: Đọc báo cáo tài chính Việt Nam theo VAS

- Ngày: `2026-11-06`
- Chốt dữ liệu lúc: `2026-11-06 10:25 UTC+7 (Asia/Ho_Chi_Minh)`
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Mục tiêu:
  - **Phần A (15–20 phút, học ở Bước 6/23 của Nhánh 1):** Mở báo cáo tài chính Việt Nam từ nguồn gốc, phân biệt báo cáo riêng với hợp nhất, nhận diện bốn biểu mẫu (`B 01-DN`, `B 02-DN`, `B 03-DN`, `B 09-DN`), hiểu khái niệm **Mã số** và tìm đúng 12 dòng cơ bản đã học ở [Bài 001](001-business-financial-statements.md) và [Bài N2](N2-statement-line-items.md).
  - **Phần B (40–50 phút, quay lại học ở Bước 16/23 sau [Bài 009](009-valuation-multiples.md)):** Phân biệt chế độ kế toán năm 2025 (`Thông tư 200/202`) và năm 2026 (`Thông tư 99/43`); tránh bẫy **mã số đổi** và **phân loại lại số đầu năm**; tự dựng `EBIT` từ `B 02-DN`; xử lý 5 khác biệt lớn giữa `VAS` và `IFRS` khi áp dụng [Bài 004](004-cash-flow-and-earnings-quality.md)–[Bài 009](009-valuation-multiples.md).
- Thời lượng: Hai chặng tách biệt (**Phần A** cho người mới; **Phần B** sau khi học xong bội số định giá) + thực hành kiểm chứng Vinamilk (`VNM`) trên [earnings_quality.py](../practice/models/earnings_quality.py).
- Bài trước liên quan:
  - **Khi đọc Phần A (Bước 6/23 Nhánh 1):** Học ngay sau [Bài N8: Tìm và kiểm nguồn doanh nghiệp](N8-finding-verifying-sources.md) (kế thừa [Bài 001](001-business-financial-statements.md) và [Bài N2](N2-statement-line-items.md)). Học xong Phần A → chuyển sang [Bài 002: Hiểu và tìm một cổ phiếu đang được định giá rẻ](002-finding-a-cheap-stock.md).
  - **Khi đọc Phần B (Bước 16/23 Nhánh 1):** Quay lại học sau [Bài 009: Định giá bằng bội số](009-valuation-multiples.md) (cùng chuỗi [Bài 003](003-business-quality-moat-and-roic.md)–[Bài 008](008-macro-transmission.md)). Học xong Phần B → chuyển sang [Bài N7: Dữ liệu, xác suất và bất định](N7-data-probability-uncertainty.md).
- Câu hỏi cốt lõi: **Chỉ tiêu mà khóa học dạy bằng thuật ngữ quốc tế nằm ở biểu mẫu nào, dòng nào, mã số nào trên báo cáo tài chính Việt Nam — và chỗ nào hai bên không khớp nhau?**

> Đây là bài học nền tảng, không phải khuyến nghị mua, bán hay nắm giữ chứng khoán. Ví dụ Vinamilk (`VNM`) dùng số từ báo cáo tài chính hợp nhất đã kiểm toán/soát xét do doanh nghiệp công bố để học cách đọc mẫu biểu.

## Hiểu bài này trong 1 phút

Ở [Bài 001](001-business-financial-statements.md) và [Bài N2](N2-statement-line-items.md), bạn đã làm quen với ba báo cáo tài chính qua **Quán cà phê Sao Biển** và ví dụ Apple (`US GAAP`) cùng thuật ngữ quốc tế (`IFRS`). Khi áp dụng [Bài N8](N8-finding-verifying-sources.md) để mở báo cáo của doanh nghiệp niêm yết Việt Nam (như Vinamilk, Hòa Phát, FPT), bạn sẽ thấy báo cáo Việt Nam được lập theo **Chuẩn mực kế toán Việt Nam (`VAS`)** và **Chế độ kế toán** do Bộ Tài chính ban hành: mẫu biểu cố định và mỗi dòng có một **Mã số** (như Mã `10` là Doanh thu thuần, Mã `110` là Tiền).

Mã số là "tọa độ" giúp tìm nhanh chỉ tiêu — cho tới khi Bộ Tài chính đổi biểu mẫu! Từ năm tài chính **2026**, chế độ kế toán mới (**Thông tư 99/2025/TT-BTC** cho báo cáo riêng và **Thông tư 43/2026/TT-BTC** cho báo cáo hợp nhất) thay thế chế độ cũ (**Thông tư 200/2014** và **Thông tư 202/2014**), làm nhiều mã số dịch chuyển.

> Câu cần nhớ: **Đọc theo tên chỉ tiêu, dùng mã số để định vị, và luôn nhìn dòng "Ban hành theo Thông tư số…" ở góc phải biểu mẫu trước khi tin một mã số.**

---

## Ôn bài cũ hoặc kiểm tra đầu vào

Hãy kiểm tra nhanh bạn đang ở chặng nào của Nhánh 1:

- **Nếu bạn vừa học xong [Bài N8](N8-finding-verifying-sources.md) (Bước 6/23 — Đọc Phần A):** Bạn đã biết phương trình `Tài sản = Nợ phải trả + Vốn chủ sở hữu` ([Bài 001](001-business-financial-statements.md), [Bài N2](N2-statement-line-items.md)) và cách tải báo cáo gốc ([Bài N8](N8-finding-verifying-sources.md)). Trong lượt này, bạn **chỉ cần đọc hết Phần A** để biết cách tìm 12 dòng cơ bản trên mẫu biểu Việt Nam (`B 01-DN`, `B 02-DN`, `B 03-DN`, `B 09-DN`), rồi **dừng ở cuối Phần A** để sang [Bài 002](002-finding-a-cheap-stock.md).
- **Nếu bạn vừa học xong [Bài 009](009-valuation-multiples.md) (Bước 16/23 — Quay lại đọc Phần B):** Hãy tự trả lời 4 câu hỏi ôn tập sau (đáp án ở mục 9): (1) Viết phương trình kế toán ([Bài N2](N2-statement-line-items.md)); (2) `EBIT` khác lợi nhuận trước thuế ở khoản nào? (3) Theo `IFRS 16`, hợp đồng thuê trên 12 tháng tạo ra hai dòng nào trên bảng cân đối? (4) Vì sao công thức `FCFF ≈ CFO + lãi vay sau thuế − CapEx` ([Bài 004](004-cash-flow-and-earnings-quality.md)) có thể tính trùng nếu áp dụng máy móc?

---

## Phần A — Tìm đường trên báo cáo (sau N2)

Khi tải tệp PDF Báo cáo tài chính từ [Cổng công bố thông tin UBCKNN](https://congbothongtin.ssc.gov.vn/) hoặc mục **Quan hệ cổ đông** trên website doanh nghiệp, hãy đi theo 3 bước:

### Bước 1: Kiểm tra 3 thông tin mở đầu
1. **Luôn mở Báo cáo Hợp nhất (`Consolidated`), không lấy nhầm Báo cáo Riêng (`Separate`):** Khi phân tích cả tập đoàn, luôn dùng báo cáo **hợp nhất** (gộp công ty mẹ và các công ty con, ký hiệu mẫu có hậu tố `/HN`).
2. **Chỉ áp dụng mẫu `B 01-DN / B 02-DN / B 03-DN` cho doanh nghiệp phi tài chính:** Ngân hàng, bảo hiểm, chứng khoán có biểu mẫu riêng ([Bài 013](013-banks-insurers.md), [Bài F4](F4-vietnam-bank-analysis.md), [Bài F8](F8-vietnam-insurance-analysis.md)).
3. **Nhìn góc trên bên phải biểu mẫu:** Ghi nhận đơn vị tiền (`VND`, `triệu đồng` hay `tỷ đồng`) và dòng `"Ban hành theo Thông tư số…"` (`200/202` cho năm 2025 trở về trước; `99/43` từ năm 2026).

### Bước 2: Nhận diện 4 bảng trong bộ Báo cáo tài chính Việt Nam

| Ký hiệu mẫu | Tên gọi trên báo cáo Việt Nam | Khái niệm ở [Bài 001](001-business-financial-statements.md) & [Bài N2](N2-statement-line-items.md) | Trả lời câu hỏi gì? |
|---|---|---|---|
| **B 01-DN** | **Báo cáo tình hình tài chính** *(mẫu cũ TT 200: Bảng cân đối kế toán)* | Bảng cân đối kế toán (`Balance Sheet`) | Tại ngày chốt sổ, doanh nghiệp có **Tài sản** gì, nợ ai (**Nợ phải trả**) và phần **Vốn chủ sở hữu** là bao nhiêu? |
| **B 02-DN** | **Báo cáo kết quả hoạt động kinh doanh** | Báo cáo kết quả kinh doanh (`Income Statement`) | Trong kỳ vừa qua, thu bao nhiêu **Doanh thu**, trừ chi phí còn bao nhiêu **Lợi nhuận**? |
| **B 03-DN** | **Báo cáo lưu chuyển tiền tệ** | Báo cáo dòng tiền (`Cash Flow Statement`) | Tiền mặt thực sự chảy vào/ra két từ 3 luồng (Kinh doanh, Đầu tư, Tài chính) là bao nhiêu? |
| **B 09-DN** | **Bản thuyết minh báo cáo tài chính** | Thuyết minh (`Notes`) | Chi tiết bên trong từng con số của 3 bảng trên là gì? |

### Bước 3: Bảng tra cứu nhanh 12 chỉ tiêu cơ bản cho người mới (nối từ Bài N2)

| # | Khái niệm ở [Bài N2](N2-statement-line-items.md) | Bảng | Tên chỉ tiêu trên báo cáo Việt Nam | Mã cũ (2025) | Mã mới (2026) | Ví dụ VNM 2025 (tỷ đồng) |
|---:|---|---|---|---:|---:|---:|
| 1 | Doanh thu thuần | **B02** | Doanh thu thuần về bán hàng và cung cấp dịch vụ | `10` | `10` | `63.645,9` |
| 2 | Giá vốn hàng bán | **B02** | Giá vốn hàng bán | `11` | `11` | `37.436,4` |
| 3 | Lợi nhuận gộp | **B02** | Lợi nhuận gộp (`Mã 20 = Mã 10 − Mã 11`) | `20` | `20` | `26.209,5` |
| 4 | Lợi nhuận trước thuế | **B02** | Tổng lợi nhuận kế toán trước thuế | `50` | `50` | `11.650,0` |
| 5 | Lợi nhuận sau thuế | **B02** | LNST thu nhập doanh nghiệp (Mã `61`: thuộc CĐ công ty mẹ) | `60` (`61`) | `60` (`61`) | `9.413,6` (`9.410,2`) |
| 6 | Tiền mặt | **B01** | Tiền và tương đương tiền *(xem thêm Mã `123`: Tiền gửi có kỳ hạn)* | `110` | `110` | `1.794,9` *(+ `21.354,4` ở mã `123`)* |
| 7 | Phải thu ngắn hạn | **B01** | Các khoản phải thu ngắn hạn | `130` | `130` | `6.245,0` |
| 8 | Hàng tồn kho | **B01** | Hàng tồn kho | `140` | `140` | `6.839,3` |
| 9 | **Tổng tài sản** | **B01** | **Tổng cộng tài sản** *(Đổi từ `270` sang `280` từ năm 2026!)* | **`270`** | **`280`** | `53.312,4` |
| 10 | **Nợ phải trả** | **B01** | **Nợ phải trả** *(Nợ ngắn hạn mã `310` + Nợ dài hạn mã `330`)* | `300` | `300` | `18.829,4` |
| 11 | **Vốn chủ sở hữu** | **B01** | **Vốn chủ sở hữu** (`Mã 300 + Mã 400 = Mã 440 = Tổng tài sản`) | `400` | `400` | `34.483,0` |
| 12 | **Dòng tiền HĐKD (`CFO`)** | **B03** | **Lưu chuyển tiền thuần từ hoạt động kinh doanh** | `20` | `20` | `8.668,1` |

Kiểm tra nhanh trên số thật Vinamilk (`VNM`) năm 2025: `PHÉP_TÍNH` `Nợ phải trả (18.829,4) + Vốn chủ sở hữu (34.483,0) = 53.312,4 tỷ đồng`, khớp 100% với **Tổng cộng tài sản** (`53.312,4 tỷ đồng`).

> **Điểm dừng Phần A (Bước 6/23 Nhánh 1):** Không ghép tùy tiện số hợp nhất với số riêng; nếu không thấy chỉ tiêu thì kiểm tra thuyết minh hoặc ghi `CHƯA_BIẾT`, không tự điền bằng `0`. Nếu bạn vừa học đến đây từ [Bài N8](N8-finding-verifying-sources.md), **hãy dừng lại tại đây** và chuyển sang **[Bài 002: Hiểu và tìm một cổ phiếu đang được định giá rẻ](002-finding-a-cheap-stock.md)**. Bạn sẽ quay lại đọc **Phần B** sau khi hoàn thành [Bài 009](009-valuation-multiples.md)!

---

## Phần B — Đối chiếu và điều chỉnh (chỉ học sau Bài 009)

## 1. Văn bản nào áp dụng cho kỳ nào

`SỰ_THẬT` **Thông tư 99/2025/TT-BTC** ban hành ngày `27/10/2025`, có hiệu lực từ `01/01/2026` và áp dụng cho **năm tài chính bắt đầu từ hoặc sau 01/01/2026**; thay thế **Thông tư 200/2014/TT-BTC** (Điều 31 TT 99). Tổ chức tín dụng theo quy định riêng của NHNN (Điều 2).

`SỰ_THẬT` Báo cáo **hợp nhất** lập theo **Thông tư 43/2026/TT-BTC** ngày `20/04/2026` sửa đổi Thông tư 202/2014/TT-BTC, áp dụng cho năm tài chính bắt đầu từ `01/01/2026` (xác nhận trên báo cáo hợp nhất quý I và quý II/2026 của `VNM`; `CHƯA_BIẾT` toàn văn gốc TT 43 chưa mở trực tiếp).

| Báo cáo bạn đang đọc | Mẫu riêng | Mẫu hợp nhất |
|---|---|---|
| Năm tài chính bắt đầu **trước** `01/01/2026` (gồm năm 2025, và mọi quý thuộc niên độ bắt đầu ví dụ `01/10/2025`) | Thông tư 200/2014 | Thông tư 202/2014 |
| Năm tài chính bắt đầu **từ** `01/01/2026` trở đi | Thông tư 99/2025 | Thông tư 43/2026 |

`SỰ_THẬT` Từ năm 2026, doanh nghiệp trình bày cột đầu năm **"đã phân loại lại"** cho khớp mẫu mới. Phân loại lại làm đổi cả **số dư**, không chỉ đổi mã: trên BCTC hợp nhất quý I và II/2026 của `VNM`, hàng tồn kho tại `31/12/2025` là `6.839,3 tỷ đồng` nhưng ở cột `01/01/2026 (đã phân loại lại)` giảm xuống `6.530,0 tỷ đồng` vì mẫu mới tách **tài sản sinh học** (đàn bò) ra dòng riêng; tài sản cố định cũng giảm từ `12.648,9` xuống `11.573,5 tỷ đồng`.

## 2. Bốn báo cáo và quy tắc mã số

`SỰ_THẬT` Theo Điều 17 TT 99, bộ báo cáo năm gồm: `B 01-DN` (**Báo cáo tình hình tài chính** — tên cũ là Bảng cân đối kế toán), `B 02-DN` (Báo cáo kết quả hoạt động kinh doanh), `B 03-DN` (Báo cáo lưu chuyển tiền tệ) và `B 09-DN` (Bản thuyết minh). Báo cáo giữa niên độ dạng đầy đủ có hậu tố `a` (`B 01a-DN`), tóm lược có hậu tố `b`; hợp nhất có hậu tố `/HN`. Chỉ tiêu không có số liệu được bỏ qua nhưng **không được đánh lại mã số**.

## 3. Bản đồ mã: từ khái niệm khóa học tới dòng trên báo cáo Việt Nam

`SỰ_THẬT` Mã cũ đối chiếu trên BCTC hợp nhất năm 2025 của `VNM` (TT 202); mã mới đối chiếu trên BCTC quý I và II/2026 của `VNM` (riêng theo TT 99, hợp nhất theo TT 43).

### B02 — Báo cáo kết quả hoạt động kinh doanh

| Khái niệm khóa học | Chỉ tiêu VAS | Mã cũ | Mã mới |
|---|---|---:|---:|
| Doanh thu thuần / Giá vốn / Lợi nhuận gộp | Doanh thu thuần / Giá vốn hàng bán / Lợi nhuận gộp | `10 / 11 / 20` | `10 / 11 / 20` |
| — *(Dòng mới)* | Lãi/lỗ bán, thanh lý bất động sản đầu tư | — | **`21`** |
| Thu nhập tài chính / Chi phí tài chính | Doanh thu hoạt động tài chính / Chi phí tài chính | `21 / 22` | **`22 / 23`** |
| **Chi phí lãi vay** | "Trong đó: chi phí lãi vay" → đổi tên "chi phí đi vay" | `23` | **`24`** |
| Chi phí bán hàng / Quản lý (`SG&A`) | Chi phí bán hàng / Chi phí quản lý doanh nghiệp | `25 / 26` | `25 / 26` |
| Lãi/lỗ công ty liên doanh, liên kết | Phần lãi/lỗ trong công ty liên doanh, liên kết (hợp nhất) | `24` | **`27`** |
| (**KHÔNG** phải `EBIT`) | Lợi nhuận thuần từ hoạt động kinh doanh | `30` | `30` |
| Lợi nhuận khác / Trước thuế / Sau thuế | Lợi nhuận khác / Tổng LN kế toán trước thuế / LNST | `40 / 50 / 60` | `40 / 50 / 60` |
| LNST thuộc CĐ công ty mẹ / EPS cơ bản | LNST của CSH công ty mẹ / Lãi cơ bản trên cổ phiếu | `61 / 70` | `61 / 70` |

**Bẫy quan trọng nhất của B02:** `SỰ_THẬT` Trên mẫu mới, `Mã 30 = Mã 20 + Mã 21 + (Mã 22 − Mã 23) − (Mã 25 + Mã 26) + Mã 27`. `SUY_LUẬN` Như vậy Mã `30` **đã cộng doanh thu tài chính và trừ chi phí tài chính (gồm cả lãi vay)** — nên **không phải `EBIT`**. Cách tự dựng `EBIT`:
$$\text{EBIT xấp xỉ} = \text{Lợi nhuận trước thuế (Mã 50)} + \text{Chi phí lãi vay (Mã 23 cũ / Mã 24 mới)}$$
$$\text{EBIT hoạt động (loại thu nhập tài chính)} \approx \text{EBIT xấp xỉ} - \text{Doanh thu tài chính (Mã 21 cũ / Mã 22 mới)}$$

### B01 — Báo cáo tình hình tài chính

| Khái niệm khóa học | Chỉ tiêu VAS | Mã cũ | Mã mới |
|---|---|---:|---:|
| Tiền / Phải thu / Tồn kho | Tiền và tương đương tiền / Phải thu ngắn hạn / Hàng tồn kho | `110 / 130 / 140` | `110 / 130 / 140` |
| — *(Dòng mới)* | Tài sản sinh học ngắn hạn / Tài sản ngắn hạn khác | `— / 150` | **`150 / 160`** |
| — *(Dòng mới)* | Tài sản sinh học dài hạn | — | **`230`** |
| Tài sản dài hạn khác & BĐS đầu tư | BĐS đầu tư / TS dở dang / Đầu tư TC dài hạn / TS dài hạn khác | `230 / 240 / 250 / 260` | **`240 / 250 / 260 / 270`** |
| `Goodwill` (hợp nhất) | Lợi thế thương mại | `269` | **`279`** |
| **Tổng tài sản** | **Tổng cộng tài sản** | **`270`** | **`280`** |
| Nợ phải trả / Phải trả cổ tức (mới) | Nợ phải trả / Phải trả cổ tức (các mã sau dịch +1) | `300 / —` | `300` / **`313`** |
| **Nợ vay ngắn hạn / dài hạn** | Vay và nợ thuê tài chính ngắn hạn / dài hạn | **`320 / 338`** | **`321 / 339`** |
| Vốn chủ / LN giữ lại / NCI / Tổng nguồn vốn | Vốn chủ / LNST chưa phân phối / CĐ không kiểm soát / Tổng nguồn vốn | `400 / 421 / 429 / 440` | `400` / **`420`** / `429 / 440` |

**Bẫy mã 270:** Trên mẫu cũ, `270` là **Tổng tài sản**; trên mẫu mới, Tổng tài sản là **`280`** còn `270` chỉ là "Tài sản dài hạn khác" (`2.049,4 tỷ đồng` trên BCTC `VNM` đầu năm 2026).

### B03 — Báo cáo lưu chuyển tiền tệ (phương pháp gián tiếp)

| Khái niệm khóa học | Chỉ tiêu VAS | Mã (Cũ = Mới) |
|---|---|---:|
| Khấu hao TSCĐ và phân bổ lợi thế thương mại | Dòng điều chỉnh khấu hao đầu phương pháp gián tiếp | `02` |
| Lãi vay đã trả | Tiền lãi vay đã trả / Chi phí đi vay đã trả (**nằm trong phần HĐKD**) | `14` |
| Dòng tiền hoạt động (`CFO`) / `CapEx` | Lưu chuyển tiền thuần từ HĐKD / Tiền chi mua sắm TSCĐ (phần HĐĐT) | `20 / 21` |
| Lãi tiền gửi, cổ tức **đã thu** | Tiền thu lãi cho vay, cổ tức và lợi nhuận được chia (**phần HĐĐT**) | `27` |

## 4. Năm khác biệt VAS–IFRS làm đổi cách áp dụng các bài 003–009

| # | Khác biệt | Ảnh hưởng | Cách xử lý khi đọc báo cáo VAS |
|---|---|---|---|
| 1 | **Thuê tài sản (`VAS 06` vs `IFRS 16`):** `SỰ_THẬT` `VAS 06` không đưa thuê hoạt động (như thuê cửa hàng) lên bảng cân đối; `IFRS 16` ghi nhận tài sản quyền sử dụng và nợ thuê cho hợp đồng trên 12 tháng. | [Bài 005](005-debt-liquidity-survival.md), [Bài 009](009-valuation-multiples.md) | Ước tính nợ thuê từ thuyết minh cam kết thuê hoạt động khi so sánh với doanh nghiệp IFRS. |
| 2 | **Lợi thế thương mại (`Goodwill`):** `SỰ_THẬT` Theo VAS (TT 202 / TT 43), `goodwill` phân bổ đường thẳng tối đa 10 năm (`VNM` năm 2025 phân bổ `246,7 tỷ đồng`, quý I/2026 phân bổ `60,8 tỷ đồng`, ở mã `02` của `B03`). Theo IFRS, `goodwill` không phân bổ định kỳ. | [Bài 003](003-business-quality-moat-and-roic.md), [Bài 006](006-capital-allocation-governance.md), [Bài 009](009-valuation-multiples.md) | Cộng lại chi phí phân bổ `goodwill` khi dựng `EBITDA` hoặc khi so `EBIT/NOPAT` với doanh nghiệp IFRS. |
| 3 | **Vị trí Lãi vay đã trả và Lãi tiền gửi đã thu trên `B03`:** Trên VAS, lãi vay đã trả (Mã `14`) nằm ở `CFO`, còn lãi tiền gửi và cổ tức đã thu (Mã `27`) nằm ở dòng tiền đầu tư (`CFI`). | [Bài 004](004-cash-flow-and-earnings-quality.md) (`FCF`, `FCFF`, `CFO/LNST`) | Được cộng lại lãi vay sau thuế khi tính `FCFF` nhanh từ `CFO`. Với công ty nhiều tiền gửi (như `VNM`), cộng thêm Mã `27` khi kiểm tra tỷ lệ thu tiền thực (xem [earnings_quality.py](../practice/models/earnings_quality.py)). |
| 4 | **Nguyên tắc giá gốc nhiều hơn giá trị hợp lý:** TSCĐ, BĐS đầu tư ghi theo giá gốc trừ hao mòn/dự phòng. | [Bài 007](007-notes-and-accounting-red-flags.md), [Bài 009](009-valuation-multiples.md) (`P/B`) | Giá trị sổ sách có thể thấp xa giá thị trường của đất đai, bất động sản. |
| 5 | **Không có tiểu tổng `Operating profit` kiểu IFRS 18 và phải trừ Quỹ khen thưởng phúc lợi khi tính `EPS`:** Mã `30` trên `B02` đã gộp tài chính; Mã `70` (`EPS`) phải trừ quỹ khen thưởng phúc lợi. | [Bài 001](001-business-financial-statements.md), [Bài 002](002-finding-a-cheap-stock.md), [Bài 009](009-valuation-multiples.md) | Tự dựng `EBIT` theo mục 3 và luôn lấy `EPS` sau khi trừ quỹ khen thưởng phúc lợi. |

`SỰ_THẬT` Về lộ trình IFRS: Quyết định 345/QĐ-BTC (`16/03/2020`) và Thời báo Tài chính Việt Nam (`13/10/2026`) cho biết Bộ Tài chính đang xây dựng 42 chuẩn mực `VFRS` dựa trên `IFRS` (`KỊCH_BẢN` mốc dự kiến `01/01/2031`).

## 5. Ví dụ doanh nghiệp thật: đọc báo cáo hợp nhất 2025 của Vinamilk bằng bản đồ mã

`SỰ_THẬT` Số liệu từ **BCTC hợp nhất năm 2025 đã kiểm toán** của CTCP Sữa Việt Nam (`VNM`), công bố `27/02/2026` (mẫu TT 202/2014, kiểm toán bởi KPMG), đơn vị **tỷ đồng**, đối chiếu với [earnings_quality.py](../practice/models/earnings_quality.py):

| Chỉ tiêu | Mã (TT 202) | 2025 | 2024 |
|---|---|---:|---:|
| Doanh thu thuần / Giá vốn / Lợi nhuận gộp | `B02-10 / 11 / 20` | `63.645,9 / 37.436,4 / 26.209,5` | `61.782,6 / 36.192,4 / 25.590,2` |
| Doanh thu hoạt động tài chính / Chi phí lãi vay | `B02-21 / B02-23` | `1.496,9 / 325,8` | `1.585,7 / 279,4` |
| Lãi/lỗ công ty liên kết / Lợi nhuận khác | `B02-24 / B02-40` | `(150,6) / (9,8)` | `32,0 / 5,7` |
| Lợi nhuận trước thuế / LNST / LNST thuộc CĐ công ty mẹ | `B02-50 / 60 / 61` | `11.650,0 / 9.413,6 / 9.410,2` | `11.599,7 / 9.452,9 / 9.392,3` |
| `EPS` cơ bản (đồng/cp, đã trừ quỹ khen thưởng phúc lợi) | `B02-70` | `4.028` | `4.022` |
| Tiền và tương đương tiền / Tiền gửi có kỳ hạn ngắn hạn | `B01-110 / B01-123` | `1.794,9 / 21.354,4` | `2.225,9 / 23.259,8` |
| Tổng tài sản / Nợ phải trả / Vốn chủ sở hữu | `B01-270 / 300 / 400` | `53.312,4 / 18.829,4 / 34.483,0` | `55.049,1 / 18.874,7 / 36.174,4` |
| Vay ngắn hạn / Vay dài hạn | `B01-320 / 338` | `9.393,7 / 62,9` | `9.115,4 / 157,9` |
| Lưu chuyển tiền thuần HĐKD (`CFO`) / `CapEx` | `B03-20 / B03-21` | `8.668,1 / (1.762,0)` | `9.685,9 / (1.741,5)` |
| Tiền thu lãi tiền gửi và cổ tức (HĐĐT) / Cổ tức đã trả (HĐTC) | `B03-27 / B03-36` | `1.428,9 / (11.264,5)` | `1.473,1 / (8.159,6)` |

`PHÉP_TÍNH` Bốn phép kiểm thực chiến trên báo cáo `VNM` 2025:
1. **`EPS` và Quỹ khen thưởng, phúc lợi (Thuyết minh VI.11):** LNST thuộc cổ đông công ty mẹ `9.410,2 tỷ` trừ quỹ khen thưởng phúc lợi `992,8 tỷ` còn `8.417,4 tỷ`; chia `2.089.955.445` cổ phiếu ra **`4.028 đồng/cp`** (nếu quên trừ quỹ sẽ tính nhầm ra `4.503 đồng/cp`, lệch `11,8%`).
2. **Tỷ lệ chuyển hóa tiền mặt (`CFO / LNST`):** Tính thô `8.668,1 / 9.413,6 = 92,1%`. Cộng lại tiền thu lãi tiền gửi và cổ tức (`1.428,9 tỷ` ở `B03-27`): `(8.668,1 + 1.428,9) / 9.413,6 = 107,3%`.
3. **Ba biến thể `EBIT`:** (a) `EBIT` xấp xỉ `= 11.650,0 + 325,8 = 11.975,8 tỷ` (`ICR = 36,8x`); (b) Loại doanh thu tài chính `= 11.975,8 − 1.496,9 = 10.478,9 tỷ` (`ICR = 32,2x`); (c) `EBIT` cốt lõi `= 10.478,9 + 150,6 + 9,8 = 10.639,3 tỷ`.
4. **Cột phân loại lại sang mẫu TT 43 (Q2/2026):** Tại cột `01/01/2026 (đã phân loại lại)`, tổng tài sản `53.312,4 tỷ` chuyển sang **Mã `280`**, vay ngắn hạn `9.393,7 tỷ` chuyển sang **Mã `321`**, và phải trả cổ tức tách riêng ra **Mã `313`**.

## 6. Năm câu hỏi khi mở một báo cáo Việt Nam

1. Góc phải mẫu biểu ghi "Ban hành theo Thông tư số" mấy (`200/202` hay `99/43`), và là báo cáo riêng hay hợp nhất?
2. Ý kiến kiểm toán/soát xét là chấp nhận toàn phần hay ngoại trừ?
3. Lợi nhuận tính `P/E` đã kiểm tra phần trích quỹ khen thưởng phúc lợi (Mã `70`) chưa?
4. Khi tính `EBIT`, đã cộng chi phí lãi vay vào Mã `50` và tách doanh thu tài chính chưa?
5. Thuyết minh có cam kết thuê hoạt động lớn (`VAS 06`) và phân bổ lợi thế thương mại (`B03-02`) không?

## 7. Bài tập

`KỊCH_BẢN` Trừ Bài 6 và Bài 10 dùng số thật của `VNM`, các bài khác dùng số giả định (đơn vị: tỷ đồng). Tự giải 10 bài trước khi mở Đáp án:

1. **Xác định văn bản chế độ kế toán:** Doanh nghiệp có năm tài chính theo năm dương lịch (trừ câu d). Bạn đọc: (a) báo cáo riêng năm 2025; (b) báo cáo hợp nhất bán niên 2026; (c) báo cáo riêng năm 2026; (d) báo cáo riêng quý II của niên độ bắt đầu `01/10/2025` (kết thúc `31/03/2026`). Mỗi báo cáo áp dụng thông tư nào?
2. **Định vị mã số cũ và mới:** Trên **mẫu mới (TT 99 / TT 43)**, tổng tài sản, vay ngắn hạn và LNST chưa phân phối nằm ở mã nào? Trên **mẫu cũ (TT 200 / TT 202)** là mã nào?
3. **Dựng `EBIT` từ B02 mẫu mới:** Mẫu mới có Mã `20 = 500`; Mã `22` (doanh thu tài chính) `= 60`; Mã `23` (chi phí tài chính) `= 90`, trong đó Mã `24` (chi phí đi vay) `= 70`; Mã `25 = 120`; Mã `26 = 80`; không có Mã `21` và `27`; Mã `40 = 10`. Tính Mã `30`, Mã `50`, `EBIT` xấp xỉ và `EBIT` loại doanh thu tài chính.
4. **Bẫy mã 270 trên báo cáo năm 2026:** Một người lấy Mã `270` trên báo cáo năm 2026 của doanh nghiệp X được `1.200` và tính `ROA = 240 / 1.200 = 20%`, trong khi Mã `280` là `6.000`. Tính `ROA` đúng và giải thích lỗi.
5. **Tính `FCF` và `FCFF` nhanh trên báo cáo VAS:** Báo cáo VAS có `B03-20` (`CFO`) `= 400`; `B03-21` (`CapEx`) `= −150`; `B03-14` (chi phí đi vay đã trả) `= −50`; thuế suất `20%`. Tính `FCF` hẹp và `FCFF` nhanh. Vì sao được cộng lại lãi vay sau thuế?
6. **Tính tỷ số trên số thật VNM 2025:** Dùng bảng mục 5, tính: (a) biên LNST; (b) nợ phải trả / vốn chủ; (c) tốc độ tăng doanh thu thuần 2025 so với 2024. Nêu một điều chưa kết luận được từ ba số này.
7. **So sánh Nợ ròng/EBITDA giữa VAS và IFRS 16:** Doanh nghiệp A (VAS) và B (IFRS) cùng ngành bán lẻ, cùng thuê toàn bộ cửa hàng. A có `Nợ vay ròng/EBITDA = 1,0x`; B có `3,0x` (đã gộp nợ thuê). Chỉ ra lỗi nếu kết luận "A an toàn gấp ba B" và nêu cách điều chỉnh.
8. **Bẫy lấy Mã 30 làm `EBIT`:** "Lợi nhuận thuần từ hoạt động kinh doanh (Mã 30) là 800, đó chính là EBIT nên hệ số trả lãi = 800 / chi phí lãi vay." Chỉ ra lỗi và cách sửa.
9. **Điều chỉnh phân bổ Lợi thế thương mại (`Goodwill`):** Tập đoàn P (VAS) có lợi nhuận trước thuế `1.000 tỷ`, chi phí lãi vay `100 tỷ`, khấu hao TSCĐ `200 tỷ` và phân bổ lợi thế thương mại `80 tỷ`. Tính `EBIT` trước phân bổ goodwill (tương đương IFRS) và `EBITDA`.
10. **Ảnh hưởng của phân loại lại Tài sản sinh học lên `DIO`:** Trên BCTC của `VNM`, hàng tồn kho tại `31/12/2025` theo mẫu cũ là `6.839,3 tỷ đồng`, nhưng theo cột `01/01/2026 (đã phân loại lại)` là `6.530,0 tỷ đồng`. Với giá vốn năm 2025 là `37.436,4 tỷ đồng` (365 ngày), tính `DIO` theo hai con số này và giải thích vì sao không được ghép số năm 2026 với số năm 2025 chưa phân loại lại khi chạy [earnings_quality.py](../practice/models/earnings_quality.py).

## 8. Đáp án

1. **Văn bản áp dụng:** (a) TT 200/2014; (b) TT 43/2026; (c) TT 99/2025; (d) vẫn TT 200/2014 vì năm tài chính bắt đầu **trước** `01/01/2026`. Kiểm bằng dòng "Ban hành theo Thông tư số…" ở góc phải biểu mẫu.
2. **Mã số cũ và mới:** Mẫu mới: tổng tài sản **280**, vay ngắn hạn **321**, LNST chưa phân phối **420**. Mẫu cũ: **270**, **320**, **421**.
3. **Dựng `EBIT` từ B02 mẫu mới:** `PHÉP_TÍNH` Mã 30 `= 500 + (60 − 90) − (120 + 80) = 270`. Mã 50 `= 270 + 10 = 280`. `EBIT` xấp xỉ `= 280 + 70 = 350`. `EBIT` loại doanh thu tài chính `= 350 − 60 = 290`.
4. **Bẫy mã 270:** `PHÉP_TÍNH` `ROA` đúng `= 240 / 6.000 = 4,0%`. Trên mẫu TT 99/TT 43, tổng tài sản là mã **280**, còn mã 270 chỉ là "tài sản dài hạn khác".
5. **Tính `FCF` và `FCFF` nhanh:** `PHÉP_TÍNH` `FCF` hẹp `= 400 − 150 = 250`. `FCFF` nhanh `= 400 + 50 × (1 − 0,2) − 150 = 290`. Được cộng lại lãi vay sau thuế vì trên B03 của VAS, lãi vay đã trả (mã 14) đã bị trừ trong `CFO`.
6. **Số thật VNM 2025:** `PHÉP_TÍNH` (a) Biên LNST `= 9.413,6 / 63.645,9 = 14,8%`; (b) Nợ phải trả / Vốn chủ `= 18.829,4 / 34.483,0 = 0,55 lần`; (c) Tăng trưởng doanh thu `= 63.645,9 / 61.782,6 − 1 = +3,0%`. `SUY_LUẬN` Chưa kết luận được tăng trưởng do giá hay sản lượng và cổ phiếu đang đắt hay rẻ.
7. **So sánh VAS và IFRS 16:** `SUY_LUẬN` A lập theo VAS nên thuê cửa hàng (thuê hoạt động) nằm ngoài bảng cân đối; B lập theo IFRS 16 đã vốn hóa nợ thuê vào tổng nợ. Muốn so sánh phải cộng giá trị hiện tại của cam kết thuê hoạt động vào nợ của A.
8. **Bẫy lấy Mã 30 làm `EBIT`:** `SUY_LUẬN` Mã 30 đã trừ chi phí lãi vay và cộng doanh thu tài chính. Cách sửa: `EBIT ≈ Mã 50 + Chi phí lãi vay (mã 23 cũ / 24 mới) − Doanh thu tài chính`.
9. **Điều chỉnh phân bổ Goodwill:** `PHÉP_TÍNH` `EBIT` theo VAS `= 1.000 + 100 = 1.100 tỷ`. `EBIT` tương đương IFRS `= 1.100 + 80 = 1.180 tỷ`. `EBITDA = 1.100 + 200 + 80 = 1.380 tỷ đồng`.
10. **Ảnh hưởng phân loại lại Tài sản sinh học lên `DIO`:** `PHÉP_TÍNH` `DIO` theo số cũ (`6.839,3 tỷ`) `= (6.839,3 / 37.436,4) × 365 ≈ 66,68 ngày`; theo số đã phân loại lại (`6.530,0 tỷ`) `≈ 63,66 ngày` (lệch `3,02 ngày`). Khi chạy [earnings_quality.py](../practice/models/earnings_quality.py) qua hai năm 2025–2026, bắt buộc phải lấy số đầu năm 2026 từ cột "đã phân loại lại".

## 9. Đáp án phần ôn bài cũ

1. `Tài sản = Nợ phải trả + Vốn chủ sở hữu`.
2. `EBIT` chưa trừ chi phí lãi vay; lợi nhuận trước thuế đã trừ.
3. Tài sản quyền sử dụng (`Right-of-use asset`) và Nợ thuê (`Lease liability`).
4. Nếu lãi vay đã trả nằm ở dòng tiền tài chính (như IFRS 18) thì `CFO` chưa trừ lãi vay; cộng lại sẽ bị tính trùng.

## Bài làm với dữ liệu thiếu hoặc lệch

Khi xử lý chuỗi dữ liệu 2024–2026 của doanh nghiệp Việt Nam, bạn sẽ gặp hai hiện tượng dữ liệu lệch:
1. **Dịch chuyển mã số và phân loại lại số dư đầu kỳ khi chuyển từ TT 200/202 sang TT 99/43:** Số dư cuối năm 2025 trên báo cáo 2025 khác với cột `01/01/2026 (đã phân loại lại)` trên báo cáo 2026 ở các dòng Hàng tồn kho, TSCĐ, Tài sản sinh học, Phải trả cổ tức.
2. **Thiếu dòng "Chi phí đi vay" trên bảng tóm tắt tự động:** Nhiều phần mềm chỉ lấy dòng tổng "Chi phí tài chính" (mã 22 cũ / 23 mới) mà bỏ sót dòng con "chi phí lãi vay / chi phí đi vay" (mã 23 cũ / 24 mới).

**Quy trình xử lý chuẩn:** Dùng cột "Số đầu năm (đã phân loại lại)" trên báo cáo 2026 khi tính tăng trưởng/vòng quay năm 2026; mở trực tiếp `B02` và `B03` để đối chiếu `B02 mã 23/24`, `B03 mã 14` và `B03 mã 27` như trong [earnings_quality.py](../practice/models/earnings_quality.py).

## Sai ở đâu

### Sai lầm 1: Quét dữ liệu tự động theo Mã `270` cho báo cáo năm 2026 và tưởng đó là Tổng tài sản
- **Sai ở đâu:** Trên mẫu TT 99/TT 43, Tổng tài sản đã chuyển xuống **Mã `280`**, còn Mã `270` chỉ là "Tài sản dài hạn khác" (`2.049,4 tỷ` so với `53.312,4 tỷ` của `VNM`).
- **Cách sửa:** Luôn kiểm tra tên chỉ tiêu và phương trình `Tổng tài sản (Mã 280) = Tổng nguồn vốn (Mã 440)`.

### Sai lầm 2: Lấy dòng "Lợi nhuận thuần từ hoạt động kinh doanh" (Mã 30) làm `EBIT`
- **Sai ở đâu:** Mã 30 đã cộng doanh thu tài chính và trừ chi phí tài chính (gồm lãi vay).
- **Cách sửa:** Tự dựng `EBIT` từ `Mã 50 + Chi phí lãi vay (Mã 23 cũ / 24 mới)` và tách doanh thu tài chính.

### Sai lầm 3: Lấy `Mã 61 / Số cổ phiếu` làm `EPS` mà quên trừ Quỹ khen thưởng, phúc lợi
- **Sai ở đâu:** Quên trừ phần trích Quỹ khen thưởng, phúc lợi (với `VNM` năm 2025 là `992,8 tỷ đồng`) khỏi tử số trước khi tính `EPS`.
- **Cách sửa:** Luôn đọc Thuyết minh "Lãi trên cổ phiếu" và dùng `EPS` ở Mã `70`.

## Kiểm tra chuyển bài

- **Nếu bạn vừa học xong Phần A (Bước 6/23 Nhánh 1):** Hãy chuyển ngay sang **[Bài 002: Hiểu và tìm một cổ phiếu đang được định giá rẻ](002-finding-a-cheap-stock.md)**.
- **Nếu bạn vừa hoàn thành Phần B (Bước 16/23 — sau [Bài 009](009-valuation-multiples.md)):** Trước khi bước sang **[Bài N7: Dữ liệu, xác suất và bất định](N7-data-probability-uncertainty.md)**, hãy trả lời 3 câu hỏi sau:
  1. **Sang Phân tích Dòng tiền ([Bài 004](004-cash-flow-and-earnings-quality.md) & [earnings_quality.py](../practice/models/earnings_quality.py)):** Vì sao với doanh nghiệp nhiều tiền gửi có kỳ hạn như `VNM` (`21.354,4 tỷ` ở `B01-123`), tỷ số `CFO / LNST` tính thô thấp hơn thực tế thu tiền, và cần lấy thêm mã nào trên `B03`?
  2. **Sang Phân tích Nợ vay ([Bài 005](005-debt-liquidity-survival.md)):** Trên báo cáo năm 2026 (TT 99 / TT 43), để tính Tổng nợ vay chịu lãi (`Total Debt`), bạn cộng hai mã số nào trên `B01`?
  3. **Sang Định giá Bội số ([Bài 009](009-valuation-multiples.md)):** Khi so `EV/EBITDA` và `P/E` của tập đoàn bán lẻ Việt Nam (VAS) với doanh nghiệp khu vực (IFRS), bạn cần điều chỉnh tối thiểu 3 khoản nào (thuê hoạt động, phân bổ goodwill, quỹ khen thưởng phúc lợi)?

## 11. Ranh giới an toàn

- Bài này **không** phải khuyến nghị mua/bán/nắm giữ `VNM` hay bất kỳ mã nào; không áp dụng mẫu `B01-DN / B02-DN / B03-DN` cho ngân hàng, bảo hiểm, chứng khoán ([Bài 013](013-banks-insurers.md), [Bài F4](F4-vietnam-bank-analysis.md), [Bài F8](F8-vietnam-insurance-analysis.md)).

## 13. Nguồn Internet đã mở

Mở ngày `2026-10-26` và kiểm tra đối chiếu `2026-11-06`:

| Nguồn | Loại | Ngày ban hành | Dùng cho |
|---|---|---|---|
| [Thông tư 99/2025/TT-BTC (PDF, LuatVietnam)](https://static3.luatvietnam.vn/uploaded/others/2025/10/30/tt99_3010133637.pdf) & [KPMG Việt Nam](https://kpmg.com/vn/vi/insights/2025/11/key-changes-in-vietnamese-accounting-system-for-enterprises.html) & [MISA](https://amis.misa.vn/251687/so-sanh-ve-bieu-mau-bao-cao-tai-chinh-giua-thong-tu-99-va-thong-tu-200/) | Văn bản gốc & Thứ cấp | 27/10/2025 & 11/2025 | Hiệu lực `01/01/2026`, thay TT 200, đổi tên "Báo cáo tình hình tài chính", các mã dịch chuyển |
| [LuatVietnam — Thông tư 43/2026/TT-BTC](https://luatvietnam.vn/tai-chinh/thong-tu-43-2026-tt-btc-sua-doi-bao-cao-tai-chinh-hop-nhat-hieu-luc-20-04-2026-432924-d1.html) & [Tạp chí Kinh tế – Tài chính](https://tapchikinhtetaichinh.vn/quy-dinh-moi-ve-phuong-phap-lap-va-trinh-bay-bao-cao-tai-chinh-hop-nhat-theo-thong-tu-so-43-2026-tt-btc-mot-so-ham-y-quan-tri-161827.html) | Thứ cấp / Tạp chí Bộ Tài chính | 20/04/2026 & 18/07/2026 | Mẫu hợp nhất mới (mã 279, mã 27) |
| [VNM — BCTC hợp nhất kiểm toán 2025](https://d8um25gjecm9v.cloudfront.net/cms/20260227_BCTC_KIEM_TOAN_2025_HOP_NHAT_VN_94f1e76e45.pdf), [Q1/2026](https://d8um25gjecm9v.cloudfront.net/cms/20260429_VNM_BCTC_DA_SOAT_XET_Q1_2026_HOP_NHAT_VN_d44326741a.pdf), [Q2/2026 HN](https://d8um25gjecm9v.cloudfront.net/cms/20260730_VNM_BCTC_da_soat_xet_Q2_2026_Hop_nhat_76ef2e29c1.pdf) & [Q2/2026 Riêng](https://d8um25gjecm9v.cloudfront.net/cms/20260730_VNM_BCTC_da_soat_xet_Q2_2026_Rieng_936c679432.pdf) | **Nguồn gốc** | 02–07/2026 | Bảng mục 5; mã cũ & mới (`280`, `321`, `420`); cột "đã phân loại lại"; EPS sau quỹ KTPL |
| [Quyết định 345/QĐ-BTC](https://luatvietnam.vn/tai-chinh/quyet-dinh-345-qd-btc-2020-de-an-ap-dung-chuan-muc-bao-cao-tai-chinh-181513-d1.html), [Thời báo Tài chính VN — 42 VFRS](https://thoibaotaichinhvietnam.vn/chinh-thuc-trien-khai-xay-dung-42-chuan-muc-bao-cao-tai-chinh-viet-nam-205280.html), [Tạp chí QLNN — VAS 06 vs IFRS 16](https://www.quanlynhanuoc.vn/?p=59652), [BDO — IFRB 2026/05](https://www.bdo.global/getmedia/d27359ee-5875-45ff-9d36-18b8aa59c8fd/IFRB_2026_05.pdf?ext=.pdf) & [UBCKNN](https://congbothongtin.ssc.gov.vn/) | Văn bản / Chuẩn mực / Cơ quan quản lý | 2020–2026 | Lộ trình VFRS, khác biệt thuê tài sản VAS 06 vs IFRS 16, phân loại lãi vay/cổ tức |
