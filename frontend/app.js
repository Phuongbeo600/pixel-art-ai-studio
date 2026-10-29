/**
 * Pixel Art AI Studio - Frontend Controller (JavaScript thuần)
 * Phục vụ TASK-001: Kết nối Frontend <-> FastAPI Backend
 */

// Xác định API Base URL linh hoạt:
// Nếu mở file trực tiếp qua file:// hoặc Live Server khác port, trỏ về http://127.0.0.1:8000
const API_BASE = (window.location.protocol === "file:" || window.location.port !== "8000")
  ? "http://127.0.0.1:8000"
  : window.location.origin;

// Elements tham chiếu
const elBackendDot = document.getElementById("backend-status-dot");
const elBackendText = document.getElementById("backend-status-text");

const elPrompt = document.getElementById("prompt-input");
const elProfileSelect = document.getElementById("profile-select");
const elProfileDesc = document.getElementById("profile-desc");
const elGenerateBtn = document.getElementById("generate-btn");

const elStatusBanner = document.getElementById("status-banner");
const elStatusIcon = document.getElementById("status-icon");
const elStatusMsg = document.getElementById("status-message");

const elPreviewImg = document.getElementById("preview-image");
const elInfoSize = document.getElementById("info-size-tag");
const elInfoPalette = document.getElementById("info-palette-tag");

const elMetaId = document.getElementById("meta-id");
const elMetaTime = document.getElementById("meta-time");
const elMetaGenerator = document.getElementById("meta-generator");
const elMetaCreated = document.getElementById("meta-created");

const elDownloadLink = document.getElementById("download-link");
const elViewRawLink = document.getElementById("view-raw-link");

// Cache danh sách profiles
let cachedProfiles = [];

/**
 * 1. Kiểm tra tình trạng kết nối của Backend qua GET /api/health
 */
async function checkBackendHealth() {
  elBackendDot.className = "status-dot dot-checking";
  elBackendText.textContent = "Đang kiểm tra kết nối...";

  try {
    const response = await fetch(`${API_BASE}/api/health`, { method: "GET" });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();

    elBackendDot.className = "status-dot dot-online";
    elBackendText.textContent = `Backend Online (v${data.version || "1.0.0"})`;
    return true;
  } catch (err) {
    elBackendDot.className = "status-dot dot-offline";
    elBackendText.textContent = "Backend Offline (chưa chạy server)";
    console.warn("Backend health check failed:", err.message);
    return false;
  }
}

/**
 * 2. Tải danh sách Art Profiles từ GET /api/profiles
 */
async function loadArtProfiles() {
  try {
    const response = await fetch(`${API_BASE}/api/profiles`, { method: "GET" });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();

    cachedProfiles = data.profiles || [];
    renderProfileSelect(cachedProfiles);
  } catch (err) {
    console.error("Không thể tải danh sách profiles:", err);
    // Fallback nếu Backend chưa mở kịp
    elProfileSelect.innerHTML = `
      <option value="medieval-pixel-art" selected>Medieval Pixel Art (Default)</option>
      <option value="cyberpunk-neon">Cyberpunk Neon</option>
      <option value="retro-gameboy">Retro 4-Color GameBoy</option>
    `;
    updateProfileDescription("medieval-pixel-art");
  }
}

/**
 * Hiển thị danh sách profile vào thẻ <select>
 */
function renderProfileSelect(profiles) {
  elProfileSelect.innerHTML = "";

  profiles.forEach(profile => {
    const opt = document.createElement("option");
    opt.value = profile.id;
    opt.textContent = `${profile.name} (${profile.default_palette})`;
    if (profile.id === "medieval-pixel-art") {
      opt.selected = true; // Cấu hình mặc định theo yêu cầu TASK-001
    }
    elProfileSelect.appendChild(opt);
  });

  updateProfileDescription(elProfileSelect.value);
}

/**
 * Cập nhật dòng mô tả của profile đã chọn
 */
function updateProfileDescription(selectedId) {
  const profile = cachedProfiles.find(p => p.id === selectedId);
  if (profile) {
    elProfileDesc.textContent = `${profile.description} (Kích thước: ${profile.supported_sizes.join(", ")}px)`;
  } else {
    elProfileDesc.textContent = "Phong cách pixel art trung cổ cổ điển, phù hợp cho hiệp sĩ, vũ khí và lâu đài.";
  }
}

/**
 * Cập nhật giao diện thanh trạng thái
 */
function setStatus(type, message) {
  elStatusBanner.className = `status-banner status-${type}`;
  if (type === "loading") {
    elStatusIcon.textContent = "⏳";
  } else if (type === "success") {
    elStatusIcon.textContent = "✅";
  } else if (type === "error") {
    elStatusIcon.textContent = "❌";
  } else {
    elStatusIcon.textContent = "💤";
  }
  elStatusMsg.textContent = message;
}

/**
 * 3. Gửi yêu cầu sinh ảnh qua POST /api/generate
 */
async function handleGenerate() {
  const prompt = elPrompt.value.trim();
  const profileId = elProfileSelect.value;
  const sizeInput = document.querySelector('input[name="canvas-size"]:checked');
  const canvasSize = sizeInput ? parseInt(sizeInput.value, 10) : 64;

  // Validation cơ bản phía client
  if (!prompt) {
    setStatus("error", "Vui lòng nhập mô tả (prompt) trước khi tạo ảnh!");
    elPrompt.focus();
    return;
  }

  // Khóa nút bấm và hiển thị trạng thái đang xử lý
  elGenerateBtn.disabled = true;
  elGenerateBtn.querySelector(".btn-text").textContent = "Đang xử lý...";
  setStatus("loading", `Đang gửi yêu cầu sinh ảnh kích thước ${canvasSize}x${canvasSize} đến Backend...`);

  try {
    const payload = {
      prompt: prompt,
      profile_id: profileId,
      canvas_size: canvasSize
    };

    const response = await fetch(`${API_BASE}/api/generate`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    const data = await response.json();

    if (!response.ok) {
      // Bắt lỗi validation (422) hoặc bad request (400)
      const errorMsg = data.detail
        ? (Array.isArray(data.detail) ? data.detail.map(d => d.msg).join(", ") : data.detail)
        : `Lỗi máy chủ HTTP ${response.status}`;
      throw new Error(errorMsg);
    }

    // Hiển thị kết quả thành công
    renderGenerationResult(data);
    setStatus("success", `Sinh ảnh thành công! [${data.generator_type.toUpperCase()} GENERATOR] Thời gian: ${data.metadata.inference_time_ms}ms`);

  } catch (err) {
    console.error("Lỗi khi sinh ảnh:", err);
    setStatus("error", `Không thể hoàn thành: ${err.message}`);
  } finally {
    // Phục hồi nút bấm
    elGenerateBtn.disabled = false;
    elGenerateBtn.querySelector(".btn-text").textContent = "Tạo Pixel Art (Mock)";
  }
}

/**
 * 4. Hiển thị kết quả sinh ảnh lên Viewport và Metadata Card
 */
function renderGenerationResult(data) {
  // Ảnh mẫu
  const fullImageUrl = data.image_url.startsWith("http")
    ? data.image_url
    : `${API_BASE}${data.image_url}`;

  elPreviewImg.src = fullImageUrl;
  elPreviewImg.alt = data.prompt;

  // Info tags
  elInfoSize.textContent = `Kích thước: ${data.canvas_size} × ${data.canvas_size} px`;
  elInfoPalette.textContent = `Palette: ${data.metadata.palette_used}`;

  // Metadata Card
  elMetaId.textContent = data.id;
  elMetaTime.textContent = `${data.metadata.inference_time_ms} ms`;
  elMetaGenerator.textContent = data.generator_type;
  elMetaCreated.textContent = new Date(data.created_at).toLocaleTimeString();

  // Links
  elDownloadLink.href = fullImageUrl;
  elDownloadLink.download = `pixel_${data.canvas_size}x${data.canvas_size}_${data.id}.png`;
  elViewRawLink.href = fullImageUrl;
}

/**
 * Gán sự kiện khi trang đã tải xong
 */
document.addEventListener("DOMContentLoaded", () => {
  // 1. Kiểm tra kết nối Backend và tải danh sách profiles
  checkBackendHealth();
  loadArtProfiles();

  // 2. Sự kiện thay đổi profile select
  elProfileSelect.addEventListener("change", (e) => {
    updateProfileDescription(e.target.value);
  });

  // 3. Sự kiện bấm nút Tạo Pixel Art
  elGenerateBtn.addEventListener("click", handleGenerate);

  // 4. Cho phép nhấn Enter + Ctrl trong textarea để tạo nhanh
  elPrompt.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) {
      handleGenerate();
    }
  });

  // 5. Gợi ý prompt mẫu khi bấm chip
  document.querySelectorAll(".btn-chip").forEach(chip => {
    chip.addEventListener("click", () => {
      elPrompt.value = chip.getAttribute("data-prompt");
      elPrompt.focus();
    });
  });
});
