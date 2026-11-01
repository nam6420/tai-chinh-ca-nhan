# Bài F2 — DDM, lợi nhuận thặng dư và tổng các bộ phận

- Ngày viết lại: `2026-10-31`. Bản này **thay thế** bản 2026-10-27; biên bản kiểm cũ gắn mã băm cũ, không còn áp dụng.
- Chốt dữ liệu lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Nguồn số Apple: Form 10-K FY2025 mở ngày `2026-10-31`.
- Mục tiêu: Tính DDM (một và hai giai đoạn), lợi nhuận thặng dư (RIM) và SOTP trên ví dụ đủ dữ kiện; chọn phương pháp theo điều kiện; tránh tính trùng nợ và quyền lợi thiểu số; nhận ra khi phương pháp **không** áp dụng được.
- Bài trước liên quan: [009](009-valuation-multiples.md), [010](010-cost-of-capital.md), [011](011-dcf-reverse-dcf.md), [012](012-scenarios-margin-of-safety.md).
- Thời lượng: 3 phiên (A: DDM; B: RIM; C: SOTP, chọn phương pháp và bài tập).
- Tệp thực hành: [valuation.py](../practice/models/valuation.py), hàm `gordon`, `ddm_two_stage`, `residual_income`, `sotp`.
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/F2-fact-check.md), [phản biện](../reviews/F2-risk-review.md).
- Câu hỏi cốt lõi: **Phương pháp định giá nào khớp với cách doanh nghiệp này tạo và trả tiền cho cổ đông, và khi nào phương pháp ấy ngừng hợp lệ?**

## Hiểu bài này trong 1 phút

DCF (bài 011) không phải công cụ duy nhất. Ba phương pháp thay thế trả lời ba câu hỏi khác nhau. **DDM** (*dividend discount model*, chiết khấu cổ tức): giá trị là cổ tức tương lai quy về hôm nay, hợp khi cổ tức ổn định và dự đoán được. **RIM** (*residual income model*, lợi nhuận thặng dư): giá trị = vốn chủ sổ sách + phần lợi nhuận vượt chi phí vốn; hợp khi sổ sách phản ánh khá tốt tài sản, ví dụ nhiều tổ chức tài chính. **SOTP** (*sum of the parts*, tổng các bộ phận): định giá riêng từng bộ phận khác bản chất rồi cộng; hợp với tập đoàn nhiều mảng. Mỗi phương pháp có một điều kiện; vi phạm điều kiện thì con số vô nghĩa dù phép tính đúng.

## Ôn bài cũ hoặc kiểm tra đầu vào

1. 010: vì sao dòng tiền cổ đông dùng chi phí vốn cổ đông (ke), không dùng WACC?
2. 011: từ EV sang vốn chủ phải làm gì với nợ, tiền?
3. 009: vì sao so P/E giữa hai công ty khác cơ cấu nợ dễ sai?
4. 011: điều kiện của công thức giá trị cuối kỳ là gì?

<details>
<summary>Mở sau khi tự làm</summary>

Đáp án ngắn: (1) vì dòng tiền đã sau chủ nợ; (2) trừ nợ, cộng tiền, điều chỉnh khoản khác; (3) vì lợi nhuận sau lãi vay bị ảnh hưởng đòn bẩy; (4) tỷ lệ chiết khấu lớn hơn tăng trưởng dài hạn.

</details>

## Bài này làm gì và chưa làm gì

| Làm | Chưa làm |
|---|---|
| Ba phương pháp với số đủ dữ kiện, tự tái lập được | Không mô hình ngân hàng thực tế (xem 013, F4) |
| Dùng số Apple để chỉ ra khi nào DDM và RIM không áp dụng | Không định giá Apple |
| Quy tắc tránh tính trùng nợ và quyền lợi thiểu số | Không dạy định giá bất động sản theo NAV chi tiết (xem F3) |

## 1. DDM: giá trị bằng cổ tức quy về hôm nay

`SỰ_THẬT` Trang [Damodaran — Gordon DDM](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/ddm.html) (mở 31/10/2026) nêu giá = `DPS1/(r − g)` và g không vượt tăng trưởng nền kinh tế quá 1–2 điểm. `PHÉP_TÍNH` Mô hình Gordon (một giai đoạn, tăng trưởng đều mãi mãi): `V0 = D1/(ke − g)` với `ke > g`. `SUY_LUẬN` Trong nhất quán nội tại, `g ≈ tỷ lệ giữ lại × ROE`: g, payout và ROE không độc lập.

`KỊCH_BẢN` Cổ tức năm tới `D1 = 4`, `ke = 10%`, `g = 3%`: `V0 = 4/0,07 = 57,14`. Độ nhạy: `g = 4%` cho `4/0,06 = 66,67` (tăng 16,7%); `ke = 11%` cho `4/0,08 = 50` (giảm 12,5%). Cũng như 011, giá nhạy khi `ke` sát `g`.

Hai giai đoạn: tăng nhanh `n` năm rồi ổn định.

`KỊCH_BẢN` `D0 = 3`, tăng 8%/năm trong 5 năm, sau đó 3%/năm mãi; `ke = 10%`.

`PHÉP_TÍNH` Cổ tức năm 1–5: `3,24; 3,5; 3,78; 4,08; 4,41` (làm tròn); `V = Σ D_t/1,1^t + [D5×1,03/(0,10−0,03)]/1,1^5 ≈ 54,47`. Thử tự cộng và đối chiếu với `ddm_two_stage(3, 0.08, 5, 0.03, 0.10)`.

Điều kiện hợp lệ: cổ tức đại diện cho dòng tiền cổ đông có thể nhận. Nếu doanh nghiệp giữ lại tiền hoặc trả cổ đông bằng cách khác thì DDM thấp hơn thực chất. Mục "Ví dụ từ nguồn thật" bên dưới cho thấy một trường hợp như vậy.

## 2. RIM: sổ sách cộng phần thặng dư

`PHÉP_TÍNH` `V0 = B0 + Σ RI_t/(1+ke)^t` với `RI_t = LN_t − ke×B_{t−1}` (lợi nhuận trừ chi phí vốn trên vốn chủ đầu kỳ); sổ sách tăng theo `B_t = B_{t−1} + LN_t×(1−payout)`. Ý nghĩa: nếu ROE bằng đúng `ke`, thặng dư bằng 0 và giá trị bằng sổ sách; chỉ phần ROE vượt `ke` mới thêm giá trị.

`KỊCH_BẢN` Tổ chức tài chính hư cấu: `B0 = 1.000`, `ke = 12%`, tỷ lệ chi trả 40%; ROE năm 1–5 giảm dần `18%, 16%, 14%, 13%, 12%`; sau năm 5 ROE bằng ke nên không còn thặng dư.

`PHÉP_TÍNH` Năm 1: `LN = 1.000×0,18 = 180`, `RI = 180 − 0,12×1.000 = 60`; `B1 = 1.000 + 180×0,6 = 1.108`. Năm 2: `LN = 1.108×0,16 = 177,28`, `RI = 177,28 − 132,96 = 44,32`; `B2 = 1.108 + 177,28×0,6 = 1.214,37`. Thặng dư các năm: `60; 44,32; 24,29; 13,16; 0`; giá trị hiện tại tổng `≈ 114,56`. **`V0 = 1.000 + 114,56 = 1.114,56`**, tức `≈ 1,11` lần sổ sách.

Kiểm tính hợp lý: nếu ROE giữ ở 12% (bằng ke) cả 5 năm, `V0 = 1.000` đúng bằng sổ sách. Đây là phép thử nên làm với mọi mô hình RIM bạn dựng.

Điều kiện hợp lệ: sổ sách phản ánh khá giá trị tài sản; quan hệ sạch (*clean surplus*): mọi thay đổi vốn chủ đi qua lợi nhuận hoặc cổ tức; nếu có khoản bỏ qua lợi nhuận (như đánh giá lại) phải xử lý riêng.

## Ví dụ từ nguồn thật

`SỰ_THẬT` [Form 10-K FY2025 của Apple](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) (kỳ 27/09/2025 và 28/09/2024, US GAAP, triệu USD): lợi nhuận sau thuế FY2025 112.010; cổ tức trả 15.421; mua lại cổ phiếu 90.711; tổng vốn chủ cuối FY2025 73.733 và cuối FY2024 56.950.

`PHÉP_TÍNH` (1) Cổ tức/lợi nhuận `= 15.421/112.010 ≈ 13,8%`; tổng chi trả cổ đông (cổ tức + mua lại) `= 106.132 = 94,8%` lợi nhuận. Một DDM chỉ dùng cổ tức sẽ bỏ sót hơn 85% phần trả cổ đông. Cách xử lý: dùng **tổng chi trả** (cổ tức + mua lại ròng) trên tổng vốn chủ, hoặc chuyển sang FCFE (bài 011). (2) ROE `= 112.010/73.733 ≈ 151,9%` theo vốn chủ cuối kỳ, `≈ 171,4%` theo bình quân `(73.733+56.950)/2 = 65.341,5`. `SUY_LUẬN` ROE cao như vậy chủ yếu phản ánh vốn chủ kế toán nhỏ so với lợi nhuận (10-K không nêu nguyên nhân; mua lại cổ phiếu quy mô lớn là một lý do khả dĩ, nhưng vốn chủ còn tăng 56.950 → 73.733 trong năm), nên không dùng được như thước đo hiệu quả vốn hoạt động; ROIC của Apple `CHƯA_BIẾT` trong bài này. Về kỹ thuật, RIM vẫn **chạy được** nếu xử lý mua lại nhất quán (coi là chi trả trong `payout`); khi quan hệ sạch đúng và tính đủ, RIM và DDM hội tụ về cùng giá trị. Ở Apple quan hệ sạch bị phá bởi SBC (12.863) và thu nhập toàn diện khác, nên cần xử lý riêng (vốn chủ tăng 56.950 → 73.733 không chỉ bằng lợi nhuận trừ chi trả). Với `B0 = 73.733` và ROE ~150%, gần như toàn bộ giá trị nằm ở thặng dư, nên rất nhạy giả định ROE suy giảm. `Ý_KIẾN` Vì vậy RIM không phải công cụ chính cho Apple; câu hỏi của bài tập chấm theo lập luận, không theo đáp án "không áp dụng".

`SUY_LUẬN` Vì vậy phải kiểm điều kiện trước khi chọn phương pháp, không chọn vì "mô hình này nghe thuyết phục".

## 3. SOTP: cộng các bộ phận, trừ một lần

`SUY_LUẬN` SOTP hợp khi các bộ phận có bản chất và bội số khác nhau (ví dụ mảng tăng trưởng và mảng chu kỳ). Quy trình: (1) định giá EV từng bộ phận bằng bội số hoặc DCF; (2) trừ chi phí trụ sở không phân bổ; (3) cộng thành EV hợp nhất; (4) trừ nợ ròng hợp nhất **một lần** và quyền lợi thiểu số; (5) chia số cổ phần pha loãng. Nợ nằm ở cấp nào, chỉ trừ một lần.

`KỊCH_BẢN` Tập đoàn hư cấu: mảng A có EBITDA 80, bội số EV/EBITDA 7; mảng B có EBITDA 40, bội số 10; chi phí trụ sở chưa phân bổ −20 (áp bội số 7); nợ ròng hợp nhất 150; cổ đông thiểu số sở hữu 20% mảng B; 50 cổ phần.

`PHÉP_TÍNH` EV(A) `= 560`; EV(B) `= 400`; chi phí trụ sở `−140`; **EV hợp nhất 820**. Trừ nợ ròng `150`, trừ thiểu số `0,20×400 = 80` (**giả định mảng B không có nợ ròng riêng**, nên 20% EV bằng 20% vốn chủ của B; nếu B có nợ, thiểu số tính trên vốn chủ của B nhỏ hơn 80): vốn chủ **590**; giá `590/50 = 11,8`. Nếu áp thêm chiết khấu cấu trúc tập đoàn 15% (giả định), vốn chủ `= 590×0,85 = 501,5`; giá `10,03`. Bội số mỗi mảng lấy từ nhóm so sánh nào, đã đồng nhất kỳ và đơn vị chưa: `CHƯA_BIẾT` trong ví dụ hư cấu.

Lỗi hay gặp: trừ nợ riêng từng mảng **và** trừ nợ hợp nhất (tính trùng); quên thiểu số; quên chi phí trụ sở; dùng bội số của mảng đỉnh chu kỳ.

## 4. Khi lợi nhuận bất thường hoặc âm

`SUY_LUẬN` Lợi nhuận âm hoặc bất thường làm P/E, ROE vô nghĩa. Cách xử lý: chuẩn hóa lợi nhuận qua chu kỳ; dùng bội số doanh thu hoặc EBITDA nếu biên còn dương; định giá theo kịch bản biên hồi phục (DCF với chuỗi biên rõ). Ghi rõ giả định, đừng để một năm đột biến quyết định kết quả. Chủ đề này sẽ đào sâu ở bài về chuẩn hóa lợi nhuận và công ty chu kỳ.

## 5. Chọn phương pháp: bảng quyết định

| Đặc điểm doanh nghiệp | Phương pháp hợp | Điều kiện kiểm |
|---|---|---|
| Cổ tức ổn định, payout rõ | DDM | Cổ tức đại diện dòng tiền cổ đông; `ke > g` |
| Chi trả qua mua lại lớn | FCFE hoặc tổng chi trả | Tính mua lại ròng sau phát hành mới |
| Tổ chức tài chính, sổ sách đáng tin | RIM (cùng 013, F4) | Sổ sách khá sát giá trị; quan hệ sạch |
| Vốn chủ kế toán rất nhỏ so với lợi nhuận | RIM chạy được nhưng thận trọng; ưu tiên FCFE hoặc tổng chi trả | Nhạy giả định ROE suy giảm; mua lại xử lý nhất quán |
| Tập đoàn nhiều mảng khác bản chất | SOTP | Không tính trùng nợ; có thiểu số |
| Doanh nghiệp phi tài chính, dòng tiền ổn định | DCF (011) | Cầu nối đủ khoản |

## Năm câu hỏi khi đọc

1. Dòng tiền được chiết khấu có phải dòng tiền cổ đông thật sự nhận không?
2. Điều kiện của phương pháp (sổ sách sạch, payout, ke > g) có đúng với doanh nghiệp này không?
3. Nợ và quyền lợi thiểu số đã trừ đúng một lần ở đúng cấp chưa?
4. Phần lợi nhuận bất thường đã chuẩn hóa chưa?
5. Giả định nào chi phối kết quả?

## Bài tập — làm trước khi mở đáp án

1. `D1 = 5`, `ke = 9%`, `g = 3%`: tính `V0`.
2. Cùng dữ kiện câu 1 nhưng `ke = 10%`: `V0` đổi bao nhiêu %?
3. RIM: `B0 = 500`, `ke = 10%`, ROE năm 1 là 15%, payout 50%: tính `LN1`, `RI1` và `B1`.
4. Nếu ROE luôn bằng `ke`, `V0` bằng bao nhiêu và vì sao?
5. SOTP: mảng X EBITDA 60 × 8, mảng Y EBITDA 30 × 6, nợ ròng 100, không thiểu số, 20 cổ phần: tính giá mỗi cổ phần.
6. Trong câu 5, nếu trừ nợ ròng của từng mảng (40 và 60) và trừ thêm 100 nợ hợp nhất, lỗi gì?
7. Từ dữ kiện Apple ở mục Ví dụ từ nguồn thật: tính tổng chi trả/lợi nhuận và giải thích vì sao DDM cổ tức đơn thuần không phù hợp.
8. Vì sao RIM không phải công cụ chính cho Apple dù công thức tính được và, nếu xử lý mua lại nhất quán, đồng nhất với DDM tổng chi trả?
9. (Chuyển giao) Chọn một công ty trả cổ tức ổn định; lấy cổ tức 5 năm, tính tăng trưởng trung bình, dựng Gordon với `ke` do bạn giả định có lý do; viết một câu về điều kiện hợp lệ.
10. (Chuyển giao) Chọn một tập đoàn nhiều mảng; từ báo cáo bộ phận, lập bảng SOTP với nhóm so sánh cho từng mảng, ghi rõ nợ và thiểu số.

## Đáp án

<details>
<summary>Mở sau khi tự làm</summary>

1. `PHÉP_TÍNH` `5/(0,09−0,03) = 83,33`.
2. `5/(0,10−0,03) = 71,43`; giảm `(83,33−71,43)/83,33 ≈ 14,3%`.
3. `LN1 = 500×0,15 = 75`; `RI1 = 75 − 0,10×500 = 25`; `B1 = 500 + 75×0,5 = 537,5`.
4. `V0 = B0`, vì thặng dư mỗi năm bằng 0: không có lợi nhuận vượt chi phí vốn.
5. `EV = 60×8 + 30×6 = 480+180 = 660`; trừ nợ ròng 100: vốn chủ 560; giá `28`.
6. Tính trùng nợ: nợ đã được trừ ở cấp hợp nhất nên trừ thêm ở từng mảng làm vốn chủ thấp hơn thực chất.
7. `(15.421+90.711)/112.010 ≈ 94,8%`; cổ tức chỉ 13,8%; DDM cổ tức đơn thuần bỏ sót phần mua lại (hơn 85% chi trả).
8. Vốn chủ kế toán nhỏ làm ROE rất cao (khoảng 150–170%) nên giá trị RIM dồn vào thặng dư và rất nhạy giả định suy giảm ROE; ROE đó không phải thước hiệu quả vốn hoạt động. Về lý thuyết, nếu quan hệ sạch đúng và mua lại tính là chi trả thì RIM và DDM tổng chi trả cho cùng giá trị; vì thế đây là hạn chế thực hành (độ nhạy, khó ước lượng), không phải phép tính sai. Chấm theo lập luận. Lưu ý quan hệ sạch của Apple còn bị SBC phá: SBC ghi vào vốn chủ là 13.246 trong báo cáo vốn chủ, khác 12.863 trong báo cáo dòng tiền, và thuế trả khi ròng cổ phiếu thưởng 5.960 làm giảm vốn chủ.
9. Rubric: nguồn và kỳ cổ tức (1đ); tăng trưởng tính đúng (1đ); `ke` có lý do (1đ); điều kiện hợp lệ nêu đúng (1đ).
10. Rubric: bội số mỗi mảng có nhóm so sánh và nguồn (3đ); nợ trừ một lần và thiểu số xử lý (2đ); ghi giả định (1đ).

</details>

## Bài làm với dữ liệu thiếu hoặc lệch

Đề: "Tập đoàn Kappa có mảng A (EBITDA 100, bội số 8) và mảng B (lợi nhuận sau thuế 30, P/E 12). Nợ ròng 200. Có 40 cổ phần. Hãy cộng hai mảng và tính giá cổ phần."

Phát hiện: (a) bội số mảng A là EV/EBITDA (ra EV), mảng B là P/E (ra vốn chủ): không cộng trực tiếp được; (b) nợ ròng 200 của cấp nào, đã nằm trong mảng B chưa; (c) chi phí trụ sở, thiểu số, pha loãng chưa nêu; (d) kỳ và đơn vị chưa nêu.

`Đáp án` Phải quy hai mảng về cùng cơ sở (cùng EV hoặc cùng vốn chủ), nêu nợ nằm ở đâu, rồi tính. Nếu thiếu dữ kiện thì ghi `CHƯA_BIẾT` và đưa các giả định thay thế có nhãn `KỊCH_BẢN`.

## Sai ở đâu

Học viên viết về Apple: "Apple trả cổ tức 15.421; tôi dùng Gordon với g 8% và ke 8,9% nên giá trị rất lớn. ROE 152% nên RIM cho thặng dư khổng lồ. Hai phương pháp đều cho giá cao nên Apple chắc chắn đáng mua."

<details>
<summary>Mở sau khi tự tìm lỗi</summary>

1. `g = 8%` sát `ke = 8,9%`: phình giá trị, vi phạm điều kiện công thức.
2. DDM cổ tức bỏ sót mua lại (mục Ví dụ từ nguồn thật).
3. RIM rất nhạy khi vốn chủ sổ sách nhỏ so với lợi nhuận; ROE 152% không phải thước hiệu quả vốn hoạt động; "khổng lồ" là dấu hiệu nên nghi ngờ giả định, không phải tín hiệu giá cao.
4. Hai phương pháp cùng sai điều kiện không thành bằng chứng; kết luận "chắc chắn đáng mua" không có cơ sở và vượt quá dữ kiện (bài học không đưa kết luận mua/bán).
5. Không có độ nhạy hay kịch bản.

</details>

## Kiểm tra chuyển bài

Làm không nhìn mẫu; đạt khi đúng cả ba.

1. `D1 = 6`, `ke = 11%`, `g = 4%`: tính `V0`. Đổi `g = 5%`: đổi bao nhiêu %?
2. `B0 = 800`, `ke = 10%`, ROE năm 1 là 14%, payout 50%: tính `RI1` và `B1`.
3. Nêu một điều kiện làm cho RIM không áp dụng được và một điều kiện làm DDM bỏ sót giá trị.

<details>
<summary>Mở sau khi tự làm</summary>

Tiêu chí đạt: câu 1 `V0 = 6/0,07 = 85,71`; `g=5%`: `6/0,06 = 100`, tăng `16,7%`. Câu 2 `LN1 = 112`; `RI1 = 112−80 = 32`; `B1 = 800+112×0,5 = 856`. Câu 3: vốn chủ kế toán méo (mua lại lớn, đánh giá lại ngoài lợi nhuận) với RIM; chi trả cổ đông chủ yếu qua mua lại hoặc giữ tiền với DDM.

</details>

## Lỗi thường gặp

- Dùng `g ≥ ke`, hoặc g sát ke.
- DDM cổ tức khi phần lớn chi trả qua mua lại.
- RIM khi sổ sách méo.
- SOTP trừ nợ hai lần, quên thiểu số hoặc chi phí trụ sở.
- Cộng EV với vốn chủ trong cùng bảng.
- Dùng một năm lợi nhuận bất thường làm mốc.

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị mua/bán/nắm giữ cá nhân hóa.
- Số hư cấu là `KỊCH_BẢN`; số Apple là lịch sử đã công bố, không phải dự báo hay định giá Apple.
- Trước khi áp dụng cho thị trường khác, kiểm lại chuẩn kế toán và thuế tại đó.

## Điều tôi vẫn chưa hiểu

- Với tổ chức tài chính thật, tôi điều chỉnh sổ sách thế nào cho RIM?
- Chiết khấu cấu trúc tập đoàn có cơ sở dữ liệu nào?
- Khi nào nên dùng tổng chi trả thay vì FCFE?

## Nguồn Internet đã mở

Truy cập `2026-10-31`. Không suy ngày truy cập thành ngày xuất bản.

| Nguồn | Phạm vi | Dùng cho |
|---|---|---|
| [Apple Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Hoa Kỳ; US GAAP; kỳ 27/09/2025 và 28/09/2024; triệu USD | Lợi nhuận, cổ tức, mua lại (số dòng tiền; báo cáo vốn chủ ghi số hơi khác, như 90.052 và 15.413), vốn chủ |
| [Damodaran — Gordon DDM](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/ddm.html) | Phương pháp; ngày `CHƯA_BIẾT` | Công thức Gordon, giới hạn g |
| [CFA — Residual Income Valuation](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/residual-income-valuation) | Refresher reading 2026 | Công thức RIM |
| [Wikipedia — Sum-of-the-parts](https://en.wikipedia.org/wiki/Sum-of-the-parts_analysis) | Nguồn thứ cấp; sửa lần cuối 05/09/2026 | Định nghĩa SOTP |

Trang Damodaran Gordon DDM xác nhận công thức Gordon. [CFA Institute — Residual Income Valuation](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/residual-income-valuation) (bản 2026) nêu `V0 = B0 + Σ RI/(1+r)^t`; trang không nêu điều kiện quan hệ sạch, nên điều kiện đó và phần "RIM hội tụ với DDM" chưa có nguồn mở được (`CHƯA_BIẾT`). [Wikipedia — Sum-of-the-parts](https://en.wikipedia.org/wiki/Sum-of-the-parts_analysis) (nguồn thứ cấp) định nghĩa SOTP; việc xử lý thiểu số và chi phí trụ sở chưa có nguồn mở được. Phép tính tái lập bằng [valuation.py](../practice/models/valuation.py).
