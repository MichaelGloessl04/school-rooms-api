from fastapi.testclient import TestClient

from backend.api.main_v1 import app

client = TestClient(app)

base_url = "/ssr-json/v1"


def test_read_main():
    response = client.get(base_url + "/")
    assert response.status_code == 200
    assert response.json() == \
        "This is the base endpoint of the school rooms reservation API v1."
