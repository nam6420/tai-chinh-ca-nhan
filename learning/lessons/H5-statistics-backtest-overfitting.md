# Bài H5 — Thống kê và kiểm thử quá khứ: kiểm tra bằng chứng trước khi tin

- Ngày: `2026-11-02`
- Chốt dữ liệu lúc: `2026-11-02 15:41 Asia/Ho_Chi_Minh`
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/H5-fact-check.md), [phản biện](../reviews/H5-risk-review.md).
- Mục tiêu: phát hiện dữ liệu tương lai, thiên lệch sống sót, thử nhiều phương án và quá khớp; phân biệt mẫu xây dựng, ngoài mẫu và kiểm tra cuốn chiếu.
- Bài trước: [N7](N7-data-probability-uncertainty.md), [H3](H3-risk-volatility-drawdown-liquidity.md), [H4](H4-twr-mwr-benchmark.md). Mô hình: [evidence_lab.py](../practice/models/evidence_lab.py).

## Hiểu bài trong một phút

Một đường lợi nhuận đẹp có thể xuất hiện vì người làm đã biết trước số liệu, bỏ những doanh nghiệp thất bại hoặc thử nhiều lần rồi giấu các lần thua. Máy tính vẫn tính đúng các phép nhân trên bảng sai ấy. Vì vậy câu hỏi đầu tiên không phải “lãi bao nhiêu?”, mà là “tại mỗi thời điểm, người ra quyết định thật sự biết gì và có những lựa chọn nào?”.

Kiểm thử quá khứ, hay backtest, áp một quy trình xác định lên dữ liệu lịch sử để đánh giá kết quả giả định. Bài này chỉ học đánh giá bằng chứng. Các bảng quy tắc đều hư cấu, không chỉ dẫn giao dịch, không xây hệ thống tự động và không xác nhận phương án nào có lợi nhuận trong tương lai.

Ba phiên lần lượt kiểm ngày biết thông tin và thành viên mẫu, kiểm quá trình chọn kết quả, rồi kiểm chi phí và độ bền của kết luận. Bạn nên che phần đáp án khi làm. Một câu trả lời tốt có thể là “chưa đủ dữ liệu để kết luận”, nhưng phải chỉ rõ thiếu gì và cần nguồn nào để kiểm.

## Phiên 1 — Dữ liệu tồn tại lúc nào và ai bị bỏ khỏi bảng?

### Ngày kết thúc kỳ khác ngày biết thông tin

Thông tin nhìn trước, hay look-ahead bias, xuất hiện khi một quyết định mô phỏng dùng dữ liệu chưa có vào ngày đó. Báo cáo cho năm kết thúc 31/12 không có nghĩa mọi con số đã được công bố ngày 31/12. Bản điều chỉnh công bố nhiều tháng sau cũng không tự thay thế thông tin mà nhà đầu tư từng có trong quá khứ.

`KỊCH_BẢN` Doanh nghiệp Mộc có báo cáo kết thúc 31/12/2021, công bố lần đầu 15/02/2022, EPS ban đầu 4.000 VND/cổ phiếu. Ngày 01/03/2023, doanh nghiệp công bố sửa EPS của kỳ ấy thành 7.000. EPS là lợi nhuận trên mỗi cổ phiếu; bài chỉ dùng số này để kiểm ngày thông tin, không để định giá hay sàng lọc tài sản.

| Ngày quyết định giả định | EPS nào đã biết từ bảng? | Điều phải loại |
|---|---|---|
| 03/01/2022 | Chưa có EPS kỳ này | Cả 4.000 và 7.000 |
| 16/02/2022 | 4.000 | Bản sửa 7.000 |
| 02/03/2023 | Có thể biết bản sửa 7.000 | Không được gán ngược kiến thức này cho 2022 |

Bảng giả định thông tin công khai sau ngày công bố, không xử lý giờ công bố trong ngày. Nếu quyết định ngay ngày 15/02 thì còn cần giờ phát hành, múi giờ và giờ ra quyết định; không nên tự coi có dữ liệu từ đầu ngày. Dữ liệu đúng thời điểm, thường gọi point-in-time, là dữ liệu giữ được bức tranh thông tin tại lúc ra quyết định, gồm cả phiên bản và ngày sẵn có.

`SỰ_THẬT` [CFA Institute, Backtesting & Simulation, chương trình 2026](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/backtesting-and-simulation) nêu thông tin nhìn trước và thiên lệch sống sót là các vấn đề cần kiểm tra. Phần công khai là tóm tắt học liệu, không phải toàn văn chương trình. Nó hỗ trợ quy trình kiểm, không xác nhận bộ số hư cấu của bài.

### Một doanh nghiệp biến mất không phải một ô trống vô hại

Thiên lệch sống sót, hay survivorship bias, là chọn mẫu chỉ gồm đối tượng còn tồn tại rồi suy cho toàn bộ quá khứ. Một danh sách cổ phiếu hiện tại không tự là danh sách đã có thể lựa chọn nhiều năm trước. Mã rời sàn có thể do nhiều nguyên nhân; không tự gán mọi mã hủy niêm yết thành mất trắng, cũng không xóa chúng vì thiếu giá cuối.

`KỊCH_BẢN` Đầu một năm, ba doanh nghiệp hư cấu Mộc, Sen, Đá đều thuộc mẫu. Chia vốn 100 triệu VND bằng nhau ngay đầu năm, không tái cân bằng, không góp/rút, không thuế/phí. Tổng lợi suất cuối năm của Mộc +10%, Sen +5%, Đá −90% đã gồm khoản thu hồi cuối cùng. Đá rời mẫu vào cuối năm; bảng hiện tại chỉ giữ Mộc và Sen.

`PHÉP_TÍNH` Với mẫu ban đầu, tổng lợi suất danh mục bằng `(10% + 5% − 90%)/3 = −25%`, vốn còn 75 triệu. Với cách giữ hai mã sống sót rồi phân đều lại vốn đầu, số được báo thành `(10%+5%)/2 = +7,5%`, vốn giả định 107,5 triệu. Khoảng cách là 32,5 điểm phần trăm. Đây là hai danh mục có mẫu đầu khác nhau; không thể gọi bảng hai mã là lịch sử nguyên vẹn của danh mục ba mã.

Đáp án đúng không phải cứ thêm một mức lỗ tùy ý vào mã thiếu. Phải truy danh sách thành viên theo ngày, sự kiện rời mẫu, cổ tức, thanh lý hoặc quyền được nhận. Nếu không tìm thấy tiền thu hồi thật thì ghi `CHƯA_BIẾT` và chạy các kịch bản được công khai, giữ số gốc riêng. Không thay thiếu dữ liệu bằng lợi suất 0%. Điểm dừng phiên một: nói lại vì sao đúng kỳ báo cáo vẫn có thể sai thời điểm sử dụng.

## Ví dụ từ nguồn thật

`SỰ_THẬT` Sullivan, Timmermann và White, bài nghiên cứu trên Journal of Finance tháng 10/1999, trang 1647–1691, mở rộng tập 26 quy tắc của nghiên cứu Brock, Lakonishok và LeBaron thành 7.846 quy tắc; nghiên cứu sử dụng dữ liệu ngày DJIA tại Hoa Kỳ trong khoảng 1897–1996. Đoạn cuối trang in 1654 và đầu 1655 giải thích phạm vi tập quy tắc và tầm quan trọng của sự phụ thuộc giữa kết quả các quy tắc. [Bản bài báo gốc lưu tại trang giảng dạy](https://www.kevinsheppard.com/files/teaching/mfe/advanced-econometrics/Sullivan_Timmermann_White.pdf).

`PHÉP_TÍNH` Phạm vi tìm kiếm tăng từ 26 lên 7.846, tức thêm 7.820 phương án và lớn gấp `7.846/26 ≈ 301,77` lần. Đây là số lượng phương án, không phải tiền hay tỷ lệ lợi nhuận. Nếu một bản giới thiệu chỉ đưa quy tắc đẹp nhất mà bỏ thông tin đã tìm kiếm trong hàng nghìn phương án, người đọc mất dữ kiện quan trọng để đánh giá bằng chứng. Một quy tắc được đưa vào sách còn có thể đã được cộng đồng chọn lọc từ trước khi người nghiên cứu bắt đầu.

`SỰ_THẬT` Chú thích 14, trang in 1659, định nghĩa lợi suất trung bình năm hóa của nghiên cứu bằng trung bình ngày nhân 252; phần trang in 1676 nêu giới hạn dữ liệu cổ tức DJIA và chi phí lịch sử. Không được đọc một số “annualized return” ở đó như CAGR tái đầu tư sau mọi chi phí. Bản sao này là bài nghiên cứu gốc do tác giả viết nhưng đặt ở máy chủ giảng dạy, không phải trang nhà xuất bản; các số đếm dựa trên một nguồn gốc duy nhất.

`SUY_LUẬN` Đếm 7.846 không cho phép tính xác suất chiến thắng thật bằng mô hình các kiểm định độc lập: chính nguồn nói sự phụ thuộc giữa kết quả có vai trò. Nó cũng không chứng minh mọi quy tắc vô dụng hoặc hiệu quả ở thị trường khác. Ta học cách đọc số lần thử, tiêu chí chọn và phạm vi kết luận, chứ không tái tạo chiến lược của nghiên cứu. Số liệu nghiên cứu lịch sử không là dữ liệu thị trường cập nhật ngày chốt.

## Phiên 2 — Người thắng được chọn trước hay sau khi xem kết quả?

### Một phòng thí nghiệm chỉ có sáu kỳ

`KỊCH_BẢN` Bảng dưới có ba phương án hư cấu A, B, C và sáu kỳ quý bằng nhau. Mỗi ô là tổng lợi suất trước chi phí trên vốn đầu quý của phương án; không có dòng tiền ngoài. Đây là các kết quả đã cho để tập kiểm chứng, không có tín hiệu mua bán hoặc dữ liệu đủ để triển khai giao dịch. Các kỳ 1–4 là mẫu xây dựng; 5–6 được khóa làm ngoài mẫu trước khi chọn.

| Phương án | Quý 1 | Quý 2 | Quý 3 | Quý 4 | Quý 5 | Quý 6 |
|---|---:|---:|---:|---:|---:|---:|
| A | +4% | +4% | +4% | +4% | −3% | −3% |
| B | +2% | +2% | +2% | +2% | +1% | +1% |
| C | −1% | +3% | −1% | +3% | +2% | −2% |

`PHÉP_TÍNH` Mẫu xây dựng: A = 1,04⁴ − 1 = 16,985856%; B = 1,02⁴ − 1 = 8,243216%; C = 0,99 × 1,03 × 0,99 × 1,03 − 1 = 3,978809%. Nếu tiêu chí đăng ký trước là lợi suất ghép cao nhất trong bốn quý đầu, A được chọn. Chỉ sau khi khóa lựa chọn mới mở quý 5–6: A = 0,97² − 1 = −5,91%; B = 1,01² − 1 = 2,01%; C = 1,02 × 0,98 − 1 = −0,04%.

Quá khớp dữ liệu, hay overfitting, là điều chỉnh mô hình hoặc tiêu chí quá sát mẫu đã nhìn đến mức khó giữ kết quả trên dữ liệu khác. Bảng này minh họa người thắng có thể thua ngoài mẫu; sáu quý hư cấu không đủ chứng minh quá khớp bằng kiểm định thống kê. Cũng không được đổi sang B sau khi mở quý 5–6 rồi báo B là lựa chọn đã được xác nhận độc lập bởi chính hai quý ấy.

Mẫu xây dựng dùng để hình thành và điều chỉnh phương án. Mẫu kiểm tra ngoài, hay out-of-sample, được giữ khỏi quá trình đó để đánh giá phiên bản đã khóa. Nếu xem mẫu ngoài rồi sửa ngưỡng, chọn lại kỳ đo hoặc loại dữ liệu xấu, ta đã dùng nó để phát triển. Đổi tên thư mục thành “test” không phục hồi tính độc lập đã mất; cần ghi lịch sử sử dụng và dữ liệu kiểm tra mới.

### Thử nhiều phương án tạo cơ hội gặp may

`KỊCH_BẢN` Giả sử 100 kiểm định độc lập, mọi giả thuyết đều không có hiệu ứng thật, mỗi kiểm định có xác suất báo dương giả 5%. Dương giả nghĩa là báo có bằng chứng trong khi giả thuyết không có hiệu ứng của mô hình này đúng. Đây là giả định toán học để thấy cơ chế, không phải mô tả 100 chiến lược thực.

`PHÉP_TÍNH` Số dương giả kỳ vọng là 100 × 0,05 = 5. Xác suất không có dương giả là 0,95¹⁰⁰; có ít nhất một là 1 − 0,95¹⁰⁰ ≈ 99,4079%. Kỳ vọng năm không có nghĩa mỗi lần làm đúng năm; xác suất có ít nhất một cũng không nói phương án thắng chắc giả. Công thức xác suất trên cần độc lập; các phương án dùng chung dữ liệu thường không thỏa điều kiện ấy. Kỳ vọng tổng vẫn cộng được nếu biết xác suất biên, nhưng không tự biết xác suất biên thực chỉ vì đã thử nhiều cách.

Giá trị p trong một kiểm định không phải xác suất phương án sẽ có lãi hoặc xác suất giả thuyết đúng. Kết luận có ý nghĩa thống kê còn phụ thuộc mô hình, giả định và toàn bộ quá trình chọn. Hãy xin danh sách mọi biến thể, kể cả các thay đổi nhỏ về ngày bắt đầu, ngưỡng, ngành hoặc tiêu chí báo cáo. Chỉ đếm ba tên phương án cuối không đủ nếu trước đó đã thử hàng trăm phiên bản.

### Kiểm tra cuốn chiếu

Kiểm tra cuốn chiếu, hay walk-forward, tiến theo thời gian: dùng một cửa sổ đã qua để chọn/hiệu chỉnh, đánh giá trên đoạn kế tiếp, rồi mới dịch cửa sổ. `Ý_KIẾN` Với phòng thí nghiệm sáu quý, có thể đăng ký trước một quy trình minh họa: dùng quý 1–3 chọn cho quý 4; dùng quý 2–4 chọn cho quý 5; dùng quý 3–5 chọn cho quý 6. Tại mỗi bước chỉ dùng thông tin đã có trước quý đánh giá.

Cách này khác giữ một lần mẫu xây dựng 1–4 rồi khóa ngoài mẫu 5–6. Cả hai đều có thể hợp lý cho câu hỏi khác nhau, nhưng không trộn kết quả hoặc chọn cách chia sau khi thấy cách nào đẹp hơn. Quy trình cập nhật, chi phí và tiêu chí chọn phải được khóa trước. Mẫu càng nhỏ càng dễ bất ổn; walk-forward không tự làm dữ liệu có nhiều thông tin hơn và không chữa được mọi thay đổi chế độ thị trường.

## Phiên 3 — Chi phí và tính khả thi trước đường lợi nhuận

Một phép thử có thể lời trước phí nhưng không còn lời sau khi tính giá trị giao dịch thực. Phí một chiều là tỷ lệ trên từng lượt mua hoặc bán. Phải cộng giá trị mua và giá trị bán; đừng tính một lần cho cả vòng. Chênh lệch mua/bán, trượt giá, tác động giá, thuế và phí khác cần được phân biệt để tránh thiếu hoặc tính trùng.

`KỊCH_BẢN` Có vốn đầu quý 100 triệu VND, lãi trước chi phí 500.000 VND, mua tổng 40 triệu và bán tổng 40 triệu. Chi phí giả định mỗi chiều 0,15% giá trị giao dịch; không phải mức phí thật tại một thị trường. Tổng mua cộng bán = 80 triệu. Chi phí = 80 triệu × 0,0015 = 120.000; lãi ròng = 380.000; lợi suất ròng = 0,38% trên vốn đầu quý.

Để áp vào bảng A/B/C, `KỊCH_BẢN` mỗi quý tổng mua cộng bán bằng đúng hai lần vốn đầu quý và chi phí giả định một chiều 0,5%, ghi nhận cuối quý; không tính ảnh hưởng tái đầu tư của thời điểm trả phí trong quý. Công thức mô hình là `r_ròng = r_gộp − (tổng giá trị mua+bán/vốn đầu kỳ) × c`. Đây là quy ước chi phí đơn giản của bài, không phải dự báo khả năng thực hiện giao dịch.

`PHÉP_TÍNH` Mỗi quý trừ 2 × 0,5% = 1 điểm phần trăm. Hai quý ngoài mẫu của A trở thành −4%, −4%, ghép = −7,84%; B thành 0%, 0%, ghép = 0%; C thành +1%, −3%, ghép = −2,03%. Không chỉ lấy lợi suất ghép hai quý rồi trừ 2 điểm phần trăm: vốn làm mẫu số đã đổi giữa hai quý. Số sau chi phí này vẫn chưa gồm thuế hoặc mọi hạn chế khớp lệnh thực.

`SUY_LUẬN` Nếu thiếu dữ liệu lượng có thể khớp, spread hoặc thời điểm giá sẵn có, kết quả chỉ là bằng chứng có điều kiện. CFA cũng cảnh báo các thay đổi cấu trúc và phân bố đuôi dày có thể làm lịch sử mô tả tương lai kém. Kết quả ngoài mẫu ngắn, dù dương, không biến thành bảo đảm. Điểm dừng phiên ba: viết một câu kết luận có điều kiện và ba điều chưa biết, thay vì chỉ báo con số đẹp nhất.

## Bài tập

1. Ngày 03/01/2022 và 16/02/2022 được dùng EPS nào của Mộc? Vì sao ngày kết thúc năm không đủ?
2. Với ba doanh nghiệp ở phiên một, tính vốn cuối mẫu đầy đủ và mẫu chỉ sống sót; nêu chênh lệch điểm phần trăm.
3. Từ nghiên cứu thật, tính số phương án thêm và tỷ số 7.846/26. Có thể coi chúng là kiểm định độc lập không?
4. Tính lợi suất ghép bốn quý xây dựng của A/B/C rồi khóa người thắng theo tiêu chí đã cho.
5. Mở hai quý ngoài mẫu và tính lại cả ba phương án; có được đổi sang B rồi dùng chính hai quý đó để xác nhận không?
6. Với 100 kiểm định theo giả định độc lập và mọi giả thuyết không có hiệu ứng, tính kỳ vọng dương giả và xác suất có ít nhất một.
7. Vốn 100 triệu, lãi gộp 500.000, mua 40 triệu, bán 40 triệu, chi phí mỗi chiều 0,15%: tính lãi và tỷ lệ ròng.
8. Áp chi phí 0,5% trên tổng mua+bán bằng hai lần vốn mỗi quý: tính kết quả ngoài mẫu sau chi phí A/B/C.
9. Thiết kế ba lượt cuốn chiếu với sáu quý; chỉ rõ dữ liệu dùng để chọn và quý dùng để đánh giá, không dùng tương lai.
10. Một báo cáo thiếu mã rời sàn và danh sách biến thể đã thử nhưng đường lợi nhuận đẹp. Hãy viết yêu cầu dữ liệu và kết luận tạm thời, không đề xuất giao dịch.

## Đáp án

1. Ngày 03/01 chưa biết cả hai EPS; 16/02 biết 4.000 nhưng chưa biết 7.000 của bản sửa 2023. Cần ngày/giờ công bố thực, không chỉ kỳ kế toán.
2. Đầy đủ: lợi suất −25%, vốn 75 triệu. Chỉ hai mã sống: +7,5%, vốn 107,5 triệu giả định; chênh 32,5 điểm phần trăm. Không xóa khoản lỗ của Đá khỏi mẫu cũ.
3. Thêm 7.820 phương án; gấp khoảng 301,77 lần. Không: các quy tắc có thể dùng chung thông tin và kết quả phụ thuộc; chính nguồn nhấn mạnh điểm này.
4. A 16,985856%; B 8,243216%; C 3,978809%. Chọn A theo bốn quý xây dựng. Câu đạt phải dùng nhân hệ số, không cộng tỷ lệ.
5. A −5,91%; B +2,01%; C −0,04%. Có thể học từ kết quả để phát triển phiên bản mới, nhưng không gọi chính dữ liệu đã dùng chọn B là kiểm tra độc lập cho B.
6. Kỳ vọng 5; xác suất 1 − 0,95¹⁰⁰ ≈ 99,4079%. Ghi đầy đủ điều kiện độc lập và không có hiệu ứng; không áp số này cho bảng A/B/C.
7. Tổng giao dịch 80 triệu, phí 120.000, lãi ròng 380.000, chia 100 triệu được 0,38%. Không lấy 0,15% nhân một lượt rồi bỏ lượt còn lại.
8. Mỗi quý giảm 1 điểm phần trăm. A: 0,96² − 1 = −7,84%; B: 1² − 1 = 0%; C: 1,01 × 0,97 − 1 = −2,03%. Không hứa đây là toàn bộ chi phí thật.
9. Chọn từ 1–3 đánh giá 4; chọn từ 2–4 đánh giá 5; chọn từ 3–5 đánh giá 6. Quy trình này phải đăng ký trước khi dùng kết quả tương lai để chọn cách chia.
10. Xin mẫu thành viên theo ngày, hồ sơ rời mẫu và thu hồi, phiên bản/ngày công bố dữ liệu, mọi lần thử và chi phí. Kết luận đạt: chưa đủ bằng chứng tái lập hoặc khả thi; không suy hiệu quả tương lai từ biểu đồ.

## Bài làm với dữ liệu thiếu hoặc lệch

`KỊCH_BẢN` Tệp chỉ có mã đang niêm yết; EPS ghi năm 2021 nhưng không ghi ngày công bố; ô lợi suất quý ghi “2” mà không có đơn vị; phí ghi “0,5” không nói phần trăm hay số thập phân. Người viết chia ngẫu nhiên các dòng rồi gọi 20% số dòng là ngoài mẫu. Hãy lập bảng lỗi trước mọi thống kê.

Cách xử lý: giữ tệp gốc, hỏi nguồn thành viên lịch sử và phiên bản EPS; xác nhận “2” là 2% hay hệ số; xác nhận phí mỗi chiều và mẫu số giá trị giao dịch. Chia dữ liệu theo thứ tự thời gian phù hợp câu hỏi; việc trộn các dòng tương lai vào xây dựng có thể rò rỉ thông tin. Ghi `CHƯA_BIẾT` cho kết quả còn thiếu, không điền số 0 hoặc tự chọn đơn vị thuận lợi. Chỉ tính lại khi có dữ liệu đủ và nhật ký chuyển đổi.

## Sai ở đâu

“Tôi thử 100 cách, chọn cách lời nhất, kiểm lại trên cùng lịch sử, bỏ các mã không có giá cuối rồi kết luận tương quan chứng minh tín hiệu gây ra lợi nhuận.” Sai ở việc giấu quá trình chọn, dùng lại mẫu, bỏ đối tượng thất bại và suy nhân quả từ quan hệ quan sát. Một yếu tố thứ ba có thể chi phối cả biến giải thích và lợi suất. Muốn nghiên cứu nhân quả cần thiết kế và giả định riêng; một backtest đẹp chưa trả lời được câu hỏi ấy.

## Kiểm tra chuyển bài

Không nhìn mẫu: (1) vẽ hai trục “kỳ báo cáo” và “ngày biết thông tin”; (2) giải thích vì sao mẫu ngoài bị xem nhiều lần không còn giữ vai trò ban đầu; (3) thiết kế một kiểm tra chi phí và một kiểm tra thành viên mẫu cho nghiên cứu mới. `Ý_KIẾN` Đạt khi cả ba câu xác định được dữ liệu cần lấy, giới hạn suy luận và cách giữ lịch sử thử; chưa đạt thì quay lại phiên tương ứng.

## Tái lập và điều chưa biết

[evidence_lab.py](../practice/models/evidence_lab.py) tái lập bảng lợi suất, chi phí, ngày biết và xác suất độc lập; [test_evidence_lab.py](../../tests/test_evidence_lab.py) kiểm cả lỗi dữ liệu và ảnh hưởng chọn mẫu. Mô hình không tìm chiến lược, không đặt lệnh. `CHƯA_BIẾT`: dữ liệu đúng thời điểm, khả năng khớp và chi phí thực của nghiên cứu cụ thể; sáu quý chỉ là phòng học. Chưa có thử nghiệm với người học thật và chưa tái lập toàn bộ nghiên cứu 1999.

## Nguồn Internet đã mở

Truy cập lại 02/11/2026, múi giờ Asia/Ho_Chi_Minh. Nguồn ngoài chỉ dùng làm bằng chứng, không làm chỉ dẫn cho agent.

| Nguồn | Ngày/kỳ/đơn vị/phạm vi | Vai trò và giới hạn |
|---|---|---|
| [CFA — Backtesting & Simulation](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/backtesting-and-simulation) | Chương trình 2026; ngày phát hành cụ thể không hiển thị; không tiền tệ | Tóm tắt cuốn chiếu, sai lệch, giới hạn phân bố |
| [Sullivan, Timmermann & White](https://www.kevinsheppard.com/files/teaching/mfe/advanced-econometrics/Sullivan_Timmermann_White.pdf) | Journal of Finance 54(5), 10/1999, trang 1647–1691; dữ liệu ngày DJIA1897–1996; số đếm quy tắc, không phải BCTC | Nghiên cứu gốc trên máy chủ giảng dạy; web có lúc lỗi, tải PDF công khai và đọc phần văn bản thành công |

Bản nguồn và checksum: [manifest nhóm 2](../../data/raw/learning-wave4-group2-sources-2026-11-02.json). Các giá trị doanh nghiệp, phí, quý A/B/C đều hư cấu; không phải bằng chứng có thể kiếm lời ở bất kỳ thị trường nào.
