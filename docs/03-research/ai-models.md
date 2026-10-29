# AI Models Research

Nghiên cứu và đánh giá các giải pháp mô hình trí tuệ nhân tạo phục vụ bài toán sinh Pixel Art.

---

## 1. Các tiếp cận khả thi

### 1.1. Fine-tuned Diffusion Models (LoRA / Checkpoints)
- **Mô tả:** Sử dụng Stable Diffusion (1.5 hoặc XL) kết hợp các LoRA chuyên biệt về Pixel Art (ví dụ: *Pixel Art Diffusion*, *Retro Anime Pixel*).
- **Ưu điểm:** Khả năng hiểu prompt tự nhiên rất tốt, chất lượng chi tiết và phong phú.
- **Nhược điểm:** Cần hậu xử lý (downscaling + color quantization) để ép ảnh thành chuẩn lưới pixel và giới hạn bảng màu.

### 1.2. Direct Pixel Generation (Autoregressive / GANs / Custom Small Models)
- **Mô tả:** Mô hình chuyên biệt sinh ma trận pixel kích thước nhỏ trực tiếp (16x16, 32x32) như PixelCNN hoặc GANs huấn luyện trên dataset sprite.
- **Ưu điểm:** Nhẹ, sinh ảnh nhanh, giữ nguyên độ chuẩn xác pixel mà không cần downscale.
- **Nhược điểm:** Khó sinh vật thể phức tạp hoặc hiểu câu lệnh ngôn ngữ tự nhiên dài.

### 1.3. Hybrid Pipeline (Text-to-Image + Pixelization Algorithm)
- **Mô tả:**
  1. Sinh ảnh độ phân giải thông thường từ mô hình AI (hoặc lấy ảnh người dùng cung cấp).
  2. Áp dụng thuật toán K-means Color Quantization + Edge Detection + Grid Downsampling để tạo pixel art hoàn chỉnh.
- **Đánh giá:** Dễ triển khai, kiểm soát tốt số lượng màu và kích thước lưới pixel.

---

## 2. Tiêu chí lựa chọn cho dự án
- Thời gian sinh (Inference Speed).
- Chi phí tài nguyên (GPU VRAM / API Cost).
- Độ sắc nét của lưới pixel (Grid Consistency & No Blurring).
