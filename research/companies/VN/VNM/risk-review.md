# Biên bản phản biện rủi ro: VNM — vòng 6

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
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

| [Vietcap gặp nhà đầu tư](https://www.vietcap.com.vn/en/research-center/vnm-continuing-to-benefit-from-broad-based-market-share-gains-premiumization-economies-of-scale-analyst-meeting-note) | 06/08/2026; H1/2026 | 02/11/2026 | Giá, sản lượng, thị phần; nguồn thứ cấp |
| [Báo Chính phủ Q1/2023](https://baochinhphu.vn/vinamilk-doanh-thu-quy-i-2023-dat-22-ke-hoach-nam-du-kien-tiep-tuc-khoi-sac-10223042910485053.htm) và [VnExpress FY2025](https://vnexpress.net/vinamilk-ghi-nhan-doanh-thu-cao-ky-luc-5012803.html) | 29/04/2023 và 02/02/2026 | 02/11/2026 | Mùa vụ và nền Q4/2025 |
| [Hiệp hội Sữa Việt Nam](https://vda.org.vn/vinamilk-sap-chot-danh-sach-co-dong-tra-co-tuc-tien-mat/) | 21/06/2026 | 02/11/2026 | Cổ tức 4.350 đồng, khoảng 9.100 tỷ |

## Phát hiện

| Mức | Phát hiện | Cách khắc phục / bằng chứng | Trạng thái |
|---|---|---|---|
| Trung bình | Mốc đuôi Q1 không cùng mùa với Q4 | Hồ sơ đã ghi quý tham chiếu và tái cấu trúc Q1/2025; không coi là phân phối xác suất Q4. Khi mở rộng nên dùng nhiều Q4 cùng cơ sở | Không chặn |
| Trung bình | Giá, sản lượng, thị phần chưa tách định lượng | Vietcap nêu tăng giá 3–4% và sản lượng H1 cao một chữ số nhưng thiếu bảng gốc. Báo cáo đã để CHƯA_BIẾT, không dùng doanh thu để tự chứng minh thị phần | Không chặn |
| Thấp | Cảnh báo chưa khớp byte đã được giải quyết trong lượt kiểm | Tự tải hai URL, cùng byte và hash như bảng nguồn; PDF là soát xét | Không chặn |

## Bằng chứng trái chiều và phép tính

Chi phí tài chính 9T tăng 86,8% khớp nguồn gốc. Kịch bản căng cho khoảng 10.264 tỷ LNST mẹ cả năm, tốc độ chạy năm 6.817 tỷ; bài nêu rõ minh họa. Cổ tức 2025 gần 96,6% LNST mẹ là rủi ro hợp lý để theo dõi, không chứng minh tiền sẽ cạn. Q1/2023 chỉ là mốc thấp khác mùa, không phải Q4 lịch sử. Doanh thu tăng có thể đến từ giá, sản lượng hay cơ cấu; chưa có dữ liệu gốc đủ tách.

## Hạn chế

Chưa có số sơ cấp về sản lượng, giá thực thu theo nhóm hàng hay thị phần cùng phạm vi. Tệp gương đã khớp byte CDN công ty; tiêu đề trang gương gọi nhầm kiểm toán. Điều phối chỉ bỏ nháp và đổi hai dòng trạng thái, không đổi nội dung chuẩn sau kiểm.

## Kết luận của agent kiểm duyệt

`ĐẠT`: không có lỗi nghiêm trọng/cao. Các giới hạn được ghi rõ; giữ hai phát hiện trung bình và một thấp cho lần nâng cấp.
