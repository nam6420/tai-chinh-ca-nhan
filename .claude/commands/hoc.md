---
description: "Học một khái niệm kinh doanh/tài chính với subagent business-tutor"
argument-hint: "<khái niệm hoặc câu hỏi>"
---

Khái niệm cần học: $ARGUMENTS

Nếu phần trên trống, hỏi lại người dùng một câu ngắn trước khi bắt đầu.

1. Giao cho subagent `business-tutor` bằng công cụ `Agent`, prompt tự chứa gồm khái niệm, trình độ người mới và yêu cầu dưới đây.
2. Bắt buộc tìm kiếm Internet trong chính lượt này (`WebSearch` rồi `WebFetch` mở trang nguồn thực tế); không dùng trí nhớ mô hình hay dữ liệu cũ trong repo.
3. Giải thích bằng tiếng Việt, có ví dụ từ một doanh nghiệp thật, 2–3 lỗi người mới hay mắc, bài tập ngắn và đáp án gợi ý.
4. Ghi `Chốt dữ liệu lúc` kèm ngày, giờ, múi giờ và dẫn nguồn sát nhận định.
5. Khi xong, trình bày bài học cho người dùng và đề xuất lưu vào `learning/` theo `templates/learning-note.md` nếu người dùng đồng ý (phiên chính ghi, subagent không ghi).

Không đưa khuyến nghị mua/bán cá nhân hóa. Người dùng phải tự quyết định.
