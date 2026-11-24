# PROVENANCE-BEGIN: HUMAN-AUTHORED
# Trace: verify-sdlc-fail-20261124-152754
# DDR: DDR-DOES-NOT-EXIST-20261124-152754
# Requirement: SRS-DOES-NOT-EXIST-20261124-152754
"""Intentionally bad: cites unknown DDR + unknown requirement.
Trial 20261124-152754 — gate must REJECT this PR."""


def should_be_rejected() -> str:
    return "trial 20261124-152754 — this file exists to prove the gate blocks bad citations"
# PROVENANCE-END
