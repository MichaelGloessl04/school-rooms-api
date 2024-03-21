from typing import List
from fastapi import FastAPI
from contextlib import asynccontextmanager

import backend.crud.models as Models
from backend.crud import create_engine, Crud

import backend.api.api_types as ApiTypes

crud = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """start the character device reader"""
    print('lifespan started')
    global crud
    engine = create_engine('sqlite:///backend/database.db')
    crud = Crud(engine)
    yield
    engine.dispose()
    crud = None
    print('lifespan finished')


app = FastAPI(lifespan=lifespan)
prefix = '/ssr-json/v1'


@app.get(prefix + '/')
async def read_main():
    return "This is the base endpoint of the school rooms reservation API v1."


@app.get(prefix + '/rooms/')
async def read_rooms() -> List[ApiTypes.Room]:
    global crud
    return crud.get(Models.Room)
