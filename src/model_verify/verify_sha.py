# PROVENANCE-BEGIN: AI-DRAFTED
# Trace: e8a8d4e34c187b27
# Requirement: SRS-D-100
import hashlib

class WeightsShaMismatch(Exception):
    def __init__(self, path, got, expected):
        self.path, self.got, self.expected = path, got, expected
        super().__init__(f"{path}: got {got}, expected {expected}")

def verify_weights_sha(path, expected_sha):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    got = h.hexdigest()
    if got != expected_sha:
        raise WeightsShaMismatch(path, got, expected_sha)
    return True
# PROVENANCE-END
