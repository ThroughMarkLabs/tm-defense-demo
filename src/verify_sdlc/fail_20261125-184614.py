# PROVENANCE-BEGIN: HUMAN-AUTHORED
# Trace: verify-sdlc-fail-20261125-184614
# DDR: DDR-DOES-NOT-EXIST-20261125-184614
# Requirement: SRS-DOES-NOT-EXIST-20261125-184614
"""Intentionally bad: cites unknown DDR + unknown requirement.
Trial 20261125-184614 — gate must REJECT this PR."""


def should_be_rejected() -> str:
    return "trial 20261125-184614 — this file exists to prove the gate blocks bad citations"
# PROVENANCE-END
