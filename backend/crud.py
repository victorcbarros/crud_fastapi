from sqlalchemy.orm import Session
from schemas import CarUpdate, CarCreate
from models import CarsModel


def get_cars(db: Session):
    """
    Essa função retorna todos os carros da banco de dados
    """
    return db.query(CarsModel).all()


def get_car(db: Session, car_id: int):
    """
    Essa função retorna um carro especifico, baseado no id, no  banco de dados
    """
    return db.query(CarsModel).filter(CarsModel.car_id == car_id).first()

def create_car(db: Session, car: CarCreate):
    """
    Essa função cria um carro no banco de dados
    """
    db_car = CarsModel(**car.model_dump())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


def delete_car(db: Session, car_id: int):
    """
    Essa função deleta um carro no banco de dados
    """
    db_car = db.query(CarsModel).filter(CarsModel.car_id == car_id).first()
    db.delete(db_car)
    db.commit()
    return db_car


def update_car(db: Session, car_id: int, car: CarUpdate):
    """
    Essa função atualiza um carro no banco de dados
    """
    db_car = db.query(CarsModel).filter(CarsModel.car_id == car_id).first()

    if db_car is None:
        return None
    if car.model is not None:
        db_car.model = car.model
    if car.brand is not None:
        db_car.brand = car.brand
    if car.model_year is not None:
        db_car.model_year = car.model_year
    if car.plate is not None:
        db_car.plate = car.plate
    if car.kilometers is not None:
        db_car.kilometers = car.kilometers
    if car.status is not None:
        db_car.status = car.status

    db.commit()
    db.refresh(db_car)
    return db_car



