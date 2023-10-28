import sys
import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient


sys.path.append("src")
load_dotenv()


from main import app
client = TestClient(app)


@pytest.mark.api
def test_home_router():
    response = client.get("http://127.0.0.1:8000/")
    
    assert response.status_code == 200
    assert response.json() == {"status": "up"}
