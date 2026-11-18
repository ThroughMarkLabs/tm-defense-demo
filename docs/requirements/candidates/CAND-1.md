## CAND-1 — Refuse to start when model weight digest does not match the signed manifest

Text: The appliance SHALL refuse to start if the sha256 of the chat model's weights does not match the digest recorded in the signed manifest shipped with the model release.
Evidence: docs/requirements/candidates/CAND-1.md (this draft)
Confidence: the developer stated this behaviour explicitly; it aligns to DoWI 8430.01 §3.6.f (see Standard)
Standard:
Notes: Standard: is left blank per the skill rule (repo does not yet state it). The draft is aligned to DoWI 8430.01 §3.6.f Weight Manifest Verification on the human's request; the id and the decision to adopt this standard are the developer's at promotion. Acceptance fields (in-memory sha256, byte-for-byte compare, abort on mismatch, ledger log with computed_digest/manifest_digest/operator_identity/timestamp) are drawn from the standard's acceptance language, not asserted as a done fact.
