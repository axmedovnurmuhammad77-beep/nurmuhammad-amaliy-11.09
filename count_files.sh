#!/usr/bin/env bash
set -euo pipefail

folder="${1:-.}"

if [[ ! -d "$folder" ]]; then
    printf 'Folder does not exist: %s\n' "$folder" >&2
    exit 2
fi

find "$folder" -maxdepth 1 -type f -print | wc -l