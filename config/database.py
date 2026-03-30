from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://admin:8pPZ7ypOKQNrFsDoAH5OOsqjY8CTQiCb@dpg-d74uc6ogjchc73beigsg-a.virginia-postgres.render.com:5432/ferreteriabd?sslmode=require"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()