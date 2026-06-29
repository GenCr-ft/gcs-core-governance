#!/usr/bin/env bash
set -euo pipefail
python3 scripts/verify_agent_context_parity.py
python3 scripts/verify_lifecycle_gate_parity.py
python3 scripts/verify_taxonomy_parity.py
