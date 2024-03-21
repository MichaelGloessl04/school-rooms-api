from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    __abstract__ = True


class Room(Base):
    """The model for the rooms table.

    Attributes:
        id (int): The primary key.
        name (str): The name of the room.
        occupied (bool): The status of the room.
    """
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    occupied = Column(Boolean, default=False)

    def __repr__(self):
        return "<Room(name='%s', description='%s')>" % (self.name,
                                                        self.description)


class User(Base):
    """The model for the users table.

    Attributes:
        id (int): The primary key.
        name (str): The name of the user.
        surname (str): The surname of the user.
        email (str): The email of the user.
    """
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
    """The model for the timetables table.

    Attributes:
        id (int): The primary key.
        start (str): The start time of the timetable.
        end (str): The end time of the timetable.
        room_id (int): The foreign key to the rooms table.
        user_id (int): The foreign key to the users table.
    """
    __tablename__ = 'timetables'

    id = Column(Integer, primary_key=True)
    start = Column(DateTime)
    end = Column(DateTime)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return \
            "<Timetable(start='%s', end='%s', room_id='%s', user_id='%s')>" % (
                self.start, self.end, self.room_id, self.user_id)
