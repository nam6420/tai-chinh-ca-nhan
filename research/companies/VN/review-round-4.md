# Kiểm duyệt vòng 4 của bốn hồ sơ Việt Nam (Đợt 2)

- Chốt dữ liệu lúc: `2026-10-31 (Asia/Ho_Chi_Minh)` (ngày truy cập của các nhánh kiểm duyệt: 01/11/2026)
- Người ghi: phiên chính (vai điều phối viên) chép kết quả của tám nhánh độc lập, chạy riêng trên bản cố định của vòng 3, không thấy kết luận của nhau và không đọc các nhật ký vòng trước.
- **Chưa có biên bản có hiệu lực xuất bản.** Không mã nào có cả hai nhánh ĐẠT trên cùng một mã băm, và mọi hồ sơ đã được sửa sau vòng này nên mã băm đổi. Cả bốn `report.md` giữ nhãn `BẢN NHÁP - CHƯA KIỂM DUYỆT`; chưa ghi `fact-check.md` hay `risk-review.md` vào thư mục từng mã.

| Mã | Bản vòng 4 (12 ký tự đầu) | Kiểm nguồn vòng 4 | Phản biện vòng 4 | Bản sau sửa (12 ký tự đầu) |
|---|---|---|---|---|
| FPT | e5784c13ebb1 | KHÔNG_ĐẠT: 0 nghiêm trọng, 2 cao, 4 trung bình, 4 thấp | ĐẠT có điều kiện: 0 nghiêm trọng, 5 cao, 6 trung bình, 3 thấp | 85446cbb27cf |
| VNM | 7dbd1cc04a28 | ĐẠT có điều kiện: 0 nghiêm trọng, 0 cao, 7 trung bình, 14 thấp | ĐẠT có điều kiện: 0 nghiêm trọng, 3 cao, 5 trung bình, 3 thấp | 57ad878bc66e |
| VCB | 3bd75f6fa282 | KHÔNG_ĐẠT: 1 nghiêm trọng, 5 trung bình, 2 thấp-trung bình, 7 thấp | KHÔNG_ĐẠT: 1 nghiêm trọng, 4 cao, 4 trung bình, 2 thấp | c7703055f7ec |
| HPG | c7ded8f6071e | KHÔNG_ĐẠT: 4 nghiêm trọng, 5 trung bình, 2 nhẹ | ĐẠT có điều kiện: 0 nghiêm trọng, 3 cao, 6 trung bình, 2 thấp | fa1e7be878e4 |

## FPT

| Mức | Phát hiện | Xử lý |
|---|---|---|
| Cao (kiểm nguồn + phản biện) | "54.000 thấp hơn đỉnh 48,6%" và "ESOP thấp hơn 81,5%" so giá sau thưởng 10% với giá trước thưởng | Điều chỉnh đỉnh theo hệ số 1,1: −43,4%; ESOP quy về sau thưởng 83,2%; nêu mốc "đỉnh" khác nhau giữa các nguồn (S6, S17, S19) |
| Cao (kiểm nguồn + phản biện) | Câu "quý 3 đã gần chạm điều kiện" sai chiều (doanh thu +8,2% nhanh hơn ký mới +3,7%); điều kiện đã bị chạm nhưng văn bản nói nhẹ | Tách thành hai điều kiện, thêm trạng thái hiện tại từng điều kiện |
| Cao (phản biện) | Kịch bản "Thuận lợi" mâu thuẫn Q3 chậm lại; P/E cũ; thiếu phép kiểm chuyển hóa tiền cổ tức FTEL; CFO cạnh khoản tiền chưa rõ thành phần | Ghi mâu thuẫn; thêm P/E thô khoảng 9,8 lần; thêm 450–500 tỷ (29–32%); thêm CFO cộng mã 27 (28%) |
| Trung bình | "Lạm phát ngược" không có trong S18; P/E 33 lần là cuối 2024; dải dự báo bỏ Vietcap; Q4/2025 tính chính xác 2.502,4; nhãn kế hoạch 11.629; rủi ro VN-Diamond; Infosys | Sửa tất cả; thêm S21–S25 |

Còn lại (ghi trong "Bất đồng chưa giải quyết"): kịch bản nhiều năm mới có một đường; ngày không hưởng quyền thưởng; báo cáo thường niên 2025; công văn gốc.

## VNM

| Mức | Phát hiện | Xử lý |
|---|---|---|
| Cao (phản biện) | Kịch bản "Căng" ghi "không có tiền lệ" nhưng Q4 giả định cao hơn LNST mẹ quý 1/2025 (khoảng 1.570 tỷ) | Bỏ câu; thêm dòng "đuôi lịch sử" (Q4 1.570 hoặc 1.906 tỷ) |
| Cao (phản biện) | Nhãn "Bất lợi" (−10%) nhẹ hơn "Q4 lõi" (−13,7%) của chính hồ sơ | Đổi tên "Giảm nhẹ" và giải thích |
| Cao (phản biện) | Cổ đông lớn ghi `CHƯA_BIẾT` trong khi có F&N 22,29% + 2,7% và Platinum Victory | Điền từ S4 (công ty công bố) và S21 |
| Trung bình (kiểm nguồn) | S17 chỉ nói biên hợp nhất; tăng giá 3–4% chỉ ở S16; nhãn bao suy diễn; bán lẻ "giá hiện hành"; nguyên nhân Q4/2025 rút gọn; quảng bá 50 năm; **chi phí tài chính 9T tăng 87%, không phải 74%** | Sửa tất cả; thêm test |
| Trung bình (phản biện) | Mâu thuẫn mức và thời điểm tăng giá; nước ngoài giảm tốc; rủi ro lãi suất có thể phóng đại; GDT và độ trễ giá | Thêm vào bài và điều kiện mất hiệu lực |
| Thấp | V.24 thay VI.24; "tổng doanh thu"; Q1 16.149; 129,7% chỉ ở S9; Dừa Á Châu nâng thành PHÉP_TÍNH | Sửa phần lớn; thiếu giờ ở "Chốt dữ liệu lúc" giữ nguyên vì định dạng bắt buộc của kho (`2026-10-31 (Asia/Ho_Chi_Minh)`) |

## VCB

| Mức | Phát hiện | Xử lý |
|---|---|---|
| **Nghiêm trọng** (kiểm nguồn) | Viết sai chiều: tốc độ chạy năm 44.872 "thấp hơn 2025 khoảng 1,9%", thực tế cao hơn 1,9% | Sửa; thêm hàm và test |
| **Nghiêm trọng** (phản biện) | Trái phiếu doanh nghiệp và nguyên nhân dự phòng ghi `CHƯA_BIẾT` trong khi nguồn nêu dự phòng trái phiếu chưa niêm yết 3.307 → 6.304 tỷ; giả thuyết "3.080 tỷ xử lý nợ" nhiều khả năng sai | Thêm số, phép đối chiếu 9.097 so với 9.180, bỏ giả thuyết; ghi điều kiện cùng định nghĩa |
| Cao (phản biện) | Nhóm 2 quý 3 (4.995 tỷ); điều kiện mất hiệu lực đã bị chạm; nguồn vốn (CASA 31,8%, Kho bạc, vay NHNN); kịch bản chưa gắn Công văn 9608 | Thêm; thêm độ nhạy cận trên −2.300 đến −3.600 tỷ mỗi quý |
| Trung bình | Nhóm nợ gán nhầm S25 (đúng là bài 325370, nay là S30); 8.651 và 9.714 là suy ra; gán nguồn 9T; "lỗi trong nguồn" 9.646 chưa kiểm; mục tiêu +5% không rõ LNTT hay LNST; ngày công văn; số cổ phiếu tăng vốn mâu thuẫn; thu nhập khác 7.443 so với 5.919 | Sửa/ghi mâu thuẫn |

## HPG

| Mức | Phát hiện | Xử lý |
|---|---|---|
| Nghiêm trọng (kiểm nguồn) | Rà soát Baosteel: là Quyết định 1902/QĐ-BCT ký 27/07/2026, "rà soát lần thứ nhất" xét việc áp dụng với doanh nghiệp này, không phải "giữa kỳ" và không có "tăng" | Sửa mọi chỗ |
| Nghiêm trọng (kiểm nguồn) | Quyết định 1917: gán nguồn sai (27,83% cho 1917 ở S32, S39, không ở S27, S28), suy luận "mức trần" bị bác, miễn trừ có nêu, 26 mã HS | Sửa; điền URL đầy đủ S27, S28, S32; thêm S37–S39 |
| Nghiêm trọng (kiểm nguồn) | Lý do hoãn Phú Yên (dư cung) gắn `SỰ_THẬT` nhưng bài không dẫn tài liệu của công ty | Tách `SỰ_THẬT` và `Ý_KIẾN` |
| Nghiêm trọng (kiểm nguồn) | Lý do Hòa Phát tăng giá HRC tháng 11 là phân tích của BigMint, bài không gán cho Hòa Phát | Sửa; thêm sự cố Formosa 04/09 |
| Cao (phản biện) | "Rất xấu" chưa phải đáy (Q4/2022 gộp âm 885 tỷ); chi phí bán hàng không co theo doanh thu (716 so với 711); thanh khoản lệch một chiều (đệm tiền 37.256 tỷ, vay USD ngắn hạn gấp 3,5 lần, vay ngắn hạn 29% → 74%) | Thêm tiền lệ, chi phí bán hàng cứng (−815 tỷ), "tái hiện Q4/2022" (−3.758 tỷ), thanh khoản và tỷ giá |
| Trung bình | Doanh thu Q3/Q2 cùng cơ sở 12,8%; chênh 810 tỷ giải thích được (giảm trừ nửa đầu năm); EBITDA lỗi thời; "nợ thấp hơn nhiều" không có nguồn | Sửa; thêm S40–S44 |

Còn lại: báo cáo hợp nhất Q3/2026 của HPG (quá 10 MB) chưa mở nên mọi số Q3 chỉ khớp tổng quan của công ty; ba văn bản gốc của Bộ Công Thương (612, 1902, 1917); tiền ròng 30/09/2026.

## Giới hạn của vòng này

- Các bản sửa dùng nguồn mới do chính các nhánh vòng 4 đã mở; phiên chính chưa tự mở lại từng nguồn mới (FPT S21–S25, VNM S18–S22, VCB S30–S31, HPG S37–S44), nên đều ghi thứ cấp và cần kiểm nguồn độc lập ở vòng 5.
- Mọi con số mới có hàm trong `calc_wave2.py` (`fpt_round3`, `vnm_round3`, `vnm_round4`, `vcb_round3`, `vcb_round4`, `hpg_round3`, `hpg_round4`) và test trong `tests/test_vn_profiles.py`.
- Hai việc phản biện vòng 4 nêu mà chưa làm: bảng hai biến cho FPT 2027 (thuế × tăng trưởng) và kịch bản VNM với lãi suất tiền gửi cụ thể; đã ghi vào "Bất đồng chưa giải quyết".
- Không tuyên bố đã kiểm duyệt. Hai dòng "Kiểm nguồn" và "Phản biện rủi ro" vẫn `ĐANG_CHỜ`.
