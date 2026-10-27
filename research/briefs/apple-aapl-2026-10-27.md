# Đề bài nghiên cứu: Apple Inc. (AAPL)

- Trạng thái: `HOÀN_TẤT_HỒ_SƠ_MẪU`
- Chủ trì: `research_coordinator`
- Chốt dữ liệu lúc: `2026-10-27 12:13 UTC+7 (Asia/Ho_Chi_Minh)`
- Phạm vi địa lý: Hoa Kỳ và hoạt động toàn cầu.
- Thị trường / mã / ngành: Nasdaq / AAPL / thiết bị và dịch vụ công nghệ tiêu dùng.
- Mục tiêu học tập: Thực hành truy báo cáo gốc, phân biệt năm và chín tháng, mô hình kinh doanh, rủi ro và kịch bản.
- Câu hỏi quyết định được hỗ trợ: Những giả định nào cần đúng để hiểu khả năng tạo dòng tiền của doanh nghiệp? Không phải lệnh giao dịch.

## Câu hỏi cốt lõi

1. Thiết bị và dịch vụ đóng góp thế nào, rủi ro tập trung và chuỗi cung ứng là gì?
2. Lợi nhuận, dòng tiền, vốn và phân bổ vốn phản ánh điều gì, giới hạn nào chưa được chứng minh?
3. Kịch bản bất lợi/cơ sở/thuận lợi và điều kiện bác bỏ là gì?

## Phạm vi

- Bao gồm: FY2025 và hồ sơ chín tháng FY2026 mới nhất được xác minh, USD, US GAAP; bối cảnh toàn cầu và rủi ro pháp lý/cung ứng.
- Không bao gồm: giá mục tiêu, khuyến nghị mua bán hay hồ sơ cá nhân.
- Nhóm so sánh toàn cầu: Chưa xây dựng bảng đồng nhất; ghi `CHƯA_BIẾT` và cách làm tiếp.

## Kế hoạch tìm nguồn trực tuyến

- Hồ sơ SEC EDGAR, quan hệ nhà đầu tư Apple; nguồn công ty là tự công bố.
- WTO/IMF hoặc nguồn có thẩm quyền cho bối cảnh, không suy dự báo chung thành dự báo Apple.
- Tách dữ liệu kiểm toán năm, hồ sơ quý chưa kiểm toán, dự báo và kịch bản.

## Phân công agent

| Nhánh | Agent | Sản phẩm | Trạng thái |
|---|---|---|---|
| Doanh nghiệp | `company_analyst` | Gói tài chính, mô hình và quản trị | Đã nhận |
| Vĩ mô | `macro_market_researcher` | Bối cảnh và phản chứng | Đã nhận |
| Kiểm nguồn | `source_fact_checker` | Kiểm bản nháp cố định | ĐẠT |
| Phản biện | `risk_bear_reviewer` | Rủi ro và điều có thể làm luận điểm sai | ĐẠT |

## Tiêu chí hoàn thành

- [x] Các nhánh bằng chứng đã tìm nguồn trực tuyến và mở trang gốc.
- [x] Nhận định trọng yếu có URL, kỳ, ngày truy cập và phép tính tái lập.
- [x] Kiểm nguồn và phản biện độc lập hoàn tất cùng mã băm.
- [x] Điều chưa biết, bất đồng và điều kiện làm luận điểm mất hiệu lực được ghi rõ.
