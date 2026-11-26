#!/usr/bin/env bash
set -eu
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd -- "$SCRIPT_DIR/.." && pwd)"
CACHE_DIR="$(cd -- "$PROJECT_DIR/.." && pwd)/.local_runtime"
export OLLAMA_HOST=127.0.0.1:11436
export OLLAMA_MODELS="$CACHE_DIR/models"
export OLLAMA_NO_CLOUD=1
export OLLAMA_NUM_PARALLEL=1
export OLLAMA_MAX_LOADED_MODELS=1
export OLLAMA_KV_CACHE_TYPE=f16
if [ ! -x "$CACHE_DIR/ollama/bin/ollama" ]; then
    echo "Local runtime cache is missing. Restore the runtime before the review."
    exit 1
fi
exec "$CACHE_DIR/ollama/bin/ollama" serve
