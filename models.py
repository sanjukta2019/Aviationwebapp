from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FlightRecord(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    airline = Column(String)
    flight_number = Column(String)
    origin = Column(String)
    destination = Column(String)
    departure_time = Column(DateTime)
    price = Column(Float)