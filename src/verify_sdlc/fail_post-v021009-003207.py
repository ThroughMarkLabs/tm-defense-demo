# PROVENANCE-BEGIN: HUMAN-AUTHORED
# Trace: verify-sdlc-fail-post-v021009-003207
# DDR: DDR-DOES-NOT-EXIST-post-v021009-003207
# Requirement: SRS-DOES-NOT-EXIST-post-v021009-003207
"""Intentionally bad: cites unknown DDR + unknown requirement.
Trial post-v021009-003207 — gate must REJECT this PR."""


def should_be_rejected() -> str:
    return "trial post-v021009-003207 — this file exists to prove the gate blocks bad citations"
# PROVENANCE-END
