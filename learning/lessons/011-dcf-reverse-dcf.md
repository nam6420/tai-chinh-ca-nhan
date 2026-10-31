# Bài 011 — DCF và định giá ngược: đọc giả định sau một mức giá

- Ngày viết lại: `2026-10-31`. Bản này **thay thế** bản 2026-10-26; các biên bản kiểm cũ gắn mã băm cũ, không còn áp dụng.
- Chốt dữ liệu lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Nguồn số Apple: Form 10-K FY2025 mở ngày `2026-10-31`.
- Mục tiêu: Dựng DCF năm giai đoạn trên số thật; kiểm tính nhất quán tái đầu tư–tăng trưởng; bắc cầu EV sang giá mỗi cổ phần; đảo mô hình để đọc giả định; đọc bảng độ nhạy.
- Bài trước liên quan: 004, 009, [010](010-cost-of-capital.md), N4. Học tiếp [012](012-scenarios-margin-of-safety.md).
- Thời lượng: 3 phiên (A: mục 1–3; B: mục 4–5; C: mục 6–8 và bài tập). Chưa đo thời gian học thực tế.
- Tệp thực hành: [valuation.py](../practice/models/valuation.py), [số Apple](../practice/models/apple_fy2025_inputs.csv) trong `learning/practice/models/`.
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/011-fact-check.md), [phản biện](../reviews/011-risk-review.md).
- Câu hỏi cốt lõi: **Giá trị ước tính đổi thế nào khi dòng tiền, thời gian tăng trưởng và tỷ lệ chiết khấu đổi — và một mức giá đang đòi hỏi ta tin điều gì?**

## Hiểu bài này trong 1 phút

Định giá giống việc trả tiền hôm nay để nhận một chuỗi khoản tiền tương lai có rủi ro. Cộng các khoản đã quy về hôm nay thì dễ; phần khó là (1) khoản tiền nào thật sự thuộc về ai, (2) tăng trưởng kéo dài bao lâu và cần bao nhiêu vốn để có nó, (3) phần nào của giá trị nằm ở "mãi mãi sau năm thứ năm". DCF (*discounted cash flow*, chiết khấu dòng tiền) không cho ta một con số đúng; nó cho ta một **bản dịch từ giả định sang giá trị**, và dịch ngược được từ giá sang giả định.

## Ôn bài cũ hoặc kiểm tra đầu vào

Trả lời bằng lời trước khi đọc tiếp (đáp án ở phần ẩn ngay dưới).

1. 004: vì sao lợi nhuận kế toán khác dòng tiền hoạt động?
2. 009: EV (*enterprise value*, giá trị doanh nghiệp) khác vốn chủ ở những khoản nào?
3. 010: dòng tiền cho mọi người cấp vốn chiết khấu bằng gì, dòng tiền riêng cổ đông bằng gì?
4. N4: tăng tỷ lệ chiết khấu thì giá trị hiện tại của cùng khoản nhận giảm hay tăng?

<details>
<summary>Mở sau khi tự làm</summary>

(1) Lợi nhuận là ghi nhận theo quy tắc kế toán, tiền là thu chi thực; chênh lệch ở vốn lưu động, khấu hao, khoản không dùng tiền. (2) Từ EV sang vốn chủ: trừ nợ, cộng tiền, điều chỉnh khoản khác. (3) FCFF dùng WACC, dòng tiền cổ đông dùng ke. (4) Giảm.

</details>

## Bài này làm gì và chưa làm gì

| Làm | Chưa làm |
|---|---|
| Dựng DCF năm năm + giá trị cuối kỳ, có kiểm nhất quán | Không đưa giá mục tiêu hay khuyến nghị mua/bán/nắm giữ |
| Dùng số báo cáo thật của Apple FY2025 làm điểm xuất phát | Không định giá Apple "đúng"; mọi giả định tương lai là giả định bài học |
| Đọc ngược giá thành giả định | Không hướng dẫn DCF cho ngân hàng, bảo hiểm (xem 013) |

## 1. Ghép đúng dòng tiền với người nhận

`SỰ_THẬT` Damodaran phân biệt FCFF (*free cash flow to the firm*, dòng tiền cho mọi người cấp vốn) chiết khấu bằng WACC, với FCFE (dòng tiền riêng cổ đông) chiết khấu bằng chi phí vốn cổ đông, và nêu không trộn lẫn hai bên. [Damodaran — Valuation](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/val.html). Hậu quả thực hành: nếu bạn chiết khấu FCFF thì phải **trừ nợ** khi đi từ EV sang vốn chủ; nếu chiết khấu FCFE thì giá trị ra thẳng là vốn chủ, không trừ nợ lần nữa.

`SUY_LUẬN` Tiền bán một nhà máy hay vay thêm không tự là dòng tiền hoạt động bền vững. Khi lấy một năm lịch sử làm gốc, hãy hỏi: năm đó có khoản bất thường nào không?

## 2. Khởi động bằng ví dụ hai năm (hư cấu)

`KỊCH_BẢN` Doanh nghiệp phi tài chính hư cấu, tỷ đồng danh nghĩa, dòng tiền cuối năm: FCFF1 = 100, FCFF2 = 110; từ năm 3 tăng 2%/năm mãi mãi; WACC 10%; nợ ròng 200; 100 triệu cổ phần sau pha loãng.

`PHÉP_TÍNH`

- FCFF3 = `110×1,02 = 112,2`.
- Giá trị cuối tại cuối năm 2: `TV2 = 112,2/(0,10−0,02) = 1.402,5`.
- EV = `100/1,1 + (110+1.402,5)/1,1² = 1.340,9091` tỷ.
- Vốn chủ = `1.340,9091 − 200 = 1.140,9091` tỷ; mỗi cổ phần = `≈ 11.409,09 đồng`.
- Phần TV đã chiết khấu: `1.402,5/1,21 ≈ 1.159,09`, bằng **86,44% EV**.

Ba điều cần thấy từ ví dụ nhỏ này: TV phải được chiết khấu về hôm nay; TV chiếm phần lớn giá trị; điều kiện `WACC > g` là bắt buộc để công thức TV có nghĩa.

## 3. Tăng trưởng không miễn phí: g = tái đầu tư × ROIC

`SUY_LUẬN` Muốn doanh nghiệp tăng trưởng g mãi mãi, nó phải giữ lại một phần lợi nhuận hoạt động để đầu tư. Ở trạng thái ổn định: `g = tỷ lệ tái đầu tư × ROIC`, nên `tỷ lệ tái đầu tư = g / ROIC`, và `FCFF = NOPAT × (1 − g/ROIC)`.

`KỊCH_BẢN` Công ty Gamma hư cấu có NOPAT năm tới 120 (NOPAT: lợi nhuận hoạt động sau thuế), tăng trưởng dài hạn 3%.

| ROIC cận biên dài hạn | Tái đầu tư = 3%/ROIC | FCFF = 120×(1−tái đầu tư) |
|---:|---:|---:|
| 15% | 20% | 96 |
| 10% | 30% | 84 |

`PHÉP_TÍNH` Cùng NOPAT và cùng g, chỉ đổi ROIC cận biên từ 15% xuống 10% làm dòng tiền cuối kỳ giảm `(96−84)/96 = 12,5%`. Bài học: **"g = 3%" không có nghĩa nếu không nói ROIC đi kèm**. Nếu ROIC dài hạn bằng WACC, tăng trưởng không tạo giá trị thêm (nối với 003 và 010).

## 4. Dựng dòng tiền xuất phát từ báo cáo thật

## Ví dụ từ nguồn thật

`SỰ_THẬT` [Form 10-K FY2025 của Apple](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) (kỳ kết thúc 27/09/2025, US GAAP, **triệu USD**): dòng tiền hoạt động 111.482; mua tài sản cố định 12.715; chi phí cổ phiếu thưởng (*share-based compensation*, SBC) 12.863; tiền và tương đương tiền 35.934; chứng khoán ngắn hạn 18.763 và dài hạn 77.723; thương phiếu 7.979; nợ dài hạn đến hạn 12.350 và không đến hạn 78.328; cổ phiếu đang lưu hành 14.776.353 nghìn (trang bìa, ngày 17/10/2025). Số nằm trong [tệp CSV](../practice/models/apple_fy2025_inputs.csv).

`PHÉP_TÍNH` Dòng tiền tự do quy ước theo hai mức:

| Cách tính | Công thức | Triệu USD |
|---|---|---:|
| FCF thô | `111.482 − 12.715` | 98.767 |
| FCF sau SBC | `111.482 − 12.715 − 12.863` | **85.904** |

Vì sao trừ SBC? SBC là chi phí thật bằng cổ phiếu: nó được cộng lại trong dòng tiền hoạt động vì không tốn tiền ngay, nhưng làm pha loãng cổ đông hiện hữu. `Ý_KIẾN` Có hai trường phái **không tương đương**: (a) trừ SBC khỏi dòng tiền như một chi phí tiền mặt (cách bài này dùng, thận trọng); (b) giữ SBC trong dòng tiền nhưng phải tính riêng giá trị các quyền đã cấp mà chưa chuyển thành cổ phiếu (RSU, quyền chọn đang lưu hành) và trừ khỏi vốn chủ, hoặc tăng số cổ phần tương ứng. Chia cho số cổ phiếu bình quân pha loãng của năm không thay thế bước đó. `CHƯA_BIẾT` Số RSU chưa vested của Apple chưa lấy từ thuyết minh; làm bài thật phải mở thuyết minh chi phí cổ phiếu thưởng.

`PHÉP_TÍNH` Cầu nối từ EV sang vốn chủ: tiền và chứng khoán `35.934+18.763+77.723 = 132.420`; nợ `7.979+12.350+78.328 = 98.657`; **tiền ròng +33.763**. Với Apple, tiền ròng dương nên *cộng* vào EV. `CHƯA_BIẾT` Bài chưa đưa nghĩa vụ thuê, thuế phải trả hoãn hay quyền lợi khác vào cầu nối; khi làm thật phải đọc thuyết minh.

`Ý_KIẾN` Hạn chế cần nêu: FCF = CFO − capex **không phải** FCFF chuẩn. Dòng tiền hoạt động đã trừ lãi vay đã trả và cộng lãi nhận được; Apple giữ 132.420 triệu USD tiền và chứng khoán nên thu nhập lãi nằm trong CFO. Nếu vừa để thu nhập lãi trong dòng tiền, vừa **cộng tiền** vào cầu nối, ta tính giá trị của tiền hai lần. Con số "thu nhập khác ròng −321" chỉ là số ròng nên không chứng minh sai lệch nhỏ. Cách làm chặt chẽ: `FCFF ≈ CFO − capex + lãi vay×(1−T) − thu nhập lãi×(1−T)`, cần thu nhập lãi và chi phí lãi từ thuyết minh (`CHƯA_BIẾT` trong bài này) và thuế biên. Trong bài này FCF được dùng như xấp xỉ thô, có thể thiên cao.

## 5. Mô hình năm giai đoạn trên số Apple

`KỊCH_BẢN` Các giả định dưới đây **không phải dự báo**: tăng trưởng FCF năm 1–5 giảm dần 6%; 5,5%; 5%; 4,5%; 4%; tăng trưởng dài hạn 3%; WACC 8,8% (đầu vào lấy từ giả định ở bài 010, người học tự thay bằng số mới tra). Xuất phát FCF0 = 85.904.

`PHÉP_TÍNH` (chạy [valuation.py](../practice/models/valuation.py))

| Năm | Tăng trưởng | FCF (triệu USD) |
|---:|---:|---:|
| 1 | 6,0% | 91.058 |
| 2 | 5,5% | 96.066 |
| 3 | 5,0% | 100.870 |
| 4 | 4,5% | 105.409 |
| 5 | 4,0% | 109.625 |

- Giá trị hiện tại năm 1–5: **390.299**.
- `TV5 = 109.625×1,03/(0,088−0,03) = 1.946.793`; chiết khấu `/1,088⁵` ra **1.276.954**.
- `EV = 390.299 + 1.276.954 = 1.667.254` triệu USD; **TV chiếm 76,6%**.
- Vốn chủ = `1.667.254 + 33.763 = 1.701.017`; chia `14.776,353 triệu cổ phiếu` ≈ **115,12 USD/cổ phiếu** (dùng số cổ phiếu bình quân pha loãng 15.004,697 triệu cho ≈ 113,37, nhưng đó **không** thay cho xử lý SBC đúng cách, xem mục 4).

Đây là kết quả của **bộ giả định này**, không phải giá trị của Apple. Dùng giả định khác, kết quả khác (mục 7).

**Chuẩn hóa FCF0 (cảnh báo bắt buộc).** `SỰ_THẬT` Theo 10-K FY2025, thuế thu nhập thực nộp bằng tiền năm đó là 43.369 triệu USD, so với chi phí thuế ghi nhận 20.719, và thuế phải trả giảm mạnh; 10-K còn nêu khoản ghi nhận và ký quỹ liên quan quyết định State Aid của châu Âu (từ năm trước) và 8,8 tỷ USD thuế chuyển đổi theo luật thuế Hoa Kỳ 2017 đến hạn trong 12 tháng; 10-K không cho biết mức ảnh hưởng của State Aid lên dòng tiền FY2025. `SUY_LUẬN` Một phần chênh lệch có thể là thanh toán thuế một lần làm CFO FY2025 thấp hơn mức "bình thường"; `CHƯA_BIẾT` phần nào, vì bài chưa tách được từ thuyết minh thuế. Hệ quả: FCF0 = 85.904 là FCF **thô, chưa chuẩn hóa**, và vì giá mô hình tỷ lệ thuận với FCF0, mỗi +10% FCF0 làm giá mỗi cổ phần đi từ 115,1 lên khoảng 126,4; +25% cho khoảng 143,3. Đồng thời quý 1–3 FY2026 đã được công bố trong 10-Q; bài này chỉ dùng 10-K FY2025 làm gốc, và sau khi Apple công bố kết quả quý 4 FY2026 mọi số cần rà lại.

Kiểm tra nhất quán tăng trưởng–tái đầu tư: tăng trưởng 3% mãi mãi cần **tái đầu tư ròng** (capex trừ khấu hao cộng thay đổi vốn lưu động hoạt động) dương. `PHÉP_TÍNH` Với số Apple: NOPAT xấp xỉ `133.050×(1−0,156) ≈ 112.294` (thu nhập hoạt động đã sau SBC; thuế suất hiệu dụng FY2025). Chi đầu tư ròng của năm là `12.715 − 11.698 = 1.017` (≈ 0,9% NOPAT), rất nhỏ. FCF sau SBC bằng `85.904/112.294 ≈ 76,5%` NOPAT; phần chênh khoảng 26.400 phần lớn **không** phải tái đầu tư mà đến từ thuế nộp tiền mặt vượt chi phí thuế (khoảng 22.650) và thay đổi vốn lưu động. `SUY_LUẬN` Vì vậy không suy ra ROIC cận biên từ tỷ số `FCF/NOPAT`: nó trộn thời điểm nộp thuế với tái đầu tư. Muốn kiểm nhất quán, tính tái đầu tư từ chi đầu tư ròng và vốn lưu động hoạt động nhiều năm, và ước lượng ROIC cận biên riêng (`CHƯA_BIẾT` trong bài này).

## 6. Đảo chiều: mức giá đang đòi hỏi giả định nào?

`SUY_LUẬN` Thay vì hỏi "giá trị là bao nhiêu", hỏi "với giá P, tăng trưởng 5 năm đầu phải là bao nhiêu để mô hình trả đúng P". Giữ WACC 8,8%, tăng trưởng dài hạn 3%, FCF0 = 85.904, tiền ròng 33.763, 14.776,353 triệu cổ phiếu.

`KỊCH_BẢN` Bốn mức giá. Ba mức đầu (150, 200, 250) là giả định để luyện; **mức 345 là giá đóng cửa AAPL ngày 30/10/2026 theo một nguồn thứ cấp** ([stockanalysis.com](https://stockanalysis.com/stocks/aapl/history/), mở 31/10/2026; chưa đối chiếu với sàn). Người học thay bằng giá tra tại ngày làm bài.

| Giá (USD) | EV hàm ý (triệu USD) | Tăng trưởng đều 5 năm đầu hàm ý (WACC 8,8%) | WACC hàm ý (giữ chuỗi tăng trưởng cơ sở) |
|---:|---:|---:|---:|
| 150 | 2.182.690 | ≈ 11,5%/năm | ≈ 7,4% |
| 200 | 2.921.508 | ≈ 18,7%/năm | ≈ 6,3% |
| 250 | 3.660.325 | ≈ 24,6%/năm | ≈ 5,7% |
| 345 | ≈ 5.064.079 | ≈ 33,5%/năm | ≈ 4,9% |

`PHÉP_TÍNH` Mỗi cột giải một phương trình một ẩn bằng chia đôi (`implied_growth()` cho cột tăng trưởng; cột WACC dùng `implied_wacc()`). Hai cột là **hai ẩn khác nhau**, mỗi cột giữ các đầu vào còn lại cố định; chúng không loại trừ nhau.

Điều bảng này **không** nói: không nói Apple đắt hay rẻ. Giá thị trường quan sát ở mức 345 cao hơn nhiều so với giá trị 115,1 của bộ giả định cơ sở; các lý do khả dĩ (chưa kiểm chứng): WACC 8,8% có thể cao hơn mức nhà đầu tư thực dùng; FCF0 chưa chuẩn hóa (mục 5); tăng trưởng gần đây cao hơn nhiều so với chuỗi giả định (`SỰ_THẬT` theo [10-Q quý 3 FY2026 của Apple](https://www.sec.gov/Archives/edgar/data/0000320193/000032019326000020/aapl-20260627.htm) (kỳ kết thúc 27/06/2026; doanh thu 109.417 so với 94.036, +16%; dịch vụ 30.739 so với 27.423, +12,1%; mở 31/10/2026); lưu ý đây là tăng trưởng doanh thu, khác đại lượng với chuỗi tăng trưởng FCF của mô hình); biên và giai đoạn tăng trưởng dài hơn; hoặc thị trường định giá sai. Việc của bạn là nêu bộ giả định nào hợp lý hơn **và vì sao**. `Ý_KIẾN` Tăng trưởng 33,5%/năm trong 5 năm rồi rơi xuống 3% là một "vách đá" khó tin; WACC hàm ý 4,9% thì thấp gần bằng lãi suất phi rủi ro giả định ở bài 010 và thấp hơn chi phí vốn cổ đông 8,95%, cũng khó chấp nhận. Cả hai nên khiến bạn kiểm lại **cả** giả định của mô hình **và** khả năng thị trường dùng giả định khác; bài không kết luận về cổ phiếu.

## 7. Bảng độ nhạy

`PHÉP_TÍNH` Giá mỗi cổ phần (USD) với chuỗi tăng trưởng mục 5, đổi WACC theo cột và tăng trưởng dài hạn theo hàng:

| g dài hạn \ WACC | 7,8% | 8,8% | 9,8% |
|---:|---:|---:|---:|
| 2% | 119,0 | 101,7 | 88,8 |
| 3% | 138,8 | **115,1** | 98,4 |
| 4% | 168,9 | 134,1 | 111,4 |

Cách đọc: đi từ ô giữa sang phải một nấc WACC (+1 điểm phần trăm) làm giá giảm `(115,1−98,4)/115,1 ≈ 14,5%`; đi lên một nấc g (+1 điểm) làm giá tăng ≈ 16,5%. Khi g tiến sát WACC, giá phình rất nhanh; đó là cảnh báo mô hình nhạy, không phải bằng chứng giá trị cao.

Thêm hai phép thử: không trừ SBC (FCF0 = 98.767) cho ≈ 132,0 USD, **cao hơn 14,7%** so với 115,1; chỉ riêng lựa chọn này đã lớn hơn nhiều chênh lệch giữa nhiều quan điểm. Giữ tăng trưởng đều 6% cả 5 năm (không giảm dần) cho ≈ 119,8. Thêm: FCF0 cao hơn 10% (nếu CFO FY2025 bị kéo thấp bởi thanh toán thuế một lần, mục 5) cho ≈ 126,4.

## 8. Quy trình đọc một DCF của người khác: năm câu hỏi

1. Dòng tiền thuộc ai (FCFF hay FCFE) và tỷ lệ chiết khấu có khớp không?
2. Tái đầu tư có khớp tăng trưởng không (g = tái đầu tư × ROIC)?
3. TV đặt tại năm nào, chiếm bao nhiêu % EV, tăng trưởng dài hạn so với tăng trưởng danh nghĩa kinh tế?
4. Cầu nối sang vốn chủ đã có nợ, tiền, thuê, quyền lợi thiểu số, pha loãng và SBC chưa?
5. Giả định nào chi phối kết quả (nhìn bảng độ nhạy trước khi tin con số)?

## Bài tập — làm trước khi mở đáp án

Câu 1–4 nhận biết và tính một bước; 5–8 tính nhiều bước; 9–10 chuyển giao. Mở đáp án chỉ sau khi tự làm.

1. Ví dụ mục 2: tính FCFF3, TV2, EV và vốn chủ.
2. TV2 ở mục 2 là giá trị tại thời điểm nào? Quy về hôm nay thế nào?
3. Vì sao dùng FCFF thì trừ nợ ròng còn FCFE thì không?
4. Công ty Gamma ở mục 3 đổi ROIC cận biên từ 15% xuống 10%: FCFF cuối kỳ giảm bao nhiêu %?
5. Mô hình ổn định: FCFF1 = 100, WACC 8%, g 3%. Tính EV; đổi WACC thành 9% thì EV đổi bao nhiêu %?
6. EV 1.500, FCFF1 = 100, WACC 8%: g hàm ý?
7. Dùng số Apple ở mục 4: nếu bạn giữ SBC trong dòng tiền (FCF0 = 98.767) thì phải xử lý SBC thế nào ở số cổ phần để không tính hai lần?
8. Chạy [valuation.py](../practice/models/valuation.py) với WACC 9,8% và g dài hạn 3%: kết quả có khớp ô tương ứng trong bảng mục 7 không?
9. (Chuyển giao) Chọn một công ty phi tài chính bạn quen, lấy CFO, capex, SBC, tiền, nợ và số cổ phiếu từ báo cáo mới nhất; tính FCF0 sau SBC và tiền ròng. Ghi kỳ, đơn vị, tiền tệ.
10. (Chuyển giao) Với công ty ở câu 9, viết ba giả định (WACC, g dài hạn, chuỗi tăng trưởng) **kèm lý do**, chạy mô hình và nộp bảng độ nhạy 3×3.

## Đáp án

<details>
<summary>Mở sau khi tự làm</summary>

1. `PHÉP_TÍNH` FCFF3 = 112,2; TV2 = 1.402,5; EV = 1.340,9091 tỷ; vốn chủ = 1.140,9091 tỷ.
2. Cuối năm 2; chia `1,1²`, được 1.159,09 tỷ, khoảng 86,44% EV.
3. FCFF thuộc mọi người cấp vốn; phần của chủ nợ phải trừ để còn vốn chủ. FCFE đã là dòng tiền sau khi trả lãi và gốc nợ nên chiết khấu ra thẳng vốn chủ; trừ nợ nữa là tính hai lần.
4. `120×(1−0,3)=84` so với `96`; giảm `12/96 = 12,5%`.
5. `100/(0,08−0,03)=2.000`; `100/(0,09−0,03)≈1.666,67`; giảm `≈16,7%`. Nhấn mạnh: một điểm phần trăm WACC đổi kết quả hơn một sáu phần.
6. `g = 0,08 − 100/1.500 ≈ 1,333%`. Đây là điều kiện tương thích, không phải dự báo.
7. Nếu giữ SBC trong dòng tiền thì phải tính riêng giá trị quyền đã cấp mà chưa vested (RSU, quyền chọn) và trừ khỏi vốn chủ, hoặc tăng số cổ phần tương ứng; dùng số cổ phiếu hiện tại hay bình quân pha loãng của năm không đủ. Cách thận trọng và đơn giản hơn là trừ SBC khỏi dòng tiền. Hai cách không tương đương hoàn toàn; chọn một và nêu rõ.
8. Có: 98,4 USD. Nếu lệch, kiểm số cổ phiếu (14.776,353 triệu), tiền ròng 33.763 và WACC nhập đúng `0.098`.
9. Rubric: đủ kỳ/đơn vị/tiền tệ (1đ); có trừ SBC hoặc nêu cách xử lý khác (1đ); tiền ròng tính đủ tiền, chứng khoán, nợ (1đ); nêu một khoản chưa đưa vào cầu nối (1đ).
10. Rubric: mỗi giả định có lý do dựa trên dữ liệu hoặc nguồn (3đ); bảng 3×3 đúng (1đ); một câu nói biến nào chi phối (1đ). Không chấm theo "giá đúng".

</details>

## Bài làm với dữ liệu thiếu hoặc lệch

Đề: "Công ty Zeta, FCFF năm nay 500 (triệu USD). Nợ ròng 1.200 tỷ VND. WACC 9%, g dài hạn 4%. Số cổ phần 80 triệu. Hãy tính giá mỗi cổ phần."

Việc phải làm trước khi tính: (a) FCFF tính bằng USD mà nợ bằng VND: không trừ được; cần tỷ giá tại cùng ngày hoặc đổi tất cả sang một tiền tệ; (b) WACC 9% bằng đồng tiền nào? Phải khớp tiền tệ của dòng tiền (xem 010); (c) "năm nay" là năm trước hay năm tới? TV cần FCFF năm kế tiếp; (d) chưa nêu thời gian tăng trưởng trước khi vào giai đoạn ổn định; (e) số cổ phần đã pha loãng chưa?

`Đáp án` Không tính được giá khi chưa trả lời (a)–(e). Cách đúng: liệt kê câu hỏi, nêu giả định tạm thời cho từng điểm, tính với giả định đó và gắn nhãn `KỊCH_BẢN`. Ghi `CHƯA_BIẾT` cho điều không có dữ liệu; không đoán tỷ giá.

## Sai ở đâu

Một học viên viết: "Apple FCF năm ngoái 98.767; tăng 5% mãi mãi; WACC 8%. EV = 98.767×1,05/(0,08−0,05) = 3.456.845 triệu USD; cộng nợ 98.657 và trừ tiền 132.420 được vốn chủ."

Tìm ít nhất bốn lỗi.

<details>
<summary>Mở sau khi tự tìm</summary>

1. Cộng nợ và trừ tiền: ngược dấu. Từ EV sang vốn chủ phải **trừ nợ, cộng tiền**.
2. Chiết khấu bằng WACC 8% nhưng dòng tiền chưa trừ SBC mà số cổ phiếu cũng không pha loãng thêm; thiếu xử lý SBC.
3. Tăng trưởng 5% mãi mãi gần sát WACC; thông thường tăng trưởng dài hạn danh nghĩa không vượt tăng trưởng nền kinh tế; phình giá trị.
4. Không có giai đoạn chuyển tiếp: chuyển thẳng từ tăng trưởng hiện tại sang vĩnh viễn.
5. Không kiểm tái đầu tư cho g = 5%.
6. Không có bảng độ nhạy.

</details>

## Kiểm tra chuyển bài

Làm không nhìn mẫu; đạt khi đúng cả ba.

1. Cho FCFF1 = 200, WACC 9%, g 3%, nợ ròng 500, 50 cổ phần: tính giá mỗi cổ phần và nêu đơn vị.
2. Giá thị trường mỗi cổ phần cho trước là 80 trong cùng dữ kiện: tăng trưởng g hàm ý là bao nhiêu (giữ nguyên các đầu vào khác) và nên hiểu thế nào?
3. Viết ba câu hỏi bạn sẽ hỏi trước khi tin một DCF do người khác trình bày.

<details>
<summary>Mở sau khi tự làm</summary>

Tiêu chí đạt: câu 1 `EV = 200/0,06 = 3.333,33`; vốn chủ `2.833,33`; giá `56,67`. Câu 2: `EV hàm ý = 80×50+500 = 4.500`; `g = 9% − 200/4.500 ≈ 4,556%`; nói rõ đây là một tổ hợp tương thích. Câu 3: bao gồm ít nhất ba mục trong năm câu hỏi mục 8.

</details>

## Lỗi thường gặp

- Chiết khấu FCFF bằng chi phí vốn cổ đông.
- Lấy FCF năm cuối thay năm kế tiếp trong TV.
- Quên chiết khấu TV.
- Dùng g ≥ WACC hoặc g dài hạn thiếu cơ sở.
- Xử lý SBC hai lần hoặc không xử lý.
- Gọi số mô hình là giá mục tiêu của công ty thật.

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị mua/bán/nắm giữ cá nhân hóa.
- Mọi giả định tương lai là `KỊCH_BẢN`; kết quả không là dự báo hay cam kết lợi nhuận. Giá 150, 200, 250 là giá giả định; giá 345 là số quan sát từ nguồn thứ cấp ngày 30/10/2026 và chỉ để đối chiếu, không phải kết luận đắt hay rẻ.
- Trước khi áp dụng cho một thị trường, kiểm lại nguồn gốc, quy định và chuẩn kế toán tại đó.

## Điều tôi vẫn chưa hiểu

- Nếu TV chiếm hơn 75% EV, tôi kiểm giả định nào trước?
- ROIC cận biên dài hạn của công ty tôi đang đọc là bao nhiêu và lấy ở đâu?
- Những khoản nào chưa vào cầu nối EV sang vốn chủ?

## Nguồn Internet đã mở

Truy cập `2026-10-31`. Không suy ngày truy cập thành ngày xuất bản.

| Nguồn | Phạm vi | Dùng cho |
|---|---|---|
| [Apple Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm) | Hoa Kỳ; US GAAP; kỳ 27/09/2025; triệu USD | Mọi số Apple ở mục 4–7 |
| [Damodaran — Valuation](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/val.html) | Phương pháp; mở 31/10/2026; ngày phiên bản `CHƯA_BIẾT` | FCFF/FCFE ghép với WACC/ke; giới hạn tăng trưởng ổn định |
| [Damodaran — FCFF notes](https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/fcff.pdf) | Slide, ví dụ năm 2000 | Tỷ lệ tái đầu tư = g/ROC |
| [stockanalysis.com — lịch sử giá AAPL](https://stockanalysis.com/stocks/aapl/history/) | Nguồn thứ cấp; đóng cửa 30/10/2026 = 344,63 | Mức giá 345 ở mục 6; chưa đối chiếu sàn |

Trang Damodaran — Valuation (mở 31/10/2026) nêu luật ghép dòng tiền với tỷ lệ chiết khấu và việc tăng trưởng vô hạn không nên vượt tăng trưởng nền kinh tế quá một biên nhỏ (trang nêu 2–3 điểm; trang DDM của Damodaran nêu 1–2 điểm). Slide FCFF của Damodaran ([fcff.pdf](https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/fcff.pdf), trang 4) nêu tỷ lệ tái đầu tư kỳ vọng bằng `g/ROC`; công thức tổng quát `g = tỷ lệ tái đầu tư × ROIC` là dạng viết lại của ví dụ đó. Mọi phép tính tái lập bằng [valuation.py](../practice/models/valuation.py).
