from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database, dependencies

router = APIRouter()

@router.post("/drinks/", response_model=schemas.Drink)
def create_drink(drink: schemas.DrinkCreate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["admin", "manager"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_drink = crud.create_drink(db, drink)
    return db_drink

@router.get("/drinks/{drink_id}", response_model=schemas.Drink)
def read_drink(drink_id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["admin", "manager", "barman"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_drink = crud.get_drink(db, drink_id)
    if db_drink is None:
        raise HTTPException(status_code=404, detail="Drink not found")
    return db_drink

@router.get("/drinks/", response_model=list[schemas.Drink])
def read_all_drinks(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["admin", "manager", "barman"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_drinks = crud.get_all_drinks(db)
    return db_drinks


@router.get("/bars/{bar_id}/drinks", response_model=list[schemas.Drink])
def read_bar_drinks(bar_id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["admin", "manager", "barman"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_drinks = crud.get_bar_drinks(db, bar_id)
    return db_drinks
#проверитт

@router.get("/bars/{bar_id}/drinks/search", response_model=list[schemas.Drink])
def search_bar_drinks(bar_id: int, drink_name: str, db: Session = Depends(database.get_db),
                      current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["admin", "manager", "barman"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_drinks = crud.search_bar_drinks(db, bar_id, drink_name)
    return db_drinks
#это тоже


@router.delete("/drinks/{drink_id}", response_model=schemas.Drink)
def delete_drink(drink_id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["admin"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_drink = crud.get_drink(db, drink_id)
    if db_drink is None:
        raise HTTPException(status_code=404, detail="Drink not found")
    crud.delete_drink(db, drink_id)
    return db_drink