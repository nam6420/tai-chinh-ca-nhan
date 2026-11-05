# Bài N4 — Giá trị thời gian của tiền và lợi suất

- Ngày: `2026-11-02`
- Chốt dữ liệu lúc: `2026-11-02 14:28 Asia/Ho_Chi_Minh`
- Mục tiêu: Tính lãi kép, giá trị hiện tại, lợi suất theo năm và lợi suất thực; biết giới hạn khi có góp/rút thêm tiền.
- Bài trước liên quan: Nhánh doanh nghiệp: [002](002-finding-a-cheap-stock.md); nhánh quỹ: N1 và N5A. Học tiếp 003 hoặc N7.
- Thời lượng: Hai hoặc ba phiên ngắn theo điểm dừng; chưa đo thời gian học thực tế.
- Câu hỏi cốt lõi: **Một đồng nhận trong tương lai tương đương bao nhiêu hôm nay?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

## Hiểu bài này trong 1 phút

Nhận 100 hôm nay và 100 sau ba năm khác nhau vì thời gian sử dụng tiền, lạm phát và rủi ro. Lãi kép đi từ hôm nay tới tương lai; chiết khấu đi ngược lại. Lãi suất trong bài là giả định học tập, không phải mức sinh lời được bảo đảm.

## Ôn bài cũ hoặc kiểm tra đầu vào

Tiền nhận từ khách có luôn bằng doanh thu không? Không. Trước khi so hai khoản tiền, thêm câu hỏi: nhận lúc nào? Nhánh quỹ chưa học kế toán chỉ cần xác định số tiền đầu kỳ, cuối kỳ và thời gian.

## Bài này làm gì và chưa làm gì

Dạy một khoản đầu tư với số kỳ rõ; dòng tiền giữa kỳ được đánh dấu để học tiếp ở N5B. Không chọn lãi suất chiết khấu thực tế cho một cổ phiếu.

## Phiên 1 — Tiền sinh thêm trên cả phần lãi cũ

`SỰ_THẬT` Tài liệu giáo dục của California BOE trình bày giá trị thời gian bằng toán lãi kép. [BOE](https://www.boe.ca.gov/info/tvm/lesson1.html). Với một khoản đầu, lãi nhập gốc mỗi kỳ, không góp/rút và tỷ lệ cố định: `FV = PV × (1+r)^n`, trong đó PV là giá trị hôm nay, FV tương lai, r tỷ lệ mỗi kỳ, n số kỳ.

`KỊCH_BẢN` 100 triệu đồng, 10%/năm trong hai năm, bỏ thuế/phí. `PHÉP_TÍNH` Năm một 110; năm hai `110×1,10=121`. Tổng tăng 21%, không phải 20%. Nếu tỷ lệ thay đổi, nhân các `(1+r_t)`, không lấy một tỷ lệ tùy ý.

### Đi ngược thời gian: chiết khấu

`PHÉP_TÍNH` Muốn nhận 121 triệu sau hai năm, dùng tỷ lệ giả định 10%/năm: `PV = 121/(1,10)^2 = 100 triệu`. Nếu r tăng 12%, PV = `121/1,12² ≈ 96,46 triệu`. Tỷ lệ cao hơn làm giá trị hiện tại thấp hơn khi giữ nguyên khoản nhận dương.

`SUY_LUẬN` Đây là phép quy đổi theo giả định, không chứng minh khoản tiền tương lai chắc chắn thu được. Rủi ro và thời điểm phải nhất quán với r; Bài 010 sẽ dạy cách đặt giả định r.

### Kiểm tra bằng phép tính ngược

`KỊCH_BẢN` Một khoản có thể nhận 150 triệu sau 3 năm. Giả sử để luyện toán ta dùng 8%/năm và khoản nhận chắc chắn; chưa thuế/phí. `PHÉP_TÍNH` 1,08³ =1,259712; PV =150/1,259712≈119,07 triệu. Dùng giá trị chưa làm tròn nhân ngược với 1,08³ phải về 150. Đổi tỷ lệ sang 10% nhưng giữ thời điểm và khoản nhận thì PV giảm: cùng số tiền tương lai nhưng cơ hội sử dụng tiền hiện tại được đặt cao hơn trong mô hình.

Một phép tính đúng chiều vẫn có thể trả lời sai câu hỏi. Nếu 150 triệu là doanh thu dự kiến, nó chưa phải tiền được phép chia cho nhà đầu tư. Nếu trả sau 3 năm nhưng có thể chậm thêm 1 năm, thời hạn chưa chắc là 3. Nếu dự báo có xác suất không trả, giả định “chắc chắn” đã bỏ phần khó nhất. N4 luyện quy đổi thời điểm, không chọn tỷ lệ chiết khấu đúng cho doanh nghiệp; việc đó nối sang bài 010 và 011.

**Điểm dừng phiên 1:** Viết dòng thời gian 0→1→2→3. Đặt 150 ở mốc 3 và 119,07 ở mốc 0. Giải thích vì sao tiền tương lai chia cho hệ số còn tiền hiện tại nhân hệ số. Nếu chưa giải thích được, đừng chuyển sang công thức nhiều dòng tiền.

## Phiên 2 — Tỷ lệ mỗi kỳ và sức mua

`PHÉP_TÍNH` Không góp/rút: lợi suất một kỳ gồm cổ tức tiền mặt không tái đầu tư là `(giá cuối−giá đầu+cổ tức)/giá đầu`. Tăng từ 100 lên 121 trong hai năm cho lợi suất kép theo năm `(121/100)^(1/2)−1=10%`. Lợi suất thực với tăng danh nghĩa 10% và lạm phát 5% là `1,10/1,05−1≈4,76%`, không đúng chính xác bằng 5%.

Nếu góp thêm 50, tài khoản từ 100 lên 150 chưa chứng minh có lãi 50%. Lợi suất nhiều kỳ có góp/rút cần xử lý thời điểm dòng tiền; xem H4. Điểm dừng: tự tính PV rồi đổi r để xem độ nhạy.

### Tỷ lệ niêm yết và tỷ lệ hiệu dụng

`KỊCH_BẢN` Lãi suất danh nghĩa 12%/năm, ghép hàng tháng, điều khoản giả định lấy 12%/12=1% mỗi tháng. Một đồng sau 12 tháng thành 1,01^12≈1,126825; lợi suất hiệu dụng năm 12,6825%. Đây khác 12% hiệu dụng năm: với loại thứ hai, tỷ lệ tháng tương đương phải là 1,12^(1/12)−1≈0,9489%.

`SỰ_THẬT` [California BOE, bài 9](https://www.boe.ca.gov/info/tvm/lesson9.html) giải thích ảnh hưởng của tần suất ghép lãi. Công thức danh nghĩa năm j, ghép m lần/năm là `(1+j/m)^m−1`. Nếu đầu vào là **hiệu dụng năm** thì dùng căn bậc m để suy tỷ lệ mỗi kỳ; chia thẳng cho m là đổi giả định. Luôn ghi loại tỷ lệ bên cạnh con số, không chỉ viết “12%”.

Cũng cần phân biệt **trả lãi** với **nhập lãi vào vốn**. Tiền lãi trả ra tài khoản khác không tự tiếp tục sinh cùng tỷ lệ trong khoản gửi ban đầu. Nếu hợp đồng trả lãi hàng tháng nhưng người gửi tiêu hết, không được áp công thức ghép tháng cho cả phần lãi đã rút. Công thức đang mô tả chính sách dòng tiền nào phải được viết rõ trước khi tính.

### Lạm phát thuộc rổ nào và thời kỳ nào?

`SỰ_THẬT` [BLS, câu hỏi thường gặp về CPI](https://www.bls.gov/cpi/questions-and-answers.htm) mô tả chỉ số giá tiêu dùng Hoa Kỳ là thay đổi giá của rổ hàng hóa/dịch vụ; nó không phản ánh chính xác chi tiêu của mọi cá nhân. Bài dùng định nghĩa để hiểu phép đo, không lấy CPI Hoa Kỳ thay CPI của một hộ tại Việt Nam.

`KỊCH_BẢN` Tài khoản tăng 8% và rổ phù hợp tăng 4% trong cùng năm. Sức mua tăng 1,08/1,04−1≈3,85%. Nếu rổ tăng 10%, sức mua giảm 1,08/1,10−1≈−1,82% dù số tiền danh nghĩa tăng. Đây là lý do cần hai câu: có thêm bao nhiêu tiền và mua được thêm bao nhiêu hàng. Một mức lạm phát quốc gia không tự mô tả chi phí học, chữa bệnh hay thuê nhà của một gia đình.

**Điểm dừng phiên 2:** Phân loại ba số trước khi tính:12% danh nghĩa ghép tháng,12% hiệu dụng năm,4% lạm phát một năm. Chỉ ra số nào có thể chia 12 theo đúng giả định, số nào phải lấy căn, số nào chỉ dùng sau khi quy về cùng kỳ và đồng tiền.

## Phiên 3 — Lợi suất tổng cộng và thời điểm góp tiền

### Một kỳ, nhiều kỳ và đường đi khác nhau

Công thức cộng cổ tức ở phiên 2 giả định tiền cổ tức giữ riêng, không phát sinh lợi nhuận từ tái đầu tư trong cùng kỳ. Nếu một chuỗi đã tái đầu tư cổ tức, không cộng cổ tức lần nữa. Lợi suất giá, lợi suất tổng cộng và lợi suất tổng cộng có tái đầu tư là các đại lượng cần ghi đúng quy ước, dù tên tài sản giống nhau.

`PHÉP_TÍNH` Từ 100 lên 121 trong 2 năm cho CAGR 10%. Nhưng năm đầu+40%, năm sau 121/140−1≈−13,57% cũng về 121. Cùng CAGR không có nghĩa cùng đường đi hay cùng mức giảm sâu. Nó là tỷ lệ đều tương đương giữa hai đầu, không phải khẳng định mỗi năm đã đạt tỷ lệ đó.

## Ví dụ từ nguồn thật

`SỰ_THẬT` Apple 10-K FY2025, mục Company Stock Performance, giả định 100 USD đầu tư tại đóng cửa 25/09/2020 và **tái đầu tư cổ tức**; bảng tháng 09/2025 ghi 234 USD cho Apple và 217 cho S&P 500. FY kết thúc 27/09/2025, hồ sơ nộp 31/10/2025. [Bảng gốcSEC](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm).

`PHÉP_TÍNH` Dùng cửa sổ 5 năm và các số bảng làm tròn: Apple `(234/100)^(1/5)−1≈18,53%/năm`; S&P 500 `(217/100)^(1/5)−1≈16,76%/năm`. Không lấy 134% chia 5 để ra CAGR. Không cộng thêm cổ tức vào 234 vì chuỗi đã tái đầu tư. Bảng này không phải số tiền sau thuế/phí của mọi nhà đầu tư, không cho biết sức mua tại Việt Nam và không dự báo giai đoạn sau.

### Góp đều khác khoản đầu tư đơn lẻ

`KỊCH_BẢN` Vốn đầu 10 triệu; góp 2 triệu vào **cuối mỗi tháng** trong 36 tháng. Giả định 6% danh nghĩa/năm chia 12, tức 0,5%/tháng; không thuế/phí và tỷ lệ cố định. `PHÉP_TÍNH` Vốn đầu thành 10×1,005^36≈11,97 triệu. Các khoản góp thành `2×(1,005^36−1)/0,005≈78,67 triệu`. Tổng 90,64 triệu, vốn nộp 82 triệu, phần tăng khoảng 8,64 triệu.

Vì sao các khoản góp không cùng sinh lời 36 tháng? Khoản đầu tháng 12 đến hạn còn 24 tháng; khoản cuối tháng 36 vừa vào tài khoản nên chưa có thời gian sinh lời. Công thức tổng cấp số nhân chỉ rút gọn phép cộng những khoản khác tuổi đó. Nếu đổi sang góp đầu tháng, mỗi khoản góp thêm một kỳ sinh lời; số dư tăng thêm khoảng 0,39 triệu. Tổng vốn nộp không đổi, lịch thời gian đổi.

Mô hình tính theo từng tháng giúp tránh học vẹt công thức. Bắt đầu với 10; mỗi tháng nhân 1,005 rồi cộng 2 cho góp cuối kỳ. Với góp đầu kỳ, cộng 2 rồi mới nhân 1,005. Tự làm 2 tháng bằng tay trước khi chạy 36 tháng sẽ cho thấy ngay khác biệt. Không gọi tổng 90,64 trừ 10 là tiền lãi: cách đó tính 72 triệu góp mới thành lợi nhuận.

Khi dòng tiền không đều hoặc cần đo hiệu quả cá nhân, phải ghi ngày từng khoản. Tỷ suất theo thời gian và tỷ suất theo dòng tiền trả lời hai câu hỏi khác nhau; [H4](H4-twr-mwr-benchmark.md) sẽ xử lý sâu. N4 chưa suy lợi suất tài khoản chỉ từ số tiền đầu và cuối nếu có khoản góp/rút chưa rõ ngày.

**Điểm dừng phiên 3:** Xác định ví dụ Apple là chuỗi tái đầu tư, còn ví dụ góp 2 triệu là nhiều khoản nộp. Chỉ ví dụ đầu mới dùng CAGR trực tiếp từ 100 và 234 mà không cần trừ dòng tiền bên ngoài.

## Năm câu hỏi khi đọc

1. Khoản tiền nhận vào ngày nào?
2. r và n có cùng đơn vị thời gian?
3. Dòng tiền và r cùng tiền tệ/danh nghĩa hay thực?
4. Có góp/rút hoặc cổ tức giữa kỳ không?
5. Tỷ lệ đang là giả định hay dữ kiện quan sát?

## Bài tập — làm trước khi mở đáp án

Câu 1–3 kiểm tra nền; câu 4–6 luyện tính và giải thích; câu 7–10 yêu cầu tính nhiều bước, nhận ra dữ liệu thiếu và chuyển sang tình huống mới. Làm trước khi mở đáp án.

1. 100 triệu tăng 10%/năm hai năm thành bao nhiêu?
2. 121 triệu sau hai năm quy về hôm nay ở 10%/năm?
3. Từ 100 lên 121 trong hai năm: lợi suất theo năm là 21% hay 10%?
4. Giá từ 50 lên 52, cổ tức 3 cùng đơn vị: lợi suất kỳ?
5. Danh nghĩa 8%, lạm phát 4%: lợi suất thực?
6. Tài khoản từ 100 lên 160 sau khi góp 50 ngay cuối kỳ: lợi nhuận và lợi suất một kỳ là bao nhiêu?
7. Cần 150 triệu sau 3 năm, dùng 8%/năm. Tính PV rồi kiểm ngược FV; đổi tỷ lệ 10% có làm PV tăng không?
8. Phân biệt 12% danh nghĩa ghép tháng với 12% hiệu dụng năm; tính tỷ lệ tháng của mỗi cách.
9. Dùng 100 USD thành 234 USD sau 5 năm từ bảng Apple. Tính CAGR, nêu hai điều không suy ra; có cộng cổ tức nữa không?
10. Góp 2 triệu cuối mỗi tháng trong 36 tháng với vốn đầu 10 triệu và 0,5%/tháng. Tính tổng vốn nộp, số dư và phần tăng; nếu không biết đầu/cuối tháng thì còn thiếu gì?

## Đáp án và điều cần hiểu

<details>
<summary>Mở sau khi tự làm</summary>

1. `PHÉP_TÍNH` 100×1,1²=121 triệu; kiểm lãi kép.
2. `PHÉP_TÍNH` 121/1,1²=100 triệu; kiểm chiều chiết khấu.
3. 10%/năm theo lãi kép; 21% là toàn kỳ.
4. `PHÉP_TÍNH` (52−50+3)/50=10%; giữ cổ tức không tái đầu tư trong kỳ.
5. `PHÉP_TÍNH` 1,08/1,04−1≈3,85%; không trừ gần đúng nếu cần chính xác.
6. `PHÉP_TÍNH` Lợi nhuận 160−100−50=10; vì góp ngay cuối kỳ nên lợi suất trước góp 10/100=10%. Góp giữa kỳ thì phải biết thời điểm.

7. PV≈119,07 triệu; dùng số chưa làm tròn nhân 1,08³ về 150. Ở 10%, PV 150/1,1³≈112,70 triệu, thấp hơn vì mẫu số lớn hơn.
8. Danh nghĩa:0,12/12=1%/tháng, hiệu dụng năm 12,6825%. Hiệu dụng năm 12%: tỷ lệ tháng 1,12^(1/12)−1≈0,9489%; không chia thẳng 12.
9. CAGR ≈18,53%/năm; không chứng minh mỗi năm tăng đều hay tương lai lặp lại. Không cộng thêm cổ tức, bảng đã tái đầu tư; chưa điều chỉnh sức mua/thuế cá nhân.
10. Vốn 10+36×2=82 triệu; số dư≈90,64, phần tăng≈8,64. Thiếu lịch góp thì chưa khóa được số kỳ sinh lời của mỗi khoản.

</details>

## Bài làm với dữ liệu thiếu hoặc lệch

`KỊCH_BẢN` Bảng ghi đầu năm 100 triệu, “góp 20 triệu trong năm”, cuối năm 132 triệu. Lời giải ghi lợi suất 32%. Có thể xác định chênh số dư 32 triệu nhưng không gọi toàn bộ là lợi nhuận:20 triệu là vốn mới. Nếu không còn khoản khác, phần tăng tiền do đầu tư là 12 triệu; lợi suất theo thời gian hoặc theo tiền vẫn chưa xác định chỉ bằng ba số này.

Hãy yêu cầu ngày góp thực, có rút/phân phối hay không, phí/thuế đã trừ và loại lợi suất cần đo. Góp 20 ngay đầu năm tạo mẫu số 120 cho một kỳ, nên 12/120=10%. Góp 20 ngay cuối năm cho 12/100=12% trước góp. Hai cách đều có cuối 132, vốn đầu 100 và góp 20; đây là phản ví dụ chứng minh thời điểm quan trọng. Với góp giữa năm còn cần cách đo phù hợp, không chọn một trong hai tỷ lệ để “ước cho nhanh”.

## Sai ở đâu

> “100 triệu, 12%/năm trả lãi tháng, sau 2 năm thành 125,44 triệu; góp 20 triệu trong năm thứ hai nên lãi 45,44 triệu. Lạm phát 4% thì lãi thực 8%.”

Có ít nhất bốn lỗi cần sửa. Trả lãi tháng chưa nói nhập gốc; nếu danh nghĩa 12% ghép tháng thì phải dùng 24 kỳ 1%. Tiền góp mới không phải lãi và phải biết ngày góp. Tỷ lệ thực dùng hiệu dụng cùng kỳ, không lấy danh nghĩa trừ lạm phát như đẳng thức chính xác. Cuối cùng phải nêu có thuế/phí hay không. Một công thức rất đẹp không cứu được đầu vào sai loại; cách sửa là viết thời gian và quy ước trước.

## Kiểm tra chuyển bài

1. 25 triệu tăng 6% hiệu dụng năm trong 4 năm: tính FV và PV ngược.
2. Có hai khoản góp giữa kỳ: liệt kê dữ kiện còn thiếu trước khi đo lợi suất tài khoản.
3. Lợi suất bằng USD 9%, USD giảm 5% so VND, lạm phát VND 4%: mô tả thứ tự quy đổi và sức mua.

**Tiêu chí đạt:** FV≈31,56 triệu và tính ngược về 25; câu 2 phải yêu cầu ngày/số tiền; câu 3 đổi sang VND bằng 1,09×0,95−1=3,55% rồi điều chỉnh 1,0355/1,04−1≈−0,43%. Không trừ 9−5−4 như phép chính xác; các tỷ lệ đều là giả định.

## Mô hình thực hành

[market_returns.py](../practice/models/market_returns.py) có hàm FV/PV, CAGR, lợi suất thực, quy đổi kỳ và mô phỏng góp đầu/cuối tháng. Mô hình không tự chọn lãi suất hợp lý; nó đòi các tỷ lệ theo dạng thập phân và thời gian rõ. Chạy bằng tay trường hợp 0% trước, rồi trường hợp dương; PV(FV) phải trở về vốn đầu khi dùng cùng giả định. Thay thời điểm góp là một phép đổi mô hình, không phải sửa số làm tròn.

## Lỗi thường gặp

- Lấy tổng lợi suất chia số năm thay cho tăng trưởng kép.
- Nhập 10 thay cho 0,10 trong công thức.
- Trộn kỳ tháng với lãi năm.
- Coi tiền góp thêm là lợi nhuận.
- Coi lợi suất giả định cố định là cam kết.

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị mua/bán/nắm giữ cá nhân hóa.
- Số hư cấu được gắn `KỊCH_BẢN`; phép tính không dự báo hay cam kết lợi nhuận.
- Trước khi áp dụng cho một thị trường, phải kiểm lại nguồn gốc, quy định và chuẩn kế toán tại đó.

## Điều tôi vẫn chưa hiểu

- Nếu dòng tiền không đều thì phải chia kỳ thế nào?
- Tại sao đổi tiền tệ cũng phải đổi giả định tỷ lệ?
- Khoản tiền tương lai có chắc nhận được không?

## Nguồn Internet đã mở

Nguồn được tìm và mở lại trong lượt nâng cấp ngày 02/11/2026. Ngày truy cập: `2026-11-02`. Không suy ngày thu thập thành ngày xuất bản. Phần công thức/ví dụ hư cấu là thiết kế bài học, không phải số thị trường.

| Nguồn | Kỳ/phiên bản, phạm vi | Dùng cho |
|---|---|---|
| [California BOE — Time Value of Money](https://www.boe.ca.gov/info/tvm/lesson1.html) | Hoa Kỳ; tài liệu giáo dục, ngày xuất bản CHƯA_BIẾT; đơn vị tùy ví dụ | Lãi kép, hiện tại/tương lai |
| [Investor.gov — Compound Interest Calculator](https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator) | Hoa Kỳ; công cụ hiện hành; chưa thấy ngày xuất bản | Đầu vào và giới hạn phép minh họa |
| [California BOE — Lesson 9](https://www.boe.ca.gov/info/tvm/lesson9.html) | Tài liệu giáo dục; ngày xuất bản CHƯA_BIẾT | Tần suất ghép lãi và kỳ |
| [BLS — CPI FAQ](https://www.bls.gov/cpi/questions-and-answers.htm) | Hoa Kỳ; trang hiện hành | Rổ CPI và giới hạn với từng cá nhân |
| [Apple Inc. — Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | FY kết thúc 27/09/2025; nộp 31/10/2025; USD; US GAAP | Chỉ số tổng lợi suất 5 năm, giả định tái đầu tư cổ tức |

Biên bản riêng cho đúng phiên bản: [kiểm nguồn](../reviews/N4-fact-check.md), [phản biện](../reviews/N4-risk-review.md). `CHƯA_BIẾT` hiệu quả học thực tế; không suy từ kiểm nguồn ra đã được người học nghiệm thu.
