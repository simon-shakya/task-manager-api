import pytest
from app import app

API_KEY = "my-secret-key"

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_all_tasks(client):
    response = client.get("/tasks", headers={"x-api-key": API_KEY})
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
