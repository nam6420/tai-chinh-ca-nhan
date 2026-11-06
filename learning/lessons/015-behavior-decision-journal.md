# Bài 015 — Tâm lý, bảng tự kiểm và nhật ký quyết định

- Ngày: `2026-10-26`
- Chốt dữ liệu lúc: `2026-10-26 17:12 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Nhận diện ba kiểu thiên lệch; viết dự đoán có thể kiểm lại; tách quy trình với kết quả và lưu phản chứng.
- Bài trước liên quan: Thứ tự đọc **Bước 22/23 của Nhánh 1** — học sâu ngay sau [Bài 012: Kịch bản, biên an toàn và điều kiện bác bỏ](012-scenarios-margin-of-safety.md) (và chuỗi thực hành [Bài Q4](Q4-getting-data-edgar-xbrl-vietnam.md) → [Bài Q2](Q2-sbc-dilution-buybacks-dividends.md) → [Bài Q1](Q1-earnings-quality-toolkit.md) → [Bài Q3](Q3-normalizing-earnings-cyclical.md); có thể dùng nghi thức nhật ký ngay từ [Bài 001](001-business-financial-statements.md)). Học tiếp: [Bài 016: Bài tổng kết nghiên cứu doanh nghiệp](016-company-research-capstone.md) (Bước 23/23).
- Thời lượng: Hai hoặc ba phiên ngắn theo điểm dừng; chưa đo thời gian học thực tế.
- Câu hỏi cốt lõi: **Làm sao biết mình đang tìm sự thật hay chỉ bảo vệ ý kiến ban đầu?**
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`

## Hiểu bài này trong 1 phút

Một lần đúng có thể do may mắn; một quyết định có cơ sở vẫn có thể gặp kết quả xấu. Muốn học được, phải ghi mình đã tin gì trước khi biết kết quả, điều gì có thể làm mình sai và khi nào xem lại.

## Ôn bài cũ hoặc kiểm tra đầu vào

Ôn lại [Bài N7 — Đọc dữ liệu và bất định](N7-data-probability-uncertainty.md) (tránh dùng thông tin tương lai để đánh giá hiểu biết quá khứ) và [Bài 012 — Kịch bản, biên an toàn và điều kiện bác bỏ](012-scenarios-margin-of-safety.md) (điều kiện bác bỏ phải gắn với cơ chế kinh doanh, không chỉ nhìn giá cổ phiếu). Nhớ hai điều này trước khi viết nhật ký.

## Bài này làm gì và chưa làm gì

Dạy kỷ luật học tập và quyết định mô phỏng, không chẩn đoán tâm lý và không cam kết nhật ký làm tăng lợi nhuận. Không yêu cầu chia sẻ tiền hay danh mục cá nhân.

## 1. Ba hành vi dễ làm lệch cách đọc

`SỰ_THẬT` SEC tổng hợp các kiểu hành vi của nhà đầu tư Hoa Kỳ, gồm giao dịch tích cực, xu hướng bán khoản lãi/giữ khoản lỗ, quen thuộc và đa dạng hóa thiếu phù hợp. [Bản tin SEC](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-72). Đây là mô tả nghiên cứu, không dự đoán hành vi của mọi cá nhân.

`Ý_KIẾN` Khi tự học, thử nhận diện: **quen thuộc** — hiểu tên thương hiệu nên tưởng hiểu rủi ro; **neo** — giữ chặt một mức giá cũ dù dữ kiện đã đổi; **chọn bằng chứng thuận ý** — đọc thông tin xác nhận và bỏ phản chứng. Hai khái niệm sau là khung câu hỏi tự kiểm trong bài, không phải chẩn đoán dựa trên một giao dịch.

## 2. Ghi trước, không sửa lại quá khứ

`KỊCH_BẢN` Một hồ sơ hư cấu: trước kết quả, bạn dự kiến doanh thu quý sau 100–110, vì lượng khách ổn định; bằng chứng chống là khách đang kéo dài thời gian trả. Kết quả đạt 108 nhưng tiền thu giảm mạnh.

`SUY_LUẬN` Dự đoán doanh thu đúng không tự xác nhận luận điểm dòng tiền. Giữ nguyên ghi chép cũ, thêm bản nhìn lại và tách điều đúng, điều sai, thông tin mới. Nếu sửa dự đoán cũ thành 105–110 sau khi biết 108, bạn mất khả năng học từ sai số.

Dùng [mẫu nhật ký](../../templates/decision-journal.md): điều tin; nguồn ủng hộ/phản đối; giả định/mức tự tin; điều kiện đổi ý; mốc xem lại. Ghi thông tin mô phỏng, không thông tin tài chính cá nhân.

## 3. Bảng tự kiểm trước và sau

`Ý_KIẾN` Trước: (1) câu hỏi cụ thể; (2) nguồn/kỳ/đơn vị; (3) kịch bản bất lợi; (4) bằng chứng mạnh nhất chống lại; (5) điều chưa biết; (6) điều kiện/mốc kiểm lại. Sau: thông tin mới nào xuất hiện; lỗi do dữ liệu/phép tính/cơ chế hay rủi ro đã nhận diện; thay đổi bước nào trong quy trình.

`PHÉP_TÍNH` Nếu giá mô phỏng tăng 10% nhưng mốc phù hợp tăng 15%, chênh kết quả là −5 điểm phần trăm, chưa đủ kết luận có/không có kỹ năng từ một kỳ. So cùng tiền tệ, cổ tức, phí và rủi ro. Điểm dừng: viết một phản chứng khiến bạn không thoải mái nhưng phải giữ lại.

## Ví dụ từ nguồn thật

`SỰ_THẬT` Bản tin hành vi SEC dẫn báo cáo do Library of Congress nghiên cứu về hành vi nhà đầu tư Hoa Kỳ. Ví dụ này cho thấy có thể xem xét hành vi có hệ thống thay vì kể chuyện một cá nhân thắng/thua. Tài liệu không chứng minh riêng quy trình nhật ký của bài giúp kiếm lời; đó vẫn là thiết kế học tập cần quan sát.

## Năm câu hỏi khi đọc

1. Tôi viết dự đoán trước hay sau sự kiện?
2. Có giữ lại bằng chứng trái chiều không?
3. Quen thương hiệu có đang thay hiểu mô hình không?
4. So kết quả cùng mốc và rủi ro chưa?
5. Tôi sẽ sửa bước nào, thay vì chỉ tự khen hoặc tự trách?

## Bài tập — làm trước khi mở đáp án

Câu 1–3 là phần cốt lõi; câu 4–6 là luyện thêm và chuyển sang tình huống mới. Nếu chưa tự giải được phần cốt lõi, quay lại ví dụ rồi thử với đầu vào khác.

1. Kết quả tốt có chứng minh quy trình tốt không? Giải thích.
2. Với ví dụ 108, cần xem lại điều gì ngoài doanh thu?
3. Viết một dòng điều kiện đổi ý có dữ kiện và ngày xem lại.
4. Tăng 10% so mốc 15%: chênh bao nhiêu điểm phần trăm?
5. Vì sao không sửa dự đoán cũ sau sự kiện?
6. Làm một nhật ký mô phỏng ngắn với ít nhất một nguồn chống lại luận điểm.

## Đáp án và điều cần hiểu

<details>
<summary>Mở sau khi tự làm</summary>

1. Không; kết quả có rủi ro và may rủi. Cần xem nguồn, giả định và chuỗi quyết định, không một lần thắng.
2. Tiền thực thu, phải thu, thời hạn và chất lượng khách; doanh thu đúng chưa đủ.
3. Đáp án mở: chỉ tiêu, nguồn, kỳ và hành động nghiên cứu lại; không chỉ 'nếu giá giảm'.
4. `PHÉP_TÍNH` 10%−15%=−5 điểm phần trăm; chưa đủ suy kỹ năng.
5. Giữ bản trước để phân biệt điều đã biết với điều chỉ biết sau; thêm ghi chú mới thay xóa cũ.
6. Đủ đề bài, bằng chứng hai chiều, giả định, điều chưa biết, điều kiện/mốc kiểm; không ghi số tiền/tài khoản cá nhân.

</details>

## Lỗi thường gặp

- Đánh giá mọi quyết định chỉ theo giá sau đó.
- Xóa sai số bằng cách viết lại dự đoán cũ.
- Nhầm quen tên với hiểu rủi ro.
- Chỉ ghi nguồn ủng hộ.
- Gọi quy trình học tập là chiến lược chắc sinh lời.

## Ranh giới an toàn

- Đây là bài học, không phải khuyến nghị mua/bán/nắm giữ cá nhân hóa.
- Số hư cấu được gắn `KỊCH_BẢN`; phép tính không dự báo hay cam kết lợi nhuận.
- Trước khi áp dụng cho một thị trường, phải kiểm lại nguồn gốc, quy định và chuẩn kế toán tại đó.

## Điều tôi vẫn chưa hiểu

- Điều gì tôi không muốn đọc nhưng cần đọc?
- Có so với mốc phù hợp chưa?
- Sai sót nào lặp lại qua nhiều nhật ký?

## Nguồn Internet đã mở

Các nguồn được nhánh chuyên môn hoặc điều phối viên tìm kiếm và mở trong lượt triển khai ngày 26/10/2026. Ngày truy cập: `2026-10-26`. Không suy ngày thu thập thành ngày xuất bản. Phần công thức/ví dụ hư cấu là thiết kế bài học, không phải số thị trường.

| Nguồn | Kỳ/phiên bản, phạm vi | Dùng cho |
|---|---|---|
| [SEC — Behavioral Patterns of U.S. Investors](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-72) | Hoa Kỳ; bản tin 16/06/2014, dẫn báo cáo Library of Congress 08/2010 | Hành vi và giới hạn khái quát |
| [St. Louis Fed — ALFRED Help](https://alfred.stlouisfed.org/help) | Kho phiên bản dữ liệu Hoa Kỳ; ngày xuất bản CHƯA_BIẾT | Phản chứng khi dùng dữ liệu tương lai |

Biên bản riêng cho đúng phiên bản: [kiểm nguồn](../reviews/015-fact-check.md), [phản biện](../reviews/015-risk-review.md). `CHƯA_BIẾT` hiệu quả học thực tế; không suy từ kiểm nguồn ra đã được người học nghiệm thu.

