import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crud.crud import Crud
from crud.models import Room, Timetable, User

from .populate import populate


@pytest.fixture
def crud_in_memory():
    engine = create_engine('sqlite:///:memory:')
    crud = Crud(engine)
    session = sessionmaker(bind=engine)
    populate(session, Room)
    populate(session, User)
    populate(session, Timetable)
    yield crud
