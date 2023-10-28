import sys
import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from .create_dummy_api import create_dummy_api


sys.path.append("src")
load_dotenv()


@pytest.mark.middlewares
def test_calculate_process_time_middleware():
    
    from api.middlewares.process_time_middleware import process_time_middleware
    
    app = create_dummy_api()
    process_time_middleware(app)
    client = TestClient(app)

    response = client.get("/")

    assert type(response.headers["process-time"]) == str


@pytest.mark.middlewares
def test_generate_request_id_middleware():
    
    from api.middlewares.request_id_middleware import request_id_middleware
    
    app = create_dummy_api()
    request_id_middleware(app)
    client = TestClient(app)

    response = client.get("/")

    assert type(response.headers["request-id"]) == str
