from sqlalchemy.orm import Session
from . import models, schemas


#all for users (almost all)

def get_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user



#all for managers (almost all)

def create_manager(db: Session, manager: schemas.ManagerCreate):
    db_manager = models.Manager(**manager.dict())
    db.add(db_manager)
    db.commit()
    db.refresh(db_manager)
    return db_manager

def get_manager(db: Session, manager_id: int):
    return db.query(models.Manager).filter(models.Manager.id == manager_id).first()

def get_managers(db: Session):
    return db.query(models.Manager).all()

def get_manager_by_user_id(db: Session, user_id: int):
    return db.query(models.Manager).filter(models.Manager.user_id == user_id).first()

def get_barmen_for_manager(db: Session, manager_id: int):
    return db.query(models.Barman).filter(models.Barman.manager_id == manager_id).all()

def get_bars_for_manager(db: Session, manager_id: int):
    return db.query(models.Bar).join(models.Manager,
                            models.Bar.id == models.Manager.bar_id).filter(models.Manager.id == manager_id).all()


def delete_manager(db: Session, manager_id: int):
    db_manager = db.query(models.Manager).filter(models.Manager.id == manager_id).first()
    if db_manager:
        db.delete(db_manager)
        db.commit()
    return db_manager




#all for barmen (almost all)

def create_barman(db: Session, barman: schemas.BarmanCreate):
    db_barman = models.Barman(**barman.dict())
    db.add(db_barman)
    db.commit()
    db.refresh(db_barman)
    return db_barman

def get_barman(db: Session, barman_id: int):
    return db.query(models.Barman).filter(models.Barman.id == barman_id).first()

def get_barmen(db: Session):
    return db.query(models.Barman).all()

def delete_barman(db: Session, barman_id: int):
    db_barman = db.query(models.Barman).filter(models.Barman.id == barman_id).first()
    if db_barman:
        db.delete(db_barman)
        db.commit()
    return db_barman

def get_barman_by_user_id(db: Session, user_id: int):
    return db.query(models.Barman).filter(models.Barman.user_id == user_id).first()

def get_managers_for_barman(db: Session, barman_id: int):
    return db.query(models.Manager).join(models.Barman,
                            models.Manager.bar_id == models.Barman.bar_id).filter(models.Barman.id == barman_id).all()

def get_bars_for_barman(db: Session, barman_id: int):
    return db.query(models.Bar).join(models.Barman,
                                     models.Bar.id == models.Barman.bar_id).filter(models.Barman.id == barman_id).all()


#all for bars (almost all)

def create_bar(db: Session, bar: schemas.BarCreate):
    db_bar = models.Bar(**bar.dict())
    db.add(db_bar)
    db.commit()
    db.refresh(db_bar)
    return db_bar

def get_bar(db: Session, bar_id: int):
    return db.query(models.Bar).filter(models.Bar.id == bar_id).first()

def get_bars(db: Session):
    return db.query(models.Bar).all()

def delete_bar(db: Session, bar_id: int):
    db_bar = db.query(models.Bar).filter(models.Bar.id == bar_id).first()
    if db_bar:
        db.delete(db_bar)
        db.commit()
    return db_bar




#all for drinks (almost all)

def create_drink(db: Session, drink: schemas.DrinkCreate):
    db_drink = models.Drink(**drink.dict())
    db.add(db_drink)
    db.commit()
    db.refresh(db_drink)
    return db_drink

def get_drink(db: Session, drink_id: int):
    return db.query(models.Drink).filter(models.Drink.id == drink_id).first()

def get_all_drinks(db: Session):
    return db.query(models.Drink).all()


def get_bar_drinks(db: Session, bar_id: int):
    return db.query(models.Drink).filter(models.Drink.bar_id == bar_id).all()

def search_bar_drinks(db: Session, bar_id: int, drink_name: str):
    return db.query(models.Drink).filter(models.Drink.bar_id == bar_id,
                                         models.Drink.drinkName.ilike(f"%{drink_name}%")).all()

def delete_drink(db: Session, drink_id: int):
    db_drink = db.query(models.Drink).filter(models.Drink.id == drink_id).first()
    if db_drink:
        db.delete(db_drink)
        db.commit()
    return db_drink








