import datetime

from crud.crud import Crud
from crud.models import Room, User, Reservation

from tests.populate import ROOMS, USERS, RESERVATIONS


def test_get_rooms(crud_in_memory: Crud):
    crud = crud_in_memory
    rooms = crud.get(Room)
    for room, test_room in zip(rooms, ROOMS):
        assert isinstance(room, Room)
        assert room.id == test_room["id"]
        assert room.name == test_room["name"]
        assert room.occupied == test_room["occupied"]


def test_get_room(crud_in_memory: Crud):
    crud = crud_in_memory
    room = crud.get_single(Room, id=ROOMS[0]["id"])
    assert isinstance(room, Room)
    assert room.id == ROOMS[0]["id"]
    assert room.name == ROOMS[0]["name"]
    assert room.occupied == ROOMS[0]["occupied"]


def test_create_room(crud_in_memory: Crud):
    crud = crud_in_memory
    new_room = {"name": "Room 4", "occupied": False}
    room = crud.create(Room, new_room)
    assert isinstance(room, Room)
    assert room.id == len(ROOMS) + 1
    assert room.name == new_room["name"]
    assert room.occupied == new_room["occupied"]


def test_update_room(crud_in_memory: Crud):
    crud = crud_in_memory
    updated_room = {"name": "Room 1 Updated"}
    room = crud.update(Room, id=1, data=updated_room)
    assert isinstance(room, Room)
    assert room.id == ROOMS[0]["id"]
    assert room.name == updated_room["name"]
    assert room.occupied == ROOMS[0]["occupied"]


def test_search_rooms(crud_in_memory: Crud):
    crud = crud_in_memory
    for i in range(1, 4):
        rooms = crud.search(Room, ["name"], f"Room {i}")
        assert len(rooms) == 1
        assert rooms[0].name == f"Room {i}"


def test_get_users(crud_in_memory: Crud):
    crud = crud_in_memory
    users = crud.get(User)
    for user, test_user in zip(users, USERS):
        assert isinstance(user, User)
        assert user.id == test_user["id"]
        assert user.name == test_user["name"]
        assert user.surname == test_user["surname"]
        assert user.email == test_user["email"]


def test_get_user(crud_in_memory: Crud):
    crud = crud_in_memory
    user = crud.get_single(User, id=USERS[0]["id"])
    assert isinstance(user, User)
    assert user.id == USERS[0]["id"]
    assert user.name == USERS[0]["name"]
    assert user.surname == USERS[0]["surname"]
    assert user.email == USERS[0]["email"]


def test_create_user(crud_in_memory: Crud):
    crud = crud_in_memory
    new_user = {
        "name": "Bob",
        "surname": "Doe",
        "email": "bobdoe@example.com"
    }
    user = crud.create(User, new_user)
    assert isinstance(user, User)
    assert user.id == len(USERS) + 1
    assert user.name == new_user["name"]
    assert user.surname == new_user["surname"]
    assert user.email == new_user["email"]


def test_update_user(crud_in_memory: Crud):
    crud = crud_in_memory
    updated_user = {"name": "John Updated"}
    user = crud.update(User, id=1, data=updated_user)
    assert isinstance(user, User)
    assert user.id == USERS[0]["id"]
    assert user.name == updated_user["name"]
    assert user.surname == USERS[0]["surname"]
    assert user.email == USERS[0]["email"]


def test_search_users(crud_in_memory: Crud):
    crud = crud_in_memory
    for i in range(1, 3):
        users = crud.search(User, ["name"], USERS[i]["name"])
        assert len(users) == 1
        assert users[0].name == USERS[i]["name"]


def test_get_reservations(crud_in_memory: Crud):
    crud = crud_in_memory
    reservations = crud.get(Reservation)
    for reservation, test_reservation in zip(reservations, RESERVATIONS):
        assert isinstance(reservation, Reservation)
        assert reservation.id == test_reservation["id"]
        assert reservation.start == test_reservation["start"]
        assert reservation.end == test_reservation["end"]
        assert reservation.room_id == test_reservation["room_id"]
        assert reservation.user_id == test_reservation["user_id"]


def test_get_reservation(crud_in_memory: Crud):
    crud = crud_in_memory
    reservation = crud.get_single(Reservation, id=RESERVATIONS[0]["id"])
    assert isinstance(reservation, Reservation)
    assert reservation.id == RESERVATIONS[0]["id"]
    assert reservation.start == RESERVATIONS[0]["start"]
    assert reservation.end == RESERVATIONS[0]["end"]
    assert reservation.room_id == RESERVATIONS[0]["room_id"]
    assert reservation.user_id == RESERVATIONS[0]["user_id"]


def test_create_reservation(crud_in_memory: Crud):
    crud = crud_in_memory
    new_reservation = {
        "start": datetime.datetime(2021, 1, 1, 12, 0, 0),
        "end": datetime.datetime(2021, 1, 1, 13, 0, 0),
        "room_id": 1,
        "user_id": 1
    }
    reservation = crud.create(Reservation, new_reservation)
    assert isinstance(reservation, Reservation)
    assert reservation.id == len(RESERVATIONS) + 1
    assert reservation.start == new_reservation["start"]
    assert reservation.end == new_reservation["end"]
    assert reservation.room_id == new_reservation["room_id"]
    assert reservation.user_id == new_reservation["user_id"]


def test_update_reservation(crud_in_memory: Crud):
    crud = crud_in_memory
    updated_reservation = {"start": datetime.datetime(2021, 1, 1, 8, 30, 0)}
    reservation = crud.update(Reservation, id=1, data=updated_reservation)
    assert isinstance(reservation, Reservation)
    assert reservation.id == RESERVATIONS[0]["id"]
    assert reservation.start == updated_reservation["start"]
    assert reservation.end == RESERVATIONS[0]["end"]
    assert reservation.room_id == RESERVATIONS[0]["room_id"]
    assert reservation.user_id == RESERVATIONS[0]["user_id"]


def test_search_reservations(crud_in_memory: Crud):
    crud = crud_in_memory
    for i in range(1, 3):
        reservations = crud.search(Reservation,
                                   ["user_id"],
                                   RESERVATIONS[i]["user_id"])
        assert len(reservations) == 1
        assert reservations[0].user_id == RESERVATIONS[i]["user_id"]
