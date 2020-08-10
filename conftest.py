import pytest
from main import app as client

@pytest.fixture
def app():
    app = client()
    return app

def test_app(app):
    console.log(123)
    assert client.get('/').status_code == 200
