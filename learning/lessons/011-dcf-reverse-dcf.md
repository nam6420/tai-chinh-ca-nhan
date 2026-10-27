# Bài 011 — DCF và định giá ngược: đọc giả định sau một mức giá

- Ngày: `2026-10-26`
- Chốt dữ liệu lúc: `2026-10-26 17:04 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Chiết khấu mô hình hai giai đoạn; dựng cầu nối EV sang vốn chủ; đảo một mô hình đơn giản để đọc kỳ vọng.
- Bài trước liên quan: 004,009,[010](010-cost-of-capital.md),N4. Học tiếp012.
- Thời lượng: Hai hoặc ba phiên ngắn theo điểm dừng; chưa đo thời gian học thực tế.
- Câu hỏi cốt lõi: **Giá trị ước tính đổi thế nào khi dòng tiền và tỷ lệ chiết khấu đổi?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

## Hiểu bài này trong 1 phút

Định giá giống trả tiền hôm nay để nhận những khoản tiền tương lai có rủi ro. Công thức cộng các khoản quy về hôm nay khá đơn giản; phần khó là khoản nào thật sự thuộc về ai và giả định kéo dài bao lâu.

## Ôn bài cũ hoặc kiểm tra đầu vào

004: lợi nhuận khác dòng tiền. 009: EV khác vốn chủ. 010: FCFF dùng WACC, dòng tiền cổ đông dùng ke. Nếu chưa phân biệt ba cặp này, quay lại bài trước.

## Bài này làm gì và chưa làm gì

Dạy một mô hình nhỏ và giới hạn, không phải mô hình hoàn chỉnh cho doanh nghiệp thật. Không dùng FCFF cho ngân hàng một cách máy móc.

## 1. Ghép đúng dòng tiền với người nhận

`SỰ_THẬT` Damodaran phân biệt FCFF, tiền cho mọi người cấp vốn, chiết khấu bằng WACC; FCFE, tiền riêng cổ đông, dùng chi phí vốn cổ đông. [Khung tiếp cận](https://pages.stern.nyu.edu/adamodar/New_Home_Page/lectures/approach.html). Tiền bán máy bất thường hoặc vay thêm không tự là năng lực tiền hoạt động bền vững.

## 2. Hai năm cụ thể rồi giai đoạn ổn định

`KỊCH_BẢN` Doanh nghiệp phi tài chính hư cấu, tỷ đồng danh nghĩa; dòng tiền cuối năm: FCFF1=100, FCFF2=110; từ năm3 tăng2%/năm mãi mãi, WACC10% cố định. Bỏ các tài sản/quyền lợi khác ngoài nợ ròng200 và100 triệu cổ phần sau pha loãng. Dòng tiền đã phản ánh nhu cầu tái đầu tư phù hợp với tăng trưởng giả định.

`PHÉP_TÍNH`

- FCFF3 = `110×1,02=112,2`.
- Giá trị cuối năm2: `TV2=112,2/(0,10−0,02)=1.402,5`.
- EV hôm nay = `100/1,1+(110+1.402,5)/1,1²=1.340,9091` tỷ.
- Vốn chủ = `1.340,9091−200=1.140,9091` tỷ; mỗi cổ phần = `1.140,9091 tỷ/100 triệu≈11.409,09 đồng`.

Không quên chiết khấu TV2 về hôm nay: `1.402,5/1,21≈1.159,09`, khoảng86,44% EV. Kết quả phụ thuộc lớn giả định sau năm2. Điều kiện của công thức TV là `WACC>g`, cùng tiền tệ/cách đo và tăng trưởng ổn định khả thi. [Khung DCF](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/val.html).

## 3. Đảo chiều: mức giá đang cần giả định nào?

`KỊCH_BẢN` Một mô hình ổn định khác có EV1.500, FCFF năm tới100, WACC8%. `PHÉP_TÍNH` Nếu giữ FCFF1 như đầu vào độc lập, `g=8%−100/1.500≈1,333%`. Đây là một tổ hợp giả định tương thích, không chứng minh “thị trường thật sự tin g này”. Giá có thể phản ánh dòng tiền/rủi ro rất khác.

Đổi một biến mỗi lần rồi viết lại câu kết luận. Nếu g tiến sát WACC, kết quả phình lớn: đó là cảnh báo mô hình nhạy, không phải bằng chứng giá trị cao chắc chắn.

## Ví dụ từ nguồn thật

`SỰ_THẬT` Apple FY2025 công bố báo cáo dòng tiền và chi đầu tư trong10-K, cùng thuyết minh các khoản khác. [Hồ sơ](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm). Đây là nơi tìm đầu vào lịch sử; không thể lấy một năm dòng tiền rồi tự gọi là dòng tiền vĩnh viễn. Mô hình100/110 ở trên hoàn toàn hư cấu, không phải định giá Apple.

## Năm câu hỏi khi đọc

1. Dòng tiền thuộc ai?
2. Tái đầu tư đã khớp tăng trưởng chưa?
3. TV đặt tại cuối năm nào?
4. Đã điều chỉnh nợ/tài sản/quyền lợi khác và pha loãng chưa?
5. Giả định nào chi phối phần lớn kết quả?

## Bài tập — làm trước khi mở đáp án

Câu 1–3 là phần cốt lõi; câu 4–6 là luyện thêm và chuyển sang tình huống mới. Nếu chưa tự giải được phần cốt lõi, quay lại ví dụ rồi thử với đầu vào khác.

1. Tính FCFF3 và TV2 theo ví dụ.
2. Tính EV và vốn chủ, giải thích vì sao phải trừ nợ ròng.
3. TV2 là giá trị hôm nay hay cuối năm2?
4. Mô hình ổn định FCFF1=100, WACC8%,g3%: EV? Đổi WACC9% thì sao?
5. EV1.500,FCFF1=100,WACC8%: g hàm ý?
6. Giữ tăng trưởng nhưng cắt tái đầu tư tùy ý làm FCFF tăng: vấn đề gì?

## Đáp án và điều cần hiểu

<details>
<summary>Mở sau khi tự làm</summary>

1. `PHÉP_TÍNH` 112,2 và1.402,5 tỷ; dùng dòng tiền năm3 ở tử số.
2. `PHÉP_TÍNH` EV1.340,9091 tỷ, vốn chủ1.140,9091 tỷ. Nợ là quyền đòi của người cấp vốn khác.
3. Cuối năm2, phải chia1,1² để quy về hôm nay; kiểm thời điểm.
4. `PHÉP_TÍNH` 100/(0,08−0,03)=2.000; 100/(0,09−0,03)≈1.666,67. Tỷ lệ chỉ là giả định.
5. `PHÉP_TÍNH` 0,08−100/1.500≈0,013333; không phải dự báo chắc chắn.
6. Tăng trưởng có thể không còn nguồn lực hỗ trợ; phải xét hiệu quả vốn và nhu cầu tái đầu tư, không chỉ chỉnh một ô để ra giá cao.

</details>

## Lỗi thường gặp

- Chiết khấu FCFF bằng ke.
- Lấy FCFF năm cuối thay năm kế tiếp trong TV.
- Quên chiết khấu TV.
- Dùng g≥WACC hoặc tăng trưởng dài hạn thiếu cơ sở.
- Gọi giá trị hư cấu là giá mục tiêu công ty thật.

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị mua/bán/nắm giữ cá nhân hóa.
- Số hư cấu được gắn `KỊCH_BẢN`; phép tính không dự báo hay cam kết lợi nhuận.
- Trước khi áp dụng cho một thị trường, phải kiểm lại nguồn gốc, quy định và chuẩn kế toán tại đó.

## Điều tôi vẫn chưa hiểu

- Nếu TV chiếm phần lớn EV, cần kiểm giả định nào trước?
- Khoản nợ/tài sản nào chưa vào cầu nối?
- Thay một mô hình khác có cùng giá nhưng giả định khác được không?

## Nguồn Internet đã mở

Các nguồn được nhánh chuyên môn hoặc điều phối viên tìm kiếm và mở trong lượt triển khai ngày 26/10/2026. Ngày truy cập: `2026-10-26`. Không suy ngày thu thập thành ngày xuất bản. Phần công thức/ví dụ hư cấu là thiết kế bài học, không phải số thị trường.

| Nguồn | Kỳ/phiên bản, phạm vi | Dùng cho |
|---|---|---|
| [Damodaran — Approaches](https://pages.stern.nyu.edu/adamodar/New_Home_Page/lectures/approach.html) | NYU; phương pháp, ngày phiên bản CHƯA_BIẾT | Ghép dòng tiền/tỷ lệ |
| [Damodaran — Valuation](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/val.html) | NYU; phương pháp, ngày phiên bản CHƯA_BIẾT | DCF và tăng trưởng ổn định |
| [Apple FY2025 Form10-K](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Hoa Kỳ; US GAAP; FY27/09/2025; triệu USD | Địa chỉ đầu vào lịch sử, không định giá Apple |

Biên bản riêng cho đúng phiên bản: [kiểm nguồn](../reviews/011-fact-check.md), [phản biện](../reviews/011-risk-review.md). `CHƯA_BIẾT` hiệu quả học thực tế; không suy từ kiểm nguồn ra đã được người học nghiệm thu.

