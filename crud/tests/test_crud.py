import datetime

from crud.crud import Crud
from crud.models import Room, User, Timetable

from .populate import ROOMS, USERS, TIMETABLES


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


def test_get_timetables(crud_in_memory: Crud):
    crud = crud_in_memory
    timetables = crud.get(Timetable)
    for timetable, test_timetable in zip(timetables, TIMETABLES):
        assert isinstance(timetable, Timetable)
        assert timetable.id == test_timetable["id"]
        assert timetable.start == test_timetable["start"]
        assert timetable.end == test_timetable["end"]
        assert timetable.room_id == test_timetable["room_id"]
        assert timetable.user_id == test_timetable["user_id"]


def test_get_timetable(crud_in_memory: Crud):
    crud = crud_in_memory
    timetable = crud.get_single(Timetable, id=TIMETABLES[0]["id"])
    assert isinstance(timetable, Timetable)
    assert timetable.id == TIMETABLES[0]["id"]
    assert timetable.start == TIMETABLES[0]["start"]
    assert timetable.end == TIMETABLES[0]["end"]
    assert timetable.room_id == TIMETABLES[0]["room_id"]
    assert timetable.user_id == TIMETABLES[0]["user_id"]


def test_create_timetable(crud_in_memory: Crud):
    crud = crud_in_memory
    new_timetable = {
        "start": datetime.datetime(2021, 1, 1, 12, 0, 0),
        "end": datetime.datetime(2021, 1, 1, 13, 0, 0),
        "room_id": 1,
        "user_id": 1
    }
    timetable = crud.create(Timetable, new_timetable)
    assert isinstance(timetable, Timetable)
    assert timetable.id == len(TIMETABLES) + 1
    assert timetable.start == new_timetable["start"]
    assert timetable.end == new_timetable["end"]
    assert timetable.room_id == new_timetable["room_id"]
    assert timetable.user_id == new_timetable["user_id"]


def test_update_timetable(crud_in_memory: Crud):
    crud = crud_in_memory
    updated_timetable = {"start": datetime.datetime(2021, 1, 1, 8, 30, 0)}
    timetable = crud.update(Timetable, id=1, data=updated_timetable)
    assert isinstance(timetable, Timetable)
    assert timetable.id == TIMETABLES[0]["id"]
    assert timetable.start == updated_timetable["start"]
    assert timetable.end == TIMETABLES[0]["end"]
    assert timetable.room_id == TIMETABLES[0]["room_id"]
    assert timetable.user_id == TIMETABLES[0]["user_id"]


def test_search_timetables(crud_in_memory: Crud):
    crud = crud_in_memory
    for i in range(1, 3):
        timetables = crud.search(Timetable,
                                 ["user_id"],
                                 TIMETABLES[i]["user_id"])
        assert len(timetables) == 1
        assert timetables[0].user_id == TIMETABLES[i]["user_id"]
