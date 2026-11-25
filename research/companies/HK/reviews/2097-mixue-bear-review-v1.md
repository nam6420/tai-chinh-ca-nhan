# Biên bản kiểm duyệt: MIXUE Group (2097.HK), đọc báo cáo tài chính FY2022–FY2025 và H1 2026 (bản nháp v1)

> Điều phối viên lưu bản tóm lược từ báo cáo của subagent `risk-bear-reviewer` (bản đầy đủ nằm trong báo cáo hand-back của phiên làm việc). Giữ nguyên kết luận, mức độ và bằng chứng chính. Bên phản biện chạy độc lập, không đọc biên bản kiểm nguồn.

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-25` (agent không có đồng hồ; điều phối viên ghi nhận hoàn tất trước 2026-11-25 08:30 +07)
- Chốt dữ liệu lúc: `2026-11-25 08:11 +07` (khớp báo cáo đích v1)
- Phạm vi: toàn bộ bản nháp v1; đối chiếu H1 2026 với bản gốc HKEX; AR 2025; ngành, đối thủ, trợ giá giao hàng, quản trị, an toàn thực phẩm, thị trường; suy luận và kịch bản
- Báo cáo đích: `research/companies/HK/reviews/2097-mixue-draft-v1-sha-a682acf7.md` (bản sao nguyên vẹn của v1)
- SHA-256 nội dung đích: `a682acf7ef69738aea03104173140ff21aa1ea50e1cbd87e2a15f529876ef6b7` (do điều phối viên cung cấp; điều phối viên đã tự tính lại và khớp)
- Kết luận: `KHÔNG_ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0` (5 phát hiện CAO, 6 TRUNG_BÌNH, 1 THẤP; chưa thấy sai số trong số gốc đã đối chiếu)

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

Ngày truy cập 2026-11-25. Nguồn gốc: S7 (HKEX H1 2026) và AR 2025 (HKEXnews). Nguồn thứ cấp (chỉ bối cảnh, một số có lỗi số): 36Kr (eu.36kr.com/en/p/3966912256237060), Huxiu (m.huxiu.com/article/4886802.html), The Standard (bài về lợi nhuận H1 2026, về Meituan Q2 2026, về vụ chanh cũ 2025-03-17), caiwennews (ĐHĐCĐ bất thường 2026-09-30), KrASIA lại Nikkei (2026-11-17), iTiger (nhiều bài), Caixin Global (2026-01-10 và 2026-08-31, bị tường phí che một phần), Inside Retail (Chagee, 2026-09-01), Yahoo Finance (2025-08-29), KrASIA (Mixue 2025), Daxue Consulting. Không mở được: Bloomberg, SCMP, Morningstar, Bamboo Works (HTTP 403).

## Phát hiện

| Mức độ | Mã | Phát hiện | Bằng chứng chính | Trạng thái (sau khi sửa v2) |
|---|---|---|---|---|
| Cao | F1 | Bỏ sót dữ kiện có sẵn trong S7: cổ tức đặc biệt; tồn kho 30/6/2026 = 3.828,2 triệu (+4,2%); nhân viên 10.374; lỗ tỷ giá H1 153,8 triệu; chủ nhượng quyền 29.775 (+27,2%) | S7; điều phối viên đã đối chiếu trên PDF | Đã sửa trong v2 |
| Cao | F2 | "Lượng hàng mỗi cửa hàng giảm" vượt bằng chứng: đó là doanh thu hàng hóa/cửa hàng, phụ thuộc mẫu số (−14,6% đến −17,2%), có FULU và nước ngoài trong mẫu số, không có doanh số cùng cửa hàng chính thức | tái tính: 1,0305/1,2346; 1,0305/1,207; 1,0305/1,2441 | Đã sửa trong v2 |
| Cao | F3 | Kịch bản thiếu chỉ báo, ngưỡng, mốc; kịch bản bất lợi dựa vào trợ giá đã hạ nhiệt (Meituan có lãi trở lại Q2 2026; cơ quan chống độc quyền rà soát ngành giao hàng tháng 1/2026); kịch bản cơ sở giả định tồn kho "được tiêu hóa" trong khi tồn kho H1 còn tăng; các chuỗi khác (Guming, Auntea Jenny) tăng nên nguyên nhân có thể riêng của Mixue (nguồn thứ cấp) | The Standard, Caixin, Huxiu, Inside Retail | Đã viết lại trong v2 |
| Cao | F4 | Sụt lợi nhuận H1 2026 chủ yếu do chi phí: lợi nhuận trước thuế −492,6 triệu, trong đó chi phí bán hàng + quản lý +381,7 triệu (≈77,5%), lợi nhuận gộp −76,7 triệu (≈15,6%); thuế suất 22,1% so với 21,6% | S7 báo cáo lãi lỗ; điều phối viên tái tính | Đã sửa trong v2 |
| Cao | F5 | Thiếu bối cảnh ngành, đối thủ, thị trường; Chagee doanh số cùng cửa hàng −16,1%; cổ phiếu chạm dưới giá IPO ngày 2026-07-10, giảm khoảng 57% từ đầu năm đến 2026-11-09 (nguồn thứ cấp) | các nguồn thứ cấp nêu trên | Đã thêm mục bối cảnh (nguồn thứ cấp, chưa kiểm chéo) |
| TB | F6 | CAGR lấy năm gốc 2022 là năm đáy; CAGR lợi nhuận 2021→2025 là 32,7% | tái tính | Đã sửa |
| TB | F7 | Thuế: nếu giữ thuế suất 2024 (23,3%) lợi nhuận 2025 ≈ 5.788 triệu (+29,9% thay vì +33,1%); các ưu đãi thuế (miền Tây, Hải Nam) có thể chấm dứt | tái tính; S7 | Đã sửa |
| TB | F8 | Tồn kho: nêu cả ba cách đo (tăng 65,8% so với giá vốn; ngày tồn kho bình quân 48,4 → 46,5; ngày tồn kho cuối kỳ 48,2 → 58,0); tồn kho H1 2026 tăng thêm | AR 2025 dòng tiền; S7 | Đã sửa |
| TB | F9 | Điều kiện mất hiệu lực: "đóng vượt mở" không bao giờ chạm; tỷ lệ đóng H1 2026 thực ra giảm (2,16% so với 2,55%); cần chỉ báo đo được | tái tính | Đã viết lại |
| TB | F10 | Quản trị: hai nhà sáng lập cùng khai 100.098.196 cổ phiếu chưa niêm yết + 53.899.028 cổ phiếu H (≈40,57% vốn), Zhang Yuan 35 tuổi làm CEO thay CFO; chủ tịch ủy ban kiểm toán có tiểu sử gắn với JD.com | AR 2025 (điều phối viên đã đối chiếu số cổ phần và Zhang Yuan) | Đã sửa; cần đọc tiếp giao dịch bên liên quan |
| TB | F11 | An toàn thực phẩm và nhượng quyền: vụ chanh cũ Hồ Bắc 2025-03, 8.727 khiếu nại Black Cat, 16 cửa hàng bị Hội người tiêu dùng Bắc Kinh nêu 2024 (nguồn thứ cấp); phí nhượng quyền cố định chỉ 2,7% doanh thu | The Standard 2025-03-17; S7 | Đã thêm (nguồn thứ cấp) |
| Thấp | F12 | Diễn đạt: "bảng cân đối rất sạch", mục "bằng chứng trái chiều" thực ra là bằng chứng ủng hộ, vế suy luận gắn nhãn sai, cần câu "không phải lời khuyên" | nội dung v1 | Đã sửa |

## Kiểm tra phép tính hoặc bằng chứng trái chiều

Agent không có Bash nên tính tay; điều phối viên tái tính lại các phép chính (cầu nối lợi nhuận trước thuế H1, tỷ lệ đóng, CAGR 2021, thuế, doanh thu/cửa hàng theo ba mẫu số, ngày tồn kho cuối kỳ) và thấy khớp. Bằng chứng ủng hộ bản nháp: ba ước tính ngoài (môi giới, Huxiu, 36Kr) cho doanh thu hàng hóa/cửa hàng giảm 15–17% nhưng đều chia từ cùng số tổng của công ty; đối thủ vẫn tăng nên vấn đề có thể đặc thù Mixue; cổ phiếu giảm sâu sau H1. Bằng chứng trái chiều: tỷ lệ đóng cửa hàng H1 giảm, chủ nhượng quyền +27%, cổ tức đặc biệt, tiền mặt dồi dào, trợ giá đã hạ nhiệt từ 2026.

## Hạn chế của lần kiểm duyệt

Không có Bash, không tự tính được SHA-256 và giờ. Nguồn thứ cấp có lỗi số rõ ràng nên chỉ dùng cho bối cảnh. Chỉ đọc một phần AR 2025; chưa có dữ liệu Q3 2026, doanh số cùng cửa hàng chính thức hay dữ liệu độc lập cấp cửa hàng.

## Kết luận của agent kiểm duyệt

`KHÔNG_ĐẠT` ở bản v1: trung thực về phạm vi và chưa thấy số gốc nào sai, nhưng còn thiếu dữ kiện, diễn giải vượt bằng chứng và kịch bản chưa đo được. Bất đồng còn lại: bản nháp coi H1 2026 là "điểm gãy" của chuỗi tăng trưởng; agent coi đó là cách đọc hợp lý nhưng nguyên nhân (trợ giá, bão hòa, chi phí tự chọn) chưa được chứng minh và cần giữ cả ba giả thuyết mở.
