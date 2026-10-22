#!/usr/bin/env python3
"""
Suno Master Cheatsheet & Prompt Builder CLI
"""
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

import argparse
from suno_prompt_builder.builder import SunoPromptBuilder
from suno_prompt_builder.genres import GENRE_PROFILES

def main():
    parser = argparse.ArgumentParser(description="Suno AI Master Prompt Builder (v5/v6)")
    parser.add_argument("input", nargs="?", help="Văn bản, ý tưởng hoặc lời trích dẫn")
    parser.add_argument("-g", "--genre", default="viet_ballad", choices=list(GENRE_PROFILES.keys()), help="Thể loại nhạc Suno")
    parser.add_argument("--list-genres", action="store_true", help="Danh sách các thể loại nhạc hỗ trợ")

    args = parser.parse_args()

    if args.list_genres:
        print("\nDANH SÁCH THỂ LOẠI NHẠC SUNO V5/V6 ĐƯỢC THIẾT KẾ SẴN:")
        for k, v in GENRE_PROFILES.items():
            print(f"  • {k:<22} -> {v['name_vi']}")
        return

    text = args.input
    if not text:
        print("Nhập ý tưởng / văn bản bài hát (nhấn Enter rồi Ctrl+Z/Ctrl+D để hoàn tất):")
        try:
            text = sys.stdin.read().strip()
        except Exception:
            text = "Quê hương mùa nước nổi, tình mẹ bao la"

    if not text:
        text = "Nhớ về mẹ và quê hương thân yêu"

    builder = SunoPromptBuilder(genre_key=args.genre)
    res = builder.build_from_input(text)

    print("\n" + res["plain_poem"] + "\n")
    print("```text\n" + res["style_prompt"] + "\n```\n")
    print("```text\n" + res["lyrics_prompt"] + "\n```\n")
    print("```text\n" + res["exclude_styles"] + "\n```\n")
    print(res["guidance"] + "\n")

if __name__ == "__main__":
    main()
