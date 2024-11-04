import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, User, Bar, Drink, Barman, Manager
from app.database import DATABASE_URL


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создаем таблицы, если они не существуют
Base.metadata.create_all(bind=engine)

# # все данные тестовые
# users_data = [
#     {"id": 2, "username": "user_8@test.com", "email": "user_8@test.com", "password_": "123456", "confirmed": True, "blocked_": False, "roles": "Authenticated"},
#     {"id": 3, "username": "user_7@test.com", "email": "user_7@test.com", "password_": "123456", "confirmed": True, "blocked_": False, "roles": "Authenticated"},
#     {"id": 4, "username": "mew@test.com", "email": "mew@test.com", "password_": "123456", "confirmed": True, "blocked_": False, "roles": "Authenticated"},
#     {"id": 5, "username": "user_5@test.com", "email": "user_5@test.com", "password_": "123456", "confirmed": True, "blocked_": False, "roles": "manager"},
#     {"id": 6, "username": "testuser", "email": "testuser@example.com", "password_": "$2b$12$iopW0AvIL1AYvLRuiQ0wme5EyDuzl.sCsfw5anPr19pdoaYFOhiQ2", "confirmed": True, "blocked_": False, "roles": "barman"},
#     {"id": 7, "username": "aboba", "email": "testuser2@example.com", "password_": "$2b$12$aDQJzoi75/fRFGbgOBvJueJG3/w702n2dKiPME5uJMEtVPQZmwGlq", "confirmed": True, "blocked_": False, "roles": "manager"},
#     {"id": 8, "username": "string", "email": "user@example.com", "password_": "$2b$12$mdIji/e.BFYLI5LJKLP5leLIduT3qm85WNLFtFRyVqzGGjMxb7/nS", "confirmed": True, "blocked_": False, "roles": "barman"},
#     {"id": 9, "username": "Semion", "email": "semion@test.com", "password_": "$2b$12$oE7bNl0OTL6Q.hlcikiaRecDLeDkTbQx7.nk9FjJjJJEhApczZ5lG", "confirmed": True, "blocked_": False, "roles": "barman"},
#     {"id": 11, "username": "Sofia", "email": "sofa@etest.com", "password_": "$2b$12$wmg2r.lAvcp6nNLlUuDSDuJ.U/pEWEvgFuhsEWUc3L66ue5lMaJT.", "confirmed": True, "blocked_": False, "roles": "Registered"},
#     {"id": 10, "username": "Admin", "email": "admin@test.com", "password_": "$2b$12$XP1trcRoI18YXXVm5fzJvu0CuwVUJ5C3.GdTM.2Qhc7yUCPEFSPOG", "confirmed": True, "blocked_": False, "roles": "admin"},
#     {"id": 12, "username": "oaoaoa", "email": "oaoaoa@test.com", "password_": "$2b$12$lHWbszVIKsJ5tkIVbhOFzuhO4DVY6eTpSxPhR2u1z4UHjZb9gnnxi", "confirmed": True, "blocked_": False, "roles": "barman"},
# ]

bars_data = [
    {"id": 1, "name": "The Tequila Tiger", "address": "г. Москва, ул. Пушкина, д. 24, стр. 1", "working_time_start": "19:00:00", "working_time_finish": "06:00:00", "description": "The Tequila Tiger is one of the best modern bars in Moscow! You can order classic drinks as a true connoisseur of traditions or you can try our craft drinks to to experience new sensations. We are waiting for you here, have fun!"},
    {"id": 2, "name": "Pussy", "address": "г. Москва, ул. Пушкина, д. 25", "working_time_start": "20:00:00", "working_time_finish": "06:00:00", "description": "lol kek"},
]

drinks_data = [
    {"id": 1, "drinkName": "Mojito", "price": 350.0, "drinkType": "Alcohol", "recipe": "1.5 oz white rum, 1 oz lime juice, 2 tsp sugar, 6-8 mint leaves, soda water", "stock": True, "bar_id": 1},
    {"id": 2, "drinkName": "Tequila Sunrice", "price": 500.0, "drinkType": "Alcohol", "recipe": "туда сюда там сям и вот ваша текила лол", "stock": True, "bar_id": 1},
]

managers_data = [
    {"id": 1, "fullName": "Dodo Pepe", "phoneNumber": "89762563452", "bar_id": 1, "user_id": 7},
]

barmen_data = [
    {"id": 1, "fullName": "Luci", "phoneNumber": "89995551234", "bar_id": 1, "user_id": 6, "manager_id": 1},
    {"id": 2, "fullName": "Lola", "phoneNumber": "89765432191", "bar_id": 1, "user_id": 8, "manager_id": 1},
    {"id": 3, "fullName": "Semion L", "phoneNumber": "87662345123", "bar_id": 1, "user_id": 9, "manager_id": 1},
    {"id": 4, "fullName": "Alena", "phoneNumber": "88654352167", "bar_id": 1, "user_id": 12, "manager_id": 1},
]

# def populate_users():
#     db = SessionLocal()
#     for user_data in users_data:
#         user = User(**user_data)
#         db.add(user)
#     db.commit()
#     db.close()

def populate_bars():
    db = SessionLocal()
    for bar_data in bars_data:
        bar = Bar(**bar_data)
        db.add(bar)
    db.commit()
    db.close()

def populate_drinks():
    db = SessionLocal()
    for drink_data in drinks_data:
        drink = Drink(**drink_data)
        db.add(drink)
    db.commit()
    db.close()

def populate_managers():
    db = SessionLocal()
    for manager_data in managers_data:
        manager = Manager(**manager_data)
        db.add(manager)
    db.commit()
    db.close()

def populate_barmen():
    db = SessionLocal()
    for barman_data in barmen_data:
        barman = Barman(**barman_data)
        db.add(barman)
    db.commit()
    db.close()


if __name__ == "__main__":
    #populate_users()
    populate_bars()
    populate_drinks()
    populate_managers()
    populate_barmen()