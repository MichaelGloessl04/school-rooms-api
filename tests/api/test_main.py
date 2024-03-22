from fastapi.testclient import TestClient

from sqlalchemy.orm import sessionmaker

import backend.crud.models as Models
from backend.crud import Crud, create_engine

import backend.api.api_types as ApiTypes
from backend.api.main import app, resources

from backend.tests.populate import ROOMS
from backend.tests.populate import populate

base_url = "/ssr-json/v1"
testing = False


def create_test_database():
    url = 'sqlite:///:memory:'
    engine = create_engine(url)
    resources['crud'] = Crud(engine)
    session = sessionmaker(bind=engine)
    populate(session, Models.Room)
    populate(session, Models.User)
    populate(session, Models.Reservation)


def test_read_main():
    global testing
    testing = True
    with TestClient(app) as client:
        response = client.get(base_url + "/")
        assert response.status_code == 200
        assert response.json() == \
            "This is the base endpoint of the school rooms reservation API v1."


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
