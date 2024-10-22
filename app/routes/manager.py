from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database, dependencies

router = APIRouter()


@router.post("/managers/", response_model=schemas.Manager)
def create_manager(manager: schemas.ManagerCreate, db: Session = Depends(database.get_db),
                   current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["admin"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_manager = crud.create_manager(db, manager)

    # Проверяем, существует ли пользователь с указанным user_id
    user = crud.get_user(db, manager.user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Создаем менеджера
    db_manager = crud.create_manager(db, manager)

    # Обновляем роль пользователя на "manager"
    user.roles = "manager"
    db.commit()
    db.refresh(user)

    return db_manager


@router.get("/managers/{manager_id}", response_model=schemas.Manager)
def read_manager(manager_id: int, db: Session = Depends(database.get_db),
                 current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["admin", "manager"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_manager = crud.get_manager(db, manager_id)
    if db_manager is None:
        raise HTTPException(status_code=404, detail="Manager not found")
    return db_manager


@router.get("/managers/", response_model=list[schemas.Manager])
def read_managers(db: Session = Depends(database.get_db),
                  current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["admin", "manager"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    managers = crud.get_managers(db)
    return managers


@router.get("/managers/me/info", response_model=schemas.ManagerInfo)
def get_manager_info(db: Session = Depends(database.get_db),
                     current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["manager", "admin"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    db_manager = crud.get_manager_by_user_id(db, current_user.id)
    if db_manager is None:
        raise HTTPException(status_code=404, detail="Manager not found")

    barmen = [schemas.Barman.from_orm(barman) for barman in crud.get_barmen_for_manager(db, db_manager.id)]
    bars = [schemas.Bar.from_orm(bar) for bar in crud.get_bars_for_manager(db, db_manager.id)]

    return schemas.ManagerInfo(barmen=barmen, bars=bars)


@router.delete("/managers/{manager_id}", response_model=schemas.Manager)
def delete_manager(manager_id: int, db: Session = Depends(database.get_db),
                   current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["admin"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_manager = crud.get_manager(db, manager_id)
    if db_manager is None:
        raise HTTPException(status_code=404, detail="Manager not found")
    crud.delete_manager(db, manager_id)
    return db_manager


# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app import models, schemas
# from app.database import get_db
#
# router = APIRouter()
#
# @router.get("/managers/{manager_id}", response_model=schemas.Manager)
# def read_manager(manager_id: int, db: Session = Depends(get_db)):
#     db_manager = db.query(models.Manager).filter(models.Manager.id == manager_id).first()
#     if db_manager is None:
#         raise HTTPException(status_code=404, detail="Manager not found")
#     return db_manager
#
# @router.post("/managers/", response_model=schemas.Manager)
# def create_manager(manager: schemas.ManagerCreate, db: Session = Depends(get_db)):
#     db_manager = models.Manager(**manager.dict())
#     db.add(db_manager)
#     db.commit()
#     db.refresh(db_manager)
#     return db_manager