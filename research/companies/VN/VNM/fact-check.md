# Biên bản kiểm nguồn: VNM — vòng 6

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-02 13:49 Asia/Ho_Chi_Minh`
- Chốt dữ liệu lúc: `2026-10-31 (Asia/Ho_Chi_Minh)`
- Phạm vi: BCTC Q3 và 9T2026, chi phí tài chính, cầu nối lợi nhuận, tiền ròng, cổ tức và kịch bản.
- Báo cáo đích: `research/companies/VN/VNM/report.md`
- SHA-256 nội dung đích: `e921a25991a02d0f36c8af7f4fb79eec5db4d9b703ee15051ba261382252c60a`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Lỗi cao chưa xử lý: `0`

Phiên chính chép tóm lược kết quả nhánh độc lập vòng 6; không tự thay kết luận. Tiêu chí: không còn lỗi nghiêm trọng/cao; trung bình/thấp ghi lại và không chặn. Toàn văn nhánh được trả trong cuộc trao đổi ngày 02/11/2026.

## Các nguồn Internet đã tự mở trong lượt kiểm duyệt

| URL | Công bố / kỳ | Truy cập | Mục đích |
|---|---|---|---|
| [Vinamilk, báo cáo tài chính](https://i04-eshop-vn.apps.vinamilk.tech/investor/reports/financial) | 30/10/2026; Q3/9T2026 | 02/11/2026 | Ngày và trạng thái soát xét |
| [PDF trên miền công ty](https://d8um25gjecm9v.cloudfront.net/cms/20261030_VNM_BCTC_da_soat_xet_Q3_2026_Hop_nhat_010a30af2b.pdf) và [PDF gương](https://cdn.24hmoney.vn/upload/file/2026-4/2026-10-31/no-name-1793388857.pdf) | Kỳ 30/09/2026 | 02/11/2026 | Tự tải qua node fetch, so byte và đọc ảnh PDF63 |
| [Trang lưu 24hmoney](https://24hmoney.vn/report/72986/financialstatements) | 31/10/2026 | 02/11/2026 | Dấu vết bản sao; trang gọi nhầm là kiểm toán |

| [VSDC cổ tức 2025](https://vsdc.vn/vi/ad1/197038) và [cổ tức 2026](https://vsdc.vn/vi/ad1/201961) | 17/06 và 29/10/2026 | 02/11/2026 | 1.850 và 2.500 đồng/cổ phiếu, ngày chốt và thanh toán |
| [VSDC hồ sơ VNM](https://vsdc.vn/en/s-detail/943) | Trang động | 02/11/2026 | 2.089.955.445 cổ phiếu |
| [Vietstock Q3](https://vietstock.vn/2026/10/dong-luc-tang-truong-loi-nhuan-rong-quy-3-hon-17-cua-vinamilk-den-tu-dau-737-1509811.htm) và [Doanh nhân - Pháp luật](https://doanhnhan.baophapluat.vn/sua-viet-nam-vinamilk-lai-rong-quy-iii-tang-17-hoan-thanh-gan-88-ke-hoach-loi-nhuan-nam.html) | 31/10/2026 | 02/11/2026 | Kiểm chéo số Q3/9T, vẫn là thứ cấp |
| [PHS giải trình](https://www.phs.vn/tin-tuc/vnm-giai-trinh-kqkd-quy-32026-va-9-thang-dau-nam-2026-so-voi-cung-ky-nam-truoc/6444605), [GDT](https://www.globaldairytrade.info/en/product-results/whole-milk-powder) | 30/10/2026; trang GDT động | 02/11/2026 | Dấu vết công bố; PDF giải trình và sự kiện GDT cũ chưa đọc được |

## Phát hiện

| Mức | Phát hiện | Bằng chứng / xử lý | Trạng thái |
|---|---|---|---|
| Thấp | S23 còn cảnh báo chưa so byte | Hai PDF tải trực tiếp cùng 3.958.733 byte, SHA-256 `fd144a9acb3bacbc745cde32d6375471b11b4b005e1919996631b6735d7c8378`. Đã khớp byte. Trang lưu gọi kiểm toán, PDF thực tế soát xét | Cảnh báo cũ bảo thủ, không chặn; manifest đã bổ sung kết quả |

## Kiểm tra phép tính

- Chi phí tài chính 9T: 453.303.861.156 / 242.667.487.576 − 1 = 86,8%, làm tròn 87%; Q3: 151.405.579.644 / 91.354.486.972 − 1 = 65,7%, làm tròn 66%.
- Cầu nối Q3: LNTT tăng 568,40 tỷ; tài chính và liên kết gộp tăng 439,72 tỷ (77,4%); trừ biến động chi phí tài chính còn 379,66 tỷ (66,8%).
- Cầu nối 9T: LNTT tăng 2.434,58 tỷ; hai khoản gộp tăng khoảng 588,82 tỷ (24,2%); sau chi phí tài chính còn khoảng 378,19 tỷ (15,5%), sai khác nhỏ do làm tròn.
- Tiền ròng: 3.611,99 + 22.925,58 − 8.384,69 − 97,39 = 18.055,49 tỷ.
- 4.350 đồng × 2.089.955.445 cổ phiếu ≈ 9.091,3 tỷ, khoảng 96,6% LNST mẹ ước tính. Tỷ lệ 108% theo EPS có mẫu số khác, đã nêu.
- Kịch bản Q4 khớp công thức; đuôi lịch sử là tham chiếu, không phải dự báo.

## Hạn chế

Trình duyệt trả 403 nhưng node fetch lấy được đúng tệp trên miền công ty; đã đọc ảnh trang chi phí tài chính. Chưa đối chiếu toàn bộ giá nguyên liệu, ngành sữa, một số số FY2025 và nguồn của kịch bản. Các giới hạn này được ghi trong hồ sơ. Điều phối chỉ bỏ tiền tố nháp và đổi hai trạng thái sau kiểm; hash chuẩn không đổi.

## Kết luận của agent kiểm duyệt

`ĐẠT`: đầu vào chi phí tài chính tăng 87% được xác nhận trực tiếp; không còn lỗi nghiêm trọng/cao. Còn một cập nhật nguồn mức thấp.
