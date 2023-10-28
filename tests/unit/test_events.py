import sys
import pytest
import logging
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from .create_dummy_api import create_dummy_api
from .pytest_fixtures import test_client_fixture


sys.path.append("src")
load_dotenv()


@pytest.mark.events
def test_startup_event(test_client_fixture: TestClient):
    
    from api.events import startup
    
    app = create_dummy_api()
    startup.include_event(app, logging)
    client = test_client_fixture(app)

    response = client.get("/")

    assert response.status_code == 200


@pytest.mark.events
def test_shutdown_event(test_client_fixture: TestClient):
    
    from api.events import shutdown
    
    app = create_dummy_api()
    shutdown.include_event(app, logging)
    client = test_client_fixture(app)

    response = client.get("/")

    assert response.status_code == 200
