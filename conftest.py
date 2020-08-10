import pytest
from main import app

@pytest.fixture
def client():
    app = app()
    return app

def test_app(app):
    console.log(123)
    assert client.get('/').status_code == 200
