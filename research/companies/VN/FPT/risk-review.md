# Biên bản phản biện: FPT — vòng 7

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-02 13:49 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Phạm vi: BCTC Q3/9T2026, FTEL, cổ tức và CFO, cổ phiếu thưởng và so giá, kịch bản và điều kiện mất hiệu lực.
- Báo cáo đích: `research/companies/VN/FPT/report.md`
- SHA-256 nội dung đích: `d658d19f135de90645033b83b533b5ca3b9d6f41b795516cd9449208bc199555`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Phiên chính ghi từ kết quả hai nhánh độc lập vòng 7; không tự thay kết luận. Tiêu chí 0 nghiêm trọng/cao; trung bình/thấp được giữ, không chặn. Toàn văn từng nhánh có trong cuộc trao đổi 02/11/2026.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Ngày công bố / kỳ | Truy cập | Mục đích |
|---|---|---|---|
| [FPT 9T2026](https://fpt.com/vi/tin-tuc/9-thang-doanh-thu-va-loi-nhuan-truoc-thue-cua-fpt-tang-12-4-va-17-0) | 21/10/2026; 9T2026 | 02/11/2026 | Số kinh doanh, AI, cơ sở FTEL |
| [FTEL danh mục](https://fpt.vn/vi/ve-fpt-telecom/quan-he-co-dong/bao-cao-tai-chinh) và [bản sao BCTC](https://financialfilings.com/filings/fpt-telecom-jsc/interim-quarterly-report/2026/74756265/) | Trang kết quả ký 23/10/2026; Q3/9T2026 | 02/11/2026 | Hai kỳ hợp nhất và phần mẹ |
| [BCTC riêng FTEL FY2025](https://fpt.vn/storage/upload/files/reports/bctc_2025_audit_eng.pdf) | Duyệt 19/03/2026; FY2025 | 02/11/2026 | Cổ tức khai báo 33(a)(iv), trang in 43/PDF 45 |
| [HOSE quyền thưởng](https://staticfile.hsx.vn/Uploads/UploadDocuments/2497378/20260915%20-%20FPT%20-%20TB%20ngay%20DKCC%20phat%20hanh%20CP%20de%20tang%20von%20tu%20NV%20CSH.pdf) | 15/09/2026; tỷ lệ 10:1 | 02/11/2026 | Không hưởng quyền 21/09, đăng ký cuối 22/09 |
| [FTEL công bố Q3](https://fpt.vn/tin-tuc/bao-cao-tai-chinh-hop-nhat-quy-03-2026-15648.html) và [PDF gốc FTEL](https://fpt.vn/storage/upload/files/reports/bctn/bao_cao_tai_chinh_hop_nhat_q03.2026_vn_compressed.pdf) | 23/10/2026; Q3/9T | 02/11/2026 | Đối chiếu số với S27, cùng số khác byte |
| [Infosys cuộc gọi Q2 FY27](https://www.infosys.com/investors/reports-filings/quarterly-results/2026-2027/q2/documents/earningscall.pdf) | 23/10/2026 | 02/11/2026 | AI, giá, nhu cầu, hợp đồng |

## Phát hiện

| Mức | Phát hiện | Cách khắc phục / bằng chứng | Trạng thái |
|---|---|---|---|
| Trung bình | So mức giảm LNST 1.089 tỷ với tác động trước thuế 434 tỷ | Tỷ số 2,5 lần khác cơ sở thuế. Nên so cùng trước/sau thuế; bài đã nói giả định minh họa, hệ số tùy ý | Còn, không chặn |
| Trung bình | Đừng quy giảm dự báo Infosys chỉ do AI | Nguồn nêu nhu cầu, khối lượng, giá, cạnh tranh; AI +29% theo quý, hợp đồng lớn 5,2 tỷ USD là đối trọng. FPT AI/Data +55% đã có trong bài | Còn, không chặn |
| Thấp | S27 khác byte PDF gốc FTEL | Gốc 5.336.462 byte, bản sao 10.997.751 byte; số chính ở ảnh trang 5/PDF 6 trùng nhau. Giới hạn đã nêu | Không chặn |

## Bằng chứng trái chiều và phép tính

Tăng FTEL 9T 13,7%, Q3 13,0%, doanh thu 16,8% khớp báo cáo gốc. Ước FTEL × 45,66% thô ≈ 1.340 tỷ đã ghi giới hạn. Cổ tức 1.124,3 tỷ là khai báo, không phải tiền nhận 2026. Giá đã điều chỉnh 43,4% và quyền 10:1 khớp HOSE. Rủi ro AI được cân bằng với tăng doanh thu AI; chưa chứng minh tác động FPT.

## Hạn chế

S27 không trùng byte PDF trên miền FTEL, nhưng trang công bố và số chính được đối chiếu. Chưa kiểm lại toàn bộ các số khác BCTC FPT và mọi nguồn thứ cấp. Điều phối chỉ bỏ tiền tố nháp và đổi 2 trạng thái vòng đời; hash chuẩn không đổi.

## Kết luận của agent kiểm duyệt

`ĐẠT`: không còn nghiêm trọng/cao. Đã xử lý tăng trưởng FTEL, phân biệt cổ tức khai báo/tiền nhận, giới hạn CFO và độ trễ ký mới/doanh thu.
