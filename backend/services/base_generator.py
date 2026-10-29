from abc import ABC, abstractmethod
from backend.schemas import GenerationRequest, GenerationResponse


class BaseGenerator(ABC):
    """
    Lớp trừu tượng (Abstract Base Class) định nghĩa giao diện chung
    cho tất cả các Generator trong Pixel Art AI Studio.
    
    Trong TASK-001: Sử dụng MockGenerator kế thừa từ BaseGenerator.
    Trong TASK-002: Khi tích hợp mô hình AI thực tế (Diffusion, LoRA, v.v.),
    chỉ cần tạo AIGenerator kế thừa BaseGenerator và implement hàm `generate`.
    Giao diện Backend (routes) và Frontend sẽ không bị ảnh hưởng.
    """

    @property
    @abstractmethod
    def generator_type(self) -> str:
        """Loại generator: 'mock' hoặc 'ai'."""
        pass

    @abstractmethod
    def generate(self, request: GenerationRequest) -> GenerationResponse:
        """
        Thực hiện sinh pixel art từ request.
        
        Args:
            request: GenerationRequest chứa prompt, profile_id, canvas_size.
            
        Returns:
            GenerationResponse chứa metadata, url ảnh kết quả và trạng thái.
        """
        pass
