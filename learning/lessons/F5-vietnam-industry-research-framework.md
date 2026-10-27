# Bài F5 — Khung nghiên cứu sáu ngành Việt Nam

- Ngày: `2026-10-27`
- Chốt dữ liệu lúc: `2026-10-27 11:57 UTC+7 (Asia/Ho_Chi_Minh)`
- Mục tiêu: Đặt câu hỏi về doanh thu, chi phí, vốn và chu kỳ cho thép, chứng khoán, bán lẻ, dầu khí, điện và thủy sản.
- Bài trước liên quan: [014](014-industry-capital-cycle.md), [F1](F1-three-statement-model-sensitivity.md), [M2](M2-credit-real-estate-cycle.md).
- Câu hỏi cốt lõi: Đơn vị kinh tế của mỗi ngành là gì, và biến nào có thể phá vỡ luận điểm?
- Kiểm nguồn: `ĐẠT`
- Phản biện rủi ro: `ĐẠT`
- Biên bản: [kiểm nguồn](../reviews/F5-fact-check.md), [phản biện](../reviews/F5-risk-review.md).

## Hiểu bài trong một phút

Không có một tỷ số áp được cho mọi ngành. Trước khi so định giá, cần hiểu sản phẩm, khách hàng, cơ chế giá, chi phí biến đổi, đầu tư và rào cản gia nhập; so các doanh nghiệp cùng phạm vi và kỳ, rồi thử kịch bản đối lập.

## 1. Bản đồ sáu ngành

| Ngành | Đầu ra và biến cần kiểm | Rủi ro/điều kiện |
|---|---|---|
| Thép | Sản lượng từng sản phẩm, giá bán so với giá quặng/than, sử dụng công suất | Chu kỳ cung, hàng nhập, đầu tư lớn, tồn kho và giá đầu vào |
| Chứng khoán | Giá trị giao dịch, thị phần/phí môi giới, dư nợ và chi phí vốn ký quỹ, tự doanh | Thanh khoản thị trường, nợ khách hàng, biến động tài sản và vốn khả dụng |
| Bán lẻ | Số cửa hàng, doanh thu cùng cửa hàng, biên gộp, tồn kho, chi phí thuê | Mở rộng không tự tạo hiệu quả; nhu cầu, cạnh tranh và chi phí mặt bằng |
| Dầu khí | Tách khai thác, dịch vụ, vận chuyển/chế biến và phân phối; sản lượng, giá, hợp đồng | Giá dầu, tiến độ, rủi ro dự án, chi phí/điều tiết khác nhau theo khâu |
| Điện | Loại nguồn điện, sản lượng, khả dụng, nhiên liệu/thủy văn, điều khoản mua điện | Giá nhiên liệu, huy động, thanh toán, đầu tư và nợ |
| Thủy sản | Loại sản phẩm, giá nguyên liệu, công suất chế biến, thị trường xuất khẩu | Thức ăn, dịch bệnh, rào cản thương mại, truy xuất và tỷ giá |

`Ý_KIẾN` Bảng là bộ câu hỏi, không khẳng định mọi doanh nghiệp trong cùng ngành có kinh tế giống nhau. Thêm đối thủ, nhà cung cấp, khách hàng, năng lực thay thế và chu kỳ vốn trước khi đánh giá lợi thế cạnh tranh.

## 2. Một ví dụ có kỳ

`SỰ_THẬT` [PV Power — nội dung trình đại hội 20/05/2026](https://pvpower.vn/vi/post/pv-power-vuot-ke-hoach-loi-nhuan-nam-thu-7-lien-tiep--dat-muc-tieu-doanh-thu-gan-50-000-ty-dong-trong-nam-2026-6909.htm) công bố sản lượng điện toàn tổng công ty năm 2025 là 18,6 tỷ kWh, doanh thu 35.364 tỷ VND và lợi nhuận trước thuế 3.234,3 tỷ VND. Đây là thông tin doanh nghiệp công bố, chưa thay việc đọc báo cáo tài chính kiểm toán và thuyết minh phạm vi hợp nhất.

`PHÉP_TÍNH` Lợi nhuận trước thuế/doanh thu ≈ `3.234,3/35.364 = 9,15%`, tính theo số làm tròn của công ty; không phải biên gộp, dòng tiền hay dự báo năm 2026. `CHƯA_BIẾT` Tác động riêng của giá nhiên liệu, hợp đồng, sản lượng từng nhà máy và dòng tiền: cần đọc hồ sơ gốc. Ví dụ không là khuyến nghị về PV Power.

## 3. Lập hồ sơ ngành có thể kiểm

`Ý_KIẾN` Chọn phạm vi địa lý và chuỗi giá trị; ghi nguồn số liệu theo kỳ/đơn vị; chọn ít nhất hai doanh nghiệp thực sự so được; dựng bảng khách hàng, giá bán, chi phí, công suất, nợ, vốn lưu động và cạnh tranh. Viết cả bằng chứng thuận và bất lợi, giả định, câu hỏi còn thiếu và điều kiện bác bỏ. Tạo hồ sơ ngành riêng trong `research/sectors/` khi dữ liệu đã thu thập đủ; bài này không giả vờ sáu hồ sơ ngành đã hoàn thành.

## Năm câu hỏi khi đọc

1. Doanh thu bằng sản lượng × giá hay còn nguồn nào khác?
2. Yếu tố nào quyết định biên và vốn phải bỏ ra?
3. Cạnh tranh và rào cản gia nhập đến từ đâu?
4. Biến số chu kỳ, hợp đồng hoặc chính sách nào có thể đổi?
5. Bằng chứng nào bác bỏ lợi thế hoặc làm kịch bản xấu xảy ra?

## Bài tập

1. Sản lượng thép tăng có tự chứng minh lợi nhuận và dòng tiền tăng không?
2. Phân biệt môi giới với cho vay ký quỹ của công ty chứng khoán.
3. Hai doanh nghiệp điện khác nhiên liệu có tự có cùng biên không?
4. Tính 3.234,3/35.364 theo phần trăm và nêu giới hạn.
5. Mở thêm cửa hàng có tự chứng minh hiệu quả vốn cao không?
6. Nêu hai biến cần kiểm với doanh nghiệp thủy sản xuất khẩu.

## Đáp án

1. Không; còn giá, chi phí, tồn kho, đầu tư và vốn lưu động.
2. Môi giới gắn giao dịch/phí; ký quỹ là khoản cho vay có lãi và rủi ro tín dụng/chi phí vốn.
3. Không; hợp đồng, nhiên liệu, huy động và chi phí khác nhau.
4. Khoảng 9,15% lợi nhuận trước thuế/doanh thu, theo số công ty công bố; không là biên gộp hay dòng tiền.
5. Không; cần xem doanh thu/biên, chi phí, đầu tư và dòng tiền.
6. Ví dụ: giá nguyên liệu, thị trường xuất, chi phí thức ăn, thuế thương mại, tỷ giá.

## Lỗi thường gặp và ranh giới an toàn

Gộp các khâu dầu khí, dùng một doanh nghiệp làm đại diện cả ngành, so số không cùng kỳ hoặc coi sản lượng tăng là giá trị tạo ra. Bài không định giá hay khuyến nghị mã cụ thể.

## Điều tôi vẫn chưa hiểu

`CHƯA_BIẾT` Quy mô, thị phần, cơ cấu cạnh tranh và dữ liệu mới nhất của sáu ngành; từng hồ sơ cần nguồn gốc và phản biện riêng.

## Nguồn Internet đã mở

Truy cập `2026-10-27`: [PV Power — thông tin ĐHĐCĐ](https://pvpower.vn/vi/post/pv-power-vuot-ke-hoach-loi-nhuan-nam-thu-7-lien-tiep--dat-muc-tieu-doanh-thu-gan-50-000-ty-dong-trong-nam-2026-6909.htm), 20/05/2026, số năm 2025 do doanh nghiệp công bố; [Hòa Phát — công bố thông tin](https://www.hoaphat.com.vn/investor-relations/information-disclosure) và [SSI — báo cáo thường niên](https://www.ssi.com.vn/quan-he-nha-dau-tu/bao-cao-thuong-nien), kiểm tài liệu gốc theo kỳ. Bảng câu hỏi không phải thống kê ngành.
