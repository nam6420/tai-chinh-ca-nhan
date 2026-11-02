# BẢN NHÁP - CHƯA KIỂM DUYỆT: Bài Q2 — Cổ phiếu thưởng nhân viên, pha loãng, mua lại và cổ tức

- Ngày viết: `2026-11-01`. Bài mới của Đợt 3; chưa có biên bản kiểm nguồn hay phản biện.
- Chốt dữ liệu lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Nguồn số: Form 10-K FY2025 của Apple (SEC), báo cáo tài chính hợp nhất kiểm toán FY2025 của Hòa Phát (HPG), bài viết Damodaran ngày 24/02/2026; mở ngày `2026-11-01` (bảng cuối bài).
- Mục tiêu: Tính chi phí thật của cổ phiếu thưởng nhân viên (SBC); phân biệt mua lại cổ phiếu làm đẹp EPS với mua lại làm tăng giá trị; tính mua lại ròng sau pha loãng; so tiền trả cổ đông với dòng tiền; xử lý cổ phiếu thưởng và điều chỉnh EPS.
- Bài trước liên quan: 006, 010, 011. Học tiếp Q3.
- Thời lượng: 3 phiên (A: mục 1–3; B: ví dụ nguồn thật và mục 4–5; C: bài tập).
- Tệp thực hành: [capital_return.py](../practice/models/capital_return.py) và [apple_capital_return_inputs.csv](../practice/models/apple_capital_return_inputs.csv); kiểm bằng `python3 -m unittest discover tests`.
- Kiểm nguồn: `CHƯA`
- Phản biện rủi ro: `CHƯA`
- Câu hỏi cốt lõi: **Công ty trả gì cho cổ đông, lấy gì từ cổ đông, và phần còn lại của mỗi cổ phiếu giá trị hơn hay kém đi?**

## Hiểu bài này trong 1 phút

Hình dung công ty là một cái bánh chia cho các cổ đông. Mua lại cổ phiếu là công ty dùng tiền của chính nó mua phần bánh của một số người; những người ở lại giữ phần lớn hơn của cái bánh nhỏ hơn. Phát hành cổ phiếu thưởng cho nhân viên làm ngược lại: cắt thêm phần cho người mới. Cổ tức bằng tiền đưa ra một lát bánh. Cổ phiếu thưởng cho cổ đông (như Hòa Phát năm 2025) chỉ cắt cùng một cái bánh thành nhiều miếng nhỏ hơn. Bài này dạy tính từng việc, rồi ghép lại để biết **giá trị mỗi cổ phiếu** của người ở lại tăng, giảm hay không đổi.

## Ôn bài cũ hoặc kiểm tra đầu vào

1. 006: nêu ba cách công ty dùng tiền dư.
2. 011: vì sao DCF của bài đó trừ SBC khỏi dòng tiền tự do?

<details>
<summary>Mở sau khi tự làm</summary>

(1) trả nợ hoặc giữ tiền, tái đầu tư, trả cổ đông; (2) SBC là chi phí thật dưới dạng cổ phiếu, không trừ thì dòng tiền bị tính cao.

</details>

## Bài này làm gì và chưa làm gì

| Làm | Chưa làm |
|---|---|
| Dạy tính SBC, pha loãng, mua lại, cổ tức, cổ phiếu thưởng; dùng số thật của Apple và Hòa Phát | Không đánh giá chính sách trả tiền của công ty nào là đúng hay sai |
| Dạy đọc bài "bẩn": đơn vị lệch, hai con số cho cùng một việc | Không dạy thuế cổ tức hay thuế bán cổ phiếu (xem L3); không dạy quyền chọn |

## 1. Bốn dòng chảy giữa công ty và cổ đông

| Dòng | Tiền ra khỏi công ty? | Số cổ phiếu | Giá trị mỗi cổ phiếu |
|---|---|---|---|
| Cổ tức tiền mặt | Có | Không đổi | Giảm đúng phần tiền trả (cổ đông nhận tiền bù) |
| Mua lại cổ phiếu | Có | Giảm | Tăng, giảm hoặc giữ tùy giá mua so với giá trị nội tại |
| Cổ phiếu thưởng cho nhân viên (SBC) | Không (trả bằng cổ phiếu) | Tăng | Giảm vì thêm người chia bánh |
| Cổ phiếu thưởng cho cổ đông | Không | Tăng theo tỷ lệ cho mọi người | Mỗi cổ phiếu giảm, tổng giá trị cổ đông không đổi |

`Ý_KIẾN` Cách nhìn dùng trong bài này là **giá trị mỗi cổ phiếu của người ở lại**, không phải EPS hay số tiền chi. Mua lại có thể làm EPS tăng trong khi giá trị mỗi cổ phiếu giảm (mục 3).

## 2. SBC: chi phí không chảy tiền nhưng có thật

`SỰ_THẬT` Form 10-K FY2025 của Apple (báo cáo lưu chuyển tiền tệ, triệu USD): chi phí SBC 12.863 (FY2025), 11.688 (FY2024), 10.833 (FY2023). Nó được cộng lại vào dòng tiền hoạt động vì không chi tiền, nhưng đã làm giảm lợi nhuận.

`SUY_LUẬN` Khi phân tích có hai cách phản ánh SBC: (a) coi như chi phí, trừ khỏi dòng tiền và dùng số cổ phiếu hiện hữu; (b) không trừ, nhưng cộng cổ phiếu sẽ phát hành theo SBC vào số cổ phiếu pha loãng (nhiều nhà phân tích cộng lại SBC theo cách này). Trùng lặp chỉ xảy ra khi cùng một khoản cấp phát vừa bị trừ khỏi dòng tiền vừa bị cộng vào số cổ phiếu. Phần đã cấp chưa vest và quyền chọn (phương pháp cổ phiếu quỹ, *treasury stock method*) cần xử lý riêng; bài này không dạy. Bỏ qua cả hai cách là bỏ sót chi phí.

`PHÉP_TÍNH` Apple FY2025: SBC `/` dòng tiền hoạt động `= 12.863/111.482 = 11,5%`; dòng tiền tự do đơn giản (dòng tiền hoạt động trừ chi mua TSCĐ 12.715) `= 98.767`; trừ thêm SBC cho `85.904`. Bài 011 dùng đúng `85.904` làm dòng tiền gốc.

`Ý_KIẾN` Quy ước của dự án này: trừ SBC khỏi dòng tiền khi định giá; đây là lựa chọn phương pháp, không phải quy định kế toán. Người học nên tự lập luận vì sao chọn.

`SỰ_THẬT` Trong bài [Data Update 8 for 2026](https://aswathdamodaran.blogspot.com/2026/02/data-update-8-for-2026-time-for.html) (Damodaran, 24/02/2026), ông nêu rằng việc trả lương bằng cổ phiếu giải thích mua lại cổ phiếu hợp với quyền chọn hơn cổ phiếu hạn chế, và mua lại vẫn tăng khi công ty chuyển sang cổ phiếu hạn chế; nghĩa là SBC không phải lời giải thích đủ cho mua lại. Bài này không dựa vào điểm đó để kết luận về công ty nào.

## 3. Mua lại: giá so với giá trị nội tại

`SỰ_THẬT` Cùng bài Damodaran (mục "Buybacks - Myths and Realities"): mua lại ở mọi mức giá không tạo hay phá giá trị, chỉ **chuyển** giá trị giữa người bán và người ở lại; mua dưới giá trị nội tại chuyển giá trị cho người ở lại, mua trên giá trị chuyển cho người bán; mua ở giá hợp lý thì giá trị mỗi cổ phiếu gần như không đổi (diễn đạt lại).

`KỊCH_BẢN` Công ty Biển Xanh (hư cấu): 100 triệu cổ phiếu, lợi nhuận ròng 1.000 tỷ đồng, giá 100.000 đồng/cổ phiếu. Mua lại 200 tỷ đồng ở giá 100.000.

`PHÉP_TÍNH` Số cổ phiếu mua `= 200 tỷ/100.000 = 2 triệu` (2%), còn 98 triệu. EPS từ `1.000 tỷ/100 triệu = 10.000` đồng lên `1.000 tỷ/98 triệu ≈ 10.204` đồng, tăng 2,04%. Trong ví dụ này (lợi nhuận không đổi), EPS tăng ở mọi giá dương, nhỏ dần khi giá cao hơn (ở giá 200.000 chỉ mua 1 triệu cổ phiếu, EPS tăng khoảng 1,01%); ví dụ giữ lợi nhuận ròng 1.000 tỷ không đổi, bỏ qua lãi tiền gửi mất đi, lãi vay phát sinh và thuế, nên mức tăng thực tế thấp hơn. `SUY_LUẬN` Khi tính các khoản đó, mua lại chỉ làm EPS tăng nếu lợi suất lợi nhuận của cổ phiếu (1/P/E) cao hơn lãi suất sau thuế của khoản tiền dùng; ở P/E rất cao EPS có thể giảm. EPS chỉ là số học, không chứng minh giá trị. Giá trị mới là câu hỏi khác:

| Giá trị nội tại vốn chủ (giả định) | Mỗi cổ phiếu trước | Mỗi cổ phiếu sau | Người ở lại |
|---|---:|---:|---|
| 15.000 tỷ (150.000/cổ phiếu) | 150.000 | `(15.000−200)/98 triệu = 151.020` | Được lợi (+0,7%) |
| 6.000 tỷ (60.000/cổ phiếu) | 60.000 | `(6.000−200)/98 triệu = 59.184` | Bị thiệt (−1,4%) |

Ở hàng thứ hai EPS vẫn tăng 2,04% nhưng người ở lại thiệt, vì công ty trả 100.000 cho thứ chỉ đáng 60.000. Giá hòa vốn của mua lại là giá trị nội tại, `breakeven_price`. `Ý_KIẾN` Giá trị nội tại là ước tính, không phải số quan sát. Mô hình trên bỏ qua thuế, chi phí giao dịch, quyền chọn và cổ phiếu chưa vest; Damodaran nêu thêm rằng thay đổi đòn bẩy có thể đổi chi phí vốn và do đó giá trị mỗi cổ phiếu. Vì vậy nó chỉ minh họa cơ chế, không cho con số thực.

## Ví dụ từ nguồn thật

### Apple FY2025: tiền trả cổ đông và pha loãng

`SỰ_THẬT` [Form 10-K FY2025 của Apple](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) (kết thúc 27/09/2025; triệu USD, cổ phiếu tính bằng nghìn; số trong tệp [apple_capital_return_inputs.csv](../practice/models/apple_capital_return_inputs.csv)):

| Chỉ tiêu | FY2025 | FY2024 | FY2023 |
|---|---:|---:|---:|
| Lợi nhuận ròng | 112.010 | 93.736 | 96.995 |
| Mua lại cổ phiếu (tiền chi) | 90.711 | 94.949 | 77.550 |
| Cổ tức và cổ tức tương đương (tiền chi) | 15.421 | 15.234 | 15.025 |
| Thuế trả hộ khi nhân viên nhận cổ phiếu thưởng (tiền chi) | 5.960 | 5.441 | 5.431 |
| Cổ phiếu bình quân gia quyền, cơ bản (nghìn) | 14.948.500 | 15.343.783 | 15.744.231 |
| Cổ phiếu bình quân gia quyền, pha loãng (nghìn) | 15.004.697 | 15.408.095 | 15.812.547 |
| EPS pha loãng (USD) | 7,46 | 6,08 | 6,13 |
| Cổ phiếu đang lưu hành cuối năm (nghìn) | 14.773.260 | 15.116.786 | không lấy |

`SỰ_THẬT` Tài liệu cũng nêu chương trình mua lại 110 tỷ USD (tháng 05/2024) đã dùng hết và chương trình mới 100 tỷ USD (tháng 05/2025) đã dùng 221 triệu USD đến 27/09/2025; có **ba** con số cho cùng việc mua lại: phần thuyết minh của ban điều hành ghi mua lại 89,3 tỷ USD trong năm; báo cáo biến động vốn chủ ghi "Common stock repurchased" 90.052 triệu USD (FY2024 95.846; FY2023 77.046); báo cáo lưu chuyển tiền tệ ghi tiền chi 90.711 (FY2024 94.949; FY2023 77.550). Số 89,3 tỷ trùng với thẻ XBRL `StockRepurchasedAndRetiredDuringPeriodValue` (bài Q4). `CHƯA_BIẾT` vì sao ba số khác nhau (thời điểm thanh toán, thuế, cách ghi); bài dùng số tiền chi trong báo cáo lưu chuyển tiền tệ.

`PHÉP_TÍNH` Cổ tức `/` lợi nhuận `= 15.421/112.010 = 13,8%`. Tiền trả cho cổ đông (cổ tức và mua lại) `= 15.421 + 90.711 = 106.132`; thêm 5.960 thuế công ty nộp hộ nhân viên khi quyết toán ròng cổ phiếu thì `112.092`, xấp xỉ lợi nhuận ròng 112.010 (cổ tức tuyên bố 15.413, khác tiền chi 15.421). Dòng tiền hoạt động trừ chi mua TSCĐ ba năm (triệu USD; từ [apple_capital_return_inputs.csv](../practice/models/apple_capital_return_inputs.csv)):

| Năm | Tiền trả cổ đông | CFO − capex | Chênh |
|---|---:|---:|---:|
| FY2025 | 106.132 | 98.767 | +7.365 |
| FY2024 | 110.183 | 108.807 | +1.376 |
| FY2023 | 92.575 | 99.584 | −7.009 |

So với 85.904 (đã trừ SBC), FY2025 vượt `20.228`. Một năm không đủ để kết luận: `SỰ_THẬT` 10-K ghi khoản thuế một lần 10,2 tỷ USD của quý 4 FY2024 gồm 15,8 tỷ USD phải trả Ireland bằng tiền giữ ký quỹ (thuyết minh 7), và `SUY_LUẬN` việc thanh toán này có thể làm lệch dòng tiền FY2025 (10-K không nói thẳng; `CHƯA_BIẾT` mức ảnh hưởng). Mẫu một công ty tiền mặt lớn, biên cao chỉ minh họa cách đọc, không chứng minh mua lại tốt hay xấu. `SUY_LUẬN` Khoản 5.960 là một phần chi phí SBC bằng tiền, nên không cộng vào phép so với số đã trừ SBC. `CHƯA_BIẾT` phần vượt được tài trợ bằng tiền sẵn có hay vay.

`PHÉP_TÍNH` EPS pha loãng tăng `7,46/6,08 − 1 = 22,7%`, trong khi lợi nhuận ròng tăng `112.010/93.736 − 1 = 19,5%` và cổ phiếu pha loãng bình quân giảm `15.004.697/15.408.095 − 1 = −2,6%`. Vậy khoảng 3 điểm phần trăm tăng EPS đến từ việc giảm số cổ phiếu. Lưu ý lợi nhuận FY2024 bị kéo thấp bởi khoản thuế thu nhập một lần 10,2 tỷ USD (thuyết minh số 7 của 10-K, quyết định State Aid), nên mức tăng 19,5% phần nào là hiệu ứng cơ sở thấp. Pha loãng: cổ phiếu pha loãng cao hơn cơ bản `15.004.697/14.948.500 − 1 = 0,38%` năm 2025.

`PHÉP_TÍNH` Số cổ phiếu đang lưu hành cuối năm giảm `14.773.260/15.116.786 − 1 = −2,27%` (giảm ròng 343.526 nghìn cổ phiếu), dù công ty chi 90.711 triệu USD để mua lại. Ngược lại hãy cẩn thận với cách tính "giá ngụ ý": `90.711/343,526 triệu = 264 USD` mỗi cổ phiếu giảm ròng **không phải giá mua thật**, vì số giảm ròng đã trừ cổ phiếu mới phát hành cho nhân viên (và cổ phiếu giữ lại để nộp thuế hộ cũng ảnh hưởng số lưu hành). `SỰ_THẬT` Note 10 của 10-K (mở 02/11/2026): năm 2025 mua lại 401.672 nghìn cổ phiếu ("402 million shares ... for $89.3 billion") và phát hành ròng 58.146 nghìn; `401.672 − 58.146 = 343.526`, đúng số giảm ròng. `PHÉP_TÍNH` Giá mua trung bình khoảng `89.300/401,672 = 222 USD` (hoặc `90.711/401,672 = 226 USD` nếu dùng tiền chi); khác 264 và dao động theo số tiền nào là đúng.

### Hòa Phát FY2025: cổ phiếu thưởng cho cổ đông

`SỰ_THẬT` [Báo cáo tài chính hợp nhất kiểm toán FY2025 của Hòa Phát](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/03/20260327-hpg-bctc-hop-nhat-nam-2025-sau-kiem-toan.pdf) (thuyết minh số 26, trang in 39): theo nghị quyết Đại hội đồng cổ đông ngày 17/04/2025, công ty chi trả cổ tức năm 2024 **bằng cổ phiếu** cho cổ đông hiện hữu, tỷ lệ 20% (cổ đông sở hữu 10 cổ phiếu nhận 2 cổ phiếu thưởng), nguồn là lợi nhuận sau thuế chưa phân phối; số cổ phiếu phổ thông tăng từ 6.396.250.200 lên 7.675.465.855 (tăng thêm 1.279.215.655; mệnh giá 10.000 đồng/cổ phiếu). Bảng cân đối (trang in 7): vốn góp của chủ sở hữu từ 63.962,5 lên 76.754,7 tỷ VND; lợi nhuận sau thuế chưa phân phối (mã 421) từ 49.599,1 lên 51.037,9 tỷ.

`PHÉP_TÍNH` `7.675.465.855/6.396.250.200 − 1 = 20,0%` (làm tròn; lệch rất nhỏ vì cổ phiếu lẻ, nguyên nhân `CHƯA_BIẾT`). Vốn góp tăng `76.754,7 − 63.962,5 = 12.792,2` tỷ VND, bằng số cổ phiếu thưởng nhân 10.000 đồng. Lợi nhuận sau thuế FY2025 là 15.514,9 tỷ nhưng lợi nhuận chưa phân phối chỉ tăng `1.438,8` tỷ. `PHÉP_TÍNH` `15.514,9 − 12.792,2 = 2.722,7`, lớn hơn mức tăng thật 1.438,8 tỷ; chênh khoảng 1.283,9 tỷ: `PHÉP_TÍNH` đã tách được từ báo cáo biến động vốn chủ (thuyết minh 26, trang in 38, cột lợi nhuận chưa phân phối): 49.599,1 − 12.792,2 (cổ phiếu thưởng) + 15.453,2 (lợi nhuận cổ đông công ty mẹ, không phải 15.514,9) − 496,0 − 600,0 (trích quỹ khen thưởng và quỹ đầu tư phát triển) + 6,4 (hoàn nhập) − 129,1 (đổi tỷ lệ lợi ích) − 3,5 (khác) = 51.037,9. Chênh 1.283,9 so với phép trừ ở trên là 61,8 (phần cổ đông không kiểm soát) cộng 496,0, 600,0, 129,1 và 3,5, trừ 6,4 (lệch làm tròn 0,1). Việc chuyển 12.792,2 tỷ sang vốn góp là chuyển khoản **bên trong** vốn chủ sở hữu; không có tiền rời công ty.

`SUY_LUẬN` Trong mô hình thuần (bỏ qua thuế, thanh khoản, tín hiệu và quy định), thưởng 20% không tạo thêm giá trị cho cổ đông hiện hữu: mỗi cổ phiếu mới ra đời làm mỗi cổ phiếu giảm giá trị tương ứng; các yếu tố ngoài mô hình có thể đổi kết luận, bài này chưa xét; EPS kỳ trước phải chia cho `1 + 0,2 = 1,2` để so được. Ví dụ: EPS 1.000 đồng trước thưởng thành `1.000/1,2 ≈ 833` sau điều chỉnh. Báo cáo kết quả kinh doanh FY2025 ghi lãi cơ bản trên cổ phiếu 1.973 đồng (FY2025) và 1.505 đồng (cột năm trước); `CHƯA_BIẾT` cột năm trước đã được điều chỉnh theo cổ phiếu thưởng chưa, và cách tính lãi cơ bản (có trừ quỹ khen thưởng phúc lợi hay không); cần đọc thuyết minh số 38.

## 4. Cổ tức bằng tiền và dòng tiền của cổ đông

`SỰ_THẬT` Damodaran (cùng bài 24/02/2026, mục "A Rational Cash Return Policy") định nghĩa dòng tiền tự do cho vốn chủ (FCFE) là lợi nhuận cộng chi phí không bằng tiền, trừ chi đầu tư TSCĐ và vốn lưu động, cộng nợ vay ròng phát hành; trả cho cổ đông nhiều hơn FCFE làm cạn tiền hoặc phải huy động vốn; trả khi FCFE âm là dấu hiệu cảnh báo. Ông cũng nêu năm 2025 khoảng 37% công ty có trả tiền cho cổ đông có FCFE âm (diễn đạt lại).

`PHÉP_TÍNH` Ba thước đo dùng trong bài: tỷ lệ chi trả cổ tức `= cổ tức/lợi nhuận` (Apple 13,8%); tổng tiền trả cổ đông so với FCFE; mua lại ròng `= số cổ phiếu mua − số cổ phiếu phát hành`. Không thước nào cho biết nên trả hay không; chúng chỉ cho biết phần đã trả có bền không.

`KỊCH_BẢN` Biển Xanh phát hành 1 triệu cổ phiếu mỗi năm cho nhân viên (trị giá `1 triệu × 100.000 = 100 tỷ`). Muốn giữ số cổ phiếu đứng yên, công ty phải mua lại 100 tỷ mỗi năm; chi 200 tỷ mua lại giảm ròng chỉ 1 triệu cổ phiếu (`net_buyback_shares`). Trong ví dụ giả định này, nửa số tiền mua lại chỉ bù pha loãng.

## 5. Quy trình đọc

1. Tìm trong báo cáo lưu chuyển tiền tệ: SBC, thuế trả hộ khi nhận cổ phiếu, mua lại, cổ tức.
2. Lập bảng số cổ phiếu: bình quân cơ bản, pha loãng, cuối năm; tính phần trăm giảm ròng.
3. Tách tăng EPS thành tăng lợi nhuận và giảm số cổ phiếu.
4. So tổng tiền trả với dòng tiền (có và không trừ SBC); ghi nguồn bù khoản vượt.
5. Với cổ phiếu thưởng và chia tách: điều chỉnh EPS các kỳ trước trước khi so sánh.
6. Kết luận về giá mua lại phải kèm ước tính giá trị nội tại và ghi rõ đó là giả định.

## Bài tập — làm trước khi mở đáp án

1. Với mỗi dòng ở mục 1, cho biết số cổ phiếu và tiền mặt của công ty thay đổi thế nào.
2. Biển Xanh mua lại 200 tỷ ở 100.000 đồng/cổ phiếu: tính EPS trước và sau.
3. Nếu giá trị nội tại là 150.000 đồng/cổ phiếu, tính giá trị mỗi cổ phiếu sau mua lại.
4. Nếu giá trị nội tại là 60.000 đồng/cổ phiếu, tính giá trị mỗi cổ phiếu sau mua lại và nêu hướng thay đổi.
5. Biển Xanh phát hành cổ phiếu trả SBC trị giá 100 tỷ ở giá 100.000: bao nhiêu cổ phiếu mới, và cần mua lại bao nhiêu tiền để số cổ phiếu không đổi?
6. Với mua lại 200 tỷ ở câu 2 và SBC 100 tỷ ở câu 5, số cổ phiếu giảm ròng là bao nhiêu?
7. Apple FY2025: tính tỷ lệ chi trả cổ tức và tiền trả cổ đông (cổ tức + mua lại), so với dòng tiền hoạt động trừ chi mua TSCĐ.
8. Apple: tính phần trăm thay đổi số cổ phiếu đang lưu hành cuối năm và tách tăng EPS pha loãng (22,7%) thành phần do lợi nhuận và phần do số cổ phiếu.
9. Hòa Phát thưởng cổ phiếu tỷ lệ 20% (10:2). EPS trước thưởng 1.000 đồng thì sau điều chỉnh là bao nhiêu? Lợi nhuận chưa phân phối và tổng vốn chủ thay đổi thế nào?
10. (Chuyển giao) Một công ty trả cổ đông nhiều hơn FCFE ba năm liền. Liệt kê ít nhất ba điều bạn kiểm trước khi coi đó là bền.

## Đáp án

<details>
<summary>Mở sau khi tự làm</summary>

1. Cổ tức tiền mặt: tiền giảm, số cổ phiếu không đổi. Mua lại: tiền giảm, số cổ phiếu giảm. SBC: không tiền ra, số cổ phiếu tăng. Thưởng cổ phiếu cho cổ đông: không tiền ra, số cổ phiếu tăng theo tỷ lệ.
2. EPS trước `1.000 tỷ/100 triệu = 10.000`; sau `1.000 tỷ/98 triệu ≈ 10.204`.
3. `(15.000 − 200) tỷ / 98 triệu = 151.020`: tăng từ 150.000.
4. `(6.000 − 200) tỷ / 98 triệu = 59.184`: giảm từ 60.000; người ở lại thiệt dù EPS tăng.
5. `100 tỷ/100.000 = 1 triệu` cổ phiếu mới; cần mua lại 100 tỷ để bù.
6. `200 tỷ/100.000 = 2 triệu` mua, trừ 1 triệu phát hành: giảm ròng 1 triệu cổ phiếu.
7. `15.421/112.010 = 13,8%`. Tiền trả cổ đông `15.421 + 90.711 = 106.132` (thêm 5.960 thuế hộ thì 112.092); dòng tiền hoạt động trừ chi mua TSCĐ `111.482 − 12.715 = 98.767`; trả cổ đông vượt 7.365.
8. `14.773.260/15.116.786 − 1 = −2,27%`. Lợi nhuận tăng 19,5% và cổ phiếu pha loãng bình quân giảm 2,6%, nên EPS tăng `1,195/0,974 − 1 ≈ 22,7%`; khoảng 3 điểm phần trăm đến từ giảm số cổ phiếu.
9. `1.000/1,2 ≈ 833` đồng. Lợi nhuận chưa phân phối giảm một khoản bằng giá trị cổ phiếu thưởng theo mệnh giá, vốn góp tăng cùng khoản, tổng vốn chủ không đổi, không có tiền rời công ty.
10. Ví dụ: FCFE gồm vay ròng bao nhiêu; tiền sẵn có còn bao nhiêu và còn dùng cho đầu tư gì; chi trả có đi kèm SBC lớn không; giá mua lại so với giá trị nội tại. Chấp nhận mục kiểm khác nếu có lý do.

</details>

## Bài làm với dữ liệu thiếu hoặc lệch

Đề: "Apple FY2025: lợi nhuận ròng 112.010, cổ phiếu pha loãng bình quân 15.004.697. Tính EPS. Công ty mua lại 89,3 tỷ USD theo ban điều hành, 90.052 triệu theo báo cáo vốn chủ và 90.711 triệu theo báo cáo lưu chuyển tiền tệ. Tính giá mua trung bình biết số cổ phiếu giảm ròng là 343.526."

Phát hiện: (a) lợi nhuận tính bằng triệu USD, cổ phiếu bằng nghìn: chia thẳng ra `0,007465` sai đơn vị, nhân 1.000 mới được 7,465; (b) ba con số mua lại khác nhau (chênh tới 1,4 tỷ USD) và nguồn không nêu lý do; (c) số cổ phiếu giảm ròng đã trừ cổ phiếu phát hành, không phải số cổ phiếu mua; (d) đề thiếu số cổ phiếu mua gộp cả năm (có trong Note 10).

`Đáp án` EPS `= 112.010 triệu/15.004,697 triệu cổ phiếu ≈ 7,46 USD`. Từ dữ kiện của đề, giá mua trung bình **không tính được**; 264 USD không phải giá mua. Dữ kiện nằm ở Note 10 của 10-K (401.672 nghìn cổ phiếu mua, giá khoảng 222–226 USD tùy số tiền dùng).

## Sai ở đâu

Một học viên viết: "Biển Xanh mua lại 200 tỷ nên EPS tăng 2% nghĩa là giá trị cổ đông tăng 2%. SBC không tốn tiền nên không phải chi phí. Hòa Phát thưởng cổ phiếu 20% nên cổ đông giàu thêm 20%."

<details>
<summary>Mở sau khi tự tìm lỗi</summary>

1. EPS tăng không bằng giá trị tăng: nếu giá mua cao hơn giá trị nội tại, người ở lại thiệt (câu 4).
2. SBC không tốn tiền nhưng chuyển giá trị cho nhân viên bằng cách thêm cổ phiếu; phải phản ánh bằng một trong hai cách (trừ khỏi dòng tiền hoặc cộng vào số cổ phiếu), không bỏ.
3. Thưởng cổ phiếu 20% chia cùng một giá trị cho nhiều cổ phiếu hơn; tổng giá trị cổ đông sở hữu không tăng.
4. Không điều chỉnh EPS kỳ trước nên so sánh sai.

</details>

## Kiểm tra chuyển bài

Làm không nhìn mẫu; đạt khi đúng cả ba.

1. Công ty có 50 triệu cổ phiếu, lợi nhuận ròng 500 tỷ đồng, mua lại 100 tỷ ở giá 50.000. Tính EPS trước và sau.
2. Cổ phiếu thưởng tỷ lệ 10% (10:1). EPS trước thưởng 10.000. Tính EPS sau điều chỉnh.
3. Nêu ít nhất hai việc phải kiểm trước khi khen một đợt mua lại.

<details>
<summary>Mở sau khi tự làm</summary>

Tiêu chí đạt: câu 1 EPS trước `500 tỷ/50 triệu = 10.000`; mua `100 tỷ/50.000 = 2 triệu`, còn 48 triệu; EPS sau `≈ 10.417`. Câu 2 `10.000/1,1 ≈ 9.091`. Câu 3: giá mua so với giá trị nội tại; mua lại ròng sau SBC; nguồn tiền (FCFE hay vay); số cổ phiếu đã giảm thật chưa.

</details>

## Lỗi thường gặp

- Coi EPS tăng do mua lại là giá trị tăng.
- Bỏ SBC vì không chảy tiền; hoặc phản ánh cùng một khoản cấp phát hai lần.
- Tính "giá mua" từ số cổ phiếu giảm ròng.
- Không điều chỉnh EPS khi có cổ phiếu thưởng hoặc chia tách.

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị mua/bán/nắm giữ và không đánh giá chính sách của Apple hay Hòa Phát.
- Giá, giá trị nội tại và số cổ phiếu của Biển Xanh là giả định.
- Quy định thuế và phát hành cổ phiếu thay đổi theo thời gian và nơi; kiểm lại nguồn hiện hành trước khi áp dụng.

## Điều tôi vẫn chưa hiểu

- Với công ty tôi đọc, giá mua lại trung bình là bao nhiêu và so với giá trị nội tại tôi ước?
- SBC của công ty tôi đọc có đang được bù bằng mua lại, và tôi tính nó thế nào trong định giá?

## Nguồn Internet đã mở

Truy cập `2026-11-01`. Không suy ngày truy cập thành ngày xuất bản.

| Nguồn | Phạm vi | Dùng cho |
|---|---|---|
| [Apple Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Hoa Kỳ; US GAAP; kết thúc 27/09/2025; triệu USD, cổ phiếu nghìn | SBC, mua lại, cổ tức, số cổ phiếu, EPS, chương trình mua lại |
| [Damodaran, Data Update 8 for 2026](https://aswathdamodaran.blogspot.com/2026/02/data-update-8-for-2026-time-for.html) | Blog tác giả; 24/02/2026; thị trường toàn cầu | Mua lại chuyển giá trị giữa người bán và người ở lại; FCFE; cảnh báo trả quá FCFE |
| [BCTC hợp nhất kiểm toán FY2025 của Hòa Phát](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/03/20260327-hpg-bctc-hop-nhat-nam-2025-sau-kiem-toan.pdf) | VND; VAS; đã đọc trang in 7 và 39 | Cổ phiếu thưởng 20%, vốn góp, lợi nhuận chưa phân phối |

`CHƯA_BIẾT` Lý do ba số mua lại (89,3 tỷ, 90.052 và 90.711 triệu USD) khác nhau; mức ảnh hưởng của khoản nộp thuế State Aid lên dòng tiền FY2025; cách tính lãi cơ bản trên cổ phiếu của Hòa Phát (EPS năm trước 1.505 có thể đã điều chỉnh theo cổ phiếu thưởng, cần thuyết minh 38); nguồn thứ hai độc lập cho nhận định "SBC là chi phí thật" (đây là quy ước phương pháp của dự án).
