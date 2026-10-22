# Suno Master Cheatsheet & Prompt Builder (v5 / v6) 🎵✨

Bộ công cụ tự động hóa sáng tác thơ vần điệu & xây dựng cấu trúc Prompt nhạc cho **Suno AI** (tối ưu toàn diện cho các phiên bản **v5, v5.5, v6, v6-wild, v6-mini** - đã lược bỏ các quy tắc cũ của v4.5).

---

## 🌟 Tính Năng Nổi Bật

1. **Chuyển hóa Ý Tưởng thành Thơ Liền Vần Tự Nhiên:**
   - Tiếp nhận văn bản thô, ý tưởng, hoặc lời trích dẫn audio/video.
   - Tự động sáng tác bài thơ tiếng Việt liền vần giữa các câu, ngắt nhịp mượt mà (Mở đầu $\rightarrow$ Chuyển tiếp $\rightarrow$ Điệp khúc hook $\rightarrow$ Đoạn hai $\rightarrow$ Cầu nối $\rightarrow$ Kết bài).
2. **Quy Tắc Vàng Thẻ Lệnh Suno (Metatags):**
   - **Tuyệt đối BỎ KHỎI bài hát thẻ `[Intro]`:** Tránh tình trạng Suno hát dính chữ "Intro" hoặc dạo nhạc quá dài làm loãng bài hát.
   - 100% thẻ lệnh đặt trong `[...]` sử dụng tiếng Anh chuẩn ngắn gọn (`[Verse]`, `[Chorus]`, `[Outro]`...).
   - Lớp bè/đồng ca đặt trong dấu `(...)` để kích hoạt hiệu ứng backing vocal tự nhiên.
   - Dấu gạch ngang (`-`) và dấu ba chấm (`...`) đặt có chủ đích để điều khiển nhả chữ, luyến láy và giữ nốt ngân dài (vibrato/hold note).
3. **Kiến Trúc Prompt V6 Chuẩn Studio:**
   - Xây dựng Style Prompt theo Producer Brief: `Identity -> Pulse -> Players -> Performance -> Arc -> Mix -> Constraints`.
   - Kết hợp độc đáo nhạc cụ truyền thống Việt Nam (Đàn Tranh, Sáo Trúc, Đàn Bầu) với các thể loại hiện đại (Pop Ballad, Lofi, Bolero, Vinahouse, Cinematic Sử Thi).
4. **Xuất Định Dạng Chuẩn 3 Code Block Riêng Biệt:**
   - **Code Block 1:** `STYLE PROMPT` (Dán vào ô "Style of Music" trên Suno).
   - **Code Block 2:** `LYRICS` (Dán vào ô "Lyrics" trên Suno, KHÔNG chứa `[Intro]`).
   - **Code Block 3:** `EXCLUDE STYLES` (Dán vào ô "Exclude Styles" trên Suno để lọc sạch tạp âm gắt).

---

## 🚀 Hướng Dẫn Cài Đặt & Sử Dụng

Dự án được xây dựng bằng **Python thuần (Standard Library)**, không yêu cầu cài đặt thêm bất kỳ thư viện pip nào!

### 1. Dùng Giao Diện Web Trực Quan (Web UI):

```bash
python -m suno_prompt_builder.web_app
```
Mở trình duyệt tại: **`http://localhost:7860`** để trải nghiệm giao diện Dark Mode với nút 1-click Copy to Clipboard.

---

### 2. Dùng Qua Dòng Lệnh (CLI):

```bash
# Xem danh sách thể loại hỗ trợ:
python -m suno_prompt_builder --list-genres

# Tạo prompt từ 1 câu ý tưởng:
python -m suno_prompt_builder "Nhớ về người mẹ hiền bên dòng sông mùa lũ" --genre viet_ballad

# Tạo prompt nhạc trẻ dân tộc điện tử:
python -m suno_prompt_builder "Khát vọng tuổi trẻ vươn ra biển lớn" --genre viet_pop_ethnic
```

---

### 3. Dùng Trong Code Python:

```python
from suno_prompt_builder.builder import SunoPromptBuilder

builder = SunoPromptBuilder(genre_key="viet_ballad")
res = builder.build_from_input("Nỗi nhớ quê hương và ánh mắt mẹ già")

print(res["plain_poem"])      # Bài thơ hoàn chỉnh
print(res["style_prompt"])    # Code block 1 (Style of Music)
print(res["lyrics_prompt"])   # Code block 2 (Lyrics - NO [Intro])
print(res["exclude_styles"])  # Code block 3 (Exclude Styles)
```

---

## 📚 Tài Liệu & Cẩm Nang Kèm Theo

Trong thư mục [`docs/`](docs/) và mã nguồn có đầy đủ các cẩm nang:
- **`SYSTEM_PROMPT_POETRY_SUNO.md`**: Master Prompt nạp vào ChatGPT/Claude/Custom GPT.
- **`docs/SUNO_V6_MASTER_CHEATSHEET.txt`**: Cẩm nang Suno V6 Master Guide (18 trang toàn diện).
- **`docs/SUNO_V5_CHEATSHEET.txt`**: Cẩm nang Suno V5/V5.5 God Mode (22 trang danh mục thẻ lệnh).

---

## ⚖️ License
Phát hành theo giấy phép **MIT**.
