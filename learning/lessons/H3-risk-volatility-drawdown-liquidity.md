# Bài H3 — Đo rủi ro: biến động, sụt giảm và thanh khoản

- Ngày: `2026-11-02`
- Chốt dữ liệu lúc: `2026-11-02 15:41 Asia/Ho_Chi_Minh`
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/H3-fact-check.md), [phản biện](../reviews/H3-risk-review.md).
- Mục tiêu: tự tính đường đi vốn, độ lệch chuẩn mẫu, mức giảm từ đỉnh và mức tăng hồi phục; phân biệt chúng với thiếu tiền và bán không được.
- Bài trước: [N7](N7-data-probability-uncertainty.md), [H2](H2-decisions-stress-position-size.md). Mô hình: [risk_performance.py](../practice/models/risk_performance.py).

## Hiểu bài trong một phút

Một tài sản có thể ít đổi giá vì lâu không có giao dịch, nhưng khi cần tiền lại không có người mua. Một tài sản khác giao dịch liên tục, giá dao động mạnh, nhưng bán một lượng nhỏ khá dễ. Vì thế câu hỏi “rủi ro bao nhiêu?” cần được tách thành những câu hỏi có thể kiểm tra: giá dao động ra sao, từng giảm sâu tới đâu, cần bao nhiêu tiền vào ngày nào và có bán được lượng cần thiết hay không.

Bài chia ba phiên. Phiên đầu tính trên một chuỗi giá trị; phiên hai đọc số lịch sử thật; phiên ba xử lý nhu cầu tiền và dữ liệu bẩn. Điểm dừng là lúc bạn giải thích được kết quả bằng lời mình, không phải lúc đã bấm ra một số phần trăm. Mọi ví dụ hư cấu được đánh dấu `KỊCH_BẢN`; chúng không phải danh mục được đề xuất.

## Ôn bài cũ

- Trong [Bài H2 — Ra quyết định dưới áp lực và quy mô vị thế](H2-decisions-stress-position-size.md) và [Bài A4 — Phân bổ tài sản, tương quan và tái cân bằng](A4-allocation-correlation-rebalancing.md), ta đã bàn về giới hạn vị thế. Bài H3 định lượng rủi ro qua độ biến động, sụt giảm tối đa (`Max Drawdown`) và thanh khoản.

---

## Phiên 1 — Đường đi của cùng một đồng vốn

### Từ số tiền sang lợi suất

`KỊCH_BẢN` Có một tài khoản bằng triệu VND, không vay, không góp hay rút tiền, đã cộng mọi thu nhập vào giá trị cuối kỳ. Mỗi kỳ là một tháng bằng quy ước của bài; chưa tính thuế cá nhân. Năm mốc quan sát liên tiếp là 100; 110; 88; 101,20; 106,26. Ta không biết giá trị giữa các mốc. Bảng là dữ liệu đầu vào đầy đủ cho phép tính mẫu, không phải đường giá thị trường.

| Mốc | Giá trị | Lợi suất tháng vừa qua | Đỉnh đã thấy | Giảm so với đỉnh |
|---|---:|---:|---:|---:|
| 0 | 100 | Không áp dụng | 100 | 0% |
| 1 | 110 | +10% | 110 | 0% |
| 2 | 88 | −20% | 110 | −20% |
| 3 | 101,20 | +15% | 110 | −8% |
| 4 | 106,26 | +5% | 110 | −3,4% |

`PHÉP_TÍNH` Lợi suất kỳ t là `r_t = V_t/V_(t−1) − 1`. Chẳng hạn kỳ ba: 101,20/88 − 1 = 15%. Mẫu số là vốn đầu đúng kỳ đó. Lợi suất cả bốn tháng là 106,26/100 − 1 = 6,26%; cũng bằng 1,10 × 0,80 × 1,15 × 1,05 − 1. Không cộng bốn tỷ lệ rồi gọi kết quả là tăng trưởng vốn.

Một thay đổi tài khoản không luôn là lợi suất. Nếu đầu có 100, góp thêm 50 và cuối còn 150 thì chưa có bằng chứng tài sản sinh lời 50%. Ngược lại, rút 20 ra khỏi tài khoản không tự là khoản lỗ đầu tư 20. Khi có dòng tiền ngoài, cần tách phần góp/rút và định giá đúng thời điểm; bài H4 sẽ làm đầy đủ. H3 chỉ dùng chuỗi không có dòng tiền ngoài để tránh trộn hai vấn đề.

### Biến động trả lời câu hỏi nào?

Biến động, hay volatility, trong bài là độ lệch chuẩn của các lợi suất tháng quanh trung bình số học. Trực giác là đo độ phân tán: các tháng có thường ở gần nhau hay rất xa nhau? Tăng bất thường cũng làm chỉ số lớn lên. Nó không chỉ đếm những tháng lỗ, cũng không đo trực tiếp số tiền cần dùng vào một hạn thanh toán.

`PHÉP_TÍNH` Trung bình số học của bốn lợi suất là `(0,10 − 0,20 + 0,15 + 0,05)/4 = 0,025`, tức 2,5%/tháng trong mẫu. Các độ lệch tương ứng là 0,075; −0,225; 0,125; 0,025. Bình phương rồi cộng được 0,0725. Độ lệch chuẩn mẫu là `s = căn[Σ(r_t − trung bình)^2/(n−1)]`; ở đây `căn(0,0725/3) = 0,155456`, khoảng 15,55% mỗi tháng quan sát.

Mẫu có bốn lợi suất nên n bằng bốn, không phải năm mốc giá trị. Chia cho n−1 là quy ước độ lệch chuẩn mẫu; nếu chọn mô tả tổng thể hữu hạn bằng mẫu số n thì phải ghi rõ và không trộn hai loại khi so sánh. [NIST, phần độ lệch chuẩn](https://www.itl.nist.gov/div898/handbook/eda/section3/eda356.htm) trình bày công thức mẫu và nhấn mạnh ảnh hưởng của các giá trị ở đuôi phân bố.

`SUY_LUẬN` Con số 15,55% không có nghĩa tháng tới chắc nằm trong một khoảng cố định, càng không có nghĩa xác suất mất toàn bộ vốn bằng không. Chỉ bốn tháng giả định không đủ mô tả một quá trình dài hạn. Bài không tự quy đổi lên năm: công thức căn số kỳ cần các giả định về phụ thuộc và tính ổn định của lợi suất mà dữ liệu này chưa chứng minh.

### Mức giảm từ đỉnh và mức tăng để trở lại

Sụt giảm từ đỉnh, hay drawdown, so giá trị hôm nay với đỉnh cao nhất đã xuất hiện trước đó hoặc ngay hôm nay. Khi có đỉnh mới, mốc tham chiếu đổi theo. Nó khác mức giảm so với ngày mua: ở mốc 2, tài khoản thấp hơn vốn đầu 12%, nhưng thấp hơn đỉnh 20%. Hai phát biểu đều đúng vì dùng hai mẫu số khác nhau.

`PHÉP_TÍNH` Gọi `P_t = max(V_0,…,V_t)`, thì `DD_t = V_t/P_t − 1`. Bài dùng dấu âm; mức sụt giảm tối đa là giá trị nhỏ nhất của DD, ở đây −20%. Có tài liệu báo độ lớn dương 20%; khi so sánh phải kiểm quy ước dấu. [Goldberg và Mahmoud, bản sửa 21/09/2016](https://arxiv.org/abs/1404.7493) nghiên cứu sụt giảm lớn nhất từ đỉnh đến đáy và sự khác biệt với các thước đo khác.

`PHÉP_TÍNH` Từ 110 xuống 88 mất 22. Muốn lấy lại 22 khi chỉ còn 88 cần tăng 22/88 = 25%, chứ không phải 20%. Với mức mất vốn d trong khoảng từ 0 đến dưới 100%, tỷ lệ tăng cần là `1/(1−d) − 1`. Giảm 50% cần tăng 100%. Công thức nói mức tăng cần thiết về số học, không nói khi nào hoặc liệu sự hồi phục có xảy ra.

Cuối chuỗi, vốn lớn hơn đầu 6,26% nhưng vẫn thấp hơn đỉnh 3,4%. Muốn từ 106,26 về 110 cần 110/106,26 − 1 ≈ 3,52%. Việc một tài khoản “đang có lãi” không loại bỏ sụt giảm từ đỉnh. Điểm dừng phiên một: tự giải thích ba tỷ lệ 6,26%, −3,4% và +3,52% bằng ba câu có nêu rõ mẫu số.

## Ví dụ từ nguồn thật

`SỰ_THẬT` Thư cổ đông Berkshire Hathaway năm 2024, đề ngày 22/02/2025, trang PDF 15, bảng so sánh lịch sử tại Hoa Kỳ, ghi S&P 500 có tính cổ tức: năm 2008 −37,0%, năm 2009 +26,5%. Đây là số phần trăm năm đã làm tròn trong nguồn; không phải số lợi nhuận kế toán, không áp dụng chuẩn VAS/IFRS. [Berkshire, thư 2024](https://www.berkshirehathaway.com/letters/2024ltr.pdf).

`PHÉP_TÍNH` Chuẩn hóa giá trị cuối 2007 thành 100 điểm, không góp/rút: cuối 2008 là 100 × 0,63 = 63; cuối 2009 là 63 × 1,265 = 79,695. Hai năm còn giảm 20,305% so với mốc đầu. Từ 63 để trở lại 100 cần tăng 100/63 − 1 ≈ 58,73%. Năm tăng 26,5% chưa bù đủ năm giảm 37,0%. Đầu vào là hai số làm tròn nên kết quả cũng chỉ là phép tái dựng xấp xỉ.

`SUY_LUẬN` Trong ba điểm cuối năm này, mức giảm lớn nhất là 37%. Không được gọi đó là sụt giảm tối đa thực tế của S&P 500 trong toàn khủng hoảng: đáy trong năm có thể thấp hơn, đỉnh trước cửa sổ có thể cao hơn. Cũng không thể biến 79,695 điểm thành tiền thực nhận của một quỹ: nguồn không cung cấp phí, thuế, sai lệch bám chỉ số hoặc khả năng thực hiện giao dịch của người học.

Nguồn gốc duy nhất cho hai tỷ lệ ở đây là bảng Berkshire; việc lưu bản PDF và đọc bản trực tuyến không tạo thành hai nguồn độc lập. Nguồn nghiên cứu drawdown giúp kiểm khái niệm, không xác nhận riêng hai con số chỉ số. Không dùng ca này để kết luận về rủi ro tương lai hoặc lựa chọn một sản phẩm. Điểm dừng phiên hai: viết điều bảng số cho phép tính, rồi viết hai điều nó chưa cho biết.

## Phiên 3 — Giá niêm yết khác tiền có thể dùng

`SỰ_THẬT` [SEC Investor.gov, mục thanh khoản](https://www.investor.gov/introduction-investing/investing-basics/glossary/liquidity-or-marketability) mô tả khả năng bán nhanh mà không làm giá bị tác động đáng kể. Một ảnh sổ lệnh cho thấy người mua đang chào giá nào và cho bao nhiêu đơn vị; đó chưa phải lời cam kết rằng mọi lệnh sẽ còn nguyên khi bạn bán. Đây là kiến thức thị trường chung, không phải mô tả quy tắc khớp lệnh cụ thể của HOSE.

`KỊCH_BẢN` Bạn có 1.200 cổ phiếu hư cấu, giá tham chiếu 20.000 VND/cổ phiếu. Sổ mua tĩnh có 200 cổ phiếu giá 20.000; 300 giá 19.800; 500 giá 19.000. Không có mức mua khác. Giả sử các lệnh này không đổi trong lúc bán, không thuế/phí, không giới hạn lô. Giá trị đánh dấu theo tham chiếu là 24 triệu, nhưng đó chưa phải tiền thu được.

`PHÉP_TÍNH` Bán vào toàn bộ lượng mua chỉ khớp 1.000 cổ phiếu: 200 × 20.000 + 300 × 19.800 + 500 × 19.000 = 19.440.000 VND. Bình quân 19.440 VND/cổ phiếu đã bán. Còn 200 cổ phiếu chưa bán được, không được âm thầm nhân chúng với một giá tưởng tượng. So với tham chiếu của đúng 1.000 cổ phiếu đã bán, hụt 560.000 VND, tức 2,8%; chưa có giá thực hiện cho toàn bộ 1.200.

Nếu cần 21 triệu tiền chi được hôm nay và chỉ có nguồn này, ngay cả phép tính trước phí cũng thiếu 1,56 triệu. Thêm ràng buộc tiền phải đã thanh toán thì tiền khớp giao dịch chưa chắc là tiền dùng ngay. Bài không đặt thời hạn thanh toán thực tế; cần kiểm quy định thị trường và tài khoản trước khi xác định ngày tiền khả dụng. Đừng lấy “bán được” thay cho “đã nhận tiền đúng hạn”.

`SUY_LUẬN` Rủi ro thanh khoản thị trường là khó chuyển tài sản thành tiền với giá hợp lý. Rủi ro thiếu tiền để thực hiện nghĩa vụ là câu hỏi về thời điểm thu/chi của người nắm giữ. Hai vấn đề có thể khuếch đại nhau: cần tiền gấp buộc bán vào thị trường mỏng, chịu giá thấp; giá thấp lại làm thiếu tiền nhiều hơn. Một chuỗi báo giá ít dao động không giải quyết vòng xoáy này.

Tập trung cũng cần đo riêng. Hai quỹ khác tên có thể cùng chịu một yếu tố ngành, quốc gia hoặc đồng tiền. Lịch sử biến động thấp của từng quỹ không tự chứng minh chúng bảo vệ nhau khi cùng gặp cú sốc. Mất vốn lâu dài còn phụ thuộc dòng tiền doanh nghiệp, nợ, pha loãng, quyền của chủ sở hữu và giá đã trả. Không thể chỉ nhìn một độ lệch chuẩn để kết luận tổn thất là tạm thời hoặc chắc chắn hồi phục.

## Bài tập

1. Từ chuỗi năm mốc của phiên một, tính bốn lợi suất và lợi suất toàn kỳ. Vì sao có bốn quan sát lợi suất?
2. Tính trung bình, tổng bình phương độ lệch và độ lệch chuẩn mẫu; ghi đúng đơn vị thời gian.
3. Điền đỉnh lũy kế và drawdown tại từng mốc. Vì sao mức lỗ từ vốn đầu khác mức giảm từ đỉnh ở mốc 2?
4. Tính mức tăng cần từ 88 về 110 và từ 106,26 về 110. Một tỷ lệ cần thiết có phải dự báo không?
5. Tái dựng 100 điểm qua hai năm 2008–2009 của S&P trong nguồn thật. Có thể suy drawdown ngày từ ba điểm cuối năm không?
6. Với sổ mua phiên ba, tính lượng bán được, lượng chưa bán, tổng tiền và bình quân. Nêu mẫu số khi tính hụt giá 2,8%.
7. Cần 21 triệu tiền dùng ngay: số tiền khớp trước phí trong bài có đủ không? Còn phải xác minh điều gì ngoài số học?
8. Một bảng đầu 100, cuối 150 có khoản góp 50 không ghi ngày. Hãy nêu điều chưa biết trước khi báo lợi suất hoặc drawdown.
9. Hai quỹ có giá gần như đứng yên suốt tháng, mỗi quỹ chỉ giao dịch một lần. Hãy đề xuất ba kiểm tra trước khi gọi chúng an toàn.
10. Chuyển giao: lập phiếu đo rủi ro cho một tài sản giả định có báo giá theo tuần, nhu cầu chi tiền theo ngày và thông tin nợ chưa đầy đủ; không đề xuất mua/bán.

## Đáp án

1. Lần lượt 10%, −20%, 15%, 5%; nhân hệ số cho 6,26%. Mỗi lợi suất cần một cặp mốc liền nhau, nên năm mốc tạo bốn khoảng.
2. Trung bình 2,5%; bình phương độ lệch cộng bằng 0,0725 khi dùng số thập phân; chia ba rồi căn được 15,5456%, làm tròn 15,55%/tháng mẫu. Không đổi thành xác suất lỗ.
3. Đỉnh lần lượt 100; 110; 110; 110; 110. Drawdown 0%; 0%; −20%; −8%; −3,4%. 88/100 − 1 = −12% so vốn đầu, còn 88/110 − 1 = −20% so đỉnh.
4. 110/88 − 1 = 25%; 110/106,26 − 1 ≈ 3,52%. Cả hai chỉ trả lời mức tăng cần nếu muốn về đích; chưa có bằng chứng về khả năng đạt đích.
5. 100 → 63 → 79,695. Toàn kỳ −20,305%. Hồi phục từ 63 cần 58,73%. Không biết đường đi trong năm nên không suy được đáy ngày hoặc thời gian hồi phục thực.
6. Khớp 1.000, còn 200; tiền 19,44 triệu; bình quân 19.440 VND. 560.000/20.000.000 = 2,8% dùng giá tham chiếu của phần đã bán, không phải toàn vị thế.
7. Thiếu 21 − 19,44 = 1,56 triệu trước phí. Cần biết lệnh có còn, thuế/phí, quy tắc thanh toán và thời điểm được sử dụng tiền; kết quả sổ tĩnh không bảo đảm tiền mặt.
8. Thiếu định giá ngay trước/sau góp, thời điểm dòng tiền và đường đi giữa hai mốc. Không gọi mức tăng tài khoản 50% là lợi suất. Chuyển sang quy trình H4 nếu cần đo chính xác.
9. Xem độ mới của giá, lượng mua thực và chênh lệch mua/bán; kiểm tài sản nền, nợ, điều kiện chuyển nhượng. Câu trả lời đạt khi phân biệt ít giao dịch với ít rủi ro và chỉ rõ nguồn cần lấy.
10. Phiếu đạt cần ghi cửa sổ và tần suất; giá có thu nhập/dòng tiền hay chưa; bảng nhu cầu tiền theo hạn; chiều sâu thanh khoản; nợ và quyền chưa biết; giới hạn phép đo. Không tự điền dữ kiện thiếu bằng giả định ngầm.

## Bài làm với dữ liệu thiếu hoặc lệch

`KỊCH_BẢN` Một bản chào có ba dòng: cuối tháng tài khoản 120 triệu; cuối tháng sau 90 “đơn vị”; góp thêm 30 triệu trong tháng; “độ biến động năm 2%” nhưng không kèm chuỗi. Người viết khẳng định drawdown −25% và tài sản an toàn do biến động thấp. Hãy làm biên bản nhận dữ liệu trước khi tính.

Cách xử lý đạt: hỏi “đơn vị” là triệu VND hay chứng chỉ, xin ngày và giá trị trước/sau góp, giá trị tại mọi mốc cần đo, cách xác định 2%, cách xử lý thu nhập. Lưu dữ liệu gốc rồi tạo bảng đã chuẩn hóa riêng. Ghi `CHƯA_BIẾT` với drawdown và biến động có thể kiểm chứng; không sửa 90 thành 90 triệu chỉ vì thấy thuận tiện. Nếu không lấy được dữ liệu bổ sung, chỉ nêu giới hạn, không xếp hạng an toàn.

## Sai ở đâu

“Danh mục giảm 20% rồi tăng 20% nên về hòa vốn; drawdown tối đa lịch sử 20% nghĩa là tương lai không thể lỗ hơn; tất cả cổ phiếu đều bán được ở giá hiển thị.” Có ba lỗi độc lập. `PHÉP_TÍNH` 100 × 0,8 × 1,2 = 96, chưa hòa vốn. Mức giảm lịch sử chỉ thuộc cửa sổ đã quan sát. Giá hiển thị thiếu lượng mua, phí và thời gian nhận tiền. Sửa một lỗi số học không tự sửa hai suy luận còn lại.

## Kiểm tra chuyển bài

Không nhìn mẫu: (1) giải thích vì sao một tài khoản lời từ ngày mua vẫn đang drawdown; (2) liệt kê dữ liệu để tách khoản rút khỏi khoản lỗ; (3) giải thích vì sao bán đủ lượng và nhận đủ tiền đúng hạn là hai kiểm tra. `Ý_KIẾN` Tiêu chí đạt: cả ba câu đúng về mẫu số, dòng tiền và thời điểm; nếu bỏ một điều kiện, quay lại phiên tương ứng trước H4.

## Tái lập và điều chưa biết

Chạy `python3 learning/practice/models/risk_performance.py`; các hàm `returns`, `sample_volatility`, `drawdowns`, `recovery`, `sell_book` tái lập ví dụ. Test trong [test_risk_performance.py](../../tests/test_risk_performance.py) kiểm cả chuỗi, dữ liệu thiếu và lượng không khớp. Mã không lấy dữ liệu thị trường, không dự báo, không gửi lệnh. `CHƯA_BIẾT`: phân bố lợi suất tương lai, thanh khoản khi khủng hoảng và mức mất vốn vĩnh viễn của một tài sản cụ thể; phải nghiên cứu riêng, không suy từ bài mẫu.

## Nguồn Internet đã mở

Truy cập lại ngày 02/11/2026, múi giờ Asia/Ho_Chi_Minh. Không dùng kết quả tìm kiếm thay nội dung nguồn.

| Nguồn gốc | Ngày/kỳ/đơn vị/phạm vi | Dùng trong bài |
|---|---|---|
| [NIST — Measures of Scale](https://www.itl.nist.gov/div898/handbook/eda/section3/eda356.htm) | Không ghi ngày; phương pháp thống kê; không tiền tệ | Độ lệch chuẩn mẫu |
| [Goldberg & Mahmoud](https://arxiv.org/abs/1404.7493) | 29/04/2014, sửa 21/09/2016, v5; nghiên cứu drawdown | Khái niệm và giới hạn thước đo |
| [SEC — Liquidity](https://www.investor.gov/introduction-investing/investing-basics/glossary/liquidity-or-marketability) | Không ghi ngày; Hoa Kỳ; không số thị trường | Khả năng bán và tác động giá |
| [Berkshire thư 2024](https://www.berkshirehathaway.com/letters/2024ltr.pdf) | 22/02/2025; PDF trang 15, năm 2008–2009; phần trăm S&P có cổ tức, cơ sở USD | Chuỗi số thực; số gốc làm tròn |

Bản nguồn và checksum được ghi trong [manifest nhóm 2](../../data/raw/learning-wave4-group2-sources-2026-11-02.json). Chưa thử khả năng hiểu bài với người học thật; các điểm dừng là đề xuất giảng dạy.
