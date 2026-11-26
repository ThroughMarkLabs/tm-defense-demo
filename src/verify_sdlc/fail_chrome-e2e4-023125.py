# PROVENANCE-BEGIN: HUMAN-AUTHORED
# Trace: verify-sdlc-fail-chrome-e2e4-023125
# DDR: DDR-DOES-NOT-EXIST-chrome-e2e4-023125
# Requirement: SRS-DOES-NOT-EXIST-chrome-e2e4-023125
"""Intentionally bad: cites unknown DDR + unknown requirement.
Trial chrome-e2e4-023125 — gate must REJECT this PR."""


def should_be_rejected() -> str:
    return "trial chrome-e2e4-023125 — this file exists to prove the gate blocks bad citations"
# PROVENANCE-END
