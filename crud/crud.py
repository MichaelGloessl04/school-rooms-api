from typing import List
from sqlalchemy.orm import Session

from crud.models import Base, Room, User, Reservation


class Crud:
    def __init__(self, engine):
        self._engine = engine
        Base.metadata.create_all(self._engine)

    def get(self, model: Base) -> List[Base]:
        self._check_model(model)
        with Session(self._engine) as session:
            return session.query(model).all()

    def get_single(self, model: Base, id: int) -> Base:
        self._check_model(model)
        with Session(self._engine) as session:
            return session.query(model).get(id)

    def search(self,
               model: Base,
               columns: List[str],
               search_term: str) -> List[Base]:
        self._check_model(model)
        with Session(self._engine) as session:
            query = session.query(model)
            for column in columns:
                query = query.filter(
                    getattr(model, column).like(f"%{search_term}%"))
        return query.all()

    def create(self, model: Base, data: dict) -> Base:
        self._check_model(model)
        with Session(self._engine) as session:
            instance = model(**data)
            session.add(instance)
            session.commit()
            session.refresh(instance)
            return instance

    def update(self, model: Base, id: int, data: dict) -> Base:
        self._check_model(model)
        with Session(self._engine) as session:
            instance = session.query(model).get(id)
            for key, value in data.items():
                setattr(instance, key, value)
            session.commit()
            session.refresh(instance)
            return instance

    def _check_model(self, model):
        if model not in [Room, User, Reservation]:
            raise TypeError(
                f"Model {model} is not in the list of available models.")
