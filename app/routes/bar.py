from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from .. import schemas, crud, database, dependencies


router = APIRouter()

@router.post("/bars/", response_model=schemas.Bar)
def create_bar(bar: schemas.BarCreate, db: Session = Depends(database.get_db),
               current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["admin", "manager"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_bar = crud.create_bar(db, bar)
    return db_bar

@router.get("/bars/{bar_id}", response_model=schemas.Bar)
def read_bar(bar_id: int, db: Session = Depends(database.get_db),
             current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["admin", "manager", "barman"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_bar = crud.get_bar(db, bar_id)
    if db_bar is None:
        raise HTTPException(status_code=404, detail="Bar not found")
    return db_bar

@router.get("/bars/", response_model=list[schemas.Bar])
def read_bars(db: Session = Depends(database.get_db),
              current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["admin", "manager", "barman"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    bars = crud.get_bars(db)
    return bars



@router.delete("/bars/{bar_id}", response_model=schemas.Bar)
def delete_bar(bar_id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["admin"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_bar = crud.get_bar(db, bar_id)
    if db_bar is None:
        raise HTTPException(status_code=404, detail="Bar not found")
    crud.delete_bar(db, bar_id)
    return db_bar


# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app import models, schemas
# from app.database import get_db
#
# router = APIRouter()
#
#
# @router.get("/bars/", response_model=list[schemas.Bar])
# def read_bars(skip: int = 0, db: Session = Depends(get_db)):
#     bars = db.query(models.Bar).offset(skip).all()
#     return bars
#
#
# @router.get("/bars/{bar_id}", response_model=schemas.Bar)
# def read_bar(bar_id: int, db: Session = Depends(get_db)):
#     db_bar = db.query(models.Bar).filter(models.Bar.id == bar_id).first()
#     if db_bar is None:
#         raise HTTPException(status_code=404, detail="Bar not found")
#     return db_bar
#
#
# @router.post("/bars/", response_model=schemas.Bar)
# def create_bar(bar: schemas.BarCreate, db: Session = Depends(get_db)):
#     db_bar = models.Bar(**bar.dict())
#     db.add(db_bar)
#     db.commit()
#     db.refresh(db_bar)
#     return db_bar
