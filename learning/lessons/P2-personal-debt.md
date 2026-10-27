# Bài P2 — Nợ cá nhân: đọc lãi suất thật và thứ tự ưu tiên

- Ngày: `2026-10-27`
- Chốt dữ liệu lúc: `2026-10-27 09:40 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Phân biệt lãi tính trên gốc ban đầu với lãi tính trên dư nợ giảm dần; quy đổi về lãi suất thật theo năm; biết thông tin một hợp đồng vay phải nêu; và so sánh trả nợ với đầu tư bằng tư duy lãi suất kỳ vọng mà không đưa lời khuyên cá nhân.
- Bài trước liên quan: [P1](P1-budget-emergency-fund-insurance.md), [N4](N4-time-value-returns.md) (lãi kép, chiết khấu).
- Thời lượng: Hai phiên; chưa đo thời gian học thực tế.
- Câu hỏi cốt lõi: **"1,5% mỗi tháng" thật sự là bao nhiêu mỗi năm, và nó so với lợi suất đầu tư kỳ vọng thế nào?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

## Hiểu bài này trong 1 phút

Hai khoản vay cùng ghi "1,5%/tháng" có thể đắt khác nhau hoàn toàn tùy lãi tính trên gốc ban đầu hay trên dư nợ còn lại. Muốn so sánh, quy mọi thứ về cùng một thước: lãi suất thật theo năm trên số tiền bạn còn nợ, cộng phí.

## Ôn bài cũ hoặc kiểm tra đầu vào

Đầu vào: gửi 100 đồng lãi 10% một năm thì cuối năm có bao nhiêu (110). Nếu vay thì ngược lại: bạn trả thêm phần lãi. Chưa cần công thức niên kim; sẽ làm trong ví dụ.

## Bài này làm gì và chưa làm gì

Dạy cách đọc lãi và chi phí vay, thông tin hợp đồng cần có, hồ sơ tín dụng và hai phương pháp trả nợ. Bài **chưa dạy thẻ tín dụng** (xem mục 7). Không khuyên bạn nên trả nợ hay đầu tư trước, không chọn phương pháp cho bạn, không kết luận một hợp đồng thực là hợp pháp hay vi phạm.

## 1. Lãi danh nghĩa, APR và lãi thật

`SỰ_THẬT` CFPB: lãi suất là chi phí trả cho bên cho vay; APR là lãi suất cộng các khoản phí khác bên cho vay tính. [CFPB — Interest rate vs APR](https://www.consumerfinance.gov/ask-cfpb/what-is-the-difference-between-a-loans-interest-rate-and-the-apr-en-733/) (sửa 31/08/2026). Đây là khái niệm Hoa Kỳ. `CHƯA_BIẾT` Chưa tìm thấy thuật ngữ "lãi suất hiệu dụng" được quy định ở Việt Nam; xem mục 2 cho quy định đã mở.

`PHÉP_TÍNH` Khoản vay trả đều (niên kim) cho lãi r mỗi tháng trong n tháng: `Số vay = Trả mỗi tháng × [1 − (1 + r)^(−n)] ÷ r`. Giả định: trả cuối mỗi kỳ, kỳ đầu cách ngày giải ngân đúng một kỳ, r cố định, không phí. Quy định lại tính theo số ngày thực tế (một năm 365 ngày) nên công thức theo tháng chỉ là xấp xỉ. Cho số vay và số trả, giải r bằng thử và sai (thử r, tính vế phải, chỉnh dần cho tới khi khớp số vay).

`KỊCH_BẢN` (hư cấu, công ty và hợp đồng đều hư cấu) Vay 30.000.000 đồng, 12 tháng, "lãi 1,5%/tháng" tính trên gốc ban đầu, không có phí, trả đều hằng tháng. Lãi mỗi tháng `30.000.000 × 1,5% = 450.000`; tổng lãi `450.000 × 12 = 5.400.000`; trả mỗi tháng `(30.000.000 + 5.400.000) ÷ 12 = 2.950.000` đồng. Lãi "trên gốc" quy năm: `1,5% × 12 = 18%/năm`. Nhưng bạn trả dần nên dư nợ giảm: giải `2.950.000 × [1 − (1+r)^−12] ÷ r = 30.000.000` được `r ≈ 2,64%/tháng`, tức khoảng `31,7%/năm` (cộng đơn) hoặc `(1,0264)^12 − 1 ≈ 36,8%/năm` (ghép lãi). Vậy "18%/năm" trên gốc ban đầu tương đương khoảng 32–37%/năm trên dư nợ còn lại. Phí giải ngân hay bảo hiểm khoản vay (không tính ở đây) làm con số cao hơn. Ví dụ chỉ minh họa kỹ thuật tính, không kết luận loại hợp đồng nào là hợp pháp hay gian lận.

`KỊCH_BẢN` Đối chứng: cùng "1,5%/tháng" nhưng tính trên **dư nợ giảm dần**, vay 30.000.000 đồng, 12 tháng. `PHÉP_TÍNH` Trả đều mỗi tháng `30.000.000 × 1,5% ÷ (1 − 1,015^−12) ≈ 2.750.400` đồng; tổng trả `≈ 33.004.800`; tổng lãi `≈ 3.004.800` đồng, so với 5.400.000 đồng ở cách tính trên gốc ban đầu. Lãi thật quy năm ghép lãi `1,015^12 − 1 ≈ 19,6%`. Cùng nhãn "1,5%/tháng" mà tổng lãi lệch khoảng 1,8 lần (5.400.000 so với 3.004.800); vì vậy phải hỏi *lãi tính trên cái gì*, không phải chỉ nhìn con số. Nếu bên cho vay là tổ chức tín dụng thuộc phạm vi Thông tư 39 (xem giới hạn ở mục 2), Điều 13 khoản 3 buộc thỏa thuận có mức lãi quy đổi theo %/năm trên dư nợ thực tế khi lãi không được nêu theo cách đó; với bên cho vay khác thì chưa suy ra được. `CHƯA_BIẾT` Văn bản không cho biết cách quy đổi nào (nhân 12 hay ghép lãi) được chấp nhận; bài chỉ đưa cả hai con số.

## 2. Hợp đồng vay phải nói gì (tổ chức tín dụng, Việt Nam)

`SỰ_THẬT` Bản hợp nhất Thông tư 39/2016/TT-NHNN (86/VBHN-NHNN, xác thực ngày 30/06/2026, phản ánh các sửa đổi tới Thông tư 29/2026 có hiệu lực 15/08/2026) có các quy định sau. [Bản hợp nhất trên datafiles.chinhphu.vn](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/86-vbhn-nhnn.pdf):

- Điều 16 khoản 1: trước khi lập thỏa thuận cho vay, tổ chức tín dụng phải cung cấp đầy đủ thông tin gồm lãi suất; nguyên tắc xác định lãi suất điều chỉnh; lãi suất với nợ gốc quá hạn; lãi suất với lãi chậm trả; phương pháp tính lãi; loại phí và mức phí.
- Điều 13 khoản 3: nếu mức lãi không được quy đổi theo %/năm và/hoặc không áp dụng phương pháp tính theo số dư nợ thực tế, thỏa thuận phải có mức lãi quy đổi theo %/năm (một năm 365 ngày) tính theo dư nợ thực tế và thời gian duy trì số dư đó.
- Điều 13 khoản 4: lãi chậm trả do hai bên thỏa thuận nhưng không vượt 10%/năm trên số dư lãi chậm trả; nợ gốc quá hạn thì lãi không vượt 150% lãi suất trong hạn tại thời điểm chuyển nợ quá hạn.
- Điều 18 khoản 4 (sửa bởi Thông tư 29/2026, hiệu lực 15/08/2026): với nợ quá hạn thu nợ gốc trước, lãi sau.

**Ai bị điều chỉnh.** Điều 2 khoản 2 của bản hợp nhất liệt kê tổ chức tín dụng cho vay gồm ngân hàng thương mại, ngân hàng hợp tác xã, tổ chức tín dụng phi ngân hàng, tổ chức tài chính vi mô, quỹ tín dụng nhân dân và chi nhánh ngân hàng nước ngoài. Nhưng Điều 5 khoản 2 nói các hoạt động cho vay cụ thể có văn bản riêng thì thực hiện theo văn bản riêng, trong đó có "hoạt động cho vay tiêu dùng của công ty tài chính" (điểm g) và cho vay của quỹ tín dụng nhân dân, tổ chức tài chính vi mô (điểm e); Thông tư 39 chỉ áp dụng cho nội dung văn bản riêng không quy định hoặc khi văn bản riêng dẫn chiếu. Ví dụ vay 30 triệu đồng 12 tháng ở trên là kiểu vay tiêu dùng điển hình của công ty tài chính, nên **không suy ra** rằng Điều 13, 16 áp nguyên cho nó. Thẻ tín dụng, vay giữa cá nhân, ứng dụng vay hay cho vay ngoài tổ chức tín dụng cũng không được suy ra từ văn bản này.

`CHƯA_BIẾT` Nội dung Thông tư 43/2016/TT-NHNN (cho vay tiêu dùng của công ty tài chính) và bản sửa đổi, văn bản về hoạt động thẻ, mức trần lãi suất hiện hành, và trần 20%/năm của Bộ luật Dân sự 2015 Điều 468 cùng ngưỡng hình sự đối với cho vay nặng lãi chưa được mở từ văn bản gốc nên bài không nêu chúng như dữ kiện. Cách xác minh: mở văn bản trên cổng văn bản pháp luật chính thức.

**Nếu không trả được nợ.** Cũng trong bản hợp nhất: Điều 21 khoản 1 cho phép tổ chức tín dụng chấm dứt cho vay và thu hồi nợ trước hạn theo thỏa thuận khi phát hiện khách hàng cung cấp thông tin sai sự thật hoặc vi phạm thỏa thuận; Điều 19 cho phép tổ chức tín dụng xem xét cơ cấu lại thời hạn trả nợ trên cơ sở đề nghị của khách hàng, thực hiện trước hoặc trong 10 ngày kể từ ngày đến kỳ hạn; Điều 20 nói nợ gốc không trả đúng hạn và không được chấp thuận cơ cấu lại sẽ chuyển nợ quá hạn, có thông báo cho khách hàng; Điều 21 khoản 2 cho phép tổ chức tín dụng áp dụng biện pháp thu hồi nợ theo thỏa thuận và hợp đồng bảo đảm, và nếu thu hồi không đủ thì khách hàng vẫn phải trả phần còn lại. Ý chính cho người học: liên hệ bên cho vay sớm, trước hạn, có thể mở ra lựa chọn cơ cấu lại; chờ quá hạn thì lãi và hậu quả tăng. Đây không phải tư vấn pháp lý và chỉ áp dụng cho bên cho vay thuộc phạm vi văn bản.

## 3. Hồ sơ tín dụng (CIC)

`SỰ_THẬT` Trung tâm Thông tin Tín dụng Quốc gia (CIC) thực hiện hoạt động thông tin tín dụng theo [Thông tư 15/2023/TT-NHNN](https://vanban.chinhphu.vn/?classid=1&docid=209158&orggroupid=4&pageid=27160), hiệu lực từ 01/01/2025. `CHƯA_BIẾT` Danh mục trường dữ liệu, phân loại nợ và ngưỡng ngày quá hạn hiện hành chưa đối chiếu đầy đủ từ văn bản gốc. Theo [Báo Điện tử Chính phủ dẫn ý kiến Ngân hàng Nhà nước, 22/09/2026](https://baochinhphu.vn/thoi-han-luu-giu-thong-tin-lich-su-no-xau-102260922073222586.htm), thông tin tiêu cực được CIC cung cấp tối đa 5 năm kể từ ngày kết thúc theo khoản 1 Điều 13 Thông tư 15. [Thông tư 46/2026/TT-NHNN](https://vanban.chinhphu.vn/?docid=219435&pageid=27160) sửa đổi có hiệu lực từ 01/11/2026; `CHƯA_BIẾT` tác động chi tiết sau ngày đó. Không dùng bài báo 2022 về Thông tư 03/2013 làm căn cứ hiện hành. Trễ hạn có thể ảnh hưởng hồ sơ tín dụng và việc vay sau này.

## 4. Hai cách trả nợ

`SỰ_THẬT` CFPB (tài liệu không in ngày xuất bản; metadata tệp 10/2018) mô tả hai chiến lược: trả khoản nhỏ nhất trước (snowball) và lãi cao nhất trước (avalanche); không chiến lược nào tốt hơn tuyệt đối. Khoản nhỏ trước cho cảm giác tiến triển nhanh nhưng có thể tốn tổng cộng nhiều hơn nếu khoản lớn có lãi và phí cao; lãi cao trước tiết kiệm tiền tổng thể nhưng tiến triển có thể chậm. [CFPB — Debt action plan, 10/2018](https://files.consumerfinance.gov/f/documents/cfpb_your-money-your-goals_debt-action-plan_tool_2018-11.pdf). Cả hai chỉ áp dụng khi đã trả đủ mức tối thiểu mọi khoản; chưa tính phạt trả nợ trước hạn hay khác biệt phí.

## 5. Trả nợ và đầu tư: tư duy lãi suất kỳ vọng

`SỰ_THẬT` FINRA mô tả trả nợ lãi cao như thẻ tín dụng là một trong những cách tốt để cải thiện nền tảng tài chính, nói khoản tiết kiệm được từ đó *có thể vượt* ("might exceed") lợi suất trung bình của hầu hết khoản đầu tư, và gợi ý cân bằng với việc xây quỹ khẩn cấp. [FINRA](https://www.finra.org/investors/investing/investing-basics/financial-foundations). Đây là nguồn Hoa Kỳ gắn với thẻ tín dụng lãi cao; việc nối sang Việt Nam là suy luận.

`SUY_LUẬN` Trả một khoản nợ có lãi 30%/năm tránh được chi phí bằng lãi suất khoản vay, còn lợi suất đầu tư chỉ là kỳ vọng và dao động. "Gần như chắc chắn" chỉ đúng khi không có phí trả nợ trước hạn (Điều 14 khoản 1 của bản hợp nhất cho phép thỏa thuận loại phí này) và khi bạn không cần giữ thanh khoản cho nhu cầu khẩn cấp. Ngược lại, với khoản vay lãi thấp, phép so sánh có thể cho kết quả khác, và còn phải tính quỹ khẩn cấp (P1). So sánh hai con số này chỉ giúp bạn hiểu vì sao nợ lãi cao thường là điểm cần cân nhắc cùng quỹ khẩn cấp. Bài không nói bạn nên làm gì: quyết định tùy mức lãi thực, hoàn cảnh và các ràng buộc khác. `KỊCH_BẢN` (số giả định, không phải dự báo) Khoản nợ 10.000.000 đồng lãi 8%/năm: giả sử dư nợ nếu không trả sớm giữ nguyên đủ một năm, không có phí trả trước và lãi không đổi; trả ngay tránh được `10.000.000 × 8% = 800.000` đồng lãi một năm. Nếu thay vào đó đem 10.000.000 đồng đi đầu tư, kết quả một năm có thể là lãi 1.500.000 đồng hoặc lỗ 2.000.000 đồng tùy năm; không con số nào được bảo đảm. Ví dụ chỉ cho thấy kết luận khác với khoản nợ lãi 30%/năm (tránh được 3.000.000 đồng), không nói bạn nên chọn gì.

**Không vay tiền để đầu tư**: đòn bẩy làm tăng rủi ro vượt khả năng chịu (P3). `CHƯA_BIẾT` Lãi tiết kiệm và lợi suất tham chiếu tại Việt Nam chưa được mở; cách xác minh là số liệu công bố của ngân hàng và Ngân hàng Nhà nước.

## 6. Nhận diện vay nóng

`SỰ_THẬT (thứ cấp)` Một bài báo năm 2020 trích Bộ Công an cảnh báo về ứng dụng vay tiền trực tuyến: Điều 201 Bộ luật Hình sự (cho vay lãi nặng) có các điều kiện về lãi suất và thu lợi bất chính hoặc tiền sử xử lý; bài cũng đề cập Điều 155, thông tin doanh nghiệp và điều khoản cần tìm hiểu, việc ứng dụng yêu cầu ảnh giấy tờ và quyền truy cập danh bạ, và tài liệu chứng minh khi tố cáo. [Báo Văn hóa, 09/07/2020](https://baovanhoa.vn/phap-luat/bo-cong-an-canh-bao-ve-bien-tuong-ung-dung-vay-tien-truc-tuyen-64234.html). Bài cũ và thứ cấp; không nêu đơn vị hay đường dây nóng cụ thể; không dùng thay văn bản pháp luật hiện hành.

`SUY_LUẬN` Việc ứng dụng yêu cầu quyền truy cập danh bạ hoặc ảnh giấy tờ là điều cần xem xét thận trọng; khi bị đe dọa, lưu bằng chứng và trình báo công an là gợi ý của giáo trình, không phải lời trích nguyên văn từ bài báo.

`CHƯA_BIẾT` Chưa mở được cảnh báo gốc hiện hành của Ngân hàng Nhà nước hay Bộ Công an; trần lãi theo Bộ luật Dân sự Điều 468 (nguồn thứ cấp nêu 20%/năm, "trừ trường hợp luật khác có quy định") chưa đối chiếu văn bản gốc. Vì quy tắc có thể khác theo loại bên cho vay (tổ chức tín dụng theo luật chuyên ngành, cá nhân theo Bộ luật Dân sự), câu hỏi đầu tiên luôn là *bên cho vay là ai*; một mức lãi bình thường với bên này có thể là vấn đề với bên kia. Bài không kết luận pháp lý cho trường hợp cụ thể.

`SUY_LUẬN` (cần nguồn trước khi dùng) Bảng dấu hiệu gợi ý:

| Dấu hiệu | Vì sao đáng lo | Nên làm |
|---|---|---|
| Đòi phí trước khi giải ngân | Có thể là lừa đảo, bạn mất phí mà không nhận tiền | Dừng, không chuyển thêm |
| Không có hợp đồng rõ ràng, lãi tính theo ngày hoặc tuần | Khó biết chi phí thật | Tự quy đổi ra %/năm; nếu không ghi rõ thì không ký |
| Ứng dụng đòi quyền danh bạ, ảnh, căn cước | Dữ liệu có thể bị dùng để gây áp lực | Không cấp quyền không cần thiết; không đưa căn cước, OTP hay mã xác thực |
| Đe dọa, nhắn cho người quen khi chậm trả | Hình thức gây áp lực (có thể liên quan hành vi đe dọa, bôi nhọ) | Lưu bằng chứng, trình báo công an |
| Vay thêm để trả khoản cũ | Vòng nợ | Dừng và tìm tư vấn tài chính chính thức |

Xem thêm [B3](B3-account-security-scams.md) cho nguyên tắc nhận diện lừa đảo.

`PHÉP_TÍNH` Đổi lãi theo ngày sang năm: lãi 0,5%/ngày, cộng đơn, bằng `0,5% × 365 = 182,5%/năm`; nếu ghép lãi hằng ngày là `1,005^365 − 1 ≈ 517%`. Con số nào cũng cho thấy khoản vay rất đắt so với lãi vay ngân hàng.

## 7. Thẻ tín dụng

`CHƯA_BIẾT` Chưa có nguồn đã mở về cách thẻ tín dụng ở Việt Nam tính lãi (thời gian miễn lãi, lãi tính từ ngày giao dịch, phí chậm thanh toán). Cách xác minh: đọc điều khoản thẻ của chính ngân hàng phát hành. `SUY_LUẬN` Vì vậy câu "chỉ trả tối thiểu là ổn" trong phần lỗi thường gặp cần được hiểu là cảnh báo chung: phần còn lại thường tiếp tục chịu lãi theo điều khoản của bạn.

## Năm câu hỏi khi đọc

1. Lãi tính trên gốc ban đầu hay trên dư nợ còn lại?
2. Lãi suất quy ra %/năm trên dư nợ thực tế là bao nhiêu, đã gồm phí chưa?
3. Lãi và phạt khi chậm trả, phí trả nợ trước hạn là gì?
4. Thông tin theo quy định đã được cung cấp đủ trước khi ký chưa?
5. Nợ này có ghi nhận ở hồ sơ tín dụng và ảnh hưởng vay sau này thế nào?

## Bài tập — làm trước khi mở đáp án

Câu 1–3 là phần cốt lõi; câu 4–6 là luyện thêm.

1. Vay 10.000.000 đồng, 10 tháng, lãi 2%/tháng tính trên gốc ban đầu. Tính tổng lãi và số trả mỗi tháng.
2. Lãi "2%/tháng trên gốc" quy năm là bao nhiêu? Có phải lãi thật theo năm trên dư nợ giảm dần không? Vì sao?
3. Liệt kê ít nhất bốn mục thông tin theo Điều 16 mà tổ chức tín dụng phải cung cấp trước khi ký.
4. Có hai khoản nợ: A nhỏ lãi thấp, B lớn lãi cao. Snowball và avalanche trả khoản nào trước? Mỗi cách được và mất gì?
5. Vì sao không nên chỉ nhìn số tiền trả hằng tháng khi so hai khoản vay?
6. Tư duy lãi suất kỳ vọng nói gì về nợ lãi cao so với đầu tư, và "lợi suất gần như chắc chắn" đúng trong điều kiện nào?
7. Lãi 0,5%/ngày cộng đơn tương đương bao nhiêu %/năm?

## Đáp án và điều cần hiểu

<details>
<summary>Mở sau khi tự làm</summary>

1. `PHÉP_TÍNH` Lãi mỗi tháng `10.000.000 × 2% = 200.000`; tổng lãi `2.000.000`; trả mỗi tháng `(10.000.000 + 2.000.000) ÷ 10 = 1.200.000` đồng.
2. `PHÉP_TÍNH` `2% × 12 = 24%/năm` trên gốc ban đầu. Không phải lãi thật trên dư nợ giảm dần: bạn trả dần nên số tiền đang nợ nhỏ hơn gốc, lãi thật cao hơn 24%. Giải `1.200.000 × [1 − (1+r)^−10] ÷ r = 10.000.000` cho `r ≈ 3,46%/tháng`, tức khoảng `41,5%/năm` cộng đơn hoặc `≈ 50,4%/năm` ghép lãi.
3. Lãi suất, nguyên tắc lãi điều chỉnh, lãi nợ quá hạn, lãi chậm trả, phương pháp tính lãi, loại và mức phí (chọn bốn).
4. Snowball trả A trước; avalanche trả B trước. Snowball cho tiến triển nhanh nhưng có thể tốn tổng cộng nhiều hơn; avalanche tiết kiệm tổng nhưng tiến triển chậm hơn. Không chiến lược nào tốt hơn tuyệt đối theo CFPB.
5. Vì lãi trên gốc, phí, bảo hiểm khoản vay, phí trả sớm và thời hạn khác nhau làm tổng chi phí khác.
6. Trả nợ lãi cao tránh được chi phí bằng lãi vay, còn đầu tư chỉ có lợi suất kỳ vọng và dao động; "gần như chắc chắn" chỉ đúng khi không có phí trả nợ trước hạn và bạn không cần giữ thanh khoản. Đó là cách so sánh, không phải chỉ dẫn.
7. `PHÉP_TÍNH` `0,5% × 365 = 182,5%/năm` cộng đơn (khoảng 517% nếu ghép lãi hằng ngày).

</details>

## Lỗi thường gặp

- So lãi %/tháng với %/năm, hoặc lãi trên gốc với lãi trên dư nợ giảm dần.
- Chỉ nhìn tiền trả hằng tháng, bỏ phí, phí trả nợ trước hạn, lãi quá hạn và bảo hiểm khoản vay.
- Coi "chỉ trả tối thiểu thẻ tín dụng" là ổn.
- Chủ quan vì không biết trễ hạn để lại dấu vết trong hồ sơ tín dụng.
- Coi hai khoản "cùng một mức lãi" là cùng chi phí, quên hỏi lãi tính trên gốc ban đầu hay dư nợ giảm dần.
- Áp quy định ngân hàng cho mọi bên cho vay.

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị trả nợ hay đầu tư trước, chọn avalanche hay snowball, đóng thẻ, gộp nợ hay vay một sản phẩm cụ thể.
- Hợp đồng và công ty trong ví dụ là hư cấu. Bài không kết luận hợp đồng thực nào hợp pháp hay vi phạm.
- Quy định Việt Nam chỉ phản ánh văn bản đã mở và phạm vi nêu; xác minh trước khi áp dụng.

## Điều tôi vẫn chưa hiểu

- Lãi thật theo năm trên dư nợ giảm dần của các khoản vay của tôi là bao nhiêu?
- Hợp đồng của tôi nói gì về phí trả nợ trước hạn và lãi quá hạn?
- Tôi đã xem hồ sơ tín dụng của mình chưa?

## Nguồn Internet đã mở

Ngày truy cập tất cả: `2026-10-27`.

| Nguồn | Ngày / phạm vi | Dùng cho |
|---|---|---|
| [CFPB — Interest rate vs APR](https://www.consumerfinance.gov/ask-cfpb/what-is-the-difference-between-a-loans-interest-rate-and-the-apr-en-733/) | Sửa 31/08/2026; Hoa Kỳ | Lãi suất và APR |
| [86/VBHN-NHNN](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/86-vbhn-nhnn.pdf) | Bản hợp nhất Thông tư 39/2016; Việt Nam; xác thực 30/06/2026 | Điều 2, 5, 13, 14, 16, 18, 19, 20, 21 |
| [Báo Văn hóa](https://baovanhoa.vn/phap-luat/bo-cong-an-canh-bao-ve-bien-tuong-ung-dung-vay-tien-truc-tuyen-64234.html) | 09/07/2020; thứ cấp | Cảnh báo ứng dụng vay |
| [Thị trường Tài chính Tiền tệ — CIC](https://thitruongtaichinhtiente.vn/hieu-dung-viec-thong-tin-xuat-hien-trong-he-thong-cic-38234.html) | 04/12/2021; thứ cấp | Nội dung CIC |
| [Tạp chí Ngân hàng](https://tapchinganhang.gov.vn/thoi-gian-luu-giu-lich-su-no-xau-tren-he-thong-trung-tam-thong-tin-tin-dung-quoc-gia-viet-nam-3131.html) | 22/08/2022; thứ cấp | Nguồn lịch sử về Thông tư 03/2013; không dùng làm căn cứ hiện hành |
| [Thông tư 15/2023](https://vanban.chinhphu.vn/?classid=1&docid=209158&orggroupid=4&pageid=27160); [Thông tư 46/2026](https://vanban.chinhphu.vn/?docid=219435&pageid=27160) | Hiệu lực lần lượt 01/01/2025 và 01/11/2026 | Văn bản thông tin tín dụng và mốc sửa đổi |
| [Báo Điện tử Chính phủ — ý kiến NHNN](https://baochinhphu.vn/thoi-han-luu-giu-thong-tin-lich-su-no-xau-102260922073222586.htm) | 22/09/2026; Việt Nam | Thời hạn cung cấp thông tin tiêu cực theo Thông tư 15 trước thay đổi tháng 11 |
| [CFPB — Debt action plan](https://files.consumerfinance.gov/f/documents/cfpb_your-money-your-goals_debt-action-plan_tool_2018-11.pdf) | 10/2018; Hoa Kỳ | Snowball, avalanche |
| [FINRA](https://www.finra.org/investors/investing/investing-basics/financial-foundations) | Không ghi ngày; Hoa Kỳ | Ưu tiên nợ lãi cao |

Không mở được trong lượt thu thập: thuvienphapluat.vn (nên chưa có Bộ luật Dân sự Điều 468, Thông tư 43/2016, Thông tư 11/2021). `PHÉP_TÍNH` Các ví dụ đã được điều phối viên tính lại bằng chương trình: lãi flat 18% cho `r ≈ 2,643%/tháng` (`≈ 31,7%/năm`, `≈ 36,8%/năm` ghép lãi); đối chứng dư nợ giảm dần trả `≈ 2.750.400`/tháng, tổng lãi `≈ 3.004.800`; bài tập 2 cho `r ≈ 3,46%/tháng`. Biên bản của bản trước (kiểm nguồn `ĐẠT`; phản biện `ĐẠT` với điểm trung bình) đã được xử lý trong bản này; cần kiểm lại phần đã đổi.
