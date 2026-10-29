import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.routes import router

# Khởi tạo ứng dụng FastAPI
app = FastAPI(
    title="Pixel Art AI Studio API",
    description="Backend API phục vụ tạo và quản lý tài nguyên Pixel Art",
    version="1.0.0",
)

# Cấu hình CORS để Frontend (dù chạy file:// hay server local khác) đều gọi được API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Đăng ký các API routes (/api/health, /api/profiles, /api/generate)
app.include_router(router)

# Đường dẫn thư mục tĩnh và frontend
BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
STATIC_DIR = BASE_DIR / "static"
FRONTEND_DIR = PROJECT_ROOT / "frontend"

# Mount thư mục static chứa ảnh mẫu (/static/samples/...)
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# Mount thư mục frontend để người dùng có thể mở thẳng http://127.0.0.1:8000
if FRONTEND_DIR.exists():
    app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")
