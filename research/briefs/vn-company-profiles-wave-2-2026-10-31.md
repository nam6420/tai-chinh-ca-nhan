# Đề bài nghiên cứu: bốn hồ sơ mẫu doanh nghiệp Việt Nam (Đợt 2)

- Trạng thái: `ĐÃ_KIỂM_DUYỆT`
- Chốt triển khai: `2026-11-02 14:00 Asia/Ho_Chi_Minh`; cả bốn hồ sơ có hai biên bản ĐẠT cùng hash, theo tiêu chí không còn lỗi nghiêm trọng/cao. Xem [nhật ký vòng 5–7](../companies/VN/review-round-5.md).
- Chủ trì: `research_coordinator`
- Chốt dữ liệu lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Phạm vi địa lý: Việt Nam, sàn HOSE; tiền tệ VND; chuẩn kế toán VAS.
- Mục tiêu học tập: có bốn mẫu đạt chuẩn cho bốn kiểu doanh nghiệp khác nhau: dịch vụ công nghệ (FPT), hàng tiêu dùng (Vinamilk, VNM), ngân hàng (Vietcombank, VCB) và công ty chu kỳ (Hòa Phát, HPG). Người học tập đọc báo cáo gốc tại địa phương, phân biệt số đã kiểm toán, đã soát xét và chưa soát xét, và biết khi nào số liệu không so được giữa các kỳ.
- Câu hỏi quyết định được hỗ trợ: những giả định nào phải đúng để hiểu khả năng tạo lợi nhuận và dòng tiền của từng doanh nghiệp. Không phải lệnh giao dịch; doanh nghiệp được chọn để học, không phải để khuyến nghị.

## Câu hỏi cốt lõi cho từng hồ sơ

1. Doanh nghiệp kiếm tiền bằng cách nào, kinh tế đơn vị và rủi ro tập trung ra sao?
2. Lợi nhuận, dòng tiền, bảng cân đối và phân bổ vốn nói gì, và điểm nào chưa được nguồn gốc xác nhận?
3. Ba kịch bản (bất lợi, cơ sở, thuận lợi) cần giả định gì, và điều kiện nào làm luận điểm mất hiệu lực?

## Điểm riêng của từng mã

- FPT: từ 01/01/2026 FPT Telecom chuyển sang ghi nhận theo phương pháp vốn chủ; số 2025 và 2026 không cùng cơ sở.
- VNM: số so sánh 2025 được phân loại lại theo Thông tư 99 và 43; báo cáo năm 2025 đã kiểm toán chưa mở được.
- VCB: ngân hàng, đo bằng thu nhập lãi thuần, chi phí dự phòng, nợ xấu, bao phủ và an toàn vốn; đã đối chiếu nhóm nợ và dự phòng từ bản BCTC ngân hàng lập được lưu trên miền tổng hợp; chưa khớp byte với miền ngân hàng/HOSE, các số khác còn thứ cấp.
- HPG: công ty chu kỳ, chuẩn hóa lợi nhuận qua năm 2021–2025 và nhìn đòn bẩy sau dự án lớn.

## Phạm vi

- Bao gồm: FY2025 và kỳ gần nhất đã công bố đến 31/10/2026, đúng đơn vị và chuẩn kế toán của từng công ty.
- Không bao gồm: giá mục tiêu, khuyến nghị mua bán, hồ sơ cá nhân. Giá thị trường chỉ dùng làm mốc có nguồn, ngày và không kết luận đắt hay rẻ.
- Nhóm so sánh toàn cầu: ghi `CHƯA_BIẾT` khi chưa mở được hồ sơ gốc của đối thủ quốc tế.

## Kế hoạch tìm nguồn

- Công bố tại trang quan hệ nhà đầu tư của từng doanh nghiệp, HOSE và UBCKNN; báo chí và báo cáo của công ty chứng khoán chỉ dùng làm bối cảnh và ghi rõ là thứ cấp.
- Vĩ mô: Cục Thống kê (NSO), Ngân hàng Nhà nước; phần chưa mở được trang gốc ghi là thứ cấp.
- Tách số đã kiểm toán, đã soát xét, chưa soát xét, phép tính và kịch bản.

## Phân công agent

- `company-analyst` thu thập bằng chứng từng công ty; `macro-market-researcher` lập bối cảnh vĩ mô; phiên chính (vai điều phối viên) ghi báo cáo và sổ nguồn.
- `source-fact-checker` và `risk-bear-reviewer` chạy độc lập trên cùng bản cố định.
