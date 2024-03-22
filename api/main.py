from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

import crud.models as Models
from crud import create_engine, Crud

import api.api_types as ApiTypes

resources = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """start the character device reader"""
    print('lifespan started')
    engine = create_engine('sqlite:///database.db')
    resources['crud'] = Crud(engine)
    yield
    engine.dispose()
    resources.clear()
    print('lifespan finished')


app = FastAPI(lifespan=lifespan,
              swagger_ui_parameters={
                    'persistAuthorization': True,
                    'docExpansion': 'none'
                })

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def read_main():
    return "This is the base endpoint of the school rooms reservation API v1."


@app.get('/rooms/', tags=['rooms'])
async def read_rooms(search_columns: str = None,
                     search_term: str = None) -> List[ApiTypes.Room]:
    if search_term and search_columns:
        return resources['crud'].search(Models.Room,
                                        search_columns.split(','),
                                        search_term)
    else:
        return resources['crud'].get(Models.Room)


@app.get('/rooms/{room_id}', tags=['rooms'])
async def read_room(room_id: int) -> ApiTypes.Room:
    return resources['crud'].get(Models.Room, room_id)


@app.post('/rooms/', tags=['rooms'])
async def create_room(room: ApiTypes.RoomNoID) -> ApiTypes.Room:
    new_room = {
        'name': room.name,
        'occupied': room.occupied,
    }
    return resources['crud'].create(Models.Room, new_room)


@app.put('/rooms/{room_id}', tags=['rooms'])
async def update_room(room_id: int, room: ApiTypes.RoomNoID) -> ApiTypes.Room:
    updated_room = {
        'name': room.name,
        'occupied': room.occupied,
    }
    return resources['crud'].update(Models.Room, room_id, updated_room)


@app.delete('/rooms/{room_id}', tags=['rooms'])
async def delete_room(room_id: int):
    resources['crud'].delete(Models.Room, room_id)


@app.get('/reservations/', tags=['reservations'])
async def read_reservations(
        search_columns: str = None,
        search_term: str = None) -> List[ApiTypes.Reservation]:
    if search_term and search_columns:
        return resources['crud'].search(Models.Reservation,
                                        search_columns.split(','),
                                        search_term)
    else:
        return resources['crud'].get(Models.Reservation)


@app.get('/reservations/{reservation_id}', tags=['reservations'])
async def read_reservation(reservation_id: int) -> ApiTypes.Reservation:
    return resources['crud'].get(Models.Reservation, reservation_id)


@app.post('/reservations/', tags=['reservations'])
async def create_reservation(
        reservation: ApiTypes.ReservationNoID) -> ApiTypes.Reservation:
    new_reservation = {
        'room_id': reservation.room_id,
        'date': reservation.date,
        'start_time': reservation.start_time,
        'end_time': reservation.end_time,
    }
    return resources['crud'].create(Models.Reservation, new_reservation)


@app.put('/reservations/{reservation_id}', tags=['reservations'])
async def update_reservation(
        reservation_id: int,
        reservation: ApiTypes.ReservationNoID) -> ApiTypes.Reservation:
    updated_reservation = {
        'room_id': reservation.room_id,
        'date': reservation.date,
        'start_time': reservation.start_time,
        'end_time': reservation.end_time,
    }
    return resources['crud'].update(
        Models.Reservation, reservation_id, updated_reservation)


@app.delete('/reservations/{reservation_id}', tags=['reservations'])
async def delete_reservation(reservation_id: int):
    resources['crud'].delete(Models.Reservation, reservation_id)


@app.get('/users/', tags=['users'])
async def read_users(search_columns: str = None,
                     search_term: str = None) -> List[ApiTypes.User]:
    if search_term and search_columns:
        return resources['crud'].search(Models.User,
                                        search_columns.split(','),
                                        search_term)
    else:
        return resources['crud'].get(Models.User)


@app.get('/users/{user_id}', tags=['users'])
async def read_user(user_id: int) -> ApiTypes.User:
    return resources['crud'].get(Models.User, user_id)


@app.post('/users/', tags=['users'])
async def create_user(user: ApiTypes.UserNoID) -> ApiTypes.User:
    new_user = {
        'name': user.name,
        'email': user.email,
        'password': user.password,
    }
    return resources['crud'].create(Models.User, new_user)


@app.put('/users/{user_id}', tags=['users'])
async def update_user(user_id: int, user: ApiTypes.UserNoID) -> ApiTypes.User:
    updated_user = {
        'name': user.name,
        'email': user.email,
        'password': user.password,
    }
    return resources['crud'].update(Models.User, user_id, updated_user)


@app.delete('/users/{user_id}', tags=['users'])
async def delete_user(user_id: int):
    resources['crud'].delete(Models.User, user_id)
