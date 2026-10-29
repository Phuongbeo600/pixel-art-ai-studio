# Project Backlog

Bảng theo dõi các đầu việc (Tasks & Features) của dự án **Pixel Art AI Studio**.

---

## 📋 To Do (Cần làm)
- [ ] **TASK-002: Tích hợp mô hình AI sinh Pixel Art thực tế**
  - [ ] Khảo sát và lựa chọn mô hình AI (Pixel Art Diffusion LoRA / API).
  - [ ] Cài đặt `AIGenerator` kế thừa `BaseGenerator`.
  - [ ] Xây dựng thuật toán hậu xử lý downsampling & color quantization.
  - [ ] Tích hợp trạng thái chờ xử lý (Loading indicator / Progress bar).
- [ ] Thiết kế các bảng màu chuẩn (Pico-8, Endesga 32, Game Boy).
- [ ] Viết tính năng tải ảnh tham chiếu (Image-to-Pixel).
- [ ] Canvas vẽ pixel tương tác trực tiếp (Pencil, Eraser, Fill).

---

## 🚧 In Progress (Đang làm)
- [ ] Chuẩn bị môi trường AI và khảo sát pipeline cho TASK-002.

---

## ✅ Done (Đã hoàn thành)
- [x] Khởi tạo cấu trúc thư mục tài liệu dự án (`docs/`, `planning/`, `README.md`).
- [x] Xác định phạm vi MVP và yêu cầu hệ thống cơ bản.
- [x] **TASK-001: Khởi tạo dự án Pixel Art AI Studio và xây dựng Frontend – Backend cơ bản:**
  - [x] Cấu trúc dự án phân tầng: `frontend/`, `backend/`, `tests/`, `docs/`, `planning/`.
  - [x] Backend FastAPI với các route `/api/health`, `/api/profiles`, `/api/generate`.
  - [x] Data schema với Pydantic và validation đầu vào chặt chẽ.
  - [x] Module `BaseGenerator` và `MockGenerator` độc lập, sẵn sàng chuyển đổi sang AI ở TASK-002.
  - [x] Giao diện người dùng HTML/CSS/JS thuần, hiển thị ảnh pixel sắc nét bằng CSS `image-rendering: pixelated`.
  - [x] Kết nối `fetch()` hai chiều, xử lý trạng thái chờ, thành công và báo lỗi.
  - [x] Bộ kiểm thử `tests/test_api.py` và End-to-End HTTP tests pass 100%.
  - [x] Cập nhật README hướng dẫn chi tiết cách chạy trên Windows.
