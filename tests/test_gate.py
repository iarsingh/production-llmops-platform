from fastapi.testclient import TestClient
from llmops.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'prompt_version': '3', 'eval_passed': True, 'cost_ok': True}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'prompt_version': '3', 'eval_passed': True}).json()
    assert bad["passed"] is False
    assert "cost_ok" in bad["failed"]
