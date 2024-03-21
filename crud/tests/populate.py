import datetime

from crud.models import Room, Timetable, User


ROOMS = [
    Room(name='Room 1', occupied=False),
    Room(name='Room 2', occupied=False),
    Room(name='Room 3', occupied=False),
]

USERS = [
    User(name='John', surname='Doe', email=''),
    User(name='Jane', surname='Doe', email=''),
    User(name='John', surname='Smith', email=''),
]

TIMETABLES = [
    Timetable(start=datetime.time(8, 0), end=datetime.time(9, 0),
              room_id=1, user_id=1),
    Timetable(start=datetime.time(9, 0), end=datetime.time(10, 0),
              room_id=2, user_id=2),
    Timetable(start=datetime.time(10, 0), end=datetime.time(11, 0),
              room_id=3, user_id=3),
]


def populate(session, obj):
    mock_data = []
    if obj == Room:
        mock_data = ROOMS
    elif obj == User:
        mock_data = USERS
    elif obj == Timetable:
        mock_data = TIMETABLES

    with session() as session:
        session.add_all(mock_data)
        session.commit()
