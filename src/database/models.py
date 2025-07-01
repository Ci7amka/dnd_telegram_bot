from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    username = Column(String, nullable=True)
    
class Character(Base):
    __tablename__ = 'characters'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    race = Column(String, nullable=True)
    character_class = Column(String, nullable=True)
    level = Column(Integer, default=1)
    
    # Храним характеристики и инвентарь в JSON
    ability_scores = Column(JSON, nullable=True)
    inventory = Column(JSON, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class CharacterHistory(Base):
    __tablename__ = 'character_history'
    
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, nullable=False)
    event_type = Column(String, nullable=False)
    event_data = Column(JSON, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
