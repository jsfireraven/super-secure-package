#!/usr/bin/env bash
# Start the MCP server (runs integration preflight first).
set -euo pipefail
cd "$(dirname "$0")/.."
bash scripts/preflight-test.sh
exec python server.py "$@"
