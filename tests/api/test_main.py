from fastapi.testclient import TestClient

from api.main import app

base_url = "/ssr-json/v1"


def test_read_main():
    with TestClient(app) as client:
        response = client.get(base_url + "/")
        assert response.status_code == 200
        assert response.json() == \
            "This is the base endpoint of the school rooms reservation API v1."


"""
def test_read_rooms():
    global testing
    testing = True
    with TestClient(app) as client:
        response = client.get(base_url + "/rooms/")
        assert response.status_code == 200
        rooms = response.json()
        assert len(rooms) == len(ROOMS)
        for room, test_room in zip(rooms, ROOMS):
            assert isinstance(room, ApiTypes.Room)
            assert room["id"] == test_room["id"]
            assert room["name"] == test_room["name"]
            assert room["occupied"] == test_room["occupied"]
"""
