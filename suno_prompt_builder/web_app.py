"""
Suno Master Prompt Builder - Zero-Dependency Local Web Interface
Run: python -m suno_prompt_builder.web_app
Opens in browser at: http://localhost:7860
"""
import json
import http.server
import socketserver
import urllib.parse
from suno_prompt_builder.builder import SunoPromptBuilder
from suno_prompt_builder.genres import GENRE_PROFILES

PORT = 7860

HTML_PAGE = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Suno AI Master Prompt Builder (v5/v6)</title>
    <style>
        :root {
            --bg: #0b0f19;
            --panel: #131b2e;
            --panel-border: #1e293b;
            --accent: #38bdf8;
            --accent-glow: rgba(56, 189, 248, 0.25);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --code-bg: #070a13;
            --btn-green: #10b981;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        body { background: var(--bg); color: var(--text-main); padding: 30px 20px; line-height: 1.6; }
        .container { max-width: 960px; margin: 0 auto; }
        header { text-align: center; margin-bottom: 30px; }
        h1 { font-size: 28px; color: #fff; margin-bottom: 8px; }
        h1 span { color: var(--accent); }
        .tagline { color: var(--text-muted); font-size: 15px; }
        .panel { background: var(--panel); border: 1px solid var(--panel-border); border-radius: 12px; padding: 24px; margin-bottom: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.4); }
        label { display: block; font-weight: 600; margin-bottom: 8px; color: var(--text-main); font-size: 14px; }
        textarea { width: 100%; min-height: 120px; background: var(--code-bg); border: 1px solid var(--panel-border); border-radius: 8px; color: #fff; padding: 14px; font-size: 15px; resize: vertical; outline: none; transition: border 0.2s; }
        textarea:focus { border-color: var(--accent); box-shadow: 0 0 0 2px var(--accent-glow); }
        .controls { display: flex; gap: 16px; margin-top: 16px; align-items: center; flex-wrap: wrap; }
        select { flex: 1; min-width: 260px; background: var(--code-bg); border: 1px solid var(--panel-border); border-radius: 8px; color: #fff; padding: 12px 14px; font-size: 14px; outline: none; }
        button.generate-btn { background: linear-gradient(135deg, #0284c7, #38bdf8); color: #000; font-weight: 700; border: none; padding: 12px 28px; border-radius: 8px; cursor: pointer; transition: transform 0.1s, opacity 0.2s; font-size: 15px; }
        button.generate-btn:hover { opacity: 0.95; transform: scale(1.02); }
        .output-section { margin-top: 24px; display: none; }
        .block-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; margin-top: 20px; }
        .block-title { font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: var(--accent); }
        .copy-btn { background: rgba(56, 189, 248, 0.15); border: 1px solid var(--accent); color: var(--accent); padding: 5px 12px; border-radius: 6px; font-size: 12px; cursor: pointer; font-weight: 600; }
        .copy-btn:hover { background: var(--accent); color: #000; }
        pre { background: var(--code-bg); border: 1px solid var(--panel-border); border-radius: 8px; padding: 16px; color: #e2e8f0; font-family: "Cascadia Code", Consolas, monospace; font-size: 14px; white-space: pre-wrap; word-break: break-word; overflow-x: auto; }
        .guidance-box { background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 16px; color: #a7f3d0; font-size: 14px; margin-top: 24px; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Suno AI <span>Master Prompt Builder</span> (v5 / v6) 🎵</h1>
            <p class="tagline">Biến bất kỳ văn bản, ý tưởng hoặc lời trích dẫn nào thành Thơ Liền Vần & Cấu Trúc Prompt Suno Chuẩn Studio</p>
        </header>

        <div class="panel">
            <label for="rawInput">Nhập ý tưởng, chủ đề hoặc văn bản thô:</label>
            <textarea id="rawInput" placeholder="Ví dụ: Viết bài hát về ký ức tuổi thơ ở làng quê, có tiếng sáo diều, dòng sông và tình mẹ bao la..."></textarea>
            
            <div class="controls">
                <select id="genreSelect">
                    <option value="viet_ballad">Ballad Việt Điện Ảnh (Trữ tình, sâu lắng)</option>
                    <option value="viet_pop_ethnic">Pop Việt Hiện Đại + Đàn Tranh & Sáo Trúc</option>
                    <option value="viet_bolero">Bolero Miền Tây / Trữ Tình Quê Hương</option>
                    <option value="viet_vinahouse">Vinahouse / Dance-Pop Việt Remix</option>
                    <option value="viet_cinematic_epic">Sử Thi Hào Hùng / Nhạc Phim Điện Ảnh</option>
                    <option value="viet_lofi_acoustic">Acoustic / Lofi Chill Việt (Mộc mạc)</option>
                </select>
                <button class="generate-btn" onclick="buildPrompts()">Tạo Prompt Suno Chuẩn ✨</button>
            </div>

            <div id="outputArea" class="output-section">
                <div class="block-header">
                    <span class="block-title">📖 Bài Thơ Liền Vần Hoàn Chỉnh</span>
                    <button class="copy-btn" onclick="copyText('plainPoemPre')">Sao chép</button>
                </div>
                <pre id="plainPoemPre"></pre>

                <div class="block-header">
                    <span class="block-title">Code Block 1: STYLE PROMPT (Dán vào "Style of Music")</span>
                    <button class="copy-btn" onclick="copyText('stylePromptPre')">Sao chép</button>
                </div>
                <pre id="stylePromptPre"></pre>

                <div class="block-header">
                    <span class="block-title">Code Block 2: LYRICS (Dán vào "Lyrics" - KHÔNG CÓ [Intro])</span>
                    <button class="copy-btn" onclick="copyText('lyricsPromptPre')">Sao chép</button>
                </div>
                <pre id="lyricsPromptPre"></pre>

                <div class="block-header">
                    <span class="block-title">Code Block 3: EXCLUDE STYLES (Dán vào "Exclude Styles")</span>
                    <button class="copy-btn" onclick="copyText('excludeStylesPre')">Sao chép</button>
                </div>
                <pre id="excludeStylesPre"></pre>

                <div class="guidance-box" id="guidanceBox"></div>
            </div>
        </div>
    </div>

    <script>
        async function buildPrompts() {
            const text = document.getElementById('rawInput').value.trim();
            const genre = document.getElementById('genreSelect').value;
            
            const resp = await fetch('/api/build', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ input: text, genre: genre })
            });
            const data = await resp.json();

            document.getElementById('plainPoemPre').textContent = data.plain_poem;
            document.getElementById('stylePromptPre').textContent = data.style_prompt;
            document.getElementById('lyricsPromptPre').textContent = data.lyrics_prompt;
            document.getElementById('excludeStylesPre').textContent = data.exclude_styles;
            document.getElementById('guidanceBox').textContent = data.guidance;

            document.getElementById('outputArea').style.display = 'block';
        }

        function copyText(elemId) {
            const text = document.getElementById(elemId).textContent;
            navigator.clipboard.writeText(text);
            alert('Đã sao chép vào bộ nhớ tạm!');
        }
    </script>
</body>
</html>
"""

class PromptServerHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path.startswith("/?"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML_PAGE.encode("utf-8"))
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == "/api/build":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            params = json.loads(post_data.decode("utf-8"))
            
            raw_input = params.get("input", "")
            genre = params.get("genre", "viet_ballad")

            builder = SunoPromptBuilder(genre_key=genre)
            result = builder.build_from_input(raw_input)

            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(result).encode("utf-8"))

def run_server():
    with socketserver.TCPServer(("", PORT), PromptServerHandler) as httpd:
        print(f"\n[Suno Prompt Builder Web UI] Running at: http://localhost:{PORT}")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    run_server()
