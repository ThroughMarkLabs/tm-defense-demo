# Human-authored (no PROVENANCE block — clean-room).
# Covers SRS-D-100 via Trace: e8a8d4e34c187b27
import pytest
from src.model_verify.verify_sha import verify_weights_sha, WeightsShaMismatch

def test_match():
    assert verify_weights_sha("tests/fixtures/weights.bin", "b5e3684a83fcc5d9bbb5c519f18fde39a48db7b3af235c62f87a01fe7d060ccd") is True

def test_mismatch():
    with pytest.raises(WeightsShaMismatch):
        verify_weights_sha("tests/fixtures/weights.bin", "0" * 64)
