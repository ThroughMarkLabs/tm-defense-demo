# PROVENANCE-BEGIN: HUMAN-AUTHORED
# Trace: verify-sdlc-fail-post-v021008-001822
# DDR: DDR-DOES-NOT-EXIST-post-v021008-001822
# Requirement: SRS-DOES-NOT-EXIST-post-v021008-001822
"""Intentionally bad: cites unknown DDR + unknown requirement.
Trial post-v021008-001822 — gate must REJECT this PR."""


def should_be_rejected() -> str:
    return "trial post-v021008-001822 — this file exists to prove the gate blocks bad citations"
# PROVENANCE-END
