# PROVENANCE-BEGIN: HUMAN-AUTHORED
# Trace: verify-sdlc-fail-20261125-044633
# DDR: DDR-DOES-NOT-EXIST-20261125-044633
# Requirement: SRS-DOES-NOT-EXIST-20261125-044633
"""Intentionally bad: cites unknown DDR + unknown requirement.
Trial 20261125-044633 — gate must REJECT this PR."""


def should_be_rejected() -> str:
    return "trial 20261125-044633 — this file exists to prove the gate blocks bad citations"
# PROVENANCE-END
