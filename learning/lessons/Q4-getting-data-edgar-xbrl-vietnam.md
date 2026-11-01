# BẢN NHÁP - CHƯA KIỂM DUYỆT: Bài Q4 — Lấy dữ liệu: EDGAR/XBRL, báo cáo Việt Nam và bảng tính

- Ngày viết: `2026-11-01`. Bài mới của Đợt 3; chưa có biên bản kiểm nguồn hay phản biện.
- Chốt dữ liệu lúc: `2026-11-01 (Asia/Ho_Chi_Minh)`
- Nguồn: trang API XBRL và quy tắc truy cập của SEC, dữ liệu `companyfacts` của Apple, báo cáo tài chính hợp nhất kiểm toán FY2025 của Hòa Phát (HPG), bản đăng lại Thông tư 96/2020/TT-BTC; mở ngày `2026-11-01` (bảng cuối bài).
- Mục tiêu: Lấy số liệu từ EDGAR bằng API có cấu trúc mà không dính các lỗi kỳ, trùng lặp, đơn vị, đổi tag; biết dữ liệu báo cáo Việt Nam nằm ở đâu và vì sao phải chép tay có kiểm; dựng bảng tính có cột nguồn và các phép kiểm đẳng thức; ghi nhận chỗ nào chưa biết.
- Bài trước liên quan: N8, V4, 004. Học trước Q1–Q3 nếu muốn tái lập số của chúng.
- Thời lượng: 3 phiên (A: mục 1–3; B: ví dụ nguồn thật và mục 4; C: bài tập).
- Tệp thực hành: [data_pull.py](../practice/models/data_pull.py), [apple_xbrl_subset.json](../practice/models/apple_xbrl_subset.json) và [hpg_fy2025_transcription.csv](../practice/models/hpg_fy2025_transcription.csv); kiểm bằng `python3 -m unittest discover tests`.
- Kiểm nguồn: `CHƯA`
- Phản biện rủi ro: `CHƯA`
- Câu hỏi cốt lõi: **Con số tôi đang cầm có đúng kỳ, đúng đơn vị, đúng khái niệm, và tôi chứng minh được nó đến từ đâu không?**

## Hiểu bài này trong 1 phút

Lấy dữ liệu giống nhặt nấm: nhặt được nhiều chưa phải tốt, quan trọng là biết cái nào ăn được. Một dòng số trong bảng tính trông giống nhau dù nó là số cả năm hay chín tháng, dù tính bằng đồng hay triệu đồng, dù là số gốc hay số đã điều chỉnh. Bài này dạy hai nguồn có thật (EDGAR cho công ty Mỹ và báo cáo PDF của công ty Việt Nam), những chỗ dễ nhầm ở từng nguồn, và cách dựng bảng tính để chính bảng tính báo lỗi cho bạn.

## Ôn bài cũ hoặc kiểm tra đầu vào

1. N8: vì sao hai trang chép cùng một thông cáo không được tính là hai nguồn độc lập?
2. 004: đơn vị của một số trong báo cáo năm có nằm trong số không?

<details>
<summary>Mở sau khi tự làm</summary>

(1) cùng một nguồn gốc nhân đôi, không thêm bằng chứng; (2) không, đơn vị nằm ở đầu bảng hoặc thuyết minh; đọc sai đơn vị là lỗi phổ biến.

</details>

## Bài này làm gì và chưa làm gì

| Làm | Chưa làm |
|---|---|
| Dạy gọi và đọc API XBRL của SEC; kiểm chéo với tài liệu gốc; chép và kiểm báo cáo Việt Nam | Không dạy cào dữ liệu hàng loạt, không vượt quy tắc truy cập của SEC |
| Dùng số Apple (khớp bài Q2) và Hòa Phát (khớp bài Q1, Q3) | Chưa đánh giá nhà cung cấp dữ liệu thương mại; chưa dạy dữ liệu giá |

## 1. Ba lớp dữ liệu

| Lớp | Ví dụ | Quy tắc |
|---|---|---|
| Gốc | 10-K của Apple, PDF báo cáo của Hòa Phát | Không sửa; ghi URL, ngày mở, mã băm tệp nếu tải về |
| Có cấu trúc | JSON `companyfacts` của SEC | Là bản máy đọc của số trong tài liệu gốc; kiểm chéo, không thay thế |
| Bảng tính của bạn | CSV, XLSX | Mỗi dòng có nguồn và kỳ; số chuyển đổi nằm ở cột riêng với công thức |

`SUY_LUẬN` Dữ liệu có cấu trúc nhanh nhưng nhận lỗi theo hai đường: lỗi của người gắn thẻ và lỗi của người đọc (bạn). Dữ liệu chép tay chậm và nhận lỗi gõ. Vì vậy mỗi con số quan trọng nên được kiểm một cách độc lập với cách lấy nó.

## 2. EDGAR và API XBRL

`SỰ_THẬT` Trang [SEC — EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) (mở 01/11/2026) mô tả các điểm cuối: `submissions` (lịch sử hồ sơ), `companyconcept` (một khái niệm của một công ty) và `companyfacts` (toàn bộ khái niệm của một công ty, mỗi công ty một tệp, đường dẫn dùng mã CIK đệm đủ 10 chữ số), cùng `frames` (một số liệu của nhiều công ty cho một kỳ). Dữ liệu lấy từ các mẫu 10-Q, 10-K, 8-K, 20-F, 40-F, 6-K và biến thể, và chỉ gồm các khái niệm chuẩn (us-gaap, ifrs-full, dei, srt) áp dụng cho cả pháp nhân, không gồm khái niệm riêng của công ty. API không cần khóa, và trang này nói XBRL API thường cập nhật dưới một phút.

`SỰ_THẬT` Trang [SEC — Accessing EDGAR Data](https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data) (mở 01/11/2026), mục "Fair Access": mức tối đa hiện là 10 yêu cầu mỗi giây và SEC có thể hạ mức này; chương trình nên khai User-Agent kèm tên và email liên hệ; công cụ tự động không được cào cả trang; SEC không hỗ trợ kỹ thuật cho việc gỡ lỗi script (diễn đạt lại). `PHÉP_TÍNH` Hàm `fetch_companyfacts` trong [data_pull.py](../practice/models/data_pull.py) bắt buộc User-Agent có dấu `@` và không được dùng trong test; hãy dùng thông tin liên hệ **của chính bạn**.

Cấu trúc một tệp `companyfacts`: `facts → us-gaap → <tên tag> → units → <đơn vị> → danh sách bản ghi`. Mỗi bản ghi có `start` và `end` (kỳ; chỉ có `end` nếu là số tại một thời điểm), `val`, `fy`, `fp`, `form`, `filed` và đôi khi `frame`.

## 3. Chín cạm bẫy của JSON

| # | Cạm bẫy | Cách xử lý |
|---|---|---|
| 1 | `fy` là năm tài chính của **hồ sơ**, không phải của kỳ: một 10-K nộp năm 2025 mang `fy = 2025` cho cả ba năm so sánh | Chọn theo `start` và `end`, không theo `fy` |
| 2 | Cùng một kỳ xuất hiện trong nhiều hồ sơ | Lấy hồ sơ nộp muộn nhất (`filed`), và so cả hai |
| 3 | Số tính bằng đơn vị gốc (USD, cổ phiếu), không phải triệu | Chia khi trình bày; ghi đơn vị ở cột |
| 4 | Công ty đổi tag giữa các thời kỳ | Chọn tag có kỳ mới nhất, không phải tag đầu tiên có dữ liệu |
| 5 | Nhãn `frame` như `CY2025` căn theo lịch, không phải theo năm tài chính | Không dùng frame để suy ra tên năm tài chính |
| 6 | Hồi tố: chia tách cổ phiếu và điều chỉnh làm cùng một kỳ có hai giá trị | Liệt kê kỳ có nhiều giá trị và hiểu nguyên nhân |
| 7 | Số quý 4 không có riêng trong 10-K | Quý 4 = cả năm − chín tháng lũy kế; ghi là suy ra |
| 8 | Cùng một sự kiện có hai khái niệm | So tag tiền chi và tag trong báo cáo vốn chủ |
| 9 | Số tại thời điểm (instant) khác số cả kỳ (duration) | Kiểm xem bản ghi có `start` không |

## Ví dụ từ nguồn thật

### Apple: API khớp với bài Q2, và các cạm bẫy có thật

`SỰ_THẬT` Dữ liệu [`companyfacts` của Apple](https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json) (mã CIK 320193; tôi tải ngày 01/11/2026 và lưu tập con 14 tag, các dòng kết thúc từ 01/09/2018, ở [apple_xbrl_subset.json](../practice/models/apple_xbrl_subset.json), giữ nguyên giá trị). `PHÉP_TÍNH` Dùng `annual_series` (lọc kỳ 350–380 ngày, lấy hồ sơ nộp muộn nhất) rồi chia 1.000.000, bảy chỉ tiêu dòng tiền và lợi nhuận của ba năm FY2023–FY2025 trùng khớp từng số với bảng ở bài Q2 (ví dụ lợi nhuận ròng 112.010, SBC 12.863, mua lại bằng tiền 90.711 triệu USD); test `test_khop_voi_bang_q2` kiểm điều đó. Số cổ phiếu cũng khớp: cổ phiếu cơ bản bình quân 14.948.500 nghìn.

`SỰ_THẬT` Cạm bẫy 1: với lợi nhuận ròng, các bản ghi `fy = 2025`, kỳ dài hơn 350 ngày, có ba ngày kết thúc khác nhau (30/09/2023, 28/09/2024, 27/09/2025). Lọc `fy == 2025` rồi lấy bản ghi đầu tiên có thể cho số của một năm khác.

`SỰ_THẬT` Cạm bẫy 4: tag `Revenues` của Apple chỉ có một giá trị cả năm trong tập con đã lưu (từ 09/2018), kết thúc 29/09/2018 (265.595 triệu USD); doanh thu các năm sau nằm ở `RevenueFromContractWithCustomerExcludingAssessedTax` (FY2025 416.161 triệu USD, khớp tệp số Apple của bài 011). Lấy tag đầu tiên có dữ liệu sẽ trả số năm 2018.

`SỰ_THẬT` Cạm bẫy 6: với kỳ kết thúc 28/09/2019, số cổ phiếu đang lưu hành có hai giá trị là 4.443.236.000 và 17.772.945.000; cổ tức công bố mỗi cổ phiếu cùng kỳ có hai giá trị 3 USD và 0,75 USD. `PHÉP_TÍNH` Tỷ lệ `17.772.945.000/4.443.236.000 = 4,000` và `3/0,75 = 4`. `SUY_LUẬN` Đây là hiệu ứng của một đợt chia tách cổ phiếu 4:1 làm các hồ sơ sau trình bày lại số cũ; nhãn "chia tách 4:1" không nằm trong dữ liệu đã đọc, chỉ tỷ lệ 4 là số quan sát. Đây là lý do EPS và cổ tức mỗi cổ phiếu của nhiều năm phải được điều chỉnh trước khi so (cùng nguyên tắc với cổ phiếu thưởng của Hòa Phát ở Q2).

`SỰ_THẬT` Cạm bẫy 7: lợi nhuận ròng cả năm FY2025 là 112.010 triệu USD, lũy kế chín tháng đến 28/06/2025 là 84.544 triệu USD (hồ sơ 10-Q quý 3). `PHÉP_TÍNH` Quý 4 FY2025 `= 112.010 − 84.544 = 27.466` triệu USD. `CHƯA_BIẾT` đối chiếu số này với công bố kết quả quý 4 của Apple.

`SỰ_THẬT` Cạm bẫy 8: số tiền chi mua lại (`PaymentsForRepurchaseOfCommonStock`) FY2025 là 90.711 triệu USD; giá trị cổ phiếu mua lại và hủy trong báo cáo vốn chủ (`StockRepurchasedAndRetiredDuringPeriodValue`) là 89.300 triệu USD. `PHÉP_TÍNH` Lệch 1.411 triệu USD. `SUY_LUẬN` Hai số đo hai khái niệm khác nhau (tiền thực chi và giá trị ghi trong vốn chủ), nên có lệch; **bài Q2 từng ghi lệch này là chưa biết nguyên nhân, nay đã xác định là hai khái niệm khác nhau**, còn lý do riêng của 1.411 (ví dụ thuế hay thời điểm thanh toán) nguồn đã mở không nêu: `CHƯA_BIẾT`.

### Hòa Phát: tài liệu PDF và cách chép có kiểm

`SỰ_THẬT` [Báo cáo tài chính hợp nhất kiểm toán FY2025 của Hòa Phát](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/03/20260327-hpg-bctc-hop-nhat-nam-2025-sau-kiem-toan.pdf) (7,9 MB) là PDF ảnh quét: công cụ đọc văn bản không lấy được chữ, tôi phải đọc từng trang như ảnh. [Bản tổng quan Q3/2026](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/10/tong-quan-tinh-hinh-kinh-doanh-quy3-2026-vn.pdf) cũng là ảnh. Ngược lại [Báo cáo thường niên 2023](https://static2.vietstock.vn/data/HOSE/2023/BCTN/VN/HPG_Baocaothuongnien_2023.pdf) tải từ Vietstock có lớp chữ trích được. Cùng một công ty, ba tài liệu, hai kiểu định dạng.

`PHÉP_TÍNH` Từ trang báo cáo tôi chép 14 chỉ tiêu hai năm vào [hpg_fy2025_transcription.csv](../practice/models/hpg_fy2025_transcription.csv) (tỷ VND; số gốc VND chia 1 tỷ). Hàm `statement_checks` kiểm năm đẳng thức; cả hai năm đều đạt trong dung sai 0,01 tỷ:

| Đẳng thức | FY2025 (tỷ VND) |
|---|---:|
| Tài sản = nợ phải trả + vốn chủ | `257.899,20 = 126.679,19 + 131.220,01` |
| Tiền cuối năm: bảng cân đối = lưu chuyển tiền tệ | `8.300,89 = 8.300,89` |
| Lợi nhuận sau thuế = trước thuế − thuế hiện hành − thuế hoãn lại | `15.514,93 = 18.040,59 − 2.574,22 − (−48,56)` |
| Lợi nhuận mẹ + không kiểm soát = sau thuế | `15.453,17 + 61,76 = 15.514,93` |
| Lợi nhuận gộp = doanh thu thuần − giá vốn | `24.497,79 = 156.116,09 − 131.618,31` |

`SUY_LUẬN` Đẳng thức đạt không chứng minh từng ô đúng (hai lỗi bù trừ vẫn qua được), nhưng đẳng thức hỏng chắc chắn báo có lỗi. Một chữ số đảo trong nợ phải trả (126.679,19 gõ thành 126.697,19) làm đẳng thức đầu lệch −18,00 tỷ trong khi bốn đẳng thức còn lại vẫn đạt; điều đó khoanh vùng lỗi vào các ô của bảng cân đối. Một ô nhập bằng triệu VND thay vì tỷ VND làm lệch cả nghìn lần; test `test_ban_chep_hpg` kiểm cả hai.

## 4. Báo cáo Việt Nam: ở đâu, khi nào, dạng gì

`SỰ_THẬT` (thứ cấp, bản đăng lại) Điều 14 [Thông tư 96/2020/TT-BTC](https://caselaw.vn/van-ban-phap-luat/372205-thong-tu-so-96-2020-tt-btc-ngay-16-11-2020-cua-bo-truong-bo-tai-chinh-huong-dan-cong-bo-thong-tin-tren-thi-truong-chung-khoan) (mở 01/11/2026; ngày ban hành 16/11/2020 theo đường dẫn) quy định cho tổ chức niêm yết: báo cáo tài chính năm kiểm toán công bố trong 10 ngày kể từ ngày kiểm toán ký và không quá 90 ngày kể từ cuối năm tài chính; báo cáo bán niên soát xét trong 5 ngày kể từ ngày ký và không quá 45 ngày (tối đa 60 ngày với công ty mẹ hoặc đơn vị kế toán cấp trên có đơn vị hạch toán riêng); báo cáo quý trong 20 ngày kể từ cuối quý (30 ngày với công ty mẹ hoặc đơn vị cấp trên). Điều 14 còn yêu cầu giải trình khi lợi nhuận sau thuế đổi từ 10% trở lên so với cùng kỳ hoặc đổi dấu lãi/lỗ (diễn đạt lại). Theo trang này, Điều 7 nêu phương tiện công bố gồm website công ty, hệ thống công bố thông tin của Ủy ban Chứng khoán Nhà nước và trang của sở giao dịch; Điều 14 không nêu định dạng XBRL. `CHƯA_BIẾT` thông tư đã được sửa đổi sau bản này chưa, và hệ thống công bố của cơ quan quản lý có cung cấp dữ liệu có cấu trúc để tải hay không (tôi mở trang chủ HOSE nhưng không đọc được nội dung hữu ích).

`SUY_LUẬN` Vì không có API tương tự `companyfacts` mà tôi đã xác nhận cho báo cáo Việt Nam, quy trình thực tế là: tìm báo cáo ở website quan hệ cổ đông của công ty hoặc cổng công bố, ghi URL và ngày mở, tải về và băm tệp, chép vào bảng, chạy đẳng thức, và ghi các ô đọc không rõ là `CHƯA_BIẾT`. Khi tệp có lớp chữ, trích tự động rồi vẫn kiểm đẳng thức; khi là ảnh, đọc từng trang và chép tay.

## 5. Bảng tính: dựng để tự báo lỗi

Mỗi bảng nên có: cột `chỉ tiêu`, `mã số hoặc tag`, `kỳ`, `giá trị gốc nguyên đơn vị`, `đơn vị`, `nguồn (URL, trang)`, `ngày mở`; cột chuyển đổi riêng có công thức, ví dụ `=D5/1000000` cho triệu USD; và một khối "kiểm" ở cuối với các ô `=ABS(B2-(B3+B4))<0,01`. Tệp CSV trong thư mục `practice/models/` làm đúng điều này bằng Python; bạn có thể làm tương đương trong bảng tính. Dữ liệu gốc và dữ liệu chuyển đổi nằm ở hai khối, đúng quy tắc nghiên cứu của dự án. Mã băm tệp: tính một lần khi tải về và ghi cạnh URL; không có nó, bạn không chứng minh được tệp hôm nay là tệp hôm qua.

## Bài tập — làm trước khi mở đáp án

1. Nêu ba lớp dữ liệu và vì sao dữ liệu gốc và dữ liệu chuyển đổi phải ở khối riêng.
2. Dựng đường dẫn `companyfacts` cho Apple (CIK 320193). Nêu hai quy tắc truy cập của SEC phải tuân thủ.
3. Ba bản ghi lợi nhuận ròng của Apple: (a) kỳ 01/10/2023–28/09/2024, 93.736 triệu USD, `fy = 2024`, nộp 01/11/2024; (b) cùng kỳ, 93.736 triệu USD, `fy = 2025`, nộp 31/10/2025; (c) kỳ 29/09/2024–27/09/2025, 112.010 triệu USD, `fy = 2025`. Bản ghi nào là FY2024 và vì sao lọc theo `fy` sai?
4. Đổi `90.711.000.000` USD sang triệu USD và `14.948.500.000` cổ phiếu sang nghìn cổ phiếu.
5. Lợi nhuận ròng cả năm 112.010 và lũy kế chín tháng 84.544 (triệu USD): quý 4 là bao nhiêu? Nhãn đúng cho con số đó là gì?
6. Mua lại: 90.711 triệu USD tiền chi, 89.300 triệu USD trong báo cáo vốn chủ. Chênh bao nhiêu, và bạn dùng số nào cho phân tích dòng tiền? Vì sao?
7. Cổ tức công bố mỗi cổ phiếu cùng một kỳ có hai giá trị 3 và 0,75 USD. Giải thích và nêu cách xử lý khi so các năm.
8. Hòa Phát FY2025: kiểm tài sản = nợ phải trả + vốn chủ với 257.899,20; 126.679,19; 131.220,01.
9. Hòa Phát FY2025: kiểm lợi nhuận sau thuế từ lợi nhuận trước thuế 18.040,59, thuế hiện hành 2.574,22, thuế hoãn lại −48,56.
10. (Chuyển giao) Thiết kế quy trình lấy dữ liệu cho một công ty Việt Nam niêm yết mà báo cáo là PDF ảnh quét: các bước, các phép kiểm và nhãn cho các ô đọc không rõ.

## Đáp án

<details>
<summary>Mở sau khi tự làm</summary>

1. Gốc, có cấu trúc, bảng tính. Tách để khi có lỗi bạn còn biết số nào là quan sát và số nào do mình tính.
2. `https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json` (CIK đệm đủ 10 chữ số). Khai User-Agent có tên và email liên hệ; không vượt 10 yêu cầu mỗi giây (mức hiện tại).
3. (a) và (b) đều là FY2024 (hai hồ sơ báo cùng một số); (c) là FY2025. Lọc `fy == 2025` lấy cả (b) và (c), tức hai năm khác nhau. Phải lọc theo `start`/`end`.
4. `90.711` triệu USD; `14.948.500` nghìn cổ phiếu.
5. `112.010 − 84.544 = 27.466` triệu USD; nhãn `PHÉP_TÍNH` (suy ra từ hai số), không phải `SỰ_THẬT` của công bố quý 4.
6. Chênh 1.411. Cho dòng tiền dùng 90.711 (tiền thực chi); số 89.300 là giá trị ghi trong vốn chủ. Nêu cả hai và nói rõ khái niệm.
7. Tỷ lệ 4: số cũ được trình bày lại sau một sự kiện chia tách (suy luận, không có nhãn trong dữ liệu). Khi so các năm, dùng cùng một cơ sở: chia số cũ cho 4 (hoặc dùng số điều chỉnh của hồ sơ mới nhất) và ghi lại.
8. `126.679,19 + 131.220,01 = 257.899,20`: đạt.
9. `18.040,59 − 2.574,22 − (−48,56) = 15.514,93`: đạt.
10. Ví dụ: ghi URL, ngày mở, băm tệp; đọc theo trang và chép vào bảng kèm số trang; chạy các đẳng thức (cân đối, tiền, lợi nhuận); với ô không đọc rõ ghi `CHƯA_BIẾT` kèm số trang chứ không đoán; đối chiếu một số quan trọng với nguồn thứ hai (thông cáo, thuyết minh); lưu bản đã chuyển ở cột riêng. Chấp nhận bước khác nếu có lý do.

</details>

## Bài làm với dữ liệu thiếu hoặc lệch

Đề: "Bảng chép tay báo cáo Hòa Phát FY2025 có: tổng tài sản 257.899,20; nợ phải trả 126.697,19; vốn chủ 131.220.010,877 (ghi chú: nguồn VND, đơn vị trong cột ghi 'triệu'). Doanh thu thuần của Apple là 416.161 và lợi nhuận của Hòa Phát là 15.514,9, so tỷ lệ."

Phát hiện: (a) `126.697,19` nghi đảo chữ số vì tổng không khớp (lệch −18,00); (b) ô vốn chủ nhập theo đơn vị khác (triệu VND, lớn hơn nghìn lần so với tỷ VND của các ô còn lại) và ghi chú đơn vị mâu thuẫn; (c) so Apple (triệu USD) với Hòa Phát (tỷ VND) là khác tiền tệ và đơn vị.

`Đáp án` Không dùng bảng này. Quay lại trang báo cáo gốc: số nợ phải trả đúng là 126.679,19 và vốn chủ 131.220,01 tỷ VND. Bảng cần một cột đơn vị thống nhất, đẳng thức chạy lại, và không so các số khác tiền tệ khi chưa đổi.

## Sai ở đâu

Một học viên viết: "Tôi lọc bản ghi `fy == 2025` của Apple, lấy hàng đầu tiên làm lợi nhuận FY2025, lấy `Revenues` làm doanh thu, chia 1.000 cho ra triệu USD, và quý 4 là số cả năm trừ quý 3 trong 10-K. Hai số mua lại 90.711 và 89.300 chắc có một số sai nên tôi bỏ số nhỏ."

<details>
<summary>Mở sau khi tự tìm lỗi</summary>

1. `fy` là năm của hồ sơ, hàng đầu tiên có thể là kỳ khác; phải lọc theo `start`/`end`.
2. `Revenues` chỉ có số năm 2018; phải chọn tag có kỳ mới nhất.
3. Chia 1.000 sai đơn vị; đổi sang triệu phải chia 1.000.000.
4. 10-K không có số quý 3 riêng để trừ; quý 4 = cả năm − lũy kế chín tháng, và đó là phép suy ra.
5. Hai số mua lại đo hai khái niệm khác nhau, không phải một số sai; bỏ một số mất thông tin.

</details>

## Kiểm tra chuyển bài

Làm không nhìn mẫu; đạt khi đúng cả ba.

1. Lợi nhuận cả năm 500, lũy kế chín tháng 360 (cùng đơn vị): quý 4 là bao nhiêu và nhãn là gì?
2. Tài sản 1.000, nợ phải trả 640, vốn chủ 350: kiểm đẳng thức và nêu hành động.
3. Nêu hai việc bạn làm trước khi tin một số lấy từ JSON XBRL.

<details>
<summary>Mở sau khi tự làm</summary>

Tiêu chí đạt: câu 1 `500 − 360 = 140`, nhãn `PHÉP_TÍNH`. Câu 2 `640 + 350 = 990 ≠ 1.000`, lệch 10; quay lại tài liệu gốc kiểm từng ô và đơn vị trước khi dùng. Câu 3: lọc theo kỳ chứ không theo `fy`, kiểm đơn vị và tag, so với bản gốc ở một vài số.

</details>

## Lỗi thường gặp

- Lọc theo `fy`; lấy tag đầu tiên có dữ liệu; quên đơn vị gốc (đồng hay triệu, cổ phiếu hay nghìn).
- Coi số suy ra (quý 4) như số công bố.
- Chép tay không kiểm đẳng thức; tin kiểm đạt là từng ô đúng.

## Ranh giới an toàn

- Đây là bài học về kỹ thuật dữ liệu, không phải khuyến nghị mua/bán/nắm giữ.
- Tuân thủ quy tắc truy cập của SEC; dùng thông tin liên hệ của chính bạn, đừng chạy script với danh tính người khác.
- Không nhập thông tin đăng nhập hay dữ liệu cá nhân vào bất kỳ trang tải dữ liệu nào; tải dữ liệu thương mại chỉ theo điều khoản của nhà cung cấp.

## Điều tôi vẫn chưa hiểu

- Hệ thống công bố thông tin chính thức của Việt Nam có cho tải dữ liệu có cấu trúc không, và dưới điều khoản nào?
- Công ty tôi theo dõi có đổi tag hay trình bày lại các kỳ trước không?

## Nguồn Internet đã mở

Truy cập `2026-11-01`. Không suy ngày truy cập thành ngày xuất bản.

| Nguồn | Phạm vi | Dùng cho |
|---|---|---|
| [SEC — EDGAR Application Programming Interfaces](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) | Gốc; trang động | Các điểm cuối, phạm vi dữ liệu XBRL, tần suất cập nhật |
| [SEC — Accessing EDGAR Data](https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data) | Gốc; trang động | Quy tắc truy cập công bằng, User-Agent, 10 yêu cầu mỗi giây |
| [SEC — companyfacts của Apple (CIK 320193)](https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json) | Hoa Kỳ; dữ liệu cập nhật động; tải 01/11/2026 | Số liệu Apple, tập con lưu trong repo |
| [Apple Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Gốc; FY kết thúc 27/09/2025 | Cơ sở đối chiếu số trong bài Q2 |
| [BCTC hợp nhất kiểm toán FY2025 của Hòa Phát](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/03/20260327-hpg-bctc-hop-nhat-nam-2025-sau-kiem-toan.pdf) | Gốc; PDF ảnh; VND; VAS; trang in 4–10 | Bản chép và các đẳng thức |
| [Thông tư 96/2020/TT-BTC (bản đăng lại trên caselaw.vn)](https://caselaw.vn/van-ban-phap-luat/372205-thong-tu-so-96-2020-tt-btc-ngay-16-11-2020-cua-bo-truong-bo-tai-chinh-huong-dan-cong-bo-thong-tin-tren-thi-truong-chung-khoan) | Thứ cấp; đã đọc đến Điều 14 | Thời hạn công bố, giải trình lợi nhuận |

`CHƯA_BIẾT` Văn bản gốc của Bộ Tài chính và các sửa đổi sau 2020; dữ liệu có cấu trúc từ cổng công bố Việt Nam; đối chiếu số quý 4 của Apple với công bố quý.
