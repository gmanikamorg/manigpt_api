from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg://localhost/manigpt_api_db"

engine = create_engine(DATABASE_URL)
