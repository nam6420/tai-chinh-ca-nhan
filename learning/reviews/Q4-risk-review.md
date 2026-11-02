# Biên bản phản biện rủi ro — Bài Q4

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Toàn bài; quy tắc SEC, nhận định pháp lý Việt Nam từ nguồn thứ cấp, quy ước hồ sơ nộp muộn nhất, dung sai, chép tay PDF ảnh, nhãn, đáp án`
- Báo cáo đích: `learning/lessons/Q4-getting-data-edgar-xbrl-vietnam.md`
- SHA-256 nội dung đích: `d08f14b282f9be4cec2af02cce8f5f9e79e683b1a8e597193cf3fd88a24e4d7c`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên chép và tổng hợp kết quả của nhánh độc lập vòng 5 (nhánh kiểm không đọc kết luận của nhánh kia và không sửa bài). Tiêu chí ĐẠT của các vòng 4–5: không còn lỗi nghiêm trọng hoặc mức cao chưa xử lý; phát hiện trung bình và thấp được liệt kê, không chặn.

## Kết quả

Tám điểm sửa sau vòng 4 khắc phục thật (ytd_value cùng quy tắc chọn hồ sơ, User-Agent, 20-F, Điều 14 khoản 4–5, năm đẳng thức chỉ kiểm tổng, bảng nguồn, dung sai).

## Hạn chế

- Nhánh kiểm duyệt đã kiểm mã băm bản nháp `283f16b2904a730535dd24c609597343823c4a6fc18e94e967fc11867a5e1020`. Sau đó điều phối viên chỉ chuẩn hóa dòng siêu dữ liệu đầu bài (bỏ nhãn nháp, đặt trạng thái ĐẠT, thêm dòng biên bản), không đổi nội dung dạy; `validate_report.py` tính mã băm trên nội dung chuẩn nên mã ở trên khác mã nhánh kiểm duyệt dùng.
- Các vòng kiểm duyệt 1–4 (nhật ký ở learning/reviews/Q-round-1.md đến Q-round-4.md) đã sửa nhiều lỗi; vòng 5 là vòng cuối trên bản này.
- Điểm trung bình còn mở (phản biện): "cùng quy tắc chọn" chưa chắc "cùng cơ sở trình bày" (số cả năm và số 9 tháng có thể thuộc hai lần trình bày); quý 4 suy ra không áp cho EPS và số bình quân gia quyền; dung sai 0,01 cho đẳng thức nhiều số hạng có thể báo lỗi giả. Điểm thấp: giới hạn độ chính xác của dung sai mặc định, đáp án bài tập 2 gọi User-Agent là "phải", nhãn câu 20-F, nguồn thứ cấp của Thông tư, `annual_series` im lặng với số tồn và kỳ chuyển đổi.
