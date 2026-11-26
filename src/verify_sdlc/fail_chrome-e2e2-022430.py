# PROVENANCE-BEGIN: HUMAN-AUTHORED
# Trace: verify-sdlc-fail-chrome-e2e2-022430
# DDR: DDR-DOES-NOT-EXIST-chrome-e2e2-022430
# Requirement: SRS-DOES-NOT-EXIST-chrome-e2e2-022430
"""Intentionally bad: cites unknown DDR + unknown requirement.
Trial chrome-e2e2-022430 — gate must REJECT this PR."""


def should_be_rejected() -> str:
    return "trial chrome-e2e2-022430 — this file exists to prove the gate blocks bad citations"
# PROVENANCE-END
