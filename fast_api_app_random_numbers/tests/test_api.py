from fastapi.testclient import TestClient
from ..app.main import app
#from app.main import app

client = TestClient(app)
def test_random_vector():
    response = client.post("/random_vector/", json={"preqin_testing_numbers": "This is a test sentence."})
    assert response.status_code == 200  # Update to the correct status code
    assert len(response.json()) == 500


def test_random_vector():
    response = client.post("/random_vector/", json={"preqin_testing_numbers": "Test is in progess"})
    assert response.status_code == 200  # Update to the correct status code
    assert len(response.json()) == 500

