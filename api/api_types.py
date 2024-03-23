import datetime

from typing import List
from pydantic import BaseModel


class RoomNoID(BaseModel):
    name: str
    occupied: bool


class Room(RoomNoID):
    id: int


class UserNoID(BaseModel):
    name: str
    surname: str
    email: str


class User(UserNoID):
    id: int


class ReservationNoID(BaseModel):
    user_id: int
    room_id: int
    start: datetime.datetime
    end: datetime.datetime


class Reservation(ReservationNoID):
    id: int


class SearchConfig(BaseModel):
    search_columns: List[str]
    search_term: str
