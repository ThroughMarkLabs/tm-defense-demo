# PROVENANCE-BEGIN: HUMAN-AUTHORED
# Trace: verify-sdlc-fail-20261124-154535
# DDR: DDR-DOES-NOT-EXIST-20261124-154535
# Requirement: SRS-DOES-NOT-EXIST-20261124-154535
"""Intentionally bad: cites unknown DDR + unknown requirement.
Trial 20261124-154535 — gate must REJECT this PR."""


def should_be_rejected() -> str:
    return "trial 20261124-154535 — this file exists to prove the gate blocks bad citations"
# PROVENANCE-END
