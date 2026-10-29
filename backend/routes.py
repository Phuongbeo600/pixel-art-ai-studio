from typing import List
from fastapi import APIRouter, HTTPException, status
from backend.schemas import (
    HealthResponse,
    ProfilesResponse,
    ArtProfile,
    GenerationRequest,
    GenerationResponse,
)
from backend.services.base_generator import BaseGenerator
from backend.services.mock_generator import MockGenerator


router = APIRouter(prefix="/api", tags=["API"])

# Danh sách Art Profile có sẵn trong hệ thống
AVAILABLE_PROFILES: List[ArtProfile] = [
    ArtProfile(
        id="medieval-pixel-art",
        name="Medieval Pixel Art",
        description="Phong cách pixel art trung cổ cổ điển, phù hợp cho hiệp sĩ, vũ khí và lâu đài.",
        default_palette="pico-8-medieval",
        supported_sizes=[64, 128, 256],
    ),
    ArtProfile(
        id="cyberpunk-neon",
        name="Cyberpunk Neon",
        description="Phong cách viễn tưởng với gam màu neon tím, xanh lam phát sáng rực rỡ.",
        default_palette="neon-cyber-16",
        supported_sizes=[64, 128, 256],
    ),
    ArtProfile(
        id="retro-gameboy",
        name="Retro 4-Color GameBoy",
        description="Phong cách hoài niệm với 4 sắc độ xanh lục kinh điển của máy cầm tay GameBoy.",
        default_palette="gameboy-classic-4",
        supported_sizes=[64, 128, 256],
    ),
]

# Generator hiện tại: Trong TASK-001 dùng MockGenerator
# Ở TASK-002: Chỉ cần đổi thành `current_generator = AIGenerator()`
current_generator: BaseGenerator = MockGenerator()


def get_generator() -> BaseGenerator:
    """Hàm cung cấp instance của Generator hiện tại."""
    return current_generator


def set_generator(generator: BaseGenerator) -> None:
    """Cho phép hoán đổi Generator khi cần (ví dụ lúc test hoặc nâng cấp AI)."""
    global current_generator
    current_generator = generator


@router.get("/health", response_model=HealthResponse)
def health_check():
    """Kiểm tra tình trạng hoạt động của Backend."""
    return HealthResponse(
        status="ok",
        message="Pixel Art AI Studio Backend is running",
        version="1.0.0",
    )


@router.get("/profiles", response_model=ProfilesResponse)
def get_profiles():
    """Lấy danh sách các Art Profiles hỗ trợ."""
    return ProfilesResponse(profiles=AVAILABLE_PROFILES)


@router.post("/generate", response_model=GenerationResponse)
def generate_pixel_art(request: GenerationRequest):
    """
    Tiếp nhận yêu cầu tạo Pixel Art từ Frontend,
    kiểm tra tính hợp lệ và gọi Generator để tạo kết quả.
    """
    # Kiểm tra profile_id có tồn tại trong danh sách không
    valid_profile_ids = [p.id for p in AVAILABLE_PROFILES]
    if request.profile_id not in valid_profile_ids:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Profile '{request.profile_id}' không hợp lệ. Các profile được chấp nhận: {valid_profile_ids}",
        )

    try:
        generator = get_generator()
        result = generator.generate(request)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Lỗi trong quá trình sinh ảnh: {str(e)}",
        )
