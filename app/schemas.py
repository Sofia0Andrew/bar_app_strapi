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





# from pydantic import BaseModel
# from typing import Optional
# from datetime import time
#
# class UserCreate(BaseModel):
#     username: str
#     email: str
#     password_: str
#
# class User(UserCreate):
#     id: int
#     confirmed: bool
#     blocked_: bool
#     roles: str
#
#     class Config:
#         orm_mode = True
#
# class ManagerCreate(BaseModel):
#     fullName: str
#     phoneNumber: str
#     bar_id: int
#     user_id: int
#
# class Manager(ManagerCreate):
#     id: int
#
#     class Config:
#         orm_mode = True
#
# class BarmanCreate(BaseModel):
#     fullName: str
#     phoneNumber: str
#     bar_id: int
#     user_id: int
#     manager_id: int
#
# class Barman(BarmanCreate):
#     id: int
#
#     class Config:
#         orm_mode = True
#
# class BarCreate(BaseModel):
#     name: str
#     address: str
#     working_time_start: time
#     working_time_finish: time
#     description: str
#
# class Bar(BarCreate):
#     id: int
#
#     class Config:
#         orm_mode = True
#
# class DrinkCreate(BaseModel):
#     drinkName: str
#     price: float
#     drinkType: str
#     recipe: str
#     stock: bool
#     bar_id: int
#
# class Drink(DrinkCreate):
#     id: int
#
#     class Config:
#         orm_mode = True
#









# from pydantic import BaseModel
# from typing import Optional
# #from datetime import time
#
# class UserBase(BaseModel):
#     username: str
#     email: str
#
# class UserCreate(UserBase):
#     password: str
#
# class User(UserBase):
#     id: int
#     confirmed: bool
#     blocked_: bool
#     roles: str
#
#     class Config:
#         orm_mode = True
#
# class ManagerBase(BaseModel):
#     fullName: str
#     phoneNumber: str
#     bar_id: int
#     user_id: int
#
# class Manager(ManagerBase):
#     id: int
#
#     class Config:
#         orm_mode = True
#
# class BarBase(BaseModel):
#     name: str
#     address: str
#     working_time_start: str
#     working_time_finish: str
#     description: str
#
# class Bar(BarBase):
#     id: int
#
#     class Config:
#         orm_mode = True
#
# class DrinkBase(BaseModel):
#     drinkName: str
#     price: float
#     drinkType: str
#     recipe: str
#     stock: bool
#     bar_id: int
#
# class Drink(DrinkBase):
#     id: int
#
#     class Config:
#         orm_mode = True
#
# class BarmanBase(BaseModel):
#     fullName: str
#     phoneNumber: str
#     bar_id: int
#     user_id: int
#     manager_id: int
#
# class Barman(BarmanBase):
#     id: int
#
#     class Config:
#         orm_mode = True