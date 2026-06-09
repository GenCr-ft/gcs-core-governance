#!/usr/bin/env bash
# check-freshness.sh - Detects documents that haven't been updated recently.
set -euo pipefail

MAX_DAYS_STALE=30
CURRENT_SECS=$(date +%s)

echo "[INFO] Scanning for stale documentation (max age: $MAX_DAYS_STALE days)..."

STALE_COUNT=0
find . -name "*.md" -not -path "*/.*" | while read -r doc; do
    # Extract date using more robust sed
    LAST_UPDATED=$(grep "last_updated_date:" "$doc" | head -n 1 | sed 's/last_updated_date: //;s/["'\'']//g;s/ //g')

    if [[ -n "$LAST_UPDATED" ]]; then
        # Try GNU date then BSD date
        DOC_SECS=$(date -d "$LAST_UPDATED" +%s 2>/dev/null || date -jf "%Y-%m-%d" "$LAST_UPDATED" +%s 2>/dev/null || echo "")

        if [[ -n "$DOC_SECS" ]]; then
            DIFF_DAYS=$(( (CURRENT_SECS - DOC_SECS) / 86400 ))
            if [ "$DIFF_DAYS" -gt "$MAX_DAYS_STALE" ]; then
                echo "[WARN] $doc is stale ($DIFF_DAYS days old)."
                STALE_COUNT=$((STALE_COUNT + 1))
            fi
        fi
    fi
done

echo "[INFO] Scan complete."
