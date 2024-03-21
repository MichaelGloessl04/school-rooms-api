from fastapi.testclient import TestClient

from backend.crud import Crud

import backend.api.api_types as ApiTypes
from backend.api.main import app

from backend.tests.populate import ROOMS

base_url = "/ssr-json/v1"


def test_read_main():
    with TestClient(app) as client:
        response = client.get(base_url + "/")
        assert response.status_code == 200
        assert response.json() == \
            "This is the base endpoint of the school rooms reservation API v1."


def test_read_rooms(crud_in_memory: Crud):
    with TestClient(app) as client:
        response = client.get(base_url + "/rooms/")
        assert response.status_code == 200
        rooms = response.json()
        for room, test_room in zip(rooms, ROOMS):
            assert isinstance(room, ApiTypes.Room)
            assert room["id"] == test_room["id"]
            assert room["name"] == test_room["name"]
            assert room["occupied"] == test_room["occupied"]
