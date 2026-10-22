"""
Suno Master Prompt Builder
Integrates Poetry Engine and Genre Profiles to output exactly 3 formatted Code Blocks:
1. Plain text poem
2. Code Block 1: STYLE PROMPT (Style of Music box)
3. Code Block 2: LYRICS (Lyrics box - NO [Intro])
4. Code Block 3: EXCLUDE STYLES (Exclude Styles box)
Plus concise copy-paste guidance notes.
"""
from typing import Dict, Any, Optional
from .genres import GENRE_PROFILES
from .poetry_engine import PoetrySunoEngine

class SunoPromptBuilder:
    def __init__(self, genre_key: str = "viet_ballad"):
        self.genre_key = genre_key if genre_key in GENRE_PROFILES else "viet_ballad"
        self.genre_info = GENRE_PROFILES[self.genre_key]

    def build_from_input(self, input_text: str, custom_genre: Optional[str] = None) -> Dict[str, str]:
        """
        Takes raw input, creates seamless rhyming lyrics and complete Suno prompt.
        """
        if custom_genre and custom_genre in GENRE_PROFILES:
            self.genre_info = GENRE_PROFILES[custom_genre]

        poem_data = PoetrySunoEngine.ensure_rhyme_and_structure(input_text)
        
        # Plain text poem
        plain_poem_lines = []
        plain_poem_lines.append(f"=== {poem_data.get('title', 'Bài Thơ Hoàn Chỉnh')} ===")
        plain_poem_lines.append("[Mở đầu]")
        plain_poem_lines.extend(poem_data.get("verse_1", []))
        if poem_data.get("pre_chorus"):
            plain_poem_lines.append("\n[Chuyển tiếp]")
            plain_poem_lines.extend(poem_data.get("pre_chorus", []))
        plain_poem_lines.append("\n[Điệp khúc]")
        plain_poem_lines.extend(poem_data.get("chorus", []))
        if poem_data.get("verse_2"):
            plain_poem_lines.append("\n[Đoạn hai]")
            plain_poem_lines.extend(poem_data.get("verse_2", []))
        if poem_data.get("bridge"):
            plain_poem_lines.append("\n[Cầu nối]")
            plain_poem_lines.extend(poem_data.get("bridge", []))
        plain_poem_lines.append("\n[Kết bài]")
        plain_poem_lines.extend(poem_data.get("outro", []))
        plain_poem = "\n".join(plain_poem_lines)

        # Code Block 1: Style Prompt
        style_prompt = self.genre_info["style_prompt"]

        # Code Block 2: Lyrics (NO [Intro])
        lyrics_prompt = PoetrySunoEngine.build_suno_lyrics(
            poem_data,
            vocal_style="High Female Lead"
        )

        # Code Block 3: Exclude Styles
        exclude_styles = self.genre_info["exclude_styles"]

        # User Guidance Notes
        guidance = (
            "📌 HƯỚNG DẪN DÁN VÀO GIAO DIỆN SUNO AI (v5 / v6):\n"
            "1. Bật chế độ [Custom Mode] trên Suno.\n"
            "2. Dán nội dung Code Block 1 vào ô [Style of Music].\n"
            "3. Dán nội dung Code Block 2 vào ô [Lyrics] (Đã loại bỏ hoàn toàn [Intro], giữ nhịp ngân luyến láy chuẩn xác).\n"
            "4. Dán nội dung Code Block 3 vào ô [Exclude Styles] (Để loại bỏ tạp âm hú hét, trống gắt và giữ giọng trong trẻo).\n"
            "5. Chọn Model: Khuyên dùng [v6] để kiểm soát nhạc chuẩn xác nhất, hoặc [v6-wild] để khám phá phối khí bất ngờ."
        )

        return {
            "plain_poem": plain_poem,
            "style_prompt": style_prompt,
            "lyrics_prompt": lyrics_prompt,
            "exclude_styles": exclude_styles,
            "guidance": guidance
        }
