#!/usr/bin/env python3
from pathlib import Path
import sys

if len(sys.argv) != 4:
    raise SystemExit("usage: build.py UPSTREAM CUSTOM OUTPUT")

upstream = Path(sys.argv[1]).read_text(encoding="utf-8")
custom = Path(sys.argv[2]).read_text(encoding="utf-8").strip()

marker = "[Rule]"
if marker not in upstream:
    raise SystemExit("Upstream config has no [Rule] section")

# Do not inherit upstream update-url: Shadowrocket must update from Mike's final config.
lines = [line for line in upstream.splitlines() if not line.strip().lower().startswith("update-url")]
upstream = "\n".join(lines) + "\n"

before, after = upstream.split(marker, 1)
header = (
    "# PERSONAL BUILD: minkaka/shadowrocket-rules\n"
    "# Upstream: Johnshall/Shadowrocket-ADBlock-Rules-Forever release/sr_cnip.conf\n"
    "# Generated automatically. Edit rules/custom.list, not this file.\n\n"
)
output = (
    header + before + marker +
    "\n\n# ===== MIKE CUSTOM RULES =====\n" +
    custom +
    "\n# ===== END MIKE CUSTOM RULES =====\n" +
    after
)
Path(sys.argv[3]).write_text(output, encoding="utf-8")
