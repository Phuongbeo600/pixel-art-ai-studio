# 👾 Pixel Art AI Studio

Nền tảng hỗ trợ nhà phát triển game indie tạo, tinh chỉnh và chuẩn hóa tài nguyên đồ họa **Pixel Art** chuẩn xác bằng AI.

---

## 📌 1. Giới thiệu dự án

Dự án được xây dựng với kiến trúc tối giản, phân tầng rõ ràng giữa **Frontend (HTML/CSS/JS thuần)** và **Backend (FastAPI)**, ưu tiên tính dễ hiểu, dễ mở rộng cho sinh viên năm 2 và sẵn sàng tích hợp các mô hình AI sinh ảnh thực tế (Diffusion, LoRA, GANs) ở các giai đoạn tiếp theo.

### 🎯 Trạng thái hiện tại: TASK-001 (Hoàn thành)
- ✅ Đã dựng khung ứng dụng Frontend - Backend hoàn chỉnh.
- ✅ API RESTful kiểm tra sức khỏe (`/api/health`), danh sách cấu hình phong cách (`/api/profiles`), và sinh ảnh (`/api/generate`).
- ✅ Kiến trúc Generator module hóa theo mô hình OOP (`BaseGenerator` -> `MockGenerator`), phân tách rạch ròi giữa Mock và AI thực tế.
- ✅ Giao diện tối ưu hiển thị pixel art với CSS `image-rendering: pixelated`, bảng mã màu, kích thước (64×64, 128×128, 256×256) và theo dõi trạng thái xử lý thời gian thực.
- ✅ Bộ kiểm thử tự động (Unit Test & End-to-End Test) đạt 100% pass.

---

## 📂 2. Cấu trúc thư mục dự án

```text
pixel-art-ai-studio/
│
├── README.md                     # Hướng dẫn chi tiết cài đặt và sử dụng
├── requirements.txt              # Danh sách thư viện Python cần thiết
├── .gitignore                    # Bỏ qua venv, cache Python và file hệ thống
│
├── backend/                      # Mã nguồn Backend FastAPI
│   ├── __init__.py
│   ├── main.py                   # Điểm khởi động FastAPI app, CORS, mount static
│   ├── schemas.py                # Pydantic models (Request, Response, Validation)
│   ├── routes.py                 # Định nghĩa các endpoint API (/api/...)
│   │
│   ├── services/                 # Tầng logic xử lý sinh ảnh (Generator Service)
│   │   ├── __init__.py
│   │   ├── base_generator.py     # Lớp trừu tượng BaseGenerator (OOP Interface)
│   │   └── mock_generator.py     # Mock Generator trả dữ liệu giả lập & ảnh mẫu
│   │
│   └── static/                   # Tài nguyên tĩnh
│       └── samples/              # Ảnh PNG pixel art mẫu (64x64, 128x128, 256x256)
│
├── frontend/                     # Mã nguồn Frontend (Không dùng framework phức tạp)
│   ├── index.html                # Giao diện chính (Prompt, Profile, Canvas size, Preview)
│   ├── style.css                 # Bố cục studio retro-dark, hỗ trợ hiển thị sắc nét pixel
│   └── app.js                    # Logic điều khiển, gọi fetch() API, render kết quả
│
├── tests/                        # Kiểm thử tự động
│   └── test_api.py               # Unit test kiểm tra đầy đủ các endpoint API
│
├── docs/                         # Tài liệu phân tích & thiết kế
│   ├── 01-requirements/          # Yêu cầu chức năng, phi chức năng, phạm vi MVP
│   ├── 02-design/                # User Flow, Use Cases, Wireframes
│   ├── 03-research/              # Nghiên cứu mô hình AI Pixel Art
│   └── 04-testing/               # Kế hoạch kiểm thử
│
└── planning/                     # Kế hoạch phát triển
    ├── roadmap.md                # Lộ trình 4 giai đoạn
    └── backlog.md                # Bảng theo dõi đầu việc (Tasks)
```

---

## 💻 3. Hướng dẫn cài đặt và chạy trên Windows

### Yêu cầu môi trường
- Hệ điều hành: **Windows 10 / 11**
- **Python**: Phiên bản 3.10 trở lên (đã có `pip`)
- Trình duyệt web hiện đại: Chrome, Edge hoặc Firefox.

---

### Bước 1: Mở terminal tại thư mục dự án
Mở **PowerShell** hoặc **Command Prompt (cmd)** và di chuyển vào thư mục dự án:
```powershell
cd "pixel-art-ai-studio"
```

### Bước 2: Tạo và kích hoạt môi trường ảo (venv)
```powershell
# Tạo môi trường ảo tên là venv
python -m venv venv

# Kích hoạt venv trên Windows PowerShell:
.\venv\Scripts\Activate.ps1

# (Nếu gặp lỗi Execution Policy trên PowerShell, chạy lệnh sau rồi kích hoạt lại):
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Hoặc nếu dùng Command Prompt thông thường:
# .\venv\Scripts\activate.bat
```

### Bước 3: Cài đặt các thư viện cần thiết
```powershell
pip install -r requirements.txt
```

### Bước 4: Khởi chạy Backend FastAPI
```powershell
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

Khi chạy thành công, terminal sẽ thông báo:
```text
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [...]
```

### Bước 5: Truy cập ứng dụng
Mở trình duyệt web và truy cập địa chỉ:
- 🌐 **Giao diện người dùng (Frontend):** [http://127.0.0.1:8000](http://127.0.0.1:8000)
- 📖 **Tài liệu Swagger API tự động:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- 🩺 **Kiểm tra API Health:** [http://127.0.0.1:8000/api/health](http://127.0.0.1:8000/api/health)

*(Lưu ý: Bạn cũng có thể mở trực tiếp file `frontend/index.html` bằng trình duyệt mà không cần tắt Backend; code JavaScript đã cấu hình sẵn tự động kết nối qua `http://127.0.0.1:8000`)*.

---

## 🧪 4. Hướng dẫn chạy kiểm thử (Testing)

Dự án đi kèm bộ kiểm thử tự động sử dụng `unittest` của Python:

```powershell
# Chạy toàn bộ test cases API
python -m unittest tests/test_api.py
```

Kết quả hiển thị:
```text
........
----------------------------------------------------------------------
Ran 8 tests in 0.4s

OK
```

Các ca kiểm thử bao gồm:
1. `test_health_check`: Đảm bảo backend trả về mã 200 và `"status": "ok"`.
2. `test_get_profiles`: Đảm bảo danh sách profile có chứa `"medieval-pixel-art"`.
3. `test_generate_success_64`: Đảm bảo tạo asset 64x64 trả về đúng metadata và ảnh `/static/samples/sample_64.png`.
4. `test_generate_success_128_and_256`: Kiểm tra tạo ảnh ở kích thước 128 và 256.
5. `test_generate_invalid_canvas_size`: Kiểm tra dữ liệu đầu vào kích thước sai (bị chặn với mã 422).
6. `test_generate_empty_prompt`: Kiểm tra prompt rỗng hoặc chỉ có khoảng trắng (bị chặn với mã 422).
7. `test_generate_invalid_profile`: Kiểm tra profile không tồn tại (bị chặn với mã 400).
8. `test_static_sample_images_exist`: Đảm bảo các file ảnh mẫu được phân phối chính xác qua HTTP tĩnh.

---

## 🏗️ 5. Thiết kế kiến trúc chuyển giao cho TASK-002

Trong `backend/services/base_generator.py`, hệ thống định nghĩa lớp cơ sở:

```python
from abc import ABC, abstractmethod
from backend.schemas import GenerationRequest, GenerationResponse

class BaseGenerator(ABC):
    @property
    @abstractmethod
    def generator_type(self) -> str:
        pass

    @abstractmethod
    def generate(self, request: GenerationRequest) -> GenerationResponse:
        pass
```

### Cách thức tích hợp AI Generator trong TASK-002:
1. Tạo file mới `backend/services/ai_generator.py` kế thừa từ `BaseGenerator`.
2. Viết logic gọi mô hình AI (qua local pipeline PyTorch hoặc API endpoint của AI Model).
3. Trong `backend/routes.py`, chỉ cần thay đổi 1 dòng duy nhất:
   ```python
   # Từ:
   # current_generator: BaseGenerator = MockGenerator()
   # Thành:
   current_generator: BaseGenerator = AIGenerator()
   ```
Toàn bộ Frontend, API routes, và Validation Pydantic giữ nguyên vẹn mà không cần sửa đổi.

---

## 📝 6. Ghi chú kỹ thuật (Technical Notes for TASK-002)

1. **Thời gian phản hồi AI (Inference Latency):**
   Mô hình AI thật thường mất từ 3s - 15s để sinh ảnh. Cần thiết kế thanh tiến trình (progress bar) hoặc chuyển sang xử lý bất đồng bộ (Polling / WebSocket / Server-Sent Events) nếu thời gian vượt quá 10 giây.
2. **Hậu xử lý lưới Pixel (Pixel Grid Quantization):**
   Mô hình diffusion thông thường hay sinh ảnh mượt (smooth edges). Để thành pixel art chuẩn cho game indie, TASK-002 cần tích hợp thuật toán Downscaling (Nearest Neighbor) và giới hạn bảng màu (Color Quantization) theo Palette của Art Profile.
3. **Yêu cầu phần cứng máy tính local:**
   Nếu chạy mô hình AI trực tiếp trên máy cục bộ (Local Model), cần tối thiểu 6GB - 8GB VRAM GPU NVIDIA. Đối với máy tính cấu hình sinh viên không có GPU rời, nên chuẩn bị giải pháp kết nối API từ xa (Hugging Face Inference API hoặc RunPod).
4. **Quản lý file sinh ra:**
   Khi sinh ảnh thật, cần cơ chế đặt tên theo UUID và lưu trữ trong thư mục `backend/static/generated/` kèm cơ chế dọn dẹp file tạm (cleanup job) để tránh đầy ổ đĩa.
