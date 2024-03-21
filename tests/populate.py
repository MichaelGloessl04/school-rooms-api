import datetime

from backend.crud.models import Room, Reservation, User


ROOMS = [
    {"id": 1, "name": "Room 1", "occupied": False},
    {"id": 2, "name": "Room 2", "occupied": False},
    {"id": 3, "name": "Room 3", "occupied": False},
]

USERS = [
    {
        "id": 1,
        "name": "John",
        "surname": "Doe",
        "email": "johndoe@example.com"
    },
    {
        "id": 2,
        "name": "Jane",
        "surname": "Doe",
        "email": "janedoe@example.com"
    },
    {
        "id": 3,
        "name": "Alice",
        "surname": "Doe",
        "email": "alicedoe@example.com"
    },
]

RESERVATIONS = [
    {
        "id": 1,
        "start": datetime.datetime(2021, 1, 1, 8, 0, 0),
        "end": datetime.datetime(2021, 1, 1, 9, 0, 0),
        "room_id": 1,
        "user_id": 1
    },
    {
        "id": 2,
        "start": datetime.datetime(2021, 1, 1, 9, 0, 0),
        "end": datetime.datetime(2021, 1, 1, 10, 0, 0),
        "room_id": 2,
        "user_id": 2
    },
    {
        "id": 3,
        "start": datetime.datetime(2021, 1, 1, 10, 0, 0),
        "end": datetime.datetime(2021, 1, 1, 11, 0, 0),
        "room_id": 3,
        "user_id": 3
    }
]


def populate(session, obj):
    mock_data = []
    if obj == Room:
        mock_data = ROOMS
    elif obj == User:
        mock_data = USERS
    elif obj == Reservation:
        mock_data = RESERVATIONS

    with session() as session:
        for data in mock_data:
            session.add(obj(**data))
        session.commit()
