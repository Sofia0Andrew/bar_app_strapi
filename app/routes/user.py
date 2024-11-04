from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database, dependencies, models
from passlib.context import CryptContext

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/users/", response_model=list[schemas.User])
def read_users(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    users = crud.get_users(db)
    return users

@router.get("/users/me", response_model=schemas.User)
def read_users_me(current_user: schemas.User = Depends(dependencies.get_current_user)):
    return current_user

@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(database.get_db),
              current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.id != user_id and current_user.roles != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(dependencies.get_current_user)):
    if current_user.roles not in ["admin"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    crud.delete_user(db, user_id)
    return db_user


@router.put("/users/me/password", response_model=schemas.User)
def update_user_password(new_password: str, db: Session = Depends(database.get_db),
                         current_user: schemas.User = Depends(dependencies.get_current_user)):
    hashed_password = pwd_context.hash(new_password)
    current_user.password_ = hashed_password
    db.commit()
    db.refresh(current_user)
    return current_user

@router.put("/users/me/username", response_model=schemas.User)
def update_user_username(new_username: str, db: Session = Depends(database.get_db),
                         current_user: schemas.User = Depends(dependencies.get_current_user)):
    db_user = db.query(models.User).filter(models.User.username == new_username).first()
    if db_user and db_user.id != current_user.id:
        raise HTTPException(status_code=400, detail="Username already registered")
    current_user.username = new_username
    db.commit()
    db.refresh(current_user)
    return current_user

