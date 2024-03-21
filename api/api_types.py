from pydantic import BaseModel


class RoomNoID(BaseModel):
    name: str
    occupied: bool


class Room(RoomNoID):
    id: int


class UserNoID(BaseModel):
    name: str
    email: str
    password: str


class User(UserNoID):
    id: int


class ReservationNoID(BaseModel):
    user_id: int
    room_id: int
    start_date: str
    end_date: str


class Reservation(ReservationNoID):
    id: int
