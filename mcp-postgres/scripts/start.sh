#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
bash scripts/preflight-test.sh
exec python server.py "$@"
