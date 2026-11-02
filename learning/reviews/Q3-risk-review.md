# Biên bản phản biện rủi ro — Bài Q3

- Loại kiểm duyệt: `PHẢN_BIỆN_RỦI_RO`
- Agent kiểm duyệt: `risk_bear_reviewer`
- Kiểm duyệt lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Chốt dữ liệu lúc: `2026-11-02 (Asia/Ho_Chi_Minh)`
- Phạm vi: `Toàn bài; cherry-pick cửa sổ, khoản một lần, kịch bản, đòn bẩy, nhãn, đáp án, ngầm đắt/rẻ hay mua/bán`
- Báo cáo đích: `learning/lessons/Q3-normalizing-earnings-cyclical.md`
- SHA-256 nội dung đích: `3b543db8af30c603e9826e2f7968e4b440753045ef64c8f01af35a9d6b82dbbc`
- Kết luận: `ĐẠT`
- Lỗi nghiêm trọng chưa xử lý: `0`
- Người ghi: Điều phối viên chép và tổng hợp kết quả của nhánh độc lập vòng 6 (nhánh kiểm không đọc kết luận của nhánh kia và không sửa bài). Tiêu chí ĐẠT của các vòng 4–6: không còn lỗi nghiêm trọng hoặc mức cao chưa xử lý; phát hiện trung bình và thấp được liệt kê, không chặn.

## Kết quả

Các điểm sửa sau vòng 5 (khoản một lần, mức A/B/C, đòn bẩy chưa chứng minh tăng, doanh thu 2017–2019 chưa trừ giảm trừ) khắc phục thật; bài không dạy coi biên 11,6% là biên chuẩn và không có kết luận đắt/rẻ hay mua/bán.

## Hạn chế

- Nhánh kiểm duyệt đã kiểm mã băm bản nháp `ae5b1af9badcc4f57798280bcf81952b5ea0bf42fe83489ff534e850453cc8db`. Sau đó điều phối viên chỉ chuẩn hóa siêu dữ liệu đầu bài (bỏ nhãn nháp, trạng thái ĐẠT, dòng biên bản, dòng "sửa sau các vòng"), không đổi nội dung dạy; `validate_report.py` tính mã băm trên nội dung chuẩn nên mã ở trên khác mã nhánh kiểm duyệt dùng.
- Các vòng 1–5 trước đó (tóm lược ở learning/reviews/Q-round-1.md đến Q-round-4.md và Q-round-5-6.md) đã sửa nhiều lỗi; vòng 6 là vòng cuối trên bản này.
- Điểm trung bình còn mở (phản biện): **đáp án bài tập 10 vẫn viết "vốn mới nhờ vay nhiều", mâu thuẫn với thân bài ("đòn bẩy tăng chưa chứng minh")**; 11,6% là biên chín tháng thuận lợi, chưa phải biên chuẩn, và nếu 3.800 là lãi trước thuế thì biên điều chỉnh cao hơn; khoản Phố Nối: người mua có thể thuộc cùng hệ sinh thái Hòa Phát (24hmoney, thứ cấp) và khoản Thiên Long khoảng 907 tỷ chỉ thấy ở trích đoạn tìm kiếm (`CHƯA_BIẾT`); điều kiện mất hiệu lực chưa gắn rõ với luận điểm.
- Điểm thấp: 4.400 so 4.512; chưa nêu chi phí đi vay từng được vốn hóa vào xây dựng dở dang; 2017–2019 là lợi nhuận hợp nhất còn FY2021+ là LNST công ty mẹ; bài tập 9 ghi "bốn câu hỏi" mà đáp án nêu nhiều hơn.
