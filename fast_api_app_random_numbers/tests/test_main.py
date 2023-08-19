from fastapi.testclient import TestClient
from ..app.main import app
#from app.main import app


client = TestClient(app)





def test_read_main():
    response = client.get("/")  # adding the url to client
    assert response.status_code == 200  # Updating correct status code
    assert response.json() == {"message": "Hello World"}


