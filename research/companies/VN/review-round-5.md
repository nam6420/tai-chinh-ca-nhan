# Nhật ký điều phối vòng 5–7: bốn hồ sơ Việt Nam

- Chốt dữ liệu hồ sơ: `2026-10-31 (Asia/Ho_Chi_Minh)`; kiểm trực tuyến ngày `02/11/2026`, bắt đầu khoảng `13:25 Asia/Ho_Chi_Minh`.
- Người ghi duy nhất: phiên chính, vai `research_coordinator`.
- Đây là **tóm lược điều phối**, không thay biên bản kiểm nguồn/phản biện của từng hồ sơ.
- Tiêu chí đã giao trước khi kiểm: ĐẠT khi không còn lỗi nghiêm trọng hoặc mức cao chưa xử lý; trung bình/thấp được ghi trong biên bản, không chặn. Giữ tiêu chí vòng 4 của giáo trình, không ngầm đổi chuẩn.
- Tám nhánh độc lập (hai nhánh mỗi mã), chuyên môn chỉ đọc và trả toàn văn trong tin nhắn; không đọc nhật ký/biên bản trước, không xem kết quả nhau. Chạy thành hai cụm theo giới hạn bốn nhánh đồng thời. Điều phối viên tự mở lại nguồn và kiểm phát hiện quan trọng trước khi sửa.

## Bản cố định vòng 5

| Mã | SHA-256 chuẩn hóa | Kiểm nguồn | Phản biện |
|---|---|---|---|
| FPT | `85446cbb27cffc4b4321ce94dc69d2a1ee071af07c1c1343b44577f89ef16ccc` | 0 nghiêm trọng/cao, 2 trung bình, 1 thấp; nhánh dùng chữ “ĐẠT có điều kiện”, chưa dùng làm cổng | KHÔNG_ĐẠT, 0 nghiêm trọng, 1 cao |
| VNM | `57ad878bc66eeb9a281d7bb89fda204a20574542024daa88c67569897ce9e6a8` | CHƯA_BIẾT: chưa tải được nguồn chi phí tài chính 9T, 0 lỗi cao đã xác nhận | ĐẠT, 0 nghiêm trọng/cao, 3 trung bình và 1 thấp |
| VCB | `c7703055f7ec0d6e568987772b223f288f2afe6e6f8af5f3a09b5aa95d0293ad` | KHÔNG_ĐẠT, 0 nghiêm trọng, 1 cao | KHÔNG_ĐẠT, 0 nghiêm trọng, 1 cao |
| HPG | `fa1e7be878e4e4e6b1a03a0128443c2fdcc3e3f38b1ff94c863bf80bed64bcc6` | KHÔNG_ĐẠT, 0 nghiêm trọng, 1 cao | KHÔNG_ĐẠT, 0 nghiêm trọng, 1 cao |

## Phát hiện và xử lý

| Mã / mức | Phát hiện độc lập | Đối chiếu và sửa của điều phối |
|---|---|---|
| FPT / cao | Tỷ lệ cổ tức 450–500 tỷ so lợi nhuận FTEL không khớp kỳ | Tự tải BCTC riêng FTEL FY2025 và đọc PDF45: 1.124.305.935.000 đồng cổ tức tiền mặt đã khai báo cho FPT. Bỏ tỷ lệ29–32% và kết luận phần lớn lợi nhuận không thành tiền; phân biệt khai báo, kỳ lợi nhuận, thực nhận2026. NguồnS26 |
| FPT / trung bình | Gạch rủi ro còn48,6% chưa điều chỉnh; cầu nối CFO chưa đủ; điều kiện2quý dùng lũy kế | Sửa43,4% cùng cơ sở thưởng; chỉ nói góp phần giải thích CFO; dùng quý riêng, ký mới chậm hơn thực hiện, chưa chứng minh2quý |
| VNM / chưa xác minh | PDF công ty trả403; chi phí tài chính9T chưa xác minh | Tìm qua trang báo cáo24hmoney, tải bản PDF gương; đọc ảnhPDF63/trangin62:453.303.861.156 so242.667.487.576 đồng, +86,8%. Bổ sungS23 và ghi giới hạn bản gương. Nhánh phản biện vòng6 tự tải được cảCDN công ty, khớp byte với bản gương; không quy lỗi403 của một công cụ thành không có nguồn |
| VCB / cao (kiểm nguồn) | Bỏ sót Vietcap30/10 về5.000tỷ dự phòng trái phiếu năng lượng | Tự tìm và mở đúng URL Vietcap (URL trả về ban đầu của nhánh thiếu chữ trong slug). ThêmS32, giữ thứ cấp, không suy danh tính hoặc nối chi phíQ3 với số dư9T |
| VCB / cao (phản biện) | Nhóm nợ và dự phòng chi tiết chỉ có một bài báo | Tìm và tải bản BCTC ngân hàng lập do24hmoney lưu. Đọc ảnhPDF27–29. Bổ sungS33: nhóm2–5 cùng cột đầu năm trình bày lại, cầu nối dự phòng riêng cho vay; dòng xử lý bằng dự phòng không phát sinh. Bỏ suy từ chênh khoảng3.080tỷ thành xử lý nợ. Vẫn công khai chưa khớp byte với miền ngân hàng/HOSE |
| HPG / cao (kiểm nguồn) | Quyết định612 có26HS, hồ sơ viết24 | Tự mở toàn văn612, sửa26HS tại cả hai chỗ; bổ sungS45 |
| HPG / cao (phản biện) | Tiền/nợ ròng/CFO/capexQ3 còn bỏ trống vì giới hạn10MB | Tải trực tiếp BCTC19MB bằngcurl, đọc ảnhPDF2,4,5,7. Bổ sungS48 và mô-đun tính nợ ròng hai phạm vi; không coi tiền gửi dùng ngay |
| HPG / bổ sung của điều phối | Quyết định1917 ký28/07 nhưng không hiệu lực cùng ngày nhưSMM | Tải bản gốc, đọc ảnhPDF2 Điều3: hiệu lực sau15ngày. Sửa12/08/2026 và tách ngày ký. S46 ghi phạm vi, ngoại lệ, miễn trừ; không suy thuế bảo đảm lợi nhuận |
| HPG / trung bình | “Tái hiệnQ4/2022” nhưng gộp giả định0 nhẹ hơn tiền lệ âm | Đổi tên kịch bản “Gộp bằng0”; giữ tiền lệ nặng hơn. Nguồn công tyQ1/2026 công bố LNST loại chuyển nhượng5.046 so tổng9.056 (S49), tách khỏi ước tính PSI5.200 |

## Vòng 6 và vòng 7

- VCB vòng6: hai nhánh ĐẠT trên `6ea21e9ad0273c942b2504b7c675907d88ef950ab330c15876a39864633f9e33`. Đã ghi [kiểm nguồn](VCB/fact-check.md), [phản biện](VCB/risk-review.md); bỏ nhãn nháp và chỉ đổi hai trạng thái vòng đời. Cổng hash in ĐẠT. Còn phát hiện trung bình/thấp về lặp nền dự phòngQ3, lời giải thích NIM củaVietcap và so bao phủ ngành.
- FPT vòng6 trên `b8618e37610b1482fa181914053482ae8af05fa91e4d60c949f38205a29c92c1`: cả hai nhánh phát hiện lỗi cao mới — tỷ lệ LNST FTEL +33%9T/+9%Q3 sai với số trong chính bảng báo cáo. Điều phối tự tải bản BCTC FTEL gương, đọc ảnhPDF6:9T2.933,945 so2.580,936 tỷ;Q31.022,468 so904,823 tỷ. Sửa+13,7%/+13,0%, doanhthu+16,8%; thêmS27 và hàm/test. Bìa ký số26/10, trang kết quả ký23/10; không trộn hai mốc. Chạy lại hai nhánh trên hash mới; biên bản cũ hết hiệu lực.
- VNM vòng6: nhánh phản biện ĐẠT trên `e921a25991a02d0f36c8af7f4fb79eec5db4d9b703ee15051ba261382252c60a`; còn chờ kiểm nguồn trên cùng bản trước khi bỏ nhãn.
- HPG vòng6: đang kiểm lại cả hai nhánh sau sửa.

## Lưu nguồn và phép tính

- [Manifest nguồn tải](../../../data/raw/company-review-sources-2026-11-02.json): URL, checksum, sốbyte, kỳ và giới hạn; payload lớn giữ cục bộ trong đường dẫn đãGit-ignore. OCR chỉ để tìm trang; điều phối đọc ảnh trước khi chép số.
- `calc_wave2.py`: thêm cầu nối dự phòngVCB, thanh khoảnHPG, tăng trưởngFTEL; test theo đơn vị gốc và tính chất kế toán, không khóa tỷ lệ từ nguồn chưa kiểm.
- Chưa commit/push/mởPR. Đang làm trên nhánh `codex/company-profiles-review-5`.

## Chốt A ngày 02/11/2026, khoảng 14:00 Asia/Ho_Chi_Minh

Cả bốn hồ sơ đã có hai biên bản ĐẠT khớp mã băm; cổng `validate_report.py` in ĐẠT cho từng mã. Điều phối chỉ bỏ tiền tố nháp và đổi hai dòng trạng thái vòng đời sau khi kiểm; các liên kết biên bản đã được đặt trước lúc tính hash.

| Mã | Hash cuối | Kiểm nguồn | Phản biện |
|---|---|---|---|
| FPT | `d658d19f135de90645033b83b533b5ca3b9d6f41b795516cd9449208bc199555` | [vòng 7](FPT/fact-check.md) | [vòng 7](FPT/risk-review.md) |
| VNM | `e921a25991a02d0f36c8af7f4fb79eec5db4d9b703ee15051ba261382252c60a` | [vòng 6](VNM/fact-check.md) | [vòng 6](VNM/risk-review.md) |
| VCB | `6ea21e9ad0273c942b2504b7c675907d88ef950ab330c15876a39864633f9e33` | [vòng 6](VCB/fact-check.md) | [vòng 6](VCB/risk-review.md) |
| HPG | `6541a57d1ed987935686a84ab4c02a7b212da993b49e4c8d56c11e83df70a620` | [vòng 7](HPG/fact-check.md) | [vòng 7](HPG/risk-review.md) |

HPG vòng 6 có thêm lỗi cao: cách viết “1.718 tỷ như Q4/2022” gán mức bán hàng Q2/2026 cho kỳ lịch sử. Sửa thành giả định giữ mức Q2/2026; Q4/2022 chỉ là tiền lệ chi phí ít co (716 so 711 tỷ). Hai nhánh chạy lại vòng 7 trên hash mới. URL S25 có bất đồng truy cập; nhánh kiểm nguồn mở Vietcap Q2 để xác nhận 1.718 tỷ, ghi nguồn dự phòng trong biên bản.

Kiểm soát chất lượng biên bản: một bản phản biện HPG vòng 6 lẫn khoản dự phòng trái phiếu VCB, bị điều phối từ chối; nhánh đã rút phát hiện và trả lại biên bản chỉ xét HPG. Một kết quả kiểm nguồn HPG gắn hash cũ do dùng nội dung đã đọc trước đó cũng bị từ chối; yêu cầu đọc mới từ đĩa, kiểm hash và mở nguồn lại. Không dùng hai kết quả lỗi này làm căn cứ xuất bản.

Các góp ý trung bình/thấp còn lưu nguyên trong từng biên bản, không bị xóa để tạo cảm giác không có giới hạn: tỷ trọng FTEL dùng tổng/phần mẹ; so tác động khác cơ sở thuế; kịch bản VNM khác mùa; dự phòng và NIM VCB; dòng tiền đầu tư và nợ ròng HPG; một số nguồn thứ cấp và khác biệt làm tròn. ĐẠT không đồng nghĩa hết điều chưa biết, đúng tương lai hay khuyến nghị đầu tư.

Kiểm tra trước chuyển B: 79 test ĐẠT; verify cấu hình ĐẠT; kiểm chiều sâu vẫn báo 9/65 bài S (chưa nâng B ở mốc này). Chưa commit/push. Nhóm B đầu: N1, N4, N5.
