# Bài B3 — Bảo vệ tài khoản và nhận diện lừa đảo đầu tư

- Ngày: `2026-10-27`
- Chốt dữ liệu lúc: `2026-10-27 10:39 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Nhận ra các dấu hiệu lừa đảo đầu tư phổ biến, biết cách tự kiểm tra một đơn vị có được cấp phép hay không, giữ tài khoản an toàn ở mức cơ bản và biết việc cần làm ngay khi nghi bị lừa.
- Bài trước liên quan: Không yêu cầu kiến thức tài chính; nên học trước khi chuyển tiền vào bất kỳ tài khoản đầu tư nào. Học tiếp [N1](N1-market-basics.md).
- Thời lượng: Một đến hai phiên ngắn; chưa đo thời gian học thực tế.
- Câu hỏi cốt lõi: **Trước khi chuyển tiền cho một nơi tự nhận là đầu tư, tôi kiểm tra được điều gì và dừng khi thấy dấu hiệu nào?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

## Hiểu bài này trong 1 phút

Kẻ lừa đảo không cần hiểu thị trường; chúng cần bạn chuyển tiền hoặc đưa mã xác thực. Mẫu hình lặp lại: ai đó chủ động tiếp cận (có thể là người lạ, cũng có thể là người giả làm người quen hoặc cơ quan), hứa lợi nhuận chắc chắn hoặc đe dọa, tạo áp lực thời gian, rồi đưa bạn tới một nơi nhận tiền không phải công ty được cấp phép. `SUY_LUẬN` Tự kiểm tra trước khi chuyển tiền có thể giúp giảm rủi ro, nhưng không bảo đảm phát hiện mọi thủ đoạn. `Ý_KIẾN` Bị lừa không có nghĩa là bạn kém thông minh: kẻ lừa đảo làm việc này chuyên nghiệp và dùng cả công nghệ giả giọng, giả mặt. Đừng để xấu hổ làm bạn chậm báo.

## Ôn bài cũ hoặc kiểm tra đầu vào

Đầu vào: nhớ lại bài N1, khi mua cổ phiếu thì tiền của bạn đi qua đâu trước khi đến người bán? Đáp án: qua công ty chứng khoán và hệ thống thanh toán theo quy định, chứ không phải chuyển thẳng vào tài khoản cá nhân của người lạ. Chưa cần biết quy trình cụ thể của thị trường Việt Nam.

## Bài này làm gì và chưa làm gì

Dạy nguyên tắc nhận diện, kiểm tra tư cách đơn vị, bảo mật cơ bản và việc cần làm đầu tiên. Không thay thế hướng dẫn của công ty chứng khoán hay ngân hàng bạn dùng, không liệt kê mọi hình thức lừa đảo, không bảo đảm khả năng thu hồi tiền và không phải tư vấn pháp lý. Quy định cụ thể và đường dây báo cáo chính thức tại Việt Nam cần được kiểm lại tại cơ quan gốc.

## 1. Mẫu hình lừa đảo đã được cơ quan Việt Nam cảnh báo

`SỰ_THẬT` (thứ cấp, qua báo chí đăng lại phát biểu cơ quan) Các cảnh báo từ Ủy ban Chứng khoán Nhà nước (UBCKNN), Bộ Công an và Ngân hàng Nhà nước (NHNN) mô tả những điểm sau; mỗi điểm ghi rõ nguồn nào nói:

- *Nhóm chat và tài khoản "chim mồi"*: Tạp chí Kinh tế Tài chính (07/10/2025) mô tả mời qua nhóm Zalo, Viber, Telegram, có livestream và tài khoản "chim mồi" khoe lãi; Nhà đầu tư (04/05/2024, lời phát ngôn Bộ Công an) mô tả nhóm chat kín, người mời tự xưng chuyên gia hoặc nhân viên công ty chứng khoán, và tài khoản ảo khoe lãi. [Tạp chí Kinh tế Tài chính](https://tapchikinhtetaichinh.vn/uy-ban-chung-khoan-nha-nuoc-canh-bao-lua-dao-lien-quan-cong-ty-sticcapital-69448.html); [Nhà đầu tư](https://nhadautu.vn/bo-cong-an-canh-bao-lua-dao-dau-tu-chung-khoan-qua-cac-nhom-tren-mang-xa-hoi-d85574.html).
- *Ứng dụng hoặc đường dẫn do đối tượng cung cấp, nạp tiền vào tài khoản mang tên công ty hoặc quỹ* (cả hai nguồn nói chung về việc cài ứng dụng hoặc truy cập đường dẫn do đối tượng cung cấp). Riêng Tạp chí Kinh tế Tài chính nói UBCKNN xác định đơn vị đó **không được cấp phép**, và ứng dụng trong vụ đó **có trên App Store và Google Play**; vì vậy có mặt trên kho chính thức **không** chứng minh đơn vị hợp pháp.
- *Đóng băng tài khoản, rút tiền không được, bị xóa khỏi nhóm* (Tạp chí Kinh tế Tài chính). *Đòi nộp thêm phí hoặc thuế khi rút* (Nhà đầu tư, lời phát ngôn của Bộ Công an).
- *Giấy phép và con dấu giả, mạo danh sở giao dịch* (Viettimes, 03/07/2023): văn bản cấp phép quỹ giả và con dấu giả của Sở Giao dịch Hà Nội; HNX nói chỉ dùng một website chính thức. [Viettimes](https://viettimes.vn/canh-bao-gia-mao-ubcknn-so-gdck-ha-noi-de-lua-dao-nha-dau-tu-post168034.html). *Mạo danh tên công ty gần giống* (Doanh nghiệp & Hội nhập, 29/12/2023). [Doanh nghiệp & Hội nhập](https://doanhnghiephoinhap.vn/uy-ban-chung-khoan-canh-bao-gia-mao-lien-quan-chung-khoan-state-street-1616.html).

`SỰ_THẬT` (thứ cấp) Phát ngôn của Bộ Công an cho biết hầu hết nhóm có địa chỉ ngoài lãnh thổ Việt Nam nên khó truy tìm (nguồn Nhà đầu tư).

`SỰ_THẬT` (thứ cấp, Báo Pháp luật, 09/09/2026, trích Công an Hà Nội) Các cảnh báo năm 2026 gồm cả mạo danh cơ quan nhà nước, ngân hàng, và dùng công nghệ giả hình, giả giọng (deepfake, DeepVoice) để giả người quen hoặc lãnh đạo; mẫu hình rút nhỏ rồi nạp lớn vẫn còn. [Báo Pháp luật](https://doanhnhan.baophapluat.vn/cong-an-ha-noi-canh-bao-nguoi-dan-canh-giac-truoc-25-kich-ban-lua-dao-tren-khong-gian-mang-nam-2026-7cc6172e.html). `SỰ_THẬT` FINRA (Hoa Kỳ, 29/04/2026) cũng nêu giọng nhân bản bằng AI và video deepfake giả lãnh đạo. Hệ quả: dấu hiệu "người lạ chủ động" không đủ; người giả quen cũng cần được kiểm.

`SỰ_THẬT` [Bộ Công an](https://mps.gov.vn/bai-viet/canh-bao-thu-doan-lua-dao-thong-qua-cac-hoi-nhom-nhom-chat-dau-tu-chung-khoan-d2-t38878) (04/05/2024) mô tả tài khoản lãi ảo, yêu cầu nộp thêm thuế hoặc phí để rút và khóa tài khoản. Nguồn này xác nhận mẫu chung, không xác nhận riêng vụ STICCAPITAL. `CHƯA_BIẾT` Trang gốc UBCKNN, Sở giao dịch và NHNN liên quan các vụ nói trên chưa mở được trong lượt soạn; số vụ, số tiền thiệt hại và mức độ phổ biến hiện nay chưa có số liệu chính thức được mở.

## 2. Dấu hiệu nguyên tắc

`SỰ_THẬT` FINRA (29/04/2026) liệt kê dấu hiệu lừa đảo mạo danh: tin nhắn không mong muốn, yêu cầu giữ bí mật, lợi nhuận cao bất thường, đòi phí "hành chính" hoặc "quản lý" để nhận tiền, tên miền nhái, và giọng nói do AI tạo ra; cách kiểm là tự tra thông tin liên hệ của cơ quan thay vì dùng liên hệ trong tin nhắn. [FINRA — Regulator imposter scams](https://www.finra.org/investors/insights/regulator-imposter-scams).

`SUY_LUẬN` Từ các nguồn trên và mục 1, danh sách tự kiểm sau là của giáo trình (không phải của một cơ quan). Một dấu hiệu nặng, như bị đòi chuyển tiền cho cá nhân hoặc đòi đọc mã xác thực, đã đủ để dừng lại; không cần chờ tới hai dấu hiệu.

1. Bên tiếp cận chủ động mời, hay nói "chỉ bạn mới có suất". Người giả quen hoặc giả cơ quan cũng nằm ở đây.
2. Hứa lãi chắc chắn, "0 rủi ro", hoặc giá thấp hơn thị trường một cách khó giải thích.
3. Có hạn chót ngắn hoặc số suất giới hạn.
4. Yêu cầu chuyển tiền vào tài khoản của cá nhân hoặc một công ty không nằm trong danh sách đơn vị được cấp phép.
5. Gửi ứng dụng hoặc đường dẫn riêng (kể cả ứng dụng có trên kho chính thức), hoặc xin cài ứng dụng điều khiển từ xa.
6. Rút nhỏ thành công, rồi bị đòi thêm phí hoặc thuế khi rút số lớn.
7. Yêu cầu giữ bí mật, hoặc đòi OTP, mật khẩu.
8. Tự xưng cơ quan nhà nước, ngân hàng hay người thân gọi video và yêu cầu chuyển tiền gấp.

Quy tắc cho nhóm mạo danh: **cúp máy, tự tra số hoặc kênh chính thức rồi gọi lại; không đọc OTP; không cài ứng dụng điều khiển từ xa**.

## 3. Kiểm tra tư cách đơn vị trước khi chuyển tiền

`CHƯA_BIẾT` Địa chỉ danh sách giấy phép hiện hành của UBCKNN cho công ty chứng khoán và quản lý quỹ chưa được xác nhận trực tiếp. Khi cần kiểm một đơn vị cụ thể, hãy tự tìm kênh liên hệ chính thức của cơ quan quản lý và yêu cầu kiểm tra tên pháp nhân, giấy phép và phạm vi hoạt động; không dùng đường dẫn hoặc số điện thoại do người lạ gửi.

`SỰ_THẬT` [VNX — Danh sách thành viên](https://www.vnx.vn/vi/danh-sach-thanh-vien) cho tra cứu tên, mã và thị trường của thành viên giao dịch. Đây là một điểm đối chiếu bổ sung, không phải danh sách đầy đủ giấy phép của UBCKNN: vắng tên trong danh sách thành viên không tự chứng minh một tổ chức không được cấp phép, và có tên cũng không loại trừ mạo danh. Trang không nêu ngày chốt dữ liệu; cần kiểm với cơ quan có thẩm quyền và kênh chính thức của đơn vị.

Giới hạn của việc kiểm này: (1) danh sách thành viên VNX không xác nhận giấy phép cho quỹ, tiền mã hóa, ngoại hối hay "sàn" khác; (2) một đơn vị có tên trong danh sách **vẫn có thể bị mạo danh** (website nhái, nhân viên giả) nên phải gọi lại qua kênh chính thức bạn tự tìm; (3) tên nhái thường chỉ khác một chữ.

`CHƯA_BIẾT` Phạm vi và hiệu lực hiện hành của Điều 91 Luật Chứng khoán về nhận định hoặc bảo đảm lợi nhuận chưa được đối chiếu văn bản gốc sau sửa đổi. Dù chưa kết luận pháp lý, lời cam kết lãi chắc chắn là dấu hiệu cần dừng lại để kiểm chứng (xem cảnh báo FINRA ở mục 2).

`CHƯA_BIẾT` Số công ty chứng khoán được cấp phép hiện hành và mức phạt đối với kinh doanh hay nhận ủy thác trái phép chưa được mở.

## 4. Bảo mật tài khoản cơ bản

`SỰ_THẬT` (thứ cấp) NHNN khuyến nghị không cung cấp mật khẩu, OTP, số thẻ, CVV hay dữ liệu sinh trắc học cho bất kỳ ai; không mở liên kết hoặc quét mã QR lạ, không cài ứng dụng không rõ nguồn; xác minh qua website, ứng dụng hoặc hotline chính thức của ngân hàng; bật cảnh báo biến động số dư và đặt hạn mức chuyển khoản. [Báo Pháp luật](https://doanhnhan.baophapluat.vn/ngan-hang-nha-nuoc-khuyen-cao-nguoi-dan-canh-giac-truoc-cac-hinh-thuc-lua-dao-trong-linh-vuc-ngan-hang-86489.html) (bài ghi ngày 10/09/2025; ngày đăng chưa xác nhận độc lập). Đây là khuyến cáo cho khách hàng ngân hàng, chưa phải quy định riêng cho tài khoản chứng khoán. Cách đặt hạn mức làm theo hướng dẫn chính thức của ngân hàng bạn.

`SỰ_THẬT` NCSC (Anh) nêu xác minh hai bước giúp kẻ gian khó vào dù đã biết mật khẩu; nên bật cho email vì ai kiểm soát email có thể đặt lại mật khẩu các tài khoản khác; ứng dụng xác thực không cần sóng điện thoại; mã dự phòng dùng một lần phải cất kỹ. [NCSC — 2SV](https://www.ncsc.gov.uk/guidance/setting-2-step-verification-2sv). Hướng dẫn cho cá nhân tại Anh, là chuẩn tham chiếu quốc tế; hệ thống ở Việt Nam (smart OTP, sinh trắc học) có thể khác, nên hãy theo hướng dẫn chính thức của công ty chứng khoán và ngân hàng bạn dùng. NCSC cũng nói SMS phổ biến nhưng không phải cách an toàn nhất.

`SUY_LUẬN` Bốn thói quen tối thiểu: mật khẩu riêng cho email và tài khoản đầu tư; bật xác minh hai bước cho email trước; không bao giờ chia sẻ OTP; chỉ cài ứng dụng do chính công ty chứng khoán hướng dẫn trên kênh bạn tự tìm, và nhớ rằng ứng dụng có trên kho chính thức chưa chắc hợp pháp.

`CHƯA_BIẾT` Quy định Việt Nam về xác thực cho giao dịch chứng khoán và hướng dẫn riêng của từng công ty chưa được mở; SIM swap và xác thực chống lừa đảo (FIDO) chưa có nguồn cơ quan đã mở, nên chưa dạy chi tiết. `SUY_LUẬN` Nếu điện thoại bỗng mất sóng không rõ lý do, hoặc bạn nhận thông báo đổi thiết bị mà mình không làm, hãy gọi nhà mạng và ngân hàng qua kênh bạn tự tìm. Cẩn trọng với người tự xưng nhân viên ngân hàng "hỗ trợ đăng ký sinh trắc học".

## 5. Ví dụ: một tin nhắn mời, nhiều dấu hiệu

`KỊCH_BẢN` (hoàn toàn hư cấu; tên, công ty và số liệu đều không có thật) Anh Minh, 29 tuổi, có 80.000.000 đồng tiết kiệm. Một tài khoản Zalo tự xưng chuyên viên chứng khoán mời anh vào nhóm "Đầu tư thông minh 0 rủi ro" có 400 thành viên, nói còn 3 suất cổ phiếu giá thấp hơn thị trường 20%, đóng đăng ký trong 48 giờ. Thành viên đăng ảnh chụp màn hình lãi. Anh được gửi đường dẫn tải ứng dụng riêng và số tài khoản của "Công ty TNHH Đầu tư ABC" để nạp 20.000.000 đồng. Ứng dụng hiện số dư 26.000.000 đồng sau 2 ngày; anh rút thử 2.000.000 đồng thành công, rồi nạp thêm 60.000.000 đồng. Khi anh rút 50.000.000 đồng, ứng dụng báo lỗi và đòi nộp phí thuế 10%; người mời nhắn "đừng nói với ai, không sẽ mất suất".

`PHÉP_TÍNH` Số dư hiển thị so với số nạp đầu: `(26.000.000 − 20.000.000) ÷ 20.000.000 = 30%`, một mức "lãi" cao bất thường chỉ sau 2 ngày. Tổng đã nạp: `20.000.000 + 60.000.000 = 80.000.000` đồng. Đã rút về: 2.000.000 đồng. Phí được đòi: `10% × 50.000.000 = 5.000.000` đồng (khoản này nằm ngoài 80 triệu tiết kiệm; giả định anh lấy từ nguồn khác). Nếu anh chuyển cả khoản này thì tổng tiền đã chuyển đi là `80.000.000 + 5.000.000 = 85.000.000` đồng, tiền nhận lại thực tế 2.000.000 đồng. Số dư hiển thị và "lãi" trên ứng dụng chỉ là số hiển thị, không có giá trị nếu không rút được thật.

Điểm dừng: liệt kê các dấu hiệu theo mục 2 bạn thấy trong tình huống, rồi so với đáp án.

## 6. Nếu nghi đã bị lừa: việc cần làm trước

Bài này chỉ là gợi ý nguyên tắc, không thay thế tư vấn pháp lý hay hướng dẫn của cơ quan chức năng.

`SỰ_THẬT` Bộ Công an khuyến nghị báo ngay công an gần nhất; NHNN khuyến nghị gọi hotline ngân hàng và công an khi nghi ngờ theo nguồn báo chí. `SỰ_THẬT` FINRA mô tả lừa đảo "thu hồi tiền" (recovery scam): thường bắt đầu bằng lời đề nghị giúp lấy lại tiền đã mất và có thể dẫn tới thiệt hại lớn hơn; FINRA mô tả riêng lừa đảo đòi phí trả trước (advance-fee). [FINRA](https://www.finra.org/investors/insights/regulator-imposter-scams). `SUY_LUẬN` Hãy cảnh giác với lời đề nghị thu hồi tiền không mời mà đến, kể cả khi chưa đòi phí; tự tìm và xác minh kênh ngân hàng, công an hoặc người hỗ trợ trước khi liên hệ, không đưa thông tin xác thực cho bên chưa kiểm chứng.

`SUY_LUẬN` Thứ tự gợi ý, với **thời gian là yếu tố quan trọng**:

1. Ngừng chuyển thêm tiền, kể cả "phí rút" hay "thuế".
2. Gọi ngay hotline ngân hàng đã chuyển tiền, càng sớm càng tốt, để đề nghị hỗ trợ tra soát. Phong tỏa tài khoản nhận tiền thường là quyền của cơ quan có thẩm quyền; kết quả không được bảo đảm (`CHƯA_BIẾT` thời hạn và thủ tục của ngân hàng).
3. Giữ bằng chứng: tin nhắn, mã giao dịch, số tài khoản nhận, ảnh màn hình và thông tin ứng dụng. Nếu làm được an toàn, lưu ảnh màn hình và tên ứng dụng trước khi gỡ; không tiếp tục tương tác với đối tượng. [FBI/IC3](https://www.ic3.gov/PSA/2026/PSA260615) gợi ý cung cấp ảnh tin nhắn và thông tin ứng dụng khi báo cáo tại Hoa Kỳ; thứ tự lưu trước khi gỡ là gợi ý của giáo trình, không phải yêu cầu pháp lý Việt Nam.
4. Báo công an gần nhất.
5. Nếu lộ thông tin tài khoản đầu tư thật, dùng thiết bị tin cậy để báo ngân hàng và công ty chứng khoán, đổi mật khẩu và yêu cầu hỗ trợ bảo vệ tài khoản. Nếu đã cài phần mềm đáng ngờ, chỉ gỡ ứng dụng có thể chưa đủ: [NCSC — Xóa thiết bị](https://www.ncsc.gov.uk/collection/device-security-guidance/managing-deployed-devices/erasing-devices) lưu ý ứng dụng bị gỡ hoặc quét bảo mật chưa chắc loại hết mã độc. NCSC khuyên quét toàn bộ bằng phần mềm bảo mật nếu có và xử lý các vấn đề phát hiện được; theo hướng dẫn chính thức của nhà cung cấp hoặc chuyên gia tin cậy để kiểm tra thiết bị. [NCSC — Phishing](https://www.ncsc.gov.uk/section/respond-recover/phishing). Đây là hướng dẫn tham khảo của Anh.
6. Cảnh giác với người tự xưng giúp lấy lại tiền hoặc "dịch vụ thu hồi" trên mạng: nạn nhân có thể bị nhắm mục tiêu lần nữa.

`CHƯA_BIẾT` Khả năng thu hồi tiền: không có số liệu thu hồi nào được mở, nên không khẳng định có thể hay không thể lấy lại. Kênh báo cáo trực tuyến chính thức và thời hạn tra soát của ngân hàng chưa được mở.

## Năm câu hỏi khi đọc

1. Ai chủ động liên lạc trước, và tôi có tự kiểm chứng họ qua kênh tôi tự tìm không?
2. Tiền sẽ vào tài khoản của ai, và tên đó có trong danh sách đơn vị được cấp phép tôi tự tra không?
3. Họ có hứa lợi nhuận chắc chắn, hù dọa, hay giục tôi quyết nhanh không?
4. Tôi có đang chia sẻ OTP, cài ứng dụng riêng hay ứng dụng điều khiển từ xa không?
5. Nguồn của cảnh báo này là cơ quan gốc hay bài đăng lại, và còn hiệu lực không?

## Bài tập — làm trước khi mở đáp án

Câu 1–3 là phần cốt lõi; câu 4–7 là luyện thêm.

1. Trong tình huống anh Minh, nêu ít nhất năm dấu hiệu cảnh báo.
2. Tính tổng tiền anh Minh đã chuyển đi và tiền thực nhận về nếu anh nộp thêm khoản phí được đòi.
3. Bạn kiểm tra một công ty có được cấp phép ở đâu, và vì sao không dùng đường dẫn do người lạ gửi? Việc có tên trong danh sách có đủ để an tâm không?
4. Vì sao "rút thử thành công" không chứng minh đơn vị là hợp pháp?
5. Vì sao nên bật xác minh hai bước cho email trước tiên?
6. Một người nhắn rằng họ có thể "lấy lại tiền đã mất" cho bạn. Theo FINRA, đây là dấu hiệu gì, và có cần họ đòi phí thì mới đáng ngờ không?
7. Một cuộc gọi video từ "người thân" xin chuyển tiền gấp. Nêu quy tắc bạn làm theo.

## Đáp án và điều cần hiểu

<details>
<summary>Mở sau khi tự làm</summary>

1. Người lạ chủ động mời; "0 rủi ro" và giá thấp hơn thị trường; áp lực 48 giờ và 3 suất; ứng dụng và đường dẫn riêng (kể cả có trên kho chính thức cũng không đủ chứng minh); nạp vào tài khoản công ty không rõ giấy phép; rút nhỏ để tạo tin; đòi phí thuế khi rút lớn; yêu cầu giữ bí mật.
2. `PHÉP_TÍNH` Đã chuyển `20.000.000 + 60.000.000 + 5.000.000 = 85.000.000` đồng; nhận về 2.000.000 đồng. Số dư hiển thị không phải tiền đã nhận.
3. Tự tìm kênh chính thức của cơ quan quản lý để kiểm tra giấy phép và phạm vi hoạt động; bài chưa xác nhận được địa chỉ danh sách giấy phép hiện hành. Danh sách thành viên VNX có thể đối chiếu thêm nhưng không thay giấy phép; đường dẫn người lạ gửi có thể là trang giả. Có tên trong danh sách vẫn chưa đủ: tên có thể bị mạo danh, nên phải gọi lại qua kênh tự tìm.
4. Rút nhỏ là công cụ tạo niềm tin trong mẫu hình lừa đảo mô tả ở mục 1; hợp pháp phải kiểm bằng giấy phép tra từ nguồn độc lập.
5. Ai kiểm soát email có thể đặt lại mật khẩu các tài khoản khác (NCSC).
6. Đó có thể là mẫu hình lừa đảo thu hồi tiền (recovery scam); FINRA cảnh báo nó có thể dẫn tới thiệt hại lớn hơn. Cần cảnh giác với lời đề nghị không mời mà đến, kể cả khi chưa đòi phí; đòi phí trả trước là một dấu hiệu riêng. Tự tìm và kiểm chứng kênh hỗ trợ.
7. Cúp máy, tự tra số hoặc kênh chính thức của người thân và gọi lại; không chuyển tiền, không đọc OTP; nghi giả giọng hoặc giả mặt là có thật.

</details>

## Lỗi thường gặp

- Tin ảnh chụp lãi của thành viên nhóm là bằng chứng.
- Cho rằng ứng dụng có trên kho chính thức thì đơn vị hợp pháp.
- Chỉ nhìn tên có chữ "chứng khoán" hay logo mà không tra danh sách, hoặc tra rồi không gọi lại qua kênh tự tìm.
- Cho rằng có OTP là đủ rồi đọc OTP cho người tự xưng nhân viên.
- Dùng cùng một mật khẩu cho email và tài khoản đầu tư.
- Chuyển thêm "phí" hay tin người tự giúp lấy lại tiền; hoặc tự trách mình mà không báo kịp thời.

## Ranh giới an toàn

- Đây là bài học bảo vệ bản thân, không phải khuyến nghị mua/bán/nắm giữ hay hướng dẫn đầu tư, và không thay thế tư vấn pháp lý.
- Tình huống anh Minh và mọi con số trong đó là `KỊCH_BẢN` hư cấu.
- Không nhập thông tin đăng nhập, OTP hay dữ liệu cá nhân vào trang bạn không tự xác minh.
- Bài không cam kết khả năng thu hồi tiền.

## Điều tôi vẫn chưa hiểu

- Công ty chứng khoán tôi định dùng được cấp phép ở đâu, tên chính xác là gì?
- Công ty đó yêu cầu xác thực nào khi đăng nhập và rút tiền?
- Kênh báo cáo chính thức nào tôi sẽ dùng nếu nghi bị lừa, và ngân hàng của tôi tra soát trong bao lâu?

## Nguồn Internet đã mở

Ngày truy cập tất cả nguồn: `2026-10-27`. Ngày dưới là ngày đăng của bài, không phải ngày truy cập.

| Nguồn | Ngày đăng / phạm vi | Dùng cho |
|---|---|---|
| [Tạp chí Kinh tế Tài chính](https://tapchikinhtetaichinh.vn/uy-ban-chung-khoan-nha-nuoc-canh-bao-lua-dao-lien-quan-cong-ty-sticcapital-69448.html) | 07/10/2025; Việt Nam; thứ cấp | Nhóm chat, livestream, tài khoản công ty, đóng băng; báo dẫn UBCKNN nói không cấp phép; ứng dụng có trên kho chính thức |
| [FBI/IC3](https://www.ic3.gov/PSA/2026/PSA260615) | 15/06/2026; Hoa Kỳ | Thông tin ứng dụng và ảnh tin nhắn để báo cáo lừa đảo |
| [Bộ Công an](https://mps.gov.vn/bai-viet/canh-bao-thu-doan-lua-dao-thong-qua-cac-hoi-nhom-nhom-chat-dau-tu-chung-khoan-d2-t38878) | 04/05/2024; Việt Nam | Mẫu lừa đảo chung qua nhóm chat và báo công an |
| [Nhà đầu tư](https://nhadautu.vn/bo-cong-an-canh-bao-lua-dao-dau-tu-chung-khoan-qua-cac-nhom-tren-mang-xa-hoi-d85574.html) | 04/05/2024; Việt Nam; thứ cấp | Phát ngôn Bộ Công an, phí/thuế, báo công an |
| [Viettimes](https://viettimes.vn/canh-bao-gia-mao-ubcknn-so-gdck-ha-noi-de-lua-dao-nha-dau-tu-post168034.html) | 03/07/2023; Việt Nam; thứ cấp | Giấy phép quỹ giả, mạo danh sở giao dịch |
| [Doanh nghiệp & Hội nhập](https://doanhnghiephoinhap.vn/uy-ban-chung-khoan-canh-bao-gia-mao-lien-quan-chung-khoan-state-street-1616.html) | 29/12/2023; Việt Nam; thứ cấp | Mạo danh tên công ty; danh sách trên ssc.gov.vn |
| [Báo Pháp luật — Công an Hà Nội](https://doanhnhan.baophapluat.vn/cong-an-ha-noi-canh-bao-nguoi-dan-canh-giac-truoc-25-kich-ban-lua-dao-tren-khong-gian-mang-nam-2026-7cc6172e.html) | 09/09/2026; Việt Nam; thứ cấp | Mạo danh cơ quan, deepfake, rút nhỏ nạp lớn |
| [Báo Pháp luật — khuyến cáo NHNN](https://doanhnhan.baophapluat.vn/ngan-hang-nha-nuoc-khuyen-cao-nguoi-dan-canh-giac-truoc-cac-hinh-thuc-lua-dao-trong-linh-vuc-ngan-hang-86489.html) | Ghi 10/09/2025, chưa xác nhận độc lập; Việt Nam; thứ cấp | Bảo mật cơ bản, gọi hotline |
| [NCSC — 2SV](https://www.ncsc.gov.uk/guidance/setting-2-step-verification-2sv) | Xuất bản 07/08/2018, rà soát 10/01/2022, phiên bản 1.0; Anh | Xác minh hai bước |
| [NCSC — Phishing](https://www.ncsc.gov.uk/section/respond-recover/phishing) | Không thấy ngày đăng; Anh | Xử lý khi đã cài phần mềm đáng ngờ hoặc lộ thông tin |
| [NCSC — Xóa thiết bị](https://www.ncsc.gov.uk/collection/device-security-guidance/managing-deployed-devices/erasing-devices) | Rà soát 13/05/2025; Anh; hướng dẫn cho tổ chức | Giới hạn của việc chỉ gỡ ứng dụng hoặc quét bảo mật |
| [VNX — Danh sách thành viên](https://www.vnx.vn/vi/danh-sach-thanh-vien) | Trang không nêu ngày chốt dữ liệu; Việt Nam | Kiểm tra bổ sung tư cách thành viên giao dịch, không thay danh sách giấy phép |
| [FINRA — Regulator imposter scams](https://www.finra.org/investors/insights/regulator-imposter-scams) | 29/04/2026; Hoa Kỳ | Dấu hiệu, AI, recovery scam |

Không dùng trong bài: Investor.gov, SEC, ASIC, FCA, ssc.gov.vn và thuvienphapluat.vn không mở được trong lượt thu thập (lỗi truy cập), nên chưa được trích dẫn là đã kiểm. Biên bản của bản trước (kiểm nguồn `ĐẠT`; phản biện `ĐẠT` có điều kiện) đã được xử lý trong bản này; cần kiểm lại phần đã đổi. `CHƯA_BIẾT` hiệu quả học thực tế.
