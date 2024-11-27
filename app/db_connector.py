from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from databases import Database
from sqlalchemy.orm import sessionmaker
from fastapi import Depends

# Database connection URL (can be updated based on environment)
sqlite_file_name = "database.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{sqlite_file_name}"

# SQLAlchemy database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Database connection for async operations
database = Database(SQLALCHEMY_DATABASE_URL)

# Base class for models
Base = declarative_base()

def get_db_session(db: Session = Depends(SessionLocal)):
    try:
        yield db
    finally:
        db.close()  # Ensure the session is closed after use