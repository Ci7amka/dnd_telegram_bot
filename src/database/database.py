from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# Базовый класс для моделей
Base = declarative_base()

class DatabaseManager:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._init_db()
        return cls._instance
    
    def _init_db(self):
        # URL базы данных из .env
        db_url = os.getenv('DATABASE_URL', 'sqlite:///data/characters.db')
        
        # Создание движка
        self.engine = create_engine(db_url, echo=False)
        
        # Создание сессии
        self.SessionLocal = sessionmaker(
            bind=self.engine, 
            autocommit=False, 
            autoflush=False
        )
    
    def get_session(self):
        return self.SessionLocal()
    
    def init_models(self):
        # Создание таблиц
        Base.metadata.create_all(self.engine)
    
    def add_entity(self, entity):
        session = self.get_session()
        try:
            session.add(entity)
            session.commit()
            return entity
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def get_character_by_user(self, user_id):
        session = self.get_session()
        try:
            return session.query(Character).filter_by(user_id=user_id).first()
        finally:
            session.close()
