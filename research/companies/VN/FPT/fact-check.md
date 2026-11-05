# Biên bản kiểm nguồn: FPT — vòng 7

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
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
| [BCTN FPT 2025](https://fpt.com/-/media/project/fpt-corporation/fpt/ir/information-disclosures/year-report/2026/april/20260408---fpt---annual-report-2025.pdf) | 08/04/2026; FY2025 | 02/11/2026 | Cơ sở hợp nhất FTEL |
| [HOSE nghị quyết tăng vốn](https://staticfile.hsx.vn/Uploads/UploadDocuments/2503014/20261007%20-%20FPT%20-%20Nghi%20quyet%20HDQT%20so%2001.10.2026%20vv%20tang%20von%20sau%20phat%20hanh%20CP%20de%20tang%20von%20tu%20NVCSH.pdf) | 06/10/2026 | 02/11/2026 | 171.401.226 CP |
| [CafeF giá28/10](https://cafef.vn/ban-rong-trien-mien-khoi-ngoai-van-con-nam-hon-455-trieu-co-phieu-fpt-188261028190244374.chn) và [giá 15/07](https://nongnghiepmoitruong.vn/ky-luc-buon-43-ty-usd-cua-fpt-nha-dau-tu-nuoc-ngoai-rut-von-manh-d821626.html) | 28/10 và 15/07/2026 | 02/11/2026 | Giá thứ cấp |
| [NSO](https://www.nso.gov.vn/?p=62592), [Bộ Công Thương](https://moit.gov.vn/en/news/u.s.-trade-representative-issues-final-determination-in-section-301-investigation-covering-60-economies.html), [USTR](https://ustr.gov/about/policy-offices/press-office/press-releases/2026/july/ustr-takes-action-forced-labor-section-301-investigations) | 03/10,28/07,23/07/2026 | 02/11/2026 | GDP và thuế 301; không suy cho dịch vụ |

## Phát hiện

| Mức | Phát hiện | Cách xử lý / bằng chứng | Trạng thái |
|---|---|---|---|
| Trung bình | Ước phầnFTEL dùng tổng LNST thay vì phần mẹ | FTEL có LNST mẹ 2.883,806 và thiểu số 50,139 tỷ. 2.883,806×45,66%≈1.316,7 tỷ ≈59,3% liên kết FPT, khác ước 1.340 tỷ nhưng vẫn xấp xỉ 60%. Hồ sơ gọi thô và CHƯA_BIẾT tỷ trọng thực | Còn, không chặn |
| Thấp | Dòng trống trước S27 làm tách bảng nguồn | Xóa dòng trống để bảng liền, URL vẫn đọc được | Còn, không chặn |

## Kiểm tra phép tính

FTEL Q3:1.022,468/904,823−1≈13,0%; 9T:2.933,945/2.580,936−1≈13,7%; doanh thu 16.690,580/14.286,917−1≈16,8%. Đã loại+33/+9 sai trong văn xuôi Znews; bảng quý của chínhZnews khớp BCTC và mâu thuẫn tỷ lệvănxuôi. Tiền ròng 16.596,5−28.827,0=−12.230,5 tỷ; CFO951,98/7.776,44≈12,2%; giá 54.000/(105.000/1,1)−1≈−43,4%; kịch bản khớp công thức.

## Hạn chế

Bản FTEL đã đối chiếu ảnh PDF 6; trang chính thức FTEL liệt kê 23/10 nhưng công cụ web có lúc timeout. PDF FPT trên HOSE mở 54 trang nhưng không có chữtrích; số chínhđối chiếu thông cáo công ty. Giá và bối cảnh một phần còn thứ cấp. Điều phối chỉ bỏ nhãn nháp/đổi 2 trạng thái sau kiểm; hash chuẩn không đổi.

## Kết luận của agent kiểm duyệt

`ĐẠT`: đã sửa lỗi cao về tăng trưởng FTEL; không còn nghiêm trọng/cao, giữ hai điểm trung bình/thấp.
