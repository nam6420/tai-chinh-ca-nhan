# Bài H4 — Đo kết quả có góp/rút: TWR, MWR và mốc so sánh

- Ngày: `2026-11-02`
- Chốt dữ liệu lúc: `2026-11-02 15:41 Asia/Ho_Chi_Minh`
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/H4-fact-check.md), [phản biện](../reviews/H4-risk-review.md).
- Mục tiêu: lập sổ nhiều kỳ có góp/rút, tính và giải thích TWR, IRR, XIRR; so kết quả trên cùng cơ sở.
- Bài trước: [N4](N4-time-value-returns.md), [H3](H3-risk-volatility-drawdown-liquidity.md). Mô hình: [risk_performance.py](../practice/models/risk_performance.py).

## Hiểu bài trong một phút

Tài khoản tăng tiền không nhất thiết đầu tư có lãi: có thể chủ tài khoản vừa góp thêm. Hai người cùng đi qua một chuỗi thị trường nhưng góp vào thời điểm khác nhau cũng có thể có trải nghiệm tiền bạc khác nhau. Đo hiệu quả cần trả lời rõ câu hỏi: ta muốn biết đường tăng giảm của danh mục, hay kết quả gắn với số tiền thực bỏ vào và thời điểm bỏ vào?

Lợi suất theo thời gian, gọi tắt TWR từ time-weighted return, ghép các đoạn đầu tư sau khi tách góp/rút. Lợi suất theo dòng tiền, gọi tắt MWR từ money-weighted return, tính đến quy mô và thời điểm tiền ra/vào của người đầu tư. IRR, tỷ suất hoàn vốn nội bộ, là một cách tính MWR. XIRR là dạng tính dùng ngày thực tế không cách đều. Không chọn chỉ số chỉ vì con số ấy đẹp hơn.

Bài có ba phiên: dựng sổ dòng tiền; giải hai cách đo; kiểm mốc so sánh và dữ liệu thiếu. Đọc xong mỗi phiên hãy tự viết một câu giải thích trước khi nhìn đáp án. Đây là bài học phương pháp, không phải báo cáo hiệu quả một tài khoản thật và không xác nhận tuân thủ tiêu chuẩn GIPS.

## Ôn bài cũ

- Trong [Bài H3 — Rủi ro, biến động, sụt giảm và thanh khoản](H3-risk-volatility-drawdown-liquidity.md) và [Bài N4 — Giá trị thời gian của tiền](N4-time-value-returns.md), ta đã biết đo rủi ro và lợi suất. Bài H4 phân biệt lợi suất theo thời gian (`TWR`), lợi suất theo dòng tiền (`MWR`) và cách chọn chỉ số chuẩn (`Benchmark`).

---

## Phiên 1 — Lập sổ trước khi tính tỷ lệ

### Phân biệt dòng tiền ngoài và chuyển động bên trong

Tiền chủ tài khoản góp thêm là dòng tiền ngoài; tiền rút ra cũng vậy. Bán cổ phiếu A rồi mua B trong cùng tài khoản là thay đổi tài sản bên trong, không phải chủ tài khoản góp thêm vốn. Cổ tức nhận vào tiền mặt của tài khoản vẫn thuộc tài khoản, nên không tự là dòng tiền ngoài. Nếu cổ tức được trả thẳng ra ngoài phạm vi đang đo thì phải ghi nhận khoản phân phối. Trước tiên vẽ ranh giới danh mục, rồi mới phân loại giao dịch.

`SỰ_THẬT` [CFA Institute, Rates and Returns, chương trình 2026](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/rates-and-returns) đặt việc so sánh TWR và MWR trong nội dung đo lợi suất. [GIPS Handbook, phần 2.A.24](https://www.gipsstandards.org/standards/gips-standards-for-firms/gips-standards-handbook-for-firms/) giải thích ghép các lợi suất phân kỳ và tác động của định giá tại dòng tiền. Các nguồn giúp kiểm phương pháp; chúng không xác nhận dữ liệu tài khoản hư cấu dưới đây.

`KỊCH_BẢN` Đơn vị mọi giá trị là triệu VND. Ba kỳ đầu tiên đều dài đúng một năm theo mô hình thời gian t=0,1,2,3; đây là trục thời gian quy ước, chưa phải lịch ngày thực. Không vay, không thuế, không phí; thu nhập đầu tư nếu có đã nằm trong giá trị tài khoản. Mỗi lần góp/rút diễn ra ngay sau định giá cuối kỳ và không phát sinh biến động giá trong lúc chuyển tiền.

| Thời điểm | Giá trị trước dòng tiền | Dòng tiền vào danh mục | Giá trị sau dòng tiền |
|---|---:|---:|---:|
| t=0 | 0 | +100 | 100 |
| t=1 | 110 | +100 | 210 |
| t=2 | 189 | −39 | 150 |
| t=3 | 180 | Không có | 180 |

Dấu trong bảng là theo phía tài khoản: góp vào dương, rút ra âm. Ngay sau đây khi dùng IRR ta đổi góc nhìn sang người bỏ tiền: góp là âm, nhận về là dương. Không trộn dấu của hai phía trong cùng phương trình. Tại t=3 ta giả định tính giá trị tài khoản còn lại như một khoản thu hồi cho mục đích đo, không yêu cầu bán tài sản thật.

`PHÉP_TÍNH` Kiểm sổ tiền: tổng tiền góp 200; rút thực 39; còn tài sản 180. Lãi tiền danh nghĩa là 39 + 180 − 200 = 19 triệu. Kiểm thêm từng kỳ: kỳ một lãi 10; kỳ hai lỗ 21; kỳ ba lãi 30; cộng 10 − 21 + 30 = 19. Hai đường kiểm khớp nhau. Tuy nhiên 19/200 = 9,5% chưa xét mỗi đồng tiền nằm trong tài khoản bao lâu, nên không tự là lợi suất năm.

Một bảng chỉ ghi đầu 100, cuối 180 và “góp thêm 100, đã rút 39” đủ kiểm lãi tiền tổng nếu không còn dòng tiền khác, nhưng thiếu định giá tại mốc để tính TWR chính xác. Tổng tiền và tỷ lệ sinh lời là hai lớp thông tin. Điểm dừng phiên một: tự lập lại bảng theo góc nhìn nhà đầu tư với bốn dòng tiền −100; −100; +39; +180.

## Phiên 2 — Hai câu hỏi, hai cách đo

### TWR: một đơn vị vốn đi qua các đoạn thế nào?

Tách mỗi đoạn ngay tại góp/rút. Vốn bắt đầu kỳ hai là 210, không phải 110; vốn bắt đầu kỳ ba là 150, không phải 189. Lấy giá trị cuối trước dòng tiền chia vốn đầu sau dòng tiền gần nhất. Nhờ vậy khoản góp không bị nhầm thành lãi và khoản rút không bị nhầm thành lỗ.

`PHÉP_TÍNH` Kỳ một: 110/100 − 1 = 10%. Kỳ hai: 189/210 − 1 = −10%. Kỳ ba: 180/150 − 1 = 20%. TWR toàn kỳ là `(1+0,10) × (1−0,10) × (1+0,20) − 1 = 18,8%`. Công thức tổng quát là `TWR = tích(1+r_i) − 1`. Đừng cộng 10 − 10 + 20 thành 20%.

Với ba năm bằng nhau của mô hình này, năm hóa thành `1,188^(1/3) − 1 ≈ 5,91%/năm`. Đây là tỷ lệ kép tương đương, không khẳng định năm nào cũng lời 5,91%. Nếu không có dòng tiền ngoài và đầu tư 100 qua đúng các lợi suất ấy, tài khoản sẽ kết thúc ở 118,8. Ta có thể tính TWR mà không biết người đầu tư muốn rút tiền lúc nào, nhưng phải có đủ định giá để tách các đoạn.

`SUY_LUẬN` TWR hữu ích khi muốn mô tả kết quả của đường đầu tư tách khỏi thời điểm khách hàng góp/rút. Nó không loại bỏ mọi ảnh hưởng kinh tế của dòng tiền: danh mục thật có thể chịu chi phí, tiền chờ hoặc khó khớp lệnh do góp/rút. Nó cũng không tự là thước đo kỹ năng đã điều chỉnh rủi ro. TWR chính xác về số học vẫn có thể dựa trên định giá thiếu tin cậy.

### MWR: tiền thực bỏ vào nhận tỷ lệ nào?

Theo góc nhìn nhà đầu tư, dãy dòng tiền là `C = [−100, −100, +39, +180]`. Giá trị hiện tại ròng, gọi NPV, là tổng các khoản tiền quy về thời điểm đầu. Tìm một lãi suất r làm tổng đó bằng không: tiền đã bỏ ra được cân bằng bởi tiền nhận và giá trị còn lại sau khi chiết khấu theo thời gian.

`PHÉP_TÍNH` Phương trình là `−100 − 100/(1+r) + 39/(1+r)^2 + 180/(1+r)^3 = 0`. Mô hình tìm nghiệm bằng chia đôi một khoảng có hai đầu trái dấu, ở đây từ −90% tới +100%. Nghiệm khoảng 0,0398248913, tức 3,98249%/năm. Thay lại phương trình cho tổng gần không theo độ chính xác số máy. Đổi triệu thành nghìn VND bằng cách nhân mọi dòng tiền cùng một hệ số không làm đổi nghiệm.

TWR năm hóa 5,91% và MWR 3,98% khác nhau vì khoản góp 100 đi vào ngay trước kỳ giảm 10%. Có nhiều tiền chịu kỳ xấu hơn so với ca giữ cố định một đơn vị vốn. Điều này không chứng minh người góp hành động sai: thời điểm có tiền có thể do thu nhập hoặc nghĩa vụ ngoài đầu tư. Hai tỷ lệ trả lời hai câu hỏi khác nhau, không thể kết luận một cách đo luôn trung thực hơn cách kia.

`SỰ_THẬT` GIPS Handbook cũng lưu ý IRR có thể có nhiều đáp án khi dòng tiền đổi dấu nhiều lần. `PHÉP_TÍNH` Ví dụ toán học `[-100, +230, −132]` tại t=0,1,2 có cả r=10% và r=20% làm NPV bằng không. Một bộ giải tìm thấy một nghiệm không chứng minh đó là nghiệm duy nhất. Bộ giải có kẹp của bài chỉ trả một nghiệm trong khoảng người dùng chọn; nếu không thấy đổi dấu hai đầu cũng không được kết luận tuyệt đối rằng không tồn tại nghiệm.

### XIRR: cùng khoản tiền nhưng ngày không đều

`KỊCH_BẢN` Bây giờ đổi lịch của chính ca tài khoản, giữ các giá trị trước/sau dòng tiền nhưng không còn giả định mỗi kỳ dài một năm. Đây là ca thời gian khác, không phải cách nhập ngày thay thế cho ba năm ở trên.

| Ngày | Dòng tiền nhà đầu tư | Số ngày từ đầu |
|---|---:|---:|
| 01/01/2023 | −100 | 0 |
| 01/07/2023 | −100 | 181 |
| 01/07/2024 | +39 | 547 |
| 01/01/2025 | +180 | 731 |

`PHÉP_TÍNH` Quy ước ngày thực/365 cố định: `Σ C_i/(1+r)^((d_i−d_0)/365) = 0`. Số mũ lần lượt là 0; 181/365; 547/365; 731/365. Kết quả XIRR ≈ 5,59966%/năm. Có ngày nhuận trong khoảng đo nhưng mẫu số vẫn 365 theo quy ước đã nêu. Không dùng IRR với các khoảng bằng nhau để xử lý lịch này.

TWR toàn khoảng vẫn là 18,8% vì các tỷ lệ giữa mốc định giá không đổi. Nếu năm hóa cho đúng 731 ngày của ca này thì là `1,188^(365/731) − 1 ≈ 8,98%/năm`, khác 5,91% của ca ba năm. Cả thời gian lẫn trọng số tiền đều có thể đổi cách diễn giải. Điểm dừng phiên hai: chỉ vào từng kết quả và nói đó là toàn kỳ hay mỗi năm, dùng lịch nào, theo phía tài khoản hay nhà đầu tư.

## Ví dụ từ nguồn thật

`SỰ_THẬT` Thư cổ đông Berkshire năm 2024, ngày 22/02/2025, PDF trang 15, ghi S&P 500 có tính cổ tức năm 2022 −18,1% và năm 2023 +26,3%. Dùng chuỗi chỉ số cơ sở USD tại Hoa Kỳ, không phải lợi suất tiền VND hoặc lợi suất sau phí của một quỹ. [Nguồn Berkshire](https://www.berkshirehathaway.com/letters/2024ltr.pdf). Các số gốc đã làm tròn một chữ số thập phân.

`PHÉP_TÍNH` Lấy 100 điểm ở đầu 2022: cuối 2022 còn 81,9; cuối 2023 thành 81,9 × 1,263 = 103,4397. Lợi suất ghép hai năm ≈ 3,4397%, không phải tổng −18,1 + 26,3 = 8,2%. Năm hóa từ số làm tròn: `căn(1,034397) − 1 ≈ 1,7053%/năm`. Bài tái dựng một chỉ số, không có dòng tiền nhà đầu tư thực nên không tự có MWR thực.

`KỊCH_BẢN` Để thấy trọng số tiền trên đường chỉ số lịch sử ấy, giả sử tài khoản lý thuyết có 100 USD đầu 2022, góp thêm 100 USD đúng cuối 2022 sau định giá. Cuối 2023 tài khoản bằng `(81,9+100) × 1,263 = 229,7397 USD`, không thuế/phí/sai lệch bám chỉ số. Đây là sự kết hợp số thị trường thật với dòng tiền hư cấu, không phải sản phẩm đã đạt kết quả này.

`PHÉP_TÍNH` TWR vẫn ≈ 3,4397% toàn hai năm. IRR theo hai khoảng năm bằng nhau giải `−100 − 100/(1+r) + 229,7397/(1+r)^2 = 0`, cho khoảng 9,61%/năm. Nó cao hơn TWR năm hóa vì tiền góp thêm đi vào trước kỳ tăng. Chỉ từ ví dụ không suy được khả năng chọn thời điểm. Nguồn số là duy nhất một bảng Berkshire; công thức từ CFA/GIPS không phải nguồn độc lập xác nhận các tỷ lệ lịch sử.

## Phiên 3 — So với cái gì và trên cơ sở nào?

Mốc so sánh, hay benchmark, cần đại diện câu hỏi đang hỏi. Cùng thời gian và loại tài sản là điểm bắt đầu; đồng tiền, cổ tức, phí và thuế phải được mô tả. Một chỉ số giá không tính cổ tức không tự là đối chứng công bằng cho tài khoản đã nhận cổ tức. Chỉ số tổng lợi suất thường là mô hình tái đầu tư; chưa chắc người đầu tư mua được đúng kết quả đó sau mọi chi phí.

`KỊCH_BẢN` Danh mục báo +8% sau phí quản lý và đã nhận cổ tức; mốc so sánh báo +6% chỉ theo giá. Phép trừ ra 2 điểm phần trăm đúng về số học nhưng chưa phải so sánh cùng định nghĩa. Cần lấy tổng lợi suất của mốc cùng kỳ, hoặc trình bày hai cơ sở riêng. Nếu danh mục VND còn mốc USD, cần tỷ giá tại hai đầu và quy tắc chuyển đổi nhất quán; không lấy hai số phần trăm sẵn có rồi trừ.

Đối với MWR, có thể dựng tài khoản đối chứng giả định đầu tư vào mốc so sánh với cùng ngày và lượng góp/rút, rồi giải MWR của đối chứng. Cần kiểm đối chứng luôn đủ tài sản để rút và có dữ liệu định giá tại ngày cần thiết. So MWR thực với TWR chỉ số mà không nói rõ câu hỏi sẽ trộn hiệu quả đường đầu tư với trải nghiệm dòng tiền. Dù chuẩn hóa tốt, chênh lệch vẫn chưa tự là alpha, tức phần lợi suất vượt mức kỳ vọng theo một mô hình điều chỉnh rủi ro đã xác định.

Phí phải được xử lý một lần và đúng góc nhìn. Nếu phí đã bị trừ khỏi giá trị cuối tài khoản, lợi suất tính trên giá trị ấy đã phản ánh phí tương ứng; đừng trừ lần hai. Nếu nhà đầu tư trả phí từ tài khoản bên ngoài, cần ghi riêng để tính trải nghiệm tiền sau phí. Thuế phụ thuộc đối tượng và thị trường; thiếu dữ liệu thì ghi `CHƯA_BIẾT`, không tự nhận kết quả “sau mọi chi phí”.

`SỰ_THẬT` GIPS là bộ chuẩn trình bày hiệu suất đầu tư với nhiều yêu cầu tổ chức. [Handbook, phần 1.A.8–1.A.9](https://www.gipsstandards.org/standards/gips-standards-for-firms/gips-standards-handbook-for-firms/) không cho suy tuân thủ chỉ từ một phương pháp tính. Bài này học TWR/MWR, không tuyên bố giáo trình, phần mềm hay tài khoản cá nhân tuân thủ GIPS. Không biến việc dẫn chuẩn thành chứng nhận chất lượng dữ liệu.

## Bài tập

1. Phân loại góp tiền, rút tiền, bán A mua B trong cùng tài khoản và cổ tức giữ trong tài khoản; xác định ranh giới đang đo.
2. Từ bảng ba năm, tính lãi tiền từng năm và lãi toàn kỳ, kiểm bằng tổng tiền góp/rút và giá trị cuối.
3. Tính ba lợi suất phân kỳ, TWR toàn kỳ và TWR năm hóa của ca ba năm.
4. Viết dòng tiền theo nhà đầu tư và phương trình IRR; tìm nghiệm bằng mô hình rồi kiểm NPV tại nghiệm.
5. Giữ ba lợi suất nhưng không góp/rút, bắt đầu 100. Cuối cùng bao nhiêu? Vì sao TWR không đổi nhưng lãi tiền khác?
6. Với lịch ngày không đều, đếm số ngày, viết phương trình XIRR và giải; TWR năm hóa theo đúng thời gian là bao nhiêu?
7. Từ S&P năm 2022–2023, tính chuỗi điểm và TWR; thêm khoản góp hư cấu 100 cuối 2022 thì giá trị cuối và IRR thế nào?
8. Đầu tài khoản 100, cuối 180, góp 100, rút 39 nhưng thiếu ngày và định giá. Những gì tính được, những gì chưa tính chính xác được?
9. Danh mục +8% sau phí và có cổ tức, chỉ số +6% chỉ giá, tiền tệ khác. Hãy lập yêu cầu sửa bảng trước khi kết luận vượt mốc.
10. Với dòng tiền −100, +230, −132 tại ba mốc năm bằng nhau, kiểm cả nghiệm 10% và 20%; giải thích giới hạn của kết quả máy tính.

## Đáp án

1. Góp/rút là ngoài; bán mua bên trong và cổ tức giữ lại là nội bộ khi phạm vi là toàn tài khoản. Nếu cổ tức chuyển ra ngoài phạm vi, ghi phân phối; cần nêu phạm vi trước khi phân loại.
2. Lãi 10, −21, +30 triệu; tổng 19. Kiểm 180 + 39 − 100 − 100 = 19. Tỷ lệ 9,5% trên tổng góp chưa xét thời gian nên không tự là số năm hóa.
3. 10%, −10%, 20%; 1,1 × 0,9 × 1,2 − 1 = 18,8%; căn bậc ba của 1,188 trừ một ≈ 5,91%/năm cho ba năm bằng nhau.
4. −100, −100, +39, +180. Nghiệm ≈ 3,98249%/năm; thay vào tổng chiết khấu cho gần không. Không đổi dấu riêng một dòng; giá trị cuối là thu hồi giả định để đo.
5. 100 × 1,1 × 0,9 × 1,2 = 118,8; lãi 18,8 triệu. TWR vẫn 18,8% vì đường tỷ lệ từng đoạn giống nhau; số vốn chịu từng kỳ đã khác.
6. Các ngày cách đầu 0, 181, 547, 731 ngày. Dùng mũ chia 365; XIRR ≈ 5,59966%/năm; TWR năm hóa ≈ 8,98%/năm. Không gọi lịch này ba năm.
7. 100 → 81,9 → 103,4397; TWR ≈ 3,4397%. Có góp, cuối là 229,7397 USD; IRR khoảng 9,61%/năm theo hai kỳ năm bằng nhau. Phần dòng tiền là hư cấu.
8. Nếu chắc không còn khoản khác, lãi tiền tổng 19; chưa có thời gian để tính MWR có ý nghĩa theo năm, cũng thiếu phân đoạn cho TWR chính xác. Cần sổ giao dịch và định giá.
9. Lấy cùng kỳ, đồng tiền, tổng lợi suất/cổ tức và trạng thái phí/thuế; kiểm phạm vi tài sản và cách tái đầu tư. Chấp nhận câu trả lời chỉ rõ dữ liệu thiếu, không chấp nhận chỉ trừ ra 2 rồi gọi alpha.
10. Cả −100 + 230/1,1 − 132/1,1² và −100 + 230/1,2 − 132/1,2² đều bằng không trong sai số làm tròn. Hai nghiệm chứng minh bộ giải một nghiệm không đủ xác nhận duy nhất.

## Bài làm với dữ liệu thiếu hoặc lệch

`KỊCH_BẢN` Bảng xuất ghi “góp 100.000”, cột tiêu đề nói nghìn VND nhưng số dư nói triệu VND; khoản rút ngày 01/07 thiếu năm; cổ tức có cả dòng nhận tiền và số dư cuối đã tái đầu tư. Người viết đã đưa mọi dòng vào XIRR. Hãy dừng xuất tỷ lệ và lập bảng lỗi.

Đáp án đạt: giữ bản gốc, xác nhận đơn vị từng cột, ngày đầy đủ, ranh giới tài khoản và cổ tức có ra ngoài hay không. Không đoán khoản góp là 100 triệu; không cộng cổ tức hai lần. Kiểm tổng chuyển tiền với sao kê, lấy giá trị trước/sau mỗi dòng tiền. Đánh dấu từng mục `CHƯA_BIẾT`, ghi nguồn cần xin để đóng lỗi. XIRR chạy thành công không chứng minh ngày và tiền đã đúng.

## Sai ở đâu

“180 cuối kỳ trừ 100 đầu kỳ là lời 80%; TWR 18,8% nghĩa là năm nào cũng lời 18,8%; MWR thấp hơn chứng minh quản lý kém; dùng công thức GIPS nên kết quả đạt GIPS.” Sai ở việc bỏ dòng tiền, nhầm toàn kỳ/năm, gán nguyên nhân từ một chênh lệch và suy chứng nhận từ công thức. Sửa thành báo cả lãi tiền, phương pháp, kỳ đo, góc nhìn và giới hạn; không suy kỹ năng nếu chưa có bằng chứng khác.

## Kiểm tra chuyển bài

Không nhìn mẫu: (1) dựng dòng tiền cho người góp hai lần và rút một lần theo hai góc nhìn; (2) giải thích TWR và MWR có thể khác dù cùng tài khoản; (3) lập danh sách dữ liệu để so với chỉ số nước ngoài. `Ý_KIẾN` Đạt khi cả ba câu nêu đúng dấu, thời gian, tiền tệ/cổ tức/phí và không gọi chênh lệch tự là kỹ năng. Chưa đạt thì quay lại phiên tương ứng.

## Tái lập và điều chưa biết

Chạy [risk_performance.py](../practice/models/risk_performance.py). Hàm `twr`, `npv`, `bracketed_irr`, `xirr` có kiểm dữ liệu thiếu; [test_risk_performance.py](../../tests/test_risk_performance.py) kiểm dòng tiền, NPV và nhiều nghiệm. `CHƯA_BIẾT`: định giá, phí, thuế và mốc phù hợp của tài khoản thật; chưa kiểm khả năng hiểu bài với người học thực tế. Không dùng mô hình này để ra lệnh hoặc cam kết hiệu quả tương lai.

## Nguồn Internet đã mở

Truy cập lại 02/11/2026, múi giờ Asia/Ho_Chi_Minh.

| Nguồn | Ngày/kỳ/phạm vi/đơn vị | Vai trò |
|---|---|---|
| [CFA — Rates and Returns](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/rates-and-returns) | Chương trình 2026; không ghi ngày phát hành; không tiền tệ | Khung đo lợi suất |
| [GIPS Handbook for Firms](https://www.gipsstandards.org/standards/gips-standards-for-firms/gips-standards-handbook-for-firms/) | Chuẩn 2020, sổ tay trực tuyến; không dùng như chứng nhận | Phân kỳ, ghép lợi suất, IRR và phạm vi tuyên bố |
| [Berkshire thư 2024](https://www.berkshirehathaway.com/letters/2024ltr.pdf) | 22/02/2025; PDF trang 15; S&P năm 2022–2023, % có cổ tức, USD | Dữ liệu thật đã làm tròn |

Bản nguồn và checksum: [manifest nhóm 2](../../data/raw/learning-wave4-group2-sources-2026-11-02.json). Chỉ số không có phí/thuế tài khoản cá nhân; chuẩn kế toán không áp dụng cho phép ghép lợi suất này.
