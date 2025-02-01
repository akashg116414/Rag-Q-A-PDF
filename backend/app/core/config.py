import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./test.db")  # SQLite for metadata
    VECTOR_DB_PATH: str = os.getenv("VECTOR_DB_PATH", "./vector_store")  # Path for FAISS or ChromaDB
    SECRET_KEY: str = os.getenv("SECRET_KEY", "mysecret")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
