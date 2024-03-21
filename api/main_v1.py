from typing import List
from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager

import backend.crud.models as Models
from backend.crud import create_engine, Crud

import backend.api.api_types as ApiTypes

resources = {}


@asynccontextmanager
async def lifespan():
    """start the character device reader"""
    print('lifespan started')
    engine = create_engine('sqlite:///database.db')
    resources['crud'] = Crud(engine)
    yield
    engine.dispose()
    resources.clear()
    print('lifespan finished')


prefix_router = APIRouter(prefix='/ssr-json/v1')


@prefix_router.get('/')
async def read_main():
    return "This is the base endpoint of the school rooms reservation API v1."


app = FastAPI(lifespan=lifespan)
app.include_router(prefix_router)


@app.get('/rooms/')
async def read_rooms() -> List[ApiTypes.Room]:
    return resources['crud'].get(Models.Room)
