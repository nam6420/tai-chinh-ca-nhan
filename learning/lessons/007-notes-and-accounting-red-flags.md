# Bài 007: Đọc thuyết minh và cờ đỏ kế toán

- Ngày: `2026-10-26`
- Chốt dữ liệu lúc: `2026-10-26 11:58 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Đọc được bản đồ thuyết minh của một báo cáo tài chính; phân biệt chính sách kế toán, thay đổi ước tính và sửa lỗi; nhận diện bốn chỗ hay được dùng để "làm đẹp" số liệu (doanh thu, phải thu, tồn kho, vốn hoá chi phí); đọc được thước đo do ban điều hành tự định nghĩa; phân biệt bốn loại ý kiến kiểm toán (một ý kiến không sửa đổi và ba loại sửa đổi).
- Thời lượng: 40 phút đọc + 45 phút bài tập (2 phiên)
- Bài trước liên quan: Thứ tự đọc **Bước 13/23 của Nhánh 1** — học ngay sau [Bài 006: Phân bổ vốn và quản trị](006-capital-allocation-governance.md) (kế thừa [Bài 005](005-debt-liquidity-survival.md), [Bài 004](004-cash-flow-and-earnings-quality.md) và [Bài 001](001-business-financial-statements.md)). Học tiếp: [Bài 008: Vĩ mô truyền dẫn vào doanh thu, chi phí và dòng tiền](008-macro-transmission.md) (Bước 14/23).
- Câu hỏi cốt lõi: **Số liệu đẹp này được tạo ra bằng chính sách kế toán nào?**

> Đây là bài học nền tảng toàn cầu, không phải khuyến nghị mua, bán hay nắm giữ chứng khoán. Mọi ví dụ số học là hư cấu. Bài này **không** kết luận doanh nghiệp nào gian lận; nó dạy cách đặt câu hỏi và cách kiểm.

## Hiểu bài này trong 1 phút

`SUY_LUẬN` Hai doanh nghiệp cùng bán một sản phẩm, cùng doanh thu, cùng số tiền thực thu. Một bên chọn khấu hao nhà máy trong 10 năm, bên kia 20 năm — bên thứ hai báo lãi cao hơn mỗi năm dù chẳng bán được nhiều hơn. Một bên ghi chi phí phát triển sản phẩm ngay vào lãi lỗ, bên kia "vốn hoá" nó thành tài sản rồi chia nhỏ nhiều năm — bên thứ hai lại báo lãi cao hơn.

Cả hai cách làm đều có thể **hợp pháp**, nhưng không phải vì doanh nghiệp được "tự chọn". `SỰ_THẬT` Thời gian khấu hao là **ước tính** phải có căn cứ. Còn theo IAS 38 (IFRS Foundation, mở `2026-10-26`), chi phí **nghiên cứu** luôn ghi vào chi phí, chi phí **phát triển** được ghi thành tài sản khi **đạt các tiêu chí** quy định. `SUY_LUẬN` Chỗ "co giãn" nằm ở việc đánh giá khi nào các tiêu chí đó được coi là đạt — một xét đoán của ban điều hành. Vì vậy câu hỏi đúng không phải "doanh nghiệp có gian lận không", mà là: **lựa chọn nào đang được dùng, đã đổi chưa, và nếu áp cách thận trọng hơn thì lợi nhuận còn bao nhiêu?**

> Câu cần nhớ: **Thuyết minh không phải phần phụ lục; đó là nơi doanh nghiệp nói ra cách nó tạo ra con số.**

## Ôn bài cũ (5 phút)

Ôn lại các bài trước trong Nhánh 1 ([Bài 004](004-cash-flow-and-earnings-quality.md) → [Bài 005](005-debt-liquidity-survival.md) → [Bài 006](006-capital-allocation-governance.md)). Đáp án ở mục 9:

1. Nếu phải thu tăng 100 trong năm, `CFO` thay đổi thế nào ([Bài 004](004-cash-flow-and-earnings-quality.md))?
2. `Goodwill` hình thành khi nào, và điều gì xảy ra nếu thương vụ không đạt kỳ vọng ([Bài 006](006-capital-allocation-governance.md))?
3. Kể hai dấu hiệu mua lại cổ phiếu đáng ngờ ([Bài 006](006-capital-allocation-governance.md)).
4. Vì sao "lãi tăng" chưa chắc là "`EPS` tăng" ([Bài 006](006-capital-allocation-governance.md))?

## Bài này làm gì và chưa làm gì

| Bài này làm | Bài này chưa làm |
|---|---|
| Dạy bản đồ thuyết minh và thứ tự đọc | Không dạy lập báo cáo tài chính hay định khoản |
| Dạy bốn nhóm chính sách hay bị dùng để làm đẹp số | Không kết luận gian lận; không thay thế kiểm toán hay điều tra |
| Dạy đọc MPM (thước đo ban điều hành tự định nghĩa) và bốn loại ý kiến kiểm toán | Không dạy phân tích định lượng chuyên sâu về chất lượng lợi nhuận (đã có Bài 004) |
| Cho bài tập "tính lại lợi nhuận theo cách thận trọng hơn" | Không định giá ảnh hưởng của các điều chỉnh đó (Đợt 2) |

## Cách chia phiên và chọn phần cốt lõi

**Bài cốt lõi trong bộ bài tập:** 1, 2, 7. Các câu còn lại là luyện thêm; không bỏ kiến thức bắt buộc của thân bài. Phiên A làm câu 1, 2; phiên B làm câu 7.

`Ý_KIẾN` Phiên A: bản đồ thuyết minh và ví dụ số; tự chỉ ra điều gì thay đổi lợi nhuận. Phiên B: đối chiếu chính sách/ước tính, thước đo điều chỉnh và ý kiến kiểm toán; ngoại lệ chuẩn mực quay lại sau khi hiểu cơ chế.

Làm câu cốt lõi theo mục tiêu phiên trước khi xem đáp án; câu xen kẽ/chuyển giao kiểm hiểu sâu. Có thể dừng giữa bài; thời lượng ban đầu chưa được đo với người học. [Bảng thực hành và hai bài ôn](../practice/research-and-model-worksheets.md).

## 1. Bản đồ thuyết minh: đọc theo thứ tự nào

`SUY_LUẬN` Thuyết minh của một doanh nghiệp lớn thường dài 50–200 trang (ước lượng thực hành, khác theo quy mô và thị trường), nên phải đọc có thứ tự. Thứ tự đề xuất:

| Bước | Đọc gì | Trả lời câu hỏi |
|---|---|---|
| 1 | Ý kiến kiểm toán và "cơ sở của ý kiến" | Có vấn đề gì bị nêu không |
| 2 | Chính sách kế toán trọng yếu | Doanh thu ghi khi nào; khấu hao bao nhiêu năm; chi phí nào được vốn hoá |
| 3 | Thay đổi chính sách/ước tính trong năm | Có gì đổi, đổi vì lý do gì, ảnh hưởng bao nhiêu |
| 4 | Các khoản mục lớn: phải thu, tồn kho, tài sản cố định, goodwill | Có dấu hiệu trích lập thiếu không |
| 5 | Nợ vay và cam kết | Lịch đáo hạn, điều khoản, tài sản bảo đảm (Bài 005) |
| 6 | Bên liên quan và thù lao ban điều hành | Có chuyển giá trị ra ngoài không (Bài 006) |
| 7 | Sự kiện sau ngày kết thúc kỳ và cam kết ngoài bảng | Có rủi ro chưa hiện trên số liệu không |

`SỰ_THẬT` Về việc phân loại thay đổi: IAS 8 (IFRS Foundation, trang chuẩn mở ngày `2026-10-26`) quy định tiêu chí lựa chọn và thay đổi **chính sách kế toán**, cùng cách xử lý và thuyết minh **thay đổi chính sách**, **thay đổi ước tính kế toán** và **sửa lỗi**. Ba khái niệm này không giống nhau:

- `SỰ_THẬT` **Thay đổi chính sách kế toán** được áp dụng **hồi tố** trừ khi không thể thực hiện được.
- `SỰ_THẬT` **Thay đổi ước tính kế toán** phát sinh từ thông tin mới hoặc diễn biến mới, và **không phải** sửa lỗi.
- `SỰ_THẬT` **Sai sót kỳ trước** là thiếu sót hoặc sai lệch trong báo cáo tài chính của kỳ trước, do không sử dụng hoặc sử dụng sai thông tin đáng tin cậy đã có.

`SỰ_THẬT` Lưu ý về tên chuẩn: IASB đã **đổi tên IAS 8** thành *Basis of Preparation of Financial Statements* (trang chuẩn ghi nhận việc đổi tên gắn với IFRS 18 thay IAS 1). Nhiều tài liệu cũ vẫn gọi là *Accounting Policies, Changes in Accounting Estimates and Errors* — khi dẫn nguồn, nên ghi cả hai tên.

`SUY_LUẬN` Vì sao phân biệt quan trọng: cùng một con số "lợi nhuận tăng", ba nhãn này có ba hệ quả khác nhau. Đổi **chính sách** phải hồi tố (so sánh được với quá khứ); đổi **ước tính** chỉ áp dụng từ nay về sau (không cần hồi tố, và đây là cửa rộng nhất cho việc "làm mượt" lợi nhuận); **sửa lỗi** phải công bố và điều chỉnh. Doanh nghiệp gọi một thay đổi là "ước tính" trong khi bản chất là chính sách là dấu hiệu cần đọc kỹ.

## 2. Doanh thu: nơi bắt đầu của mọi câu chuyện

`SỰ_THẬT` Theo IFRS 15 (IFRS Foundation, trang chuẩn mở `2026-10-26`), nguyên tắc cốt lõi là doanh nghiệp ghi nhận doanh thu để phản ánh việc **chuyển giao hàng hoá/dịch vụ đã cam kết cho khách hàng**, với số tiền phản ánh khoản đối ứng mà doanh nghiệp dự kiến được hưởng. Mô hình gồm năm bước: xác định hợp đồng; xác định nghĩa vụ thực hiện; xác định giá giao dịch; phân bổ giá cho từng nghĩa vụ; và **ghi nhận doanh thu khi nghĩa vụ được thoả mãn bằng việc chuyển giao hàng hoá/dịch vụ — tức khi khách hàng có được quyền kiểm soát**.

`SUY_LUẬN` Bốn kiểu ghi nhận sớm thường gặp, và cách nhận diện:

1. **Ghi nhận khi giao hàng cho kênh phân phối, không phải người dùng cuối.** Nhận diện: doanh thu tăng mạnh nhưng phải thu cũng tăng mạnh; hàng tồn ở nhà phân phối; có chính sách đổi trả/chiết khấu lớn.
2. **Hợp đồng nhiều thành phần được gộp làm một.** Nhận diện: doanh thu ghi hết một lần trong khi nghĩa vụ còn phải thực hiện nhiều năm (bảo trì, nâng cấp).
3. **Doanh thu từ hợp đồng dài hạn ghi theo tiến độ quá lạc quan.** Nhận diện: phải thu theo tiến độ tăng, dòng tiền thu chậm hơn doanh thu (nối Bài 004).
4. **Hoàn nhập dự phòng hoặc hạch toán khoản phải trả thành thu nhập.** Nhận diện: lợi nhuận tăng nhưng không có dòng tiền tương ứng.

`Ý_KIẾN` Ba câu hỏi kiểm nhanh: doanh thu có tương ứng với dòng tiền vào không (Bài 004); phải thu có quay vòng chậm hơn không; và doanh nghiệp có thuyết minh chính sách ghi nhận doanh thu cụ thể hay chỉ một câu chung chung.

## 3. Tài sản: phải thu, tồn kho và giá trị có thể thu hồi

`SỰ_THẬT` Về hàng tồn kho, IAS 2 (IFRS Foundation, mở `2026-10-26`): hàng tồn kho được đo theo **giá thấp hơn** giữa giá gốc và **giá trị thuần có thể thực hiện được**; giá trị thuần có thể thực hiện được là giá bán ước tính trong điều kiện kinh doanh bình thường trừ chi phí hoàn thành ước tính và chi phí cần thiết để bán.

`SỰ_THẬT` Về tổn thất tài sản, IAS 36 (mở `2026-10-26`): **giá trị có thể thu hồi** là giá trị cao hơn giữa (a) giá trị hợp lý trừ chi phí bán và (b) giá trị sử dụng; tài sản không được ghi nhận cao hơn mức cao nhất có thể thu hồi qua sử dụng hoặc bán. `SỰ_THẬT` Cùng trang: giá trị có thể thu hồi của **goodwill**, **tài sản vô hình có thời gian sử dụng không xác định** và **tài sản vô hình chưa sẵn sàng sử dụng** **phải được đánh giá mỗi năm**, và **lỗ tổn thất của goodwill không bao giờ được hoàn nhập**.

`SUY_LUẬN` Bốn "cờ đỏ" đọc được từ số liệu và thuyết minh:

| Cờ đỏ | Dấu hiệu định lượng | Câu hỏi |
|---|---|---|
| Phải thu tăng nhanh hơn doanh thu | DSO tăng liên tiếp 2–3 năm | Khách hàng có trả nổi; dự phòng có đủ |
| Tồn kho tăng nhanh hơn giá vốn | DIO tăng; dự phòng giảm giá mỏng | Hàng có lỗi thời; giá bán có đang giảm |
| Vốn hoá chi phí | Capex tăng nhưng doanh thu không tăng theo; tài sản vô hình tăng | Chi phí này có tạo ra lợi ích tương lai thật không |
| Goodwill không bao giờ giảm | Goodwill giữ nguyên qua nhiều năm, kể cả khi doanh thu mảng mua lại giảm | Có đang bị trì hoãn ghi lỗ không (vì không thể hoàn nhập) |

`SỰ_THẬT` Điểm cuối quan trọng: **lỗ tổn thất goodwill không được hoàn nhập**, và khi đã ghi thì không được xoá. `SUY_LUẬN` Vì quy tắc một chiều đó, ban điều hành có động cơ trì hoãn ghi giảm — đây là suy luận về động cơ, không phải dữ kiện. Cách kiểm: doanh nghiệp báo "hoàn nhập lỗ goodwill" cần được soi ngay, **sau khi** loại trừ hai khả năng hợp lệ: (a) đó thật ra là tài sản **khác goodwill** — IAS 36 cho phép hoàn nhập tổn thất của mọi tài sản khác goodwill (kể cả tài sản vô hình có thời gian sử dụng không xác định) khi nguyên nhân tổn thất được giải quyết, nhưng không vượt giá trị lẽ ra có nếu chưa từng ghi tổn thất; (b) đó là điều chỉnh **sai sót kỳ trước** theo IAS 8, không phải hoàn nhập tổn thất.

## 4. Thước đo do ban điều hành tự định nghĩa (MPM)

`SỰ_THẬT` Theo IFRS 18 (IFRS Foundation, mở `2026-10-26`), chuẩn yêu cầu doanh nghiệp công bố **management-defined performance measures** — được mô tả là "các tiểu tổng thu nhập và chi phí **không do IFRS quy định**, được dùng trong truyền thông công khai để truyền đạt quan điểm của ban điều hành về một khía cạnh hiệu quả tài chính của doanh nghiệp". `SỰ_THẬT` Chuẩn có hiệu lực với kỳ báo cáo năm **bắt đầu từ hoặc sau `2027-01-01`**, cho phép áp dụng sớm.

`CHƯA_BIẾT` Yêu cầu chi tiết về **cách đối chiếu MPM về chỉ tiêu IFRS gần nhất** (bảng đối chiếu từng dòng, xử lý thuế và lợi ích cổ đông thiểu số): toàn văn IFRS 18 nằm sau đăng nhập IFRS Digital nên trong lượt này chỉ đọc được phần mô tả cấp trang và **một nguồn thứ cấp** (RSM UK). Khi soạn bài giảng tiếp theo phải mở chuẩn gốc; trong bài này, phần đối chiếu được trình bày như **thông lệ** và gắn nhãn `SUY_LUẬN`.

`SỰ_THẬT` Không phải tiểu tổng nào cũng là MPM. IFRS 18 loại trừ khỏi yêu cầu MPM một số tiểu tổng thông dụng, gồm lợi nhuận gộp, **"lợi nhuận hoạt động trước khấu hao, phân bổ và tổn thất theo IAS 36"** (tức EBITDA "thuần" theo đúng định nghĩa này), lợi nhuận trước thuế và lợi nhuận từ hoạt động liên tục (nguồn thứ cấp: BDO UK, `2026-09-22`). `SUY_LUẬN` Vì vậy EBITDA đúng bằng tiểu tổng loại trừ này **không** phải MPM; "EBITDA **điều chỉnh**" (cộng lại cổ phiếu thưởng, tái cấu trúc...) thì thường là MPM nếu được dùng trong truyền thông công khai — phải xét từng trường hợp.

`SUY_LUẬN` Vì sao MPM là công cụ tốt cho người đọc: trước đây "EBITDA điều chỉnh" chỉ nằm trong slide hội nghị nhà đầu tư; với kỳ báo cáo năm bắt đầu từ `2027-01-01` (báo cáo năm đầu tiên thường chỉ được công bố vào **đầu 2028**), nó phải được thuyết minh **trong báo cáo tài chính**, kèm đối chiếu về chỉ tiêu IFRS. Nghĩa là người đọc có thể tự kiểm: **khoảng cách giữa MPM và chỉ tiêu IFRS gồm những gì, có lặp lại hằng năm không, và khoản nào thực sự là "một lần"**.

`PHÉP_TÍNH` Ví dụ hư cấu: doanh nghiệp công bố "EBITDA điều chỉnh 500" trong khi EBIT theo IFRS là 300. Cầu nối 200 gồm: khấu hao 150 + chi phí cổ phiếu thưởng 50. Tiểu tổng loại trừ (EBIT + khấu hao) là `300 + 150 = 450`, không phải MPM; phần cộng thêm 50 cổ phiếu thưởng mới biến 500 thành MPM. Ba câu hỏi: (a) chi phí cổ phiếu thưởng có thực sự là "không bằng tiền" khi nó pha loãng cổ đông (Bài 006); (b) khoản điều chỉnh nào lặp lại 3 năm liên tiếp thì không còn là "một lần"; (c) nếu bỏ toàn bộ điều chỉnh, lợi nhuận còn bao nhiêu.

## 5. Ý kiến kiểm toán: đọc đúng ba chữ

`SỰ_THẬT` Theo chuẩn kiểm toán tương ứng (ISA 700, bản Australia ASA 700 dẫn chiếu ISA 700 — AUASB, mở `2026-10-26`): kiểm toán viên đưa **ý kiến không sửa đổi** khi kết luận báo cáo được lập, trên mọi khía cạnh trọng yếu, phù hợp khuôn khổ lập báo cáo tài chính. — `SỰ_THẬT` Theo ISA 705 (ASA 705): có ba loại **ý kiến sửa đổi**: **ý kiến ngoại trừ** khi sai lệch là trọng yếu nhưng **không lan rộng**; **ý kiến trái ngược** khi sai lệch **trọng yếu và lan rộng**; **từ chối đưa ý kiến** khi không thu thập được đủ bằng chứng và ảnh hưởng có thể **trọng yếu và lan rộng**. — `SỰ_THẬT` Theo ISA 706: đoạn "vấn đề cần nhấn mạnh" (emphasis of matter) chỉ nêu một vấn đề đã trình bày hoặc thuyết minh phù hợp, quan trọng cho hiểu biết của người sử dụng, và phải **nói rõ ý kiến không bị sửa đổi** vì vấn đề đó.

`CHƯA_BIẾT` Toàn văn ISA 700/705/706 trên trang IAASB yêu cầu đăng nhập để tải; bài này dẫn qua **ASA 700/705/706** (AUASB, HTML) — `SUY_LUẬN` AUASB công bố các chuẩn ASA tương ứng với ISA, nhưng phần câu chữ đối chiếu ("conforms with…", "enables compliance with…") **chưa mở được** trên trang đã dẫn trong lượt này. Khác biệt câu chữ (ví dụ "financial report" thay "financial statements") chưa được kiểm toàn văn.

`SUY_LUẬN` Cách đọc thực dụng:

- **Không sửa đổi** = không có vấn đề trọng yếu được nêu.
- **Ngoại trừ** = có một vấn đề trọng yếu nhưng giới hạn ở một phần. Phải đọc "cơ sở của ý kiến" để biết phần nào.
- **Trái ngược** = báo cáo sai ở mức lan rộng. Đây là mức nghiêm trọng nhất còn được đưa ý kiến.
- **Từ chối** = kiểm toán viên không đủ bằng chứng. Không có ý kiến nghĩa là **không có gì được xác nhận**.
- **Đoạn nhấn mạnh** (EoM) = không phải ý kiến sửa đổi; nhưng doanh nghiệp có EoM thì nên đọc kỹ vấn đề đó, vì kiểm toán viên thấy cần thiết phải gọi ra.

## 6. Ví dụ số học hư cấu: ba cách "làm đẹp" và lợi nhuận còn lại

`KỊCH_BẢN` Công ty E công bố lợi nhuận sau thuế **100** (thuế suất 20%). Ba thay đổi được thực hiện trong năm, tất cả đều có thể biện minh được bằng lý do hợp lý. Đơn vị: tỷ đồng.

| Thay đổi | Ảnh hưởng trước thuế | Ảnh hưởng sau thuế |
|---|---:|---:|
| Kéo dài thời gian khấu hao tài sản 500 từ 10 năm lên 20 năm | +25 | +20 |
| Đánh giá 40 chi phí phát triển là đã đạt tiêu chí vốn hoá của IAS 38 thay vì chi phí hoá ngay (khấu hao 5 năm) | +32 | +25,6 |
| Hoàn nhập dự phòng 30 vì "không còn rủi ro" | +30 | +24 |

`PHÉP_TÍNH` Khấu hao cũ `500/10 = 50`; khấu hao mới `500/20 = 25`; chênh `25`; sau thuế `25 × 0,8 = 20` (giản lược: coi tài sản mới đưa vào dùng; với tài sản đã khấu hao một phần, thay đổi ước tính được áp từ nay, chia **giá trị còn lại** cho **thời gian còn lại**). Vốn hoá: chênh trước thuế `40 − 8 = 32` (khấu hao 8/năm); sau thuế `25,6`. Hoàn nhập: `30 × 0,8 = 24`.

`PHÉP_TÍNH` Nếu áp cả ba một cách **thận trọng hơn** (khấu hao 10 năm, chi phí hoá ngay, không hoàn nhập), lợi nhuận sau thuế khoảng `100 − 20 − 25,6 − 24 = 30,4`.

`SUY_LUẬN` Đây không phải kết luận "công ty gian lận". Đây là **phép thử độ nhạy**: nếu ba lựa chọn hợp pháp làm lợi nhuận thay đổi khoảng 70% **so với lợi nhuận báo cáo 100** (tức 100 → 30,4; đọc ngược lại là +229%, không phải −70%) thì luận điểm đầu tư dựa trên "lợi nhuận tăng trưởng" phải được viết lại bằng con số đã chuẩn hoá. Cách trình bày trung thực: "lợi nhuận báo cáo 100; lợi nhuận theo cách thận trọng ước khoảng 30–40; khoảng cách do ba ước tính, đã nêu ở thuyết minh".

## 7. Năm câu hỏi khi đọc thuyết minh

1. Ý kiến kiểm toán là loại nào; nếu có "cơ sở của ý kiến", vấn đề nằm ở khoản mục nào?
2. Trong năm có thay đổi chính sách hay ước tính nào; doanh nghiệp gọi nó là gì, và ảnh hưởng định lượng bao nhiêu?
3. Chính sách ghi nhận doanh thu có mô tả cụ thể điều kiện chuyển giao không, hay chỉ một câu chung?
4. Dự phòng phải thu và dự phòng giảm giá hàng tồn kho có tương xứng với tốc độ tăng của phải thu và tồn kho không?
5. Có thước đo do ban điều hành tự định nghĩa nào đang được nhắc trong truyền thông; khoảng cách tới chỉ tiêu IFRS gồm những gì?

## 8. Bài tập (8 câu, 45 phút)

`KỊCH_BẢN` Số liệu hư cấu; đơn vị: tỷ đồng, thuế suất 20% nếu không nói khác.

### Bài 1 (nhớ lại) — ba nhãn
Phân loại ba tình huống: (a) doanh nghiệp đổi cách tính khấu hao từ đường thẳng sang theo sản lượng; (b) doanh nghiệp điều chỉnh thời gian sử dụng hữu ích của máy móc từ 10 xuống 8 năm do dữ liệu vận hành mới; (c) doanh nghiệp phát hiện năm trước ghi thiếu một khoản chi phí 50.

### Bài 2 (vận dụng) — khấu hao
Tài sản 1.200, khấu hao cũ 8 năm, đổi sang 12 năm. Tính chênh lệch lợi nhuận sau thuế và nêu hai câu hỏi phải hỏi.

### Bài 3 (vận dụng) — hàng tồn kho
Hàng tồn kho: giá gốc 100; giá bán ước tính 90; chi phí bán ước tính 10. Tính giá trị thuần có thể thực hiện được và mức trích lập cần thiết.

### Bài 4 (vận dụng) — IAS 36
Một bộ phận có giá trị sổ sách 900; giá trị sử dụng 800; giá trị hợp lý trừ chi phí bán 700. Tính giá trị có thể thu hồi và lỗ tổn thất. Nếu tài sản gây lỗ là **goodwill**, năm sau giá trị phục hồi thì xử lý thế nào?

### Bài 5 (vận dụng, câu cũ xen kẽ) — nối Bài 004
Doanh nghiệp hoàn nhập dự phòng 30, lợi nhuận sau thuế tăng 24. Hỏi: CFO có tăng tương ứng không; giải thích; chỉ tiêu nào trong Bài 004 sẽ phát hiện ra điều này.

### Bài 6 (vận dụng, câu cũ xen kẽ) — nối Bài 006
Đọc thấy dòng "hoàn nhập lỗ tổn thất lợi thế thương mại 40 trong năm". Nêu nhận xét và căn cứ chuẩn mực.

### Bài 7 (chuyển giao) — soi đoạn thuyết minh
Cho đoạn: "Doanh thu được ghi nhận khi hàng hoá được giao cho khách hàng. Chi phí phát triển sản phẩm mới được vốn hoá và phân bổ trong 7 năm. Thời gian khấu hao nhà xưởng được điều chỉnh từ 15 lên 25 năm trong năm nay. Công ty tin rằng các ước tính này là hợp lý." Nêu **ba** câu hỏi cần hỏi và **một** con số cần tính.

### Bài 8 (chuyển giao) — MPM
Doanh nghiệp công bố "lợi nhuận hoạt động điều chỉnh 420", EBIT theo IFRS 260. Cầu nối gồm: khấu hao tài sản vô hình mua lại 80, chi phí tái cấu trúc 50, chi phí cổ phiếu thưởng 30. Hỏi: cầu nối có khớp không; khoản nào nên coi là chi phí thật; nếu bỏ toàn bộ điều chỉnh thì con số là bao nhiêu.

## 9. Đáp án

### Bài 1

`SỰ_THẬT` (a) Đổi **phương pháp khấu hao** (ví dụ từ đường thẳng sang theo sản lượng) là **thay đổi ước tính kế toán**, áp dụng **từ nay, không hồi tố** — không phải thay đổi chính sách. Cơ sở: IAS 16 yêu cầu xem xét lại phương pháp khấu hao, thời gian hữu ích và giá trị còn lại mỗi năm; IAS 8 xếp thay đổi phương pháp khấu hao vào nhóm thay đổi ước tính. (b) Điều chỉnh **thời gian sử dụng hữu ích** cũng là **thay đổi ước tính** → áp dụng từ nay. (c) Phát hiện năm trước ghi thiếu chi phí là **sai sót kỳ trước** → điều chỉnh hồi tố và công bố.
`SUY_LUẬN` Muốn một ví dụ **thay đổi chính sách** đúng nghĩa (áp dụng hồi tố) thì dùng: đổi công thức tính giá gốc hàng tồn kho (FIFO sang bình quân gia quyền), hoặc đổi mô hình giá gốc sang mô hình đánh giá lại của IAS 16.
`SUY_LUẬN` Câu này kiểm: bạn có phân biệt "đổi ước tính" với "đổi chính sách" — đây là chỗ rất dễ nhầm, kể cả người có kinh nghiệm.

### Bài 2

`PHÉP_TÍNH` Khấu hao cũ `1.200/8 = 150`; mới `1.200/12 = 100`; chênh trước thuế 50; sau thuế `50 × 0,8 = 40`.
`SUY_LUẬN` Hai câu hỏi: (a) dữ liệu nào chứng minh tài sản dùng được 12 năm (nhật ký bảo trì, tuổi thọ thiết bị); (b) nếu giữ 8 năm thì lợi nhuận giảm 40 — doanh nghiệp có công bố ảnh hưởng này không.

### Bài 3

`PHÉP_TÍNH` Giá trị thuần có thể thực hiện được = `90 − 10 = 80`; trích lập = `100 − 80 = 20`.
`SUY_LUẬN` Câu này kiểm: bạn có nhớ IAS 2 dùng **giá thấp hơn** giữa giá gốc và NRV, và NRV trừ **chi phí bán**.

### Bài 4

`PHÉP_TÍNH` Giá trị có thể thu hồi = `max(800, 700) = 800`; lỗ tổn thất = `900 − 800 = 100`.
`SUY_LUẬN` Nếu là goodwill: `SỰ_THẬT` theo IAS 36, lỗ tổn thất goodwill **không bao giờ được hoàn nhập**, nên năm sau giá trị phục hồi cũng **không** được ghi tăng. Câu này kiểm: bạn có nhớ quy tắc một chiều của goodwill.

### Bài 5

`SUY_LUẬN` CFO **không** tăng tương ứng: hoàn nhập dự phòng là khoản không phải tiền, lại **cộng** vào lợi nhuận; nếu ở phương pháp gián tiếp thì nó bị trừ ra khi đi từ lợi nhuận sang CFO. Chỉ tiêu phát hiện: **tỷ lệ chuyển hoá tiền mặt** giảm (Bài 004) và dòng "điều chỉnh khác" trong cầu nối.

### Bài 6

`SUY_LUẬN` Nhận xét: đây là dấu hiệu **không đúng chuẩn** — IAS 36 quy định lỗ tổn thất của goodwill không được hoàn nhập. Căn cứ: trang IAS 36 của IFRS Foundation (đã mở trong lượt này). Cần kiểm: (a) khoản đó có phải goodwill không hay tài sản khác — mọi tài sản khác goodwill, kể cả tài sản vô hình không xác định thời hạn, được hoàn nhập khi nguyên nhân tổn thất được giải quyết, trong giới hạn giá trị lẽ ra có nếu chưa từng ghi tổn thất; (b) ý kiến kiểm toán có nêu vấn đề này không.

### Bài 7

`SUY_LUẬN` Ba câu hỏi: (1) "giao cho khách hàng" nghĩa là giao cho người dùng cuối hay nhà phân phối; có điều kiện đổi trả/chiết khấu không; (2) 7 năm phân bổ chi phí phát triển dựa trên căn cứ nào, và nếu chi phí hoá ngay thì lợi nhuận giảm bao nhiêu; (3) điều chỉnh khấu hao từ 15 lên 25 năm làm lợi nhuận tăng bao nhiêu.
`PHÉP_TÍNH` Con số cần tính: ảnh hưởng của việc kéo dài khấu hao. Nếu nhà xưởng có nguyên giá X thì chênh mỗi năm là `X/15 − X/25 = X × (1/15 − 1/25) = X × 0,02667`; ví dụ X = 1.500 → chênh 40 trước thuế, 32 sau thuế.

### Bài 8

`PHÉP_TÍNH` Cầu nối: `80 + 50 + 30 = 160`; `260 + 160 = 420` — khớp.
`SUY_LUẬN` Khoản nên coi là chi phí thật: **chi phí cổ phiếu thưởng 30** (pha loãng cổ đông — Bài 006) và **khấu hao tài sản vô hình mua lại 80** (đã trả tiền thật khi mua). Chi phí tái cấu trúc 50: là chi phí thật nếu lặp lại, chỉ được coi là "một lần" nếu thật sự không lặp. Nếu bỏ toàn bộ điều chỉnh: 260 (chính là EBIT IFRS).
`SUY_LUẬN` Câu này kiểm: bạn có đọc được cầu nối và biết khoản nào không thể "biến mất".

### Đáp án phần ôn bài cũ

1. CFO **giảm 100** (Bài 004).
2. Goodwill hình thành khi giá mua vượt giá trị hợp lý của tài sản/nợ xác định được; nếu không đạt kỳ vọng thì bị ghi giảm (impairment) và lỗ đi vào lãi lỗ (Bài 006).
3. Ví dụ: mua mạnh khi giá cao kỷ lục rồi dừng khi giá thấp; mua để bù pha loãng ESOP; mua bằng nợ trong khi FCF âm (Bài 006).
4. Vì số cổ phiếu lưu hành có thể tăng nhanh hơn lợi nhuận (Bài 006).

## 10. Lỗi thường gặp

- Bỏ qua thuyết minh vì "dài và toàn chữ", rồi tranh luận về con số mà không biết con số được tạo ra thế nào.
- Nhầm "thay đổi ước tính" với "thay đổi chính sách" — hệ quả hồi tố khác hẳn.
- Đọc ý kiến kiểm toán chỉ ở dòng kết luận, không đọc "cơ sở của ý kiến".
- Nghĩ "đoạn nhấn mạnh" là ý kiến sửa đổi (không phải).
- Tin "EBITDA điều chỉnh" mà không đọc cầu nối về chỉ tiêu IFRS.
- Thấy dự phòng giảm là "quản trị tốt" mà không xét dự phòng có tương xứng với rủi ro.
- Cho rằng goodwill giảm giá rồi phục hồi thì được hoàn nhập (không được).
- Đọc báo cáo theo chuẩn IFRS nhưng áp nguyên vào hồ sơ lập theo chuẩn khác (VAS hoặc US GAAP) — khác biệt về ghi nhận và thuyết minh là thật.

## 11. Ranh giới an toàn

- Bài này **không** kết luận gian lận hay chất lượng quản trị của bất kỳ doanh nghiệp nào; chỉ dạy câu hỏi và cách kiểm.
- Không thay thế kiểm toán độc lập, không thay thế tư vấn pháp lý.
- Mọi ví dụ số học là hư cấu; không suy ra "công thức tìm cổ phiếu".
- Khi áp vào hồ sơ thật: phải mở báo cáo gốc, ghi kỳ, tiền tệ, đơn vị và chuẩn mực áp dụng; nếu không mở được thì ghi `CHƯA_BIẾT`.

## 12. Điều tôi vẫn chưa hiểu

1. Bạn muốn luyện với báo cáo lập theo **VAS** (Việt Nam) hay **IFRS** trước? Khác biệt về thuyết minh và cách ghi nhận là đáng kể.
2. Bạn có cần một bài riêng về **thuế hoãn lại** (deferred tax) — chỗ hay bị bỏ qua nhưng ảnh hưởng lớn tới lợi nhuận?
3. Bạn muốn tôi làm một **checklist 20 câu** dạng bảng tính để bạn tự điền khi đọc một báo cáo thật không?
4. Bạn đang đọc báo cáo tài chính bằng tiếng Việt hay tiếng Anh?

## 13. Nguồn Internet đã mở

<details>
<summary>Nguồn chi tiết và lịch sử kiểm — giữ mốc dữ liệu gốc</summary>

Tất cả mở ngày `2026-10-26`; câu chữ trích dẫn giữ nguyên tiếng Anh để đối chiếu.

- [IFRS 18 Presentation and Disclosure in Financial Statements — IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/) — HTTP 200; ban hành `2024-04`; hiệu lực kỳ báo cáo năm từ hoặc sau `2027-01-01`. Cung cấp mô tả MPM ("subtotals of income and expenses not specified by IFRS Accounting Standards that are used in public communications…"). **Giới hạn**: toàn văn chuẩn nằm sau đăng nhập IFRS Digital; định nghĩa Appendix A và các đoạn yêu cầu đối chiếu **CHƯA** mở được.
- [RSM UK — IFRS 18: Understanding MPM](https://www.rsmuk.com/insights/bridging-the-gaap/ifrs-18-understanding-management-defined-performance-measures) — HTTP 200; **nguồn thứ cấp**, không ghi ngày. Dùng cho yêu cầu đối chiếu (bảng đối chiếu về chỉ tiêu IFRS gần nhất, một ghi chú duy nhất, ảnh hưởng thuế và cổ đông thiểu số) — phần này gắn nhãn `SUY_LUẬN` trong bài.
- [IFRS 15 Revenue from Contracts with Customers — IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/) — HTTP 200; ban hành `2014-05`; hiệu lực `2018-01-01`. Cung cấp nguyên tắc cốt lõi và mô hình năm bước, gồm điều kiện chuyển giao quyền kiểm soát.
- [IAS 36 Impairment of Assets — IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ias-36-impairment-of-assets/) — HTTP 200. Cung cấp định nghĩa giá trị có thể thu hồi (cao hơn giữa giá trị hợp lý trừ chi phí bán và giá trị sử dụng); danh mục phải đánh giá hằng năm (goodwill, tài sản vô hình không xác định thời hạn, tài sản chưa sẵn sàng sử dụng); quy tắc lỗ goodwill không được hoàn nhập, còn tổn thất của **tài sản khác** được hoàn nhập khi nguyên nhân được giải quyết, không vượt giá trị lẽ ra có nếu chưa ghi tổn thất.
- [IAS 2 Inventories — IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/) — HTTP 200. Cung cấp nguyên tắc đo theo giá thấp hơn giữa giá gốc và giá trị thuần có thể thực hiện được, cùng định nghĩa NRV.
- [IAS 8 Basis of Preparation of Financial Statements — IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ias-8-basis-of-preparation-of-financial-statements/) — HTTP 200. Cung cấp phạm vi (chính sách, thay đổi chính sách, thay đổi ước tính, sửa lỗi), quy tắc áp dụng hồi tố cho thay đổi chính sách, định nghĩa sai sót kỳ trước, và việc IASB đổi tên IAS 8 (gắn với IFRS 18 thay IAS 1).
- [IAS 38 Intangible Assets — IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/) — HTTP 200. Cung cấp: chi phí nghiên cứu ghi vào chi phí; chi phí phát triển đạt tiêu chí quy định được ghi nhận là nguyên giá tài sản vô hình.
- [BDO UK — IFRS 18 Series Part 2: Management-defined Performance Measures](https://www.bdo.co.uk/en-gb/insights/audit-and-assurance/financial-reporting-solutions/ifrs-18-series-part-2-management-defined-performance-measures) — HTTP 200; đăng `2026-09-22`; **nguồn thứ cấp**. Dùng cho danh sách tiểu tổng được loại trừ khỏi MPM (mục 4).
- [ASA 700 — AUASB](https://standards.auasb.gov.au/node/1975), [ASA 705 — AUASB](https://standards.auasb.gov.au/node/393), [ASA 706 — AUASB](https://standards.auasb.gov.au/asa-706-jun-2020) — HTTP 200. Dùng cho bốn loại ý kiến (không sửa đổi; ngoại trừ; trái ngược; từ chối) và định nghĩa đoạn nhấn mạnh. `SUY_LUẬN` AUASB công bố ASA tương ứng với ISA; câu chữ "conforms with…" nằm ở phần đầu bản chuẩn và **chưa mở được** trên các trang đã dẫn trong lượt này. **Giới hạn**: toàn văn ISA trên trang IAASB yêu cầu đăng nhập để tải, nên không trích trực tiếp ISA.
- `CHƯA_BIẾT` Ví dụ thuyết minh chính sách kế toán của **doanh nghiệp thật** ở dạng HTML đọc được: trong lượt này không mở được (báo cáo thường niên thường là PDF; EDGAR bị chặn tự động). Vì vậy bài dùng **thuyết minh giả lập tự viết** và ghi rõ là ví dụ minh hoạ. Cách xác minh đề nghị: mở 10-K/20-F bằng trình duyệt, tìm mục "Note — Significant Accounting Policies".

**Trạng thái kiểm nguồn**: đã qua một lượt `source-fact-checker` độc lập ngày `2026-10-26`, kết luận **KHÔNG ĐẠT** với **1 lỗi nghiêm trọng** — đáp án Bài 1(a) phân loại sai: đổi **phương pháp khấu hao** là **thay đổi ước tính** (IAS 16/IAS 8), không phải thay đổi chính sách, nên **không hồi tố**. Đã sửa cùng 4 lỗi mức "cần sửa" (một ký tự lạ trong câu, mâu thuẫn "ba/bốn loại ý kiến", câu chữ AUASB chưa kiểm được, tách nhãn cho nhận định về động cơ). Lượt review sau đó cùng ngày sửa thêm: phạm vi hoàn nhập tổn thất theo IAS 36 (chỉ goodwill bị cấm), cách diễn đạt vốn hoá chi phí phát triển theo IAS 38, ngoại lệ MPM của IFRS 18 cho EBITDA "thuần", mốc báo cáo năm đầu tiên theo IFRS 18, và bỏ nguồn IFRS 9 không dùng trong bài. Bản hiện tại **chưa có biên bản mới** cho hash sau khi sửa. Các dẫn chuẩn mực trong bài đều trích từ trang IFRS Foundation mở ngày `2026-10-26`, trừ phần ghi rõ là nguồn thứ cấp (RSM UK cho yêu cầu đối chiếu MPM).


</details>
