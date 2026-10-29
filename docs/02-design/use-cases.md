# Use Cases

## Danh sách Use Cases

### UC-01: Tạo Pixel Art từ câu lệnh (Text-to-Pixel)
- **Actor:** Người dùng / Game Developer
- **Pre-condition:** Hệ thống sẵn sàng, mô hình AI đang hoạt động.
- **Main Flow:**
  1. Người dùng nhập câu mô tả (ví dụ: *"retro knight character with sword"*).
  2. Người dùng chọn kích thước canvas (32x32) và bộ màu (Pico-8).
  3. Người dùng nhấn nút **"Generate"**.
  4. Hệ thống xử lý qua AI model và trả về hình ảnh pixel art tương ứng.
  5. Người dùng xem ảnh trên preview panel.

---

### UC-02: Chỉnh sửa ảnh trên Pixel Canvas
- **Actor:** Pixel Artist / Người dùng
- **Pre-condition:** Ảnh pixel art đã được tải lên hoặc sinh ra từ AI.
- **Main Flow:**
  1. Người dùng chọn công cụ vẽ (Pencil hoặc Eraser).
  2. Người dùng chọn màu từ bảng màu hiện tại.
  3. Người dùng tương tác trực tiếp lên từng ô pixel trên canvas để chấm nét hoặc tẩy xóa.
  4. Người dùng sử dụng Undo/Redo nếu muốn hoàn tác thao tác.

---

### UC-03: Xuất tài nguyên (Export Asset)
- **Actor:** Người dùng
- **Pre-condition:** Người dùng hoàn thiện tác phẩm trên canvas hoặc preview.
- **Main Flow:**
  1. Người dùng nhấn **"Export"**.
  2. Người dùng chọn tỉ lệ phóng đại (ví dụ: 1x, 4x, 8x).
  3. Hệ thống áp dụng thuật toán Nearest Neighbor scaling để ảnh giữ nguyên độ sắc cạnh của pixel.
  4. Tệp tin PNG được tải về máy của người dùng.
