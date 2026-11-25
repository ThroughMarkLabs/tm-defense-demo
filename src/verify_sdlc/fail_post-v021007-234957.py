# PROVENANCE-BEGIN: HUMAN-AUTHORED
# Trace: verify-sdlc-fail-post-v021007-234957
# DDR: DDR-DOES-NOT-EXIST-post-v021007-234957
# Requirement: SRS-DOES-NOT-EXIST-post-v021007-234957
"""Intentionally bad: cites unknown DDR + unknown requirement.
Trial post-v021007-234957 — gate must REJECT this PR."""


def should_be_rejected() -> str:
    return "trial post-v021007-234957 — this file exists to prove the gate blocks bad citations"
# PROVENANCE-END
