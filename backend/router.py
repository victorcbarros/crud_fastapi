from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import CarCreate,CarResponse,CarUpdate
from typing import List
from crud import (
    create_car,
    get_car,
    get_cars,
    delete_car,
    update_car
)

router = APIRouter()


@router.get("/cars/", response_model=List[CarResponse])
def read_all_cars(db: Session = Depends(get_db)):
    """
    Essa retorna todos os carros no banco de dados
    """
    cars = get_cars(db=db)
    return cars 


@router.get("/cars/{car_id}", response_model=CarResponse)
def read_one_car(car_id: int,db: Session = Depends(get_db)):
    db_car = get_car(db=db,car_id=car_id)
    """
    Essa busca um carro no banco de dados pelo id
    """
    if db_car is None:
        raise HTTPException(status_code=404, detail="Id do carro não encontrado no banco de dados para busca")
    return db_car


@router.post("/cars/", response_model=CarResponse)
def create_one_car(car: CarCreate,db: Session = Depends(get_db)):
    """
    Essa rota cria um carro no banco de dados
    """
    return create_car(car=car, db=db)

@router.delete("/cars/{car_id}", response_model=CarResponse)
def delete_one_car(car_id: int,db: Session = Depends(get_db)):
    """
    Essa rota deleta um carro no banco de dados pelo id
    """
    db_car = delete_car(car_id=car_id, db=db)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Id do carro não encontrado no banco de dados para deleção")
    return db_car


@router.put("/cars/{car_id}", response_model=CarResponse)
def update_one_car(car_id: int,car: CarUpdate,db: Session = Depends(get_db)):
    db_car = update_car(db=db,car_id=car_id,car=car )
    if db_car is None:
        raise HTTPException(status_code=404, detail="Id do carro não encontrado no banco de dados para atualização")
    return db_car