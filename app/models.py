from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Numeric, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_ = Column(String, nullable=False)
    confirmed = Column(Boolean, default=False, nullable=False)
    blocked_ = Column(Boolean, default=False, nullable=False)
    roles = Column(String, nullable=False)


class Manager(Base):
    __tablename__ = "managers"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fullName = Column(String, index=True, nullable=False)
    phoneNumber = Column(String(11), unique=True, index=True, nullable=False)
    bar_id = Column(Integer, ForeignKey("bars.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User")
    bar = relationship("Bar")


class Barman(Base):
    __tablename__ = "barmen"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fullName = Column(String, index=True, nullable=False)
    phoneNumber = Column(String(11), unique=True, index=True, nullable=False)
    bar_id = Column(Integer, ForeignKey("bars.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    manager_id = Column(Integer, ForeignKey("managers.id"), nullable=False)
    user = relationship("User")
    bar = relationship("Bar")
    manager = relationship("Manager")


class Bar(Base):
    __tablename__ = "bars"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    address = Column(String, nullable=False)
    working_time_start = Column(Time, nullable=False)
    working_time_finish = Column(Time, nullable=False)
    description = Column(String, nullable=False)


class Drink(Base):
    __tablename__ = "drinks"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    drinkName = Column(String, index=True, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)  # Денежное значение
    drinkType = Column(String, nullable=False)
    recipe = Column(String, nullable=False)
    stock = Column(Boolean, default=True, nullable=False)
    bar_id = Column(Integer, ForeignKey("bars.id"), nullable=False)
    bar = relationship("Bar")


