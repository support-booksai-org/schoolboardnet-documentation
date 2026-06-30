#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
rm -rf site .cache
find . -name "__pycache__" -type d -prune -exec rm -rf {} +
echo "Clean complete."
