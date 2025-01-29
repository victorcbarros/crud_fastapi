from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base


class CarsModel(Base):
    __tablename__ = "cars"

    car_id = Column(Integer, primary_key=True)
    model = Column(String)
    brand = Column(String)
    model_year = Column(Integer)
    plate = Column(String)
    kilometers = Column(Float)
    status = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())    

