# BẢN NHÁP - CHƯA KIỂM DUYỆT: Review bài học và kế hoạch bổ sung

- Ngày: `2026-10-26`
- Chốt dữ liệu lúc: `2026-10-26 16:42 UTC+7 (Asia/Ho_Chi_Minh)`
- Trạng thái: Đề xuất để triển khai; chưa thử nghiệm với người học; không chứng nhận độ chính xác của toàn bộ bài học.
- Người tổng hợp và ghi duy nhất: `research_coordinator`.
- Phạm vi: 11 bài trong `learning/lessons/`, README học tập, lộ trình, bảng thuật ngữ, mẫu bài học và hướng dẫn khởi động tại thời điểm đọc.
- Đối tượng giả định: Người mới, muốn hiểu doanh nghiệp và có thể tiến tới tự nghiên cứu cổ phiếu trên phạm vi toàn cầu.
- Kiểm nguồn: `ĐẠT` trong phạm vi bản kế hoạch; source_fact_checker tái kiểm bản chốt 16:42, mã băm canonical 448c8c449f4fd50d9bd15f140840d1aebca74dc7f2e0e0cfd8a9506d1f0b61d6; 0 lỗi nghiêm trọng. Không kiểm lại toàn bộ 11 bài; biên bản trả trong cuộc trò chuyện.
- Phản biện rủi ro: `ĐẠT` trong phạm vi bản kế hoạch; risk_bear_reviewer tái kiểm cùng bản chốt 16:42 và cùng mã băm; 0 lỗi nghiêm trọng. Không chứng nhận hiệu quả học thực tế; biên bản trả trong cuộc trò chuyện.

## 1. Kết luận review

`Ý_KIẾN` Bộ bài có khung tư duy tốt và đủ chiều sâu để tiếp tục phát triển. Tuy nhiên, chưa phải một giáo trình thuận tiện để người hoàn toàn mới tự học từ đầu tới cuối.

| Tiêu chí | Đánh giá | Cơ sở quan sát |
|---|---|---|
| Logic tổng thể | Khá | Từ báo cáo → chất lượng doanh nghiệp → tiền → nợ → quản trị → định giá; nhưng các bài nền bổ sung chưa đồng bộ phụ thuộc |
| Dễ hiểu trong từng đoạn | Khá, không đồng đều | Có trực giác, ví dụ số, phản ví dụ; một số bài chứa nhiều tầng thuật ngữ và ngoại lệ chuẩn mực |
| Dễ tự học cả bộ | Cần cải thiện | Chưa thống nhất đường học, phần bắt buộc/đọc thêm và cách biết mình đã đủ hiểu để chuyển bài |
| Độ chính xác toàn bộ | CHƯA_BIẾT trong lượt này | Đây là review thiết kế học tập; không kiểm lại tất cả số liệu doanh nghiệp, văn bản và phép tính của 11 bài |

`SỰ_THẬT — quan sát tệp` Hiện có **11 bài đã soạn**: 001–009, N2, N3. Có **10 bài đã lên kế hoạch nhưng chưa soạn**: N1, N4, N5 và 010–016. Đếm theo tệp và trạng thái tại [README](README.md), [lộ trình §5](roadmap.md#5-bản-đồ-13-bài); “đã soạn” không đồng nghĩa “đã kiểm duyệt”.

Điểm nên giữ: câu hỏi cốt lõi; phần “Hiểu bài này trong 1 phút”; ví dụ từ trực giác sang công thức; đáp án có giải thích; câu hỏi yêu cầu tìm dữ liệu thiếu và phân biệt giả thuyết với kết luận. Các bài 004–009 đã có ôn bài cũ và bài tập tích lũy.

`SỰ_THẬT — nguồn trực tuyến` IES khuyến nghị ôn cách quãng, xen lời giải mẫu với bài tự giải và dùng câu hỏi giúp nhớ lại. AERO khuyến nghị chia kỹ năng phức tạp thành bước nhỏ, dạy theo kiến thức nền và giảm dần trợ giúp. Đây là cơ sở cho các đề xuất dưới đây, **không phải bằng chứng bộ bài này đã hiệu quả với người học Việt Nam cụ thể**. [IES](https://ies.ed.gov/ncee/wwc/PracticeGuide/1), [AERO](https://www.edresearch.edu.au/guides-resources/practice-guides/explicit-instruction-practice-guide-full-publication).

## 2. Các vấn đề cần xử lý theo thứ tự

Mức “cao/trung bình” dưới đây là `Ý_KIẾN` về tác động tới việc học, không phải kết luận sai chuẩn mực kế toán.

| Ưu tiên | Phát hiện và bằng chứng trong tệp | Cách xử lý dự kiến | Đóng việc khi |
|---|---|---|---|
| Cao | N3 được xếp ngay sau N2 nhưng phần ôn câu 3–4 hỏi IFRS 16 của 005 và FCFF của 004; bài tập 5 lại dùng FCFF. Xem [N3: phần ôn](lessons/N3-vietnam-vas-statements.md#ôn-bài-cũ-5-phút), phần 7 | Chia N3 thành **phần A** chỉ tìm tên chỉ tiêu, kỳ và mẫu báo cáo sau N2; **phần B** đối chiếu/điều chỉnh sau 009. Phần A bỏ mọi nội dung định giá, tỷ số hoặc điều chỉnh của các bài chưa học | Không còn câu bắt buộc dùng kiến thức chưa học; phần B có chỉ dẫn quay lại rõ ràng |
| Cao | README yêu cầu N1 đầu tiên; roadmap §17.3 lại để việc soạn N1 tới Giai đoạn C | Soạn N1 ở đợt đầu; phân biệt thứ tự soạn với thứ tự học; đưa một danh sách hiện trạng duy nhất lên đầu roadmap | README, roadmap và liên kết bài trước/sau thống nhất |
| Cao | Hướng dẫn khởi động yêu cầu mô hình kinh doanh, khách hàng, hiệu quả kinh tế một đơn vị; hiện chưa có một bài tập trung dạy chuỗi đó | Thêm N6, dùng một cửa hàng hư cấu trước khi đưa người học vào tỷ số tài chính | Người học giải thích được bán gì, cho ai, thu tiền thế nào và bán thêm có tạo lãi không |
| Trung bình | N2 gộp phương trình kế toán, bút toán, tầng lợi nhuận, sáu tỷ số và phân rã ROE; 003 gộp lợi thế cạnh tranh, ROIC, chi phí vốn, tái đầu tư, quản trị | Chia mỗi bài thành các phiên có điểm dừng; N2: sổ sách → tầng lợi nhuận → tỷ số; 003: lợi thế cạnh tranh → hiệu quả vốn → tái đầu tư | Mỗi phiên có một kết quả học chính và một câu tự làm; giữ mã bài và đường dẫn |
| Trung bình | Roadmap còn mở đầu bằng “ba bài đã có”; mục sửa bài cũ và lịch sử kiểm duyệt xen cùng kế hoạch hiện hành | Đưa hiện trạng và việc tiếp theo lên đầu; chuyển lịch sử xuống cuối; cập nhật số bài và phụ thuộc thực tế | Không dùng phần lịch sử để mô tả hiện trạng; dẫn chéo tới bài đã soạn chính xác |
| Trung bình | Mật độ nhãn, chuẩn mực, nguồn và số liệu thời sự làm thân bài nặng; điều này đã được review trước ở roadmap §17 | Giữ nhãn ở nhận định trọng yếu; đặt ngoại lệ và nguồn chi tiết ở phần đọc thêm; giữ khái niệm vĩ mô tách khỏi bảng số cập nhật | Phần chính vẫn đủ dữ kiện để hiểu ví dụ; bỏ phụ lục không làm đứt lập luận |
| Trung bình | Chưa có dữ liệu học thực tế; thời lượng ghi trong bài chỉ là dự kiến | Dùng ba phiên đầu để ghi phút thực tế, lỗi và câu chưa hiểu; điều chỉnh khối lượng từ kết quả đó | Có phản hồi thật trước khi chốt lịch dài hạn |

`SUY_LUẬN` N2 và N3 đã xử lý một phần khoảng trống được nêu trong roadmap §17; không tính chúng là bài mới cần viết lần nữa. Các phát hiện về độ dày và nhãn cũng là việc tồn đọng đã biết. Điểm cần bổ sung trong lượt này là phụ thuộc ngược của N3, cập nhật hiện trạng và các khoảng trống N6–N8.

`SỰ_THẬT — quan sát tệp` N3 tự ghi chưa mở được một số văn bản/phụ lục gốc; 009 tự ghi số liệu ví dụ còn dựa vào nguồn thứ cấp. Chúng là **hạng mục cần kiểm tiếp**, chưa phải bằng chứng các nội dung ấy sai. Không dùng lượt review này để công nhận các mã số biểu mẫu hay số liệu doanh nghiệp là đã xác minh lại.

## 3. Các bài còn thiếu: tiếp tục kế hoạch cũ

Toàn bộ bảng là `Ý_KIẾN` về thiết kế học tập. Giữ mã hiện có để bảo toàn liên kết.

| Bài | Nội dung nên soạn | Đầu ra người học | Ưu tiên |
|---|---|---|---|
| N1 | Sở hữu cổ phần; doanh nghiệp huy động vốn; thị trường sơ cấp/thứ cấp; giá và thanh khoản; ai có trách nhiệm công bố | Kể đúng tiền đi đâu khi mua cổ phiếu phát hành mới và khi mua lại từ người khác | Sớm nhất |
| N4 | Lãi kép, giá trị hiện tại/tương lai, lợi suất tổng cộng và lợi suất theo năm; tiền tệ và lạm phát | Tính một ví dụ đơn giản, giải thích vì sao thời điểm nhận tiền quan trọng | Trước 010 |
| N5 | Chia **A: khái niệm danh mục và quỹ**; **B: đo lợi suất, mốc so sánh, chi phí và tái cân bằng**; quỹ ETF là quỹ giao dịch trên sàn | Nhận ra tập trung rủi ro, hiểu đa dạng hóa không bảo đảm tránh lỗ khi toàn thị trường giảm; biết so kết quả với mốc phù hợp | A sau N1, tùy chọn với nhánh doanh nghiệp; B sau N4/N7 |
| 010 | Chi phí vốn; chi phí nợ và vốn chủ; WACC là chi phí vốn bình quân gia quyền; độ nhạy | Dựng được giả định, nêu giới hạn và kiểm tính nhất quán tiền tệ/dòng tiền | Sau N4, N7, 003, 008 |
| 011 | DCF là định giá bằng dòng tiền chiết khấu; định giá ngược từ giá để đọc giả định | Dựng mô hình nhỏ có kiểm tra chéo và giải thích giả định chi phối | Sau 004, 009, 010 |
| 012 | Ba kịch bản, biên an toàn, điều kiện bác bỏ; phí/thuế/thanh khoản | Viết được luận điểm có điều kiện; không biến xác suất chủ quan thành độ chính xác giả | Sau 011, N7, N5B |
| 013 | Ngân hàng và bảo hiểm là hai phần riêng; mỗi phần có mô hình kiếm tiền và bộ chỉ số phù hợp | Biết vì sao không bê nguyên bộ phân tích doanh nghiệp phi tài chính sang | Nhánh chuyên ngành |
| 014 | Cấu trúc ngành, công suất và chu kỳ vốn | Chọn nhóm so sánh và phân biệt hiệu quả bền vững với đỉnh chu kỳ | Trước bài tổng kết nếu ngành được chọn cần kiến thức này |
| 015 | Thiên kiến, bảng câu hỏi tự kiểm và nhật ký quyết định | Ghi dự đoán trước, đối chiếu sau; tách chất lượng quyết định khỏi may rủi kết quả | Thực hành nhẹ từ đầu, đào sâu sau 012 |
| 016 | Bài tổng kết nghiên cứu một doanh nghiệp thật | Hồ sơ nguồn, bảng số tái lập được, ba kịch bản, rủi ro và điều chưa biết | Sau phần nền và định giá; thêm 013/014 tùy doanh nghiệp |

`SỰ_THẬT — nguồn trực tuyến` Khung Investment Foundations của CFA Institute có các nhóm thị trường, định lượng, công cụ đầu tư, báo cáo tài chính, danh mục và đánh giá kết quả. Khung này dùng để đối chiếu độ bao phủ; không bắt buộc sao chép một khóa đào tạo nghề vào lộ trình này. [CFA Institute, tài liệu ©2024](https://store.cfainstitute.org/content/Investment-Foundations-Learning-Goals-and-Topics.pdf).

`SỰ_THẬT — nguồn trực tuyến` Investor.gov giải thích đa dạng hóa ở cả giữa và trong các nhóm tài sản; đồng thời lưu ý tác động của phí lên kết quả đầu tư. `Ý_KIẾN` Vì vậy nên đưa phần nhập môn N5 lên sớm, không đợi người học hoàn thành DCF. Nguồn thuộc Hoa Kỳ, chỉ tham chiếu khái niệm; không suy ra thuế/phí hay quy định Việt Nam. [Phân bổ và đa dạng hóa](https://www.investor.gov/introduction-investing/getting-started/asset-allocation), [Phí và chi phí, 23/07/2025](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/updated).

`SỰ_THẬT` Đa dạng hóa không bảo đảm danh mục tránh thua lỗ khi thị trường giảm. Đây là giới hạn phải dạy cùng lợi ích, không để tới phần đọc thêm. [Investor.gov — Diversify Your Investments](https://www.investor.gov/introduction-investing/investing-basics/save-and-invest/diversify-your-investments).

## 4. Ba bài mới đề xuất ngoài danh sách cũ

Mã N6–N8 là `Ý_KIẾN`, chưa phải bài đã soạn hoặc nội dung đã được duyệt.

| Mã | Câu hỏi chính | Nội dung giới hạn | Bài thực hành và tiêu chí hoàn thành | Đặt ở đâu |
|---|---|---|---|---|
| N6 — Doanh nghiệp kiếm tiền thế nào? | Ai trả tiền, trả vì điều gì, và mỗi đơn hàng còn lại bao nhiêu? | Khách hàng, sản phẩm, doanh thu theo giá × lượng, định phí/biến phí, phần còn lại mỗi đơn vị để bù định phí, điểm hòa vốn, thu tiền sớm/muộn | Một cửa hàng hư cấu: tăng doanh thu nhưng lợi nhuận/tiền có thể giảm; chỉ ra giả định giá và chi phí | Trước 001; có thể quay lại sau N2 |
| N7 — Đọc dữ liệu và bất định | Con số trung bình có đang đánh lừa mình không? | Phần trăm/điểm phần trăm, trung bình/trung vị, số danh nghĩa/thực; xác suất và giá trị kỳ vọng; tương quan khác quan hệ nhân quả; thiên lệch chọn mẫu | Sửa một bảng so sánh trộn kỳ/đơn vị; nêu vì sao xác suất gán cho kịch bản chưa được kiểm chứng | Sau N4, trước 010/012 và N5B |
| N8 — Từ câu hỏi tới bằng chứng | Tìm nguồn nào và biết mình đã đọc đúng hồ sơ bằng cách nào? | Trang quan hệ nhà đầu tư/cơ quan quản lý; kỳ, đơn vị, hợp nhất/riêng; công bố gốc/bản sửa; số liệu/diễn giải | Sau N2: lập một bảng nguồn nhỏ và đối chiếu hai tài liệu; nhận ra một lỗi đơn vị hoặc khác phạm vi | Trước khi tự đọc ví dụ báo cáo thật; quay lại ở 007/016 |

`SỰ_THẬT — nguồn trực tuyến` SBA trình bày phân tích hòa vốn dựa trên giá bán, biến phí và định phí. `Ý_KIẾN` Đây là điểm tựa phù hợp để N6 nối hoạt động bán hàng với con số lợi nhuận. Khi soạn phải mở lại nguồn và ghi giả định; không dùng công thức đơn sản phẩm để khái quát mọi ngành. [SBA](https://legacy.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs/break-even-point).

`Ý_KIẾN` Ngoài phần bắt buộc, có thể mở các chuyên đề: trái phiếu; bất động sản; thuế hoãn lại; tồn kho trong lạm phát; bán lẻ, phần mềm, sản xuất hoặc hàng hóa cơ bản. Bốn chủ đề đầu đã xuất hiện trong kế hoạch cũ. Chọn theo doanh nghiệp nghiên cứu, không biến tất cả thành điều kiện để bắt đầu bài tổng kết. Công cụ phái sinh và giao dịch ngắn hạn chưa cần ưu tiên cho mục tiêu hiện tại.

## 5. Kế hoạch triển khai theo đợt

Đây là **thứ tự biên soạn**, không phải thời khóa biểu học. Mọi thời lượng học và công sức soạn vẫn `CHƯA_BIẾT`; ba phiên đầu chỉ giúp ước lượng sơ bộ cho người học đang tham gia, không đủ chốt cho cả khóa hoặc mọi người học. Không có công việc chạy tự động hay lịch hẹn nào được tạo.

| Đợt | Công việc cụ thể | Sản phẩm | Điều kiện hoàn thành |
|---|---|---|---|
| 0 — Làm rõ đường học | Đồng bộ hiện trạng; tách N3A/B; chia phiên N2/003; đánh dấu nội dung cốt lõi/đọc thêm; sửa dẫn chéo | README và roadmap thống nhất; các bài bị ảnh hưởng có điểm vào/ra rõ | Không có phụ thuộc ngược ở phần bắt buộc; không còn việc đã xong bị ghi là chưa làm |
| 1 — Bổ sung nền | Soạn N1, N6, N8; dùng lại cửa hàng hư cấu xuyên N6/001/N2, mỗi bài ghi đủ đầu vào riêng | 3 bài + bộ bài tập ngắn + thuật ngữ | Người học tự giải được tình huống mới, biết dữ liệu cần tìm; bài không cần tra ví dụ cũ để hiểu số |
| 2 — Toán và danh mục | Soạn N4, N7, N5A/B | 3 bài với phần học theo nhánh; bài đo lợi suất và tác động chi phí | Có bài tự giải không nhìn mẫu; không hướng dẫn tỷ trọng cá nhân hóa; xác suất giả định có nhãn |
| 3 — Hoàn thiện định giá | Soạn 010 → 011 → 012; hoàn thiện bảng kiểm nợ/nguồn/giả định và bài ôn tích lũy đã hứa | 3 bài và mô hình nhỏ tái lập được | Đồng nhất kỳ, tiền tệ và dòng tiền; ba kịch bản; người học giải thích được biến chi phối kết quả |
| 4 — Vận dụng | Soạn 015 rồi 016 cho doanh nghiệp phi tài chính; 013/014 trước nếu chọn trường hợp cần chúng | Nhật ký, bài tổng kết, các nhánh chuyên ngành | Không buộc học hết mọi ngành; hồ sơ nguồn và phản chứng đầy đủ cho doanh nghiệp đã chọn |

`PHÉP_TÍNH` Phạm vi bài chưa soạn sau khi thêm ba đề xuất: **10 bài có trong kế hoạch cũ + 3 bài mới = 13 bài**. Tổng dự kiến là **11 bài đã có + 13 bài chưa soạn = 24 mã bài**. N3A/B và N5A/B là phần bên trong mã hiện có, không cộng thành bài mới; chuyên đề tùy chọn chưa tính vào tổng.

## 6. Thứ tự học đề xuất và hai nhánh kết thúc

`Ý_KIẾN` Nhánh học doanh nghiệp và phân tích cổ phiếu sau khi soạn xong:

1. N1 → N6 → 001 → N2 → N8 → N3A; N5A có thể đọc sớm sau N1 nhưng không là điều kiện chặn 001.
2. 002 → N4 → 003 → 004 → 005 → 006 → 007.
3. 008 → 009 → N3B → N7 → N5A (nếu chưa đọc) → N5B.
4. Nếu muốn nghiên cứu cổ phiếu riêng lẻ: 010 → 011 → 012 → 015 → 016; thêm 013/014 tùy trường hợp.
5. Nhánh ngắn cho danh mục/quỹ: **N1 → N5A → N4 → N7 → N5B → bài tổng kết về rủi ro, chi phí và mốc so sánh**. Ví dụ N7 ở nhánh này tự đủ dữ kiện, không đòi kiến thức kế toán. Các bài phân tích doanh nghiệp và định giá là lựa chọn.

Từ 003, chi phí vốn chỉ được dùng như **đầu vào giả định đã cho**; không yêu cầu tự ước tính trước khi học 010. Bài 009 giữ khung chọn nhóm so sánh cơ bản tại chỗ, không phụ thuộc ngầm vào 014. N8 được xếp trước phần đọc báo cáo thật tự làm; ví dụ mẫu do gia sư dẫn ở 001/N2 vẫn có thể đọc trước.

Ngay lúc này, khi các bài mới còn thiếu: **001 → N2 → 002 → 003–009 → N3**. N3 được lùi toàn bài tới sau 009 để không buộc người học tự đoán cần bỏ câu nào. Nếu cần mở báo cáo Việt Nam sớm, dùng phần tìm tên chỉ tiêu của N3 với gia sư hướng dẫn, chưa làm phần điều chỉnh hoặc bài tập. Đây là đường tạm, không phải trạng thái các bài đã được sửa.

## 7. Chuẩn “dễ học” để áp dụng khi triển khai

Các con số dưới đây là `Ý_KIẾN` để thử, không phải ngưỡng khoa học đã được xác nhận:

- Mỗi phiên có một mục tiêu chính; mở bằng tình huống đời thường, sau đó ví dụ mẫu, công thức, câu tự làm và phản ví dụ.
- Một bộ cốt lõi gồm 3 câu: giải thích bằng lời, tính và diễn giải, phát hiện lỗi hoặc nêu dữ liệu thiếu. Câu luyện thêm tách rõ; không bỏ những năng lực bắt buộc của bài.
- Đáp án đặt sau bài tự làm; giải thích từng bước và vì sao cách hiểu thường gặp sai. Bài kiểm chuyển giao dùng tình huống mới, không chép lại lời giải mẫu.
- Chuyển bài khi tự làm được phần cốt lõi và giải thích được kết quả. Chưa đạt thì quay lại đúng phần vướng rồi thử câu tương tự; không chỉ nhìn phần trăm câu đúng.
- Ôn lại ở phiên kế tiếp và sau một khoảng nghỉ; lịch cụ thể điều chỉnh theo lỗi thực tế, không coi một lịch cố định là công thức tối ưu.
- Giữ một ví dụ cửa hàng xuyên các bài nền, nhưng mỗi bài tự đủ dữ kiện. Thêm ví dụ doanh nghiệp thật thuộc nhiều thị trường khi đã đủ kỹ năng đọc nguồn.

## 8. Kiểm nguồn, phản biện và giới hạn

`Ý_KIẾN` Ưu tiên kiểm lại các bài nền có nhiều phạm vi áp dụng (N2/N3), sau đó những công thức/cảnh báo chi phối các bài tiếp theo. Khi sửa một bài phải xét lại liên kết vào/ra; kiểm trên đúng phiên bản nội dung sau sửa.

Mỗi bài triển khai: soạn nháp → cố định phiên bản → `source_fact_checker` và `risk_bear_reviewer` kiểm độc lập → xử lý bất đồng → kiểm lại phiên bản đổi → cập nhật trạng thái. Điều phối viên là người ghi duy nhất. Không gọi toàn bộ giáo trình “đã kiểm duyệt” từ một lượt review kế hoạch.

**Rủi ro của chính kế hoạch:** quá nhiều bài nền có thể trì hoãn thực hành; tách nhỏ có thể gây lặp; ví dụ quán cà phê không đại diện mọi ngành; thứ tự đề xuất có thể chưa hợp nền tảng của người học. Cách xử lý: cho phép bỏ qua bằng bài đầu vào; thực hành nhỏ ngay từ 001; dùng bảng phụ thuộc thay vì ép mọi người học toàn bộ; không khái quát ví dụ đơn giản sang ngân hàng/bảo hiểm.

**Điều chưa biết:** người học đã hiểu tới đâu; tốc độ đọc/tính; phần thích học nhất; mục tiêu cuối là hiểu kinh doanh, đọc cổ phiếu hay danh mục/quỹ. Ghi nền tảng và mục tiêu trước khi thử ba phiên ngắn, quan sát sản phẩm tự làm; tiếp tục hiệu chỉnh ở các khối sau, không khái quát vòng thử này cho mọi người học và không suy từ ngày tạo tệp.

**Điều kiện đổi kế hoạch:** nếu người học đã vững kế toán, dùng bài đầu vào để bỏ qua phần nền tương ứng; nếu chỉ muốn danh mục/quỹ, chuyển ưu tiên sang N5; nếu học một ngành cụ thể, chọn nhánh 013/014 hoặc chuyên đề phù hợp. Thay đổi văn bản pháp lý chỉ cập nhật bài liên quan, không mặc định phải viết lại toàn khóa.

## 9. Sổ nguồn trực tuyến mở trong lượt review

Truy cập ngày `2026-10-26`, trước thời điểm chốt; nội dung là giáo dục, không lấy dữ liệu thị trường hay áp dụng mức thuế/phí quốc gia cụ thể. Kỳ báo cáo/tiền tệ/đơn vị tài chính: không áp dụng cho các nhận định được sử dụng ở đây. Phiên bản tài liệu là trang/PDF tại URL lúc mở; không suy ngày crawler thành ngày xuất bản.

| Nguồn đã mở thực tế | Ngày xuất bản/phiên bản hiển thị | Phạm vi sử dụng và giới hạn |
|---|---|---|
| [IES — Organizing Instruction and Study](https://ies.ed.gov/ncee/wwc/PracticeGuide/1) | 09/2007 | Ôn cách quãng, lời giải mẫu và câu hỏi nhớ lại; không đo hiệu quả bộ bài này |
| [AERO — Explicit instruction](https://www.edresearch.edu.au/guides-resources/practice-guides/explicit-instruction-practice-guide-full-publication) | CHƯA_BIẾT ngày xuất bản từ nội dung mở | Chia bước, kiến thức nền, giảm dần trợ giúp; nguồn tổng hợp thực hành giáo dục |
| [CFA — Learning Goals and Topics](https://store.cfainstitute.org/content/Investment-Foundations-Learning-Goals-and-Topics.pdf) | ©2024, PDF 3 trang; chưa thấy số sửa đổi | Đối chiếu nhóm nội dung; không khẳng định là khung duy nhất/phiên bản mới nhất |
| [SBA — Break-even point](https://legacy.sba.gov/business-guide/plan-your-business/calculate-your-startup-costs/break-even-point) | CHƯA_BIẾT ngày xuất bản từ nội dung mở | Cơ sở giới hạn cho N6; không phải công thức cho mọi mô hình kinh doanh |
| [Investor.gov — Asset Allocation and Diversification](https://www.investor.gov/introduction-investing/getting-started/asset-allocation) | CHƯA_BIẾT ngày xuất bản từ nội dung mở | Tham chiếu khái niệm danh mục; nguồn của SEC Hoa Kỳ |
| [Investor.gov — Fees and Expenses](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/updated) | 23/07/2025 | Phí ảnh hưởng kết quả; không lấy mức phí mẫu làm mức thực tế ở Việt Nam |
| [Investor.gov — Diversify Your Investments](https://www.investor.gov/introduction-investing/investing-basics/save-and-invest/diversify-your-investments) | CHƯA_BIẾT ngày xuất bản từ nội dung mở | Phản chứng: đa dạng hóa không bảo đảm tránh lỗ khi thị trường giảm |

Giới hạn bằng chứng: IES và AERO là hai tổ chức độc lập hỗ trợ hướng thiết kế; đây vẫn là suy luận khi áp dụng cho giáo trình tài chính tự học này. Investor.gov thuộc SEC, không được đếm là một cơ quan độc lập với SEC. CFA là một nguồn gốc duy nhất cho nội dung của chính khung CFA, không phải hai nguồn kiểm chứng.

## 10. Nhật ký review bản kế hoạch

- Đã nhận nhánh `business_tutor`: review cách dạy trên 11 bài; đề nghị ưu tiên N1, chia N2/003 và tách phần luyện thêm; chưa quan sát người học thực tế.
- Hai nhánh đã đọc độc lập bản nháp đầu, mã băm bắt đầu `a8e533fe`. Đã sửa N3B về sau 009, bỏ yêu cầu N5A trước 001, thêm nhánh ngắn danh mục/quỹ và giới hạn vòng thử ba phiên; bản sửa cần tái kiểm cùng phiên bản. Kết quả chỉ áp dụng review kế hoạch, không bao trùm mọi nguồn của 11 bài.
- Bất đồng metadata còn công khai: nhánh kiểm nguồn thấy ngày xuất bản/cập nhật của AERO trong bản trích; điều phối viên không thấy các trường ấy trong bản trích hoặc HTML trực tiếp của cùng URL. Giữ ngày xuất bản `CHƯA_BIẾT`, không dùng ngày này để lập luận; nội dung khuyến nghị trên trang đã được đối chiếu.
- Tài liệu giữ nhãn bản nháp; kết quả trao đổi và những chỉnh sửa sau kiểm không tự tạo chứng nhận xuất bản cho toàn bộ giáo trình.


## 11. Nhật ký triển khai sau yêu cầu “làm đi”

- Ngày triển khai: `2026-10-26`. Các mục0–10 phía trên là bản kế hoạch đã được review, giữ lại làm lịch sử; con số11 đã có/13 chưa soạn ở đó không còn mô tả hiện trạng.
- **Đã soạn đủ13 bài còn thiếu**, thành24 mã bài hiện có. Xem [mục lục hiện hành](README.md), không dùng thứ tự soạn để suy thứ tự học.
- Đợt0: đồng bộ mục lục/lộ trình/hướng dẫn bắt đầu; chia phiên N2/003 và004–009; tách N3A/B, phần B sau009; ẩn đáp án tự kiểm phần A; bảng số vĩ mô tách ra lịch sử và mẫu cập nhật.
- Đợt1: đã soạn N1,N6,N8.
- Đợt2: đã soạn N4,N7,N5A/B, gồm tái cân bằng và bài tổng kết riêng nhánh quỹ.
- Đợt3: đã soạn010–012, có mô hình DCF nhỏ, kịch bản, chi phí và điều kiện bác bỏ.
- Đợt4: đã soạn013–016; ngân hàng/bảo hiểm là hai phần riêng; bài tổng kết dùng số Apple lịch sử và kịch bản hư cấu riêng, không tuyên bố đã định giá Apple.
- Sản phẩm thực hành: [bảng nguồn, nợ, DCF, hai bài ôn, bảng kiểm20câu và quản trị12điểm](practice/research-and-model-worksheets.md); bảng thuật ngữ đã bổ sung.
- **13 bài mới đã được hai nhánh kiểm độc lập**, xử lý lỗi rồi xác nhận lại phiên bản; đã lưu26biên bản và đối chiếu bằng cổng cấu trúc. [Sổ kiểm duyệt](reviews/README.md) ghi đúng phạm vi và giới hạn.
- Chưa thử nghiệm với người học; chưa có dữ liệu ba phiên thực tế. Không tuyên bố toàn bộ11bài cũ đã được tái kiểm mọi dữ kiện; các giới hạn nguồn cũ vẫn còn.
- Không tạo lịch tự động, không đặt lệnh, không truy cập tài khoản và không đưa khuyến nghị tài chính cá nhân.
