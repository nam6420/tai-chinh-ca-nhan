# Bài M1 — Tiền tệ, lãi suất, tỷ giá và tín dụng Việt Nam

- Ngày: `2026-10-27`
- Chốt dữ liệu lúc: `2026-10-27 11:41 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Đọc đúng kỳ và mẫu số của dữ liệu tín dụng; giải thích các kênh truyền dẫn có điều kiện của lãi suất và tỷ giá.
- Bài trước liên quan: [008](008-macro-transmission.md), [N7](N7-data-probability-uncertainty.md), [A5](A5-international-investing-currency-tax.md).
- Câu hỏi cốt lõi: Chính sách, thị trường và doanh nghiệp có thể liên hệ với nhau bằng những kênh nào, và điều gì còn chưa biết?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/M1-fact-check.md), [phản biện](../reviews/M1-risk-review.md).

## Hiểu bài trong một phút

Ngân hàng trung ương tác động đến điều kiện tiền tệ, nhưng lãi suất điều hành không đồng nhất với lãi vay của từng doanh nghiệp. Tỷ giá, tín dụng và lạm phát phản ứng qua nhiều kênh và độ trễ; một con số đơn lẻ không chứng minh nguyên nhân hay dự báo giá cổ phiếu.

## 1. Lãi suất và tín dụng

`SỰ_THẬT` [BIS — Monetary and fiscal policy](https://www.bis.org/publications/aer-2023/monetary-fiscal-policy-safeguarding-stability-trust), báo cáo năm 2023, mô tả chính sách tiền tệ truyền qua lãi suất, chi phí vay, giá tài sản và tỷ giá. Đây là khung quốc tế; mức tác động thực tế ở Việt Nam phụ thuộc hợp đồng, thời gian tái định giá, cung/cầu tín dụng và kỳ vọng.

`KỊCH_BẢN` Dư nợ thả nổi 1 tỷ VND không đổi, lãi suất áp dụng tăng 1 điểm phần trăm/năm sau khi tái định giá. `PHÉP_TÍNH` Chi phí lãi đơn tăng khoảng `1 tỷ × 1% = 10 triệu VND/năm`, trước trả gốc, thuế và phí. Đây không phải dự báo lãi vay hay ước lượng truyền dẫn cho toàn nền kinh tế.

`SỰ_THẬT` [Cục Thống kê — báo cáo quý III và 9 tháng 2026](https://www.nso.gov.vn/bai-top/2026/10/bao-cao-tinh-hinh-kinh-te-xa-hoi-quy-iii-va-9-thang-nam-2026/) ghi đến 28/09/2026 tín dụng nền kinh tế tăng 10,89% và huy động vốn của các tổ chức tín dụng tăng 9,78% so với cuối năm 2025. Đây là thay đổi từ đầu năm đến ngày đo, không phải mức tăng 12 tháng hay số dư tuyệt đối. Một mức tăng không tự chứng minh chính sách nới lỏng hoặc chất lượng khoản vay.

## 2. Tỷ giá và doanh nghiệp

VND/USD tăng nghĩa là cần nhiều VND hơn cho một USD. `KỊCH_BẢN` Doanh nghiệp phải trả 1 triệu USD, tỷ giá giả định tăng từ 25.000 lên 25.250 VND/USD. `PHÉP_TÍNH` Chi phí quy đổi tăng `1.000.000 × 250 = 250 triệu VND`, trước phòng hộ, phí và thay đổi điều khoản hợp đồng.

`SUY_LUẬN` Doanh nghiệp có nguồn thu USD có thể hưởng lợi khi quy đổi, trong khi bên nhập khẩu hoặc có nợ USD có thể chịu chi phí cao hơn. Tác động ròng phụ thuộc cả nguồn thu/chi cùng đồng tiền, phòng hộ, giá bán và lượng hàng; không thể kết luận chỉ từ ngành hay một tỷ giá.

## 3. Sổ theo dõi đúng kỳ

| Dữ liệu | Ghi gì? | Nguồn cần kiểm |
|---|---|---|
| Lãi suất | Loại lãi suất, kỳ hạn, ngày hiệu lực và bên trả | Ngân hàng Nhà nước, ngân hàng hoặc hợp đồng |
| Tỷ giá | Chiều tỷ giá, ngày, tỷ giá trung tâm hay giao dịch | Ngân hàng Nhà nước và báo giá phù hợp |
| Tín dụng | Số dư hoặc tăng trưởng, mốc so sánh, phạm vi tổ chức/ngành | Cục Thống kê, Ngân hàng Nhà nước |
| Giá và tăng trưởng | Tháng/quý/năm, so kỳ trước hay cùng kỳ, bản sơ bộ/sửa đổi | Cục Thống kê |

`CHƯA_BIẾT` Lãi suất điều hành, tỷ giá giao dịch, dự trữ và cơ cấu tín dụng mới nhất tại ngày chốt chưa được xác nhận riêng trong bài; phải mở dữ liệu gốc trước khi dùng. Không điền từ ví dụ giả định.

## Năm câu hỏi khi đọc

1. Chỉ tiêu đo số dư, mức tăng từ đầu năm hay cùng kỳ?
2. Lãi suất nào, của ai, kỳ hạn và ngày hiệu lực?
3. Tỷ giá ghi VND/USD hay USD/VND, nguồn và thời điểm?
4. Doanh nghiệp vay/thu/chi bằng đồng nào và có phòng hộ không?
5. Bằng chứng nào khác có thể giải thích diễn biến?

## Bài tập

1. Dư nợ 2 tỷ, lãi tăng 1 điểm %/năm: chi phí đơn giản tăng bao nhiêu?
2. Trả 1 triệu USD khi tỷ giá tăng 100 VND/USD: chênh lệch bao nhiêu VND?
3. Tín dụng tăng từ cuối năm có tự là mức tăng 12 tháng không?
4. Lãi suất điều hành có tự bằng lãi vay của mọi doanh nghiệp không?
5. Doanh thu USD có tự bảo đảm hưởng lợi khi VND yếu đi không?
6. Nêu hai trường cần ghi khi trích dữ liệu tín dụng.

## Đáp án

1. `2 tỷ × 1% = 20 triệu VND/năm`, theo giả định.
2. `1 triệu × 100 = 100 triệu VND`, trước phòng hộ và phí.
3. Không; mẫu số và kỳ khác nhau.
4. Không; lãi vay tùy kỳ hạn, hợp đồng và điều kiện thị trường.
5. Không; phải xét cả chi phí, nợ, phòng hộ và nhu cầu.
6. Ngày đo, mốc so sánh, phạm vi, đơn vị và phiên bản nguồn.

## Lỗi thường gặp và ranh giới an toàn

Nhầm điểm phần trăm với phần trăm, đổi chiều tỷ giá hoặc dùng tương quan làm quan hệ nhân quả. Bài không dự báo tỷ giá/lãi suất hay khuyến nghị giao dịch.

## Điều tôi vẫn chưa hiểu

`CHƯA_BIẾT` Truyền dẫn cụ thể theo ngành, lãi suất/tỷ giá và tín dụng mới nhất của một đối tượng; cần dữ liệu gốc và giả định công khai.

## Nguồn Internet đã mở

Truy cập `2026-10-27`: [Cục Thống kê — quý III/9 tháng 2026](https://www.nso.gov.vn/bai-top/2026/10/bao-cao-tinh-hinh-kinh-te-xa-hoi-quy-iii-va-9-thang-nam-2026/), mốc tín dụng 28/09/2026; [BIS — chính sách tiền tệ và tài khóa](https://www.bis.org/publications/aer-2023/monetary-fiscal-policy-safeguarding-stability-trust), 2023. Các tỷ giá/lãi vay trong ví dụ hư cấu.
