from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app import models
from app.database import engine
from app.routes import user, barman, manager, bar, drink, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(barman.router)
app.include_router(manager.router)
app.include_router(bar.router)
app.include_router(drink.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    html_content = "<h2>Hi bro! This is app for barmen</h2>"
    return HTMLResponse(content=html_content)

















# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from . import schemas, dependencies, dao, models
#
# app = FastAPI()
#
# # Маршруты для получения данных
#
# @app.get("/users/", response_model=List[schemas.User])
# async def read_users(db: Session = Depends(dependencies.get_db)):
#     return await dao.UserDAO.find_all()
#
# @app.get("/users/{user_id}", response_model=schemas.User)
# async def read_user(user_id: int, db: Session = Depends(dependencies.get_db)):
#     user = await dao.UserDAO.find_one_or_none_by_id(user_id)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
#
# @app.get("/drinks/", response_model=List[schemas.Drink])
# async def read_drinks(db: Session = Depends(dependencies.get_db)):
#     return await dao.DrinkDAO.find_all()
#
# @app.get("/drinks/{drink_id}", response_model=schemas.Drink)
# async def read_drink(drink_id: int, db: Session = Depends(dependencies.get_db)):
#     drink = await dao.DrinkDAO.find_one_or_none_by_id(drink_id)
#     if drink is None:
#         raise HTTPException(status_code=404, detail="Drink not found")
#     return drink
#
# @app.get("/barmen/", response_model=List[schemas.Barman])
# async def read_barmen(db: Session = Depends(dependencies.get_db)):
#     return await dao.BarmanDAO.find_all()
#
# @app.get("/barmen/{barman_id}", response_model=schemas.Barman)
# async def read_barman(barman_id: int, db: Session = Depends(dependencies.get_db)):
#     barman = await dao.BarmanDAO.find_one_or_none_by_id(barman_id)
#     if barman is None:
#         raise HTTPException(status_code=404, detail="Barman not found")
#     return barman
#
# @app.get("/bars/", response_model=List[schemas.Bar])
# async def read_bars(db: Session = Depends(dependencies.get_db)):
#     return await dao.BarDAO.find_all()
#
# @app.get("/bars/{bar_id}", response_model=schemas.Bar)
# async def read_bar(bar_id: int, db: Session = Depends(dependencies.get_db)):
#     bar = await dao.BarDAO.find_one_or_none_by_id(bar_id)
#     if bar is None:
#         raise HTTPException(status_code=404, detail="Bar not found")
#     return bar
#
# # Маршруты для создания данных
#
# @app.post("/users/", response_model=schemas.User)
# async def create_user(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
#     try:
#         new_user = await dao.UserDAO.add(**user.dict())
#         return new_user
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#
# @app.post("/bars/", response_model=schemas.Bar)
# async def create_bar(bar: schemas.BarBase, db: Session = Depends(dependencies.get_db)):
#     try:
#         new_bar = await dao.BarDAO.add(**bar.dict())
#         return new_bar
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#
# @app.post("/drinks/", response_model=schemas.Drink)
# async def create_drink(drink: schemas.DrinkBase, db: Session = Depends(dependencies.get_db)):
#     try:
#         new_drink = await dao.DrinkDAO.add(**drink.dict())
#         return new_drink
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#
# @app.post("/barmen/", response_model=schemas.Barman)
# async def create_barman(barman: schemas.BarmanBase, db: Session = Depends(dependencies.get_db)):
#     try:
#         new_barman = await dao.BarmanDAO.add(**barman.dict())
#         return new_barman
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#
# @app.post("/managers/", response_model=schemas.Manager)
# async def create_manager(manager: schemas.ManagerBase, db: Session = Depends(dependencies.get_db)):
#     try:
#         new_manager = await dao.ManagerDAO.add(**manager.dict())
#         return new_manager
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))