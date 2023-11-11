import pytest
from ponderada_openweather import create_app

@pytest.fixture
def app():
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_openweatherdata(client):
    response = client.get('/get_openweatherdata')
    assert response.status_code == 200
