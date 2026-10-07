from sqlalchemy.orm import sessionmaker

from database.connection import engine

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)
