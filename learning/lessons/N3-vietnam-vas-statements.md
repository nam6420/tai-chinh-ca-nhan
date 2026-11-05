# Bài N3: Đọc báo cáo tài chính Việt Nam theo VAS

- Ngày: `2026-11-05`
- Chốt dữ liệu lúc: `2026-11-05 12:30 UTC+7 (Asia/Ho_Chi_Minh)`
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Mục tiêu: Nói được chế độ kế toán nào áp dụng cho báo cáo năm 2025 và năm 2026; tìm được trên mẫu B01/B02/B03 các chỉ tiêu mà khóa học dùng (doanh thu, lợi nhuận gộp, EBIT, lãi vay, lợi nhuận thuộc công ty mẹ, tổng tài sản, nợ vay, dòng tiền hoạt động, chi tiêu vốn); tránh bẫy **mã số đổi** giữa mẫu cũ và mẫu mới; nêu được năm khác biệt VAS–IFRS làm thay đổi cách áp các bài 004–009.
- Thời lượng: Ba phiên học có điểm dừng (Phần A, Phần B1, Phần B2) + thực hành kiểm chứng số liệu VNM trên [earnings_quality.py](../practice/models/earnings_quality.py).
- Bài trước liên quan: [Bài 001](001-business-financial-statements.md), [Bài N2](N2-statement-line-items.md).
- Câu hỏi cốt lõi: **Chỉ tiêu mà khóa học dạy bằng IFRS nằm ở dòng nào, mã nào trên báo cáo Việt Nam — và chỗ nào hai bên không khớp?**

> Đây là bài học nền tảng, không phải khuyến nghị mua, bán hay nắm giữ chứng khoán. Ví dụ Vinamilk (VNM) dùng số từ báo cáo tài chính hợp nhất đã kiểm toán do doanh nghiệp công bố để học cách đọc mẫu biểu.

## Hiểu bài này trong 1 phút

Các bài 001–009 dạy bằng ngôn ngữ IFRS và ví dụ Apple (US GAAP). Nhưng báo cáo của doanh nghiệp niêm yết Việt Nam được lập theo **chuẩn mực kế toán Việt Nam (VAS)** và **chế độ kế toán** do Bộ Tài chính ban hành: mẫu biểu cố định, mỗi dòng có **mã số**. Mã số là "tọa độ" giúp bạn tìm nhanh một chỉ tiêu — cho tới khi Bộ Tài chính đổi mẫu và tọa độ dịch chuyển. Từ năm tài chính 2026 có chế độ kế toán mới và nhiều mã đã đổi: người đọc báo cáo 2025 và 2026 cạnh nhau mà chỉ nhìn mã sẽ đọc nhầm.

> Câu cần nhớ: **Đọc theo tên chỉ tiêu, dùng mã để định vị, và luôn nhìn dòng "Ban hành theo Thông tư số…" ở góc mẫu trước khi tin một mã số.**

## Phần A — Tìm đường trên báo cáo (học ngay sau N2)

- **Lấy báo cáo ở đâu:** [Cổng công bố thông tin của UBCKNN](https://congbothongtin.ssc.gov.vn/) hoặc trang quan hệ nhà đầu tư của doanh nghiệp.
- **Riêng hay hợp nhất:** Khi phân tích một tập đoàn, luôn dùng báo cáo **hợp nhất** (gộp công ty mẹ và các công ty con).
- **Chọn doanh nghiệp phi tài chính:** Ngân hàng, bảo hiểm, chứng khoán có mẫu biểu riêng ([Bài 013](013-financial-institutions-wear-hats.md), [F4](F4-vietnam-bank-analysis.md), [F8](F8-insurance-float-actuarial.md)).

Mở một báo cáo và ghi bốn thông tin: tên doanh nghiệp, kỳ báo cáo, đơn vị tiền, báo cáo riêng hay hợp nhất; sau đó tìm theo **tên chỉ tiêu**: (1) doanh thu và lợi nhuận trên B02; (2) tiền, tài sản, nợ và vốn chủ trên B01; (3) dòng tiền hoạt động trên B03 và trang thuyết minh.

> **Điểm dừng Phần A:** Không ghép tùy tiện số hợp nhất với số riêng; dòng tiền đo trong một kỳ; nếu không thấy chỉ tiêu thì kiểm tên khác/thuyết minh, chưa tìm được thì ghi `CHƯA_BIẾT`, không tự điền bằng 0.

## Phần B — Đối chiếu và điều chỉnh (học sau Bài 009)

Câu hỏi ôn đầu Phần B (đáp án ở mục 9): (1) Viết phương trình kế toán (Bài N2); (2) EBIT khác lợi nhuận trước thuế ở khoản nào? (3) Theo IFRS 16, hợp đồng thuê trên 12 tháng tạo ra hai dòng nào trên bảng cân đối? (4) Vì sao công thức FCFF nhanh `CFO + lãi vay sau thuế − capex` có thể tính trùng nếu áp dụng máy móc?

## 1. Văn bản nào áp dụng cho kỳ nào

`SỰ_THẬT` **Thông tư 99/2025/TT-BTC** "Hướng dẫn Chế độ kế toán doanh nghiệp" ban hành ngày `27/10/2025`, có hiệu lực từ `01/01/2026` và áp dụng cho **năm tài chính bắt đầu từ hoặc sau 01/01/2026**; thay thế **Thông tư 200/2014/TT-BTC** (trừ phần kế toán cổ phần hóa DNNN), cùng các Thông tư 75/2015, 53/2016 và 195/2012 (Điều 31 TT 99). Tổ chức tín dụng theo quy định riêng của NHNN (Điều 2).

`SỰ_THẬT` Báo cáo tài chính **hợp nhất** lập theo văn bản riêng: **Thông tư 43/2026/TT-BTC** ngày `20/04/2026` sửa đổi Thông tư 202/2014/TT-BTC và thay mẫu biểu, áp dụng cho năm tài chính bắt đầu từ `01/01/2026` (xác nhận trên báo cáo hợp nhất quý I và quý II/2026 của VNM ghi "Ban hành theo Thông tư số 43/2026/TT-BTC"; `CHƯA_BIẾT` văn bản gốc TT 43 chưa mở được trực tiếp).

| Báo cáo bạn đang đọc | Mẫu riêng | Mẫu hợp nhất |
|---|---|---|
| Năm tài chính bắt đầu **trước** 01/01/2026 (gồm năm 2025, và mọi quý thuộc niên độ bắt đầu ví dụ 01/10/2025) | Thông tư 200/2014 | Thông tư 202/2014 |
| Năm tài chính bắt đầu từ 01/01/2026 trở đi | Thông tư 99/2025 | Thông tư 43/2026 |

`SỰ_THẬT` Từ năm 2026, doanh nghiệp trình bày cột kỳ trước **"đã phân loại lại"** cho khớp mẫu mới. Phân loại lại có thể đổi cả **số dư** của từng khoản, không chỉ đổi mã: trên BCTC hợp nhất quý I và II/2026 của VNM, hàng tồn kho tại 31/12/2025 là `6.839,3 tỷ đồng` nhưng ở cột `01/01/2026 (đã phân loại lại)` là `6.530,0 tỷ đồng` vì mẫu mới tách **tài sản sinh học** (đàn bò) ra dòng riêng; tài sản cố định cũng giảm từ `12.648,9` xuống `11.573,5 tỷ đồng`.

## 2. Bốn báo cáo và tên gọi

`SỰ_THẬT` Theo Điều 17 TT 99, bộ báo cáo năm của doanh nghiệp hoạt động liên tục gồm:

| Mẫu | Tên theo TT 99 | Tên cũ theo TT 200 | Khái niệm trong khóa học |
|---|---|---|---|
| B 01-DN | **Báo cáo tình hình tài chính** | Bảng cân đối kế toán | Bảng cân đối (balance sheet) |
| B 02-DN | Báo cáo kết quả hoạt động kinh doanh | (giữ tên) | Báo cáo kết quả kinh doanh |
| B 03-DN | Báo cáo lưu chuyển tiền tệ | (giữ tên) | Báo cáo dòng tiền |
| B 09-DN | Bản thuyết minh báo cáo tài chính | (giữ tên) | Thuyết minh (Bài 007) |

`SỰ_THẬT` Báo cáo giữa niên độ dạng đầy đủ có hậu tố `a` (`B 01a-DN`…), dạng tóm lược dùng hậu tố `b`; hậu tố `/HN` dành cho báo cáo hợp nhất. Theo Điều 17.4 TT 99, chỉ tiêu không có số liệu được bỏ không trình bày nhưng **không được đánh lại mã số**.

## 3. Bản đồ mã: từ khái niệm khóa học tới dòng trên báo cáo Việt Nam

`SỰ_THẬT` Mã cũ đối chiếu trên BCTC hợp nhất năm 2025 của VNM (TT 202); mã mới đối chiếu trên BCTC quý I và II/2026 của VNM (riêng theo TT 99, hợp nhất theo TT 43).

### B02 — Báo cáo kết quả hoạt động kinh doanh

| Khái niệm khóa học | Chỉ tiêu VAS | Mã cũ | Mã mới |
|---|---|---|---|
| Doanh thu thuần | Doanh thu thuần về bán hàng và cung cấp dịch vụ | 10 | 10 |
| Giá vốn | Giá vốn hàng bán | 11 | 11 |
| Lợi nhuận gộp | Lợi nhuận gộp | 20 | 20 |
| — | Lãi/lỗ bán, thanh lý bất động sản đầu tư (dòng **mới**) | — | 21 |
| Thu nhập tài chính | Doanh thu hoạt động tài chính | 21 | **22** |
| Chi phí tài chính | Chi phí tài chính | 22 | **23** |
| **Chi phí lãi vay** | "Trong đó: chi phí lãi vay" → đổi tên "chi phí đi vay" | 23 | **24** |
| Chi phí bán hàng / quản lý | Chi phí bán hàng / Chi phí quản lý doanh nghiệp | 25 / 26 | 25 / 26 |
| Lãi/lỗ công ty liên doanh, liên kết | Phần lãi/lỗ trong công ty liên doanh, liên kết (hợp nhất) | 24 | **27** |
| (**không** phải EBIT) | Lợi nhuận thuần từ hoạt động kinh doanh | 30 | 30 |
| Thu nhập/chi phí khác | Thu nhập khác / Chi phí khác / Lợi nhuận khác | 31 / 32 / 40 | 31 / 32 / 40 |
| Lợi nhuận trước thuế | Tổng lợi nhuận kế toán trước thuế | 50 | 50 |
| Lợi nhuận sau thuế | Lợi nhuận sau thuế thu nhập doanh nghiệp | 60 | 60 |
| Lợi nhuận thuộc cổ đông công ty mẹ | LNST của chủ sở hữu công ty mẹ (hợp nhất) | 61 | 61 |
| EPS cơ bản | Lãi cơ bản trên cổ phiếu | 70 | 70 |

**Bẫy quan trọng nhất của B02:** `SỰ_THẬT` Công thức của mã 30 trên mẫu mới là `30 = 20 + 21 + (22 − 23) − (25 + 26) + 27`. `SUY_LUẬN` Như vậy "lợi nhuận thuần từ hoạt động kinh doanh" (mã 30) **đã cộng doanh thu tài chính và trừ chi phí tài chính (gồm cả lãi vay)** — nên **không phải EBIT**. Cách dựng EBIT từ B02:

```text
EBIT xấp xỉ = Lợi nhuận trước thuế (50) + Chi phí lãi vay (23 cũ / 24 mới)
EBIT hoạt động (loại thu nhập tài chính) ≈ EBIT xấp xỉ − Doanh thu tài chính (21 cũ / 22 mới)
```

### B01 — Báo cáo tình hình tài chính

| Khái niệm khóa học | Chỉ tiêu VAS | Mã cũ | Mã mới |
|---|---|---|---|
| Tiền | Tiền và các khoản tương đương tiền | 110 | 110 |
| Phải thu | Các khoản phải thu ngắn hạn | 130 | 130 |
| Tồn kho | Hàng tồn kho (mẫu mới tách tài sản sinh học ra dòng riêng) | 140 | 140 |
| — | Tài sản sinh học ngắn hạn (dòng **mới**) / Tài sản ngắn hạn khác | — / 150 | **150 / 160** |
| — | Tài sản sinh học dài hạn (dòng **mới**) | — | **230** |
| — | BĐS đầu tư / TS dở dang dài hạn / Đầu tư tài chính dài hạn / TS dài hạn khác | 230 / 240 / 250 / 260 | **240 / 250 / 260 / 270** |
| Goodwill (hợp nhất) | Lợi thế thương mại | 269 | **279** |
| **Tổng tài sản** | Tổng cộng tài sản | **270** | **280** |
| Nợ phải trả / Người mua trả trước | Nợ phải trả / Người mua trả tiền trước ngắn hạn | 300 / 312 | 300 / 312 |
| — | Phải trả cổ tức (dòng **mới**; các mã sau dịch thêm 1) | — | **313** |
| **Nợ vay ngắn hạn / dài hạn** | Vay và nợ thuê tài chính ngắn hạn / dài hạn | **320 / 338** | **321 / 339** |
| Vốn chủ sở hữu / LN giữ lại / NCI | Vốn chủ sở hữu / LNST chưa phân phối / Lợi ích CĐ không kiểm soát | 400 / 421 / 429 | 400 / **420** / 429 |
| Tổng nguồn vốn | Tổng cộng nguồn vốn | 440 | 440 |

**Bẫy mã 270:** Trên mẫu cũ, `270` là **tổng tài sản**; trên mẫu mới, tổng tài sản là **`280`** còn `270` là "tài sản dài hạn khác" (trên BCTC VNM cột 01/01/2026 là `2.049,4 tỷ đồng`). Lấy nhầm mã `270` trên báo cáo 2026 làm tổng tài sản sẽ làm sai lệch toàn bộ ROA và vòng quay tài sản!

### B03 — Báo cáo lưu chuyển tiền tệ (phương pháp gián tiếp)

| Khái niệm khóa học | Chỉ tiêu VAS | Mã (cũ = mới) |
|---|---|---:|
| Khấu hao TSCĐ và phân bổ lợi thế thương mại | Dòng điều chỉnh đầu phương pháp gián tiếp | 02 |
| Lãi vay đã trả | "Tiền lãi vay đã trả" / "Chi phí đi vay đã trả" (**nằm trong phần HĐKD**) | 14 |
| Dòng tiền hoạt động (CFO) | Lưu chuyển tiền thuần từ hoạt động kinh doanh | 20 |
| Chi tiêu vốn (CapEx) | Tiền chi mua sắm, xây dựng TSCĐ và TS dài hạn khác (phần đầu tư) | 21 |
| Lãi tiền gửi, cổ tức **đã thu** | Tiền thu lãi cho vay, cổ tức và lợi nhuận được chia (**phần đầu tư**) | 27 |
| Dòng tiền đầu tư / tài chính / Tiền cuối kỳ | Lưu chuyển tiền thuần HĐĐT / HĐTC / Tiền cuối kỳ | 30 / 40 / 70 |

> **Điểm dừng Phiên B1:** Tìm tổng tài sản (`270` cũ / `280` mới) và vay ngắn hạn (`320` / `321`) trên báo cáo thật, dựng `EBIT` xấp xỉ từ B02.

## 4. Năm khác biệt VAS–IFRS làm đổi cách áp các bài trước

| # | Khác biệt | Ảnh hưởng | Cách xử lý khi đọc báo cáo VAS |
|---|---|---|---|
| 1 | **Thuê tài sản (VAS 06 vs IFRS 16):** `SỰ_THẬT` VAS 06 chia thuê tài chính và thuê hoạt động; thuê hoạt động **không** lên bảng cân đối. IFRS 16 ghi nhận tài sản quyền sử dụng và nợ thuê cho hợp đồng trên 12 tháng. | Bài 005 (nợ ròng), Bài 009 (EV/EBITDA) | Khi so doanh nghiệp VAS (như chuỗi bán lẻ thuê cửa hàng) với doanh nghiệp IFRS, phải ước nợ thuê từ thuyết minh cam kết thuê hoạt động hoặc loại thuê ở cả hai bên. |
| 2 | **Lợi thế thương mại (`Goodwill`):** `SỰ_THẬT` Theo VAS (TT 202 / TT 43), lợi thế thương mại được **phân bổ đường thẳng tối đa 10 năm** (VNM năm 2025 phân bổ `246,7 tỷ đồng`, quý I/2026 phân bổ `60,8 tỷ đồng`, nằm ở mã 02 của B03). Theo IFRS, goodwill không phân bổ định kỳ mà kiểm tra suy giảm giá trị. | Bài 006, 007, 009 | Lợi nhuận VAS đã bị trừ khoản phân bổ này; khi dựng EBITDA hoặc so với doanh nghiệp IFRS phải cộng lại. |
| 3 | **Vị trí Lãi vay đã trả và Lãi tiền gửi đã thu trên B03:** Trên VAS, lãi vay đã trả (mã 14) nằm ở **dòng tiền hoạt động (CFO)**, còn lãi tiền gửi và cổ tức đã thu (mã 27) nằm ở **dòng tiền đầu tư**. | Bài 004 (FCF, FCFF, `CFO/LNST`) | Khi tính FCFF nhanh từ CFO của VAS thì **được** cộng lại lãi vay sau thuế. Với doanh nghiệp nhiều tiền gửi (như VNM), lợi nhuận có lãi tiền gửi nhưng CFO không có, làm tỷ lệ `CFO/LNST` bị đánh giá thấp nếu không điều chỉnh (xem [earnings_quality.py](../practice/models/earnings_quality.py)). |
| 4 | **Nguyên tắc giá gốc nhiều hơn giá trị hợp lý:** Tài sản cố định, bất động sản đầu tư, chứng khoán kinh doanh khi hoạt động liên tục ghi theo giá gốc trừ dự phòng. | Bài 007, 009 (P/B) | Giá trị sổ sách có thể thấp xa giá thị trường của đất đai, chứng khoán; thận trọng khi so P/B. |
| 5 | **Không có tiểu tổng "Lợi nhuận hoạt động" kiểu IFRS 18 và không có MPM bắt buộc:** Mã 30 trên B02 đã gộp tài chính. | Bài 001, 007 | Tự dựng `EBIT` theo công thức ở mục 3 và tự đối chiếu các chỉ tiêu điều chỉnh về B02. |

`SỰ_THẬT` Về lộ trình IFRS: Quyết định 345/QĐ-BTC (`16/03/2020`) và thông tin từ Thời báo Tài chính Việt Nam (`13/10/2026`) cho biết Bộ Tài chính đã khởi động xây dựng 42 chuẩn mực báo cáo tài chính Việt Nam (VFRS) dựa trên IFRS (`KỊCH_BẢN` mốc dự kiến `01/01/2031`). Do đó trong những năm tới, đọc thành thạo VAS vẫn là kỹ năng bắt buộc.

## 5. Ví dụ doanh nghiệp thật: đọc báo cáo hợp nhất 2025 của Vinamilk bằng bản đồ mã

`SỰ_THẬT` Số dưới đây lấy từ **Báo cáo tài chính hợp nhất năm 2025 đã kiểm toán** của CTCP Sữa Việt Nam (`VNM`), công bố `27/02/2026` (mẫu TT 202/2014, kiểm toán bởi KPMG với ý kiến chấp nhận toàn phần), đơn vị quy đổi **tỷ đồng** (làm tròn 1 chữ số thập phân), và đối chiếu với dữ liệu kiểm chứng trong [earnings_quality.py](../practice/models/earnings_quality.py):

| Chỉ tiêu | Mã (TT 202) | 2025 | 2024 |
|---|---|---:|---:|
| Doanh thu thuần | B02-10 | 63.645,9 | 61.782,6 |
| Giá vốn hàng bán | B02-11 | 37.436,4 | 36.192,4 |
| Lợi nhuận gộp | B02-20 | 26.209,5 | 25.590,2 |
| Doanh thu hoạt động tài chính | B02-21 | 1.496,9 | 1.585,7 |
| Chi phí lãi vay | B02-23 | 325,8 | 279,4 |
| Lãi/lỗ công ty liên kết / Lợi nhuận khác | B02-24 / B02-40 | (150,6) / (9,8) | 32,0 / 5,7 |
| Lợi nhuận trước thuế | B02-50 | 11.650,0 | 11.599,7 |
| Lợi nhuận sau thuế / LNST thuộc CĐ công ty mẹ | B02-60 / B02-61 | 9.413,6 / 9.410,2 | 9.452,9 / 9.392,3 |
| EPS cơ bản (đồng/cp, đã trừ quỹ khen thưởng phúc lợi) | B02-70 | 4.028 | 4.022 |
| Tiền và tương đương tiền / Đầu tư nắm giữ đến ngày đáo hạn ngắn hạn | B01-110 / B01-123 | 1.794,9 / 21.354,4 | 2.225,9 / 23.259,8 |
| Tổng tài sản / Nợ phải trả / Vốn chủ sở hữu | B01-270 / 300 / 400 | 53.312,4 / 18.829,4 / 34.483,0 | 55.049,1 / 18.874,7 / 36.174,4 |
| Vay ngắn hạn / Vay dài hạn | B01-320 / 338 | 9.393,7 / 62,9 | 9.115,4 / 157,9 |
| Lưu chuyển tiền thuần từ HĐKD (CFO) / Tiền chi mua sắm TSCĐ (CapEx) | B03-20 / B03-21 | 8.668,1 / (1.762,0) | 9.685,9 / (1.741,5) |
| Tiền thu lãi tiền gửi và cổ tức (HĐĐT) / Cổ tức đã trả (HĐTC) | B03-27 / B03-36 | 1.428,9 / (11.264,5) | 1.473,1 / (8.159,6) |

`PHÉP_TÍNH` Bốn phép kiểm thực chiến trên báo cáo VNM 2025:
1. **EPS và Quỹ khen thưởng, phúc lợi (Thuyết minh VI.11):** Lợi nhuận thuộc cổ đông phổ thông `9.410,2 tỷ`, trừ trích quỹ khen thưởng phúc lợi `992,8 tỷ`, còn `8.417,4 tỷ`; chia `2.089.955.445` cổ phiếu ra EPS **`4.028 đồng/cp`**. Nếu tự lấy mã 61 chia số cổ phiếu sẽ ra `4.503 đồng/cp` (lệch `11,8%`).
2. **Tỷ lệ chuyển hóa tiền mặt (`CFO / LNST`):** Tính thô `8.668,1 / 9.413,6 = 92,1%`. Nếu cộng lại tiền thu lãi tiền gửi và cổ tức (`1.428,9 tỷ` ở B03-27): `(8.668,1 + 1.428,9) / 9.413,6 = 107,3%`.
3. **Ba biến thể `EBIT`:** (a) `EBIT` xấp xỉ = `11.650,0 + 325,8 = 11.975,8 tỷ` (`ICR = 36,8x`); (b) Loại doanh thu tài chính = `11.975,8 − 1.496,9 = 10.478,9 tỷ` (`ICR = 32,2x`); (c) `EBIT` cốt lõi (loại thêm lỗ liên kết và lỗ khác) = `10.478,9 + 150,6 + 9,8 = 10.639,3 tỷ`.
4. **Đối chiếu cột phân loại lại sang mẫu TT 43 (Q2/2026):** Tại cột `01/01/2026 (đã phân loại lại)`, tổng tài sản `53.312,4 tỷ` chuyển sang **mã 280**, vay ngắn hạn `9.393,7 tỷ` chuyển sang **mã 321**, và phải trả cổ tức tách riêng ra **mã 313**.

## 6. Năm câu hỏi khi mở một báo cáo Việt Nam

1. Góc phải mẫu biểu ghi "Ban hành theo Thông tư số" mấy (`200/202` hay `99/43`), và là báo cáo riêng hay hợp nhất?
2. Ý kiến kiểm toán/soát xét là chấp nhận toàn phần hay ngoại trừ?
3. Lợi nhuận dùng tính P/E đã lấy đúng mã 61 và kiểm tra phần trích quỹ khen thưởng phúc lợi chưa?
4. Khi tính `EBIT`, đã cộng chi phí lãi vay vào mã 50 và tách doanh thu tài chính chưa?
5. Thuyết minh có cam kết thuê hoạt động lớn (VAS 06) và phân bổ lợi thế thương mại (mã 02 trên B03) không?

## 7. Bài tập

`KỊCH_BẢN` Trừ Bài 6 và Bài 10 dùng số thật của VNM, các bài khác dùng số giả định (đơn vị: tỷ đồng). Hãy tự giải toàn bộ 10 bài trước khi mở Đáp án:

1. **Xác định văn bản chế độ kế toán:** Doanh nghiệp có năm tài chính theo năm dương lịch (trừ câu d). Bạn đọc: (a) báo cáo riêng năm 2025; (b) báo cáo hợp nhất bán niên 2026; (c) báo cáo riêng năm 2026; (d) báo cáo riêng quý II của niên độ bắt đầu `01/10/2025` (kết thúc `31/03/2026`). Mỗi báo cáo áp dụng thông tư nào và kiểm chắc ở đâu?
2. **Định vị mã số cũ và mới:** Trên **mẫu mới (TT 99 / TT 43)**, tổng tài sản, vay ngắn hạn và lợi nhuận sau thuế chưa phân phối nằm ở mã nào? Trên **mẫu cũ (TT 200 / TT 202)** là mã nào?
3. **Dựng `EBIT` từ B02 mẫu mới:** Mẫu mới có mã 20 = 500; mã 22 (doanh thu tài chính) = 60; mã 23 (chi phí tài chính) = 90, trong đó mã 24 (chi phí đi vay) = 70; mã 25 = 120; mã 26 = 80; không có mã 21 và 27; mã 40 = 10. Tính mã 30, mã 50, `EBIT` xấp xỉ và `EBIT` loại doanh thu tài chính.
4. **Bẫy mã 270 trên báo cáo năm 2026:** Một người lấy mã 270 trên báo cáo năm 2026 của doanh nghiệp X được `1.200` và tính `ROA = 240 / 1.200 = 20%`, trong khi mã 280 là `6.000`. Tính `ROA` đúng và giải thích lỗi.
5. **Tính `FCF` và `FCFF` nhanh trên báo cáo VAS:** Báo cáo VAS có B03-20 (`CFO`) = 400; B03-21 (`CapEx`) = −150; B03-14 (chi phí đi vay đã trả) = −50; thuế suất 20%. Tính `FCF` hẹp và `FCFF` nhanh. Vì sao được cộng lại lãi vay sau thuế?
6. **Tính tỷ số trên số thật VNM 2025:** Dùng bảng mục 5, tính: (a) biên lợi nhuận sau thuế; (b) tỷ lệ nợ phải trả / vốn chủ; (c) tốc độ tăng doanh thu thuần 2025 so với 2024. Nêu một điều chưa kết luận được từ ba số này.
7. **So sánh Nợ ròng/EBITDA giữa VAS và IFRS 16:** Doanh nghiệp A (VAS) và B (IFRS) cùng ngành bán lẻ, cùng thuê toàn bộ cửa hàng. A có `Nợ vay ròng/EBITDA = 1,0x`; B có `3,0x` (đã gộp nợ thuê). Chỉ ra lỗi nếu kết luận "A an toàn gấp ba B" và nêu cách điều chỉnh.
8. **Bẫy lấy mã 30 làm `EBIT`:** "Lợi nhuận thuần từ hoạt động kinh doanh (mã 30) là 800, đó chính là EBIT nên hệ số trả lãi = 800 / chi phí lãi vay." Chỉ ra lỗi và cách sửa.
9. **Điều chỉnh phân bổ Lợi thế thương mại (`Goodwill`) khi so sánh quốc tế:** Tập đoàn P (lập theo VAS) có lợi nhuận trước thuế `1.000 tỷ đồng`, chi phí lãi vay `100 tỷ đồng`, khấu hao TSCĐ `200 tỷ đồng` và chi phí phân bổ lợi thế thương mại 10 năm nằm trong chi phí quản lý doanh nghiệp là `80 tỷ đồng`. Hãy tính `EBIT` trước phân bổ lợi thế thương mại (tương đương chuẩn IFRS không phân bổ goodwill) và `EBITDA` của Tập đoàn P.
10. **Kiểm chứng ảnh hưởng của phân loại lại Tài sản sinh học lên Số ngày tồn kho (`DIO`):** Trên BCTC của VNM, hàng tồn kho tại `31/12/2025` theo mẫu cũ (gồm cả đàn bò) là `6.839,3 tỷ đồng`, nhưng theo cột `01/01/2026 (đã phân loại lại)` sau khi tách tài sản sinh học ra dòng riêng là `6.530,0 tỷ đồng`. Với giá vốn năm 2025 là `37.436,4 tỷ đồng` (năm tính 365 ngày), hãy tính `DIO` theo hai con số tồn kho này và giải thích vì sao không được ghép số năm 2026 (mẫu mới) với số năm 2025 (chưa phân loại lại) khi chạy [earnings_quality.py](../practice/models/earnings_quality.py).

## 8. Đáp án

1. **Văn bản áp dụng:** (a) TT 200/2014; (b) TT 43/2026; (c) TT 99/2025; (d) vẫn TT 200/2014 vì năm tài chính bắt đầu **trước** `01/01/2026`. Kiểm chắc bằng dòng "Ban hành theo Thông tư số…" ở góc phải mẫu biểu.
2. **Mã số cũ và mới:** Mẫu mới: tổng tài sản **280**, vay ngắn hạn **321**, LNST chưa phân phối **420**. Mẫu cũ: **270**, **320**, **421**.
3. **Dựng `EBIT` từ B02 mẫu mới:** `PHÉP_TÍNH` Mã 30 = `500 + (60 − 90) − (120 + 80) = 270`. Mã 50 = `270 + 10 = 280`. `EBIT` xấp xỉ = `280 + 70 = 350`. `EBIT` loại doanh thu tài chính = `350 − 60 = 290`.
4. **Bẫy mã 270:** `PHÉP_TÍNH` `ROA` đúng = `240 / 6.000 = 4,0%`. Trên mẫu TT 99/TT 43, tổng tài sản là mã **280**, còn mã 270 chỉ là "tài sản dài hạn khác".
5. **Tính `FCF` và `FCFF` nhanh:** `PHÉP_TÍNH` `FCF` hẹp = `400 − 150 = 250`. `FCFF` nhanh = `400 + 50 × (1 − 0,2) − 150 = 290`. Được cộng lại lãi vay sau thuế vì trên B03 của VAS, lãi vay đã trả (mã 14) đã bị trừ trong `CFO`.
6. **Số thật VNM 2025:** `PHÉP_TÍNH` (a) Biên LNST = `9.413,6 / 63.645,9 = 14,8%`; (b) Nợ phải trả / Vốn chủ = `18.829,4 / 34.483,0 = 0,55 lần`; (c) Tăng trưởng doanh thu = `63.645,9 / 61.782,6 − 1 = +3,0%`. `SUY_LUẬN` Chưa kết luận được tăng trưởng do giá hay sản lượng và cổ phiếu đang đắt hay rẻ.
7. **So sánh VAS và IFRS 16:** `SUY_LUẬN` A lập theo VAS nên thuê cửa hàng (thuê hoạt động) nằm ngoài bảng cân đối; B lập theo IFRS 16 đã vốn hóa nợ thuê vào tổng nợ. Muốn so sánh phải cộng giá trị hiện tại của cam kết thuê hoạt động vào nợ của A (và cộng chi phí thuê vào EBITDA của A).
8. **Bẫy lấy mã 30 làm `EBIT`:** `SUY_LUẬN` Mã 30 đã trừ chi phí lãi vay và cộng doanh thu tài chính. Cách sửa: `EBIT ≈ Mã 50 + Chi phí lãi vay (mã 23 cũ / 24 mới) − Doanh thu tài chính (nếu tính EBIT hoạt động)`.
9. **Điều chỉnh phân bổ Goodwill:** `PHÉP_TÍNH` `EBIT` theo báo cáo VAS = `1.000 + 100 = 1.100 tỷ đồng`. `EBIT` tương đương IFRS (cộng lại phân bổ goodwill `80 tỷ`) = `1.100 + 80 = 1.180 tỷ đồng`. `EBITDA` = `1.100 + 200 (khấu hao) + 80 (phân bổ goodwill) = 1.380 tỷ đồng`.
10. **Ảnh hưởng phân loại lại Tài sản sinh học lên `DIO`:** `PHÉP_TÍNH` `DIO` theo số cũ (`6.839,3 tỷ`) = `(6.839,3 / 37.436,4) × 365 ≈ 66,68 ngày`; `DIO` theo số đã phân loại lại (`6.530,0 tỷ`) = `(6.530,0 / 37.436,4) × 365 ≈ 63,66 ngày` (lệch `3,02 ngày` chỉ do tách đàn bò sang mã tài sản sinh học!). Vì vậy khi tính biến động tồn kho qua hai năm 2025–2026 trên [earnings_quality.py](../practice/models/earnings_quality.py), bắt buộc phải lấy số đầu năm 2026 từ cột "đã phân loại lại".

## 9. Đáp án phần ôn bài cũ

1. `Tài sản = Nợ phải trả + Vốn chủ sở hữu`.
2. `EBIT` chưa trừ chi phí lãi vay; lợi nhuận trước thuế đã trừ.
3. Tài sản quyền sử dụng (`Right-of-use asset`) và Nợ thuê (`Lease liability`).
4. Nếu lãi vay đã trả nằm ở dòng tiền tài chính (như IFRS 18) thì `CFO` chưa trừ lãi vay; cộng lại sẽ bị tính trùng.

## Bài làm với dữ liệu thiếu hoặc lệch

Khi xử lý chuỗi dữ liệu lịch sử 2024–2026 của doanh nghiệp Việt Nam, bạn chắc chắn gặp hai hiện tượng dữ liệu lệch giữa các kỳ:
1. **Dịch chuyển mã số và phân loại lại số dư đầu kỳ khi chuyển từ TT 200/202 sang TT 99/43:** Số dư cuối năm 2025 trên báo cáo kiểm toán 2025 khác với số dư đầu năm 2026 (`01/01/2026 đã phân loại lại`) trên báo cáo năm 2026 ở các dòng Hàng tồn kho, Tài sản cố định, Tài sản sinh học, Phải trả cổ tức.
2. **Thiếu dòng "Chi phí đi vay" trên các bảng tóm tắt dữ liệu tự động:** Nhiều phần mềm dữ liệu tài chính chỉ lấy dòng "Chi phí tài chính" (mã 22 cũ / 23 mới) mà bỏ sót dòng con "Trong đó: chi phí lãi vay / chi phí đi vay" (mã 23 cũ / 24 mới).

**Quy trình xử lý chuẩn Bậc S:**
- **Bước 1 — Dùng cột "Số đầu năm (đã phân loại lại)" trên báo cáo năm 2026 khi tính tốc độ tăng trưởng hoặc vòng quay năm 2026:** Tuyệt đối không lấy cột cuối năm 2025 từ báo cáo cũ ghép trực tiếp với cột cuối năm 2026 theo mã số.
- **Bước 2 — Mở trực tiếp B02 và B03 để lấy đúng cặp Lãi vay và Lãi tiền gửi:** Kiểm tra chéo giữa `B02 mã 23/24` (chi phí lãi vay hạch toán), `B03 mã 14` (tiền lãi vay thực trả) và `B03 mã 27` (tiền lãi tiền gửi và cổ tức thực thu) như đã lập trình trong mô hình [earnings_quality.py](../practice/models/earnings_quality.py). Nếu báo cáo tóm lược quý (`B 01b/02b-DN`) không tách chi tiết một khoản mục, hãy mở Thuyết minh `B 09a-DN` hoặc gắn nhãn `CHƯA_BIẾT`.

## Sai ở đâu

### Sai lầm 1: Quét dữ liệu tự động theo mã `270` cho báo cáo năm 2026 và tưởng đó là Tổng tài sản
- **Bối cảnh:** Một nhà đầu tư dùng script Excel/Python cũ lấy ô `Mã 270` trên BCTC quý II/2026 của Vinamilk (`2.049,4 tỷ đồng`) làm Tổng tài sản thay vì `Mã 280` (`53.312,4 tỷ đồng`).
- **Sai ở đâu:** Không cập nhật thay đổi biểu mẫu của Thông tư 99/2025/TT-BTC và Thông tư 43/2026/TT-BTC (trong đó các dòng tài sản sinh học mới đẩy Tổng tài sản từ mã `270` xuống mã `280`).
- **Cách sửa:** Luôn kiểm tra tên chỉ tiêu kèm dòng "Ban hành theo Thông tư số…" ở góc phải biểu mẫu và kiểm chứng phương trình `Tổng tài sản (mã 280) = Tổng nguồn vốn (mã 440)`.

### Sai lầm 2: Lấy dòng "Lợi nhuận thuần từ hoạt động kinh doanh" (Mã 30) trên báo cáo VAS làm `EBIT`
- **Bối cảnh:** Khi tính hệ số khả năng trả lãi (`ICR = EBIT / Chi phí lãi vay`) hoặc `EV/EBIT`, người viết lấy luôn con số ở Mã 30 chia cho chi phí lãi vay.
- **Sai ở đâu:** Trên mẫu B02 của Việt Nam, Mã 30 đã **cộng doanh thu tài chính** và **trừ chi phí tài chính (bao gồm cả chi phí lãi vay)**. Với công ty nhiều tiền gửi như VNM (doanh thu tài chính `1.496,9 tỷ` lớn gấp 4,6 lần chi phí lãi vay `325,8 tỷ`), Mã 30 bị phóng đại bởi lãi tiền gửi; ngược lại với công ty vay nợ lớn, Mã 30 đã bị trừ sẵn lãi vay.
- **Cách sửa:** Tự dựng `EBIT` từ `Mã 50 (Lợi nhuận trước thuế) + Chi phí lãi vay (Mã 23 cũ / 24 mới)` và tách riêng doanh thu tài chính khi đánh giá mảng kinh doanh cốt lõi.

### Sai lầm 3: Lấy `Mã 61 / Số cổ phiếu` làm `EPS` mà quên phần trích Quỹ khen thưởng, phúc lợi
- **Bối cảnh:** Nhà đầu tư tự chia `LNST thuộc cổ đông công ty mẹ` của VNM (`9.410,2 tỷ đồng`) cho `2,09 tỷ cổ phiếu` ra `EPS = 4.503 đồng`, rồi kết luận báo cáo của công ty tính sai khi ghi `EPS = 4.028 đồng`.
- **Sai ở đâu:** Quên quy định kế toán Việt Nam yêu cầu trừ phần lợi nhuận trích lập **Quỹ khen thưởng, phúc lợi** (khoản tiền chia cho người lao động, không thuộc về cổ đông phổ thông — với VNM năm 2025 là `992,8 tỷ đồng`) khỏi tử số trước khi tính `EPS`.
- **Cách sửa:** Luôn đọc Thuyết minh "Lãi trên cổ phiếu" và dùng `EPS` sau trích quỹ khen thưởng, phúc lợi khi tính `P/E` thực tế cho cổ đông.

## Kiểm tra chuyển bài

Trước khi áp dụng bài `N3` vào chuỗi bài phân tích dòng tiền, nợ vay và định giá ([Bài 004](004-cash-flow-truth.md), [Bài 005](005-debt-liquidity-survival.md), [Bài 009](009-valuation-multiples.md)), hãy trả lời 3 câu hỏi dưới đây:

1. **Chuyển giao sang Phân tích Dòng tiền ([Bài 004](004-cash-flow-truth.md) & [earnings_quality.py](../practice/models/earnings_quality.py)):** Vì sao đối với một doanh nghiệp Việt Nam có lượng tiền gửi có kỳ hạn rất lớn (như `VNM` với `21.354,4 tỷ đồng` ở mã `B01-123`), tỷ số `CFO / LNST` tính thô luôn thấp hơn thực tế chuyển hóa tiền mặt, và bạn cần lấy thêm mã nào trên `B03` để điều chỉnh?
2. **Chuyển giao sang Phân tích Nợ vay ([Bài 005](005-debt-liquidity-survival.md)):** Trên báo cáo năm 2026 theo mẫu mới (TT 99 / TT 43), để tính Tổng nợ vay chịu lãi (`Total Debt`), bạn phải cộng hai mã số nào trên `B01`?
3. **Chuyển giao sang Định giá Bội số ([Bài 009](009-valuation-multiples.md)):** Khi so sánh bội số `EV/EBITDA` và `P/E` của một tập đoàn bán lẻ Việt Nam (lập theo VAS) với một tập đoàn bán lẻ khu vực (lập theo IFRS), bạn phải thực hiện tối thiểu 3 bút toán điều chỉnh nào (về thuê hoạt động, phân bổ lợi thế thương mại và quỹ khen thưởng phúc lợi)?

## 11. Ranh giới an toàn

- Bài này **không** phải khuyến nghị mua/bán/nắm giữ VNM hay bất kỳ mã nào; số VNM chỉ dùng để luyện đọc mẫu biểu.
- Không áp dụng mẫu `B01-DN / B02-DN / B03-DN` của bài này cho ngân hàng, bảo hiểm, chứng khoán (xem [Bài 013](013-financial-institutions-wear-hats.md), [F4](F4-vietnam-bank-analysis.md), [F8](F8-insurance-float-actuarial.md)).

## 13. Nguồn Internet đã mở

Mở ngày `2026-10-26` và kiểm tra đối chiếu `2026-11-05`:

| Nguồn | Loại | Ngày ban hành / xuất bản | Dùng cho |
|---|---|---|---|
| [Thông tư 99/2025/TT-BTC (PDF, LuatVietnam)](https://static3.luatvietnam.vn/uploaded/others/2025/10/30/tt99_3010133637.pdf) | Văn bản gốc (bản sao) | 27/10/2025 | Hiệu lực `01/01/2026`, thay thế TT 200, phạm vi, Điều 17 (tên mẫu, không đánh lại mã), Điều 24.6 |
| [KPMG Việt Nam — Điểm nổi bật TT 99](https://kpmg.com/vn/vi/insights/2025/11/key-changes-in-vietnamese-accounting-system-for-enterprises.html) | Big4, thứ cấp | 25/11/2025 | Đổi tên "Báo cáo tình hình tài chính" |
| [MISA — So sánh biểu mẫu TT 99 và TT 200](https://amis.misa.vn/251687/so-sanh-ve-bieu-mau-bao-cao-tai-chinh-giua-thong-tu-99-va-thong-tu-200/) | Thứ cấp | 31/10/2025 | Dòng mới mã 21 (B02), các mã dịch chuyển |
| [LuatVietnam — Thông tư 43/2026/TT-BTC](https://luatvietnam.vn/tai-chinh/thong-tu-43-2026-tt-btc-sua-doi-bao-cao-tai-chinh-hop-nhat-hieu-luc-20-04-2026-432924-d1.html) & [Tạp chí Kinh tế – Tài chính](https://tapchikinhtetaichinh.vn/quy-dinh-moi-ve-phuong-phap-lap-va-trinh-bay-bao-cao-tai-chinh-hop-nhat-theo-thong-tu-so-43-2026-tt-btc-mot-so-ham-y-quan-tri-161827.html) | Thứ cấp / Tạp chí Bộ Tài chính | 20/04/2026 & 18/07/2026 | Mẫu hợp nhất mới (mã 279, mã 27) |
| [VNM — BCTC hợp nhất kiểm toán 2025](https://d8um25gjecm9v.cloudfront.net/cms/20260227_BCTC_KIEM_TOAN_2025_HOP_NHAT_VN_94f1e76e45.pdf) | **Nguồn gốc** (VAS/TT 202) | 27/02/2026 | Bảng mục 5; mã cũ; phân bổ lợi thế thương mại; EPS sau quỹ khen thưởng phúc lợi |
| [VNM — BCTC hợp nhất soát xét Q1/2026](https://d8um25gjecm9v.cloudfront.net/cms/20260429_VNM_BCTC_DA_SOAT_XET_Q1_2026_HOP_NHAT_VN_d44326741a.pdf) & [Q2/2026](https://d8um25gjecm9v.cloudfront.net/cms/20260730_VNM_BCTC_da_soat_xet_Q2_2026_Hop_nhat_76ef2e29c1.pdf) | **Nguồn gốc** (mẫu TT 43) | 29/04/2026 & 30/07/2026 | Mã mới hợp nhất (`150`, `230–280`, `313`, `321`); cột "đã phân loại lại" |
| [VNM — BCTC riêng soát xét Q2/2026](https://d8um25gjecm9v.cloudfront.net/cms/20260730_VNM_BCTC_da_soat_xet_Q2_2026_Rieng_936c679432.pdf) | **Nguồn gốc** (mẫu TT 99) | 30/07/2026 | Mã mới báo cáo riêng (`280`, `321`, `420`) |
| [Quyết định 345/QĐ-BTC](https://luatvietnam.vn/tai-chinh/quyet-dinh-345-qd-btc-2020-de-an-ap-dung-chuan-muc-bao-cao-tai-chinh-181513-d1.html) & [Thời báo Tài chính Việt Nam — 42 VFRS](https://thoibaotaichinhvietnam.vn/chinh-thuc-trien-khai-xay-dung-42-chuan-muc-bao-cao-tai-chinh-viet-nam-205280.html) | Văn bản / Báo Bộ Tài chính | 16/03/2020 & 13/10/2026 | Lộ trình IFRS và kế hoạch 42 chuẩn mực VFRS |
| [Tạp chí Quản lý Nhà nước — VAS 06 và IFRS 16](https://www.quanlynhanuoc.vn/?p=59652) | Bài học thuật | 17/03/2026 | Khác biệt kế toán thuê tài sản giữa VAS 06 và IFRS 16 |
| [BDO — IFR Bulletin 2026/05](https://www.bdo.global/getmedia/d27359ee-5875-45ff-9d36-18b8aa59c8fd/IFRB_2026_05.pdf?ext=.pdf) & [AASB — IAS 7](https://standards.aasb.gov.au/node/6600) | Chuẩn mực / Thứ cấp | 08/2026 | Phân loại lãi vay và cổ tức theo IFRS 18 / IAS 7.34A |
| [Cổng công bố thông tin UBCKNN](https://congbothongtin.ssc.gov.vn/) | Cơ quan quản lý | — | Tra cứu BCTC doanh nghiệp đại chúng |
