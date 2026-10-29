# MVP Scope (Phạm vi sản phẩm khả thi tối thiểu)

## 🎯 Mục tiêu MVP
Xây dựng một phiên bản thử nghiệm có thể sinh ảnh pixel art từ văn bản, hỗ trợ chỉnh sửa trực tiếp trên canvas pixel đơn giản và xuất ảnh chuẩn pixel không vỡ nét.

---

## ✅ In-Scope (Thuộc phạm vi MVP)
1. **Text-to-Pixel-Art:** Sinh ảnh pixel kích thước 32x32 và 64x64 từ text prompt.
2. **Canvas Editor cơ bản:**
   - Bút vẽ (Pen), Tẩy (Eraser), Chọn màu (Color Picker).
   - Bật/tắt lưới pixel (Grid toggle).
   - Undo / Redo (tối thiểu 10 bước).
3. **Palette Presets:** Cung cấp sẵn một số bảng màu phổ biến (Pico-8, Game Boy, v.v.).
4. **Export:** Xuất ảnh PNG tỉ lệ 1x và scale-up 4x (Nearest Neighbor sampling).

---

## ❌ Out-of-Scope (Dành cho các phiên bản tiếp theo)
- Sinh Sprite Sheet chuyển động (animation walk/attack cycle).
- Đăng nhập tài khoản / Lưu trữ đám mây.
- Hỗ trợ đa lớp (Multi-layer phức tạp).
- Huấn luyện fine-tune mô hình AI trực tiếp trên giao diện người dùng.
