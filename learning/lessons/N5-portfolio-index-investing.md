# Bài N5 — Danh mục, đa dạng hóa và đầu tư theo chỉ số

- Ngày: `2026-10-26`
- Chốt dữ liệu lúc: `2026-10-26 17:08 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Nhận ra rủi ro tập trung và giới hạn đa dạng hóa; đọc mục tiêu/chi phí quỹ; tính lợi suất đơn giản không lẫn tiền góp.
- Bài trước liên quan: Phần A: sau N1, không chặn 001. Phần B: sau [N4](N4-time-value-returns.md) và [N7](N7-data-probability-uncertainty.md).
- Thời lượng: Hai hoặc ba phiên ngắn theo điểm dừng; chưa đo thời gian học thực tế.
- Câu hỏi cốt lõi: **Kết quả đầu tư cần so với điều gì và đang gánh những rủi ro nào?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

## Hiểu bài này trong 1 phút

Một doanh nghiệp có thể tốt mà cổ phiếu vẫn giảm. Giữ nhiều mã cùng phụ thuộc một yếu tố cũng chưa chắc phân tán rủi ro. Quỹ chỉ số là một cách tiếp cận để tìm hiểu, không phải cam kết an toàn hay lời khuyên chọn quỹ cụ thể.

## Ôn bài cũ hoặc kiểm tra đầu vào

Phần A chỉ cần N1: cổ phiếu là sở hữu hay khoản gửi được bảo đảm? Sở hữu, không bảo đảm. Phần B: N4 cho100 tăng10% thành110; N7 nhắc hai tỷ lệ khác mốc không thể ghép tùy ý.

## Bài này làm gì và chưa làm gì

Phần A dạy khái niệm danh mục/quỹ; có thể dừng trước phần B. Phần B dạy đo kết quả/chi phí và một bài tổng kết nhánh quỹ. Không thiết kế tỷ trọng cho tài chính cá nhân.

## Phần A — Danh mục và quỹ (sau N1)

`SỰ_THẬT` Investor.gov giải thích đa dạng hóa giữa các nhóm tài sản và trong mỗi nhóm; nó không bảo đảm tránh lỗ khi thị trường giảm. [Phân bổ](https://www.investor.gov/introduction-investing/getting-started/asset-allocation), [giới hạn](https://www.investor.gov/introduction-investing/investing-basics/save-and-invest/diversify-your-investments). Hai trang cùng thuộc SEC, không tính là hai cơ quan độc lập.

`SỰ_THẬT` Quỹ chỉ số tìm cách theo dõi một chỉ số; quỹ ETF là quỹ giao dịch trên sàn. Không phải mọi ETF đều theo chỉ số, không phải chỉ số nào cũng phân tán rộng. [Index Funds](https://www.investor.gov/introduction-investing/investing-basics/investment-products/mutual-funds-and-exchange-traded-4). Cần đọc tài sản, phương pháp, mức tập trung và chi phí. Có thể **dừng tại đây**, quay lại B sau N4/N7.

## Phần B1 — Tính kết quả, không tính tiền góp thành lãi

`KỊCH_BẢN` Danh mục100 triệu gồm60 cổ phiếu và40 tiền mặt, không góp/rút; cổ phiếu giảm20%, tiền mặt giả định không sinh lãi. `PHÉP_TÍNH` Cuối kỳ `60×0,8+40=88`, lợi suất−12%. Đây không là tỷ trọng đề xuất. Nếu mọi tài sản rủi ro cùng giảm, giữ nhiều mã vẫn có thể lỗ.

Đo kết quả so với mốc có cùng kỳ, tiền tệ, phạm vi và cách tính cổ tức. `SỰ_THẬT` Mốc tổng lợi suất có tính tái đầu tư cổ tức/khoản phân phối khác chỉ số chỉ phản ánh giá. [S&P Dow Jones Indices — Methodology Matters](https://www.spglobal.com/spdji/en/research-insights/index-literacy/methodology-matters/). Khi có dòng tiền, chia kỳ ở thời điểm góp/rút rồi ghép lợi suất: `(1+r1)×(1+r2)−1`.

`KỊCH_BẢN` Đầu100 tăng10% thành110; góp100, sau đó210 tăng10% thành231. `PHÉP_TÍNH` Lãi tiền31; lợi suất ghép theo thời gian `1,1²−1=21%`, không phải131%. Hiệu quả tiền thực của người góp còn phụ thuộc thời điểm; không coi21% là lợi suất cá nhân theo tiền khi có góp.

## Phần B2 — Phí và bài tổng kết nhánh quỹ

`KỊCH_BẢN` Gộp5%/năm, phí cuối năm bằng1% tài sản sau tăng trưởng: hệ số sau phí `1,05×0,99=1,0395`, tương đương3,95%, trước thuế. Quy ước thu phí chỉ để tính minh họa, không mô tả mọi quỹ. `SỰ_THẬT` SEC phân biệt phí giao dịch và chi phí thường xuyên; đọc hồ sơ quỹ để tránh tính phí đã nằm trong lợi suất công bố thêm lần nữa. [Phí quỹ](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/mutual-fund-and-etf-fees-and-expenses-investor-bulletin).

**Tái cân bằng** là đưa cơ cấu trở lại mức mục tiêu đã xác định trong mô hình. `SỰ_THẬT` Investor.gov mô tả có thể điều chỉnh qua mua/bán hoặc dòng tiền góp thêm; phải xét chi phí/thuế. Ví dụ hư cấu, chưa phí/thuế: đầu60 cổ phiếu/40 tiền mặt, cổ phiếu tăng50% thành90, tiền vẫn40; tổng130, tỷ trọng cổ phiếu90/130≈69,23%. Muốn trở lại60/40 trong mô hình, mức cổ phiếu là130×60%=78, tức chuyển12 sang tiền mặt, còn78/52. Đây là bài tính, không khuyến nghị tỷ trọng hoặc lịch giao dịch.

Bài tổng kết nhánh quỹ: chọn một tài liệu quỹ công khai, ghi chỉ số/tài sản, rủi ro tập trung, phí, tiền tệ và mốc so sánh. Trả ba câu: điều đã biết, điều chưa biết và dữ kiện sẽ làm đổi cách hiểu. Không cần hoàn thành DCF hay kế toán để làm bài này.

## Ví dụ từ nguồn thật

`SỰ_THẬT` Hướng dẫn báo cáo hiệu quả của Fidelity phân biệt lợi suất đầu tư theo thời gian với lợi suất cá nhân theo tiền, vì thời điểm góp/rút ảnh hưởng trải nghiệm người đầu tư. Đây là mô tả phương pháp của tổ chức Hoa Kỳ, không khuyến nghị sản phẩm hay so sánh hiệu quả quỹ. [Fidelity](https://www.fidelity.com/webcontent/ap002390-mlo-content/20.04/help/learn_performancereporting.shtml). Phí thực phải đọc hồ sơ đúng quỹ/lớp chứng chỉ/ngày hiệu lực.

## Năm câu hỏi khi đọc

1. Đang phân tán rủi ro thật hay chỉ tăng số mã?
2. Quỹ nắm gì và tập trung ở đâu?
3. Phí đã nằm trong số lợi suất chưa?
4. Mốc so sánh cùng kỳ/tiền tệ/cổ tức không?
5. Tôi có đang nhầm tiền góp thành kết quả đầu tư?

## Bài tập — làm trước khi mở đáp án

Câu 1–3 là phần cốt lõi; câu 4–6 là luyện thêm và chuyển sang tình huống mới. Nếu chưa tự giải được phần cốt lõi, quay lại ví dụ rồi thử với đầu vào khác.

1. Phần A: 20 cổ phiếu cùng một ngành có bảo đảm đa dạng hóa tốt không?
2. Phần A: quỹ chỉ số có bảo đảm không mất tiền không?
3. Phần B: tính kết quả danh mục60/40 trong ví dụ giảm20%.
4. Tính lợi suất ghép khi kỳ1 tăng10%, kỳ2 giảm10%, không góp/rút.
5. 100 triệu theo quy ước tăng5% rồi thu1% phí mỗi năm, sau2năm còn bao nhiêu?
6. Với ví dụ tái cân bằng90/40, tính mức tài sản sau khi trở lại60/40; sau đó làm bài tổng kết bằng một tài liệu công khai.

## Đáp án và điều cần hiểu

<details>
<summary>Mở sau khi tự làm</summary>

1. Không; có thể cùng chịu cú sốc giá, lãi suất hoặc quy định. Kiểm yếu tố chung.
2. Không; phụ thuộc tài sản/chỉ số và các rủi ro khác. Kiểm giới hạn lời hứa.
3. `PHÉP_TÍNH` 88 triệu, −12%; tỷ trọng là giả định.
4. `PHÉP_TÍNH` 1,1×0,9−1=−1%; trung bình số học0% không phải kết quả kép.
5. `PHÉP_TÍNH` 100×1,0395²=108,056025 triệu, trước thuế. Không trừ phí lần nữa nếu số công bố đã sau phí.
6. `PHÉP_TÍNH` Tổng130; mục tiêu78/52, chuyển12 từ cổ phiếu sang tiền, trước phí/thuế. Bài tổng kết đủ địa chỉ nguồn, tập trung, phí/đơn vị, mốc và điều chưa biết; không chọn quỹ/tỷ trọng cho cá nhân.

</details>

## Lỗi thường gặp

- Đếm mã thay cho kiểm rủi ro chung.
- Coi ETF và quỹ chỉ số là một khái niệm.
- So chỉ số giá với lợi suất có cổ tức.
- Tính tiền góp là lợi nhuận.
- Trừ phí hai lần hoặc sao thuế nước khác.

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị mua/bán/nắm giữ cá nhân hóa.
- Số hư cấu được gắn `KỊCH_BẢN`; phép tính không dự báo hay cam kết lợi nhuận.
- Trước khi áp dụng cho một thị trường, phải kiểm lại nguồn gốc, quy định và chuẩn kế toán tại đó.

## Điều tôi vẫn chưa hiểu

- Rủi ro nào đa dạng hóa không loại bỏ?
- Mốc phù hợp cần điều chỉnh tiền tệ/cổ tức ra sao?
- Quỹ đổi phương pháp thì phải đọc lại phần nào?

## Nguồn Internet đã mở

Các nguồn được nhánh chuyên môn hoặc điều phối viên tìm kiếm và mở trong lượt triển khai ngày 26/10/2026. Ngày truy cập: `2026-10-26`. Không suy ngày thu thập thành ngày xuất bản. Phần công thức/ví dụ hư cấu là thiết kế bài học, không phải số thị trường.

| Nguồn | Kỳ/phiên bản, phạm vi | Dùng cho |
|---|---|---|
| [Investor.gov — Asset Allocation](https://www.investor.gov/introduction-investing/getting-started/asset-allocation) | Hoa Kỳ; ngày xuất bản CHƯA_BIẾT | Đa dạng hóa và tái cân bằng |
| [Investor.gov — Diversify](https://www.investor.gov/introduction-investing/investing-basics/save-and-invest/diversify-your-investments) | Hoa Kỳ; ngày xuất bản CHƯA_BIẾT | Giới hạn tránh thua lỗ |
| [Investor.gov — Index Funds](https://www.investor.gov/introduction-investing/investing-basics/investment-products/mutual-funds-and-exchange-traded-4) | Hoa Kỳ; ngày xuất bản CHƯA_BIẾT | Khái niệm và rủi ro chỉ số |
| [SEC — Mutual Fund and ETF Fees](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/mutual-fund-and-etf-fees-and-expenses-investor-bulletin) | 23/07/2025; Hoa Kỳ; không lấy mức phí hiện hành | Các lớp phí |
| [S&P Dow Jones Indices — Methodology Matters](https://www.spglobal.com/spdji/en/research-insights/index-literacy/methodology-matters/) | Phương pháp chỉ số; ngày xuất bản CHƯA_BIẾT | Price return và total return |
| [Fidelity — Performance](https://www.fidelity.com/webcontent/ap002390-mlo-content/20.04/help/learn_performancereporting.shtml) | Hoa Kỳ; phương pháp báo cáo, ngày xuất bản CHƯA_BIẾT | Lợi suất theo thời gian và theo tiền |

Biên bản riêng cho đúng phiên bản: [kiểm nguồn](../reviews/N5-fact-check.md), [phản biện](../reviews/N5-risk-review.md). `CHƯA_BIẾT` hiệu quả học thực tế; không suy từ kiểm nguồn ra đã được người học nghiệm thu.

