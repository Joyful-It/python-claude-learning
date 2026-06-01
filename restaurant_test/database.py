from sqlalchemy import create_engine,Column,Integer,Float,String
from sqlalchemy.orm import DeclarativeBase


engine=create_engine("sqlite:///restaurant.db")

class Base(DeclarativeBase):
    pass