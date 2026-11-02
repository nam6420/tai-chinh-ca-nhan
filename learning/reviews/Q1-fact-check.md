# Biên bản kiểm nguồn — Bài Q1

- Loại kiểm duyệt: `KIỂM_NGUỒN`
- Agent kiểm duyệt: `source_fact_checker`
- Kiểm duyệt lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Phạm vi: `BCTC HPG FY2025, Altman (2000) bản sao, Piotroski (2000), Wikipedia Beneish và Altman, nghiên cứu Ba Lan, earnings_quality.py, CSV và test`
- Báo cáo đích: `learning/lessons/Q1-earnings-quality-toolkit.md`
- SHA-256 nội dung đích: `24094d79412f978315831ab00ed85071672e24694c194b4fe6bab8d6fdbe36c3`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên chép và tổng hợp kết quả của nhánh độc lập vòng 6 (nhánh kiểm không đọc kết luận của nhánh kia và không sửa bài). Tiêu chí ĐẠT của các vòng 4–6: không còn lỗi nghiêm trọng hoặc mức cao chưa xử lý; phát hiện trung bình và thấp được liệt kê, không chặn.

## Kết quả

Mọi số HPG (bảng cân đối, kết quả kinh doanh, lưu chuyển tiền tệ, thuyết minh 7, 12, 23, 26), M-score −1,5748, Z'' 2,525, Z' ≈ 1,49, độ nhạy Z'' (2,47 và 2,69), F-score 6/5, Bảng 7 và hệ số của Altman (2000), danh mục tham khảo Wikipedia khớp nguồn. 76 test đạt.

## Hạn chế

- Nhánh kiểm duyệt đã kiểm mã băm bản nháp `31e2d2c6abdf78e65e4e2352bc406bc20bd9daba1e903529442ebbc5f32d6503`. Sau đó điều phối viên chỉ chuẩn hóa siêu dữ liệu đầu bài (bỏ nhãn nháp, trạng thái ĐẠT, dòng biên bản, dòng "sửa sau các vòng"), không đổi nội dung dạy; `validate_report.py` tính mã băm trên nội dung chuẩn nên mã ở trên khác mã nhánh kiểm duyệt dùng.
- Các vòng 1–5 trước đó (tóm lược ở learning/reviews/Q-round-1.md đến Q-round-4.md và Q-round-5-6.md) đã sửa nhiều lỗi; vòng 6 là vòng cuối trên bản này.
- Điểm trung bình/thấp còn mở (kiểm nguồn): chưa mở lại tóm tắt Beneish 1999, hai nghiên cứu Việt Nam và báo cáo thường niên 2023 ở vòng 6; "−2,22 đúng 71%" nên ghi là độ chính xác chung (67% nhóm thao túng, 75% nhóm không); bản sao Altman tự mâu thuẫn 1,21 so với 1,23; cụm "không rõ bản quyền" về bản Scribd là nhận xét của người soạn, chưa kiểm.
- `CHƯA_BIẾT` còn mở: Beneish (1999) và Altman (1968, 2017) toàn văn; hệ số Beneish và cận 2,6/1,1 chỉ có nguồn thứ cấp.
