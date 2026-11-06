# Bài Q4 — Lấy dữ liệu: EDGAR/XBRL, báo cáo Việt Nam và bảng tính

- Ngày viết: `2026-11-01`; sửa sau các vòng kiểm duyệt 1–4 ngày `2026-11-02`.
- Chốt dữ liệu lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Nguồn: trang SEC, `companyfacts` của Apple, BCTC kiểm toán FY2025 của Hòa Phát, bản đăng lại Thông tư 96/2020/TT-BTC; mở `2026-11-01` và `2026-11-02` (bảng cuối bài).
- Mục tiêu: Lấy số từ EDGAR bằng API mà không dính lỗi kỳ, trùng lặp, đơn vị, đổi tag; biết báo cáo Việt Nam nằm ở đâu và vì sao phải chép tay có kiểm; dựng bảng tính có phép kiểm đẳng thức; ghi chỗ chưa biết.
- Bài trước liên quan: Chuỗi định lượng thực hành sau [Bài 012: Kịch bản, biên an toàn và điều kiện bác bỏ](012-scenarios-margin-of-safety.md) (**Bước 1/4 của chuỗi `Q4 → Q2 → Q1 → Q3`**; kế thừa [Bài N8: Tìm và kiểm nguồn](N8-finding-verifying-sources.md), [Bài N3](N3-vietnam-vas-statements.md), [Bài V4](V4-disclosure-and-source-tracing.md) và [Bài 004](004-cash-flow-and-earnings-quality.md)). Học tiếp: [Bài Q2: Cổ phiếu thưởng nhân viên, pha loãng, mua lại và cổ tức](Q2-sbc-dilution-buybacks-dividends.md).
- Thời lượng: 3 phiên.
- Tệp thực hành: [data_pull.py](../practice/models/data_pull.py), [apple_xbrl_subset.json](../practice/models/apple_xbrl_subset.json) và [hpg_fy2025_transcription.csv](../practice/models/hpg_fy2025_transcription.csv); kiểm bằng `python3 -m unittest discover tests`.
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/Q4-fact-check.md), [phản biện](../reviews/Q4-risk-review.md)
- Câu hỏi cốt lõi: **Con số tôi đang cầm có đúng kỳ, đúng đơn vị, đúng khái niệm, và tôi chứng minh được nó đến từ đâu không?**

## Hiểu bài này trong 1 phút

Lấy dữ liệu giống nhặt nấm: quan trọng là biết cái nào ăn được. Một dòng số trông giống nhau dù là cả năm hay chín tháng, đồng hay triệu đồng, số gốc hay đã điều chỉnh. Bài dạy hai nguồn có thật (EDGAR và PDF công ty Việt Nam), chỗ dễ nhầm ở từng nguồn, và cách dựng bảng tính tự báo lỗi.

## Ôn bài cũ hoặc kiểm tra đầu vào

Ôn lại [Bài N8 — Tìm và kiểm nguồn](N8-finding-verifying-sources.md) và [Bài 012 — Kịch bản, biên an toàn và điều kiện bác bỏ](012-scenarios-margin-of-safety.md): vì sao hai trang web chép cùng một thông cáo báo chí không được tính là hai nguồn độc lập?
Bài này dạy gọi API XBRL của SEC, chép và kiểm báo cáo Việt Nam, dựng bảng tính tự báo lỗi, chuẩn bị đầu vào số thật của Apple cho [Bài Q2](Q2-sbc-dilution-buybacks-dividends.md) và Hòa Phát cho [Bài Q1](Q1-earnings-quality-toolkit.md), [Bài Q3](Q3-normalizing-earnings-cyclical.md).

## 1. Ba lớp dữ liệu

| Lớp | Ví dụ | Quy tắc |
|---|---|---|
| Gốc | 10-K của Apple, PDF báo cáo của Hòa Phát | Không sửa; ghi URL, ngày mở, mã băm tệp nếu tải về |
| Có cấu trúc | JSON `companyfacts` của SEC | Là bản máy đọc của số trong tài liệu gốc; kiểm chéo, không thay thế |
| Bảng tính của bạn | CSV, XLSX | Mỗi dòng có nguồn và kỳ; số chuyển đổi nằm ở cột riêng với công thức |

`SUY_LUẬN` Dữ liệu có cấu trúc nhận lỗi của người gắn thẻ và của người đọc; dữ liệu chép tay nhận lỗi gõ. Vì vậy kiểm mỗi số quan trọng độc lập với cách lấy nó.

## 2. EDGAR và API XBRL

`SỰ_THẬT` Trang [SEC — EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) (mở 02/11/2026; trang ghi xem lại 08/04/2025) mô tả các điểm cuối: `submissions` (lịch sử hồ sơ), `companyconcept` (một khái niệm của một công ty) và `companyfacts` (toàn bộ khái niệm của một công ty, mỗi công ty một tệp, đường dẫn dùng mã CIK đệm đủ 10 chữ số), cùng `frames` (một số liệu của nhiều công ty cho một kỳ). Dữ liệu lấy từ các mẫu 10-Q, 10-K, 8-K, 20-F, 40-F, 6-K và biến thể, và chỉ gộp các sự kiện dùng taxonomy không tùy chỉnh (trang viết "e.g." us-gaap, ifrs-full, dei, srt); khái niệm tùy chỉnh (extension) của riêng công ty bị loại. API không cần khóa; độ trễ thường dưới một phút; `companyfacts.zip` được dựng lại hằng đêm khoảng 3 giờ sáng giờ miền Đông, và trang nói ZIP gộp là cách hiệu quả nhất để lấy lượng dữ liệu lớn.

`SỰ_THẬT` Trang [SEC — Accessing EDGAR Data](https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data) (mở 02/11/2026; trang ghi xem lại 26/06/2024), mục "Fair Access": mức tối đa hiện là 10 yêu cầu mỗi giây và SEC có thể hạ mức này; chương trình nên khai User-Agent kèm tên và email liên hệ theo mẫu của SEC (FAQ webmaster); mức 10 yêu cầu/giây áp cho tổng mọi máy của một người dùng và SEC có thể chặn IP vượt mức (developer-resources); SEC không cho botnet hay công cụ tự động cào cả trang; SEC không hỗ trợ gỡ lỗi script. Điều khoản sao chép và ghi nguồn: `CHƯA_BIẾT` (trang khác, chưa mở); hãy ghi nguồn khi đăng lại. `PHÉP_TÍNH` Hàm `fetch_companyfacts` trong [data_pull.py](../practice/models/data_pull.py) bắt buộc User-Agent có tên và email, cách nhau tối thiểu 0,2 giây giữa hai lần gọi (mức tối đa không phải mức nên dùng; biến đếm toàn cục chỉ đúng trong một tiến trình; chưa xử lý lỗi 403/429), có bộ nhớ đệm; test dùng hàm gọi giả. Dùng liên hệ của bạn.

Cấu trúc một tệp `companyfacts`: `facts → us-gaap → <tên tag> → units → <đơn vị> → danh sách bản ghi`. Mỗi bản ghi có `start` và `end` (kỳ; chỉ có `end` nếu là số tại một thời điểm), `val`, `fy`, `fp`, `form`, `filed` và đôi khi `frame`.

## 3. Mười ba cạm bẫy của JSON

| # | Cạm bẫy | Cách xử lý |
|---|---|---|
| 1 | `fy` là năm tài chính của **hồ sơ**, không phải của kỳ: một 10-K nộp năm 2025 mang `fy = 2025` cho cả ba năm so sánh | Chọn theo `start` và `end`, không theo `fy` |
| 2 | Cùng một kỳ xuất hiện trong nhiều hồ sơ | Quy ước tùy mục đích: lấy hồ sơ nộp muộn nhất (`filed`; hòa thì `accn` lớn hơn) hoặc hồ sơ gốc; luôn so cả hai |
| 3 | Số tính bằng đơn vị gốc (USD, cổ phiếu), không phải triệu | Chia khi trình bày; ghi đơn vị ở cột |
| 4 | Công ty đổi tag giữa các thời kỳ | Chọn tag có kỳ mới nhất, không phải tag đầu tiên có dữ liệu |
| 5 | Nhãn `frame` như `CY2025` căn theo lịch, không phải theo năm tài chính | Không dùng frame để suy ra tên năm tài chính |
| 6 | Hồi tố: chia tách cổ phiếu và điều chỉnh làm cùng một kỳ có hai giá trị | Liệt kê kỳ có nhiều giá trị và hiểu nguyên nhân |
| 7 | Số quý 4 không có riêng trong 10-K | Quý 4 = cả năm − chín tháng lũy kế, cùng một cơ sở trình bày (`ytd_value` và `annual_series` dùng cùng quy ước chọn hồ sơ); ghi là suy ra (bộ lọc 350–380 và 265–280 ngày là quy ước cho năm 52/53 tuần) |
| 8 | Cùng một sự kiện có nhiều số (tiền chi, giá trị ghi trong vốn chủ, số trong MD&A) | Ghi từng số kèm khái niệm; không chọn số "đúng" khi chưa biết nguyên nhân |
| 9 | Số tại thời điểm (instant) khác số cả kỳ (duration); quý 4 chỉ suy ra được cho số dòng chảy, không cho số tồn | Kiểm xem bản ghi có `start` không |
| 10 | Khoản mục tùy chỉnh (extension) và số theo phân đoạn không có trong `companyfacts` | Mở tài liệu gốc cho các số đó |
| 11 | Công ty nộp 20-F thường dùng `ifrs-full` (một số dùng `us-gaap`); tiền tệ có thể không phải USD | Đọc khóa taxonomy và đơn vị có trong tệp, đừng mặc định |
| 12 | Một tag có nhiều mảng đơn vị (ví dụ USD và USD/shares) | Chọn đúng đơn vị; kiểm danh sách khóa `units` |
| 13 | 10-K/A và "hồ sơ nộp muộn nhất" chỉ là quy ước | Ghi quy ước đã dùng; hòa `filed` thì so `accn` và `form` |

## Ví dụ từ nguồn thật

### Apple: API khớp với bài Q2, và các cạm bẫy có thật

`SỰ_THẬT` Dữ liệu [`companyfacts` của Apple](https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json) (mã CIK 320193; tôi tải ngày 01/11/2026 và lưu tập con 14 tag, các dòng kết thúc từ 01/09/2018 (ngày sớm nhất thực tế 29/09/2018; tệp đầy đủ còn kỳ FY2016–FY2017 của `Revenues`), ở [apple_xbrl_subset.json](../practice/models/apple_xbrl_subset.json), giữ nguyên giá trị). `PHÉP_TÍNH` Dùng `annual_series` (lọc kỳ 350–380 ngày, lấy hồ sơ nộp muộn nhất) rồi chia 1.000.000, bảy chỉ tiêu dòng tiền và lợi nhuận của ba năm FY2023–FY2025 trùng khớp từng số với bảng ở bài Q2 (ví dụ lợi nhuận ròng 112.010, SBC 12.863, mua lại bằng tiền 90.711 triệu USD). Cổ phiếu cơ bản bình quân cũng khớp: 14.948.500 nghìn.

`SỰ_THẬT` Cạm bẫy 1: với lợi nhuận ròng, các bản ghi `fy = 2025`, kỳ dài hơn 350 ngày, có ba ngày kết thúc khác nhau (30/09/2023, 28/09/2024, 27/09/2025).

`SỰ_THẬT` Cạm bẫy 4: tag `Revenues` của Apple chỉ có một giá trị cả năm trong tập con đã lưu (từ 09/2018), kết thúc 29/09/2018 (265.595 triệu USD); doanh thu sau đó nằm ở `RevenueFromContractWithCustomerExcludingAssessedTax` (FY2025 416.161 triệu USD). Lấy tag đầu tiên có dữ liệu sẽ trả số năm 2018.

`SỰ_THẬT` Cạm bẫy 6: với kỳ kết thúc 28/09/2019, số cổ phiếu đang lưu hành có hai giá trị là 4.443.236.000 và 17.772.945.000; cổ tức công bố mỗi cổ phiếu cùng kỳ có hai giá trị 3 USD và 0,75 USD. `PHÉP_TÍNH` Tỷ lệ `17.772.945.000/4.443.236.000 = 4,000` và `3/0,75 = 4`. `SUY_LUẬN` Có vẻ là một đợt chia tách 4:1 làm hồ sơ sau trình bày lại số cũ; nhãn "4:1" không nằm trong dữ liệu, chỉ tỷ lệ 4 là quan sát. Vì vậy EPS và cổ tức mỗi cổ phiếu nhiều năm phải điều chỉnh trước khi so.

`SỰ_THẬT` Cạm bẫy 7: lợi nhuận ròng cả năm FY2025 là 112.010 triệu USD, lũy kế chín tháng đến 28/06/2025 là 84.544 triệu USD. `PHÉP_TÍNH` Quý 4 FY2025 `= 112.010 − 84.544 = 27.466` triệu USD. `SỰ_THẬT` Phụ lục 99.1 của [8-K quý 4 FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000077/a8-kex991q4202509272025.htm) (mở 02/11/2026) ghi lợi nhuận ròng ba tháng kết thúc 27/09/2025 là 27.466 triệu USD, khớp phép suy ra. Văn bản không nêu ngày công bố, chỉ nêu cuộc gọi kết quả ngày 30/10/2025.

`SỰ_THẬT` Cạm bẫy 8: Apple FY2025 có **ba** số cho việc mua lại cổ phiếu: (i) tiền chi trong báo cáo lưu chuyển tiền tệ, dòng "Repurchases of common stock", 90.711 triệu USD; (ii) dòng "Common stock repurchased" trong báo cáo biến động vốn chủ của [10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) (mở 02/11/2026), 90.052 triệu USD, nằm ở cột lợi nhuận giữ lại (accumulated deficit); (iii) giá trị cổ phiếu mua lại và hủy theo tag `StockRepurchasedAndRetiredDuringPeriodValue` trong `companyfacts`, 89.300 triệu USD (bài Q2 ghi cùng số này từ MD&A). `PHÉP_TÍNH` Chênh (i) − (iii) = 1.411; (i) − (ii) = 659; (ii) − (iii) = 752 (triệu USD). Tập con không chứa thẻ nào có giá trị 90.052 (test kiểm); `SUY_LUẬN` chưa kiểm: số theo thành phần vốn chủ có thể bị loại khỏi `companyfacts`. `CHƯA_BIẾT` vì sao ba số khác nhau (89.300 trong MD&A của 10-K ghi "$89.3 billion", làm tròn 0,1 tỷ nên các chênh lệch với số này có sai số khoảng ±50 triệu; phần 10-K tôi đã đọc không nêu nguyên nhân, phần còn lại chưa đọc). Cách dùng: nêu cả ba kèm khái niệm; cho dòng tiền ưu tiên 90.711 (`Ý_KIẾN`).

### Hòa Phát: tài liệu PDF và cách chép có kiểm

`SỰ_THẬT` [Báo cáo tài chính hợp nhất kiểm toán FY2025 của Hòa Phát](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/03/20260327-hpg-bctc-hop-nhat-nam-2025-sau-kiem-toan.pdf) (8.270.589 byte; SHA-256 `f38c5f75becf7d3f145d27183eec81f119fd4f75e378b983a2763ddc3f7e0c07`, tính trên bản tải ngày 02/11/2026) là PDF ảnh quét: không lấy được chữ, phải đọc từng trang như ảnh (trang PDF = số trang in + 2; bảng cân đối ở trang in 5–7, kết quả kinh doanh trang 8, lưu chuyển tiền tệ trang 9–10). [Bản tổng quan Q3/2026](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/10/tong-quan-tinh-hinh-kinh-doanh-quy3-2026-vn.pdf) cũng là ảnh. Ngược lại [Báo cáo thường niên 2023](https://static2.vietstock.vn/data/HOSE/2023/BCTN/VN/HPG_Baocaothuongnien_2023.pdf) tải từ Vietstock có lớp chữ trích được. 

`PHÉP_TÍNH` Từ các trang đó tôi chép 14 chỉ tiêu hai năm, mỗi dòng có cột `trang_in`, vào [hpg_fy2025_transcription.csv](../practice/models/hpg_fy2025_transcription.csv) (tỷ VND; số gốc VND chia 1 tỷ). Hàm `statement_checks` kiểm năm đẳng thức; cả hai năm đều đạt ở dung sai mặc định 1e-5 tỷ (10.000 đồng; số chép đến nghìn đồng, 6 chữ số thập phân của tỷ). Dung sai 0,01 tỷ (10 triệu đồng) chỉ dùng khi so với số đã làm tròn 0,01 tỷ:

| Đẳng thức | FY2025 (tỷ VND) |
|---|---:|
| Tài sản = nợ phải trả + vốn chủ | `257.899,20 = 126.679,19 + 131.220,01` |
| Tiền cuối năm: bảng cân đối = lưu chuyển tiền tệ | `8.300,89 = 8.300,89` |
| Lợi nhuận sau thuế = trước thuế − thuế hiện hành − thuế hoãn lại | `15.514,93 = 18.040,59 − 2.574,22 − (−48,56)` |
| Lợi nhuận mẹ + không kiểm soát = sau thuế | `15.453,17 + 61,76 = 15.514,93` |
| Lợi nhuận gộp = doanh thu thuần − giá vốn | `24.497,79 = 156.116,09 − 131.618,31` |

`SUY_LUẬN` Năm đẳng thức chỉ kiểm quan hệ giữa các tổng, không kiểm khoản thành phần, nên bảng "báo một số loại lỗi", không phải mọi lỗi; chép thêm các khoản thành phần và kiểm tổng khi cần. Đẳng thức đạt không chứng minh từng ô đúng: hai lỗi bù trừ vẫn qua, và nếu cả ba ô của một đẳng thức cùng sai một đơn vị (đều nhân 1.000) thì đẳng thức vẫn đạt, nên phải kiểm thêm độ lớn so với trang gốc. Đẳng thức hỏng thường báo có lỗi, nhưng không phải lúc nào cũng là lỗi chép: làm tròn từng dòng cũng làm lệch. Ví dụ: báo cáo in bằng đồng (lợi nhuận gộp 24.497.788.183.182); làm tròn từng số sang tỷ thì `156.116,09 − 131.618,31 = 24.497,78`, còn số gộp làm tròn là 24.497,79 (lệch 0,01 do làm tròn, không phải lỗi chép). Đảo chữ số nợ phải trả (126.679,19 thành 126.697,19) làm đẳng thức đầu lệch −18,00 tỷ **khi các ô còn lại đúng**, bốn đẳng thức kia vẫn đạt, nên lỗi khoanh vào bảng cân đối. Ô vốn chủ nhập bằng triệu VND thay vì tỷ VND làm lệch cả nghìn lần; test `test_ban_chep_hpg` kiểm các trường hợp này.

## 4. Báo cáo Việt Nam: ở đâu, khi nào, dạng gì

`SỰ_THẬT` (thứ cấp: nội dung bản đăng lại gốc 2020, chưa hợp nhất) Theo [Thông tư 96/2020/TT-BTC](https://caselaw.vn/van-ban-phap-luat/372205-thong-tu-so-96-2020-tt-btc-ngay-16-11-2020-cua-bo-truong-bo-tai-chinh-huong-dan-cong-bo-thong-tin-tren-thi-truong-chung-khoan) (mở 02/11/2026; ban hành 16/11/2020, hiệu lực 01/01/2021 theo trang): báo cáo tài chính năm kiểm toán nằm ở Điều 10 khoản 1 điểm c, và Điều 14 khoản 1 (tổ chức niêm yết) dẫn chiếu Điều 10: công bố trong 10 ngày kể từ ngày kiểm toán ký, không quá 90 ngày kể từ cuối năm tài chính. Bán niên soát xét (Điều 14 khoản 2c): 5 ngày kể từ ngày ký, không quá 45 ngày (60 ngày với công ty mẹ hoặc đơn vị cấp trên). Quý (khoản 3c): 20 ngày kể từ cuối quý (30 ngày với công ty mẹ); quý soát xét: 5 ngày kể từ ngày ký, không quá 45 ngày. Điều 14 áp cho tổ chức niêm yết và công ty đại chúng quy mô lớn. Trang còn nêu giải trình khi lợi nhuận sau thuế đổi từ 10% trở lên, đổi dấu, hoặc chênh lệch trước/sau kiểm toán từ 5% (khoản 4–5). Trang ghi "đang có hiệu lực" và có Thông tư 68/2024/TT-BTC (hiệu lực 02/11/2024) sửa đổi Điều 5 và bổ sung Điều 25, 33; nguồn thứ cấp khác nhắc sửa đổi 18/2025 và 08/2026 (chưa mở văn bản gốc). `CHƯA_BIẾT` liệu các sửa đổi đó có đổi Điều 10, 14 không; có nguồn thứ cấp nhắc một dự thảo thông tư thay thế Thông tư 96 (chưa mở), nên số ngày trên đây không được dùng làm quy tắc hành động khi chưa đối chiếu văn bản hợp nhất. `CHƯA_BIẾT` hệ thống công bố của cơ quan quản lý có cung cấp dữ liệu có cấu trúc hay không.

`CHƯA_BIẾT` Việt Nam có API tương tự `companyfacts` hay không (thông tin thứ cấp, chưa mở, về cổng công bố một đầu mối của Ủy ban Chứng khoán Nhà nước từ tháng 03/2024). `SUY_LUẬN` Cho tới khi xác nhận, quy trình là: tìm báo cáo ở website quan hệ cổ đông hoặc cổng công bố, ghi URL và ngày mở, tải và băm tệp, chép vào bảng, chạy đẳng thức, ghi ô đọc không rõ là `CHƯA_BIẾT`. Trước hết tìm bản có lớp chữ hoặc Excel (IR công ty, cổng sở giao dịch, Vietstock); có thì trích tự động rồi vẫn kiểm đẳng thức. PDF ảnh mới phải đọc từng trang và chép tay; CSV của bài **chưa được chép lần hai** bởi người khác (số FY2024 trong CSV là số trình bày lại, đừng so với báo cáo FY2024 gốc khi chưa kiểm).

## 5. Bảng tính: dựng để tự báo lỗi

Mỗi bảng có các cột: chỉ tiêu, mã số hoặc tag, kỳ, giá trị gốc nguyên đơn vị, đơn vị, nguồn (URL, trang), ngày mở; cột chuyển đổi riêng có công thức (ví dụ `=D5/1000000`); và khối "kiểm" ở cuối (ví dụ `=ABS(B2-(B3+B4))<0,01`). Ghi mã băm tệp cạnh URL khi tải.

## Bài tập — làm trước khi mở đáp án

1. Nêu ba lớp dữ liệu và vì sao dữ liệu gốc và dữ liệu chuyển đổi phải ở khối riêng.
2. Dựng đường dẫn `companyfacts` cho Apple (CIK 320193). Nêu hai quy tắc truy cập của SEC phải tuân thủ.
3. Ba bản ghi lợi nhuận ròng của Apple: (a) kỳ 01/10/2023–28/09/2024, 93.736 triệu USD, `fy = 2024`, nộp 01/11/2024; (b) cùng kỳ, 93.736 triệu USD, `fy = 2025`, nộp 31/10/2025; (c) kỳ 29/09/2024–27/09/2025, 112.010 triệu USD, `fy = 2025`. Bản ghi nào là FY2024 và vì sao lọc theo `fy` sai?
4. Đổi `90.711.000.000` USD sang triệu USD và `14.948.500.000` cổ phiếu sang nghìn cổ phiếu.
5. Lợi nhuận ròng cả năm 112.010 và lũy kế chín tháng 84.544 (triệu USD): quý 4 là bao nhiêu? Nhãn đúng cho con số đó là gì?
6. Mua lại FY2025 của Apple có ba số: 90.711 (lưu chuyển tiền tệ), 90.052 (báo cáo biến động vốn chủ), 89.300 (thẻ XBRL `StockRepurchasedAndRetiredDuringPeriodValue`), triệu USD. Tính các chênh lệch từng đôi, nêu số bạn dùng cho dòng tiền và điều bạn ghi là `CHƯA_BIẾT`.
7. Cổ tức công bố mỗi cổ phiếu cùng một kỳ có hai giá trị 3 và 0,75 USD. Giải thích và nêu cách xử lý khi so các năm.
8. Hòa Phát FY2025: kiểm tài sản = nợ phải trả + vốn chủ với 257.899,20; 126.679,19; 131.220,01.
9. Hòa Phát FY2025: kiểm lợi nhuận sau thuế từ lợi nhuận trước thuế 18.040,59, thuế hiện hành 2.574,22, thuế hoãn lại −48,56.
10. Thiết kế quy trình lấy dữ liệu cho một công ty Việt Nam niêm yết mà báo cáo là PDF ảnh quét: các bước, các phép kiểm và nhãn cho các ô đọc không rõ.

## Đáp án

<details>
<summary>Mở sau khi tự làm</summary>

1. Gốc, có cấu trúc, bảng tính. Tách để khi có lỗi bạn còn biết số nào là quan sát và số nào do mình tính.
2. `https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json` (CIK đệm đủ 10 chữ số). Khai User-Agent có tên và email liên hệ; không vượt 10 yêu cầu mỗi giây (mức hiện tại).
3. (a) và (b) đều là FY2024 (hai hồ sơ báo cùng một số); (c) là FY2025. Lọc `fy == 2025` lấy cả (b) và (c), tức hai năm khác nhau. Phải lọc theo `start`/`end`.
4. `90.711` triệu USD; `14.948.500` nghìn cổ phiếu.
5. `112.010 − 84.544 = 27.466` triệu USD; nhãn `PHÉP_TÍNH` (suy ra từ hai số), không phải `SỰ_THẬT` của công bố quý 4.
6. 90.711 − 90.052 = 659; 90.052 − 89.300 = 752; 90.711 − 89.300 = 1.411 (hai số có 89.300 mang sai số khoảng ±50 triệu vì MD&A làm tròn 0,1 tỷ; độ chính xác `decimals` của thẻ là `CHƯA_BIẾT`, kiểm bằng trang R của 10-K). Cho dòng tiền ưu tiên 90.711 (`Ý_KIẾN`: là số trong báo cáo lưu chuyển tiền tệ). Nêu cả ba số kèm khái niệm; nguyên nhân khác nhau là `CHƯA_BIẾT`, không được đoán và không được bỏ số nào.
7. Tỷ lệ 4: số cũ được trình bày lại sau một sự kiện chia tách (suy luận, không có nhãn trong dữ liệu). Khi so các năm, dùng cùng một cơ sở: chia số cũ cho 4 (hoặc dùng số điều chỉnh của hồ sơ mới nhất) và ghi lại.
8. `126.679,19 + 131.220,01 = 257.899,20`: đạt.
9. `18.040,59 − 2.574,22 − (−48,56) = 15.514,93`: đạt.
10. Ví dụ: ghi URL, ngày mở, băm tệp; đọc theo trang và chép vào bảng kèm số trang; chạy các đẳng thức (cân đối, tiền, lợi nhuận); với ô không đọc rõ ghi `CHƯA_BIẾT` kèm số trang chứ không đoán; đối chiếu một số quan trọng với nguồn thứ hai; lưu bản đã chuyển ở cột riêng. Chấp nhận bước khác nếu có lý do.

</details>

## Bài làm với dữ liệu thiếu hoặc lệch

Đề: "Bảng chép tay báo cáo Hòa Phát FY2025 có: tổng tài sản 257.899,20; nợ phải trả 126.697,19; vốn chủ 131.220.010,877 (ghi chú: nguồn VND, đơn vị trong cột ghi 'triệu'). Doanh thu thuần của Apple là 416.161 và lợi nhuận của Hòa Phát là 15.514,9, so tỷ lệ."

Phát hiện: (a) `126.697,19` nghi đảo chữ số (lệch −18,00); (b) ô vốn chủ khác đơn vị (triệu VND, lớn hơn nghìn lần) và ghi chú mâu thuẫn; (c) Apple (triệu USD) và Hòa Phát (tỷ VND) khác tiền tệ và đơn vị.

`Đáp án` Không dùng bảng này. Quay lại trang gốc: nợ phải trả đúng là 126.679,19 và vốn chủ 131.220,01 tỷ VND. Cần cột đơn vị thống nhất, chạy lại đẳng thức, không so số khác tiền tệ khi chưa đổi.

## Sai ở đâu

Một học viên viết: "Tôi lọc bản ghi `fy == 2025` của Apple, lấy hàng đầu tiên làm lợi nhuận FY2025, lấy `Revenues` làm doanh thu, chia 1.000 cho ra triệu USD, và quý 4 là số cả năm trừ quý 3 trong 10-K. Ba số mua lại 90.711, 90.052 và 89.300 chắc có hai số sai nên tôi bỏ số nhỏ."

<details>
<summary>Mở sau khi tự tìm lỗi</summary>

1. `fy` là năm của hồ sơ, hàng đầu tiên có thể là kỳ khác; phải lọc theo `start`/`end`.
2. `Revenues` chỉ có số năm 2018; phải chọn tag có kỳ mới nhất.
3. Chia 1.000 sai đơn vị; đổi sang triệu phải chia 1.000.000.
4. 10-K không có số quý 3 riêng để trừ; quý 4 = cả năm − lũy kế chín tháng, và đó là phép suy ra.
5. Ba số mua lại đến từ ba chỗ khác nhau, nguyên nhân khác nhau chưa biết; không có căn cứ để coi số nào là sai và bỏ số nhỏ mất thông tin.

</details>

## Kiểm tra chuyển bài

Đạt khi đúng cả ba.

1. Lợi nhuận cả năm 500, lũy kế chín tháng 360 (cùng đơn vị): quý 4 là bao nhiêu và nhãn là gì?
2. Tài sản 1.000, nợ phải trả 640, vốn chủ 350: kiểm đẳng thức và nêu hành động.
3. Nêu hai việc bạn làm trước khi tin một số lấy từ JSON XBRL.

<details>
<summary>Mở sau khi tự làm</summary>

Tiêu chí đạt: câu 1 `500 − 360 = 140`, nhãn `PHÉP_TÍNH`. Câu 2 `640 + 350 = 990 ≠ 1.000`, lệch 10; quay lại tài liệu gốc kiểm từng ô và đơn vị trước khi dùng. Câu 3: lọc theo kỳ chứ không theo `fy`, kiểm đơn vị và tag, so với bản gốc ở một vài số.

</details>

## Lỗi thường gặp

- Lọc theo `fy`; lấy tag đầu tiên có dữ liệu; quên đơn vị gốc; coi số suy ra (quý 4) như số công bố.
- Chép tay không kiểm đẳng thức; tin kiểm đạt là từng ô đúng; dùng "hồ sơ nộp muộn nhất" như quy tắc chung; mặc định `us-gaap` và USD.

## Ranh giới an toàn

- Bài về kỹ thuật dữ liệu, không phải khuyến nghị mua/bán/nắm giữ.
- Tuân thủ quy tắc truy cập của SEC, dùng thông tin liên hệ của chính bạn.
- Không cào hàng loạt; cần nhiều công ty thì dùng tệp ZIP của SEC; ghi nguồn khi đăng lại.
- Không nhập thông tin đăng nhập hay dữ liệu cá nhân vào trang tải dữ liệu.

## Khi nào bài này hết hiệu lực

Hết đúng nếu: BCTC FY2025 của Hòa Phát bị phát hành lại; Việt Nam đổi chuẩn kế toán (`CHƯA_BIẾT`); SEC đổi quy tắc truy cập hoặc đường dẫn API; Thông tư 96 bị thay thế hoặc sửa; Apple nộp 10-K/A hoặc trình bày lại số; cấu trúc JSON của `companyfacts` đổi; hoặc Việt Nam bắt buộc báo cáo XBRL tải được. Tập con `apple_xbrl_subset.json` (SHA-256 `04b292c59cb19cff018dc7418a8f03b59001069885766f43f766e314f6766c6b`, tải 01/11/2026) là ảnh chụp; số trong tệp đầy đủ có thể bị trình bày lại, nên so mã băm trước khi dùng.

## Điều tôi vẫn chưa hiểu

- Hệ thống công bố của Việt Nam có cho tải dữ liệu có cấu trúc không?
- Công ty tôi theo dõi có đổi tag hay trình bày lại kỳ trước không?

## Nguồn Internet đã mở

Truy cập `2026-11-01` và mở lại `2026-11-02` (các mục đã mở lại ghi ngày trong bài). Không suy ngày truy cập thành ngày xuất bản.

| Nguồn | Phạm vi | Dùng cho |
|---|---|---|
| [SEC — EDGAR Application Programming Interfaces](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) | Gốc; trang động | Các điểm cuối, phạm vi dữ liệu XBRL, tần suất cập nhật |
| [SEC — Accessing EDGAR Data](https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data), [webmaster FAQ](https://www.sec.gov/os/webmaster-faq), [developer resources](https://www.sec.gov/about/developer-resources) | Gốc; trang động | Quy tắc truy cập, User-Agent, 10 yêu cầu/giây tổng mọi máy |
| [SEC — companyfacts của Apple (CIK 320193)](https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json) | Hoa Kỳ; dữ liệu cập nhật động; tải 01/11/2026 | Số liệu Apple, tập con lưu trong repo |
| [Apple Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Gốc; FY kết thúc 27/09/2025 | Cơ sở đối chiếu số trong bài Q2; báo cáo biến động vốn chủ 90.052 và lưu chuyển tiền tệ 90.711 |
| [BCTC hợp nhất kiểm toán FY2025 của Hòa Phát](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/03/20260327-hpg-bctc-hop-nhat-nam-2025-sau-kiem-toan.pdf) | Gốc; PDF ảnh; VND; VAS; trang in 4–10 | Bản chép và các đẳng thức |
| [Apple 8-K quý 4 FY2025, phụ lục 99.1](https://www.sec.gov/Archives/edgar/data/320193/000032019325000077/a8-kex991q4202509272025.htm) | Gốc; quý kết thúc 27/09/2025 | Lợi nhuận ròng quý 4 27.466 |
| [Thông tư 96/2020/TT-BTC (bản đăng lại trên caselaw.vn)](https://caselaw.vn/van-ban-phap-luat/372205-thong-tu-so-96-2020-tt-btc-ngay-16-11-2020-cua-bo-truong-bo-tai-chinh-huong-dan-cong-bo-thong-tin-tren-thi-truong-chung-khoan) | Thứ cấp; đã đọc toàn văn bản đăng lại (235.516 ký tự), gồm Điều 10 và 14 | Thời hạn công bố, giải trình lợi nhuận |

`CHƯA_BIẾT` Văn bản gốc của Bộ Tài chính và các sửa đổi 18/2025, 08/2026 có đổi Điều 10, 14 không; dữ liệu có cấu trúc từ cổng công bố Việt Nam; nguyên nhân ba số mua lại của Apple khác nhau; điều khoản ghi nguồn khi đăng lại dữ liệu SEC.
