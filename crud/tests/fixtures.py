import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crud.crud import Crud
from crud.models import Base, Room, Timetable, User

from .populate import populate


@pytest.fixture
def crud_in_memory():
    engine = create_engine('sqlite:///:memory:')
    session = sessionmaker(bind=engine)()
    yield Crud(session)
