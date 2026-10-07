import os

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+psycopg://localhost/manigpt_api_db"
)
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "manigptjwtsecretkey27101987")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
