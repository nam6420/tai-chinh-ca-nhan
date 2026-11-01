# Bài 008: Vĩ mô truyền dẫn vào doanh thu, chi phí và dòng tiền

- Ngày: `2026-10-26`
- Chốt dữ liệu lúc: `2026-10-26 12:08 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Chỉ ra được bốn kênh truyền dẫn từ số liệu vĩ mô vào báo cáo tài chính; tính được tác động của nén biên do giá đầu vào tăng nhanh hơn giá bán; tính được tác động của lãi suất thả nổi lên lãi vay; phân biệt được **chỉ số giá** với **mức tỷ giá**; đọc đúng một bảng số vĩ mô (kỳ dữ liệu, so sánh cùng kỳ hay so với đầu năm, đơn vị).
- Thời lượng: 35 phút đọc + 40 phút bài tập (2 phiên)
- Bài trước liên quan: [Bài 003](003-business-quality-moat-and-roic.md) (moat, pricing power), [Bài 005](005-debt-liquidity-survival.md) (lãi vay)
- Câu hỏi cốt lõi: **Lãi suất, lạm phát, tỷ giá và chu kỳ đi vào báo cáo tài chính qua đường nào?**

> Đây là bài học nền tảng toàn cầu, không phải khuyến nghị mua, bán hay nắm giữ chứng khoán. Số liệu dùng trong bài là số liệu thật, đã mở trang gốc ngày `2026-10-26`; khi bạn đọc lại bài này vào lúc khác, **phải cập nhật số** — xem mục 13.

## Hiểu bài này trong 1 phút

`SUY_LUẬN` Cùng một tin "lạm phát 5%" có thể là tin tốt với doanh nghiệp này và tin xấu với doanh nghiệp khác. Với doanh nghiệp bán được giá cao hơn (thương hiệu mạnh, sản phẩm khó thay thế), lạm phát là chuyện chuyển chi phí sang khách. Với doanh nghiệp bán hàng hoá giống hệt đối thủ, lạm phát là chuyện **biên lợi nhuận bị bào mòn** vì chi phí đầu vào lên mà giá bán không lên theo.

Vì vậy học vĩ mô không phải học thuộc con số. Học vĩ mô là học **đường đi**: từ một chỉ tiêu trên bản tin đến dòng nào trong báo cáo tài chính, mất bao lâu, và ai hấp thụ khoản chênh lệch.

> Câu cần nhớ: **Vĩ mô không phải bối cảnh; vĩ mô là một chuỗi phép tính từ giá đầu vào đến biên lợi nhuận của một doanh nghiệp cụ thể.**

## Ôn bài cũ (5 phút)

Đáp án ở mục 9.

1. Vì sao ROIC phải so với chi phí vốn mới biết tăng trưởng tạo hay phá giá trị (Bài 003)?
2. Hệ số trả lãi tính thế nào, và vì sao nó nhạy với lãi suất thả nổi (Bài 005)?
3. Nếu doanh thu tăng do giá bán tăng mà sản lượng không tăng, dòng tiền hoạt động có tăng tương ứng không (Bài 004)?
4. Nêu một dấu hiệu doanh nghiệp có "quyền định giá" (Bài 003).

## Bài này làm gì và chưa làm gì

| Bài này làm | Bài này chưa làm |
|---|---|
| Dạy bốn kênh truyền dẫn và cách tính tác động bằng số | Không dự báo vĩ mô, không dự báo lãi suất |
| Dạy phân biệt chỉ số giá, mức tỷ giá, so sánh cùng kỳ và so với đầu năm | Không tính chi phí vốn (WACC) — Bài 010 |
| Dạy cách đọc bảng số vĩ mô có kỳ và đơn vị rõ ràng | Không dạy cách chọn bội số theo chu kỳ — Bài 009 |
| Nêu số liệu thật của Việt Nam và thế giới tại ngày chốt | Không đưa ra nhận định về một doanh nghiệp cụ thể |

## Cách chia phiên và chọn phần cốt lõi

**Bài cốt lõi trong bộ bài tập:** 1, 2, 4, 8. Các câu còn lại là luyện thêm; không bỏ kiến thức bắt buộc của thân bài. Phiên A làm câu 1, 2; phiên B làm câu 4, 8.

`Ý_KIẾN` Phiên A: bốn kênh truyền dẫn và một tình huống hư cấu. Phiên B: bài tập và đọc số thực theo mẫu kỳ/đơn vị; số thời sự giữ mốc cũ, không học thuộc hoặc coi là đã cập nhật hôm nay.

Làm câu cốt lõi theo mục tiêu phiên trước khi xem đáp án; câu xen kẽ/chuyển giao kiểm hiểu sâu. Có thể dừng giữa bài; thời lượng ban đầu chưa được đo với người học. [Bảng thực hành và hai bài ôn](../practice/research-and-model-worksheets.md).

## 1. Bốn kênh truyền dẫn

`Ý_KIẾN` Kênh thứ năm — **bội số định giá** — cố ý để sang Bài 009 và Bài 010, vì muốn dùng nó phải biết bội số là gì và chi phí vốn là gì.

| Kênh | Đi vào đâu | Độ trễ điển hình | Ai hấp thụ khoản chênh lệch |
|---|---|---|---|
| Giá đầu vào / giá bán | Doanh thu, giá vốn, biên gộp | Ngay trong quý | Doanh nghiệp (nếu không có quyền định giá) hoặc khách hàng |
| Chi phí lãi vay | Lãi vay, lợi nhuận sau thuế, hệ số trả lãi | Theo kỳ điều chỉnh lãi suất (thả nổi) | Cổ đông |
| Tỷ giá | Doanh thu xuất khẩu, chi phí nhập khẩu, lãi/lỗ đánh giá lại nợ ngoại tệ | Từng tháng | Doanh nghiệp hoặc khách, tùy hợp đồng |
| Chu kỳ tín dụng | Sản lượng bán, tồn kho, đầu tư | 1–3 quý | Doanh nghiệp và người lao động |

`SUY_LUẬN` Điểm quan trọng: cùng một cú sốc, **doanh nghiệp có quyền định giá** chuyển được nó sang khách; **doanh nghiệp không có quyền định giá** phải hấp thụ trong biên. Đây là chỗ Bài 003 (moat) gặp Bài 008 (vĩ mô): moat không phải khái niệm trừu tượng, nó là **khả năng chuyển chi phí sang giá bán**.

## 2. Kênh giá: nén biên khi giá đầu vào tăng nhanh hơn giá bán

`SỰ_THẬT` Số liệu Việt Nam 9 tháng 2026 (Cục Thống kê — `nso.gov.vn`, mở `2026-10-26`): **chỉ số giá nguyên, nhiên, vật liệu dùng cho sản xuất tăng 5,12%** so cùng kỳ; **chỉ số giá xuất khẩu tăng 2,38%**; chỉ số giá nhập khẩu tăng 2,56%; tỷ giá thương mại hàng hoá **giảm 0,17%**.

`PHÉP_TÍNH` Chênh lệch tốc độ: `5,12 − 2,38 = 2,74 điểm phần trăm`. `SUY_LUẬN` Con số này chỉ cho biết **hướng** áp lực, chưa phải mức nén biên: (a) hai chỉ số khác phạm vi (giá đầu vào sản xuất trong nước so với giá hàng xuất khẩu) — chính checklist ở mục 6 cảnh báo ghép hai chuỗi khác hệ quy chiếu; (b) mức nén thật phụ thuộc **tỷ trọng giá vốn trong doanh thu**, nên phải tính lại doanh thu và giá vốn rồi mới chia, như bảng dưới. Với một doanh nghiệp có đầu vào tăng theo mặt bằng chung và đầu ra bán theo giá xuất khẩu chung, phần chênh phải được hấp thụ bằng: giảm biên, giảm chi phí khác, hoặc tăng năng suất.

`KỊCH_BẢN` `PHÉP_TÍNH` Ví dụ hư cấu: doanh nghiệp có doanh thu 1.000, giá vốn 700 (biên gộp 30%). Giả định giá đầu vào tăng 5,12% và giá bán tăng 2,38%:

| Chỉ tiêu | Trước | Sau khi giá đổi |
|---|---:|---:|
| Doanh thu | 1.000,0 | 1.023,8 |
| Giá vốn | 700,0 | 735,8 |
| Lợi nhuận gộp | 300,0 | 288,0 |
| Biên gộp | 30,0% | **28,13%** |

`PHÉP_TÍNH` Lợi nhuận gộp giảm `300 − 288 = 12` (tương đương 4% lợi nhuận gộp). Nếu doanh nghiệp chuyển được toàn bộ 5,12% vào giá bán, doanh thu thành `1.051,2`, biên gộp **giữ nguyên 30,0%**.

`SUY_LUẬN` Ba câu hỏi để biết doanh nghiệp cụ thể nằm ở đâu giữa hai kịch bản trên: (a) doanh thu/đơn vị sản phẩm có tăng theo lạm phát không; (b) biên gộp 3–5 năm có ổn định qua các năm lạm phát cao không; (c) thuyết minh có nói gì về khả năng chuyển giá, hợp đồng có điều khoản điều chỉnh giá không.

`SỰ_THẬT` Bối cảnh lạm phát chung: CPI tháng 9/2026 **+5,08%** so cùng kỳ, bình quân 9 tháng **+4,52%**, lạm phát cơ bản 9 tháng **+4,26%**; mục tiêu của NHNN là kiểm soát lạm phát **bình quân năm 2026** khoảng **4,5%**. `PHÉP_TÍNH` So **đúng mốc**: bình quân 9 tháng `4,52 − 4,5 = **+0,02 điểm phần trăm**` — coi như đang đúng mục tiêu. `SUY_LUẬN` CPI tháng 9 **+5,08% là so cùng kỳ**, một phép đo khác; **không** so trực tiếp nó với mục tiêu bình quân năm (nếu so, sẽ báo động sai 0,58 điểm phần trăm). (Nguồn: Cục Thống kê, trang CPI tháng 9 và quý III/2026; cổng NHNN Khu vực 1 cho mục tiêu bình quân.)

## 3. Kênh lãi suất: đọc bằng lãi suất thực, không bằng lãi suất danh nghĩa

`SỰ_THẬT` Theo cổng NHNN Khu vực 1 (bài đăng `2026-10-08`, mở `2026-10-26`): trong 9 tháng đầu 2026, NHNN **tiếp tục giữ nguyên các mức lãi suất điều hành**; mục tiêu kiểm soát lạm phát bình quân khoảng **4,5%**; **dư nợ tín dụng toàn hệ thống đến 30/09/2026 đạt 20,75 triệu tỷ đồng, tăng 11,59% so với cuối 2025** và tăng 16,69% so cùng kỳ. `CHƯA_BIẾT` **Mức số** của các lãi suất điều hành (tái cấp vốn, tái chiết khấu) và **tỷ giá trung tâm USD/VND**: `sbv.gov.vn` trả HTTP 403 với truy cập tự động trong lượt này. Không được tự điền con số.

`PHÉP_TÍNH` Lãi suất thực xấp xỉ = lãi suất danh nghĩa − lạm phát. Với lãi suất cho vay danh nghĩa giả định 8%/năm (`KỊCH_BẢN`, vì chưa có số chính thức):

| Mốc lạm phát | Lãi suất thực xấp xỉ | Xấp xỉ Fisher |
|---|---:|---:|
| CPI bình quân 9 tháng 4,52% | 3,48% | 3,33% |
| CPI tháng 9 so cùng kỳ 5,08% | 2,92% | 2,78% |

`SUY_LUẬN` Vì sao dạy bằng lãi suất thực: khi lãi suất điều hành giữ nguyên nhưng lạm phát tăng, **chi phí vay thực bị nén** — doanh nghiệp vay nhiều vẫn thấy "rẻ", và đây là một lý do khiến tăng trưởng tín dụng cao trong khi lãi suất danh nghĩa không đổi. Đồng thời nó tạo rủi ro: nếu lạm phát buộc phải tăng lãi suất sau đó, chi phí lãi sẽ nhảy.

`KỊCH_BẢN` `PHÉP_TÍNH` Tác động lên một doanh nghiệp: nợ vay 1.000, trong đó **50% thả nổi** lãi suất (500); nếu lãi suất thả nổi tăng **150 điểm cơ bản**, chi phí lãi tăng `500 × 1,5% = 7,5`. Đây là mức nhỏ; nhưng với doanh nghiệp có EBIT 120 và lãi vay 90 (ví dụ ở Bài 005), khoản +7,5 đưa hệ số trả lãi từ 1,33 xuống `120 / 97,5 = 1,23` — mất thêm biên an toàn.

`SỰ_THẬT` Mốc neo toàn cầu (mở `2026-10-26`): Fed nâng lãi suất mục tiêu **25 điểm cơ bản lên 3,75–4,00%** tại cuộc họp 15–16/09/2026 (federalreserve.gov); kỳ họp kế tiếp **27–28/10/2026 chưa diễn ra** nên chưa có quyết định mới. Lợi suất trái phiếu chính phủ Mỹ kỳ hạn 10 năm **4,96%** cho kỳ quan sát **22/10/2026** (FRED DGS10; các ngày trước: 5,13% / 5,12% / 5,15%). ECB: lãi suất tiền gửi **2,50%**, lãi suất tái cấp vốn chính **2,65%**, hiệu lực 16/09/2026.

`SUY_LUẬN` Ý nghĩa cho người học: chi phí vốn toàn cầu không còn trong pha nới lỏng. Điều này đặt **trần** cho bội số định giá (Bài 009/010) và là lý do doanh nghiệp vay bằng ngoại tệ chịu hai lực cùng lúc: lãi suất cao hơn và tỷ giá có thể bất lợi.

## 4. Kênh tỷ giá: đọc đúng chỉ số giá USD

`SỰ_THẬT` Số liệu chính thức mở được trong lượt này: **chỉ số giá đô la Mỹ** tháng 9/2026 **giảm 0,69%** so tháng trước, **giảm 1,34%** so cùng kỳ, bình quân 9 tháng **tăng 1,01%** (Cục Thống kê). `SỰ_THẬT` Theo phần phương pháp của Cục Thống kê, chỉ số này phản ánh biến động **giá đô la Mỹ trên thị trường**: giá USD được thu thập tại các **điểm bán lẻ**, giá tháng là **bình quân giá các ngày trong tháng**. `CHƯA_BIẾT` Mức tỷ giá trung tâm USD/VND chính thức: nguồn NHNN bị chặn trong lượt này.

`SUY_LUẬN` Cách đọc đúng: "−1,34% so cùng kỳ" nghĩa là **giá USD bán lẻ bình quân tháng 9/2026 tính bằng VND thấp hơn khoảng 1,34%** so tháng 9/2025 — tức VND đã mạnh lên một chút so với USD theo thước đo này. Ba điều **không** được suy ra: (a) đây không phải **tỷ giá trung tâm** của NHNN hay tỷ giá liên ngân hàng; (b) đây là **bình quân tháng**, không phải tỷ giá cuối kỳ dùng để đánh giá lại nợ ngoại tệ trên báo cáo tài chính; (c) mức VND lên giá chính xác là `1 / (1 − 1,34%) − 1 ≈ 1,36%`, không đúng bằng 1,34%. Lỗi hay gặp khi đọc bản tin là trộn ba loại tỷ giá này với nhau.

`SỰ_THẬT` Bối cảnh thương mại 9 tháng 2026 (Cục Thống kê): xuất khẩu **+24,5%**, nhập khẩu **+36,7%** so cùng kỳ; **nhập siêu 19,42 tỷ USD**; tồn kho ngành chế biến chế tạo **+11,9%** so cùng kỳ tại 30/09/2026.

`PHÉP_TÍNH` `KỊCH_BẢN` Hai doanh nghiệp hư cấu, cùng doanh thu 1.000:

- Doanh nghiệp **nhập khẩu**: 60% nguyên liệu nhập, tỷ giá tăng 5% (giả định) → chi phí tăng `1.000 × 60% × 5% = 30`.
- Doanh nghiệp **xuất khẩu**: toàn bộ doanh thu bằng ngoại tệ, tỷ giá tăng 5% → doanh thu quy đổi tăng `1.000 × 5% = 50` (nếu giá bán ngoại tệ không đổi).

`SUY_LUẬN` Trong bối cảnh nhập khẩu tăng nhanh hơn xuất khẩu và có nhập siêu, áp lực tỷ giá thường nghiêng về phía bất lợi cho doanh nghiệp nhập khẩu nhiều. Nhưng đây là **suy luận về hướng**, không phải dự báo tỷ giá — muốn kết luận phải có mức tỷ giá thật, mà lượt này chưa mở được.

`SUY_LUẬN` **Góc nhìn của nhà đầu tư, không chỉ của doanh nghiệp**: nếu bạn giữ tài sản bằng VND, lợi nhuận danh nghĩa của bạn tính bằng VND; người giữ USD nhận kết quả khác trong cùng kỳ. Cùng một doanh nghiệp, hai đơn vị tiền tệ, hai kết quả — phải ghi rõ đang đo bằng đồng tiền nào. Đây là chủ đề bắt buộc, không phải phần phụ.

## 5. Kênh chu kỳ tín dụng: "van" mở bao nhiêu

`SỰ_THẬT` Theo cổng NHNN Khu vực 1 (bài đăng `2026-10-08`): tín dụng đến **30/09/2026 tăng 11,59%** so cuối 2025 (và +16,69% so cùng kỳ); văn bản nêu NHNN đã "thông báo công khai, minh bạch **nguyên tắc** giao tăng trưởng tín dụng năm 2026" nhưng **không nêu con số mục tiêu**. `CHƯA_BIẾT` Mục tiêu tăng trưởng tín dụng 2026 bằng số (một số nguồn thứ cấp nêu ~15% từ Chỉ thị 01/CT-NHNN, nhưng **văn bản gốc chưa mở được** trong lượt này). Vì vậy bài này **không** tính "dư địa tín dụng" — phép trừ đó chỉ có nghĩa sau khi xác minh được mục tiêu.

`SỰ_THẬT` Cục Thống kê ghi tín dụng đến **28/09/2026** tăng **10,89%** so đầu năm, huy động vốn **+9,78%**. Hai nguồn lệch nhau vì **khác ngày chốt và khác mốc so sánh** (28/09 so đầu năm so với 30/09 so cuối 2025) — đây là ví dụ sống về việc phải đọc kỳ và mốc so sánh trước khi so hai con số.

`SUY_LUẬN` Vì sao kênh này quan trọng với người phân tích doanh nghiệp: tăng trưởng doanh thu của nhiều ngành (bán lẻ, bất động sản, vật liệu, ngân hàng) phụ thuộc vào việc tín dụng có chảy hay không. Bài học phương pháp ở đây còn quan trọng hơn con số: khi mục tiêu tín dụng là **văn bản chưa mở được**, mọi phép "còn dư địa bao nhiêu" đều là giả định — phải ghi rõ trong kịch bản (Bài 012) thay vì trình bày như dữ kiện.

`SỰ_THẬT` Về phân loại thị trường (ảnh hưởng dòng vốn ngoài): Việt Nam **đã** được FTSE Russell phân loại lại thành Secondary Emerging, hiệu lực từ mở cửa **21/09/2026**, với việc đưa vào chỉ số theo **bốn đợt**, bắt đầu 9/2026 và kết thúc 9/2027 (LSEG, thông cáo tháng 4 và tháng 10/2026). `SUY_LUẬN` (dựa trên **một bài báo thứ cấp**, chưa mở văn bản MSCI) MSCI vẫn giữ Việt Nam ngoài danh sách theo dõi nâng hạng tại kỳ review 24/06/2026; `CHƯA_BIẾT` văn bản gốc MSCI vì `msci.com` chặn truy cập tự động. `SUY_LUẬN` Bài học: "được nâng hạng" không phải một sự kiện duy nhất — phải nói rõ **nhà cung cấp chỉ số nào**, và dòng vốn vào theo lịch nhiều đợt chứ không phải một cục.

## 6. Cách đọc một bảng số vĩ mô (checklist 5 điểm)

`Ý_KIẾN` Trước khi dùng bất kỳ con số vĩ mô nào, kiểm năm điểm:

1. **Kỳ dữ liệu**: tháng nào, quý nào; công bố ngày nào; số là sơ bộ hay chính thức.
2. **Mốc so sánh**: so tháng trước (mom), so cùng kỳ (yoy), hay so đầu năm (YTD). Ba mốc này cho ba con số khác nhau từ cùng một dữ liệu.
3. **Đơn vị**: %/năm hay điểm phần trăm; triệu tỷ đồng hay tỷ USD; chỉ số (index) hay mức tuyệt đối. Không bao giờ cộng hai đại lượng khác đơn vị.
4. **Chuỗi gốc**: tốc độ tăng GDP (theo giá so sánh) và CPI bình quân lũy kế là hai phép đo khác nhau; trước khi ghép chúng vào một phép tính, phải đọc định nghĩa của từng chuỗi (ví dụ ngay dưới cho thấy phép trừ hai chuỗi này là sai).
5. **Nguồn gốc**: cơ quan thống kê/ngân hàng trung ương của nước đó, không dùng bài báo tóm tắt làm số chính.

`SỰ_THẬT` Ví dụ áp checklist, có một bẫy: GDP 9 tháng **+9,01%** (so cùng kỳ) và CPI bình quân 9 tháng **+4,52%**. Nhiều tài liệu lấy `9,01 − 4,52 = 4,49 điểm phần trăm` và gọi là "tăng trưởng thực". Theo trang "Khái niệm, phương pháp tính" của Cục Thống kê, tốc độ tăng GDP quý, 6 tháng, 9 tháng và năm được tính **theo giá so sánh**: GDP giá so sánh kỳ này chia GDP giá so sánh cùng kỳ năm trước. `SUY_LUẬN` Vậy 9,01% **đã là** tăng trưởng thực; trừ thêm CPI là trừ lạm phát **hai lần**, và CPI cũng không phải chỉ số giảm phát của GDP. Đây là ví dụ điển hình của quy tắc: **không tự chế ra một chỉ tiêu mới bằng cách trừ hai số khác hệ quy chiếu**.

## 7. Năm câu hỏi khi đọc vĩ mô cho một doanh nghiệp

1. Doanh thu của doanh nghiệp này nhạy với giá bán, sản lượng, hay cả hai; giá đầu vào của nó là gì?
2. Trong 5 năm, biên gộp có giữ được khi lạm phát đầu vào tăng không?
3. Bao nhiêu phần nợ là lãi suất thả nổi; lãi suất tăng 150–200 điểm cơ bản thì lợi nhuận giảm bao nhiêu?
4. Doanh thu/chi phí ngoại tệ chiếm bao nhiêu; doanh nghiệp có nợ ngoại tệ không?
5. Cầu của doanh nghiệp phụ thuộc bao nhiêu vào tín dụng và vào dòng vốn ngoài?

## 8. Bài tập (8 câu, 40 phút)

`KỊCH_BẢN` Số liệu hư cấu trừ khi ghi rõ; đơn vị: tỷ đồng.

### Bài 1 (nhớ lại) — bốn kênh
Với mỗi sự kiện, chỉ ra kênh truyền dẫn và dòng báo cáo bị ảnh hưởng trước: (a) giá nguyên liệu nhập tăng; (b) lãi suất cho vay tăng; (c) VND yếu đi so với USD; (d) tín dụng bị siết.

### Bài 2 (vận dụng) — nén biên
Doanh nghiệp có doanh thu 2.000, giá vốn 1.400. Giá bán tăng 2% nhưng giá đầu vào tăng 6%. Tính biên gộp trước và sau, và lợi nhuận gộp chênh bao nhiêu.

### Bài 3 (vận dụng) — lãi suất thực
Lãi suất cho vay danh nghĩa 9%/năm. CPI bình quân 4,52%. Tính lãi suất thực xấp xỉ và xấp xỉ Fisher. Nêu một lý do doanh nghiệp vay nhiều có thể "không thấy đau" trong ngắn hạn.

### Bài 4 (vận dụng) — nợ thả nổi
Nợ vay 2.000, 40% thả nổi. Lãi suất tăng 200 điểm cơ bản. Tính chi phí lãi tăng thêm và cho biết nếu EBIT 300, chi phí lãi ban đầu 150 thì hệ số trả lãi đổi thế nào.

### Bài 5 (vận dụng, câu cũ xen kẽ) — nối Bài 004
Doanh thu tăng 20% nhờ giá bán tăng, sản lượng không đổi; phải thu và tồn kho tăng 30%. Hỏi CFO có tăng theo lợi nhuận không; chỉ tiêu nào ở Bài 004 phát hiện điều này.

### Bài 6 (vận dụng, câu cũ xen kẽ) — nối Bài 005
Một doanh nghiệp có lịch nợ: 40% trái phiếu đáo hạn trong 8 tháng; lãi suất thả nổi 70%. Nêu hai rủi ro vĩ mô cộng hưởng và một dữ liệu cần kiểm.

### Bài 7 (chuyển giao) — xuất khẩu hay nhập khẩu
Ba doanh nghiệp: A bán 100% trong nước, nguyên liệu trong nước; B xuất khẩu 100%, nguyên liệu trong nước; C bán trong nước nhưng 60% nguyên liệu nhập. Trong bối cảnh nhập khẩu tăng nhanh hơn xuất khẩu và nhập siêu, doanh nghiệp nào chịu rủi ro tỷ giá lớn nhất, và cần dữ liệu gì để kết luận chắc hơn?

### Bài 8 (chuyển giao) — tìm lỗi trong đoạn đọc số
"CPI tháng 9 tăng 5,08% nên cả năm lạm phát là 5,08%. Chỉ số giá USD giảm 1,34% nghĩa là VND lên giá 1,34% so với USD. GDP tăng 9,01% nên tăng trưởng thực là 9,01%." Chỉ ra **ba** lỗi và cách sửa.

## 9. Đáp án

### Bài 1

`SUY_LUẬN` (a) Kênh chi phí → **giá vốn**, biên gộp. (b) Kênh lãi suất → **chi phí lãi vay**, lợi nhuận sau thuế, hệ số trả lãi. (c) Kênh tỷ giá → **doanh thu** (nếu xuất khẩu) hoặc **giá vốn** (nếu nhập khẩu), và lãi/lỗ đánh giá lại nợ ngoại tệ. (d) Kênh tín dụng → **sản lượng bán** và tồn kho; với ngân hàng là tăng trưởng dư nợ.

### Bài 2

`PHÉP_TÍNH` Trước: biên gộp `(2.000 − 1.400)/2.000 = 30,0%`; gộp 600.
Sau: doanh thu `2.000 × 1,02 = 2.040`; giá vốn `1.400 × 1,06 = 1.484`; gộp `556`; biên `556/2.040 = 27,25%`.
`PHÉP_TÍNH` Chênh lợi nhuận gộp: `600 − 556 = 44` (giảm 7,3%).
`SUY_LUẬN` Câu này kiểm: bạn có tính lại **từng dòng** (doanh thu × 1,02; giá vốn × 1,06) rồi mới chia, thay vì lấy hiệu hai tốc độ `6 − 2 = 4` điểm phần trăm làm mức giảm biên. Biên thực tế chỉ giảm `30,0 − 27,25 = 2,75` điểm phần trăm, vì giá vốn chỉ chiếm 70% doanh thu.

### Bài 3

`PHÉP_TÍNH` Xấp xỉ: `9 − 4,52 = 4,48%`. Xấp xỉ Fisher: `(1,09 / 1,0452) − 1 = 4,29%`.
`SUY_LUẬN` Lý do "không thấy đau" trong ngắn hạn: lãi suất thực bị nén khi lạm phát tăng mà lãi suất danh nghĩa giữ nguyên; doanh thu của doanh nghiệp tăng theo giá, còn khoản trả lãi thì cố định theo hợp đồng. Rủi ro: khi lãi suất phải điều chỉnh, chi phí tăng trong khi giá đầu ra đã hết dư địa tăng.

### Bài 4

`PHÉP_TÍNH` Nợ thả nổi `2.000 × 40% = 800`; chi phí lãi tăng `800 × 2% = 16`; lãi vay mới `166`.
`PHÉP_TÍNH` Hệ số trả lãi: trước `300/150 = 2,00`; sau `300/166 = 1,81`.
`SUY_LUẬN` Câu này kiểm: bạn có nối được kênh vĩ mô với chỉ tiêu sống còn của Bài 005.

### Bài 5

`SUY_LUẬN` CFO **không** tăng tương ứng: doanh thu tăng do giá, nhưng phải thu và tồn kho tăng 30% — tiền bị giam trong vốn lưu động. Chỉ tiêu phát hiện: **tỷ lệ chuyển hoá tiền mặt** giảm và **DSO/DIO** tăng (Bài 004).

### Bài 6

`SUY_LUẬN` Hai rủi ro cộng hưởng: (a) **tái cấp vốn** — 40% trái phiếu đáo hạn trong 8 tháng, nếu thị trường tín dụng đóng thì phải huy động với lãi suất cao; (b) **lãi suất thả nổi 70%** — chi phí lãi tăng ngay khi lãi suất thị trường lên. Dữ liệu cần kiểm: đã có cam kết gia hạn/tái cấp vốn bằng văn bản chưa, và điều khoản vay có giới hạn vay thêm không.

### Bài 7

`SUY_LUẬN` Doanh nghiệp **C** chịu rủi ro tỷ giá lớn nhất trong bối cảnh nhập siêu và tỷ giá chịu áp lực: nó nhập 60% nguyên liệu nhưng bán trong nước bằng VND — chi phí bằng ngoại tệ, doanh thu bằng nội tệ, không có nguồn thu ngoại tệ tự nhiên để bù. Doanh nghiệp B hưởng lợi nếu tỷ giá tăng (doanh thu ngoại tệ, chi phí nội tệ). A gần như trung tính.
`SUY_LUẬN` Cần thêm: tỷ trọng chi phí nhập khẩu trên tổng chi phí; doanh nghiệp có nợ ngoại tệ không; hợp đồng bán có điều khoản điều chỉnh theo tỷ giá không; và **mức tỷ giá thật** (lượt này `CHƯA_BIẾT`).

### Bài 8

`SUY_LUẬN` Lỗi 1: "CPI tháng 9 tăng 5,08% nên cả năm 5,08%" — 5,08% là **so cùng kỳ**, còn lạm phát cả năm là bình quân hoặc so tháng 12; số đúng cho 9 tháng là **+4,52%** bình quân. Lỗi 2: "chỉ số giá USD giảm 1,34% nghĩa là VND lên giá 1,34%" — hướng đúng nhưng câu bị **nói quá**: chỉ số đo giá USD **bán lẻ bình quân tháng**, không phải tỷ giá trung tâm hay tỷ giá cuối kỳ, và mức lên giá chính xác của VND là `1/0,9866 − 1 ≈ 1,36%`. Cách sửa: "giá USD bán lẻ bình quân tháng 9 thấp hơn cùng kỳ khoảng 1,34%". Lỗi 3: câu "GDP tăng 9,01% nên tăng trưởng thực là 9,01%" thật ra **đúng**, vì Cục Thống kê tính tốc độ tăng GDP theo giá so sánh; nhưng người viết phải nêu căn cứ đó. Lỗi đi kèm hay gặp là lấy `9,01 − 4,52` rồi gọi là "tăng trưởng thực" — trừ lạm phát hai lần.
`SUY_LUẬN` Câu này kiểm: bạn có đọc **định nghĩa và phương pháp** của từng chỉ tiêu trước khi kết luận, kể cả khi câu kết luận hoá ra đúng.

### Đáp án phần ôn bài cũ

1. Vì ROIC thấp hơn chi phí vốn nghĩa là mỗi đồng tái đầu tư phá huỷ giá trị (Bài 003).
2. `EBIT / lãi vay`; nhạy với thả nổi vì lãi vay thay đổi ngay khi lãi suất thị trường đổi (Bài 005).
3. Không hẳn — giá tăng làm lợi nhuận tăng nhưng dòng tiền phụ thuộc thu tiền và vốn lưu động (Bài 004).
4. Ví dụ: tăng giá mà khách không rời đi; biên gộp ổn định qua nhiều năm kể cả năm lạm phát cao (Bài 003).

## 10. Lỗi thường gặp

- Dùng số vĩ mô mà không ghi kỳ và mốc so sánh (mom / yoy / YTD).
- Đọc **chỉ số giá USD** (giá bán lẻ bình quân tháng) như tỷ giá trung tâm hoặc tỷ giá cuối kỳ dùng trên báo cáo tài chính.
- Lấy tốc độ tăng GDP (đã tính theo giá so sánh) trừ tiếp CPI rồi gọi là "tăng trưởng thực" — trừ lạm phát hai lần.
- Nghĩ lạm phát tốt hay xấu cho mọi doanh nghiệp như nhau.
- Bỏ qua tỷ trọng nợ thả nổi khi đánh giá tác động lãi suất.
- Cho rằng "nâng hạng" là một sự kiện duy nhất, không phân biệt FTSE và MSCI.
- Dùng lãi suất danh nghĩa để nói chi phí vốn "rẻ" trong khi lạm phát cao.
- Lấy số từ một bài báo tóm tắt thay vì mở trang của cơ quan thống kê/ngân hàng trung ương.

## 11. Ranh giới an toàn

- Bài này **không** dự báo lãi suất, lạm phát, tỷ giá và không phải khuyến nghị mua/bán/nắm giữ.
- Số liệu trong bài có ngày chốt; không dùng lại cho quyết định ở thời điểm khác mà không cập nhật.
- Các con số `CHƯA_BIẾT` (lãi suất điều hành, tỷ giá trung tâm, văn bản MSCI) **không được** thay bằng ước lượng từ trí nhớ.
- Không suy ra hành động đầu tư từ một chỉ tiêu vĩ mô; phải đi qua hồ sơ doanh nghiệp (Đợt 2) và kịch bản (Bài 012).

## 12. Điều tôi vẫn chưa hiểu

1. Bạn muốn luyện kênh nào trước: **giá đầu vào → biên gộp** hay **lãi suất → chi phí vốn**?
2. Bạn có cần một bài riêng về **lạm phát và hàng tồn kho** (ảnh hưởng tới giá vốn, lợi nhuận ảo khi giá lên) không?
3. Bạn muốn bảng theo dõi 8 chỉ tiêu vĩ mô ở dạng tệp để tự điền hằng tháng không?
4. Bạn đang theo dõi doanh nghiệp xuất khẩu hay phục vụ thị trường trong nước? (quyết định kênh tỷ giá có quan trọng với bạn không)

## 13. Bảng theo dõi: tách số liệu khỏi khái niệm

Dùng [mẫu cập nhật](../../data/processed/macro-observation-template.md) để ghi số mới cùng kỳ, đơn vị, mốc so sánh, phiên bản và nguồn. Mẫu không tự thu thập dữ liệu và không dùng0 thay số chưa biết.

[Bảng lịch sử được tách nguyên văn](../../data/raw/macro-lesson-008-legacy-2026-10-26.md) chỉ để truy dấu. Các số của bảng đó chưa được xác minh lại trong lượt chỉnh cách học này. Ví dụ thời sự còn trong các mục khác cũng giữ mốc gốc; khi áp dụng phải mở lại nguồn, không coi việc tách tệp là cập nhật dữ liệu.

## 14. Nguồn Internet đã mở

<details>
<summary>Nguồn chi tiết và lịch sử kiểm — giữ mốc dữ liệu gốc</summary>

Tất cả mở ngày `2026-10-26`.

- [Chỉ số giá tiêu dùng, chỉ số giá vàng và chỉ số giá đô la Mỹ tháng 9, quý III và 9 tháng năm 2026 — Cục Thống kê](https://www.nso.gov.vn/du-lieu-va-so-lieu-thong-ke/2026/10/chi-so-gia-tieu-dung-chi-so-gia-vang-va-chi-so-gia-do-la-my-thang-chin-quy-iii-va-9-thang-nam-2026/) — HTTP 200; đăng `2026-10-03`. Cung cấp CPI (mom, yoy, lũy kế), lạm phát cơ bản, chỉ số giá USD, chỉ số giá vàng.
- [Báo cáo tình hình kinh tế – xã hội quý III và 9 tháng năm 2026 — Cục Thống kê](https://www.nso.gov.vn/tin-tuc-thong-ke/2026/10/bao-cao-tinh-hinh-kinh-te-xa-hoi-quy-iii-va-9-thang-nam-2026/) — HTTP 200; đăng `2026-10-03`. Cung cấp GDP quý III và lũy kế, giá đầu vào sản xuất, giá xuất/nhập khẩu, xuất nhập khẩu, nhập siêu, tồn kho, tín dụng và huy động vốn của hệ thống.
- [Chỉ số giá — Khái niệm, phương pháp tính — Cục Thống kê](https://www.nso.gov.vn/?p=16942) — HTTP 200; mở `2026-10-26`. Cung cấp: chỉ số giá USD phản ánh biến động giá USD trên thị trường; giá thu thập tại điểm bán lẻ, bình quân các ngày trong tháng.
- [Tổng sản phẩm trong nước — Khái niệm, phương pháp tính — Cục Thống kê](https://www.nso.gov.vn/?p=16552) — HTTP 200; mở `2026-10-26`. Cung cấp: tốc độ tăng GDP quý/6 tháng/9 tháng/năm tính **theo giá so sánh**, so với cùng kỳ năm trước.
- [Kết quả điều hành chính sách tiền tệ và hoạt động ngân hàng 9 tháng đầu năm 2026 — NHNN Khu vực 1](https://sbv.hanoi.gov.vn/chi-tiet-tin-bai-lanh-dao/-/view_content/6711809-ket-qua-dieu-hanh-chinh-sach-tien-te-va-hoat-dong-ngan-hang-9-thang-dau-nam-2026.html) — HTTP 200; đăng `2026-10-08`. Cung cấp: giữ nguyên lãi suất điều hành; mục tiêu lạm phát **bình quân năm 2026** khoảng 4,5%; dư nợ tín dụng 30/09/2026 là 20,75 triệu tỷ đồng (+11,59% so cuối 2025, +16,69% so cùng kỳ); nguyên tắc giao tăng trưởng tín dụng nhưng **không nêu con số mục tiêu**. `CHƯA_BIẾT` mức số lãi suất điều hành và mục tiêu tín dụng bằng số.
- [FOMC statement 2026-09-16 — Federal Reserve](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm) — HTTP 200. Cung cấp lãi suất mục tiêu 3,75–4,00%.
- [FOMC calendar — Federal Reserve](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) — HTTP 200. Xác nhận kỳ họp 27–28/10/2026 chưa diễn ra tại ngày chốt.
- [DGS10 — FRED, Federal Reserve Bank of St. Louis](https://fred.stlouisfed.org/series/DGS10) — HTTP 200; cập nhật ngày quan sát 22/10/2026 (4,96%); ghi chú "next release 26/10/2026".
- [Key ECB interest rates — ECB](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html) — HTTP 200; hiệu lực 16/09/2026.
- [FTSE Russell — kết quả phân loại lại Việt Nam (LSEG press release)](https://www.lseg.com/en/media-centre/press-releases/ftse-russell/2026/ftse-country-classification-review-september-2026) và [LSEG Insights — Why Vietnam is joining the FTSE GEIS](https://www.lseg.com/en/insights/ftse-russell/why-vietnam-is-joining-the-ftse-geis) — HTTP 200. Cung cấp: hiệu lực 21/09/2026; LSEG Insights nêu nguyên văn việc đưa vào diễn ra theo **bốn đợt**, bắt đầu 9/2026, kết thúc 9/2027. **Giới hạn**: PDF kèm theo không đọc được bằng công cụ, nên tỷ lệ % từng đợt **CHƯA** lấy được từ văn bản gốc.
- [MSCI keeps Việt Nam off upgrade watch list — Vietnam News](https://vietnamnews.vn/economy/1784056/msci-keeps-viet-nam-off-upgrade-watch-list.html) — HTTP 200; đăng `2026-06-24`; **nguồn thứ cấp**. `CHƯA_BIẾT` văn bản gốc MSCI: `msci.com` trả trang "Challenge Validation" với truy cập tự động.
- `CHƯA_BIẾT` Tỷ giá trung tâm USD/VND: `sbv.gov.vn` trả **HTTP 403** trong lượt này; không dùng nguồn tổng hợp thứ cấp làm số chính. Cách xác minh: mở trang tỷ giá trung tâm của NHNN bằng trình duyệt, ghi ngày.

**Trạng thái kiểm nguồn**: đã qua một lượt `source-fact-checker` độc lập ngày `2026-10-26`, kết luận **KHÔNG ĐẠT** với **2 lỗi nghiêm trọng**: (a) so CPI tháng 9 (+5,08% **so cùng kỳ**) với mục tiêu **bình quân năm** 4,5% — sai mốc; so đúng mốc là bình quân 9 tháng 4,52% so 4,5% = **+0,02 điểm %**; (b) nêu "mục tiêu tăng trưởng tín dụng ~15%" như số liệu của trang NHNN, trong khi trang đó **không có con số này** → đã hạ xuống `CHƯA_BIẾT` và **bỏ** phép tính "dư địa 3,41 điểm %". Đã sửa thêm 3 lỗi "cần sửa" (giải thích lệch hai nguồn tín dụng, nhãn MSCI, lỗi chính tả) và làm rõ chỗ **không được** lấy GDP trừ CPI để suy ra tăng trưởng thực. Số liệu vĩ mô khác (CPI, GDP, giá XK/NK, XNK, nhập siêu, tín dụng 11,59%, Fed, DGS10, ECB, FTSE) đều khớp nguồn gốc. Lượt review sau đó cùng ngày sửa thêm: cách đọc chỉ số giá USD theo phương pháp của Cục Thống kê; chốt GDP tính theo giá so sánh (bỏ `CHƯA_BIẾT`); thống nhất cách tính nén biên giữa mục 2 và đáp án Bài 2; bảng mục 13 còn sót "mục tiêu tín dụng ~15%" đã hạ về `CHƯA_BIẾT`. Bản hiện tại **chưa có biên bản mới** cho hash sau khi sửa.


</details>
