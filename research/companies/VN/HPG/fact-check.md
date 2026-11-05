# Biên bản kiểm nguồn: HPG — vòng 7

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-02 13:58 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Phạm vi: kịch bản chi phí bán hàng, tiền và nợ, CFO/capex, Phố Nối, tiền lệ Q4/2022 và Quyết định 612/1917/1902.
- Báo cáo đích: `research/companies/VN/HPG/report.md`
- SHA-256 nội dung đích: `6541a57d1ed987935686a84ab4c02a7b212da993b49e4c8d56c11e83df70a620`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Phiên chính ghi tóm lược kết quả nhánh độc lập vòng 7; không tự thay kết luận. Tiêu chí: không còn nghiêm trọng/cao; các mức trung bình/thấp được lưu, không chặn. Toàn văn nhánh có trong cuộc trao đổi ngày 02/11/2026.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Công bố / kỳ | Truy cập | Mục đích |
|---|---|---|---|
| [Trang báo cáo HPG](https://www.hoaphat.com.vn/quan-he-co-dong/bao-cao-tai-chinh) và [PDF Q3/2026](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/10/bao-cao-tai-chinh-hop-nhat-qiii-2026.pdf) | 29/10/2026; 30/09/2026, 9T | 02/11/2026 | Tải trực tiếp, so byte và đọc các trang tiền/nợ/dòng tiền |
| [Quyết định 612](https://moit.gov.vn/upload/2005517/fck/files/QD_612_ap_dung_chong_lan_tranh_bien_phap_PVTM_thep_can_nong_e85ba.pdf) | 02/04/2026 | 02/11/2026 | 26 mã HS, biện pháp tạm thời |
| [Cục PVTM về 1917](https://www.trav.gov.vn/default.aspx?category_id=7ab9bb3e-2cbb-421a-bcbd-26aa48d301c3&do=detail&id=ec556014-bec8-491f-84e6-3ef90f2df5a3&page=news-detail) và [PDF gốc](https://www.trav.gov.vn/data/00195410-a87c-4a80-989d-83a83a4e020d/userfiles/files/QD%201917%20ap%20dung%20chong%20lan%20tranh%20chinh%20thuc%20thep%20can%20nong_28_07_2026.pdf) | 28/07/2026 | 02/11/2026 | Điều 3, mức thuế, ngoại lệ, miễn trừ |
| [HPG tổng quan Q1/2026](https://file.hoaphat.com.vn/hoaphat-com-vn/2026/04/bcq1-2026-vn-v4.pdf) | Q1/2026 | 02/11/2026 | LNST không gồm chuyển nhượng, tổng LNST, mảng Phố Nối |
| [HPG tổng quan Q4/2022](https://file.hoaphat.com.vn/hoaphat-com-vn/2023/01/quarter-summary-q4-2022.pdf) | Q4/FY2022 | 02/11/2026 | Tiền lệ gộp âm, lỗ hợp nhất |

| [Vietcap Q2/2026](https://trading.vietcap.com.vn/iq/report-detail/vi/hpg-loi-nhuan-cot-loi-quy-2-tiep-tuc-tang-truong-voi-bien-loi-nhuan-tiep-tuc-cai-thien-phu-hop-voi-ky-vong-bao-cao-kqkd) | 01/08/2026; Q2/2026 | 02/11/2026 | Xác nhận chi phí bán hàng 1.718 tỷ |
| [ABS Q4/2022](https://www.abs.vn/wp-content/uploads/2023/03/HPG-Earning-review-report.pdf) và [VDSC Q4/2022](https://vdsc.com.vn/data/api/app/file-storage/bacfbc52-d124-4fcb-a5bf-08db33e114fc/HPG_Result%20Update_Mar%202023_Vie.pdf) | 03/2023; Q4/2022 | 02/11/2026 | Bán hàng 716, quản lý 343, lãi vay 933 tỷ |

## Phát hiện

| Mức | Phát hiện | Bằng chứng / khắc phục | Trạng thái |
|---|---|---|---|
| Trung bình | URL Elibook S25 không truy cập được | Vietcap Q2 đang mở xác nhận 1.718 tỷ. Bản sửa gắn đúng Q2/2026 và nêu rõ giả định giữ chi phí, không gán mức này cho Q4/2022 | Không chặn; nên bổ sung URL Vietcap khi cập nhật nguồn |
| Thấp | Lỗ Q4/2022 1.992 theo ABS/VDSC khác 1.999 theo HPG | Hồ sơ ghi khoảng và nguồn thứ cấp; có thể ghi khoảng 2.000 hoặc cả hai nguồn | Không chặn |

## Kiểm tra phép tính

Đã đọc lại tệp từ đĩa và kiểm hash mới. 1.718 tỷ là mức Q2/2026; tiền lệ Q4/2022 chỉ là độ cứng chi phí (716 so 711). Stress: 36.794×8%=2.943,52; lãi vay 1.774×1,15=2.040,1; trừ bán hàng 1.718 còn khoảng−815 trước khoản khác. Gộp bằng 0 cho−3.758. Các phép tính không mô tả tái hiện đầy đủ lịch sử.

612 và 1917 đều 26HS;1917 hiệu lực sau 15 ngày, suy ra 12/08/2026. PDF HPG19.523.137 byte tải trực tiếp có SHA-256 `a54c55eff615a80cb9c2e80da7893881d0dc31c1fa6aa81b682873bc89de01e2`, khớp payload. Tiền 6.852,877, đầu tư ngắn hạn 39.273,855, vay 78.615,049+27.121,713; nợ ròng theo tiền 98.883,885, theo cả đầu tư 59.610,030 tỷ; CFO20.936,329−capex 14.607,166=6.329,163 tỷ. Số Q1 không trộn với số PSI hay suy tiền thu/thuế.

## Hạn chế

BCTC Q3 chưa kiểm toán/soát xét; S25 không mở được nhưng đã kiểm số bằng Vietcap. Chưa rà hết các nguồn hàng hóa/vĩ mô nhỏ. Điều phối chỉ bỏ nhãn nháp và đổi hai trạng thái vòng đời sau kiểm; hash chuẩn không đổi.

## Kết luận của agent kiểm duyệt

`ĐẠT`: không còn nghiêm trọng/cao, giữ hai phát hiện trung bình/thấp.
