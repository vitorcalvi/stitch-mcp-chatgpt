from pathlib import Path
import json, re, sys
root=Path(__file__).resolve().parents[1]
for p in [root/'.mcp.json', root/'.codex-plugin/plugin.json']:
    json.loads(p.read_text())
for p in root.rglob('*'):
    if p.is_file() and '.git' not in p.parts:
        text=p.read_text(errors='ignore')
        if re.search(r'(?i)(STITCH_API_KEY\s*[=:]\s*["\']?[A-Za-z0-9_\-]{20,})', text) and 'your-key' not in text:
            raise SystemExit(f'possible secret in {p}')
print('validation ok')
