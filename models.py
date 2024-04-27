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

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    username = Column(String)
    password = Column(String)

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise ValueError("Username cannot be empty")
        return username
    
    @validates('password')
    def validate_password(self, key, password):
        if not password:
            raise ValueError("Password cannot be empty")
        return password
    
    @classmethod
    def get_by_username(cls, username):
        return session.query(cls).filter_by(username==username).first()

Session = sessionmaker(bind=engine)
session = Session()

def user_filter_by(username):
    return session.query(User).filter_by(username).first()

def get_categoryList():
    return session.query(Food_Category).all()

def get_categoryName(category_id):
    return session.query(Food_Category).get(category_id)

def get_food(food_id):
    return session.query(FoodInfo).get(food_id)

def get_foodList(category_id):
    return session.query(FoodInfo).filter_by(category_id=category_id).all()