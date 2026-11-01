# Kiểm duyệt vòng 3 của bốn hồ sơ Việt Nam (Đợt 2)

- Chốt dữ liệu lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Người ghi: phiên chính (vai điều phối viên) chép kết quả của tám nhánh độc lập (bốn kiểm nguồn, bốn phản biện rủi ro); hai bên chạy riêng trên cùng bản cố định, không thấy kết luận của nhau, không đọc `learning/reviews` hay các nhật ký vòng trước.
- **Chưa có biên bản có hiệu lực xuất bản.** Tám nhánh đã kiểm các bản mang mã băm ở cột "Bản vòng 3". Mọi hồ sơ sau đó đã được sửa theo phát hiện, nên mã băm đổi và các kết luận dưới đây **không áp dụng cho bản hiện tại**. Vì vậy chưa ghi `fact-check.md` và `risk-review.md` vào thư mục từng mã (biên bản phải khớp mã băm của bản xuất bản), và cả bốn `report.md` giữ nhãn `BẢN NHÁP - CHƯA KIỂM DUYỆT`.
- Để gỡ nhãn cần vòng 4: mỗi mã một kiểm nguồn và một phản biện độc lập trên bản đã sửa, rồi ghi biên bản khớp mã băm.

| Mã | Bản vòng 3 (SHA-256, 12 ký tự đầu) | Kiểm nguồn vòng 3 | Phản biện vòng 3 | Bản sau sửa (12 ký tự đầu) |
|---|---|---|---|---|
| FPT | 0e108d4382d5 | ĐẠT có điều kiện: 0 nghiêm trọng, 2 cao, 3 trung bình, 5 thấp | ĐẠT có điều kiện: 0 nghiêm trọng, 5 cao, 5 trung bình, 2 thấp | e5784c13ebb1 |
| VNM | d3b06ba37e8e | KHÔNG_ĐẠT: 0 nghiêm trọng, 3 cao, 3 trung bình, 5 thấp | ĐẠT có điều kiện: 0 nghiêm trọng, 3 cao, 4 trung bình, 3 thấp | 7dbd1cc04a28 |
| VCB | a79b0e7c3ce0 | ĐẠT có điều kiện (nguồn thứ cấp): 0 nghiêm trọng, 2 cao, 3 trung bình, 8 thấp | ĐẠT có điều kiện: 0 nghiêm trọng, 5 cao, 7 trung bình, 3 thấp | 3bd75f6fa282 |
| HPG | 17a0ca9a05ac | KHÔNG_ĐẠT: 1 nghiêm trọng, 2 cao, 4 trung bình, 7 thấp | KHÔNG_ĐẠT: 0 nghiêm trọng, 5 cao, 5 trung bình, 2 thấp | c7ded8f6071e |

Cả tám nhánh ghi cùng hạn chế: PDF của doanh nghiệp là ảnh quét nên phải đọc bằng mắt; các nguồn gốc thật sự chưa mở được được ghi ở cột "Còn lại" bên dưới.

## FPT

| Mức | Phát hiện | Xử lý |
|---|---|---|
| Cao (kiểm nguồn) | Kịch bản "Căng 2" ghi "pha loãng thêm 10,7%" nhưng thưởng cổ phiếu đã phát hành ngày 25/09/2026 và đã nằm trong EPS | Bỏ cụm; ghi thưởng là điều chỉnh hồi tố, ESOP mới là chuyển giá trị; đối chiếu 108,2 tỷ với 10,8 triệu cổ phiếu × 10.000 đồng |
| Cao (kiểm nguồn) | Lẫn cổ tức FTEL với lợi nhuận liên kết (theo vốn chủ, tính theo lãi chứ không theo cổ tức) | Sửa cột "điều gì phải đúng" và điều kiện mất hiệu lực |
| Cao (phản biện) | Giá và dòng vốn đã cũ (66.800 đồng ngày 15/07; thực tế 54.000 đồng ngày 28/10; khối ngoại bán ròng khoảng 211 triệu cổ phiếu) | Thêm giá 28/10, đỉnh 105.000, P/E 33 → 16–18 lần, nguồn S17 và S19; sửa 35,7% thành 36,4% |
| Cao (phản biện) | Kịch bản chưa so Q4 với Q4/2025 và chưa có tốc độ chạy năm; dải hẹp | Thêm cột Q4 so Q4/2025 (ước tính khoảng 2.504 tỷ), tốc độ chạy năm 10.892 tỷ, kịch bản minh họa 2027, sắp lại thứ tự |
| Cao (phản biện) | Quý 3 chậm lại: ký mới khoảng +3,7%, doanh thu khoảng +8,2% (6 tháng +32,3% và +13,4%) | Thêm phép tính thô và ngưỡng minh họa vào rủi ro và điều kiện mất hiệu lực |
| Cao (phản biện) | Thiếu thuế hiệu dụng (ưu đãi 10% của FPT Software hết từ 06/2026) | Thêm (thứ cấp), phép tính thô 15,2% |
| Trung bình | Ước FTEL trộn kỳ; giải thích giá cổ phiếu bỏ hai nguyên nhân; S9 thiếu "(thứ cấp)"; FTEL 9 tháng +33% | Sửa theo 9 tháng; liệt kê bốn nguyên nhân; thêm nhãn và 37%; thêm S16 |
| Thấp | Nhãn mã 120, chênh cổ tức 13 tỷ, ngữ pháp, CFO thiếu mã 11 và lãi vay đã trả, mã 26b | Sửa tất cả |

Còn lại: công văn gốc Bộ Công an và công bố 18–19/03/2026; nghị quyết ESOP và thưởng; báo cáo thường niên 2025 bản PDF; CFO theo quý; so sánh quốc tế; mọi số FTEL vẫn thứ cấp.

## VNM

| Mức | Phát hiện | Xử lý |
|---|---|---|
| Cao (kiểm nguồn) | Driftwood: quý 3 thấp hơn cùng kỳ nhưng bài xếp vào bằng chứng thuận chiều (trộn kỳ) | Tách kỳ; chuyển quý 3 sang rủi ro và điều kiện mất hiệu lực |
| Cao (kiểm nguồn) | Gán "chủ yếu từ Angkor Milk" cho nguồn chỉ nói "các công ty con ở nước ngoài"; "nền thấp" không có trong S10; bỏ sót Lao-Jagro | Viết lại; quy mô `CHƯA_BIẾT` |
| Cao (kiểm nguồn) | "Lợi nhuận cốt lõi" trừ doanh thu tài chính gộp nhưng giữ chi phí tài chính (+66%) | Cầu nối ròng: 66,8% (quý 3) và 15,5% (9 tháng), thay vì 77% và 24%; đổi tên; thêm biến thể Q4 lõi ròng 2.452 tỷ |
| Cao (phản biện) | Bỏ sót định hướng công ty (giá nguyên liệu đã khóa, biên 2H kỳ vọng 43,1%) so với thực tế 41,36% | Thêm mục định hướng so với thực tế (S16, S17) |
| Cao (phản biện) | "Cơ sở" mang cả khoản khó lặp; thứ tự kịch bản không đơn điệu | Đổi tên "Giữ nguyên Q3 (cận trên của không đổi)", sắp lại, không chọn kịch bản trung tâm |
| Cao (phản biện) | Điều kiện "tiền ròng giảm" bị kích hoạt cơ học bởi tạm ứng cổ tức 5.225 tỷ rơi vào Q4 | Đổi điều kiện sang tiền ròng cộng cổ tức đã công bố (12.831 tỷ); thêm minh họa 14.975 tỷ |
| Trung bình | Kịch bản "Căng" không có neo; Q2 lệch 9 tỷ; Q1 điền được; nhãn tỷ giá lẫn suy luận; vận chuyển +44,8%; báo cáo FY2025 có liên kết | Nêu neo cơ chế (biên khoảng 35,0%); điền Q1 thứ cấp; tách nhãn; sửa số |
| Thấp | Nhãn "cao", "ngành yếu", thị phần, Thông tư 99, Hormuz | Sửa nhãn, thêm vào điều chưa biết |

Còn lại: báo cáo FY2025 đã kiểm toán và báo cáo riêng; cổ đông lớn ngoài SCIC; Miraka; nguyên nhân biên gộp Q3 thấp hơn định hướng; giá sữa bột chính thức; phần tăng giá bán 3–4% từ 04/2026 chỉ có nguồn thứ cấp, mức chưa xác minh.

## VCB

| Mức | Phát hiện | Xử lý |
|---|---|---|
| Cao (kiểm nguồn) | "Nợ nghi ngờ tăng nhiều quý liên tiếp" thiếu nguồn và nhóm 4 không đơn điệu (1.586 → 1.227 → 1.657) | Giới hạn "liên tiếp" ở nhóm 2; nhóm 3–4 ghi "tăng mạnh so với đầu năm" |
| Cao (kiểm nguồn + phản biện) | Mô tả kịch bản "Thuận lợi" (dự phòng 500) không khớp phép tính (hàm ý khoảng 4.244 tỷ) | Sửa mô tả; thêm biến thể dự phòng 500 → 57.342 tỷ |
| Cao (phản biện) | Chưa so với mục tiêu ban lãnh đạo (+5% hàm ý 46.221 tỷ; Q4 khoảng 5.781 tỷ) | Thêm so sánh (số kế hoạch chính thức vẫn `CHƯA_BIẾT`) |
| Cao (phản biện) | Thiếu cột Q4/Q4 và tốc độ chạy năm | Thêm: Q4 từ −70% đến +21%; chạy năm 44.872 tỷ |
| Cao (phản biện) | Bỏ sót dự báo MBS sai xa (PBT 14.567 và dự phòng 687 so với 11.218 và 6.184) | Thêm mục riêng |
| Cao (phản biện) | Nhóm nợ mở được nhưng ghi `CHƯA_BIẾT`: nhóm 3 + 4 gấp khoảng 4 lần; bốn phiên bản số nợ xấu đầu năm | Thêm bảng nhóm (S25); nêu bốn phiên bản |
| Cao (phản biện) | Trái phiếu doanh nghiệp nhóm 4 khoảng 6,6 nghìn tỷ ngoài tỷ lệ nợ xấu cho vay (blog, chưa xác minh) | Thêm với nhãn `Ý_KIẾN` và `CHƯA_BIẾT` |
| Trung bình | Bao phủ 279% → 244% có thể khác định nghĩa; "cổ tức 20.332" thực là "phân phối"; công văn 9608 sau quý 3; nguồn vốn, NIM ngành, VietinBank vượt VCB | Sửa theo từng điểm; thêm S23–S29 |
| Thấp | 49.620 nêu trực tiếp; DBS 16 điểm cơ bản; nhãn các câu; luận điểm "chất lượng còn tốt" | Sửa |

Còn lại: toàn bộ số ngân hàng là thứ cấp (nhiều bài có thể dùng chung một bản tin gốc); BCTC gốc trên vietcombank.com.vn, HOSE, SBV chưa mở được; chênh 770 tỷ trong thu nhập ngoài lãi; CAR chính thức; toàn văn Công văn 9608.

## HPG

| Mức | Phát hiện | Xử lý |
|---|---|---|
| **Nghiêm trọng** (kiểm nguồn) | Bỏ sót Quyết định 1917/QĐ-BCT ngày 28/07/2026 (biện pháp chống lẩn tránh đã chính thức), bài vẫn viết còn tạm thời | Cập nhật mọi mục liên quan; thêm rủi ro hồ sơ miễn trừ và rà soát thuế của Baosteel |
| Cao (kiểm nguồn) | Gán sai: ">10% từ đỉnh" là của tác giả, "−7%" là dự báo VDSC/MBS và không "so với quý trước" | Sửa nguồn; hạ suy luận về biên Q3 |
| Cao (kiểm nguồn) | Tóm tắt nói "vượt xa dự báo" nhưng thân bài nói chưa mở nguồn | Nêu số dự báo, người dự báo, phạm vi |
| Cao (phản biện) | Kịch bản "chu kỳ xấu" bỏ chi phí bán hàng nên có thể là quý lỗ; chưa so Q4/Q4; chưa quy năm | Thêm chỉ báo sau chi phí bán hàng (−243 tỷ so với lãi vay), Q4/Q4 (−22%), cột quy năm; đổi tên Rất xấu / Xấu |
| Cao (phản biện) | Quý 3 tăng 28,7% so với quý 2 chưa được tách; dự báo sai xa | Thêm phép tính; nguyên nhân `CHƯA_BIẾT` |
| Cao (phản biện) | Rà soát thuế chống bán phá giá do Baosteel; trần giá nhập khẩu và cầu yếu | Thêm (S29, S33) |
| Cao (phản biện) | Đòn bẩy: nợ vay +15.100 tỷ từ cuối quý 1, lãi vay 1.333 → 1.520 → 1.774 | Thêm chuỗi quý |
| Trung bình | Tồn kho +27,8% chỉ +5,3% so với cuối 2025; trích dẫn 4.915/Phố Nối; doanh thu gộp nâng lên PHÉP_TÍNH (lệch biên 0,13–0,14 điểm); VinMetal 2031; xuất khẩu Trung Quốc 9 tháng −2,6% | Sửa tất cả |
| Thấp | Tỷ lệ 20,7% thêm 16,2%; nhãn dòng tiền; 684,7 USD là tháng 3; 16% lãi vay; EBITDA định nghĩa khác; P/E đỉnh chu kỳ | Sửa tất cả |

Còn lại: BCTC hợp nhất Q3/2026 (quá 10 MB) chưa mở, nên biên gộp 19,0%, lãi vay 1.774, nợ vay 105.737 chỉ khớp tổng quan của công ty; văn bản gốc Quyết định 612 và 1917; thông báo gốc về Phú Yên; giao dịch bên liên quan; ba URL nguồn thứ cấp về Quyết định 1917 (S27, S28, S32) chưa có địa chỉ đầy đủ trong sổ nguồn.

## Việc chưa làm và giới hạn của vòng này

- Chưa chạy vòng 4 trên bản đã sửa; các bản sửa dùng nguồn do các nhánh vòng 3 đã mở nhưng chính phiên chính chưa mở lại từng nguồn mới, nên nguồn mới (S16–S20 FPT, S15–S17 VNM, S23–S29 VCB, S25–S36 HPG) đều ghi thứ cấp và cần kiểm nguồn độc lập ở vòng 4.
- Mọi con số mới trong bài đã có hàm trong `calc_wave2.py` (`fpt_round3`, `vnm_round3`, `vcb_round3`, `hpg_round3`) và test trong `tests/test_vn_profiles.py`.
- Không tuyên bố đã kiểm duyệt. Trạng thái hai dòng "Kiểm nguồn" và "Phản biện rủi ro" vẫn `ĐANG_CHỜ`.
