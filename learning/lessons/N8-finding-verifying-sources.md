# Bài N8 — Từ câu hỏi tới bằng chứng: Cách tìm, đọc và kiểm chứng nguồn dữ liệu

- Ngày cập nhật: `2026-11-06`
- Chốt dữ liệu lúc: `2026-11-06 10:12 UTC+7 (Asia/Ho_Chi_Minh)`
- Bậc chiều sâu: `Bậc S`
- Lộ trình đọc: **Bài 5 / 23 của Nhánh 1 (Hiểu doanh nghiệp & Phân tích cổ phiếu)**.
  - **Bài trước liên quan:** [Bài N2 — Đọc từng dòng ba báo cáo tài chính](N2-statement-line-items.md) (Bước 4/23) và [Bài 001 — Một doanh nghiệp đi qua ba báo cáo tài chính](001-business-financial-statements.md) (Bước 3/23).
  - **Học tiếp theo đúng thứ tự:** [Bài N3 (Phần A) — Tìm đường trên báo cáo Việt Nam](N3-vietnam-vas-statements.md#phần-a--tìm-đường-trên-báo-cáo-sau-n2) (Bước 6/23), sau đó tới [Bài 002 — Ba câu hỏi trước khi gọi cổ phiếu rẻ](002-finding-a-cheap-stock.md) (Bước 7/23).
- Mục tiêu: Biến câu hỏi mơ hồ thành câu hỏi kiểm chứng được bằng số liệu; tìm đúng hồ sơ gốc của doanh nghiệp và cơ quan quản lý; phân biệt **Báo cáo riêng (công ty mẹ)** với **Báo cáo hợp nhất (toàn tập đoàn)**, **Kỳ báo cáo** với **Ngày công bố**, và **Nguồn gốc** với **Nguồn sao chép lại**; ghi lại "địa chỉ nguồn" chuẩn xác.
- Thời lượng: Ba phiên học ngắn + thực hành đối chiếu trên [`practice/models/data_pull.py`](../practice/models/data_pull.py) và [`practice/models/hpg_fy2025_transcription.csv`](../practice/models/hpg_fy2025_transcription.csv).
- Câu hỏi cốt lõi: **Làm sao biết một con số tài chính lấy từ đúng hồ sơ gốc, đúng đơn vị, đúng kỳ kế toán và chưa bị bóp méo?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

---

## Hiểu bài này trong 1 phút

Một con số tài chính không rõ nguồn gốc giống như hộp sữa không có tên hãng sản xuất và hạn sử dụng. Trước khi bấm máy tính chia bất kỳ tỷ số nào ngoài đời thực, bạn phải đi qua **3 chốt chặn kiểm nguồn**:
1. **Tìm tận gốc nơi phát sinh con số (`Primary Source`):** Nếu 10 trang báo cùng chép lại một thông cáo báo chí, đó vẫn chỉ là **1 nguồn tin được nhân bản 10 lần**, không phải 10 bằng chứng độc lập! Hãy mở trực tiếp báo cáo tài chính đã kiểm toán hoặc hồ sơ tại sở giao dịch / Ủy ban Chứng khoán.
2. **Kiểm tra "chứng minh thư" 6 dòng của con số:** (a) Pháp nhân nào; (b) Báo cáo riêng hay Báo cáo hợp nhất; (c) Kỳ kế toán nào và công bố ngày nào; (d) Đơn vị tiền tệ (đồng, triệu đồng hay tỷ đồng); (e) Chuẩn kế toán nào; (f) Có bản đính chính / phân loại lại nào không.
3. **Tách bạch "Dữ kiện trong nguồn" với "Suy luận của người đọc":** Báo cáo xác nhận sự thật *"Doanh thu tăng 15%"*; còn lý do *"nhờ khách hàng yêu thích thương hiệu"* là suy luận cần kiểm tra thêm.

---

## Ôn bài cũ hoặc kiểm tra đầu vào

Ôn lại kiến thức từ [Bài N2 — Đọc từng dòng ba báo cáo tài chính](N2-statement-line-items.md) trước khi mở báo cáo Việt Nam ở [Bài N3](N3-vietnam-vas-statements.md):

1. **Câu hỏi 1 (từ [Bài N2](N2-statement-line-items.md)):** Báo cáo kết quả kinh doanh đo **trong một kỳ**, còn Bảng cân đối kế toán chụp ảnh **tại một ngày khóa sổ**. Chỉ cần đổi mẫu số từ vốn chủ đầu năm sang cuối năm là `ROE` của Apple đã nhảy từ `196,7%` xuống `151,9%`!
2. **Câu hỏi 2 (cầu nối sang Bài N8):** Nếu hai trang web hiển thị hai con số doanh thu hoặc `ROE` khác nhau cho cùng một cổ phiếu, không được lấy trung bình cộng mà phải mở **báo cáo tài chính gốc do doanh nghiệp công bố** để kiểm tra dòng, kỳ và đơn vị.

## Bài này làm gì và chưa làm gì

| Bài này làm | Bài này chưa làm |
|---|---|
| Dạy cách đặt câu hỏi nghiên cứu cụ thể và truy về tận hồ sơ gốc (`Primary Source`) | Chưa đi vào mã số từng dòng của báo cáo Việt Nam (học ngay ở [Bài N3 — Phần A](N3-vietnam-vas-statements.md#phần-a--tìm-đường-trên-báo-cáo-sau-n2)) |
| Hướng dẫn lập "dòng địa chỉ nguồn" đầy đủ (kỳ, đơn vị, riêng/hợp nhất) | Chưa dạy viết script tải `XBRL/JSON` hàng loạt (học ở [Bài Q4](Q4-getting-data-edgar-xbrl-vietnam.md)) |
| Chỉ ra cách xử lý khi một con số có nhiều phiên bản sửa đổi / đính chính | Không thay thế công việc của kiểm toán viên độc lập |

---

## Phiên 1 — Đặt đúng câu hỏi và Tìm đúng cửa lấy hồ sơ gốc

### 1.1. Đổi câu hỏi mơ hồ thành câu hỏi kiểm chứng được

Người mới bắt đầu thường gõ vào ô tìm kiếm những câu hỏi rất rộng và cảm tính như: *"Cổ phiếu Hòa Phát có tốt không?"* hoặc *"Vinamilk năm nay làm ăn thế nào?"*. Khi hỏi như vậy, bạn sẽ nhận về hàng loạt bài viết quảng cáo, ý kiến khen chê chủ quan hoặc tin đồn không thể kiểm chứng.

`Ý_KIẾN` Trong nghiên cứu có bằng chứng, hãy luôn đổi câu hỏi cảm tính thành **câu hỏi gắn với dữ kiện có địa chỉ kiểm tra được**:

| Câu hỏi mơ hồ (khó kiểm chứng) | Câu hỏi nghiên cứu chuẩn (kiểm chứng được ngay) |
|---|---|
| *"Công ty này làm ăn có tốt không?"* | *"Doanh thu thuần và lợi nhuận sau thuế **hợp nhất** năm tài chính 2025 đã kiểm toán của công ty là bao nhiêu, tính bằng đơn vị gì, và dòng tiền hoạt động (`CFO`) cùng kỳ là bao nhiêu?"* |
| *"Nghe nói công ty này nợ nhiều lắm?"* | *"Tại ngày 31/12/2025 trên Bảng cân đối kế toán hợp nhất, tổng nợ vay ngắn hạn và dài hạn chịu lãi của công ty là bao nhiêu tỷ đồng so với số dư tiền mặt và vốn chủ sở hữu?"* |
| *"Quy định mới có cấm việc này không?"* | *"Văn bản pháp luật số mấy, do cơ quan nào ban hành, có hiệu lực từ ngày tháng năm nào quy định về điều khoản đó?"* |

### 1.2. Bậc thang độ tin cậy của nguồn tin: Đâu là nguồn gốc?

Khi cần tìm số liệu của một doanh nghiệp niêm yết hoặc một quy định thị trường, hãy đi thẳng tới **nguồn gốc có thẩm quyền (`Primary / Authoritative Source`)** thay vì đọc qua trung gian:

1. **Với số liệu và sự kiện của doanh nghiệp:**
   - **Ưu tiên số 1 (Nguồn gốc):** Báo cáo tài chính đã kiểm toán/soát xét, Báo cáo thường niên, Nghị quyết Đại hội đồng cổ đông và Bản cáo bạch do chính doanh nghiệp công bố trên **Cổng công bố thông tin của Ủy ban Chứng khoán / Sở giao dịch chứng khoán** (ví dụ tại Việt Nam là cổng [UBCKNN](https://congbothongtin.ssc.gov.vn/), HOSE, HNX; tại Hoa Kỳ là hệ thống [SEC EDGAR](https://www.sec.gov/edgar/searchedgar/companysearch)) hoặc mục **Quan hệ cổ đông (`Investor Relations — IR`)** trên website chính thức của doanh nghiệp.
   - **Ưu tiên số 2 (Nguồn thứ cấp — chỉ dùng để tham khảo bối cảnh hoặc đối chiếu nhanh):** Các bài báo tài chính, báo cáo phân tích của công ty chứng khoán, hoặc bảng số liệu tổng hợp trên các trang web tài chính. *Quy tắc bắt buộc:* Mọi con số trọng yếu nhìn thấy trên nguồn thứ cấp đều phải được mở lại báo cáo gốc ở Ưu tiên số 1 để xác nhận trước khi dùng!
2. **Tại sao "10 tờ báo cùng đăng một con số" KHÔNG phải là 10 nguồn độc lập?**
   - Hãy hình dung Công ty X phát đi 1 bản thông cáo báo chí có một lỗi đánh máy. Ngay chiều hôm đó, 10 tờ báo điện tử và 5 trang web chứng khoán cùng sao chép nguyên văn bản thông cáo đó.
   - Nếu bạn đọc 3 tờ báo trong số đó và thấy con số giống hệt nhau, bạn **chưa hề kiểm tra chéo hai nguồn độc lập** — bạn chỉ đang đọc 3 bản photocopy của cùng 1 tờ giấy gốc! Hai nguồn chỉ thực sự độc lập khi chúng phát sinh từ hai hệ thống ghi nhận hoặc hai bên kiểm chứng tách biệt (ví dụ: đối chiếu báo cáo của doanh nghiệp với số liệu thống kê hải quan, thuế hoặc báo cáo của đối tác/khách hàng).

> **Điểm dừng Phiên 1:** Hãy tự lấy ví dụ: nếu bạn thấy một bức ảnh chụp bảng tóm tắt tài chính của một công ty được chia sẻ trên mạng xã hội, vì sao bạn không được dùng ngay bức ảnh đó làm bằng chứng kết luận mà phải tìm bản PDF báo cáo tài chính gốc của công ty?

---

## Phiên 2 — "Chứng minh thư" 6 dòng của một con số tài chính

Mỗi khi bạn ghi một con số từ báo cáo ra sổ tay hoặc bảng tính, hãy tập thói quen ghi kèm **6 thông tin định danh** (giống như căn cước công dân của con số đó):

### 2.1. Sáu câu hỏi định danh bắt buộc cho mọi con số

1. **Đúng pháp nhân và mã chứng khoán chưa?**
   - Nhiều tập đoàn có hàng chục công ty thành viên có tên gần giống nhau (ví dụ: Công ty Cổ phần Tập đoàn Hòa Phát — mã `HPG` khác với Công ty TNHH Thép Hòa Phát Hưng Yên; hay Tập đoàn FPT khác với CTCP Bán lẻ Kỹ thuật số FPT — `FRT` và CTCP Viễn thông FPT — `FOX`). Mở nhầm báo cáo của công ty con/công ty liên kết thay vì công ty niêm yết bạn cần phân tích là lỗi rất phổ biến.
2. **Báo cáo Riêng (`Separate / Parent-only`) hay Báo cáo Hợp nhất (`Consolidated`)?**
   - Một tập đoàn lớn thường có **Công ty mẹ** và nhiều **Công ty con** trực tiếp vận hành nhà máy, cửa hàng.
   - **Báo cáo tài chính riêng:** Chỉ ghi nhận hoạt động của riêng pháp nhân công ty mẹ (doanh thu trên báo cáo riêng nhiều khi chỉ là tiền cổ tức từ các công ty con gửi về mẹ!).
   - **Báo cáo tài chính hợp nhất:** Cộng gộp toàn bộ doanh thu, chi phí, tài sản và nợ của công ty mẹ cùng tất cả các công ty con thành một bức tranh chung của cả tập đoàn (sau khi đã loại trừ các giao dịch mua bán nội bộ giữa mẹ và con).
   - `SUY_LUẬN` Khi phân tích cổ phiếu của một tập đoàn, ta **luôn ưu tiên đọc Báo cáo hợp nhất** để thấy toàn bộ hoạt động kinh doanh, và tuyệt đối **không bao giờ lấy trung bình cộng** hay ghép trộn một con số trên báo cáo riêng với một con số trên báo cáo hợp nhất!
3. **Kỳ kế toán (`Reporting Period`) khác với Ngày công bố (`Filing / Publication Date`) như thế nào?**
   - **Kỳ kế toán:** Là khoảng thời gian hoặc thời điểm mà con số đó đo lường (ví dụ: *"Năm tài chính 2025 kết thúc ngày 31/12/2025"* hoặc *"Kết thúc ngày 27/09/2025"* như Apple).
   - **Ngày công bố:** Là ngày báo cáo đó thực sự được ký phát hành và đăng tải lên cổng thông tin cho công chúng biết (ví dụ: báo cáo năm 2025 của Vinamilk được công bố vào ngày `27/02/2026`).
   - *Tại sao phải tách hai ngày này?* Vì vào ngày `31/12/2025`, chưa một nhà đầu tư nào trên thị trường biết được số liệu kiểm toán cả năm 2025! Phải tới ngày `27/02/2026` thị trường mới đọc được báo cáo đó.
4. **Đơn vị tiền tệ và thang đo (`Currency & Scale`) là gì?**
   - Báo cáo Việt Nam thường viết đầy đủ từng **đồng (`VND`)** (ví dụ `63.645.900.000.000 đồng`), trong khi bảng thuyết minh hoặc bản tin tóm tắt lại viết theo **triệu đồng** hoặc **tỷ đồng**. Báo cáo Mỹ (như Apple, Starbucks) thường ghi ở dòng đầu bảng là *(in millions — tính bằng triệu USD)*.
   - `PHÉP_TÍNH` Khi đổi đơn vị, hãy luôn viết rõ phép chia trên giấy hoặc trong công thức bảng tính:
     $$\text{Doanh thu gốc} = 10.100\text{ triệu đồng} \implies \text{Đổi sang tỷ đồng} = \frac{10.100}{1.000} = 10,1\text{ tỷ đồng}$$
     Việc ghi rõ phép chia `/ 1.000` giúp bạn không bao giờ bị lệch 1.000 lần khi ghép hai bảng khác thang đo!
5. **Chuẩn mực kế toán (`Accounting Standard`) đang áp dụng là gì?**
   - Doanh nghiệp lập báo cáo theo Chuẩn mực kế toán Việt Nam (`VAS` — Thông tư 200/202 hoặc Thông tư 99/43), Chuẩn mực quốc tế (`IFRS`) hay Chuẩn mực Hoa Kỳ (`US GAAP`)? (Ta sẽ học cách đối chiếu ngay ở **[Bài N3](N3-vietnam-vas-statements.md)**).
6. **Vị trí chính xác trong tài liệu và Ngày truy cập:**
   - Không chỉ lưu mỗi đường dẫn URL chung chung, hãy ghi rõ: *Trang mấy, Bảng nào, Dòng mã số mấy* và *Ngày bạn mở đọc tài liệu đó*.

### 2.2. Xử lý thế nào khi một con số có nhiều phiên bản sửa đổi / đính chính?

`KỊCH_BẢN` Giả sử khi tra cứu doanh thu hợp nhất năm 2025 của Công ty Sao Biển (cùng một pháp nhân, cùng kỳ năm 2025, cùng phạm vi hợp nhất, đơn vị tỷ đồng), bạn bắt gặp 3 con số khác nhau ở 3 nơi:
1. Một trang web tin tức tổng hợp ghi: **`10,5 tỷ đồng`** (không rõ lấy từ đâu).
2. Báo cáo tự lập quý 4 công bố ngày `20/01/2026` ghi: **`10,2 tỷ đồng`**.
3. Báo cáo tài chính năm đã kiểm toán (hoặc bản đính chính chính thức) công bố ngày `15/03/2026` ghi: **`10,1 tỷ đồng`**.

Bạn phải xử lý 3 con số này theo quy tắc nào?
- **Quy tắc 1 — Tuyệt đối không lấy trung bình cộng `(10,5 + 10,2 + 10,1) / 3`!** Sai số kế toán không phải là phép đo vật lý để lấy trung bình cộng giữa một trang tin không rõ nguồn với báo cáo kiểm toán.
- **Quy tắc 2 — Chọn đúng con số theo câu hỏi bạn đang trả lời:**
  - Nếu câu hỏi là: *"Theo dữ liệu chính thức đã kiểm toán mới nhất hiện nay, doanh thu năm 2025 của công ty là bao nhiêu?"* $\to$ Dùng con số **`10,1 tỷ đồng`** từ báo cáo kiểm toán ngày `15/03/2026`, đồng thời ghi chú lịch sử là bản tự lập trước kiểm toán từng ghi `10,2 tỷ đồng`.
  - Nếu câu hỏi là: *"Vào ngày `01/02/2026` (tức trước khi có báo cáo kiểm toán tháng 3), những người tham gia thị trường lúc đó biết thông tin chính thức gì?"* $\to$ Phải dùng con số **`10,2 tỷ đồng`** của báo cáo đã công bố tại ngày `20/01/2026`. Không được lấy con số ngày `15/03/2026` đem ngược về quá khứ ngày `01/02/2026` để phán xét quyết định lúc đó (lỗi này gọi là **nhìn trước tương lai — `look-ahead bias`**, sẽ học sâu ở **[Bài H5](H5-statistics-backtest-overfitting.md)**).

> **Điểm dừng Phiên 2:** Hãy tự viết ra giấy một dòng nguồn đầy đủ cho con số doanh thu `416.161 triệu USD` của Apple mà bạn đã gặp ở **[Bài 001](001-business-financial-statements.md)**: Tên công ty, tên mẫu hồ sơ, kỳ kết thúc ngày nào, đơn vị tiền tệ, chuẩn kế toán, phạm vi riêng hay hợp nhất?

---

## Phiên 3 — Từ bằng chứng tới kết luận và An toàn khi đọc nguồn Internet

### 3.1. Phân biệt rõ 3 tầng: Số gốc (`SỰ_THẬT`) → Phép tính (`PHÉP_TÍNH`) → Suy luận (`SUY_LUẬN`)

Khi viết một ghi chú học tập hay một báo cáo phân tích doanh nghiệp trong dự án này, chúng ta luôn tách 3 tầng nhận định để không tự đánh lừa mình:
- **Tầng 1 — Số gốc (`SỰ_THẬT`):** *"Theo Báo cáo kết quả kinh doanh hợp nhất FY2025 của Apple (Form 10-K, trang 30), doanh thu thuần năm FY2025 là `416.161 triệu USD`, năm FY2024 là `391.035 triệu USD`."* (Ai mở đúng trang đó ra cũng thấy đúng hai con số này).
- **Tầng 2 — Phép tính tái lập được (`PHÉP_TÍNH`):** *"Tốc độ tăng trưởng doanh thu thuần FY2025 so với FY2024 là `(416.161 − 391.035) / 391.035 = +6,43%`."* (Có công thức và đầu vào rõ ràng, bất kỳ ai bấm máy tính lại cũng ra `+6,43%`).
- **Tầng 3 — Suy luận về nguyên nhân hoặc tương lai (`SUY_LUẬN` / `KỊCH_BẢN`):** *"Doanh thu tăng nhờ khách hàng nâng cấp dòng sản phẩm mới và mảng dịch vụ tăng trưởng bền vững."* Đây là lời giải thích cơ chế kinh tế: một phần có thể kiểm tra tiếp trong thuyết minh doanh thu theo mảng sản phẩm/dịch vụ, nhưng phần dự đoán tương lai luôn mang tính bất định và cần có bằng chứng phản biện.

### 3.2. Khi hai tài liệu chính thức có số khác nhau thì làm sao?

Nếu bạn mở báo cáo năm 2025 thấy "Tổng tài sản ngày 31/12/2025" là một số, nhưng mở báo cáo năm 2026 ở cột "Số đầu năm (01/01/2026)" lại thấy một số hơi khác, **đừng vội áp quy tắc "báo cáo mới nhất luôn thắng" một cách mù quáng!**
- Trước hết, hãy kiểm tra xem định nghĩa chỉ tiêu hoặc chế độ kế toán giữa hai năm có thay đổi làm công ty phải **"phân loại lại (`reclassified`)"** số liệu kỳ trước để so sánh cho cùng mặt bằng hay không (bạn sẽ gặp ví dụ thật cực kỳ thú vị của Vinamilk ngay ở **[Bài N3](N3-vietnam-vas-statements.md)**!).
- Nếu chưa tìm được thuyết minh giải thích vì sao hai số lệch nhau, hãy ghi trung thực là `CHƯA_BIẾT` nguyên nhân chênh lệch và nêu rõ cả hai số kèm nguồn của từng số, tuyệt đối không tự ý bịa số để lấp chỗ trống.

### 3.3. Quy tắc an toàn bắt buộc khi đọc tài liệu trên Internet

Trong thời đại tìm kiếm trực tuyến và dùng công cụ AI hỗ trợ nghiên cứu, bạn cần tuân thủ quy tắc an toàn thông tin:
- Chỉ mở đọc các báo cáo, văn bản pháp규 và dữ liệu bằng thao tác đọc an toàn.
- Nếu một trang web lạ, một tệp tải về hoặc một tài liệu đính kèm yêu cầu bạn **nhập mật khẩu tài khoản chứng khoán, nhập khóa cá nhân (`API key`), cài đặt phần mềm lạ, hoặc chạy một đoạn lệnh/macro trên máy tính** với lý do "để xác minh hoặc mở khóa báo cáo tài chính", hãy coi đó là **dấu hiệu không đáng tin / lừa đảo**, dừng lại ngay lập tức và tìm nguồn chính thức khác (xem thêm tại **[Bài B3 — Bảo mật tài khoản và nhận diện lừa đảo](B3-account-security-scams.md)**).

---

## Ví dụ từ nguồn thật

Hãy xem hệ thống công bố hồ sơ gốc của Ủy ban Chứng khoán Hoa Kỳ (`SEC EDGAR`) phân loại các báo cáo doanh nghiệp như thế nào để bạn tra cứu đúng nơi:

- `SỰ_THẬT` Theo hướng dẫn chính thức của [SEC — Investor.gov: Using EDGAR to Research Investments](https://www.investor.gov/introduction-investing/getting-started/researching-investments/using-edgar-research-investments) (mở kiểm chứng trực tuyến ngày `2026-11-06`, HTTP 200), hệ thống **EDGAR** (*Electronic Data Gathering, Analysis, and Retrieval*) lưu trữ công khai các mẫu hồ sơ chuẩn của doanh nghiệp niêm yết tại Hoa Kỳ:
  1. **Form 10-K:** Báo cáo tài chính và hoạt động thường niên (hàng năm, có kiểm toán độc lập).
  2. **Form 10-Q:** Báo cáo tài chính hàng quý (giữa niên độ, thường được soát xét chứ chưa kiểm toán toàn diện như 10-K).
  3. **Form 8-K:** Báo cáo sự kiện bất thường/quan trọng phát sinh giữa hai kỳ báo cáo (như thay đổi tổng giám đốc, mua bán sáp nhập lớn, thay đổi kiểm toán viên, công bố kết quả kinh doanh).
  4. **Hậu tố `/A` (ví dụ `10-K/A` hoặc `10-Q/A`):** Báo hiệu đây là **bản sửa đổi / bổ sung (`Amendment`)** cho hồ sơ đã nộp trước đó. Khi thấy hậu tố `/A`, người đọc phải mở mục ghi chú đầu hồ sơ (`Explanatory Note`) để xem công ty sửa phần nào (có khi chỉ bổ sung thông tin quản trị, nhưng có khi là sửa lại báo cáo tài chính do phát hiện sai sót — gọi là `Restatement`).
- `SỰ_THẬT` Đối chiếu thực tế trên hồ sơ [Apple Inc. Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) và tệp thực hành [`practice/models/data_pull.py`](../practice/models/data_pull.py):
  - **Tên pháp nhân:** Apple Inc. (Mã CIK trên EDGAR: `0000320193`, mã giao dịch: `AAPL`).
  - **Loại hồ sơ:** `Form 10-K` cho năm tài chính kết thúc ngày `27/09/2025` (`FY2025`), nộp lên SEC ngày `31/10/2025`.
  - **Phạm vi và chuẩn mực:** Báo cáo tài chính hợp nhất (`Consolidated Financial Statements`), lập theo chuẩn `US GAAP`, đơn vị trong các bảng tài chính chính là **triệu USD** (trừ dữ liệu trên mỗi cổ phiếu tính bằng `USD` và số lượng cổ phiếu trong bảng tính bằng **nghìn cổ phiếu**).

---

## Năm câu hỏi khi đọc

Trước khi đưa bất kỳ con số nào vào bài phân tích của mình, hãy điểm qua 5 câu hỏi kiểm tra:
1. **Pháp nhân & Thị trường:** Con số này thuộc về đúng công ty cổ phần niêm yết mà tôi đang nghiên cứu hay thuộc về một công ty con/công ty cùng tên?
2. **Kỳ báo cáo & Ngày công bố:** Con số này đo lường khoảng thời gian nào (hoặc chụp tại ngày nào), và được công bố ra công chúng vào ngày nào?
3. **Đơn vị & Phạm vi:** Đơn vị là đồng, triệu đồng, tỷ đồng hay triệu USD? Là số của Báo cáo hợp nhất hay Báo cáo riêng công ty mẹ?
4. **Phiên bản sửa đổi:** Hồ sơ này là bản tự lập, bản đã kiểm toán, hay đã có bản đính chính (`/A`) hoặc phân loại lại ở kỳ sau?
5. **Ranh giới bằng chứng:** Nguồn gốc chỉ xác nhận con số thực tế được công bố, hay xác nhận luôn cả lời giải thích nguyên nhân do tôi đang suy luận ra?

---

## Bài tập — làm trước khi mở đáp án

Câu 1–4 kiểm tra kỹ năng đổi đơn vị và phân biệt nguồn; câu 5–7 rèn luyện cách ghi địa chỉ nguồn và xử lý nhiều phiên bản dữ liệu; câu 8–10 kết hợp kiểm tra tính toàn vẹn dữ liệu trên bảng tính thực hành.

1. Báo cáo tài chính ghi doanh thu thuần là `10.100 triệu đồng`. Khi đưa vào bảng tóm tắt tính theo đơn vị **tỷ đồng**, con số này bằng bao nhiêu tỷ đồng? Hãy viết rõ phép tính chuyển đổi.
2. Bạn đọc hai trang web tin tức tài chính khác nhau và thấy cả hai trang đều trích dẫn nguyên văn cùng một thông cáo báo chí của Công ty X. Bạn có được tính đây là "hai nguồn độc lập đã kiểm chứng chéo" không? Vì sao?
3. Trên Báo cáo tài chính hợp nhất năm 2025 của Tập đoàn M, doanh thu thuần là `50.000 tỷ đồng`; còn trên Báo cáo tài chính riêng của Công ty mẹ M cùng năm 2025, doanh thu thuần là `12.000 tỷ đồng`. Vì sao hai số này khác nhau, và bạn có được cộng lại chia đôi (`31.000 tỷ đồng`) cho "chắc ăn" không?
4. Trong ví dụ ở Phiên 2 (trang tổng hợp ghi `10,5 tỷ`, báo cáo tự lập ngày 20/01 ghi `10,2 tỷ`, báo cáo kiểm toán ngày 15/03 sửa thành `10,1 tỷ` cho cùng kỳ năm 2025): (a) Nếu hôm nay bạn lập hồ sơ phân tích kết quả năm 2025, bạn chọn số nào? (b) Nếu bạn muốn kiểm tra xem tại ngày `01/02` nhà đầu tư trên thị trường được biết con số chính thức nào, bạn dùng số nào?
5. Hãy viết một dòng địa chỉ nguồn đầy đủ (gồm 7 thành phần: Pháp nhân, Loại tài liệu, Kỳ báo cáo, Ngày nộp/công bố, Chuẩn kế toán, Đơn vị tiền tệ, Phạm vi hợp nhất/riêng) cho báo cáo thường niên `FY2025` của Apple Inc.
6. Khi đang tìm báo cáo tài chính của một công ty trên mạng, bạn thấy một trang web lạ yêu cầu tải về một tệp `.exe` hoặc chạy một dòng lệnh trong cửa sổ Terminal của máy tính để "giải mã bảng số liệu kiểm toán". Bạn xử lý như thế nào?
7. Một bảng báo cáo của công ty Mỹ ghi ở đầu trang là *(in millions, except number of shares, which are reflected in thousands, and per-share amounts)*. Nếu dòng số lượng cổ phiếu bình quân ghi là `15.000.000` và dòng lợi nhuận ròng ghi là `90.000`, hãy đổi cả hai con số này ra đơn vị đầy đủ (cổ phiếu và USD) rồi tính `EPS`.
8. Trên cổng thông tin SEC EDGAR, bạn thấy một công ty nộp hồ sơ `Form 10-K` vào tháng 2, sau đó nộp tiếp hồ sơ `Form 10-K/A` vào tháng 5 cùng năm. Ký hiệu `/A` có ý nghĩa gì, và bạn cần đọc mục nào trong hồ sơ `10-K/A` trước tiên?
9. Khi chép lại bảng cân đối kế toán của một doanh nghiệp (như trong tệp thực hành [`practice/models/hpg_fy2025_transcription.csv`](../practice/models/hpg_fy2025_transcription.csv) và [`practice/models/data_pull.py`](../practice/models/data_pull.py)), làm thế nào để dùng ngay phương trình kế toán của **[Bài N2](N2-statement-line-items.md)** nhằm phát hiện xem mình có gõ nhầm một chữ số hay lệch đơn vị ở dòng nào không?
10. Một bài phân tích viết: *"Theo báo cáo kiểm toán 2025 (trang 8), doanh thu của Công ty Z tăng 25% so với năm 2024; điều này chứng minh sản phẩm của Công ty Z có chất lượng vượt trội và sẽ tiếp tục tăng trưởng 25%/năm trong 5 năm tới."* Hãy tách câu trên thành phần nào là `SỰ_THẬT / PHÉP_TÍNH` được báo cáo kiểm toán xác nhận, và phần nào là `SUY_LUẬN / KỊCH_BẢN` chưa được báo cáo kiểm toán bảo chứng.

## Đáp án và giải thích từng bước

<details>
<summary>Mở sau khi tự làm</summary>

1. **Đáp án câu 1 (`PHÉP_TÍNH`):**
   - Vì `1 tỷ = 1.000 triệu`, ta lấy:
     $$\frac{10.100\text{ triệu đồng}}{1.000} = 10,1\text{ tỷ đồng}$$
2. **Đáp án câu 2 (`SUY_LUẬN`):**
   - **Không.** Hai trang web cùng chép lại một thông cáo báo chí chỉ là hai bản sao của cùng một nguồn gốc duy nhất. Nếu bản thông cáo gốc có sai sót hoặc trình bày một chiều, cả hai trang web đều lặp lại đúng sai sót đó.
3. **Đáp án câu 3 (`SỰ_THẬT` & `SUY_LUẬN`):**
   - Hai con số khác nhau vì chúng đo **hai phạm vi hoàn toàn khác nhau**: Báo cáo riêng chỉ tính riêng pháp nhân công ty mẹ, còn Báo cáo hợp nhất cộng gộp công ty mẹ và tất cả các công ty con (đã loại trừ giao dịch nội bộ).
   - **Tuyệt đối không được cộng lại chia đôi**, vì làm vậy sẽ tạo ra một con số vô nghĩa không đại diện cho công ty mẹ mà cũng chẳng đại diện cho cả tập đoàn.
4. **Đáp án câu 4 (`SUY_LUẬN`):**
   - (a) Để phân tích kết quả thực tế năm 2025 ở thời điểm hiện tại: chọn **`10,1 tỷ đồng`** (số từ báo cáo đã kiểm toán chính thức mới nhất) và ghi chú lịch sử điều chỉnh từ `10,2 tỷ`.
   - (b) Để đánh giá thông tin mà thị trường biết vào ngày `01/02` (trước ngày 15/03 công bố kiểm toán): phải dùng **`10,2 tỷ đồng`** (báo cáo tự lập công bố ngày 20/01) để không mắc lỗi dùng thông tin tương lai phán xét quá khứ.
5. **Đáp án câu 5 (`SỰ_THẬT`):**
   - Pháp nhân: `Apple Inc.` (CIK `0000320193`, mã `AAPL`); Loại tài liệu: `Form 10-K`; Kỳ báo cáo: `Năm tài chính FY2025 kết thúc ngày 27/09/2025`; Ngày nộp SEC: `31/10/2025`; Chuẩn kế toán: `US GAAP`; Đơn vị tiền tệ: `Triệu USD` (trừ số cổ phiếu tính bằng nghìn và số trên mỗi cổ phiếu tính bằng USD); Phạm vi: `Báo cáo tài chính hợp nhất (Consolidated)`.
6. **Đáp án câu 6 (`SỰ_THẬT`):**
   - **Dừng lại ngay lập tức, tuyệt đối không tải hay chạy tệp thực thi/lệnh đó.** Báo cáo tài chính công bố chuẩn chỉ là văn bản đọc trực tiếp (HTML, PDF, XBRL/CSV). Mọi yêu cầu chạy lệnh hoặc nhập thông tin nhạy cảm từ nguồn bên ngoài đều phải coi là nội dung không đáng tin / tấn công mã độc.
7. **Đáp án câu 7 (`PHÉP_TÍNH`):**
   - Số cổ phiếu ghi `15.000.000` theo đơn vị **nghìn cổ phiếu (`in thousands`)** $\to$ Số cổ phiếu thực tế là `15.000.000 × 1.000 = 15.000.000.000 cổ phiếu` (`15 tỷ cổ phiếu`).
   - Lợi nhuận ròng ghi `90.000` theo đơn vị **triệu USD (`in millions`)** $\to$ Lợi nhuận ròng thực tế là `90.000 × 1.000.000 = 90.000.000.000 USD` (`90 tỷ USD`).
   - Tính `EPS`: `90.000.000.000 USD / 15.000.000.000 cổ phiếu = 6,00 USD/cổ phiếu`. *(Nếu không đọc kỹ dòng ghi chú đơn vị ở đầu bảng mà lấy thẳng `90.000 / 15.000.000`, bạn sẽ tính sai gấp 1.000 lần!).*
8. **Đáp án câu 8 (`SỰ_THẬT`):**
   - Hậu tố `/A` (`Amendment`) nghĩa là bản sửa đổi, bổ sung cho báo cáo `10-K` đã nộp trước đó. Bạn cần đọc ngay mục `Explanatory Note` ở đầu hồ sơ `10-K/A` để biết lý do sửa đổi và những bảng/mục nào đã thay đổi.
9. **Đáp án câu 9 (`PHÉP_TÍNH`):**
   - Sau khi nhập số liệu vào bảng tính, luôn đặt công thức kiểm tra đẳng thức tự động: (1) `Tổng Tài sản − (Tổng Nợ phải trả + Vốn chủ sở hữu) == 0`; (2) `Tài sản ngắn hạn + Tài sản dài hạn == Tổng Tài sản`; (3) `Doanh thu thuần − Giá vốn == Lợi nhuận gộp`. Nếu bất kỳ phép trừ kiểm tra nào khác `0`, bảng tính phải báo lỗi ngay để dò lại dòng chép sai.
10. **Đáp án câu 10 (`SUY_LUẬN`):**
    - Phần `SỰ_THẬT / PHÉP_TÍNH`: Doanh thu năm 2025 trên báo cáo kiểm toán tăng 25% so với năm 2024 (cần kiểm tra thêm xem năm 2025 có mua gộp công ty con hay thay đổi kỳ kế toán không).
    - Phần `SUY_LUẬN / KỊCH_BẢN` (chưa được báo cáo kiểm toán chứng minh): Việc gán nguyên nhân tăng doanh thu cho "chất lượng sản phẩm vượt trội" (vì doanh thu có thể tăng nhờ giảm giá mạnh hoặc bán chịu nới lỏng) và lời phóng chiếu "sẽ tiếp tục tăng 25%/năm trong 5 năm tới".

</details>

---

## Bài làm với dữ liệu thiếu hoặc lệch

`KỊCH_BẢN` Bạn đang lập bảng so sánh hai năm 2024 và 2025 của Công ty H từ hai tài liệu khác nhau:
- Cột năm 2024 bạn chép từ một bài báo tóm tắt: ghi `Doanh thu = 15.200` (bài báo quên không ghi đơn vị và không nói là báo cáo riêng hay hợp nhất).
- Cột năm 2025 bạn chép từ Báo cáo tài chính hợp nhất kiểm toán năm 2025: ghi `Doanh thu thuần = 18.500.000 triệu đồng` (tức `18.500 tỷ đồng`).
- Một người nhìn vào hai số `15.200` và `18.500.000` rồi hoảng hốt kết luận doanh thu tăng gấp hơn 1.200 lần; người khác tự ý đoán `15.200` là `15.200 tỷ đồng` rồi tính tốc độ tăng trưởng là `(18.500 − 15.200) / 15.200 = +21,71%`.

**Cách phát hiện và xử lý chuẩn:**
1. **Không tự đoán đơn vị của bài báo cũ:** Bạn không cần và không được lấy con số `15.200` không rõ nguồn/đơn vị từ bài báo đó!
2. **Mở ngay cột so sánh năm trước trên chính Báo cáo tài chính hợp nhất kiểm toán năm 2025:** Trên mọi báo cáo tài chính chuẩn (cả VAS, IFRS lẫn US GAAP), bên cạnh cột `Năm nay (2025)` luôn có sẵn cột `Năm trước (2024)` được trình bày **cùng đơn vị tiền tệ, cùng phạm vi hợp nhất và đã phân loại lại đồng nhất**. Hãy lấy số năm 2024 trực tiếp từ cột so sánh trên báo cáo gốc năm 2025 (hoặc mở báo cáo kiểm toán gốc năm 2024) thay vì dùng số trôi nổi từ bài báo thứ cấp.

---

## Sai ở đâu

Hãy đọc cách làm việc dưới đây và chỉ ra 3 lỗi sai nghiêm trọng về kiểm nguồn:

> *"Để tiết kiệm thời gian nghiên cứu Công ty V, tôi chỉ cần xem bảng chỉ số tài chính tóm tắt trên một ứng dụng điện thoại miễn phí, không cần tải file PDF báo cáo tài chính của công ty. Để kiểm tra chắc chắn hơn, tôi mở thêm 2 ứng dụng điện thoại khác và thấy cả 3 ứng dụng đều ghi P/E và ROE giống nhau, vậy là đã kiểm tra chéo 3 nguồn độc lập! Hơn nữa, vì số liệu đã lên ứng dụng chứng khoán nên chắc chắn công ty không thể có rủi ro kế toán nào."*

**Phân tích 3 lỗi sai:**
1. **Lỗi 1 — Dùng nguồn thứ cấp tự động thay cho hồ sơ gốc:** Các ứng dụng tổng hợp dữ liệu thường dùng phần mềm quét tự động, rất dễ lấy nhầm mã dòng khi biểu mẫu kế toán thay đổi, quên trừ quỹ khen thưởng phúc lợi khi tính `EPS`, hoặc bỏ sót toàn bộ phần **Thuyết minh báo cáo tài chính** (nơi chứa các cam kết nợ, chi tiết tài sản và chính sách kế toán).
2. **Lỗi 2 — Nhầm 3 ứng dụng dùng chung một nhà cung cấp dữ liệu là "3 nguồn độc lập":** Rất nhiều trang web và ứng dụng chứng khoán thực chất mua lại dữ liệu từ cùng một đơn vị cung cấp dữ liệu đầu nguồn (`data vendor`). Khi đầu nguồn tính theo một công thức cố định, cả 3 ứng dụng đều hiện ra cùng một con số; đó không phải là kiểm chứng độc lập.
3. **Lỗi 3 — Nhầm "số liệu đã công bố" với "không có rủi ro kế toán":** Ngay cả báo cáo đã kiểm toán cũng chỉ cung cấp mức bảo đảm hợp lý theo chuẩn mực kế toán, hoàn toàn không bảo đảm mô hình kinh doanh bền vững hay cổ phiếu đang được định giá rẻ.

---

## Kiểm tra chuyển bài

Trước khi mở báo cáo tài chính thật tại Việt Nam ở bài kế tiếp ([Bài N3 — Phần A](N3-vietnam-vas-statements.md#phần-a--tìm-đường-trên-báo-cáo-sau-n2)), hãy tự trả lời 3 câu hỏi sau:

1. Nêu 6 thông tin cần ghi trong "chứng minh thư" của một con số tài chính để người khác truy nguyên lại được.
2. Khi phân tích một tập đoàn có nhiều công ty con, vì sao phải mở **Báo cáo tài chính hợp nhất** thay vì Báo cáo riêng của công ty mẹ?
3. Báo cáo tự lập quý 4 (ngày `25/01/2026`) ghi LNST năm 2025 là `500 tỷ đồng`, nhưng báo cáo kiểm toán (ngày `28/03/2026`) điều chỉnh còn `420 tỷ đồng`. Bạn dùng số nào để đánh giá hiện trạng công ty, và cần kiểm tra gì về mức chênh lệch `−80 tỷ đồng`?

- **Tiêu chí đạt:** (1) Đủ Pháp nhân, Tài liệu/Nơi công bố, Kỳ & Ngày công bố, Đơn vị, Riêng/Hợp nhất, Chuẩn kế toán, Vị trí trang/mã dòng; (2) Báo cáo hợp nhất mới phản ánh toàn bộ doanh thu, tài sản và nợ vay của cả tập đoàn; (3) Dùng số kiểm toán `420 tỷ đồng` và đọc văn bản giải trình chênh lệch `−16%` sau kiểm toán.
- **Điểm đến tiếp theo:** Mở ngay **[Bài N3 (Phần A) — Tìm đường trên báo cáo tài chính Việt Nam](N3-vietnam-vas-statements.md#phần-a--tìm-đường-trên-báo-cáo-sau-n2)** (Bước 6/23 của Nhánh 1)!

---

## Mô hình thực hành

Thực hành kiểm tra tính toàn vẹn khi lấy và chép dữ liệu báo cáo tài chính trong [`practice/models/data_pull.py`](../practice/models/data_pull.py) và [`practice/models/hpg_fy2025_transcription.csv`](../practice/models/hpg_fy2025_transcription.csv) (`python3 -m unittest tests/test_data_pull_models.py`; học sâu hơn tại [Bài Q4](Q4-getting-data-edgar-xbrl-vietnam.md)).

## Ranh giới an toàn

- Bài học này hướng dẫn phương pháp kiểm chứng nguồn dữ liệu, **không phải** khuyến nghị mua, bán hay nắm giữ chứng khoán.
- Không nhập mật khẩu, thông tin tài khoản hay chạy mã thực thi từ các nguồn tài liệu bên ngoài.

## Nguồn Internet đã mở

Các nguồn dưới đây đã được tìm kiếm và mở kiểm chứng trực tiếp (cập nhật ngày `2026-11-06`):

| Nguồn | Kỳ / Phiên bản & Phạm vi | Nội dung xác minh dùng trong bài |
|---|---|---|
| [Investor.gov (SEC) — Using EDGAR to Research Investments](https://www.investor.gov/introduction-investing/getting-started/researching-investments/using-edgar-research-investments) | Hoa Kỳ; trang hướng dẫn chính thức của SEC (`2026-11-06`, HTTP 200) | Phân biệt `Form 10-K`, `Form 10-Q`, `Form 8-K` và bản sửa đổi (`/A`) |
| [Apple Inc. — Form 10-K FY2025 (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Năm tài chính kết thúc `27/09/2025`; nộp `31/10/2025`; `US GAAP`; triệu USD | Thực hành đọc thông tin định danh hồ sơ gốc, kỳ báo cáo, ngày nộp và quy ước đơn vị |
| [Cổng công bố thông tin — UBCKNN](https://congbothongtin.ssc.gov.vn/) | Việt Nam; cổng công bố thông tin chính thức | Nguồn tra cứu báo cáo tài chính của công ty đại chúng tại Việt Nam |
