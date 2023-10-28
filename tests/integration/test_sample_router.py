import sys
import json
import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient


sys.path.append("src")
load_dotenv()


from main import app
client = TestClient(app)


url = "http://127.0.0.1:8000/sample"
headers = {"Content-Type": "application/json"}


with open("tests/resources/inputs.json", "r") as fp:
    inputs = json.load(fp)
with open("tests/resources/outputs.json", "r") as fp:
    outputs = json.load(fp)


@pytest.mark.api
def test_with_get_request():
    response = client.get(url=url)
    assert response.status_code == 405


@pytest.mark.api
def test_with_no_input():
    response = client.post(url=url)
    assert response.status_code == 400


@pytest.mark.api
def test_with_true_input():
    response = client.post(url=url, headers=headers, data=json.dumps(inputs))
    assert response.status_code == 200
    assert response.json() == outputs


@pytest.mark.api
def test_with_additional_kays():
    custom_inputs = inputs.copy()
    custom_inputs["email"] = "animesh.ani@live.com"
    response = client.post(url=url, headers=headers, data=json.dumps(custom_inputs))
    assert response.status_code == 400


@pytest.mark.api
def test_with_missing_kays():
    custom_inputs = inputs.copy()
    custom_inputs.pop("first_name")
    response = client.post(url=url, headers=headers, data=json.dumps(custom_inputs))
    assert response.status_code == 400
