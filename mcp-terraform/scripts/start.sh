#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
bash scripts/preflight-test.sh
bash scripts/backend-init.sh "${1:-./infra}"
exec python server.py "$@"
