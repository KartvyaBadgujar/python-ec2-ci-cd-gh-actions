import pytest
from app.main import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello from GitHub Actions CI/CD Pipeline!" in response.data

