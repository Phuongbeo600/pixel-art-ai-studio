# Functional Requirements

## 1. Introduction
Tài liệu đặc tả các yêu cầu chức năng (Functional Requirements) cho hệ thống **Pixel Art AI Studio**.

---

## 2. Core Functional Modules

### 2.1. AI Pixel Art Generation
- **FR-01 (Text-to-Pixel-Art):** Cho phép người dùng nhập câu lệnh (prompt) văn bản để tạo hình ảnh pixel art theo chủ đề, độ phân giải (16x16, 32x32, 64x64, 128x128) và bảng màu (color palette).
- **FR-02 (Image-to-Pixel-Art):** Cho phép tải lên hình ảnh thông thường và chuyển đổi (pixelize/quantize) sang phong cách pixel art.
- **FR-03 (Style & Palette Control):** Lựa chọn các bảng màu kinh điển (Game Boy, NES, Pico-8, v.v.) hoặc tùy chỉnh palette màu.

### 2.2. Interactive Pixel Editor (Canvas)
- **FR-04 (Drawing Tools):** Bút vẽ (Pencil), Tẩy (Eraser), Tô màu (Bucket Fill), Bút chọn màu (Color Picker).
- **FR-05 (Grid & Zoom):** Bật/tắt lưới pixel, phóng to/thu nhỏ canvas, hoàn tác/làm lại (Undo/Redo).
- **FR-06 (Layers):** Hỗ trợ tối thiểu 2-3 layers cơ bản (Background, Main, Foreground).

### 2.3. Export & Management
- **FR-07 (Export Formats):** Xuất định dạng PNG (với hệ số tỉ lệ scale 1x, 2x, 4x, 8x chống mờ), sprite sheet, hoặc GIF animation cơ bản.
- **FR-08 (Project Save/Load):** Lưu dự án và phiên làm việc để chỉnh sửa lại sau.
