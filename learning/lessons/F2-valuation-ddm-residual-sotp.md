# Bài F2 — DDM, lợi nhuận thặng dư và tổng các bộ phận

- Ngày: `2026-10-27`
- Chốt dữ liệu lúc: `2026-10-27 12:04 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Tính ví dụ DDM, lợi nhuận thặng dư và SOTP; chọn phương pháp theo điều kiện và tránh tính trùng nợ.
- Bài trước liên quan: [009](009-valuation-multiples.md), [010](010-cost-of-capital.md), [011](011-dcf-reverse-dcf.md), [012](012-scenarios-margin-of-safety.md).
- Câu hỏi cốt lõi: Phương pháp định giá nào phù hợp với dòng tiền, tài sản và giai đoạn của doanh nghiệp?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/F2-fact-check.md), [phản biện](../reviews/F2-risk-review.md).

## Hiểu bài trong một phút

Các mô hình nhìn cùng câu hỏi từ những đầu vào khác nhau. Chiết khấu cổ tức (DDM) tập trung tiền phân phối cho cổ đông; lợi nhuận thặng dư bắt đầu từ giá trị sổ sách rồi tính phần vượt chi phí vốn chủ; tổng các bộ phận (SOTP) đánh giá các mảng riêng rồi ghép lại. Không mô hình nào tự tạo ra sự chắc chắn từ giả định yếu.

## 1. Chiết khấu cổ tức

`SỰ_THẬT` [Damodaran — Valuation](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/val.html) mô tả DDM là trường hợp định giá vốn chủ bằng giá trị hiện tại của cổ tức kỳ vọng. Công thức tăng trưởng ổn định `P0 = D1/(r − g)` chỉ dùng khi cổ tức kỳ tới D1 và tốc độ g bền vững theo giả định, r > g, cùng đồng tiền và cơ sở danh nghĩa/thực.

`KỊCH_BẢN` Cổ tức năm tới 2.000 VND/cổ phần, chi phí vốn chủ 10%/năm, tăng trưởng ổn định 2%/năm. `PHÉP_TÍNH` `P0 = 2.000/(0,10 − 0,02) = 25.000 VND/cổ phần`. Đây là đầu ra giả định, không là giá mục tiêu. Nếu r hoặc g thay đổi nhỏ, mẫu số thay đổi lớn; nếu r ≤ g, công thức này không hợp lệ.

[Damodaran — DDM](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/ddm.html) nêu mô hình tăng trưởng ổn định phù hợp hơn với doanh nghiệp tăng trưởng và đòn bẩy ổn định, có cổ tức cao gần dòng tiền tự do cho cổ đông (FCFE). Khi cổ tức thấp hoặc bằng không, cần xem tiền giữ lại và khả năng phân phối tương lai; có thể đối chiếu FCFE hoặc lợi nhuận thặng dư với giả định nhất quán, không coi cổ tức hiện tại bằng 0 là giá trị cổ phần bằng 0.

## 2. Lợi nhuận thặng dư

`SỰ_THẬT` [CFA Institute — Residual Income Valuation, chương trình 2026](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/residual-income-valuation) định nghĩa lợi nhuận thặng dư bằng lợi nhuận ròng trừ chi phí cơ hội vốn chủ; giá trị vốn chủ có thể được tính từ giá trị sổ sách cộng giá trị hiện tại của lợi nhuận thặng dư kỳ vọng, với các điều kiện kế toán phù hợp.

`KỊCH_BẢN` Vốn chủ đầu kỳ 100 tỷ VND, lợi nhuận ròng năm 1 là 15 tỷ, chi phí vốn chủ 10%; giả định lợi nhuận thặng dư sau năm 1 bằng 0 và không có điều chỉnh sổ sách ngoài giả định mô hình. `PHÉP_TÍNH` Thặng dư năm 1 = `15 − 100 × 10% = 5` tỷ; giá trị mô hình = `100 + 5/1,10 ≈ 104,55` tỷ. Nếu còn giá trị thặng dư sau năm 1 phải cộng phần đó; không tự giả định về 0 khi áp dụng thật.

## 3. SOTP và NAV

`KỊCH_BẢN` Hai mảng có giá trị hoạt động lần lượt 500 và 300 tỷ; tiền dư thừa 20, nợ vay 120, không có lợi ích thiểu số hoặc khoản điều chỉnh khác. `PHÉP_TÍNH` Giá trị vốn chủ mô hình = `500 + 300 + 20 − 120 = 700` tỷ VND. Đây là phép cộng các giá trị hoạt động trước khi điều chỉnh cấp công ty. Nếu một mảng đã được định giá bằng giá trị vốn chủ sau nợ, không trừ lại cùng khoản nợ của mảng đó.

NAV (giá trị tài sản ròng) thường là giá trị tài sản trừ nghĩa vụ theo phương pháp cụ thể; với bất động sản cần kiểm pháp lý, tỷ lệ sở hữu, thời điểm hoàn thành, chi phí, nợ và khả năng chuyển nhượng. NAV sổ sách và ước tính giá trị thị trường không tự bằng nhau.

## 4. Khi lợi nhuận bất thường hoặc âm

`Ý_KIẾN` Doanh nghiệp chu kỳ cần xem lợi nhuận qua nhiều giai đoạn và công suất, không áp đỉnh chu kỳ mãi mãi. Doanh nghiệp lỗ hoặc tăng trưởng cao cần giả định đường tới biên lợi nhuận, nhu cầu tái đầu tư, khả năng huy động vốn và pha loãng; không lấy P/E âm làm bằng chứng giá rẻ. Có thể dùng nhiều phương pháp như kiểm chéo nếu đầu vào nhất quán, không lấy trung bình cơ học các số không cùng phạm vi.

## Năm câu hỏi khi đọc

1. Đang định giá vốn chủ hay toàn bộ hoạt động, và ghép đúng tỷ lệ chiết khấu chưa?
2. Tăng trưởng và chi phí vốn có cùng đồng tiền, lạm phát và kỳ không?
3. Giá trị sổ sách, cổ tức và lợi nhuận có được dự báo nhất quán?
4. SOTP có cộng/trừ trùng tiền, nợ, chi phí công ty mẹ hoặc lợi ích thiểu số không?
5. Mô hình có đứng vững trong kịch bản xấu và khi giả định đổi không?

## Bài tập

1. D1 = 1.000 đồng, r = 12%, g = 2%: DDM một giai đoạn cho giá trị bao nhiêu?
2. Với r ≤ g có dùng công thức ổn định đó được không?
3. Vốn chủ đầu kỳ 200 tỷ, lợi nhuận 30 tỷ, chi phí vốn 10%: thặng dư năm một?
4. Mảng hoạt động 400 + 200 tỷ, tiền dư 30, nợ 100: vốn chủ mô hình?
5. Có nên trừ cùng một khoản nợ hai lần trong SOTP không?
6. Lợi nhuận đỉnh chu kỳ có tự là lợi nhuận bình thường dài hạn không?

## Đáp án

1. `1.000/(0,12 − 0,02) = 10.000` đồng/cổ phần, theo giả định.
2. Không; mẫu số không đáp ứng điều kiện mô hình tăng trưởng ổn định.
3. `30 − 200 × 10% = 10` tỷ VND.
4. `400 + 200 + 30 − 100 = 530` tỷ VND, với giả định không điều chỉnh khác.
5. Không; xác định giá trị từng mảng là vốn chủ hay hoạt động trước khi cộng trừ.
6. Không; cần xem chu kỳ, đầu tư và điều kiện bình thường hóa.

## Lỗi thường gặp và ranh giới an toàn

Ghép dòng tiền vốn chủ với WACC, dùng g ≥ r, bỏ pha loãng, hoặc trừ nợ hai lần. Mọi đầu vào là giả định học tập, không là khuyến nghị hay giá mục tiêu.

## Điều tôi vẫn chưa hiểu

`CHƯA_BIẾT` Cổ tức, thặng dư, giá tài sản, nợ và tăng trưởng của một doanh nghiệp cụ thể; cần dữ liệu gốc và kịch bản có thể kiểm.

## Nguồn Internet đã mở

Truy cập `2026-10-27`: [Damodaran — Valuation](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/val.html), NYU Stern, trang không ghi ngày trong phần đọc; [Damodaran — DDM](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/ddm.html), không ghi ngày; [CFA Institute — Residual Income Valuation](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/residual-income-valuation), chương trình 2026. Số ví dụ hư cấu.
