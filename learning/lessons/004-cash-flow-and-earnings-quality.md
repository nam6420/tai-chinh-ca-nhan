# Bài 004: Dòng tiền và chất lượng lợi nhuận

- Ngày: `2026-10-26`
- Chốt dữ liệu lúc: `2026-10-26 09:02 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Dựng lại được cầu nối từ lợi nhuận kế toán sang dòng tiền hoạt động; tính và đọc được tỷ lệ chuyển hoá tiền mặt qua nhiều năm; phân biệt ba định nghĩa dòng tiền tự do đang lưu hành; tính chu kỳ chuyển đổi tiền mặt và biết khi nào nó cảnh báo điều xấu; nêu được ba câu hỏi phải hỏi khi lợi nhuận và tiền lệch nhau.
- Thời lượng: 35 phút đọc + 40 phút bài tập (2 phiên)
- Bài trước liên quan: [Bài 001](001-business-financial-statements.md) (ba báo cáo), [Bài 003](003-business-quality-moat-and-roic.md) (ROIC)
- Câu hỏi cốt lõi: **Lợi nhuận kế toán này có chuyển thành tiền không, và phần nào là tiền thật?**

> Đây là bài học nền tảng toàn cầu, không phải khuyến nghị mua, bán hay nắm giữ chứng khoán. Mọi ví dụ số học đều là doanh nghiệp hư cấu, trừ mục 4 có một ví dụ doanh nghiệp thật (đã đối chiếu với báo cáo 10-K gốc nộp SEC). Bài này kế thừa Bài 001 (cách ba báo cáo nối với nhau) và chuẩn bị cho Bài 005 (nợ) và Bài 010 (chi phí vốn).

## Hiểu bài này trong 1 phút

`SUY_LUẬN` Một người bán hàng ghi nhận doanh thu 100 triệu khi giao hàng, nhưng khách trả tiền sau 90 ngày. Trong 90 ngày đó, sổ sách đã có lợi nhuận, nhưng tài khoản ngân hàng thì chưa có đồng nào. Nếu người đó phải trả lương và tiền nhập hàng ngay trong tháng này, họ có thể **có lãi trên giấy mà vẫn vỡ nợ**.

Với doanh nghiệp cũng vậy: lợi nhuận là **một quy ước kế toán** về việc ghi nhận doanh thu và chi phí trong kỳ; tiền là **thứ không thể tranh cãi**. Câu hỏi của bài này không phải "công ty lãi bao nhiêu" mà là **"bao nhiêu phần của số lãi đó đã thành tiền, và phần chưa thành tiền đang nằm ở đâu"**.

> Câu cần nhớ: **Lợi nhuận là ý kiến có quy tắc; tiền là sự thật. Khi hai thứ lệch nhau, chỗ lệch chính là câu chuyện.**

## Ôn bài cũ (5 phút, làm trước khi đọc tiếp)

Trả lời bằng lời của bạn, không nhìn tài liệu. Đáp án ở mục 9, cuối bài.

1. Trong ba báo cáo tài chính, báo cáo nào cho biết doanh nghiệp **đã thực thu** tiền trong kỳ?
2. Nếu một doanh nghiệp bán chịu, khoản phải thu tăng lên thì tài sản tăng hay giảm? Đối ứng bên kia của bút toán là gì?
3. ROIC của Bài 003 được tính bằng công thức nào, và mẫu số lấy giá trị đầu kỳ hay cuối kỳ?
4. Nêu một lý do khiến ROIC cao **chưa chắc** là doanh nghiệp tốt.

## Bài này làm gì và chưa làm gì

| Bài này làm | Bài này chưa làm |
|---|---|
| Dạy cầu nối lợi nhuận → dòng tiền hoạt động, bằng số học tái lập được | Không kết luận doanh nghiệp cụ thể nào "tốt" hay "xấu" |
| Cho ba công cụ đo chất lượng lợi nhuận: chuyển hoá tiền mặt, chu kỳ tiền mặt, dòng tiền tự do | Không dạy cách phát hiện gian lận kế toán có chủ đích (Bài 007) |
| Chỉ ra vì sao dòng tiền tự do có nhiều định nghĩa và mỗi định nghĩa trả lời câu hỏi khác nhau | Không định giá doanh nghiệp (Đợt 2) |
| Dạy cách đọc dòng tiền của doanh nghiệp thật qua một ví dụ đã đối chiếu với 10-K gốc | Không dạy dựng mô hình tài chính ba báo cáo |

## Cách chia phiên và chọn phần cốt lõi

**Bài cốt lõi trong bộ bài tập:** 1, 2, 7. Các câu còn lại là luyện thêm; không bỏ kiến thức bắt buộc của thân bài. Phiên A làm câu 1, 2; phiên B làm câu 7.

`Ý_KIẾN` Phiên A: mục 1, 2.1 và ví dụ mục 3; tự dựng cầu nối lợi nhuận–tiền. Phiên B: chu kỳ tiền mặt, các định nghĩa FCF và ví dụ thật; chỉ sang tiếp khi nói được mỗi thước đo trả lời câu hỏi gì.

Làm câu cốt lõi theo mục tiêu phiên trước khi xem đáp án; câu xen kẽ/chuyển giao kiểm hiểu sâu. Có thể dừng giữa bài; thời lượng ban đầu chưa được đo với người học. [Bảng thực hành và hai bài ôn](../practice/research-and-model-worksheets.md).

## 1. Vì sao lợi nhuận và tiền lại lệch nhau

`SỰ_THẬT` Theo IAS 7 của IFRS Foundation (trang chuẩn, mở ngày `2026-10-26`), báo cáo lưu chuyển tiền tệ chia dòng tiền của một kỳ thành **ba loại hoạt động**: hoạt động kinh doanh (operating), đầu tư (investing) và tài chính (financing). Chuẩn cho phép trình bày dòng tiền hoạt động kinh doanh theo **phương pháp trực tiếp** (liệt kê các khoản thu, chi tiền gộp) hoặc **phương pháp gián tiếp** (điều chỉnh lợi nhuận bằng các khoản không phải tiền và các thay đổi vốn lưu động).

`SỰ_THẬT` Cùng trang chuẩn này: các giao dịch đầu tư và tài chính **không dùng tiền** (ví dụ mua tài sản bằng cách phát hành cổ phiếu) bị loại khỏi báo cáo lưu chuyển tiền tệ nhưng phải **thuyết minh riêng**; doanh nghiệp cũng phải thuyết minh thành phần tiền và tương đương tiền, và đối chiếu số trên báo cáo lưu chuyển tiền tệ với số trên bảng cân đối kế toán.

Ba nguồn gây lệch giữa lợi nhuận và tiền:

1. **Khấu hao và phân bổ** — chi phí được trừ khỏi lợi nhuận nhưng không có tiền ra trong kỳ đó. Vì vậy khi đi từ lợi nhuận sang tiền, ta **cộng lại** khấu hao.
2. **Thay đổi vốn lưu động** — phải thu, tồn kho, phải trả. Bán chịu làm lợi nhuận tăng nhưng tiền chưa về; tăng tồn kho làm tiền ra mà chưa thành chi phí; kéo dài thời gian trả nhà cung cấp làm tiền còn lại trong két nhưng không phải lợi nhuận.
3. **Các khoản bất thường và ước tính** — dự phòng, đánh giá lại, lãi/lỗ chưa thực hiện.

`PHÉP_TÍNH` **Cầu nối cơ bản (phương pháp gián tiếp, dạng rút gọn cho người mới)**:

```text
Dòng tiền hoạt động (CFO)
  = Lợi nhuận sau thuế
  + Khấu hao và phân bổ
  − Tăng phải thu khách hàng (hoặc + giảm)
  − Tăng hàng tồn kho (hoặc + giảm)
  + Tăng phải trả người bán (hoặc − giảm)
  ± Các khoản điều chỉnh khác
```

`SỰ_THẬT` Lưu ý quan trọng về phân loại: từ khi IFRS 18 có hiệu lực với kỳ báo cáo năm bắt đầu từ hoặc sau `2027-01-01`, IAS 7 được sửa để buộc doanh nghiệp **dùng tiểu tổng lợi nhuận hoạt động (operating profit) làm điểm xuất phát** cho phương pháp gián tiếp, kèm yêu cầu mới về phân loại dòng tiền lãi vay và cổ tức (nguồn: trang IAS 7, mục Standard history, mở `2026-10-26`). `SỰ_THẬT` Với doanh nghiệp không có hoạt động kinh doanh chính là đầu tư hay cho vay, **lãi vay đã trả** xếp vào dòng tiền **tài chính**, lãi và cổ tức nhận được xếp vào **đầu tư**, cổ tức đã trả xếp vào **tài chính** — không còn được để trong dòng tiền hoạt động (nguồn thứ cấp: BDO, `2026-10-13`). Vì vậy khi báo cáo đổi sang IFRS 18, **điểm bắt đầu của cầu nối sẽ khác** báo cáo bạn quen đọc hôm nay. Đây là lý do phải ghi rõ "cầu nối này bắt đầu từ chỉ tiêu nào" mỗi khi trình bày.

### Cạm bẫy số 1: lợi nhuận là ước tính, tiền là quan sát

`SUY_LUẬN` Doanh thu ghi nhận khi quyền kiểm soát hàng hoá/dịch vụ chuyển giao, không phải khi thu tiền. Ước tính nằm rải rác: mức dự phòng phải thu khó đòi, thời gian khấu hao, giá trị tồn kho, mức dự phòng bảo hành. Mỗi ước tính đều có một khoảng hợp lý; người đọc không cần biết ước tính "đúng" là bao nhiêu, chỉ cần biết **ước tính đang nghiêng về phía nào và đã đổi qua các năm ra sao**.

## 2. Ba thước đo chất lượng lợi nhuận

### 2.1 Tỷ lệ chuyển hoá tiền mặt

`PHÉP_TÍNH` Công thức dùng trong bài này, và phải ghi rõ đã dùng biến thể nào:

```text
Tỷ lệ chuyển hoá tiền mặt = Dòng tiền hoạt động (CFO) / Lợi nhuận sau thuế
```

`Ý_KIẾN` Có nhiều biến thể (chia cho NOPAT, chia cho EBITDA, dùng trung bình nhiều năm). Điều quan trọng không phải chọn công thức "chuẩn" mà là **giữ nguyên một công thức khi so sánh giữa các năm và các doanh nghiệp** — đúng tinh thần bài học về ROIC ở Bài 003.

`Ý_KIẾN` Ba mốc dưới đây là **quy ước thực hành** để phát hiện chỗ cần đọc tiếp, không phải chuẩn mực kế toán:

- Xấp xỉ 100% trong nhiều năm: lợi nhuận chuyển thành tiền đều đặn.
- Thường xuyên dưới 80% kèm phải thu/tồn kho tăng nhanh: lợi nhuận đang bị "giam" trong bảng cân đối. Cần hỏi: bán cho ai, điều kiện thanh toán thế nào, có phải nới lỏng điều kiện bán hàng để đạt chỉ tiêu?
- Trên 120% kéo dài: có thể tốt (thu tiền tốt, khách trả trước) hoặc xấu (đang kéo dài thời gian trả nhà cung cấp, hoặc cắt đầu tư cần thiết). Phải xem tiếp phần chu kỳ tiền mặt và chi tiêu vốn.

### 2.2 Chu kỳ chuyển đổi tiền mặt

`PHÉP_TÍNH` Ba vòng quay và chu kỳ:

```text
DSO (số ngày thu tiền)        = Phải thu bình quân / Doanh thu × 365
DIO (số ngày tồn kho)         = Tồn kho bình quân / Giá vốn hàng bán × 365
DPO (số ngày trả người bán)   = Phải trả người bán bình quân / Giá vốn hàng bán × 365

Chu kỳ chuyển đổi tiền mặt (CCC) = DSO + DIO − DPO
```

CCC là số ngày trung bình doanh nghiệp phải "cầm" tiền của mình cho hoạt động kinh doanh trước khi thu lại. CCC dài hơn nghĩa là cần nhiều vốn lưu động hơn cho cùng mức doanh thu — và thường là lý do doanh nghiệp phải đi vay.

`SUY_LUẬN` Ba cách đọc CCC:

- **So với chính mình qua nhiều năm** quan trọng hơn so với người khác, vì cơ cấu thương lượng với nhà cung cấp và khách hàng rất khác nhau giữa các ngành.
- CCC giảm nhờ **DPO tăng vọt** không phải là cải thiện vận hành — đó là dùng tiền của nhà cung cấp. Khi nhà cung cấp không chịu nổi nữa, CCC sẽ bật lại.
- CCC tăng do **DIO tăng** thường là dấu hiệu bán chậm hoặc chuẩn bị cho đơn hàng lớn; phải đọc thuyết minh hàng tồn kho để phân biệt.

### 2.3 Dòng tiền tự do (FCF) và câu hỏi "capex nào là duy trì"

`PHÉP_TÍNH` Ba định nghĩa thường gặp, từ hẹp đến rộng:

```text
FCF (hẹp, phổ biến nhất) = CFO − Chi tiêu vốn (capex)
FCF (sau thanh toán thuê) = CFO − capex − Tiền trả nợ gốc thuê tài sản
FCF cho doanh nghiệp (FCFF) ≈ CFO + Lãi vay sau thuế − capex   (cách ước lượng nhanh)
```

`SUY_LUẬN` Điều kiện của công thức FCFF nhanh: chỉ **cộng lại lãi vay** khi lãi vay đã trả đang nằm **trong CFO** (thường gặp với US GAAP, và với IFRS trước IFRS 18 nếu doanh nghiệp chọn xếp lãi vay vào hoạt động kinh doanh). Nếu lãi vay đã nằm ở dòng tiền tài chính — bắt buộc với đa số doanh nghiệp khi áp dụng IFRS 18 — thì CFO đã "sạch" lãi vay và cộng lại là **tính trùng**. Luôn mở báo cáo xem lãi vay đã trả nằm ở dòng nào trước khi dùng công thức.

`SUY_LUẬN` Chênh lệch giữa các định nghĩa có thể rất lớn với doanh nghiệp thuê nhiều tài sản (bán lẻ, hàng không, khách sạn). Theo **IFRS 16**, phần trả gốc nợ thuê nằm ở dòng tiền **tài chính**, nên FCF "hẹp" **bỏ qua** khoản tiền thuê phải trả hằng năm, trong khi đó là chi phí thật. `SỰ_THẬT` Theo **US GAAP** (ASC 842-20-45-5), tiền trả cho **thuê hoạt động** lại nằm **trong dòng tiền hoạt động**; chỉ thuê tài chính mới tách gốc sang tài chính (nguồn thứ cấp: Deloitte DART). Vì vậy cùng một hợp đồng thuê, FCF "hẹp" theo US GAAP đã trừ tiền thuê còn theo IFRS thì chưa. Đây là lý do khi so sánh hai doanh nghiệp phải dùng **cùng định nghĩa** và biết **chuẩn kế toán** của từng bên.

`SỰ_THẬT` Báo cáo tài chính **không** tách sẵn capex thành hai phần. `Ý_KIẾN` **Capex duy trì** (maintenance capex) là phần chi tiêu vốn tối thiểu để giữ năng lực hiện tại; **capex mở rộng** là phần tăng thêm. Đây là một trong những chỗ người đọc phải tự ước lượng và ghi rõ giả định. Nếu không tách được, hãy ghi `CHƯA_BIẾT` và dùng cách thay thế: so capex với khấu hao nhiều năm (capex xấp xỉ khấu hao thường là mức duy trì, nhưng không phải quy tắc).

## 3. Ví dụ số học hư cấu: cùng lãi 120, một doanh nghiệp có tiền, một doanh nghiệp không

`KỊCH_BẢN` Hai doanh nghiệp hư cấu, cùng năm, đơn vị: tỷ đồng.

| Chỉ tiêu | Công ty A | Công ty C |
|---|---:|---:|
| Lợi nhuận sau thuế | 120 | 120 |
| Khấu hao | 40 | 20 |
| Phải thu khách hàng tăng | 50 | 120 |
| Hàng tồn kho tăng | 30 | 40 |
| Phải trả người bán tăng | 20 | 0 |
| Chi tiêu vốn (capex) | 70 | 70 |

`PHÉP_TÍNH` Cầu nối:

- Công ty A: `120 + 40 − 50 − 30 + 20 = 100` → CFO 100.
- Công ty C: `120 + 20 − 120 − 40 + 0 = −20` → CFO **âm 20**.

`PHÉP_TÍNH` Tỷ lệ chuyển hoá tiền mặt: A = `100 / 120 = 83,3%`; C = `−20 / 120 = −16,7%`.

`PHÉP_TÍNH` FCF hẹp: A = `100 − 70 = 30`; C = `−20 − 70 = −90`.

`SUY_LUẬN` Hai doanh nghiệp báo cùng một con số lãi, nhưng A tạo ra 30 tỷ tiền mặt ròng còn C phải huy động thêm 90 tỷ để duy trì hoạt động. Với C, câu hỏi tiếp theo không phải "lãi có tăng không" mà là **"lấy tiền ở đâu để bù 90 tỷ này"** — vay, phát hành cổ phiếu, hay bán tài sản? Đó chính là nội dung Bài 005.

`SUY_LUẬN` Chú ý cách C "có lãi" một cách hợp pháp: bán chịu nhiều hơn (phải thu +120). Không có gì sai về kế toán nếu doanh thu đã thực sự chuyển giao. Nhưng nếu doanh thu tăng nhờ **nới điều kiện thanh toán** cho khách yếu, lợi nhuận năm nay là lợi nhuận đi vay từ năm sau.

## 4. Ví dụ doanh nghiệp thật: Apple, ba năm tài chính

`SỰ_THẬT` Số dưới đây lấy từ bảng dòng tiền hợp nhất trong **báo cáo 10-K FY2025 của Apple nộp SEC** (mở ngày `2026-10-26`, HTTP 200 khi gửi User-Agent khai báo; khớp dữ liệu XBRL trên `data.sec.gov` và trang tổng hợp `stockanalysis.com`), đơn vị **triệu USD**, năm tài chính **tháng 10 → tháng 9** (FY2025 kết thúc ngày 27/09/2025). Apple lập báo cáo theo **US GAAP**, không phải IFRS. Ba dòng "tài sản/nợ hoạt động khác" của 10-K được gộp thành một dòng ròng trong bảng dưới; phần tách ở ngay sau bảng.

| Chỉ tiêu (triệu USD) | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Lợi nhuận sau thuế | 96.995 | 93.736 | 112.010 |
| Khấu hao và phân bổ | 11.519 | 11.445 | 11.698 |
| Chi phí cổ phiếu thưởng (SBC) | 10.833 | 11.688 | 12.863 |
| Điều chỉnh khác ("Other" trong 10-K) | −2.227 | −2.266 | −89 |
| Thay đổi phải thu | −1.688 | −3.788 | −6.682 |
| Thay đổi tồn kho | −1.618 | −1.046 | +1.400 |
| Thay đổi phải trả người bán | −1.889 | +6.020 | +902 |
| Thay đổi tài sản và nợ hoạt động khác (ròng) | −1.382 | +2.465 | −20.620 |
| **Dòng tiền hoạt động (CFO)** | **110.543** | **118.254** | **111.482** |
| Chi tiêu vốn | 10.959 | 9.447 | 12.715 |

`PHÉP_TÍNH` Cầu nối FY2025 khớp số: `112.010 + 11.698 + 12.863 − 89 − 6.682 + 1.400 + 902 − 20.620 = 111.482`.

`PHÉP_TÍNH` Tách dòng ròng −20.620 của FY2025 theo 10-K: phải thu khác từ nhà cung cấp (vendor non-trade receivables) `−347`; tài sản ngắn và dài hạn khác `−9.197`; **nợ phải trả ngắn và dài hạn khác `−11.076`** → `−347 − 9.197 − 11.076 = −20.620`. Kiểm FY2024: `−1.356 − 11.731 + 15.552 = +2.465`; FY2023: `+1.271 − 5.684 + 3.031 = −1.382`. Tất cả khớp.

`PHÉP_TÍNH` Tỷ lệ chuyển hoá tiền mặt: FY2023 = `110.543 / 96.995 = 114,0%`; FY2024 = `118.254 / 93.736 = 126,2%`; FY2025 = `111.482 / 112.010 = 99,5%`.

`PHÉP_TÍNH` FCF hẹp: FY2023 = 99.584; FY2024 = 108.807; FY2025 = 98.767 (triệu USD).

`SUY_LUẬN` Ba điều đáng học từ ví dụ này:

1. **Lợi nhuận tăng mạnh nhưng CFO giảm** ở FY2025. Phần lớn chênh lệch nằm ở các dòng "tài sản và nợ hoạt động khác" (−20.620), trong đó hơn một nửa là **nợ phải trả khác giảm** (−11.076), tức tiền đã chi để trả một nghĩa vụ ghi nhận từ trước; phải thu khách hàng tăng (−6.682) cũng góp phần. `SỰ_THẬT` Thuyết minh thuế của 10-K ghi: quý IV năm 2024 Apple ghi một khoản chi phí thuế một lần **10,2 tỷ USD** (ròng), tương ứng **15,8 tỷ USD phải trả cho Ireland** qua việc giải phóng tiền ký quỹ theo quyết định State Aid. `SUY_LUẬN` Chi phí đã nằm trong lợi nhuận FY2024 còn tiền có thể ra ở FY2025 — một ứng viên giải thích dòng nợ khác giảm; `CHƯA_BIẾT` 10-K không tách riêng con số này trong bảng dòng tiền. Đây đúng là lý do phải đọc **cầu nối chi tiết và thuyết minh**, không chỉ nhìn hai con số tổng.
2. **SBC là chi phí thật nhưng được cộng lại** trong CFO. Người đọc phải tự hỏi: nếu coi chi phí cổ phiếu thưởng là tiền mặt (vì nó pha loãng cổ đông), thì FCF còn bao nhiêu? `PHÉP_TÍNH` FY2025: `98.767 − 12.863 = 85.904` triệu USD. Không có con số nào "đúng" tuyệt đối, nhưng phải nói rõ cách tính.
3. **Capex rất nhỏ so với CFO** — đặc trưng mô hình kinh doanh ít tài sản cố định. Với một doanh nghiệp sản xuất, tỷ lệ này khác hẳn. Vì vậy đừng dùng Apple làm chuẩn cho mọi doanh nghiệp.
4. **Chuẩn kế toán đổi cách đọc tiền thuê**: theo US GAAP, khoản tiền thuê hoạt động cố định Apple trả (`SỰ_THẬT` 2,1 tỷ USD ở FY2025 theo thuyết minh thuê của 10-K) đã nằm **trong** CFO, nên FCF hẹp của Apple đã trừ khoản này. Với một doanh nghiệp lập theo IFRS 16, phần gốc thuê lại nằm ở dòng tiền tài chính (mục 2.3).

> Cách tự kiểm: mở báo cáo 10-K, tìm mục "Consolidated Statements of Cash Flows", đối chiếu ba dòng: lợi nhuận sau thuế, CFO, chi tiêu vốn. Nếu số trên trang tổng hợp lệch với hồ sơ gốc, **luôn dùng hồ sơ gốc**.

## 5. Năm câu hỏi khi đọc dòng tiền

1. CFO ba đến năm năm gần nhất là bao nhiêu, so với lợi nhuận sau thuế cùng kỳ thế nào?
2. Chỗ lệch nằm ở đâu: khấu hao, phải thu, tồn kho, phải trả, hay khoản bất thường?
3. Chi tiêu vốn đang ở mức duy trì hay mở rộng; có dấu hiệu cắt đầu tư để làm đẹp CFO không?
4. Chu kỳ chuyển đổi tiền mặt đang dài ra hay ngắn lại; nếu ngắn lại, nhờ vận hành hay nhờ kéo dài thời gian trả nhà cung cấp?
5. FCF sau khi trừ các khoản phải trả bằng tiền (thuê tài sản, lãi vay, cổ phiếu thưởng) còn bao nhiêu, và doanh nghiệp dùng số đó để làm gì?

## 6. Bài tập (8 câu, làm trong 40 phút)

`KỊCH_BẢN` Tất cả số liệu dưới đây là hư cấu, đơn vị: tỷ đồng.

### Bài 1 (nhớ lại) — dựng cầu nối

Cho: lợi nhuận sau thuế 200; khấu hao 60; phải thu tăng 90; tồn kho tăng 25; phải trả người bán tăng 45; điều chỉnh khác +10. Tính CFO và tỷ lệ chuyển hoá tiền mặt.

### Bài 2 (nhớ lại) — xu hướng ba năm

| Năm | Lợi nhuận sau thuế | CFO |
|---|---:|---:|
| 1 | 150 | 110 |
| 2 | 160 | 128 |
| 3 | 170 | 96 |

Tính tỷ lệ chuyển hoá tiền mặt từng năm và nêu nhận xét trong hai câu.

### Bài 3 (vận dụng) — chu kỳ chuyển đổi tiền mặt

Năm nay: doanh thu 1.800; giá vốn 1.200; phải thu bình quân 250; tồn kho bình quân 250; phải trả bình quân 200.
Năm trước: doanh thu 1.600; giá vốn 1.100; phải thu bình quân 240; tồn kho bình quân 200; phải trả bình quân 220.
Tính DSO, DIO, DPO, CCC cả hai năm và cho biết thay đổi đến từ đâu.

### Bài 4 (vận dụng) — ba định nghĩa FCF

Cho CFO 250; capex 120; tiền trả nợ gốc thuê tài sản 30; lãi vay đã trả 20; thuế suất 20%.
Tính FCF hẹp, FCF sau thanh toán thuê, và ước lượng FCFF nhanh. Nêu một tình huống mà ba con số này dẫn tới ba kết luận khác nhau.

### Bài 5 (vận dụng, câu cũ xen kẽ) — ROIC cao nhưng tiền âm

Cho NOPAT 90; vốn đầu tư đầu kỳ 300. Tính ROIC. Sau đó: doanh nghiệp này có CFO −50, capex 80. Hãy nêu **ba** giả thuyết có thể cùng đúng với hai dữ kiện trên, và một dữ liệu cần kiểm tra cho mỗi giả thuyết.

### Bài 6 (vận dụng, câu cũ xen kẽ) — báo cáo nào thay đổi

Một doanh nghiệp đổi điều kiện bán hàng từ "thu tiền ngay" sang "cho nợ 60 ngày", doanh thu và giá vốn không đổi, không có thay đổi nào khác. Hỏi: (a) lợi nhuận sau thuế kỳ này thay đổi không? (b) CFO thay đổi thế nào? (c) khoản nào trên bảng cân đối tăng?

### Bài 7 (chuyển giao) — tìm lỗi trong đoạn kết luận

"CFO của công ty âm trong năm nay nên chắc chắn công ty bị lỗ. Hơn nữa CFO âm nghĩa là công ty đang phá sản." Hãy chỉ ra **hai** lỗi lập luận và nói cách kiểm tra.

### Bài 8 (chuyển giao) — hỏi gì tiếp

Cho một doanh nghiệp mới với: CFO 300; lợi nhuận sau thuế 120; capex 60; phải trả người bán tăng 150; phải thu giảm 40; tồn kho giảm 30. Nêu **ba câu hỏi** phải hỏi trước khi kết luận "doanh nghiệp này tạo tiền tốt".

## 7. Đáp án

### Bài 1

`PHÉP_TÍNH` `200 + 60 − 90 − 25 + 45 + 10 = 200`. Tỷ lệ chuyển hoá tiền mặt `200 / 200 = 100%`.
`SUY_LUẬN` Câu này kiểm: bạn có nhớ **chiều dấu** của từng khoản vốn lưu động không. Tăng phải thu và tăng tồn kho là **trừ**; tăng phải trả là **cộng**. Sai chiều dấu là lỗi phổ biến nhất khi mới học.

### Bài 2

`PHÉP_TÍNH` Năm 1: `110 / 150 = 73,3%`; năm 2: `128 / 160 = 80,0%`; năm 3: `96 / 170 = 56,5%`.
`SUY_LUẬN` Lợi nhuận tăng 13,3% trong khi CFO giảm 12,7%; khoảng cách mở rộng dần. Nhận xét đúng: **chất lượng lợi nhuận đang xấu đi**, và câu hỏi tiếp theo là chỗ lệch nằm ở phải thu, tồn kho hay khoản bất thường — không được kết luận "công ty lừa đảo" từ ba con số.

### Bài 3

`PHÉP_TÍNH` Năm nay: DSO = `250/1.800 × 365 = 50,7` ngày; DIO = `250/1.200 × 365 = 76,0` ngày; DPO = `200/1.200 × 365 = 60,8` ngày; CCC = `50,7 + 76,0 − 60,8 = 65,9` ngày.
`PHÉP_TÍNH` Năm trước: DSO = `240/1.600 × 365 = 54,8`; DIO = `200/1.100 × 365 = 66,4`; DPO = `220/1.100 × 365 = 73,0`; CCC = `54,8 + 66,4 − 73,0 = 48,1` ngày.
`SUY_LUẬN` CCC tăng `65,9 − 48,1 = 17,8` ngày, đến từ hai phía: **tồn kho quay chậm hơn** (66,4 → 76,0 ngày) và **trả nhà cung cấp nhanh hơn** (73,0 → 60,8 ngày). Thu tiền thì nhanh hơn (54,8 → 50,7), tức là cải thiện nhỏ không bù được hai khoản xấu. Câu này kiểm: bạn có tách CCC thành ba phần thay vì chỉ nhìn tổng.

### Bài 4

`PHÉP_TÍNH` FCF hẹp = `250 − 120 = 130`.
`PHÉP_TÍNH` FCF sau thanh toán thuê = `250 − 120 − 30 = 100`.
`PHÉP_TÍNH` FCFF ước lượng nhanh = `250 + 20 × (1 − 0,2) − 120 = 250 + 16 − 120 = 146`.
`SUY_LUẬN` Ba tình huống dẫn ba kết luận: (a) doanh nghiệp thuê nhiều tài sản — FCF hẹp 130 nghe tốt nhưng thực tế chỉ 100; (b) doanh nghiệp nợ nhiều — FCFF 146 phù hợp để so với chi phí vốn toàn doanh nghiệp, còn FCF 130 phù hợp để nhìn cổ đông; (c) nếu quên thuế của lãi vay, FCFF bị thổi lên 150 thay vì 146. Lưu ý: phép cộng lại lãi vay 20 chỉ đúng khi lãi vay đã trả nằm **trong** CFO 250; nếu báo cáo (ví dụ theo IFRS 18) đã xếp lãi vay vào dòng tiền tài chính thì FCFF nhanh là `250 − 120 = 130`, cộng thêm 16 là tính trùng. Câu này kiểm: bạn có ghi rõ **mình đang tính cho ai** (chủ nợ hay cổ đông) và **lãi vay đang nằm ở dòng nào**.

### Bài 5

`PHÉP_TÍNH` ROIC = `90 / 300 = 30%`.
`SUY_LUẬN` Ba giả thuyết có thể cùng đúng với "ROIC 30% và CFO −50":
1. **Tăng trưởng nhanh cần vốn lưu động**: doanh thu tăng mạnh, phải thu và tồn kho phình ra. Cần kiểm: vòng quay phải thu và tồn kho so với năm trước; điều kiện thanh toán có đổi không.
2. **Đang mở rộng công suất**: capex 80 và tiền đổ vào tài sản cố định xây dở. Cần kiểm: capex so với khấu hao, tiến độ dự án trong thuyết minh.
3. **Lợi nhuận có khoản không phải tiền**: dự phòng hoàn nhập, đánh giá lại tài sản. Cần kiểm: dòng "điều chỉnh khác" trong cầu nối và thuyết minh khoản bất thường.
`SUY_LUẬN` Điểm cần nhớ: ROIC và CFO **trả lời hai câu hỏi khác nhau**, không mâu thuẫn nhau.

### Bài 6

`SUY_LUẬN` (a) Lợi nhuận sau thuế **không đổi** về nguyên tắc, vì doanh thu và chi phí ghi nhận như cũ; chỉ thời điểm thu tiền thay đổi. (b) CFO **giảm** (tiền chưa về). (c) Phải thu khách hàng tăng.
`SUY_LUẬN` Câu này kiểm: bạn có phân biệt được **thay đổi chính sách thương mại** với **thay đổi hiệu quả kinh doanh** không. Đây là lý do phải đọc cả ba báo cáo, không chỉ báo cáo kết quả kinh doanh.

### Bài 7

`SUY_LUẬN` Lỗi 1: "CFO âm ⇒ lỗ" — sai, vì doanh nghiệp có thể lãi (kế toán) mà CFO âm do tăng vốn lưu động hoặc do lỗi thời điểm. Lỗi 2: "CFO âm ⇒ phá sản" — CFO âm một năm không nói lên khả năng thanh toán; phải xem tiền mặt, hạn mức tín dụng chưa dùng, lịch đáo hạn nợ. Cách kiểm: dựng cầu nối chi tiết, xem 3–5 năm, rồi xem dòng tiền tài chính (doanh nghiệp có huy động được vốn không).
`SUY_LUẬN` Câu này kiểm mức "phát hiện lỗi": chỉ ra **lỗi lập luận**, không chỉ nói "kết luận sai".

### Bài 8

`SUY_LUẬN` Ba câu hỏi gợi ý: (1) CFO 300 đến từ đâu khi lợi nhuận chỉ 120 — phải trả người bán tăng 150 là dấu hiệu dùng tiền nhà cung cấp, không phải vận hành tốt hơn; (2) phải thu và tồn kho giảm có phải do bán tài sản/thu hồi nợ một lần, hay do vận hành tốt lên; (3) capex 60 có đủ duy trì năng lực hiện tại không, hay doanh nghiệp đang cắt đầu tư để làm đẹp dòng tiền.
`PHÉP_TÍNH` Kiểm thêm cầu nối: `120 + 150 + 40 + 30 = 340`, trong khi CFO là 300, nên còn **−40** điều chỉnh chưa được giải thích (đề không cho khấu hao, mà khấu hao lại làm CFO **tăng**). Người đọc kỹ sẽ hỏi thêm: khoản −40 đó là gì — thuế đã nộp, hoàn nhập dự phòng, hay lãi không phải tiền? Câu này kiểm: bạn có tự dựng lại cầu nối trước khi tin con số tổng.

## 8. Lỗi thường gặp

- Nghĩ "lãi = có tiền", hoặc ngược lại "CFO âm = lỗ".
- Sai chiều dấu khi cộng trừ thay đổi vốn lưu động.
- So sánh tỷ lệ chuyển hoá tiền mặt giữa hai doanh nghiệp tính bằng hai công thức khác nhau.
- Dùng FCF hẹp cho doanh nghiệp thuê nhiều tài sản lập theo IFRS 16, rồi kết luận "tạo tiền tốt"; hoặc so FCF của một doanh nghiệp IFRS với một doanh nghiệp US GAAP mà quên tiền thuê nằm ở hai dòng khác nhau.
- Cộng lại lãi vay vào CFO để ra FCFF trong khi lãi vay đã nằm ở dòng tiền tài chính.
- Cộng lại SBC (chi phí cổ phiếu thưởng) mà quên rằng nó pha loãng cổ đông — tiền không ra nhưng giá trị có mất.
- Coi DPO tăng là "quản lý vốn lưu động giỏi" mà không xét khả năng nhà cung cấp chấp nhận được bao lâu.
- Đọc CFO của **một năm** rồi kết luận về chất lượng doanh nghiệp.
- Quên rằng từ kỳ báo cáo `2027-01-01`, IFRS 18 đổi điểm xuất phát của phương pháp gián tiếp — so sánh báo cáo cũ và mới phải cẩn thận.

## 9. Đáp án phần ôn bài cũ

1. Báo cáo lưu chuyển tiền tệ (Bài 001).
2. Tài sản tăng (phải thu là tài sản); đối ứng là doanh thu trong báo cáo kết quả kinh doanh — lợi nhuận tăng mà chưa có tiền.
3. `ROIC = NOPAT năm t / Vốn đầu tư đầu kỳ (t−1)` (Bài 003).
4. Ví dụ: ROIC cao một năm có thể do đỉnh chu kỳ giá, do bán tài sản, hoặc do lợi nhuận chứa khoản không phải tiền (Bài 003, mục 6).

## 10. Ranh giới an toàn

- Bài này là khung phân tích, **không** phải khuyến nghị mua/bán/nắm giữ cho bất kỳ mã nào.
- Không kết luận về một doanh nghiệp thật từ một chỉ tiêu duy nhất (CFO cao, FCF dương).
- Số liệu Apple ở mục 4 đã đối chiếu 10-K FY2025 tại ngày chốt; chúng là ví dụ học tập, không phải đánh giá doanh nghiệp, và phải mở lại hồ sơ mới nhất trước khi dùng vào bất kỳ việc gì khác.
- Mọi ví dụ hư cấu không đại diện cho doanh nghiệp thật nào; không dùng bài này để suy ra "công thức chọn cổ phiếu".

## 11. Điều tôi vẫn chưa hiểu

1. Bạn muốn luyện với hồ sơ thật ở thị trường nào — Việt Nam (báo cáo theo VAS) hay Mỹ (10-K)? Điều này quyết định bài 005 có ví dụ nợ ở đâu.
2. Bạn có đọc được dòng "thay đổi tài sản hoạt động khác (ròng)" trong báo cáo tiếng Anh không, hay cần bản giải thích từng dòng?
3. Bạn muốn tôi tách riêng một bài ngắn về **thuê tài sản (IFRS 16)** trước Bài 005, hay gộp vào Bài 005?
4. Với doanh nghiệp bạn đang quan tâm, ba năm CFO và lợi nhuận đang lệch theo chiều nào?

## 12. Nguồn Internet đã mở

Tất cả mở ngày `2026-10-26`; số liệu và định nghĩa dưới đây lấy trực tiếp từ các trang này, không dùng đoạn trích từ trang kết quả tìm kiếm.

- [IAS 7 Statement of Cash Flows — IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/) — HTTP 200; trang chuẩn "Standard 2026 Issued"; phạm vi: chuẩn mực IFRS toàn cầu; không có đơn vị tiền. Cung cấp: định nghĩa ba loại hoạt động, phương pháp trực tiếp/gián tiếp, yêu cầu loại và thuyết minh giao dịch không dùng tiền, yêu cầu đối chiếu tiền, và **sửa đổi do IFRS 18** (dùng lợi nhuận hoạt động làm điểm xuất phát phương pháp gián tiếp; yêu cầu mới về phân loại dòng tiền lãi và cổ tức).
- [IFRS 18 Presentation and Disclosure in Financial Statements — IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/) — HTTP 200; ban hành `2024-04`; hiệu lực kỳ báo cáo năm bắt đầu từ hoặc sau `2027-01-01`; thay thế IAS 1; hai tiểu tổng mới; bắt buộc công bố MPM. Dùng cho lưu ý ở mục 1 và mục 8.
- [Apple Inc. Form 10-K FY2025 — SEC EDGAR](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) — HTTP 200 khi gửi User-Agent khai báo (không khai báo thì SEC trả 403); kỳ FY2023–FY2025 kết thúc 27/09/2025; **triệu USD**; **US GAAP**; nguồn **gốc**. Dùng cho bảng dòng tiền mục 4 (gồm ba dòng tài sản/nợ khác), thuyết minh thuế (khoản 10,2 tỷ USD ròng, 15,8 tỷ USD phải trả cho Ireland) và thuyết minh thuê (tiền thuê hoạt động cố định 2,1 tỷ USD FY2025).
- [Apple company facts — SEC XBRL API](https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json) — HTTP 200 với User-Agent khai báo; dùng để đối chiếu máy từng dòng của bảng mục 4.
- [Apple Cash Flow Statement — stockanalysis.com](https://stockanalysis.com/stocks/aapl/financials/cash-flow-statement/) — HTTP 200; nguồn **thứ cấp** tổng hợp; số liệu khớp 10-K (gộp ba dòng tài sản/nợ khác thành một).
- [Deloitte DART — Roadmap Statement of Cash Flows, 7.6 Leases](https://dart.deloitte.com/USDART/home/codification/presentation/asc230-10/roadmap-statement-cash-flow/chapter-7-common-issues-related-cash/7-6-leases) — HTTP 200; **nguồn thứ cấp** trích ASC 842-20-45-5: tiền thuê hoạt động thuộc dòng tiền hoạt động; gốc thuê tài chính thuộc tài chính, lãi thuê tài chính thuộc hoạt động.
- [BDO — How will IFRS 18 impact the classification of interest and dividends](https://www.bdo.com.au/en-au/blogs/corporate-reporting/how-will-ifrs-18-impact-the-classification-of-interest-and-dividends-in-your-statement-of-cash-flows) — HTTP 200; đăng `2026-10-13`; **nguồn thứ cấp**. Dùng cho phân loại lãi vay/cổ tức sau IFRS 18 ở mục 1 và điều kiện của công thức FCFF.

**Trạng thái kiểm nguồn**: đã qua một lượt `source-fact-checker` độc lập ngày `2026-10-26`, kết luận **ĐẠT** với 0 lỗi nghiêm trọng. Lượt review sau đó cùng ngày đã nâng ví dụ Apple lên nguồn gốc 10-K, sửa diễn giải dòng −20.620, thêm khác biệt IFRS 16/US GAAP về tiền thuê và điều kiện của công thức FCFF (xem [lộ trình §16.5](../roadmap.md#165-review-tổng-thể-và-sửa-ngày-2026-10-26)). Bản hiện tại **chưa có biên bản kiểm nguồn mới** cho hash sau khi sửa.
