# PROVENANCE-BEGIN: HUMAN-AUTHORED
# Trace: verify-sdlc-fail-walkthrough-205359
# DDR: DDR-DOES-NOT-EXIST-walkthrough-205359
# Requirement: SRS-DOES-NOT-EXIST-walkthrough-205359
"""Intentionally bad: cites unknown DDR + unknown requirement.
Trial walkthrough-205359 — gate must REJECT this PR."""


def should_be_rejected() -> str:
    return "trial walkthrough-205359 — this file exists to prove the gate blocks bad citations"
# PROVENANCE-END
