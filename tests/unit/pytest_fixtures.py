import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def test_client_fixture() -> TestClient:
    return TestClient
