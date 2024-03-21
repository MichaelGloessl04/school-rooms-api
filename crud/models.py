from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    __abstract__ = True


class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    occupied = Column(Boolean, default=False)

    def __repr__(self):
        return "<Room(name='%s', description='%s')>" % (self.name,
                                                        self.description)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)

    def __repr__(self):
        return "<User(name='%s', surname='%s', email='%s')>" % (self.name,
                                                                self.surname,
                                                                self.email)


class Timetable(Base):
    __tablename__ = 'timetables'

    id = Column(Integer, primary_key=True)
    start = Column(String)
    end = Column(String)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return \
            "<Timetable(start='%s', end='%s', room_id='%s', user_id='%s')>" % (
                self.start, self.end, self.room_id, self.user_id)
