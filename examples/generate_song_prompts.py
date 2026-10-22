"""
Example script demonstrating automated prompt generation for 4 distinct Vietnamese styles.
"""
import sys, os
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from suno_prompt_builder.builder import SunoPromptBuilder

def run_demo():
    demos = [
        ("viet_ballad", "Nỗi nhớ mẹ hiền nơi quê nghèo mùa mưa lũ"),
        ("viet_pop_ethnic", "Tuổi trẻ Việt Nam bay cao vươn ra thế giới cùng đàn tranh sáo trúc"),
        ("viet_bolero", "Chuyến đò miền Tây hoàng hôn tím ráng chiều"),
        ("viet_vinahouse", "Đêm nhạc quẩy cực sung cùng bạn bè cuối tuần")
    ]

    for genre, idea in demos:
        print(f"\n=======================================================")
        print(f"DEMO THỂ LOẠI: {genre.upper()} - Ý TƯỞNG: {idea}")
        print(f"=======================================================")
        builder = SunoPromptBuilder(genre_key=genre)
        res = builder.build_from_input(idea)

        print("\n[1. BÀI THƠ LIỀN VẦN]")
        print(res["plain_poem"])

        print("\n[2. CODE BLOCK 1: STYLE PROMPT]")
        print(res["style_prompt"])

        print("\n[3. CODE BLOCK 2: LYRICS (NO [Intro])]")
        print(res["lyrics_prompt"])

        print("\n[4. CODE BLOCK 3: EXCLUDE STYLES]")
        print(res["exclude_styles"])
        print("-" * 55)

if __name__ == "__main__":
    run_demo()
