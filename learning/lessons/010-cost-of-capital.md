# Bài 010 — Chi phí vốn: ke, kd, WACC và cách kiểm giả định

- Ngày viết lại: `2026-10-31`. Bản này **thay thế** bản 2026-10-26; biên bản kiểm cũ gắn mã băm cũ, không còn áp dụng.
- Chốt dữ liệu lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Nguồn số Apple: Form 10-K FY2025 mở ngày `2026-10-31`.
- Mục tiêu: Tính chi phí vốn cổ đông bằng CAPM, nợ sau thuế, WACC theo trọng số thị trường; gỡ và gắn lại beta theo đòn bẩy; kiểm nhất quán tiền tệ, thực/danh nghĩa; đọc độ nhạy.
- Bài trước liên quan: N4, N7, 003, 008. Học tiếp [011](011-dcf-reverse-dcf.md).
- Thời lượng: 2–3 phiên (A: mục 1–3; B: mục 4–6; C: bài tập).
- Tệp thực hành: [valuation.py](../practice/models/valuation.py) (hàm `capm`, `unlever`, `relever`, `wacc`, `convert_rate`) và [số Apple](../practice/models/apple_fy2025_inputs.csv).
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/010-fact-check.md), [phản biện](../reviews/010-risk-review.md).
- Câu hỏi cốt lõi: **Người cấp vốn đòi hỏi bao nhiêu để chấp nhận rủi ro của doanh nghiệp này, và ta kiểm con số ấy thế nào?**

## Hiểu bài này trong 1 phút

Vay tiền có lãi vay nhìn thấy trên hóa đơn. Vốn cổ đông không có hóa đơn lãi cố định, nhưng người góp vốn vẫn đòi phần bù cho thời gian và rủi ro; nếu doanh nghiệp không kiếm được ít nhất bằng mức đó trên vốn đã dùng, giá trị của cổ đông bị bào mòn. Chi phí vốn là **một ước tính**, dùng làm thước so với ROIC và làm tỷ lệ chiết khấu. Phần khó không phải công thức mà là giữ cho mọi đầu vào cùng tiền tệ, cùng ngày, cùng kỳ hạn.

## Ôn bài cũ hoặc kiểm tra đầu vào

1. N4: tăng tỷ lệ chiết khấu thì giá trị hiện tại của khoản nhận trong tương lai tăng hay giảm?
2. N7: xác suất do mình tự gán có phải dữ kiện đã kiểm chứng không?
3. 003: ROIC cần được so với đại lượng nào để kết luận có tạo giá trị không?
4. 008: lạm phát kỳ vọng ảnh hưởng thế nào tới lãi suất danh nghĩa?

<details>
<summary>Mở sau khi tự làm</summary>

Đáp án ngắn: (1) giảm; (2) không; (3) chi phí vốn tính nhất quán; (4) lạm phát kỳ vọng cao hơn thường đi cùng lãi suất danh nghĩa cao hơn, nhưng không là quan hệ cố định.

</details>

## Bài này làm gì và chưa làm gì

| Làm | Chưa làm |
|---|---|
| Dạy CAPM, chi phí nợ, WACC, gỡ/gắn beta, kiểm nhất quán | Không đưa WACC hiện hành của cổ phiếu cụ thể |
| Dùng số nợ và vốn thật của Apple để thấy trọng số sổ sách và thị trường khác nhau | Không dùng bảng ngành như mức chuẩn bắt buộc |
| Dạy đổi tỷ lệ giữa hai tiền tệ qua lạm phát | Không ước tính phần bù rủi ro quốc gia cho một nước cụ thể |

## 1. Hai người cấp vốn, hai yêu cầu

`SỰ_THẬT` Trang [Damodaran — Valuation](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/val.html) (mở 31/10/2026) viết chi phí vốn cổ đông theo CAPM là `ke = Rf + beta × (E(RM) − Rf)`, tức lãi suất phi rủi ro cộng beta nhân phần bù rủi ro; ta gọi phần bù là ERP (*equity risk premium*). Beta đo độ nhạy với rủi ro thị trường theo mô hình. Beta không đo mọi dạng rủi ro và không là thước chất lượng doanh nghiệp.

Chi phí nợ `kd` là chi phí vay **hiện tại** phù hợp rủi ro, không mặc định bằng coupon cũ. Nếu lãi vay trừ được thuế và doanh nghiệp có lãi để dùng lợi ích đó, chi phí nợ sau thuế là `kd×(1−T)`; doanh nghiệp đang lỗ có thể chưa dùng được lá chắn thuế.

## 2. Ví dụ trộn trọng số (hư cấu)

`KỊCH_BẢN` Doanh nghiệp phi tài chính hư cấu, cùng tiền tệ danh nghĩa: Rf 3%, beta 1,2, ERP 5%; kd 5%, thuế biên 25%; vốn chủ thị trường 70, nợ thị trường 30.

`PHÉP_TÍNH` `ke = 3% + 1,2×5% = 9%`. `kd sau thuế = 5%×0,75 = 3,75%`.
`WACC = 9%×0,70 + 3,75%×0,30 = 7,425%`.
Nếu chưa dùng được lá chắn thuế: `9%×0,70 + 5%×0,30 = 7,8%`.

WACC là mức trung bình có trọng số, **không** phải tổng ke + kd. Dòng tiền cho mọi người cấp vốn (FCFF) chiết khấu bằng WACC; dòng tiền riêng cổ đông chiết khấu bằng ke (bài 011).

## 3. Beta phụ thuộc đòn bẩy: gỡ rồi gắn lại

`SUY_LUẬN` Doanh nghiệp vay càng nhiều, rủi ro đặt lên cổ đông càng lớn, nên beta vốn chủ (`βL`) cao hơn beta của chính hoạt động kinh doanh (`βu`, beta không đòn bẩy). Khi lấy beta từ doanh nghiệp tương tự có cơ cấu vốn khác, phải gỡ đòn bẩy rồi gắn theo cơ cấu của doanh nghiệp mình. Slide FCFF của Damodaran ([fcff.pdf](https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/fcff.pdf)) có dạng gắn lại `βL = βu × (1 + (1−T) × D/E)` (ví dụ ở trang 4 của slide; chưa đối chiếu công thức tổng quát ngoài ví dụ đó). Công thức (Hamada, giả định nợ không rủi ro vỡ nợ, thuế biên cố định): `βu = βL/(1+(1−T)×D/E)` và `βL = βu×(1+(1−T)×D/E)`.

`KỊCH_BẢN` Công ty so sánh có βL = 1,3, D/E thị trường 0,5, thuế 25%.

`PHÉP_TÍNH` `βu = 1,3/(1+0,75×0,5) = 1,3/1,375 ≈ 0,9455`. Gắn lại:

| D/E mục tiêu | βL |
|---:|---:|
| 0,2 | 1,0873 |
| 0,5 | 1,3 |
| 1,0 | 1,6545 |

Dùng Rf 4%, ERP 5%: ở D/E = 0,5, `ke = 4%+1,3×5% = 10,5%`; với kd 7%, thuế 25% và trọng số vốn chủ 2/3, nợ 1/3:
`WACC = 10,5%×2/3 + 7%×0,75×1/3 = 7% + 1,75% = 8,75%`.

Giới hạn: công thức giả định lá chắn thuế và rủi ro nợ đơn giản; với nợ rủi ro cao hoặc cơ cấu vốn đổi nhanh, beta gắn lại chỉ là xấp xỉ. `Ý_KIẾN` Dùng nhiều doanh nghiệp so sánh và lấy trung vị, đừng dựa một beta.

## 4. Trọng số: giá trị thị trường, không phải sổ sách

## Ví dụ từ nguồn thật

`SỰ_THẬT` [Form 10-K FY2025 của Apple](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) (27/09/2025, triệu USD): thương phiếu 7.979; nợ dài hạn đến hạn 12.350 và không đến hạn 78.328; tổng nợ vay 98.657; tổng vốn chủ sổ sách 73.733 (10-K không nêu nguyên nhân; `SUY_LUẬN` vốn chủ kế toán nhỏ có thể liên quan việc mua lại cổ phiếu quy mô lớn, 90.711 triệu USD dòng tiền chi trong FY2025, nhưng vốn chủ thực tế còn tăng từ 56.950 lên 73.733 trong năm).

`PHÉP_TÍNH` Nợ/vốn chủ **sổ sách** `= 98.657/73.733 ≈ 1,34`. Nếu giả định giá trị thị trường vốn chủ là 3.500.000 (giả định bài học, không phải số liệu; ngày 30/10/2026 một nguồn thứ cấp ghi giá AAPL khoảng 345 USD, tức vốn hóa lớn hơn nhiều, nhưng với nợ nhỏ như vậy WACC gần như không đổi; người học thay bằng vốn hóa tra tại ngày làm bài), nợ/vốn chủ **thị trường** `≈ 0,028`.

Hai cách trọng số cho WACC khác nhau xa. `KỊCH_BẢN` với Rf 4%, beta 1,1, ERP 4,5% (giả định, tự cập nhật nguồn): `ke = 4% + 1,1×4,5% = 8,95%`; kd 4,5%, thuế 16% (lấy gần thuế suất **hiệu dụng** FY2025 là 15,6% chỉ để minh họa; lá chắn thuế của nợ phải dùng thuế **biên**, `CHƯA_BIẾT` ở đây; tác động nhỏ vì nợ chỉ khoảng 2,7% vốn thị trường).

| Trọng số | E | D | WACC |
|---|---:|---:|---:|
| Thị trường (E = 3.500.000) | 3.500.000 | 98.657 | **≈ 8,81%** |
| Sổ sách | 73.733 | 98.657 | ≈ 5,99% |

`SUY_LUẬN` Dùng trọng số sổ sách cho Apple kéo WACC xuống gần 6% chỉ vì vốn chủ kế toán nhỏ; đó là lỗi, vì người góp vốn đòi hỏi trên giá trị thị trường của phần góp. Với Apple, nợ chiếm tỷ trọng rất nhỏ nên `WACC ≈ ke`; mô hình đòn bẩy quan trọng hơn ở doanh nghiệp vay nhiều.

## 5. Nhất quán tiền tệ và thực/danh nghĩa

`SỰ_THẬT` Trang [Damodaran — Valuation](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/val.html) (mở 31/10/2026) nêu "Luật thứ nhất của định giá": không trộn dòng tiền với tỷ lệ chiết khấu không tương ứng (dòng tiền vốn chủ với chi phí vốn chủ, dòng tiền doanh nghiệp với WACC). `Ý_KIẾN` Cùng tinh thần, tỷ lệ chiết khấu phải cùng tiền tệ và cùng cơ sở thực/danh nghĩa với dòng tiền; trang trên không nêu rõ điều này nên cần nguồn khác khi kiểm duyệt.

`SUY_LUẬN` Damodaran ([Currency Choices in Valuation](https://aswathdamodaran.substack.com/p/currency-choices-in-valuation-10-04-16)) nêu chênh lệch lãi suất giữa hai tiền tệ phản ánh chênh lệch lạm phát kỳ vọng, nhưng trang này không viết công thức dạng nhân dưới đây; đó là dạng tính của người soạn, **giả định lãi suất thực hai đồng tiền bằng nhau**, và dùng cho Rf, không cho phần bù rủi ro cổ phiếu. `PHÉP_TÍNH` Đổi lãi suất giữa hai tiền tệ qua lạm phát kỳ vọng: `(1+r_VND) = (1+r_USD)×(1+π_VND)/(1+π_USD)`. `KỊCH_BẢN` r_USD 4%, lạm phát USD kỳ vọng 2,5%, lạm phát VND kỳ vọng 4%: `r_VND = 1,04×1,04/1,025 − 1 ≈ 5,52%`. Đây chỉ là xấp xỉ lý thuyết; thực tế còn phụ thuộc phần bù kỳ hạn, rủi ro quốc gia và biến động tỷ giá.

Tránh cộng trùng rủi ro: nếu ERP đã chứa phần bù cho thị trường mới nổi thì không cộng thêm phần bù quốc gia lần nữa; nếu dòng tiền đã bị chiết khấu bằng xác suất khủng hoảng thì không đồng thời cộng vào tỷ lệ.

## 6. Một con số không đủ: độ nhạy

`KỊCH_BẢN` Mô hình ổn định FCFF1 = 100, g 2%: WACC 7%, 8%, 9% cho EV lần lượt `100/0,05 = 2.000`; `100/0,06 ≈ 1.666,67`; `100/0,07 ≈ 1.428,57`.

`PHÉP_TÍNH` Với g = 2% và WACC quanh 7–9%, lệch một điểm phần trăm WACC làm EV đổi khoảng 14–17% (mức nhạy phụ thuộc `WACC − g`: khoảng cách càng hẹp càng nhạy). Vì thế một "WACC chính xác tới hai chữ số thập phân" là ảo tưởng; hãy báo cáo khoảng. Điểm dừng: ghi một giả định bạn muốn đổi, tính lại và giải thích vì sao kết quả đổi.

## Năm câu hỏi khi đọc

1. Dòng tiền thuộc mọi người cấp vốn hay riêng cổ đông?
2. Rf và dòng tiền cùng tiền tệ, cùng kỳ hạn phù hợp chưa?
3. Trọng số là giá trị thị trường hay sổ sách?
4. Beta lấy từ đâu; đã gỡ/gắn đòn bẩy theo cơ cấu vốn mục tiêu chưa?
5. Có cộng trùng rủi ro quốc gia hay rủi ro dòng tiền không?

## Bài tập — làm trước khi mở đáp án

1. Tính ke với Rf 3%, beta 1,2, ERP 5%.
2. Tính WACC ở ví dụ mục 2 (70/30).
3. Không dùng được lá chắn thuế: WACC bao nhiêu?
4. ke tăng từ 9% lên 11%, giữ kd 5%, thuế 25%, trọng số 70/30: WACC mới?
5. Gỡ beta: βL = 1,5, D/E 0,8, thuế 20%: tính βu.
6. Gắn βu đó cho doanh nghiệp có D/E 0,3, thuế 20%: βL mới?
7. Tính ke và WACC cho doanh nghiệp ở câu 6 với Rf 4%, ERP 5%, kd 6%, trọng số vốn chủ `1/(1+0,3)`.
8. Đổi lãi suất 5% danh nghĩa trong tiền A (lạm phát kỳ vọng 2%) sang tiền B (lạm phát kỳ vọng 6%).
9. (Chuyển giao) Vì sao không lấy WACC trung bình ngành Mỹ làm số chính xác cho doanh nghiệp ở thị trường khác?
10. (Chuyển giao) Chọn một doanh nghiệp niêm yết: lấy nợ vay và vốn hóa thị trường, tính D/E sổ sách và D/E thị trường; giải thích khoảng chênh.

## Đáp án

<details>
<summary>Mở sau khi tự làm</summary>

1. `PHÉP_TÍNH` `3%+1,2×5% = 9%`. Lưu ý ERP không phải tổng lợi suất thị trường.
2. `PHÉP_TÍNH` `9%×0,7 + 3,75%×0,3 = 6,3% + 1,125% = 7,425%`.
3. `PHÉP_TÍNH` `9%×0,7 + 5%×0,3 = 7,8%`; kiểm điều kiện thuế.
4. `PHÉP_TÍNH` `11%×0,7 + 3,75%×0,3 = 8,825%`.
5. `βu = 1,5/(1+0,8×0,8) = 1,5/1,64 ≈ 0,9146`.
6. `βL = 0,9146×(1+0,8×0,3) = 0,9146×1,24 ≈ 1,134`.
7. `ke = 4%+1,134×5% ≈ 9,67%`; trọng số vốn chủ `1/1,3 ≈ 0,7692`, nợ `0,2308`; `WACC ≈ 9,67%×0,7692 + 6%×0,8×0,2308 ≈ 7,44% + 1,11% ≈ 8,55%`.
8. `(1,05)×(1,06)/(1,02) − 1 ≈ 9,12%`.
9. Khác rủi ro, tiền tệ, cơ cấu vốn, phương pháp, ngày dữ liệu; chỉ là điểm tham chiếu để điều chỉnh có giải thích.
10. Rubric: có nguồn, ngày, đơn vị cho nợ và vốn hóa (2đ); tính đúng hai tỷ số (2đ); giải thích chênh lệch qua mua lại cổ phiếu, lợi nhuận giữ lại, giá thị trường khác giá sổ (2đ).

</details>

## Bài làm với dữ liệu thiếu hoặc lệch

Đề: "Công ty Beta ở Việt Nam, dòng tiền dự báo bằng VND danh nghĩa. Dùng Rf = 4,2% (lãi suất trái phiếu chính phủ Mỹ 10 năm), ERP 5%, beta 1,0 và chiết khấu. Nợ 800 tỷ VND, vốn chủ sổ sách 1.000 tỷ."

Phát hiện: (a) Rf bằng USD nhưng dòng tiền bằng VND; (b) không có lãi vay, thuế, trọng số thị trường (đã dùng sổ sách); (c) beta lấy từ đâu và đòn bẩy nào; (d) ERP đã chứa rủi ro quốc gia hay chưa; (e) kỳ hạn Rf với kỳ hạn dòng tiền.

`Đáp án` Không tính WACC được ngay. Phải (1) đổi Rf sang VND qua chênh lệch lạm phát hoặc dùng lãi suất VND tương đương, nêu giả định; (2) thu thập kd, thuế và vốn hóa thị trường; (3) gỡ/gắn beta; (4) ghi rõ việc có hay không cộng phần bù quốc gia. Nếu thiếu, ghi `CHƯA_BIẾT` và không bịa.

## Sai ở đâu

Một học viên viết cho Apple: "Vốn chủ sổ sách 73.733, nợ 98.657 nên nợ chiếm 57%. ke 8,95%, kd sau thuế 3,78%. WACC = 8,95%×0,43 + 3,78%×0,57 ≈ 6,0%. Dùng 6% chiết khấu FCFF."

<details>
<summary>Mở sau khi tự tìm lỗi</summary>

1. Trọng số sổ sách thay cho thị trường; vốn chủ thị trường lớn hơn sổ sách nhiều lần.
2. Beta 1,1 lấy từ thị trường đã phản ánh nợ rất thấp so với vốn thị trường; không nhất quán với cơ cấu 57% nợ.
3. Hạ WACC tạo giá trị cao giả tạo (mục 6: 1 điểm WACC đổi giá trị 14–17%).
4. Không ghi nguồn và ngày cho ERP, Rf.

</details>

## Kiểm tra chuyển bài

Làm không nhìn mẫu; đạt khi đúng cả ba.

1. Rf 3,5%, beta 0,9, ERP 5%, kd 6%, thuế 20%, vốn chủ 60, nợ 40: tính ke và WACC.
2. Lãi suất danh nghĩa 8% trong tiền A (lạm phát kỳ vọng 5%) sang tiền B (lạm phát kỳ vọng 2%).
3. Nêu hai kiểm tra nhất quán bạn phải làm trước khi dùng một WACC.

<details>
<summary>Mở sau khi tự làm</summary>

Tiêu chí đạt: câu 1 `ke = 3,5%+4,5% = 8%`; `WACC = 8%×0,6 + 6%×0,8×0,4 = 4,8% + 1,92% = 6,72%`. Câu 2 `1,08×1,02/1,05 − 1 ≈ 4,91%`. Câu 3: tiền tệ/kỳ hạn của Rf khớp dòng tiền và trọng số thị trường (hoặc thực/danh nghĩa, cộng trùng rủi ro).

</details>

## Lỗi thường gặp

- Gọi lợi nhuận giữ lại là vốn miễn phí.
- Cộng ke với kd thay vì dùng trọng số.
- Dùng lãi nợ cũ thay chi phí huy động hiện tại mà không giải thích.
- Lấy lợi ích thuế khi chưa dùng được.
- Trọng số sổ sách thay vì thị trường.
- Ghép khác tiền tệ, hoặc thực với danh nghĩa, hoặc cộng trùng rủi ro quốc gia.

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị mua/bán/nắm giữ cá nhân hóa.
- Mọi giả định (Rf, ERP, beta, vốn hóa) là `KỊCH_BẢN`, không phải số thị trường hiện hành; người học tự cập nhật nguồn tại ngày dùng.
- Trước khi áp dụng cho thị trường khác, kiểm lại nguồn gốc, quy định và chuẩn kế toán tại đó.

## Điều tôi vẫn chưa hiểu

- CAPM bỏ sót những rủi ro nào, và tôi có chấp nhận phần bỏ sót đó không?
- Cơ cấu vốn tương lai của công ty có khác hiện tại không?
- Phần bù rủi ro quốc gia cho thị trường tôi quan tâm lấy từ nguồn nào, cập nhật khi nào?

## Nguồn Internet đã mở

Truy cập `2026-10-31`. Không suy ngày truy cập thành ngày xuất bản.

| Nguồn | Phạm vi | Dùng cho |
|---|---|---|
| [Apple Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Hoa Kỳ; US GAAP; 27/09/2025; triệu USD | Số nợ, vốn chủ, mua lại cổ phiếu |
| [Damodaran — Valuation](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/val.html) | Phương pháp; ngày phiên bản `CHƯA_BIẾT`; mở 31/10/2026 | CAPM, ghép dòng tiền với tỷ lệ chiết khấu |
| [Damodaran — FCFF notes](https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/fcff.pdf) | Slide, ví dụ năm 2000 | Gắn lại beta theo D/E |
| [Damodaran — Currency Choices in Valuation](https://aswathdamodaran.substack.com/p/currency-choices-in-valuation-10-04-16) | Bài viết; ngày đăng ghi trên trang 16/04/2010 (cần kiểm lại) | Dòng tiền và tỷ lệ cùng tiền tệ; chênh lệch lạm phát |

`CHƯA_BIẾT` Dạng nhân của công thức đổi lãi suất qua lạm phát chưa có nguồn chính thức nêu rõ. Công thức gắn/gỡ beta (Hamada) và đổi lãi suất qua lạm phát là kiến thức tiêu chuẩn cần đối chiếu nguồn khi kiểm duyệt.
