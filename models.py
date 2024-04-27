from sqlalchemy import create_engine, Column, Integer, String, Text, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, validates

engine = create_engine ('postgresql://postgres:postgres@localhost:5432/food_website')

Base = declarative_base()

class FoodInfo(Base):
    __tablename__ = 'foodinfo'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category_id = Column(Integer)
    nickname = Column(String)
    taste = Column(String)
    efficacy = Column(Text)
    suitable_for = Column(Text)
    not_suitable_for = Column(Text)
    note = Column(Text)
    image = Column(BLOB)
    thumbnail = Column(BLOB)

class Food_Category(Base):
    __tablename__ = 'food_category'
    id = Column(Integer, primary_key=True)
    name = Column(String)    


Session = sessionmaker(bind=engine)
session = Session()

def get_categoryList():
    return session.query(Food_Category).all()

def get_categoryName(category_id):
    return session.query(Food_Category).get(category_id)

def get_food(food_id):
    return session.query(FoodInfo).get(food_id)

def get_foodList(category_id):
    return session.query(FoodInfo).filter_by(category_id=category_id).all()