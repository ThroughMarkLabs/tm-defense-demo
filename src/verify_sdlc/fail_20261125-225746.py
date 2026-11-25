# PROVENANCE-BEGIN: HUMAN-AUTHORED
# Trace: verify-sdlc-fail-20261125-225746
# DDR: DDR-DOES-NOT-EXIST-20261125-225746
# Requirement: SRS-DOES-NOT-EXIST-20261125-225746
"""Intentionally bad: cites unknown DDR + unknown requirement.
Trial 20261125-225746 — gate must REJECT this PR."""


def should_be_rejected() -> str:
    return "trial 20261125-225746 — this file exists to prove the gate blocks bad citations"
# PROVENANCE-END
