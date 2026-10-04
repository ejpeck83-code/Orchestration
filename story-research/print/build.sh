#!/usr/bin/env bash
# Rebuilds premise-packet.pdf from premise-packet.html.
# Downloads the 2 Google Fonts (OFL) into fonts/ on first run, then prints with headless Chromium.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p fonts
css="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400"
if [ ! -f fonts/SourceSerif4-400i.ttf ]; then
  curl -sS "$css" | python3 -c '
import re, sys, subprocess
for face in re.findall(r"@font-face \{(.*?)\}", sys.stdin.read(), re.S):
    fam = re.search(r"font-family: .(.+?).;", face).group(1).replace(" ", "")
    wt = re.search(r"font-weight: (\d+)", face).group(1)
    it = "i" if "italic" in face else ""
    url = re.search(r"url\((.+?)\)", face).group(1)
    subprocess.run(["curl", "-sS", "-o", f"fonts/{fam}-{wt}{it}.ttf", url], check=True)
'
fi
chrome="${CHROME:-$(ls -d /opt/pw-browsers/chromium-*/chrome-linux/chrome 2>/dev/null | head -1)}"
"$chrome" --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=5000 --print-to-pdf=premise-packet.pdf \
  "file://$PWD/premise-packet.html" 2>/dev/null
echo "wrote $PWD/premise-packet.pdf"
