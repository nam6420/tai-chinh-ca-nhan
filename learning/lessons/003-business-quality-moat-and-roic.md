# Bài 003: Chất lượng doanh nghiệp — lợi thế cạnh tranh, ROIC và khả năng tái đầu tư

- Ngày: `2026-08-12`
- Chốt dữ liệu lúc: `2026-08-12 20:12 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Hiểu vì sao lợi nhuận cao một năm chưa nói lên chất lượng doanh nghiệp; biết lợi thế cạnh tranh (economic moat) là gì và phải được xác nhận bằng bằng chứng định lượng nào; tính và đọc được ROIC (tỷ suất lợi nhuận trên vốn đầu tư), so nó với chi phí vốn, phân rã nó thành biên lợi nhuận và vòng quay vốn; nhận diện vài cờ đỏ quản trị (pha loãng, giao dịch bên liên quan).

> Đây là bài học nền tảng toàn cầu, không phải khuyến nghị mua, bán hay nắm giữ chứng khoán. Các ví dụ số học đều là doanh nghiệp hư cấu. IAS 24, IFRS 3 và SEC chỉ là ví dụ chuẩn mực/cơ quan quản lý; với thị trường khác phải dùng chuẩn mực và hồ sơ tương ứng. Bài này kế thừa Bài 001 (ba báo cáo tài chính) và Bài 002 (ba câu hỏi trước khi định giá).

Thời lượng gợi ý: 25-35 phút.

## Hiểu bài này trong 1 phút

`SUY_LUẬN` Bài này giải quyết một nhầm lẫn khác: **lợi nhuận cao trong một năm chưa chứng minh doanh nghiệp tốt**. Muốn đánh giá chất lượng, phải trả lời hai câu: lợi nhuận trên vốn có cao **kéo dài qua nhiều năm** không, và điều gì **ngăn đối thủ cạnh tranh** bào mòn mức lợi nhuận đó?

Có thể hình dung bằng ngôn ngữ vận hành hệ thống: một dịch vụ đạt latency tốt trong một ngày đẹp trời chưa nói lên điều gì; thứ đáng tin là p99 ổn định qua nhiều tháng, nhiều đợt cao điểm và nhiều lần bị "tấn công" bởi đối thủ. Với doanh nghiệp cũng vậy: một năm lãi lớn có thể do chu kỳ giá, sự kiện một lần hoặc may mắn; **lợi nhuận trên vốn cao lặp lại nhiều năm, đi kèm bằng chứng khách hàng không rời bỏ và giá bán không bị ép xuống, mới là tín hiệu chất lượng.**

`SỰ_THẬT` Nghiên cứu của McKinsey trên khoảng 7.000 công ty phi tài chính niêm yết tại Mỹ giai đoạn 1963-2004 cho thấy ROIC trung vị (loại trừ goodwill) chỉ quanh 10%, xấp xỉ chi phí vốn dài hạn — tức doanh nghiệp "bình thường" chỉ đủ bù chi phí vốn. Cạnh tranh có xu hướng kéo lợi nhuận siêu ngạch về mức trung bình; moat là thứ hiếm giúp doanh nghiệp chống lại lực kéo đó (nguồn: McKinsey, dẫn ở cuối bài).

### Bài này làm gì và chưa làm gì?

| Bài này làm | Bài này chưa làm |
|---|---|
| Dạy cách đặt câu hỏi về chất lượng: moat, ROIC, chi phí vốn, tái đầu tư, cờ đỏ quản trị | Kết luận doanh nghiệp cụ thể nào "tốt" hay "xấu" |
| Cung cấp công thức khái quát và các biến thể cần biết trước khi tính | Dạy cách ước lượng chi phí vốn chính xác (chủ đề định giá, tuần 5-6) |
| Chỉ ra bằng chứng định lượng cần tìm để xác nhận moat | Thay thế việc đọc báo cáo tài chính và thuyết minh của doanh nghiệp thật |

> Câu cần nhớ: **Đừng hỏi "năm nay công ty lãi bao nhiêu?"; hãy hỏi "công ty tạo lợi nhuận trên vốn cao trong bao lâu, nhờ điều gì bảo vệ, và tái đầu tư thêm một đồng vốn thì sinh ra bao nhiêu?"**

## 1. Lợi thế cạnh tranh (economic moat) là gì?

Lợi thế cạnh tranh bền vững — thường gọi là **moat** (hào nước quanh lâu đài) — là điều kiện khiến đối thủ khó hoặc không thể giành khách hàng và ép giá doanh nghiệp. `Ý_KIẾN` Thuật ngữ này phổ biến trong giới đầu tư; điều quan trọng không phải cái tên mà là **bằng chứng**.

Theo tài liệu whitepaper của VanEck mô tả phương pháp luận moat của Morningstar, có năm nguồn moat thường gặp:

| Nguồn moat | Trực giác | Ví dụ trong whitepaper (doanh nghiệp Mỹ) |
|---|---|---|
| Tài sản vô hình (thương hiệu, bằng sáng chế, giấy phép) | Khách trả giá cao hơn hoặc đối thủ bị cấm sao chép | Starbucks, Eli Lilly |
| Chi phí chuyển đổi (switching cost) | Đổi nhà cung cấp tốn tiền, thời gian, rủi ro | Salesforce, Stryker |
| Hiệu ứng mạng lưới (network effect) | Càng nhiều người dùng, sản phẩm càng giá trị | Visa, Google |
| Lợi thế chi phí (cost advantage) | Cùng giá bán nhưng chi phí thấp hơn nhờ quy mô, quy trình | Walmart, AB InBev |
| Quy mô hiệu quả (efficient scale) | Thị trường chỉ đủ chỗ cho một/vài người có lãi | Union Pacific, Dominion Energy |

`SỰ_THẬT` Bảng trên lấy từ whitepaper bản quyền © Morningstar 2020 và © 2020 VanEck, mô tả phương pháp luận Morningstar (trang morningstar.com không truy cập được trong lượt này — xem phần Nguồn). Đây là nguồn thứ cấp mô tả phương pháp luận, không phải tuyên bố của chính Morningstar.

### Moat phải được xác nhận bằng bằng chứng, không bằng tuyên bố

Báo cáo thường niên nào cũng viết "chúng tôi dẫn đầu". Tuyên bố đó là `Ý_KIẾN` của doanh nghiệp. Moat chỉ đáng cân nhắc khi có bằng chứng định lượng lặp lại nhiều năm:

- Biên lợi nhuận gộp/hoạt động cao hơn hẳn nhóm so sánh **và ổn định** qua nhiều năm, kể cả năm khó.
- Quyền định giá (pricing power): tăng giá mà khách không bỏ đi; doanh thu/đơn vị không giảm khi tăng giá.
- Tỷ lệ giữ chân/gia hạn cao kéo dài; khách hàng rời bỏ rất ít ngay cả khi đối thủ rẻ hơn.
- ROIC cao hơn chi phí vốn qua nhiều chu kỳ (xem mục 2-3).

`SUY_LUẬN` Ngược lại, moat có thể bị bào mòn: công nghệ thay đổi, quy định mở cửa, đối thủ tìm ra cách vượt chi phí chuyển đổi. Vì vậy câu hỏi đúng không phải "công ty có moat không?" mà là "bằng chứng moat còn nguyên vẹn đến kỳ báo cáo gần nhất không, và điều gì có thể phá vỡ nó?".

## 2. ROIC: lợi nhuận trên vốn đầu tư

**ROIC (Return on Invested Capital)** đo một đồng vốn bỏ vào doanh nghiệp tạo ra bao nhiêu lợi nhuận hoạt động. Với người làm backend, đây giống số đo throughput trên mỗi đơn vị tài nguyên bỏ tiền mua — muốn biết hệ thống "đáng tiền" hay không, không nhìn tổng throughput, mà nhìn hiệu quả trên vốn đã triển khai.

`SỰ_THẬT` Theo tài liệu của Damodaran (NYU Stern), công thức khái quát là:

```text
ROIC = Lợi nhuận hoạt động sau thuế (NOPAT) năm t / Giá trị sổ sách của vốn đầu tư đầu kỳ (t-1)
```

Trong đó, cũng theo Damodaran:

- **NOPAT** thường tính là `EBIT × (1 - thuế suất)`, phản ánh lợi nhuận tạo ra cho **mọi** người cấp vốn (chủ nợ lẫn cổ đông). Lưu ý dùng thuế suất hiệu dụng/giả định trên EBIT, không dùng thuế thực nộp, vì thuế thực nộp đã chứa lợi ích lá chắn thuế của lãi vay — dùng sai sẽ tính trùng.
- **Vốn đầu tư (invested capital)** có thể tính từ nguồn vốn: `nợ vay có giá trị sổ sách + vốn chủ sở hữu - tiền mặt`; hoặc từ tài sản: `tài sản cố định + vốn lưu động phi tiền mặt`. Hai cách thường cho kết quả tương đương.
- Dùng **giá trị sổ sách đầu kỳ** của vốn, vì lợi nhuận năm nay được tạo ra từ vốn đã bỏ ra trước đó.

`SỰ_THẬT` Damodaran nhấn mạnh có **nhiều biến thể** (ROIC kế toán, cash ROIC, CFROI...) và các điều chỉnh (R&D bị tính là chi phí, thuê hoạt động, chi phí bất thường, goodwill). Điều quan trọng với người mới: **chọn một công thức và nhất quán khi so sánh giữa các doanh nghiệp và giữa các năm**; so sánh hai con số tính bằng hai công thức khác nhau là so sánh sai.

Cảnh báo:

- `SUY_LUẬN` Với **ngân hàng và bảo hiểm**, khái niệm "vốn đầu tư" và "lợi nhuận hoạt động" theo công thức trên không áp dụng sạch: tiền gửi là nguyên liệu đầu vào chính và cũng là nợ. Kế thừa Bài 002: ngành tài chính cần bộ chỉ số và cách phân tích riêng (như ROE, ROA, an toàn vốn), không áp máy móc ROIC của doanh nghiệp phi tài chính.
- `SỰ_THẬT` Damodaran cảnh báo ROA (lợi nhuận trên tổng tài sản) không được dùng để so với chi phí vốn, vì mẫu số của ROA chứa cả nợ ngắn hạn không chịu lãi.
- Goodwill (lợi thế thương mại): `SỰ_THẬT` theo IFRS 3 của IFRS Foundation, goodwill là phần chênh lệch còn lại của giá phí hợp nhất kinh doanh sau khi phân bổ vào giá trị hợp lý của tài sản và nợ phải trả xác định được. Doanh nghiệp mua bán nhiều mà không loại/điều chỉnh goodwill thì ROIC dễ bị bóp méo; nghiên cứu của McKinsey dùng ROIC **loại trừ goodwill** để phản ánh hiệu quả hoạt động.

## 3. ROIC so với chi phí vốn: tạo hay phá hủy giá trị?

**Chi phí vốn (cost of capital)** là mức lợi nhuận tối thiểu mà người cấp vốn (chủ nợ và cổ đông) kỳ vọng cho rủi ro họ gánh. `SỰ_THẬT` Theo Damodaran, thước đo giá trị cốt lõi là **excess return = ROIC - chi phí vốn**:

- `SỰ_THẬT` ROIC > chi phí vốn: mỗi đồng vốn mới tạo ra nhiều hơn chi phí của nó → tăng trưởng **tạo** giá trị.
- `SỰ_THẬT` ROIC < chi phí vốn: mỗi đồng vốn mới sinh ra ít hơn chi phí của nó → tăng trưởng càng nhanh càng **phá hủy** giá trị.
- `SỰ_THẬT` Tính nhất quán bắt buộc: NOPAT sau thuế (đã loại lợi ích thuế của nợ) phải được so với chi phí vốn bình quân (WACC) sau thuế.

Chi phí vốn là một **ước tính phụ thuộc giả định** (lãi suất phi rủi ro, phần bù rủi ro, cơ cấu vốn), không phải con số quan sát trực tiếp. Trong phạm vi bài này: nếu không tự ước lượng được, hãy ghi `CHƯA_BIẾT` và chỉ kết luận định tính ("ROIC cao hơn đáng kể mặt bằng lãi vay và lợi nhuận kỳ vọng hợp lý"), không bịa một con số WACC chính xác.

`SỰ_THẬT` McKinsey (McKinsey on Finance, 2006) cung cấp thêm bối cảnh: nhà đầu tư trả bội số cao hơn cho công ty có ROIC vượt trội ngay cả khi tăng trưởng hạn chế; trong mẫu nghiên cứu, công ty có ROIC trên 20% có khoảng 50% xác suất duy trì mức đó sau một thập kỷ — còn công ty tăng trưởng "nóng" (trên 20%/năm) có tới 56% xác suất rơi xuống dưới 5% sau 10 năm, chỉ khoảng 13% duy trì được đà tăng trưởng. Nói cách khác: **ROIC cao bền vững hiếm và đáng giá hơn tăng trưởng nhanh nhất thời.**

## 4. Tái đầu tư và tăng trưởng

`SỰ_THẬT` Damodaran nêu quan hệ nền tảng:

```text
Tăng trưởng lợi nhuận ≈ Tỷ lệ tái đầu tư × ROIC
```

trong đó tỷ lệ tái đầu tư là phần lợi nhuận hoạt động sau thuế được tái đầu tư trở lại doanh nghiệp (phần không trả cổ tức/mua lại cổ phiếu). Suy ra:

```text
Tỷ lệ tái đầu tư cần thiết ≈ Tốc độ tăng trưởng mong muốn / ROIC
```

`PHÉP_TÍNH` `MINH HỌA` (số hư cấu): Công ty A có ROIC 30% muốn tăng trưởng 6%/năm chỉ cần giữ lại `6% / 30% = 20%` NOPAT. Công ty B có ROIC 5% muốn tăng 6%/năm cần `6% / 5% = 120%` NOPAT — tức là **toàn bộ lợi nhuận vẫn không đủ**, phải vay thêm hoặc phát hành cổ phiếu. Cùng một tốc độ tăng, doanh nghiệp ROIC cao cần rất ít vốn hơn và không phải pha loãng hay vay nợ.

`SUY_LUẬN` Đây là lý do "khả năng tái đầu tư" đi kèm moat: moat cho ROIC cao, ROIC cao cho phép tăng trưởng rẻ; hết chỗ tái đầu tư trong ngành thì ROIC cao biến thành dòng tiền tự do trả lại cho cổ đông — vẫn là dấu hiệu tốt nếu phân bổ vốn hợp lý (xem mục 7).

## 5. Phân rã ROIC: biên lợi nhuận × vòng quay vốn

`PHÉP_TÍNH` ROIC có thể tách thành hai đòn bẩy (trực giác DuPont):

```text
ROIC = (NOPAT / Doanh thu) × (Doanh thu / Vốn đầu tư)
     = Biên lợi nhuận hoạt động × Vòng quay vốn
```

Có hai con đường tạo ROIC cao: bán với biên dày (thương hiệu, khác biệt hóa) hoặc quay vòng vốn nhanh (hiệu quả vận hành, ít tài sản). `MINH HỌA` tiếp theo ví dụ Công ty A/B ở mục 4: A đạt `15% × 2,0 = 30%`; B đạt `6% × 0,83 ≈ 5%`. Khi ROIC của một doanh nghiệp thay đổi, hãy hỏi: biên thay đổi (giá bán, chi phí đầu vào) hay vòng quay thay đổi (tài sản phình to, hàng tồn chậm)?

## 6. ROIC cao do moat hay do đỉnh chu kỳ?

`SUY_LUẬN` ROIC cao của một năm có thể đến từ: giá hàng hóa đầu ra tăng đột biến, giá đầu vào giảm tạm thời, một hợp đồng lớn một lần, đánh giá lại tài sản, hoặc cắt giảm chi phí không lặp lại. Phân biệt bằng ba phép thử:

1. **Xem nhiều năm, tốt nhất trọn một chu kỳ ngành** (bao gồm cả năm xấu). Moat thật thường lộ ra ở chỗ biên lợi nhuận và thị phần **chống chịu tốt trong năm khó**.
2. **Tách giá và lượng**: lợi nhuận tăng do giá bán tăng theo thị trường (chu kỳ) khác với tăng do bán được nhiều hơn trong khi giữ giá (sức mạnh thật).
3. **Loại sự kiện một lần** khỏi lợi nhuận trước khi tính ROIC "chuẩn hóa" — tương tự Bài 002 đã làm với P/E trên EPS bất thường.

`SỰ_THẬT` McKinsey quan sát thấy xếp hạng ROIC giữa các ngành khá ổn định theo thời gian, nhưng **phương sai ROIC trong cùng một ngành đôi khi lớn hơn giữa các ngành** (ngành phần mềm và dịch vụ trong mẫu có trung vị 18%, nhưng chênh lệch giữa tứ phân vị trên và tứ phân vị dưới lên tới 31 điểm phần trăm). Vì vậy luôn so doanh nghiệp với nhóm cùng mô hình kinh doanh, không so với trung bình ngành chung chung.

## 7. Ví dụ số học hư cấu: cùng doanh thu, ROIC khác nhau, giá trị khác nhau

`KỊCH_BẢN` `MINH HỌA` — tất cả số dưới đây là hư cấu, đơn vị tiền:

| Chỉ tiêu (năm) | Công ty A | Công ty B |
|---|---:|---:|
| Doanh thu | 1.000 | 1.000 |
| NOPAT | 150 | 60 |
| Vốn đầu tư đầu kỳ | 500 | 1.200 |
| **ROIC** | **150/500 = 30%** | **60/1.200 = 5%** |
| Biên lợi nhuận hoạt động | 15% | 6% |
| Vòng quay vốn | 2,0 lần | 0,83 lần |

Giả sử chi phí vốn của cả hai là 10% (`KỊCH_BẢN`, giả định minh họa, `CHƯA_BIẾT` chi phí vốn thật vì chưa ước lượng):

- `PHÉP_TÍNH` Công ty A: ROIC 30% > 10%. Mỗi 100 đồng vốn mới tạo 30 đồng lợi nhuận trong khi chi phí vốn chỉ 10 đồng → tăng trưởng tạo giá trị.
- `PHÉP_TÍNH` Công ty B: ROIC 5% < 10%. Mỗi 100 đồng vốn mới tạo 5 đồng trong khi chi phí vốn là 10 đồng → càng mở rộng càng lỗ kinh tế, dù báo cáo vẫn "có lãi kế toán".

Ví dụ thứ hai — vì sao lợi nhuận một năm gây hiểu nhầm:

`KỊCH_BẢN` `MINH HỌA` Công ty C (hư cấu, mang tính chu kỳ) có 50 triệu cổ phiếu, giá 24. Lợi nhuận 5 năm gần nhất: 20, 25, 22, 100, 30 (năm thứ tư bùng nổ do giá bán tăng đột biến, năm sau đã rơi về vùng cũ).

- `PHÉP_TÍNH` Nếu nhìn đúng năm đỉnh: vốn hóa = 24 × 50 = 1.200; P/E = 1.200/100 = 12 lần — trông "rẻ".
- `PHÉP_TÍNH` Nếu dùng lợi nhuận đại diện quanh 25: P/E = 1.200/25 = 48 lần — thực tế là đắt.

`SUY_LUẬN` P/E 12 ở đây là ảo giác của chu kỳ: mẫu số (lợi nhuận) đang ở đỉnh tạm thời. Bài 002 gọi đây là bẫy P/E thấp; bài này cho thấy cơ chế của nó nằm ở việc **lợi nhuận đỉnh chu kỳ thổi phồng NOPAT và cả ROIC**, nên phải kiểm tra cả P/E lẫn ROIC trên dữ liệu nhiều năm.

## 8. Cờ đỏ quản trị (chạm nhẹ)

- **Pha loãng cổ phiếu:** phát hành thêm với giá thấp hơn giá trị hợp lý, ESOP quá lớn, hoặc liên tục gọi vốn trong khi lợi nhuận không chuyển thành tiền. `SỰ_THẬT` Theo Investor Bulletin của SEC (bản cập nhật 2022-10-14), hồ sơ chào bán tại Mỹ phải có mục "Dilution" so sánh giá chào bán với giá trị sổ sách mỗi cổ phần và với giá mà cổ đông hiện hữu đã trả; cấu trúc cổ phiếu hai lớp (dual-class) có thể khiến cổ đông đại chúng khó hoặc không thể gây ảnh hưởng lên các vấn đề doanh nghiệp. Kiểm tra số cổ phiếu lưu hành qua nhiều năm: lợi nhuận tăng nhưng EPS không tăng vì cổ phiếu tăng nhanh hơn là dấu hiệu pha loãng.
- **Giao dịch bên liên quan:** `SỰ_THẬT` Theo IAS 24 của IFRS Foundation, bên liên quan bao gồm cá nhân (hoặc thành viên gia đình thân thiết) kiểm soát, đồng kiểm soát, có ảnh hưởng đáng kể hoặc là nhân sự quản lý chủ chốt, cùng các thực thể như công ty mẹ, công ty con, công ty liên kết; giao dịch bên liên quan là mọi chuyển giao nguồn lực, dịch vụ hoặc nghĩa vụ, **bất kể có tính giá hay không**; doanh nghiệp phải thuyết minh bản chất quan hệ, giá trị giao dịch, số dư và thù lao quản lý chủ chốt. Đọc thuyết minh để hỏi: giao dịch này có theo điều kiện thị trường không, hay chuyển lợi nhuận ra ngoài tầm cổ đông thiểu số?
- **Phân bổ vốn lịch sử:** doanh nghiệp mua lại với giá đắt tạo goodwill lớn (IFRS 3: goodwill là phần giá phí hợp nhất vượt giá trị hợp lý của tài sản và nợ xác định được; mua rẻ thì ghi lãi ngay vào báo cáo lãi lỗ), mua đỉnh chu kỳ, hoặc đầu tư dàn trải khiến vòng quay vốn giảm nhiều năm liên tiếp — tất cả sẽ hiện ra trong xu hướng ROIC đi xuống dù lợi nhuận tuyệt đối vẫn tăng.

## Năm câu hỏi khi đọc

1. Moat được tuyên bố có bằng chứng định lượng nào: biên lợi nhuận cao bền vững nhiều năm, pricing power, retention?
2. ROIC tính theo công thức nào, có nhất quán giữa các năm và với nhóm so sánh không, và nó nằm trên hay dưới chi phí vốn?
3. Tăng trưởng hiện tại cần bao nhiêu tái đầu tư; doanh nghiệp tài trợ bằng nội lực, nợ vay hay pha loãng?
4. Lợi nhuận năm nay có tính đại diện không, hay là đỉnh chu kỳ/sự kiện một lần?
5. Lịch sử phân bổ vốn nói gì: phát hành cổ phiếu, giao dịch bên liên quan và các thương vụ mua lại có làm hỏng ROIC không?

## Bài tập

### Bài 1: tính ROIC nhiều năm và nhận xét xu hướng

`KỊCH_BẢN` Công ty T (hư cấu), số liệu NOPAT và vốn đầu tư **đầu kỳ** (đơn vị tiền):

| Năm | NOPAT | Vốn đầu tư đầu kỳ |
|---|---:|---:|
| 1 | 80 | 800 |
| 2 | 100 | 900 |
| 3 | 108 | 1.200 |
| 4 | 110 | 1.500 |

Tính ROIC từng năm, nhận xét xu hướng, và nêu ít nhất hai giả thuyết cần kiểm tra thêm.

### Bài 2: phân biệt tuyên bố moat và bằng chứng moat

`KỊCH_BẢN` Khi đọc hồ sơ công ty S (hư cấu), bạn gặp năm câu sau. Phân loại từng câu là **tuyên bố** hay **bằng chứng**, và nêu dữ liệu cần kiểm tra để biến tuyên bố thành bằng chứng:

1. "Chúng tôi sở hữu thương hiệu được yêu thích nhất ngành."
2. "Tỷ lệ khách hàng gia hạn hợp đồng đạt 95% trong 5 năm liên tiếp."
3. "Ban lãnh đạo tin rằng hệ sinh thái của chúng tôi không có đối thủ."
4. "Biên lợi nhuận gộp duy trì 45-48% suốt 10 năm, trong khi trung vị nhóm cùng ngành là 22-25%."
5. "Khách hàng muốn đổi sang đối thủ sẽ phải tích hợp lại toàn bộ hệ thống, ước tính tốn 6 tháng chi phí vận hành."

### Bài 3: lợi nhuận bùng nổ — moat hay chu kỳ?

`KỊCH_BẢN` Công ty V (hư cấu) sản xuất hàng hóa cơ bản: lợi nhuận tăng từ 40 lên 160 trong một năm; giá bán thành phẩm tăng 60% do nguồn cung toàn cầu gián đoạn; chi phí đầu vào gần như không đổi; giá cổ phiếu tăng mạnh và P/E trượt trông rất thấp. Đặt giả thuyết và liệt kê dữ liệu cần kiểm tra để phân biệt "moat thật" với "đỉnh chu kỳ".

## Đáp án hoàn chỉnh

### Bài 1

`PHÉP_TÍNH` Dùng vốn đầu tư đầu kỳ theo công thức mục 2:

- Năm 1: `80 / 800 = 10,0%`
- Năm 2: `100 / 900 = 11,1%`
- Năm 3: `108 / 1.200 = 9,0%`
- Năm 4: `110 / 1.500 = 7,3%`

`SUY_LUẬN` Nhận xét: NOPAT tăng đều 80 → 110 nhưng ROIC tăng nhẹ rồi **giảm liên tiếp hai năm** — vốn tăng nhanh hơn lợi nhuận. Nếu chi phí vốn là 10% (giả định minh họa), năm 4 công ty đã tiến sát ngưỡng không tạo giá trị. Giả thuyết cần kiểm tra: (a) vốn tăng do một thương vụ mua lại (kiểm tra goodwill và thuyết minh hợp nhất); (b) biên lợi nhuận bị ép do cạnh tranh giá hoặc chi phí đầu vào (tách biên và vòng quay theo mục 5); (c) đầu tư mở rộng chưa đạt công suất (kiểm tra tiến độ và kế hoạch công suất). Nếu dùng bình quân vốn thay vì vốn đầu kỳ, các tỷ lệ sẽ khác đôi chút — phải ghi rõ quy ước đã dùng.

### Bài 2

- Câu 1: **Tuyên bố** (ý kiến marketing). Cần: dữ liệu khảo sát nhận diện thương hiệu độc lập, khả năng giữ giá cao hơn đối thủ, biên lợi nhuận so nhóm cùng ngành qua nhiều năm.
- Câu 2: **Bằng chứng định lượng ban đầu** — nhưng phải kiểm tra nguồn số liệu, định nghĩa "gia hạn" (tính theo số khách hàng hay theo giá trị hợp đồng), và tỷ lệ này có giảm trong năm khó không.
- Câu 3: **Tuyên bố/ý kiến** của người trong cuộc. Cần: thị phần qua nhiều năm, phản ứng của khách hàng khi có đối thủ mới xuất hiện.
- Câu 4: **Bằng chứng định lượng mạnh** — vẫn cần kiểm tra nhóm so sánh có thật sự cùng mô hình kinh doanh không và biên có chứa khoản một lần không.
- Câu 5: **Bán bằng chứng** — ước tính chi phí chuyển đổi cần được xác nhận bằng dữ liệu thực: tỷ lệ rời bỏ sau khi đối thủ giảm giá, thời gian khách thực sự đã gắn bó.

`SUY_LUẬN` Quy tắc: tuyên bố trả lời "chúng tôi nói gì về mình"; bằng chứng trả lời "số liệu nhiều năm và hành vi khách hàng nói gì". Moat đáng tin khi tuyên bố được đỡ bởi nhiều bằng chứng độc lập.

### Bài 3

- `SUY_LUẬN` Giả thuyết 1 — đỉnh chu kỳ giá: lợi nhuận tăng chủ yếu do giá bán tăng 60% từ cú sốc nguồn cung bên ngoài, không phải do doanh nghiệp mạnh lên. Dữ liệu kiểm tra: chuỗi giá bán và chi phí 5-10 năm; công suất ngành đang mở rộng ở đâu; hợp đồng tương lai/giá kỳ hạn nếu có; khi nguồn cung phục hồi lợi nhuận có rơi về vùng 40 không.
- `SUY_LUẬN` Giả thuyết 2 — hưởng lợi tạm thời từ tồn kho/ghi nhận một lần: giá tăng làm phần tồn kho giá rẻ được bán với giá cao, hoặc có khoản hoàn nhập dự phòng. Dữ liệu kiểm tra: thuyết minh hàng tồn kho, phương pháp tính giá xuất, dòng tiền hoạt động so với lợi nhuận (nối lại Bài 001).
- `SUY_LUẬN` Giả thuyết 3 — moat thật (xác suất thấp hơn với hàng hóa cơ bản): chi phí sản xuất thấp nhất ngành, hợp đồng dài hạn, vị trí/logistics độc quyền. Dữ liệu kiểm tra: so chi phí đơn vị với đối thủ cùng ngành qua **cả chu kỳ**, đặc biệt năm giá xuống; thị phần có tăng trong giai đoạn khó không.
- `SUY_LUẬN` Điều kiện bác bỏ "moat": nếu lợi nhuận trở về xu hướng cũ khi nguồn cung phục hồi, hoặc biên lợi nhuận biến động cùng nhịp giá hàng hóa thay vì ổn định, thì mức lợi nhuận 160 là chu kỳ, không phải chất lượng. P/E trượt thấp lúc này nhiều khả năng là bẫy của Bài 002.

## Lỗi thường gặp

- Tin moat vì báo cáo thường niên tuyên bố, không đòi bằng chứng định lượng nhiều năm.
- Dùng ROIC một năm duy nhất để kết luận chất lượng; phải xem qua nhiều năm và cả chu kỳ, kể cả năm xấu.
- So sánh ROIC tính bằng hai công thức/quy ước khác nhau (vốn đầu kỳ vs bình quân, có/không goodwill, có/không điều chỉnh R&D) rồi gọi là so sánh.
- Áp máy móc công thức ROIC cho ngân hàng, bảo hiểm — vốn và lợi nhuận của ngành tài chính có cấu trúc khác hẳn.
- Nói "ROIC 8% là tạm ổn" mà không so với chi phí vốn; hoặc tự bịa một con số chi phí vốn chính xác khi chưa ước lượng được (phải ghi `CHƯA_BIẾT`).
- Ca ngợi tăng trưởng cao mà quên rằng với ROIC dưới chi phí vốn, tăng trưởng càng nhanh càng phá hủy giá trị.
- Bỏ qua goodwill và lịch sử mua lại khi tính ROIC của doanh nghiệp hay đi thâu tóm.
- Thấy P/E thấp ở đỉnh chu kỳ rồi gọi là rẻ, không chuẩn hóa lợi nhuận.
- Thấy lợi nhuận tăng liền cho là tốt, không kiểm tra số cổ phiếu lưu hành (pha loãng) và giao dịch bên liên quan trong thuyết minh.

## Ranh giới an toàn

- Bài này là khung phân tích, không phải khuyến nghị mua/bán/nắm giữ cho bất kỳ mã nào.
- Không đặt lệnh dựa trên một chỉ số duy nhất (ROIC cao, P/E thấp, "có moat").
- Không dùng đòn bẩy để thực hành; ví dụ hư cấu không đại diện cho doanh nghiệp thật nào.
- Mọi kết luận về doanh nghiệp thật phải đi qua hồ sơ gốc, kịch bản bất lợi/cơ sở/thuận lợi và bước kiểm nguồn theo quy trình của repo.

## Điều tôi vẫn chưa hiểu

- Người học muốn thực hành tính ROIC trên thị trường nào (Việt Nam, Mỹ, khác), và doanh nghiệp thật đầu tiên để luyện là doanh nghiệp nào?
- Ngành nào người học muốn chọn làm bài tập chu kỳ (hàng hóa cơ bản, bán lẻ, phần mềm...)?
- Khả năng đọc thuyết minh tiếng Anh hiện tại đến đâu để chọn hồ sơ gốc phù hợp?
- Người học muốn đào sâu ước lượng chi phí vốn ngay bây giờ hay để cùng chủ đề định giá tuần 5-6?

## Nguồn Internet đã mở và nghiên cứu liên quan

Các nguồn dưới đây được mở trực tiếp ngày `2026-08-12` (không dùng đoạn trích trên trang kết quả làm bằng chứng).

- [IAS 24 - Related Party Disclosures, IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ias-24-related-party-disclosures/) — HTTP 200; ngày xuất bản trang: `CHƯA_BIẾT` (trang chuẩn hiện hành, cập nhật thường xuyên); lịch sử chuẩn: ban hành 07/1984 (IASC), IASB tiếp nhận 04/2001, sửa đổi 12/2003 và 11/2009, sửa đổi hệ quả từ IFRS 18 (04/2024); phạm vi: chuẩn mực IFRS toàn cầu; tiền tệ/đơn vị: không áp dụng. Cung cấp định nghĩa bên liên quan, giao dịch bên liên quan và yêu cầu thuyết minh (kể cả thù lao quản lý chủ chốt) dùng ở mục 8.
- [IFRS 3 - Business Combinations, IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-3-business-combinations/) — HTTP 200; ngày xuất bản trang: `CHƯA_BIẾT`; ban hành lần đầu 03/2004 (thay IAS 22), sửa đổi toàn diện 01/2008, sửa đổi gần nhất từ IFRS 18 (04/2024); phạm vi: chuẩn mực IFRS toàn cầu; tiền tệ/đơn vị: không áp dụng. Cung cấp cách ghi nhận goodwill (phần giá phí hợp nhất còn lại sau khi phân bổ vào giá trị hợp lý của tài sản và nợ xác định được; mua rẻ ghi lãi ngay vào báo cáo lãi lỗ).
- [Return on Capital (ROC), Return on Invested Capital (ROIC) and Return on Equity (ROE): Measurement and Implications — Aswath Damodaran, NYU Stern (PDF)](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/returnmeasures.pdf) — HTTP 200; bản PDF đề tháng 07/2007; phạm vi: khung đo lường toàn cầu, trung lập tiền tệ. Cung cấp công thức ROIC (NOPAT/vốn đầu tư giá trị sổ sách đầu kỳ), hai cách tính invested capital, cảnh báo tính trùng thuế, các điều chỉnh (R&D, thuê, goodwill), quan hệ excess return = ROIC − chi phí vốn, `tăng trưởng = tỷ lệ tái đầu tư × ROC` và cảnh báo về ROA.
- [Balancing ROIC and growth to build value — McKinsey on Finance](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/balancing-roic-and-growth-to-build-value) — HTTP 200 (lần mở thứ hai trong phiên kiểm tra; lần đầu gặp 403 do máy chủ chặn tạm thời); xuất bản `2006-03-01`; tác giả Bing Cao và Bin Jiang; phạm vi: các công ty niêm yết lớn nhất Mỹ theo dõi từ 1965/1975/1985/1995 đến 2004; tiền tệ: USD. Cung cấp luận điểm ROIC là thước đo tạo giá trị, xác suất duy trì ROIC > 20% sau một thập kỷ khoảng 50%, và độ bền thấp của tăng trưởng nóng (56% rơi xuống dưới 5%, chỉ ~13% duy trì).
- [A long-term look at ROIC — McKinsey on Finance](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/a-long-term-look-at-roic) — HTTP 200 (lần mở thứ hai trong phiên kiểm tra; lần đầu gặp 403 do máy chủ chặn tạm thời); xuất bản `2006-02-01`; tác giả Bin Jiang; phạm vi: khoảng 7.000 công ty phi tài chính niêm yết Mỹ 1963-2004, doanh thu > 200 triệu USD theo giá 2003; tiền tệ: USD; ROIC dùng trong nghiên cứu **loại trừ goodwill**. Cung cấp trung vị ROIC ~10% ≈ chi phí vốn dài hạn và phương sai ROIC trong ngành (phần mềm và dịch vụ trung vị 18%, chênh lệch tứ phân vị trên/dưới tới 31 điểm phần trăm).
- [Five Sources of Moats Whitepaper — VanEck (mô tả phương pháp luận Morningstar)](https://www.vaneck.com/nl/en/moat-investing/five-sources-of-moats-whitepaper.pdf) — HTTP 200; bản quyền © Morningstar 2020 và © 2020 VanEck, ngày xuất bản chính xác: `CHƯA_BIẾT`; phạm vi: ví dụ lấy từ doanh nghiệp niêm yết Mỹ; tiền tệ: USD. Đây là **nguồn thứ cấp** mô tả năm nguồn moat (tài sản vô hình, chi phí chuyển đổi, hiệu ứng mạng lưới, lợi thế chi phí, quy mô hiệu quả) theo phương pháp luận Morningstar.
- [Investor Bulletin: Investing in an IPO — SEC Investor.gov](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-17) — HTTP 200; cập nhật `2022-10-14`; phạm vi: chào bán IPO tại Mỹ; tiền tệ/đơn vị: không áp dụng. Cung cấp yêu cầu mục "Dilution" trong hồ sơ chào bán (so giá chào bán với giá trị sổ sách và giá cổ đông hiện hữu đã trả) và rủi ro cấu trúc hai lớp cổ phiếu.
- Ghi nhận nguồn không truy cập được: `https://www.morningstar.com/business/insights/blog/equity-economic-moat-ratings` và `https://www.morningstar.com/stocks/morningstar-economic-moat-rating-3` đều trả về HTTP 202 với nội dung rỗng (nghi do chặn truy cập tự động) trong lượt này; vì vậy mục 1 dùng whitepaper VanEck như nguồn thứ cấp thay thế và đã ghi nhãn tương ứng.
