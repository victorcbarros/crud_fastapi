from pydantic import BaseModel, PositiveFloat, PositiveInt
from datetime import datetime
from typing import Optional


class CarBase(BaseModel):
   model: str 
   brand: str 
   model_year : PositiveInt
   plate: str 
   kilometers : PositiveFloat
   status : str

class CarCreate(CarBase):
   pass 

class CarResponse(CarBase):
    car_id: int
    created_at: datetime

    class Config:
       from_attributes = True

class CarUpdate(BaseModel):
   model: Optional[str] = None
   brand: Optional[str] = None
   model_year: Optional[PositiveInt] = None
   plate: Optional[str] = None
   kilometers: Optional[PositiveFloat] = None
   status: Optional[str] = None
