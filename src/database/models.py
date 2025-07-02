from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Character(Base):
    __tablename__ = 'characters'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    race = Column(String)
    character_class = Column(String)
    
def init_database(db_path='characters.db'):
    DATABASE_URL = f'sqlite:///{db_path}'
    engine = create_engine(DATABASE_URL, echo=True)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)
