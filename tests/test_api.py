import sys
import unittest
from fastapi.testclient import TestClient
from backend.main import app


class TestPixelArtStudioAPI(unittest.TestCase):
    """Bộ kiểm thử cho các API của Pixel Art AI Studio."""

    def setUp(self):
        self.client = TestClient(app)

    def test_health_check(self):
        """Kiểm tra GET /api/health trả về status 200 và trạng thái 'ok'."""
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data.get("status"), "ok")
        self.assertIn("version", data)

    def test_get_profiles(self):
        """Kiểm tra GET /api/profiles trả về danh sách các profile gồm Medieval Pixel Art."""
        response = self.client.get("/api/profiles")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("profiles", data)
        self.assertGreaterEqual(len(data["profiles"]), 1)
        
        # Kiểm tra sự tồn tại của profile mặc định medieval-pixel-art
        medieval_profile = next((p for p in data["profiles"] if p["id"] == "medieval-pixel-art"), None)
        self.assertIsNotNone(medieval_profile, "Profile 'medieval-pixel-art' phải có trong danh sách.")
        self.assertEqual(medieval_profile["name"], "Medieval Pixel Art")

    def test_generate_success_64(self):
        """Kiểm tra POST /api/generate với dữ liệu hợp lệ (64x64)."""
        payload = {
            "prompt": "Retro knight with sword",
            "profile_id": "medieval-pixel-art",
            "canvas_size": 64,
        }
        response = self.client.post("/api/generate", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["generator_type"], "mock")
        self.assertEqual(data["canvas_size"], 64)
        self.assertEqual(data["image_url"], "/static/samples/sample_64.png")
        self.assertIn("metadata", data)

    def test_generate_success_128_and_256(self):
        """Kiểm tra sinh ảnh ở kích thước 128x128 và 256x256."""
        for size in (128, 256):
            payload = {
                "prompt": f"Pixel art asset test for size {size}",
                "profile_id": "medieval-pixel-art",
                "canvas_size": size,
            }
            response = self.client.post("/api/generate", json=payload)
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertEqual(data["canvas_size"], size)
            self.assertEqual(data["image_url"], f"/static/samples/sample_{size}.png")

    def test_generate_invalid_canvas_size(self):
        """Kiểm tra xử lý lỗi khi gửi kích thước canvas không hợp lệ (ví dụ: 100)."""
        payload = {
            "prompt": "Test invalid size",
            "profile_id": "medieval-pixel-art",
            "canvas_size": 100,
        }
        response = self.client.post("/api/generate", json=payload)
        self.assertEqual(response.status_code, 422, "Canvas size không thuộc [64, 128, 256] phải trả về 422 Unprocessable Entity")

    def test_generate_empty_prompt(self):
        """Kiểm tra xử lý lỗi khi prompt rỗng hoặc chỉ có khoảng trắng."""
        payload = {
            "prompt": "   ",
            "profile_id": "medieval-pixel-art",
            "canvas_size": 64,
        }
        response = self.client.post("/api/generate", json=payload)
        self.assertEqual(response.status_code, 422, "Prompt rỗng phải trả về 422 Unprocessable Entity")

    def test_generate_invalid_profile(self):
        """Kiểm tra xử lý lỗi khi profile_id không tồn tại."""
        payload = {
            "prompt": "Test invalid profile",
            "profile_id": "non_existent_profile",
            "canvas_size": 64,
        }
        response = self.client.post("/api/generate", json=payload)
        self.assertEqual(response.status_code, 400, "Profile không hợp lệ phải trả về 400 Bad Request")

    def test_static_sample_images_exist(self):
        """Kiểm tra tải được ảnh mẫu từ /static/samples/."""
        for size in (64, 128, 256):
            response = self.client.get(f"/static/samples/sample_{size}.png")
            self.assertEqual(response.status_code, 200, f"Ảnh mẫu sample_{size}.png phải truy cập được qua HTTP")
            self.assertEqual(response.headers.get("content-type"), "image/png")


if __name__ == "__main__":
    unittest.main()
