# Chuẩn chiều sâu của bài học

Trạng thái: `Ý_KIẾN` — ngưỡng để thử, không phải ngưỡng khoa học. Cơ sở: [đánh giá 2026-10-31](../learning/review-depth-audit-and-gap-plan-2026-10-31.md). Kiểm tự động: `python3 scripts/check_lesson_depth.py`.

## Hai bậc

- **Bậc S (sâu)**: bài dạy được người mới làm việc đó. Mọi bài lõi định giá, mô hình, chất lượng lợi nhuận phải đạt bậc này.
- **Bậc P (tóm tắt)**: phiếu khái niệm có kiểm nguồn. Chấp nhận cho chủ đề ngoài lõi, nhưng phải được ghi là bậc P và nằm trong danh sách nâng cấp.

## Yêu cầu bậc S

1. Tổng độ dài tệp từ 2.500 đến 6.500 từ, chia phiên có điểm dừng (nới trần từ 4.500 lên 6.500 từ để các bài chuyên sâu không phải viết nén hoặc dính chữ).
2. Mục `## Ví dụ từ nguồn thật` (hoặc có đánh số thứ tự mục): ít nhất một số liệu từ báo cáo gốc, ghi kỳ, đơn vị, phạm vi và liên kết mở được. Có ví dụ hư cấu đủ dữ kiện để tự tính.
3. Mục `## Bài tập` (hoặc có đánh số thứ tự mục) có ít nhất 8 câu đánh số, gồm nhận biết, tính nhiều bước và tình huống chuyển giao; có mục `## Đáp án` giải từng bước.
4. Mục `## Bài làm với dữ liệu thiếu hoặc lệch` (bài "bẩn"): đề cố ý thiếu dữ kiện hoặc lệch đơn vị/kỳ; đáp án nêu cách phát hiện.
5. Mục `## Sai ở đâu`: một phân tích sai có chủ ý để người học tìm lỗi.
6. Mục `## Kiểm tra chuyển bài`: 3 câu làm không nhìn mẫu, kèm tiêu chí đạt.
7. Với bài có tính toán: liên kết tới tệp mẫu trong `learning/practice/models/` tái lập được ví dụ chính.
8. Siêu dữ liệu kiểm duyệt gọn ở đầu; bảng nguồn ở cuối.

## Sau khi nâng cấp

Bản đã sửa là bản mới. Biên bản kiểm nguồn/phản biện cũ gắn với mã băm cũ **không còn áp dụng**; bài mang nhãn `BẢN NHÁP - CHƯA KIỂM DUYỆT` đến khi hai biên bản mới khớp mã băm mới.
