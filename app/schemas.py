from pydantic import BaseModel, EmailStr, constr, field_validator
from typing import Optional, List
from datetime import time
import re

class UserBase(BaseModel):
    username: str
    email: EmailStr
    password_: str
    confirmed: bool = False
    blocked_: bool = False
    roles: str
    access_token: Optional[str] = None  # Добавляем поле access_token

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class ManagerBase(BaseModel):
    fullName: str
    bar_id: int
    user_id: int
    phoneNumber: constr(min_length=11, max_length=11)

    @field_validator('phoneNumber')
    def validate_phone_number(cls, v):
        phone_regex = r'^8\d{10}$'
        if not re.match(phone_regex, v):
            raise ValueError('Invalid phone number format. It should be in the format 8XXXXXXXXXX')
        return v

class ManagerCreate(ManagerBase):
    pass

class Manager(ManagerBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True

class BarmanBase(BaseModel):
    fullName: str
    phoneNumber: constr(min_length=11, max_length=11)

    @field_validator('phoneNumber')
    def validate_phone_number(cls, v):
        phone_regex = r'^8\d{10}$'
        if not re.match(phone_regex, v):
            raise ValueError('Invalid phone number format. It should be in the format 8XXXXXXXXXX')
        return v

    bar_id: int
    user_id: int
    manager_id: int



class BarmanCreate(BarmanBase):
    pass

class Barman(BarmanBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True


class BarBase(BaseModel):
    name: str
    address: str
    working_time_start: time
    working_time_finish: time
    description: str

class BarCreate(BarBase):
    pass

class Bar(BarBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True

class BarmanInfo(BaseModel):
    managers: List[Manager]
    bars: List[Bar]

    class Config:
        orm_mode = True
        from_attributes = True

class ManagerInfo(BaseModel):
    barmen: List[Barman]
    bars: List[Bar]

    class Config:
        orm_mode = True
        from_attributes = True


class DrinkBase(BaseModel):
    drinkName: str
    price: float
    drinkType: str
    recipe: str
    stock: bool = True
    bar_id: int

class DrinkCreate(DrinkBase):
    pass

class Drink(DrinkBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str

