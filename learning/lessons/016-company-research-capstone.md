# Bài 016 — Bài tổng kết: từ báo cáo thật tới một hồ sơ nghiên cứu

- Ngày: `2026-10-26`
- Chốt dữ liệu lúc: `2026-10-26 17:12 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Truy được đầu vào; tái tính chỉ số; tách sự thật/kịch bản; lập kế hoạch kiểm luận điểm với bằng chứng hai chiều.
- Bài trước liên quan: Thứ tự đọc **Bước 23/23 (Bài tổng kết Nhánh 1)** — học ngay sau [Bài 015: Tâm lý, bảng tự kiểm và nhật ký quyết định](015-behavior-decision-journal.md), tổng hợp toàn bộ chuỗi nền tảng ([Bài N1](N1-market-basics.md)–[Bài 003](003-business-quality-moat-and-roic.md)) và chuỗi phân tích – định giá ([Bài 004](004-cash-flow-and-earnings-quality.md)–[Bài 012](012-scenarios-margin-of-safety.md), [Bài Q4](Q4-getting-data-edgar-xbrl-vietnam.md)–[Bài Q3](Q3-normalizing-earnings-cyclical.md)); đọc thêm [Bài 013](013-banks-insurers.md) nếu nghiên cứu ngân hàng/bảo hiểm, hoặc [Bài 014](014-industry-capital-cycle.md) nếu cần khung ngành chu kỳ.
- Thời lượng: Hai hoặc ba phiên ngắn theo điểm dừng; chưa đo thời gian học thực tế.
- Câu hỏi cốt lõi: **Tôi có thể để người khác kiểm lại một kết luận từ đầu tới cuối không?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

## Hiểu bài này trong 1 phút

Bài tổng kết không phải đoán mã sẽ tăng giá. Sản phẩm là một đường đi có thể truy lại: câu hỏi → tài liệu gốc → số liệu → phép tính → giả định → phản chứng. Nếu thiếu mắt xích, ghi điều chưa biết thay vì lấp bằng câu chuyện.

## Ôn bài cũ hoặc kiểm tra đầu vào

Ôn lại các chốt chặn cốt lõi từ những bài trước trong Nhánh 1: [Bài N8](N8-finding-verifying-sources.md) (nguồn gốc khác nguồn sao chép), [Bài 011](011-dcf-reverse-dcf.md) (`EV` khác vốn chủ), [Bài 012](012-scenarios-margin-of-safety.md) (ba kịch bản không phải lời tiên tri), và [Bài 015](015-behavior-decision-journal.md) (phải ghi luận điểm trước khi biết kết quả).

## Bài này làm gì và chưa làm gì

Ví dụ thật chỉ tập đọc một lát cắt lịch sử Apple FY2025. Đây chưa là báo cáo định giá Apple hoàn chỉnh, không có giá mục tiêu hay khuyến nghị. Kịch bản luyện tính dùng doanh nghiệp hư cấu riêng.

## 1. Đề bài và bảng số gốc

`Ý_KIẾN` Chọn một doanh nghiệp có hồ sơ công khai đọc được, ghi thị trường, đồng tiền, chuẩn và kỳ; bắt đầu bằng câu hỏi hẹp. Ví dụ: “Lợi nhuận FY2025 của Apple chuyển thành dòng tiền ra sao, cần đọc thêm gì để giải thích?”.

`SỰ_THẬT` Apple, Hoa Kỳ, US GAAP, hợp nhất; FY kết thúc 27/09/2025, đơn vị **triệu USD** trong 10-K:

| Chỉ tiêu gốc | FY2025 | Vị trí |
|---|---:|---|
| Doanh thu thuần |416.161|Báo cáo kết quả hoạt động|
| Lợi nhuận ròng |112.010|Cùng báo cáo|
| Tiền tạo từ hoạt động |111.482|Báo cáo lưu chuyển tiền|
| Tiền chi mua tài sản cố định |12.715|Dòng đầu tư; báo cáo trình bày khoản chi âm|

Nguồn gốc: [Apple 10-K](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm). Dấu chấm trong bảng là phân cách nghìn, không phải dấu thập phân. Giữ dấu gốc của dòng chi; khi dùng “mức chi capex” lấy độ lớn dương có giải thích.

`PHÉP_TÍNH` Biên ròng `112.010/416.161≈26,92%`; chuyển hóa tiền `111.482/112.010≈99,53%`; CFO trừ capex giản lược `111.482−12.715=98.767` triệu USD. Chỉ số cuối **không tự là FCFF hoặc FCFE đã chuẩn hóa**; còn phải kiểm phân loại lãi, khoản bất thường, trả công cổ phiếu và nhu cầu đầu tư. Một năm không chứng minh bền vững.

## 2. Từ số sang giả thuyết, rồi tìm phản chứng

`SUY_LUẬN` CFO gần lợi nhuận là một quan sát để nghiên cứu thêm, chưa đủ kết luận chất lượng lợi nhuận cao. Kiểm các năm, vốn lưu động, thuế một lần và thuyết minh. Báo cáo công ty là nguồn gốc của số công bố, nhưng cơ chế cần dữ liệu/nguồn độc lập phù hợp; chưa có thì ghi rõ chỉ một nguồn.

`Ý_KIẾN` Bộ hồ sơ nộp gồm: đề bài; bảng nguồn; bảng số gốc và chuyển đổi tách riêng; mô hình; rủi ro/bằng chứng trái chiều; điều chưa biết và điều kiện bác bỏ; nhật ký. Dùng [bảng thực hành](../practice/research-and-model-worksheets.md) để giữ mọi bước cùng địa chỉ.

## 3. Bài luyện kịch bản — tách khỏi Apple

`KỊCH_BẢN` Công ty Sao Biển hư cấu, FCFF năm tới 80/100/120 **tỷ đồng** ở bất lợi/cơ sở/thuận lợi. WACC 10%, g 2% chung; mô hình ổn định giản lược đã giả định tái đầu tư phù hợp. `PHÉP_TÍNH` EV tương ứng `80/0,08=1.000`, `100/0,08=1.250`, `120/0,08=1.500 tỷ`. Nếu nợ ròng 200 và 100 triệu cổ phần thì vốn chủ 800/1.050/1.300 tỷ, tương đương 8.000/10.500/13.000 đồng/cổ phần. Không dùng các con số này định giá Apple.

Sản phẩm hoàn thành khi người khác tái lập được số, chỉ được giả định chủ chốt và phản chứng. Công bố nghiên cứu thật còn cần kiểm nguồn/phản biện đúng phiên bản theo quy trình repo; bài học này không tự tạo một báo cáo đã duyệt.

## Ví dụ từ nguồn thật

Ví dụ Apple ở phần 1 là dữ liệu công bố lịch sử từ một doanh nghiệp thật. Các nguyên nhân kinh tế chưa được kết luận tại đây. `CHƯA_BIẾT` trong bài: số cần chuẩn hóa qua nhiều năm, bộ giả định định giá và giá thị trường cùng ngày; cách xác minh là mở hồ sơ kỳ tương ứng và nguồn giá sở giao dịch. Vì vậy không có kết luận đắt/rẻ.

## Năm câu hỏi khi đọc

1. Người khác có truy lại đúng bảng/số không?
2. Tỷ lệ giữ cùng kỳ/đơn vị/phạm vi không?
3. Kịch bản có bị trình bày như dữ kiện công ty thật không?
4. Phản chứng mạnh nhất và dữ liệu thiếu là gì?
5. Kiểm duyệt áp dụng đúng phiên bản và phạm vi nào?

## Bài tập — làm trước khi mở đáp án

Câu 1–3 là phần cốt lõi; câu 4–6 là luyện thêm và chuyển sang tình huống mới. Nếu chưa tự giải được phần cốt lõi, quay lại ví dụ rồi thử với đầu vào khác.

1. Tái tính biên ròng và chuyển hóa tiền Apple, ghi đơn vị.
2. Vì sao 98.767 chưa đủ để gọi là FCFF chuẩn hóa?
3. Tính EV/vốn chủ mỗi cổ phần của kịch bản cơ sở Sao Biển.
4. Viết một câu sự thật và một câu suy luận khác nhau từ bảng Apple.
5. Lập hồ sơ theo mẫu cho câu hỏi hẹp, chưa cần kết luận đầu tư.
6. Nếu người kiểm tìm lỗi làm đổi mô hình, biên bản cũ còn áp dụng không?

## Đáp án và điều cần hiểu

<details>
<summary>Mở sau khi tự làm</summary>

1. `PHÉP_TÍNH` Khoảng 26,92% và 99,53%; tử/mẫu cùng triệu USD nên tỷ lệ không có đơn vị tiền.
2. Cần xét dòng tiền thuộc ai, phân loại lãi/thuế, khoản bất thường và tái đầu tư; không chỉ trừ hai dòng.
3. `PHÉP_TÍNH` EV 1.250 tỷ, vốn chủ 1.050 tỷ, 10.500 đồng/cổ phần; kiểm cầu nối và thang đo.
4. Ví dụ: SỰ_THẬT CFO 111.482 triệu USD; SUY_LUẬN cần kiểm cầu nối vì CFO gần lợi nhuận chưa đủ giải thích chất lượng.
5. Đáp án mở: đủ câu hỏi, nguồn, phép tính, giả định, ba kịch bản khi định giá, phản chứng/unknown; không nộp thông tin tài khoản cá nhân.
6. Không nếu nội dung trọng yếu đổi; tính hash mới và kiểm lại. Không suy một hash hay cổng cấu trúc là bằng chứng nguồn đúng.

</details>

## Lỗi thường gặp

- Coi bài tổng kết là cuộc thi chọn mã.
- Lẫn tỷ đồng với triệuUSD.
- Bê kịch bản hư cấu sang công ty thật.
- Coi CFO−capex luôn là FCFF.
- Tuyên bố báo cáo đã duyệt chỉ vì có liên kết/biên bản cũ.

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị mua/bán/nắm giữ cá nhân hóa.
- Số hư cấu được gắn `KỊCH_BẢN`; phép tính không dự báo hay cam kết lợi nhuận.
- Trước khi áp dụng cho một thị trường, phải kiểm lại nguồn gốc, quy định và chuẩn kế toán tại đó.

## Điều tôi vẫn chưa hiểu

- Câu hỏi nào hiện chưa đủ bằng chứng trả lời?
- Nếu bỏ nguồn chính, có thể truy lại từ đâu?
- Điều gì làm luận điểm cần viết lại hoàn toàn?

## Nguồn Internet đã mở

Các nguồn được nhánh chuyên môn hoặc điều phối viên tìm kiếm và mở trong lượt triển khai ngày 26/10/2026. Ngày truy cập: `2026-10-26`. Không suy ngày thu thập thành ngày xuất bản. Phần công thức/ví dụ hư cấu là thiết kế bài học, không phải số thị trường.

| Nguồn | Kỳ/phiên bản, phạm vi | Dùng cho |
|---|---|---|
| [Apple FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | FY 27/09/2025; nộp 31/10/2025; Hoa Kỳ; US GAAP; hợp nhất; triệu USD; số lịch sử | Bảng gốc và tái tính; một nguồn gốc duy nhất cho số công bố |
| [SEC — Filing Detail](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/0000320193-25-000079-index.htm) | Hồ sơ nộp 31/10/2025; kỳ báo cáo 27/09/2025 | Phân biệt ngày nộp và kỳ |
| [Investor.gov — Using EDGAR](https://www.investor.gov/introduction-investing/getting-started/researching-investments/using-edgar-research-investments) | Hoa Kỳ; ngày xuất bản CHƯA_BIẾT | Truy hồ sơ và loại tài liệu |
| [Damodaran — Valuation](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/val.html) | NYU; phương pháp, ngày phiên bản CHƯA_BIẾT | Công thức kịch bản hư cấu |

Biên bản riêng cho đúng phiên bản: [kiểm nguồn](../reviews/016-fact-check.md), [phản biện](../reviews/016-risk-review.md). `CHƯA_BIẾT` hiệu quả học thực tế; không suy từ kiểm nguồn ra đã được người học nghiệm thu.

