# Bài A2 — Quỹ mở, ETF, chi phí và sai lệch theo dõi

- Ngày: `2026-10-27`
- Chốt dữ liệu lúc: `2026-10-27 11:34 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Tính NAV/đơn vị, phân biệt cách giao dịch quỹ mở và ETF, đọc phí và phân biệt hai loại sai lệch chỉ số.
- Bài trước liên quan: [N5](N5-portfolio-index-investing.md), [N8](N8-finding-verifying-sources.md), [B1](B1-broker-fees-custody.md).
- Câu hỏi cốt lõi: Quỹ nắm gì, đơn vị được mua bán ở giá nào, và mọi chi phí ảnh hưởng kết quả ra sao?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/A2-fact-check.md), [phản biện](../reviews/A2-risk-review.md).

## Hiểu bài trong một phút

Quỹ gom vốn để nắm một danh mục tài sản. Giá trị tài sản ròng cho biết phần còn lại sau nợ; giá giao dịch ETF trên sàn có thể khác giá trị đó. Chi phí có thể nằm trong tài sản quỹ hoặc được tính riêng khi giao dịch, nên không được cộng hai lần một khoản đã phản ánh trong kết quả.

## 1. Quỹ mở và ETF

`SỰ_THẬT` [SEC Hoa Kỳ — đặc điểm quỹ mở và ETF](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/characteristics-mutual-funds-exchange-traded-funds) giải thích quỹ mở phát hành/mua lại đơn vị quỹ theo giá xác định trên NAV, còn chứng chỉ ETF giao dịch trên sàn theo giá thị trường trong phiên. Điều kiện giao dịch, thời điểm định giá và pháp luật cụ thể phụ thuộc quỹ và quốc gia; SEC không xác định hợp đồng cho mọi quỹ Việt Nam.

`SỰ_THẬT` [SEC — Net Asset Value](https://www.investor.gov/introduction-investing/investing-basics/glossary/net-asset-value): NAV là giá trị tài sản trừ nợ; NAV mỗi đơn vị bằng NAV chia số đơn vị lưu hành. `KỊCH_BẢN` Tài sản 1.050 triệu, nợ 50 triệu, 100.000 đơn vị: `PHÉP_TÍNH` NAV = 1.000 triệu, NAV/đơn vị = 10.000 đồng. Tài sản được định giá theo chính sách của quỹ, không tự bảo đảm giá bán thực tế từng khoản.

ETF có thể mô phỏng chỉ số hoặc có chiến lược khác; không mặc định mọi quỹ được quản lý thụ động. Chỉ số và thành phần, phương pháp theo dõi, độ tập trung và điều kiện giao dịch phải đọc trong tài liệu quỹ.

## 2. Giá sàn, NAV và phí

`KỊCH_BẢN` NAV/đơn vị 21.000 đồng, giá ETF trên sàn 21.210 đồng. `PHÉP_TÍNH` Giá cao hơn NAV `(21.210 − 21.000)/21.000 = 1%`, gọi là mức cao hơn NAV (premium); ngược lại là mức thấp hơn NAV (discount). Giá khớp thực tế còn phụ thuộc sổ lệnh và thời điểm; khi giao dịch thưa thớt, có thể khó bán nhanh hoặc giá lệch NAV nhiều hơn. [SEC — cảnh báo ETF](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-24), Hoa Kỳ, nêu rủi ro thị trường ETF có thể không hình thành hoặc duy trì. Ví dụ không phải giá một quỹ thật.

[SEC — phí quỹ mở và ETF](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/mutual-fund-and-etf-fees-and-expenses-investor-bulletin), 23/07/2025, phân biệt chi phí hoạt động của quỹ với phí giao dịch, chênh lệch giá mua/bán và những khoản phát sinh ngoài bảng phí quỹ. Đọc biểu phí phát hành/mua lại, phí quản lý, chi phí khác, môi giới và thuế theo sản phẩm. `CHƯA_BIẾT` Mức thực tế, cách hạch toán và ngày hiệu lực của từng quỹ/kênh: xem bản cáo bạch, điều lệ và biểu phí mới nhất.

`KỊCH_BẢN` Mua 250 đơn vị quỹ mở; sau đó NAV là 21.000 đồng/đơn vị và phí mua lại giả định 1%. Bỏ thuế, phí khác và giả định toàn bộ được mua lại ở NAV này: `PHÉP_TÍNH` giá trị trước phí = 250 × 21.000 = 5.250.000; phí = 52.500; tiền còn lại = 5.197.500 đồng. Đây không là báo giá hay cam kết kết quả.

## 3. Hai cách đo khoảng cách với chỉ số

Theo [NSE Ấn Độ — tracking error](https://www.nseindia.com/static/products-services/indices-tracking-error), sai lệch theo dõi liên quan độ lệch chuẩn của chênh lệch lợi suất quỹ và chỉ số; đây là nguồn phương pháp, không thay quy định Việt Nam. [SEBI — quy định về quỹ thụ động tại Ấn Độ](https://www.sebi.gov.in/sebi_data/attachdocs/may-2022/1653307308174.pdf), mục V, phân biệt tracking error với tracking difference; phương pháp công bố cụ thể tại Ấn Độ có quy đổi theo năm. Trong ví dụ học tập dưới đây, *tracking difference* là chênh lệch lợi suất quỹ và chỉ số trong một kỳ xác định. *Tracking error* là thước đo độ biến động của chênh lệch lợi suất qua nhiều kỳ; công thức, tần suất và cách quy đổi phụ thuộc phương pháp hoặc quy định được áp dụng. Không gọi một con số chênh lệch lợi suất của một kỳ là tracking error.

`KỊCH_BẢN` Một kỳ quỹ tăng 4%, chỉ số tăng 5%: `PHÉP_TÍNH` chênh lệch = 4% − 5% = −1 điểm phần trăm. Con số một kỳ không đủ tính độ biến động của chênh lệch qua nhiều kỳ. `CHƯA_BIẾT` Tracking error thực tế của quỹ cụ thể, cách tính theo văn bản và kỳ được công bố; kiểm phương pháp và dữ liệu gốc trước khi so sánh.

## 4. Đọc bản cáo bạch và điều lệ

`Ý_KIẾN` Tìm mục tiêu, tài sản và giới hạn, chỉ số tham chiếu, rủi ro, phí, lịch giao dịch, định giá, lưu ký và cơ chế mua lại; kiểm ngày và phiên bản. Giấy đăng ký hay việc được phép chào bán không tự bảo đảm quỹ có lãi hay giữ nguyên vốn. Kết quả quá khứ không bảo đảm kết quả tương lai.

## Năm câu hỏi khi đọc

1. Quỹ nắm gì, theo chỉ số nào và tập trung vào đâu?
2. Mua/bán theo lịch và giá NAV hay khớp giá trên sàn?
3. Phí nào đã nằm trong NAV, phí nào trả riêng, có bị tính hai lần không?
4. Chênh lệch quỹ–chỉ số là một kỳ hay độ biến động qua nhiều kỳ?
5. Bản cáo bạch, điều lệ, báo cáo và biểu phí là phiên bản ngày nào?

## Bài tập

1. Tài sản 2 tỷ, nợ 200 triệu, 90.000 đơn vị: NAV/đơn vị?
2. NAV 20.000, giá ETF 20.400: cao hơn NAV bao nhiêu phần trăm?
3. 100 đơn vị có NAV 20.000, phí mua lại 1%, bỏ khoản khác: tiền sau phí?
4. Quỹ tăng 3%, chỉ số tăng 5%: chênh lệch bao nhiêu điểm phần trăm?
5. Có thể gọi chênh lệch của câu 4 là tracking error không?
6. Nêu hai khoản có thể phải xem ngoài phí quản lý của quỹ.

## Đáp án

1. `(2.000.000.000 − 200.000.000)/90.000 = 20.000` đồng/đơn vị.
2. `(20.400 − 20.000)/20.000 = 2%`.
3. Giá trị 2.000.000; phí 20.000; còn 1.980.000 đồng theo giả định.
4. `3% − 5% = −2` điểm phần trăm.
5. Không; cần chuỗi chênh lệch và phương pháp tính độ biến động.
6. Ví dụ: phí mua lại, môi giới, chênh lệch giá mua/bán, thuế hoặc chi phí khác.

## Lỗi thường gặp và ranh giới an toàn

Nhầm NAV với giá khớp, tracking difference với tracking error, hoặc trừ lại chi phí đã nằm trong lợi suất NAV. Không có quỹ, tỷ trọng hoặc lịch mua bán nào được đề xuất cho cá nhân.

## Điều tôi vẫn chưa hiểu

`CHƯA_BIẾT` Phí thực tế, cách giao dịch và sai lệch theo dõi của từng quỹ tại ngày sử dụng; cần đọc tài liệu chính thức đúng phiên bản và quy định áp dụng.

## Nguồn Internet đã mở

Truy cập `2026-10-27`: [SEC — đặc điểm quỹ mở và ETF](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/characteristics-mutual-funds-exchange-traded-funds); [SEC — NAV](https://www.investor.gov/introduction-investing/investing-basics/glossary/net-asset-value); [SEC — phí quỹ](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/mutual-fund-and-etf-fees-and-expenses-investor-bulletin), 23/07/2025. [NSE Ấn Độ — tracking error](https://www.nseindia.com/static/products-services/indices-tracking-error), không ghi ngày; [SEBI — quỹ thụ động](https://www.sebi.gov.in/sebi_data/attachdocs/may-2022/1653307308174.pdf), 23/05/2022, Ấn Độ; [SEC — cảnh báo ETF](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-24), 23/02/2023, Hoa Kỳ. Các trang SEC là giáo dục Hoa Kỳ; ví dụ số hư cấu.
