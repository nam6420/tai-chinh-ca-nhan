# Phòng học và nghiên cứu chứng khoán

Đây là kho học tập và nghiên cứu về kinh doanh, doanh nghiệp, thị trường và chứng khoán trên phạm vi toàn cầu. Mục tiêu là giúp người học đi từ kiến thức nền đến quy trình nghiên cứu có nguồn, có phản biện và có nhật ký quyết định.

Repo này **không phải dịch vụ tư vấn đầu tư**. Các agent không đặt lệnh, không quản lý tài khoản, không cam kết lợi nhuận và không thay người dùng đưa ra quyết định tài chính.

## Bắt đầu nhanh

1. Đọc [lộ trình khởi động](docs/GETTING_STARTED.md).
2. Chọn mục tiêu: học khái niệm, nghiên cứu ngành/thị trường hoặc nghiên cứu doanh nghiệp.
3. Dùng câu lệnh mẫu trong [đội agent](docs/AGENT_TEAM.md).
4. Lưu đầu ra theo [quy trình nghiên cứu](docs/WORKFLOW.md).
5. Chạy kiểm tra cấu hình:

   ```bash
   python3 scripts/verify.py
   ```

Trong một phiên Codex mới, yêu cầu: `Hãy spawn business_tutor, chờ agent hoàn tất rồi cho tôi biết tên vai trò của agent đó.` Sau đó dùng `/agent` trong giao diện dòng lệnh và xác nhận có luồng `business_tutor`. Việc chỉ liệt kê tệp trong `.codex/agents/` không chứng minh custom agent đã được nạp hoặc spawn thành công.

Trong một phiên Qwen Code mới, yêu cầu tương tự: `Hãy spawn business_tutor, chờ agent hoàn tất rồi cho tôi biết tên vai trò của agent đó.` Sau đó dùng `/agents manage` và xác nhận có `business_tutor`. Việc chỉ liệt kê tệp trong `.qwen/agents/` không chứng minh custom agent đã được nạp hoặc spawn thành công. Ba lệnh tắt của dự án: `/hoc`, `/nghien-cuu-doanh-nghiep`, `/nghien-cuu-nganh`.

Trong một phiên DeepSeek Harness (DSH) mới, các vai trò là project skill native: gõ `/` để thấy `hoc`, `nghien-cuu-doanh-nghiep`, `nghien-cuu-nganh` và chọn, hoặc nhờ agent nạp skill `business-tutor`. Để kiểm tra Agent Teams, yêu cầu: `Hãy spawn một teammate tên business-tutor, bảo nó đọc skill business-tutor rồi trả lời tôi nó giữ vai trò gì.` Xác nhận trong danh sách thành viên nhóm có `business-tutor`. Việc chỉ liệt kê tệp trong `.agents/skills/` không chứng minh skill đã được nạp hoặc teammate đã spawn thành công.

Trong một phiên Claude Code mới (mở tại gốc repo), yêu cầu: `Hãy dùng subagent business-tutor, chờ hoàn tất rồi cho tôi biết tên vai trò của agent đó.` Sau đó gõ `/agents` và xác nhận có `business-tutor` trong mục project. Ba lệnh tắt: `/hoc`, `/nghien-cuu-doanh-nghiep`, `/nghien-cuu-nganh`. Việc chỉ liệt kê tệp trong `.claude/agents/` không chứng minh subagent đã được nạp.

## Cấu trúc

```text
.agents/skills/      Vai trò và lệnh tắt native của DeepSeek Harness
.claude/agents/      Subagent của dự án (bản Claude Code)
.claude/commands/    Lệnh tắt slash cho Claude Code
.codex/agents/       Custom agent của dự án (bản Codex)
.qwen/agents/        Custom agent của dự án (bản Qwen Code)
.qwen/commands/      Lệnh tắt slash của dự án cho Qwen Code
docs/                Cách học, quy trình và tiêu chuẩn nghiên cứu
learning/            Lộ trình, bảng thuật ngữ và bài học
research/            Đề bài, hồ sơ nghiên cứu và báo cáo tổng hợp
data/                Dữ liệu gốc, dữ liệu xử lý và nguồn gốc dữ liệu
watchlists/          Danh sách theo dõi, không đồng nghĩa khuyến nghị
journal/             Nhật ký giả thuyết và quyết định của người học
templates/           Mẫu tài liệu chuẩn
scripts/             Kiểm tra cấu hình và cổng xuất bản
```

## Nguyên tắc cốt lõi

- Tất cả đầu ra cho người dùng bằng tiếng Việt.
- Mọi câu trả lời nội dung phải tìm kiếm Internet trong chính lượt hiện tại; không trả lời từ trí nhớ mô hình hoặc bản lưu cũ trong repo.
- Phạm vi nghiên cứu là toàn cầu. Dùng nguồn gốc chính thức tại thị trường liên quan và đối chiếu quốc tế khi hữu ích.
- Ghi rõ thời điểm chốt dữ liệu và dẫn nguồn sát nhận định.
- Tách biệt `SỰ_THẬT`, `PHÉP_TÍNH`, `SUY_LUẬN`, `KỊCH_BẢN`, `Ý_KIẾN`.
- Mọi báo cáo doanh nghiệp phải có luận điểm thuận, nghịch và điều kiện làm luận điểm mất hiệu lực.
- Không biến định giá thành khuyến nghị mua/bán.

Xem bài [Khởi đầu 30 phút](learning/lessons/001-business-financial-statements.md) và [bảng thuật ngữ](learning/glossary.md) nếu bạn bắt đầu từ con số 0.
