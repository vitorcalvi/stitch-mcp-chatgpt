#!/usr/bin/env bash
set -euo pipefail
npx -y @_davideast/stitch-mcp@0.9.0 --help >/tmp/stitch-help.txt
grep -qi "stitch" /tmp/stitch-help.txt
echo "stitch upstream CLI smoke test ok"
