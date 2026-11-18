## SRS-D-100 — Chat model weights manifest verification
Text: The appliance SHALL refuse to start if the chat model's weights sha256 does not match the signed manifest.
Standard: DoWI 8430.01 §3.6.f (Weight Manifest Verification)
Acceptance: On startup the appliance computes sha256 of the chat model weights file in-memory and compares it byte-for-byte against the digest recorded in the signed weights manifest shipped with the model release; on any mismatch it aborts initialization before starting and logs the abort to the integrity ledger with computed_digest, manifest_digest, operator_identity, and timestamp.
Promoted-from: CAND-1
Trace: 3f71f5662de8d2c1
Promoted-by: andrew@defense.demo
Promoted-at: 2026-11-18T04:25:41.869075Z
