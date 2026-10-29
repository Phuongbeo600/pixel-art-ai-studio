from typing import List, Literal, Optional
from pydantic import BaseModel, Field, field_validator


class HealthResponse(BaseModel):
    """Schema cho phản hồi kiểm tra sức khỏe của Backend."""
    status: str = "ok"
    message: str = "Pixel Art AI Studio Backend is running"
    version: str = "1.0.0"


class ArtProfile(BaseModel):
    """Schema biểu diễn cấu hình phong cách Pixel Art."""
    id: str
    name: str
    description: str
    default_palette: str
    supported_sizes: List[int] = [64, 128, 256]


class ProfilesResponse(BaseModel):
    """Schema danh sách các Art Profiles có sẵn."""
    profiles: List[ArtProfile]


class GenerationRequest(BaseModel):
    """Schema dữ liệu yêu cầu sinh Pixel Art từ Frontend."""
    prompt: str = Field(..., min_length=1, max_length=500, description="Mô tả tài nguyên cần tạo")
    profile_id: str = Field(default="medieval-pixel-art", description="ID cấu hình phong cách đồ họa")
    canvas_size: int = Field(default=64, description="Kích thước canvas: 64, 128, hoặc 256")

    @field_validator("prompt")
    @classmethod
    def validate_prompt(cls, v: str) -> str:
        clean = v.strip()
        if not clean:
            raise ValueError("Prompt không được để trống hoặc chỉ chứa khoảng trắng.")
        return clean

    @field_validator("canvas_size")
    @classmethod
    def validate_canvas_size(cls, v: int) -> int:
        allowed = (64, 128, 256)
        if v not in allowed:
            raise ValueError(f"Kích thước canvas không hợp lệ: {v}. Chỉ chấp nhận {allowed}.")
        return v


class GenerationMetadata(BaseModel):
    """Metadata bổ sung cho tác vụ sinh ảnh."""
    palette_used: str
    inference_time_ms: int
    note: str


class GenerationResponse(BaseModel):
    """Schema kết quả trả về sau khi sinh ảnh."""
    id: str
    status: Literal["success", "error"]
    prompt: str
    profile_id: str
    canvas_size: int
    image_url: str
    generator_type: Literal["mock", "ai"]
    created_at: str
    metadata: GenerationMetadata
