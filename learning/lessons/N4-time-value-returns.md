# Bài N4 — Giá trị thời gian của tiền và lợi suất

- Ngày: `2026-10-26`
- Chốt dữ liệu lúc: `2026-10-26 16:54 UTC+7 (Asia/Ho_Chi_Minh)`
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

## 1. Tiền sinh thêm trên cả phần lãi cũ

`SỰ_THẬT` Tài liệu giáo dục của California BOE trình bày giá trị thời gian bằng toán lãi kép. [BOE](https://www.boe.ca.gov/info/tvm/lesson1.html). Với một khoản đầu, lãi nhập gốc mỗi kỳ, không góp/rút và tỷ lệ cố định: `FV = PV × (1+r)^n`, trong đó PV là giá trị hôm nay, FV tương lai, r tỷ lệ mỗi kỳ, n số kỳ.

`KỊCH_BẢN` 100 triệu đồng, 10%/năm trong hai năm, bỏ thuế/phí. `PHÉP_TÍNH` Năm một 110; năm hai `110×1,10=121`. Tổng tăng 21%, không phải 20%. Nếu tỷ lệ thay đổi, nhân các `(1+r_t)`, không lấy một tỷ lệ tùy ý.

## 2. Đi ngược thời gian: chiết khấu

`PHÉP_TÍNH` Muốn nhận 121 triệu sau hai năm, dùng tỷ lệ giả định 10%/năm: `PV = 121/(1,10)^2 = 100 triệu`. Nếu r tăng 12%, PV = `121/1,12² ≈ 96,46 triệu`. Tỷ lệ cao hơn làm giá trị hiện tại thấp hơn khi giữ nguyên khoản nhận dương.

`SUY_LUẬN` Đây là phép quy đổi theo giả định, không chứng minh khoản tiền tương lai chắc chắn thu được. Rủi ro và thời điểm phải nhất quán với r; Bài 010 sẽ dạy cách đặt giả định r.

## 3. Đừng nhầm lợi suất, tăng tài khoản và sức mua

`PHÉP_TÍNH` Không góp/rút: lợi suất một kỳ gồm cổ tức tiền mặt không tái đầu tư là `(giá cuối−giá đầu+cổ tức)/giá đầu`. Tăng từ 100 lên 121 trong hai năm cho lợi suất kép theo năm `(121/100)^(1/2)−1=10%`. Lợi suất thực với tăng danh nghĩa 10% và lạm phát 5% là `1,10/1,05−1≈4,76%`, không đúng chính xác bằng 5%.

Nếu góp thêm 50, tài khoản từ 100 lên 150 chưa chứng minh có lãi 50%. Lợi suất nhiều kỳ có góp/rút cần xử lý thời điểm dòng tiền; xem N5B. Điểm dừng: tự tính PV rồi đổi r để xem độ nhạy.

## Ví dụ từ nguồn thật

`SỰ_THẬT` Công cụ của Investor.gov cho nhập khoản đầu, khoản góp, thời gian và lãi suất ước tính. Nó minh họa phép tính lãi kép, không dự báo thị trường. [Máy tính chính thức](https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator). Trong bài chỉ đọc cơ chế; không nhập dữ liệu tài chính cá nhân.

## Năm câu hỏi khi đọc

1. Khoản tiền nhận vào ngày nào?
2. r và n có cùng đơn vị thời gian?
3. Dòng tiền và r cùng tiền tệ/danh nghĩa hay thực?
4. Có góp/rút hoặc cổ tức giữa kỳ không?
5. Tỷ lệ đang là giả định hay dữ kiện quan sát?

## Bài tập — làm trước khi mở đáp án

Câu 1–3 là phần cốt lõi; câu 4–6 là luyện thêm và chuyển sang tình huống mới. Nếu chưa tự giải được phần cốt lõi, quay lại ví dụ rồi thử với đầu vào khác.

1. 100 triệu tăng 10%/năm hai năm thành bao nhiêu?
2. 121 triệu sau hai năm quy về hôm nay ở 10%/năm?
3. Từ 100 lên 121 trong hai năm: lợi suất theo năm là 21% hay 10%?
4. Giá từ 50 lên 52, cổ tức 3 cùng đơn vị: lợi suất kỳ?
5. Danh nghĩa 8%, lạm phát 4%: lợi suất thực?
6. Tài khoản từ 100 lên 160 sau khi góp 50 ngay cuối kỳ: lợi nhuận và lợi suất một kỳ là bao nhiêu?

## Đáp án và điều cần hiểu

<details>
<summary>Mở sau khi tự làm</summary>

1. `PHÉP_TÍNH` 100×1,1²=121 triệu; kiểm lãi kép.
2. `PHÉP_TÍNH` 121/1,1²=100 triệu; kiểm chiều chiết khấu.
3. 10%/năm theo lãi kép; 21% là toàn kỳ.
4. `PHÉP_TÍNH` (52−50+3)/50=10%; giữ cổ tức không tái đầu tư trong kỳ.
5. `PHÉP_TÍNH` 1,08/1,04−1≈3,85%; không trừ gần đúng nếu cần chính xác.
6. `PHÉP_TÍNH` Lợi nhuận160−100−50=10; vì góp ngay cuối kỳ nên lợi suất trước góp10/100=10%. Góp giữa kỳ thì phải biết thời điểm.

</details>

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

Các nguồn được nhánh chuyên môn hoặc điều phối viên tìm kiếm và mở trong lượt triển khai ngày 26/10/2026. Ngày truy cập: `2026-10-26`. Không suy ngày thu thập thành ngày xuất bản. Phần công thức/ví dụ hư cấu là thiết kế bài học, không phải số thị trường.

| Nguồn | Kỳ/phiên bản, phạm vi | Dùng cho |
|---|---|---|
| [California BOE — Time Value of Money](https://www.boe.ca.gov/info/tvm/lesson1.html) | Hoa Kỳ; tài liệu giáo dục, ngày xuất bản CHƯA_BIẾT; đơn vị tùy ví dụ | Lãi kép, hiện tại/tương lai |
| [Investor.gov — Compound Interest Calculator](https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator) | Hoa Kỳ; công cụ hiện hành; chưa thấy ngày xuất bản | Đầu vào và giới hạn phép minh họa |

Biên bản riêng cho đúng phiên bản: [kiểm nguồn](../reviews/N4-fact-check.md), [phản biện](../reviews/N4-risk-review.md). `CHƯA_BIẾT` hiệu quả học thực tế; không suy từ kiểm nguồn ra đã được người học nghiệm thu.

