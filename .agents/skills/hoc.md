---
name: hoc
description: "Lệnh tắt /hoc: gọi vai trò business-tutor để học một khái niệm kinh doanh hoặc tài chính."
disable-model-invocation: true
user-invocable: true
---

# `/hoc` — học một khái niệm

Phần văn bản còn lại sau `/hoc` là khái niệm hoặc câu hỏi cần học. Nếu người dùng chưa nêu khái niệm, hỏi lại một câu ngắn trước khi bắt đầu.

## Cách thực hiện

1. Nạp kỹ năng `business-tutor` và làm đúng vai trò đó.
2. Nếu phiên có Agent Teams: `spawn_teammate` một teammate với `description` "Gia sư kinh doanh/tài chính" và `prompt` tự chứa, trong đó yêu cầu teammate đọc skill `business-tutor` trước khi dạy. Nếu không có Agent Teams, tự thực hiện theo skill `business-tutor`.
3. Bắt buộc tìm kiếm Internet trong chính lượt này (`web_search` rồi `web_fetch` mở trang nguồn thực tế); không dùng trí nhớ mô hình hay dữ liệu cũ trong repo.
4. Giải thích bằng tiếng Việt, có ví dụ từ một doanh nghiệp thật, 2–3 lỗi người mới hay mắc, bài tập ngắn và đáp án gợi ý.
5. Ghi `Chốt dữ liệu lúc` kèm ngày, giờ, múi giờ và dẫn nguồn sát nhận định.
6. Khi xong, tóm tắt lại cho người dùng và đề xuất lưu bài học vào `learning/` theo `templates/learning-note.md` nếu người dùng đồng ý.

Không đưa khuyến nghị mua/bán cá nhân hóa. Người dùng phải tự quyết định.
