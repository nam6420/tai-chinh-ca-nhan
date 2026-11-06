# Bài P1 — Ngân sách, quỹ khẩn cấp và bảo hiểm: nền trước khi đầu tư

- Ngày: `2026-10-27`
- Chốt dữ liệu lúc: `2026-10-27 09:40 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Lập được bảng dòng tiền hằng tháng từ số liệu thật, tính được mục tiêu quỹ khẩn cấp theo hoàn cảnh của mình, và phân biệt bảo hiểm (chuyển rủi ro) với đầu tư (chấp nhận rủi ro để tìm lợi nhuận).
- Bài trước liên quan: Không yêu cầu kiến thức tài chính; nên học trước [N1](N1-market-basics.md) và trước khi dùng tiền vào đầu tư. Học tiếp [P2](P2-personal-debt.md).
- Thời lượng: Hai phiên ngắn; chưa đo thời gian học thực tế.
- Câu hỏi cốt lõi: **Nếu một tháng tôi mất thu nhập hoặc có khoản chi lớn bất ngờ, tôi có phải bán tài sản đầu tư giữa lúc giá xấu không?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

## Hiểu bài này trong 1 phút

Đầu tư là việc của tiền chưa cần dùng. Quỹ khẩn cấp và bảo hiểm là lớp đệm để một biến cố (mất việc, nằm viện) không buộc bạn bán tài sản đầu tư đúng lúc giá thấp. Bài này không bảo bạn phải giữ bao nhiêu; nó chỉ dạy cách tính theo hoàn cảnh riêng và cách đọc các nguồn khuyến nghị.

## Ôn bài cũ hoặc kiểm tra đầu vào

- **Điểm xuất phát (Trước khi mở tài khoản chứng khoán):** Đây là bài khởi đầu về tài chính cá nhân, khuyến nghị đọc **trước hoặc song song với [Bài B3 — Bảo vệ tài khoản và nhận diện lừa đảo](B3-account-security-scams.md) và [Bài N1 — Thị trường chứng khoán vận hành thế nào?](N1-market-basics.md)** (học tiếp: [Bài P2 — Nợ cá nhân](P2-personal-debt.md)).
- **Kiểm tra đầu vào:** Giá cổ phiếu có thể giảm trong thời gian ngắn mà doanh nghiệp không hỏng (sẽ học ở [Bài N1](N1-market-basics.md) và [Bài 002](002-finding-a-cheap-stock.md)). Hỏi: nếu bạn buộc phải bán đúng lúc đó để trả viện phí thì điều gì xảy ra? Đáp án: bạn chốt lỗ vì nhu cầu tiền, không vì đánh giá lại doanh nghiệp.

## Bài này làm gì và chưa làm gì

Dạy lập ngân sách, tính quỹ khẩn cấp và đọc khái niệm bảo hiểm ở mức nhập môn. Không chọn mức quỹ, loại bảo hiểm, sản phẩm hay ngân hàng cho bạn. Các quy định bảo hiểm, bảo hiểm xã hội và bảo hiểm tiền gửi của Việt Nam chỉ ở mức tổng quan và phải kiểm lại văn bản gốc.

## 1. Ngân sách là bảng dòng tiền, không phải một tỷ lệ cố định

`SỰ_THẬT` CFPB (Hoa Kỳ) mô tả các bước: liệt kê mọi nguồn thu, ghi chi tiêu theo nhóm, lập lịch hóa đơn và ngày đến hạn vì thu và chi lệch thời điểm gây thiếu hụt, rồi lập ngân sách làm việc. [CFPB — Budgeting](https://www.consumerfinance.gov/archive/blog/budgeting-how-to-create-a-budget-and-stick-with-it/) (đăng 05/06/2019; trang là nội dung lưu trữ và có thể lỗi thời).

`Ý_KIẾN` Bài này không dạy tỷ lệ cố định như 50/30/20 làm chân lý vì thu nhập, nghĩa vụ và chi phí sống khác nhau. Bắt đầu từ số liệu thật của chính bạn.

## 2. Quỹ khẩn cấp

`SỰ_THẬT` CFPB: quỹ khẩn cấp là khoản tiền dành riêng cho chi phí ngoài dự kiến; mức cần có phụ thuộc hoàn cảnh; xem lại các khoản bất ngờ đã từng gặp để đặt mục tiêu; số tiền nhỏ vẫn có ích; nơi giữ cần an toàn, dễ rút và khó bị tiêu vào việc khác. [CFPB — Emergency fund](https://www.consumerfinance.gov/an-essential-guide-to-building-an-emergency-fund/) (trang ghi sửa lần cuối 29/10/2025).

`SỰ_THẬT` FINRA (Hoa Kỳ) ghi rằng các nhà hoạch định thường khuyến nghị khoảng 3–6 tháng chi phí sinh hoạt, và có thể cần nhiều hơn nếu thu nhập biến động hoặc nghề chuyên biệt; thứ tự FINRA đề xuất là biết dòng tiền, tính tài sản ròng, xử lý nợ rồi xây quỹ. [FINRA — Financial foundations](https://www.finra.org/investors/investing/investing-basics/financial-foundations) (không ghi ngày); [FINRA — Financial hardship](https://www.finra.org/investors/insights/prepare-survive-financial-hardship) (30/04/2024). Đây là khuyến nghị của một cơ quan Hoa Kỳ, không phải chuẩn Việt Nam.

`PHÉP_TÍNH` Công thức: `mục tiêu quỹ = số tháng đặt ra × chi thiết yếu mỗi tháng`; `còn thiếu = mục tiêu − số đã có`; `số tháng góp = còn thiếu ÷ số tiền để dành mỗi tháng` (làm tròn lên, chưa tính lãi).

`KỊCH_BẢN` (hư cấu) Minh có thu nhập thực nhận 20.000.000 đồng/tháng; chi thiết yếu: thuê nhà 5.000.000, ăn uống 4.000.000, điện nước internet đi lại 2.500.000, bảo hiểm 800.000, tổng 12.300.000 đồng; đã có 15.000.000 đồng tiết kiệm riêng; để dành được 3.000.000 đồng/tháng. Với mốc 3 tháng: `3 × 12.300.000 = 36.900.000` đồng; còn thiếu `36.900.000 − 15.000.000 = 21.900.000` đồng; `21.900.000 ÷ 3.000.000 = 7,3`, tức 8 tháng góp. Với mốc 6 tháng: `73.800.000` đồng. Mốc 6 tháng cần `73.800.000 − 15.000.000 = 58.800.000` đồng, tức `58.800.000 ÷ 3.000.000 = 19,6`, làm tròn thành 20 tháng góp, gấp khoảng 2,5 lần mốc 3 tháng. Dòng "bảo hiểm 800.000" trong ví dụ giả định là khoản bảo hiểm tự nguyện Minh đang đóng, chưa gồm phần đóng bắt buộc đã trừ khỏi thu nhập thực nhận. Ví dụ chỉ minh họa cách tính; không nói Minh "nên" giữ mấy tháng.

`KỊCH_BẢN` Minh thứ hai (hư cấu): thu nhập biến động, đang nuôi một người phụ thuộc, chi thiết yếu 18.000.000 đồng/tháng, chưa có tiết kiệm. Cùng công thức, mốc 3 tháng đã là `54.000.000` đồng và cần nhiều thời gian hơn để đạt. Hai ví dụ cho thấy cùng một công thức cho kết quả rất khác tùy hoàn cảnh, nên không có con số chung cho mọi người.

Điểm dừng: tự dựng bảng chi thiết yếu của mình, chưa cần biết số tháng.

### Quan điểm khác về khung "3–6 tháng"

`Ý_KIẾN` (blog cá nhân Hoa Kỳ, 07/09/2016) Trong khi bàn về mốc 3–6 tháng, tác giả Early Retirement Now viết rằng ông có lẽ đồng ý với tổng số tiền dự phòng mà một nhà phân tích tính, nhưng không xác định rõ số đó có đúng bằng 3–6 tháng hay không. Ông phản đối việc giữ toàn bộ bằng tiền mặt vì chi phí cơ hội và phản đối khuyến nghị 8 tháng của Suze Orman; ông mô tả cách dự phòng của mình bằng một danh mục tài sản tài chính lớn. Trong phần bình luận, ông đề cập đến tiết kiệm tích cực ở các tài khoản khác. [Early Retirement Now](https://earlyretirementnow.com/2016/09/07/debunking-emergency-funds-part1/). Đây là quan điểm cá nhân trong bối cảnh Hoa Kỳ, không đủ để xác định mức phù hợp cho người học; `CHƯA_BIẾT` mức tối ưu có được nghiên cứu học thuật chứng minh hay không. Ở chiều ngược lại, 3 tháng có thể quá ít nếu tìm việc lâu. Hộ Việt Nam còn có yếu tố riêng (thu nhập phi chính thức, hỗ trợ gia đình, bảo hiểm thất nghiệp, chi y tế tự trả) mà bài chưa có dữ liệu để định lượng (`CHƯA_BIẾT`).

### Lạm phát và nơi giữ quỹ

`SUY_LUẬN` Tiền giữ lâu có thể mất sức mua nếu lãi suất thấp hơn lạm phát; ngược lại, gửi kỳ hạn dài để lãi cao hơn có thể mất lãi khi rút trước hạn. Với quỹ khẩn cấp, khả năng rút nhanh thường được cân nhắc trước lãi cao. `CHƯA_BIẾT` Lãi suất tiết kiệm và lạm phát Việt Nam hiện nay chưa được mở; cách xác minh là số liệu của Tổng cục Thống kê và Ngân hàng Nhà nước. Quỹ cũng không nên toàn bộ nằm ở tài sản dao động mạnh như cổ phiếu (xem bài tập 6).

## 3. Nơi giữ quỹ và bảo hiểm tiền gửi

`SỰ_THẬT` Theo [Bảo hiểm tiền gửi Việt Nam](https://div.gov.vn/tu-ngay-13-7-2026-han-muc-chi-tra-tien-bao-hiem-cua-bao-hiem-tien-gui-viet-nam-la-350-trieu-dong), từ 13/07/2026 hạn mức chi trả thông thường là 350 triệu đồng cho tổng gốc và lãi tiền gửi được bảo hiểm của một người tại một tổ chức tham gia, theo Thông tư 05/2026/TT-NHNN. Hạn mức có thể thay đổi; kiểm lại khi sử dụng. Phần vượt hạn mức có thể không được chi trả đủ theo mức thông thường; việc chia tiền là quyết định của người gửi.

`SỰ_THẬT` [Bảo hiểm tiền gửi Việt Nam](https://www.div.gov.vn/quy-trinh-chi-tra-bao-hiem-tien-gui-theo-luat-bao-hiem-tien-gui-nam-2025-bao-dam-tot-hon-quyen-loi-nguoi-gui-tien) nêu thời hạn chi trả tối đa 45 ngày kể từ khi phát sinh nghĩa vụ trả tiền bảo hiểm và cơ chế đặc biệt trong điều kiện luật định. `CHƯA_BIẾT` Các trường hợp loại trừ và điều kiện chi trả vượt hạn mức cần kiểm đầy đủ trong Luật Bảo hiểm tiền gửi 2025; không suy ra rằng mọi khoản tiền gửi đều được bảo hiểm.

`KỊCH_BẢN` Nếu một người có 400.000.000 đồng gửi tại một tổ chức tham gia, phần vượt mức tối đa là `400.000.000 − 350.000.000 = 50.000.000` đồng (giả sử toàn bộ tiền gửi thuộc phạm vi được bảo hiểm, không có khoản nợ tại tổ chức đó và áp dụng hạn mức thông thường). Mức tối đa này nói về giới hạn chi trả của bảo hiểm, không nói lãi suất hay xác suất tổ chức gặp khó khăn.

## 4. Bảo hiểm khác đầu tư

`Ý_KIẾN` Bảo hiểm chuyển một rủi ro tài chính lớn (bệnh nặng, tai nạn, mất người trụ cột) sang bên khác để đổi lấy phí; đầu tư chấp nhận rủi ro để tìm lợi nhuận kỳ vọng. Trộn hai thứ này có thể dẫn tới quyết định tồi, ví dụ mua sản phẩm vừa bảo hiểm vừa đầu tư mà không hiểu phí. `CHƯA_BIẾT` Chưa có nguồn pháp luật hoặc cơ quan quản lý đã mở để dẫn cho định nghĩa này, nên đây là cách diễn đạt của giáo trình. Không phải ai cũng cần mọi loại bảo hiểm, và thứ tự ưu tiên tùy hoàn cảnh; bài này không khuyến nghị mua loại nào.

`SỰ_THẬT` (thứ cấp, Nhân Dân, 2025) Về bảo hiểm liên kết đầu tư, bài báo nêu phí ban đầu có thể bị khấu trừ tới mức tối đa 50% phí năm đầu, 30% năm hai, 20% năm 3–5 và 2% từ năm sáu; giá trị hoàn lại thấp trong 2–3 năm đầu; có tranh chấp do bán hàng sai thông tin và hai công ty bảo hiểm bị phạt vì thông tin sai hoặc gây hiểu nhầm. [Nhân Dân](https://nhandan.vn/cuoc-dai-phau-thi-truong-bao-hiem-nhan-tho-post882473.html). `CHƯA_BIẾT` Văn bản gốc (Nghị định 46/2023/NĐ-CP) chưa mở; không dùng các con số này để kết luận sản phẩm cụ thể tốt hay xấu.

`SỰ_THẬT` Điều 35 [Văn bản hợp nhất Luật Kinh doanh bảo hiểm](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/31-vbhn-vpqh.pdf) quy định với hợp đồng có thời hạn trên một năm, bên mua có 21 ngày kể từ khi nhận hợp đồng để từ chối tiếp tục tham gia; phí đã đóng được hoàn lại sau khi trừ chi phí hợp lý theo thỏa thuận nếu có, và doanh nghiệp không phải chi trả bảo hiểm khi xảy ra sự kiện bảo hiểm. Phải đọc điều khoản và kiểm hiệu lực tại thời điểm áp dụng.

`CHƯA_BIẾT` Cấu trúc phí, thời hạn tối thiểu và ai chịu rủi ro đầu tư của bảo hiểm liên kết đầu tư (Nghị định 46/2023/NĐ-CP); loại trừ, thời gian chờ, mức khấu trừ của bảo hiểm sức khỏe và tai nạn. Bài không đưa con số hay kết luận "tốt/xấu" cho nhóm này; cách xác minh là đọc bộ quy tắc điều khoản và bảng minh họa quyền lợi của sản phẩm thật.

`SỰ_THẬT` Theo [Bảo hiểm xã hội Việt Nam, 30/05/2025](https://baohiemxahoi.gov.vn/tintuc/Pages/hoat-dong-bhxh-viet-nam.aspx?CateID=0&ItemID=24900), mức đóng tổng hợp cho người lao động Việt Nam thuộc diện nêu trong nguồn là người lao động 10,5% (8% hưu trí và tử tuất, 1,5% y tế, 1% thất nghiệp) và người sử dụng lao động 21,5%, gồm BHXH, BHYT và BHTN. `CHƯA_BIẾT` Điều khoản gốc, mức trần lương đóng và quyền lợi chi tiết chưa được đối chiếu đầy đủ. Bài chỉ nêu tổng quan: kiểm tra mình đã được đóng đúng chưa trên cổng bảo hiểm xã hội chính thức.

## Năm câu hỏi khi đọc

1. Khoản này là thu hay chi thiết yếu, và nó xảy ra mỗi tháng hay theo kỳ?
2. Tiền đang giữ cho mục đích gì và cần dùng trong bao lâu?
3. Nếu thu nhập dừng lại, tiền có đủ cho bao nhiêu tháng chi thiết yếu của tôi?
4. Khoản bảo hiểm này chuyển rủi ro nào, và loại trừ gì?
5. Con số quy định tôi đang dùng có ngày hiệu lực và nguồn gốc nào?

## Bài tập — làm trước khi mở đáp án

Câu 1–3 là phần cốt lõi; câu 4–6 là luyện thêm.

1. Chi thiết yếu 10.000.000 đồng/tháng, đã có 12.000.000 đồng. Quỹ 4 tháng cần bao nhiêu, còn thiếu bao nhiêu?
2. Nếu để dành được 2.000.000 đồng mỗi tháng, cần mấy tháng để đạt mốc câu 1?
3. Cùng một mốc "6 tháng" có thể quá nhiều với người này và quá ít với người khác. Phân các yếu tố sau thành hai cột "làm cần quỹ lớn hơn" và "làm cần quỹ nhỏ hơn": thu nhập biến động; có bảo hiểm sức khỏe tốt; có người phụ thuộc; có người thân sẵn sàng hỗ trợ; nghề chuyên biệt khó tìm việc; chi thiết yếu thấp.
4. Một người gửi 500 triệu đồng thuộc phạm vi được bảo hiểm tại một tổ chức tham gia và không có nợ tại tổ chức đó. Nếu hạn mức thông thường là 350 triệu đồng, mức chi trả tối đa là bao nhiêu? Mức đó có cho biết lãi suất hay độ an toàn tuyệt đối không?
5. Phân biệt bảo hiểm và đầu tư bằng một câu.
6. Vì sao không nên giữ quỹ khẩn cấp hoàn toàn ở cổ phiếu?

## Đáp án và điều cần hiểu

<details>
<summary>Mở sau khi tự làm</summary>

1. `PHÉP_TÍNH` `4 × 10.000.000 = 40.000.000`; thiếu `40.000.000 − 12.000.000 = 28.000.000` đồng.
2. `28.000.000 ÷ 2.000.000 = 14` tháng, chưa tính lãi.
3. Cần quỹ lớn hơn: thu nhập biến động; có người phụ thuộc; nghề chuyên biệt khó tìm việc. Cần quỹ nhỏ hơn: bảo hiểm sức khỏe tốt; có người thân sẵn sàng hỗ trợ; chi thiết yếu thấp. Mỗi yếu tố chỉ là chiều hướng, không cho ra con số.
4. Với giả định toàn bộ khoản tiền thuộc phạm vi bảo hiểm, tối đa 350 triệu đồng theo hạn mức thông thường; phần 150 triệu đồng nằm ngoài mức đó. Có cơ chế đặc biệt với điều kiện riêng; bài chưa xác minh đủ điều kiện. Hạn mức không cho biết lãi suất hay độ an toàn tuyệt đối.
5. Bảo hiểm chuyển rủi ro lớn đổi lấy phí; đầu tư chấp nhận rủi ro để tìm lợi nhuận kỳ vọng.
6. Giá cổ phiếu có thể giảm đúng lúc cần tiền, buộc bán trong điều kiện xấu; quỹ khẩn cấp thường ưu tiên khả năng rút nhanh và hạn chế biến động danh nghĩa. Tiền gửi không kỳ hạn hoặc kỳ hạn ngắn có thể được cân nhắc nhưng không bảo đảm tuyệt đối: còn rủi ro tổ chức nhận tiền, giới hạn và điều kiện bảo hiểm, lạm phát và lãi suất. Rút sớm tiền gửi kỳ hạn dài có thể mất lãi.

</details>

## Lỗi thường gặp

- Coi "6 tháng" hay "50/30/20" là chân lý, bỏ qua hoàn cảnh riêng.
- Gộp quỹ khẩn cấp với tiền đầu tư.
- Mua bảo hiểm liên kết đầu tư như thể gửi tiết kiệm mà không đọc phí, thời gian đóng và điều kiện rút.
- Nhầm giới hạn chi trả của bảo hiểm tiền gửi với bảo đảm an toàn tuyệt đối.
- Quên kiểm tra ngày hiệu lực của mức hạn mức đang dùng.

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị về số tháng quỹ, loại hay hãng bảo hiểm, hoặc ngân hàng để gửi.
- Mọi số liệu nhân vật Minh là `KỊCH_BẢN` hư cấu.
- Bài kết hợp nguồn cơ quan và một số nguồn thứ cấp; các điều kiện còn chưa biết cần được đối chiếu văn bản gốc hiện hành trước khi áp dụng.

## Điều tôi vẫn chưa hiểu

- Chi thiết yếu thật của tôi là bao nhiêu, theo dữ liệu tháng gần nhất?
- Hợp đồng bảo hiểm tôi có loại trừ gì và thời gian chờ nào?
- Tôi đã được đóng bảo hiểm xã hội và y tế đầy đủ chưa?

## Nguồn Internet đã mở

Ngày truy cập tất cả: `2026-10-27`. Ngày dưới là ngày đăng hoặc sửa của trang.

| Nguồn | Ngày / phạm vi | Dùng cho |
|---|---|---|
| [CFPB — Budgeting](https://www.consumerfinance.gov/archive/blog/budgeting-how-to-create-a-budget-and-stick-with-it/) | 05/06/2019, trang lưu trữ; Hoa Kỳ | Các bước ngân sách |
| [CFPB — Emergency fund](https://www.consumerfinance.gov/an-essential-guide-to-building-an-emergency-fund/) | Sửa 29/10/2025; Hoa Kỳ | Định nghĩa quỹ khẩn cấp |
| [FINRA — Financial foundations](https://www.finra.org/investors/investing/investing-basics/financial-foundations) | Không ghi ngày; Hoa Kỳ | 3–6 tháng, thứ tự |
| [FINRA — Hardship](https://www.finra.org/investors/insights/prepare-survive-financial-hardship) | 30/04/2024; Hoa Kỳ | "Mọi khoản đều có ích" |
| [Luật Kinh doanh bảo hiểm hợp nhất](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/31-vbhn-vpqh.pdf) | 13/03/2026; Việt Nam | Điều 35, thời gian cân nhắc 21 ngày |
| [Bảo hiểm xã hội Việt Nam](https://baohiemxahoi.gov.vn/tintuc/Pages/hoat-dong-bhxh-viet-nam.aspx?CateID=0&ItemID=24900) | 30/05/2025; Việt Nam | Tổng tỷ lệ BHXH, BHYT, BHTN cho đối tượng nêu trong nguồn |
| [Bảo hiểm tiền gửi Việt Nam — hạn mức](https://div.gov.vn/tu-ngay-13-7-2026-han-muc-chi-tra-tien-bao-hiem-cua-bao-hiem-tien-gui-viet-nam-la-350-trieu-dong) | 15/07/2026; Việt Nam | Hạn mức thông thường |
| [Bảo hiểm tiền gửi Việt Nam — chi trả](https://www.div.gov.vn/quy-trinh-chi-tra-bao-hiem-tien-gui-theo-luat-bao-hiem-tien-gui-nam-2025-bao-dam-tot-hon-quyen-loi-nguoi-gui-tien) | 2026; Việt Nam | Thời hạn chi trả và cơ chế đặc biệt |
| [Nhân Dân](https://nhandan.vn/cuoc-dai-phau-thi-truong-bao-hiem-nhan-tho-post882473.html) | 26/05/2025; thứ cấp | Phí bảo hiểm liên kết đầu tư |
| [Early Retirement Now](https://earlyretirementnow.com/2016/09/07/debunking-emergency-funds-part1/) | 07/09/2016; blog cá nhân Hoa Kỳ | Quan điểm về giữ quỹ bằng tiền mặt và mức 8 tháng |

Không dùng được trong lượt thu thập: investor.gov, Bogleheads, thuvienphapluat.vn và ssc.gov.vn (lỗi truy cập); một bài báo 2017 về hạn mức 50 triệu đồng đã lỗi thời nên không dùng. Biên bản của bản trước (kiểm nguồn `ĐẠT`; phản biện `ĐẠT` có điều kiện) đã được xử lý trong bản này; cần kiểm lại phần đã đổi. `CHƯA_BIẾT` hiệu quả học thực tế.
