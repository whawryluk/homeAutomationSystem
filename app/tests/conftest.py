import pytest
from app.main import create_app


@pytest.fixture()
def app():
    app = create_app("config.py")
    app.config.update({
        "TESTING": True,
    })

    return app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_temperature_reading(client):
    response = client.get("/temperature")
    assert b"<h2>asdasd</h2>" in response.data

