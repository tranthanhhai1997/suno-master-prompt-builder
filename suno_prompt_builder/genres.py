"""
Suno v5/v6 Curated Music Genre Profiles & Style Blueprints
Follows V6 Architecture: Identity -> Pulse -> Players -> Performance -> Arc -> Mix -> Constraints
"""
from typing import Dict, Any

GENRE_PROFILES: Dict[str, Dict[str, Any]] = {
    "viet_ballad": {
        "name_vi": "Ballad Việt Điện Ảnh (Trữ tình, sâu lắng)",
        "tempo": "74 BPM, 6/8, slow swaying groove",
        "style_prompt": (
            "Vietnamese cinematic pop ballad, 74 BPM, 6/8, melancholic and heartfelt\n"
            "High emotional female lead, airy intimate verses, controlled powerful belting in choruses\n"
            "Warm grand piano carries harmony, sparse đàn tranh answering motifs, soft cello swelling in lifts\n"
            "Sparse opening, gradual build, wide anthemic final chorus, close-mic vocal, polished cinematic mix"
        ),
        "exclude_styles": "rock, heavy metal, screaming, shouting, distorted vocals, aggressive drums, harsh EDM drop, fast tempo",
        "recommended_voice": "female lead, soprano, airy and breathy"
    },
    "viet_pop_ethnic": {
        "name_vi": "Pop Việt Hiện Đại Kết Hợp Dân Tộc (Đàn Tranh & Sáo Trúc)",
        "tempo": "98 BPM, 4/4, modern groove",
        "style_prompt": (
            "Vietnamese modern ethnic pop, 98 BPM, uplifting and nostalgic\n"
            "Bright expressive female lead, occasional warm male backing accents\n"
            "Đàn tranh and bamboo flute answering phrases, tight modern synth bass, organic crisp percussion\n"
            "Intimate verse, rising pre-chorus tension, explosive hook-driven chorus, wide radio-ready mix"
        ),
        "exclude_styles": "rock, heavy metal, screaming, shouting, distorted vocals, aggressive drums, dark ambient, chaotic noise",
        "recommended_voice": "bright female lead, energetic and clear"
    },
    "viet_bolero": {
        "name_vi": "Bolero Miền Tây / Trữ Tình Quê Hương",
        "tempo": "72 BPM, 4/4, gentle swaying bolero rhythm",
        "style_prompt": (
            "Vietnamese Mekong bolero, 72 BPM, nostalgic and bittersweet\n"
            "Warm female lead with natural conversational phrasing and sweet vibrato\n"
            "Nylon-string acoustic guitar, expressive accordion, upright acoustic bass, brushed percussion\n"
            "Gentle sway, memorable melodic hook, intimate room sound, warm organic acoustic mix"
        ),
        "exclude_styles": "rock, heavy metal, screaming, shouting, distorted vocals, aggressive drums, EDM, electronic synth, autotune",
        "recommended_voice": "warm female alto, sweet vibrato, traditional phrasing"
    },
    "viet_vinahouse": {
        "name_vi": "Vinahouse / Dance-Pop Việt Remix (Sôi động, bắt tai)",
        "tempo": "128 BPM, 4/4, four-on-the-floor club groove",
        "style_prompt": (
            "Vietnamese dance-pop / modern vinahouse, 128 BPM, energetic and celebratory\n"
            "Bright punchy female lead vocal, infectious repetitive vocal hook\n"
            "Punchy four-on-the-floor kick, rolling bounce bass, bright pluck synth lead, ethnic flute drop hook\n"
            "Tension riser pre-drop, explosive main drop, high-energy festival mix, tight sub bass"
        ),
        "exclude_styles": "rock, heavy metal, screaming, acoustic slow ballad, sad mood, dark gloomy, distorted vocals",
        "recommended_voice": "bright clear female vocals, punchy delivery"
    },
    "viet_cinematic_epic": {
        "name_vi": "Sử Thi Hào Hùng / Nhạc Phim Điện Ảnh (Tráng lệ, thiêng liêng)",
        "tempo": "82 BPM, 4/4, majestic orchestral pulse",
        "style_prompt": (
            "Vietnamese cinematic orchestral epic, 82 BPM, heroic and breathtaking\n"
            "Powerful soaring female lead with full choir harmonies and thunderous backing\n"
            "Taiko drums, bronze gong, traditional trống đồng pulse, sweeping cinematic strings, bamboo flute solo\n"
            "Slow solemn build into colossal climactic finale, wide stereo soundstage, Hollywood master mix"
        ),
        "exclude_styles": "rock, heavy metal, screaming, shouting, distorted vocals, aggressive drums, lo-fi, casual pop, flat production",
        "recommended_voice": "soaring female soprano, powerful operatic resonance, choir backing"
    },
    "viet_lofi_acoustic": {
        "name_vi": "Acoustic / Lofi Chill Việt (Mộc mạc, bình yên)",
        "tempo": "78 BPM, 4/4, relaxed laid-back pocket",
        "style_prompt": (
            "Vietnamese intimate acoustic chill, 78 BPM, peaceful and nostalgic\n"
            "Close-mic breathy female lead, vulnerable and soothing vocal delivery\n"
            "Fingerpicked acoustic guitar, subtle rhodes piano, soft upright bass, warm tape flutter ambience\n"
            "Gentle natural progression, cozy room reverb, warm vintage analog master"
        ),
        "exclude_styles": "rock, heavy metal, screaming, shouting, distorted vocals, aggressive drums, loud EDM, harsh synths, bombastic choir",
        "recommended_voice": "intimate breathy female vocal, close-mic, warm whisper"
    }
}
