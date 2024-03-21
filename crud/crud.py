from sqlalchemy.orm import Session

from backend.crud import create_engine
from backend.crud.models import Base, Room, User, Timetable


class Crud:
    def __init__(self, url: str):
        self._engine = create_engine(url)
        self._session = Session(bind=self._engine)
        Base.metadata.create_all(self._engine)
