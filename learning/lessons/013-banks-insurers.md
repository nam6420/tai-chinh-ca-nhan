# Bài 013 — Ngân hàng và bảo hiểm: hai mô hình cần đọc riêng

- Ngày: `2026-10-26`
- Chốt dữ liệu lúc: `2026-10-26 17:12 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Giải thích nguồn lợi nhuận và rủi ro của ngân hàng/phi nhân thọ; tính NIM, CET1 và tỷ lệ kết hợp giả định; biết giới hạn nhân thọ.
- Bài trước liên quan: N2,005,007,009; hai phiên A ngân hàng và B bảo hiểm, không bắt buộc trước016 nếu chọn doanh nghiệp phi tài chính.
- Thời lượng: Hai hoặc ba phiên ngắn theo điểm dừng; chưa đo thời gian học thực tế.
- Câu hỏi cốt lõi: **Vì sao tiền gửi và phí bảo hiểm không giống doanh thu của một cửa hàng?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

## Hiểu bài này trong 1 phút

Ngân hàng nhận vốn rồi cấp tín dụng và dịch vụ; tổn thất tín dụng có thể xuất hiện muộn hơn thu nhập lãi. Công ty bảo hiểm thu phí trước rồi chịu nghĩa vụ bồi thường tương lai. Nhiều tiền đang giữ không có nghĩa là nhiều tiền tự do cho cổ đông.

## Ôn bài cũ hoặc kiểm tra đầu vào

005: trả lãi được chưa bảo đảm trả nợ gốc đúng hạn. 007: chính sách/dự phòng làm cách đọc lợi nhuận thay đổi. Hai ý này đặc biệt quan trọng với tín dụng và bồi thường.

## Bài này làm gì và chưa làm gì

Phiên A: ngân hàng; phiên B: bảo hiểm phi nhân thọ rồi giới hạn nhân thọ. Không đưa ngưỡng vốn pháp lý chung cho mọi nước, không áp EV/EBITDA máy móc.

## Phần A — Ngân hàng: lãi chênh lệch chưa phải toàn bộ lợi nhuận

`SỰ_THẬT` Tài liệu nghiên cứu do Federal Reserve công bố định nghĩa NIM bằng thu nhập lãi ròng chia tài sản sinh lãi. [IFDP1197](https://www.federalreserve.gov/econresdata/ifdp/2017/files/ifdp1197.pdf). Ví dụ dưới dùng tài sản sinh lãi bình quân năm và chưa điều chỉnh tương đương thuế; báo cáo thật có thể điều chỉnh theo định nghĩa riêng, phải đối chiếu trước khi so. Còn có thu nhập phí, chi phí vận hành, tổn thất tín dụng và thuế.

`KỊCH_BẢN` Đơn vị tỷ đồng, ngân hàng hư cấu trong một năm: thu lãi120, trả lãi70, tài sản sinh lãi bình quân1.000. `PHÉP_TÍNH` NIM = `(120−70)/1.000=5%`. Sau phí ròng10, chi phí vận hành30 và dự phòng tín dụng20, lợi nhuận trước thuế giả định chỉ `50+10−30−20=10`, không phải50.

Nợ xấu phụ thuộc định nghĩa, phân loại và kỳ; tỷ lệ thấp không bảo đảm tổn thất tương lai thấp. Vốn CET1 là vốn cổ phần phổ thông cấp1 theo quy định; tỷ lệ CET1 = vốn CET1/tài sản có trọng số rủi ro (RWA). RWA không bằng tổng tài sản kế toán. Cần kiểm cơ quan sở tại, bộ đệm và phương pháp; tỷ lệ không tự bảo đảm thanh khoản.

## Phần B — Bảo hiểm: tách khai thác với đầu tư

`SỰ_THẬT` NAIC định nghĩa tỷ lệ kết hợp bằng tổng tỷ lệ tổn thất và tỷ lệ chi phí. [NAIC](https://content.naic.org/glossary-insurance-terms). Định nghĩa mẫu số cần đọc đúng báo cáo; đừng tự ghép hai tỷ lệ khác cơ sở. [Báo cáo Allstate](https://www.allstatecorporation.com/resources/allstate/attachments/annual-report/allstate-year-end-report-combo-2025.pdf).

`KỊCH_BẢN` Bảo hiểm phi nhân thọ hư cấu, cùng kỳ và cùng cơ sở phí đã kiếm được1.000: bồi thường và chi phí liên quan650, chi phí khai thác250. `PHÉP_TÍNH` Tỷ lệ tổn thất65%, chi phí25%, kết hợp90%; chênh khai thác100 trước đầu tư/thuế/các khoản khác. Bồi thường tăng200 làm kết hợp110%, lỗ khai thác100. Lãi đầu tư có thể bù một phần nhưng không xóa nghĩa vụ.

Khoản phí thu trước mà chưa phải chi ngay tạo nguồn tiền để đầu tư trong thời gian giữ, thường gọi float. Không gọi đó là vốn miễn phí: nghĩa vụ bồi thường, dự phòng và chi phí khai thác vẫn còn. [Berkshire FY2025, phần bảo hiểm](https://www.berkshirehathaway.com/2025ar/2025ar.pdf).

## Giới hạn — Không bê phi nhân thọ sang nhân thọ

`SỰ_THẬT` IFRS17 tách kết quả dịch vụ bảo hiểm với thu nhập/chi phí tài chính bảo hiểm. [IFRS Foundation](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-17-insurance-contracts/). Với nhân thọ cần đọc thời hạn nghĩa vụ, giả định tử vong/duy trì hợp đồng, tài sản đảm bảo và rủi ro lãi suất; combined ratio không là bộ đo thay thế. Các công ty US GAAP không mặc định trình bày như IFRS17.

Điểm dừng mỗi phần: chỉ ra một cách “lợi nhuận đẹp” vẫn đi cùng rủi ro nghĩa vụ tương lai.

## Ví dụ từ nguồn thật

`SỰ_THẬT` JPMorgan Chase FY2025, Hoa Kỳ, US GAAP, nêu hai tỷ lệ CET1 cuối31/12/2025: Standardized14,6% và Advanced14,1% (mục Regulatory capital, bảng tỷ lệ theo phương pháp Standardized/Advanced). [PDF doanh nghiệp](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2025/4th-quarter/corp-10k-2025.pdf). Cùng ngân hàng vẫn có hai số do cách tính; không chọn số cao để tuyên bố an toàn hơn. Ví dụ này không phải ngưỡng vốn áp dụng cho Việt Nam.

## Năm câu hỏi khi đọc

1. Lợi nhuận đến từ lãi, phí, khai thác hay đầu tư?
2. Dự phòng có cùng định nghĩa và kỳ không?
3. Mẫu số là tài sản bình quân, RWA hay phí đã kiếm?
4. Thanh khoản và nghĩa vụ tương lai nằm ở đâu?
5. Chuẩn kế toán/quy định có cho so trực tiếp không?

## Bài tập — làm trước khi mở đáp án

Câu 1–3 là phần cốt lõi; câu 4–6 là luyện thêm và chuyển sang tình huống mới. Nếu chưa tự giải được phần cốt lõi, quay lại ví dụ rồi thử với đầu vào khác.

1. Tính NIM và lợi nhuận trước thuế ngân hàng hư cấu.
2. CET1=80,RWA=800: tỷ lệ? Tổng tài sản1.200 có thay được RWA không?
3. Tính tỷ lệ kết hợp và chênh khai thác của ví dụ bảo hiểm.
4. Tổn thất tăng200, các yếu tố khác giữ nguyên: tỷ lệ kết hợp và chênh khai thác?
5. NIM tăng hoặc nợ xấu thấp có đủ kết luận ngân hàng tốt không?
6. Vì sao không dùng combined ratio của phi nhân thọ để kết luận hiệu quả nhân thọ?

## Đáp án và điều cần hiểu

<details>
<summary>Mở sau khi tự làm</summary>

1. `PHÉP_TÍNH` 5% và10 tỷ; NIM không phải biên lãi ròng toàn doanh nghiệp.
2. `PHÉP_TÍNH` 80/800=10%; không thay bằng1.200 vì RWA là cơ sở quy định khác.
3. `PHÉP_TÍNH` 65%+25%=90%; chênh100 trước các khoản đã loại.
4. `PHÉP_TÍNH` (850+250)/1.000=110%; chênh−100.
5. Không; cần chất lượng tín dụng, cấu trúc tài sản, vốn, thanh khoản, phí/chi phí và định nghĩa số.
6. Nghĩa vụ/thời hạn/giả định khác nhau; cần bộ đo, dự phòng và chuẩn kế toán tương ứng.

</details>

## Lỗi thường gặp

- Coi tiền gửi giống doanh thu bán hàng.
- Gọi NIM là lợi nhuận cuối cùng.
- Thay RWA bằng tài sản kế toán.
- Cộng tỷ lệ khác mẫu số.
- Coi float là tiền không có nghĩa vụ hoặc dùng ngưỡng nước khác.

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị mua/bán/nắm giữ cá nhân hóa.
- Số hư cấu được gắn `KỊCH_BẢN`; phép tính không dự báo hay cam kết lợi nhuận.
- Trước khi áp dụng cho một thị trường, phải kiểm lại nguồn gốc, quy định và chuẩn kế toán tại đó.

## Điều tôi vẫn chưa hiểu

- Tỷ lệ vốn có yêu cầu bộ đệm nào tại quốc gia đang học?
- Dự phòng phản ánh dữ liệu và giả định nào?
- Tài sản và nghĩa vụ có lệch kỳ hạn/tiền tệ không?

## Nguồn Internet đã mở

Các nguồn được nhánh chuyên môn hoặc điều phối viên tìm kiếm và mở trong lượt triển khai ngày 26/10/2026. Ngày truy cập: `2026-10-26`. Không suy ngày thu thập thành ngày xuất bản. Phần công thức/ví dụ hư cấu là thiết kế bài học, không phải số thị trường.

| Nguồn | Kỳ/phiên bản, phạm vi | Dùng cho |
|---|---|---|
| [Federal Reserve — IFDP1197](https://www.federalreserve.gov/econresdata/ifdp/2017/files/ifdp1197.pdf) | 02/2017; nghiên cứu đa quốc gia, không phải ngưỡng quản lý | Định nghĩa NIM; không áp kết quả định lượng nghiên cứu vào ví dụ |
| [NAIC — Glossary](https://content.naic.org/glossary-insurance-terms) | Hoa Kỳ; ngày xuất bản CHƯA_BIẾT; định nghĩa chung có thể khác theo thực thể | Tỷ lệ kết hợp |
| [OCC — Earnings](https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/earnings/pub-ch-earnings.pdf) | Hoa Kỳ; bản1.0,09/2021; có ghi sửa tham chiếu20/03/2025 | Tài liệu bổ sung; root mở được, nhánh kiểm nguồn gặp lỗi truy cập; định nghĩa chính dùng Fed |
| [JPMorgan Chase FY2025 10-K PDF](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2025/4th-quarter/corp-10k-2025.pdf) | 31/12/2025; US GAAP; bảng vốn triệu USD; tỷ lệ% | CET1 Standardized/Advanced |
| [Allstate 2025 Annual Report trong tệp kết hợp2026 Proxy](https://www.allstatecorporation.com/resources/allstate/attachments/annual-report/allstate-year-end-report-combo-2025.pdf) | FY2025; Hoa Kỳ; US GAAP; phần báo cáo năm, không phần thư quảng bá | Định nghĩa tỷ lệ kết hợp |
| [Berkshire FY2025 Annual Report](https://www.berkshirehathaway.com/2025ar/2025ar.pdf) | FY2025; Hoa Kỳ; US GAAP; phần định nghĩa float | Float gắn với nghĩa vụ và chi phí |
| [IFRS Foundation — IFRS17](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-17-insurance-contracts/) | Chuẩn quốc tế; áp dụng tùy quốc gia; trang hiện hành | Tách kết quả dịch vụ và tài chính |

Biên bản riêng cho đúng phiên bản: [kiểm nguồn](../reviews/013-fact-check.md), [phản biện](../reviews/013-risk-review.md). `CHƯA_BIẾT` hiệu quả học thực tế; không suy từ kiểm nguồn ra đã được người học nghiệm thu.

