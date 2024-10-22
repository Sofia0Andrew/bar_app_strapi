from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database, dependencies

router = APIRouter()


@router.post("/barmen/", response_model=schemas.Barman)
def create_barman(barman: schemas.BarmanCreate, db: Session = Depends(database.get_db),
                  current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["admin", "manager"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_barman = crud.create_barman(db, barman)

    # Обновляем роль пользователя, связанного с барменом
    user = crud.get_user(db, barman.user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Создаем бармена
    db_barman = crud.create_barman(db, barman)

    # Обновляем роль пользователя на "barman"
    user.roles = "barman"
    db.commit()
    db.refresh(user)

    return db_barman

@router.get("/barmen/{barman_id}", response_model=schemas.Barman)
def read_barman(barman_id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["admin", "manager"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_barman = crud.get_barman(db, barman_id)
    if db_barman is None:
        raise HTTPException(status_code=404, detail="Barman not found")
    return db_barman

@router.get("/barmen/", response_model=list[schemas.Barman])
def read_barmen(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["admin", "manager"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    barmen = crud.get_barmen(db)
    return barmen

@router.delete("/barmen/{barman_id}", response_model=schemas.Barman)
def delete_barman(barman_id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["admin", "manager"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_barman = crud.get_barman(db, barman_id)
    if db_barman is None:
        raise HTTPException(status_code=404, detail="Barman not found")
    crud.delete_barman(db, barman_id)
    return db_barman


@router.get("/barmen/me/info", response_model=schemas.BarmanInfo)
def get_barman_info(db: Session = Depends(database.get_db),
                    current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["barman", "admin"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    db_barman = crud.get_barman_by_user_id(db, current_user.id)
    if db_barman is None:
        raise HTTPException(status_code=404, detail="Barman not found")

    managers = [schemas.Manager.from_orm(manager) for manager in crud.get_managers_for_barman(db, db_barman.id)]
    bars = [schemas.Bar.from_orm(bar) for bar in crud.get_bars_for_barman(db, db_barman.id)]

    return schemas.BarmanInfo(managers=managers, bars=bars)

@router.put("/barmen/me/phone", response_model=schemas.Barman)
def update_barman_phone(new_phone: str, db: Session = Depends(database.get_db),
                        current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["barman"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    db_barman = crud.get_barman_by_user_id(db, current_user.id)
    if db_barman is None:
        raise HTTPException(status_code=404, detail="Barman not found")

    db_barman.phoneNumber = new_phone
    db.commit()
    db.refresh(db_barman)
    return db_barman




# @router.post("/barmen/", response_model=schemas.Barman)
# def create_barman(barman: schemas.BarmanCreate, db: Session = Depends(database.get_db),
#                   current_user: schemas.User = Depends(dependencies.get_current_user)):
#     if current_user.roles not in ["admin", "manager"]:
#         raise HTTPException(status_code=403, detail="Not enough permissions")
#     db_barman = crud.create_barman(db, barman)
#     return db_barman
#
# @router.get("/barmen/{barman_id}", response_model=schemas.Barman)
# def read_barman(barman_id: int, db: Session = Depends(database.get_db),
#                 current_user: schemas.User = Depends(dependencies.get_current_user)):
#     if current_user.roles not in ["admin", "manager", "barman"]:
#         raise HTTPException(status_code=403, detail="Not enough permissions")
#     db_barman = crud.get_barman(db, barman_id)
#     if db_barman is None:
#         raise HTTPException(status_code=404, detail="Barman not found")
#     return db_barman
#
# @router.get("/barmen/", response_model=list[schemas.Barman])
# def read_barmen(db: Session = Depends(database.get_db),
#                 current_user: schemas.User = Depends(dependencies.get_current_user)):
#     if current_user.roles not in ["admin", "manager", "barman"]:
#         raise HTTPException(status_code=403, detail="Not enough permissions")
#     barmen = crud.get_barmen(db)
#     return barmen



# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app import models, schemas
# from app.database import get_db
#
# router = APIRouter()
#
# @router.get("/barmen/{barman_id}", response_model=schemas.Barman)
# def read_barman(barman_id: int, db: Session = Depends(get_db)):
#     db_barman = db.query(models.Barman).filter(models.Barman.id == barman_id).first()
#     if db_barman is None:
#         raise HTTPException(status_code=404, detail="Barman not found")
#     return db_barman
#
# @router.post("/barmen/", response_model=schemas.Barman)
# def create_barman(barman: schemas.BarmanCreate, db: Session = Depends(get_db)):
#     db_barman = models.Barman(**barman.dict())
#     db.add(db_barman)
#     db.commit()
#     db.refresh(db_barman)
#     return db_barman