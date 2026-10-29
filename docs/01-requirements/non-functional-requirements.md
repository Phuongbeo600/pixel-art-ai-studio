# Non-Functional Requirements

## 1. Performance (Hiệu năng)
- **NFR-01 (Inference Time):** Thời gian sinh ảnh AI trung bình < 10 giây (trên GPU) hoặc < 25 giây (trên CPU / API bên thứ 3).
- **NFR-02 (Canvas Responsiveness):** Tốc độ phản hồi của công cụ vẽ canvas đạt 60 FPS, độ trễ khi vẽ pixel < 16ms.

## 2. Usability & UI/UX (Khả năng sử dụng)
- **NFR-03 (Intuitive Interface):** Giao diện thân thiện, dễ dùng cho cả người dùng mới và họa sĩ pixel chuyên nghiệp.
- **NFR-04 (Theme):** Hỗ trợ Dark Mode / Retro Gaming Aesthetic phù hợp với phong cách pixel art.

## 3. Reliability & Compatibility (Độ tin cậy & Tương thích)
- **NFR-05 (Browser/OS Support):** Hoạt động ổn định trên các trình duyệt hiện đại (Chrome, Edge, Firefox) hoặc hệ điều hành Windows/macOS.
- **NFR-06 (Data Integrity):** Tự động lưu bản nháp vào LocalStorage/IndexedDB tránh mất dữ liệu khi mất kết nối.
