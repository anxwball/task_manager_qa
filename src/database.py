# src/database.py
from contextlib import contextmanager
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from src.settings import DATABASE_URL # src/db/tasks.db

if DATABASE_URL is None:
    raise ValueError("La variable de entorno DATABASE_URL no está configurada.")

# 1. Instancias globales thread-safe
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 2. Base declarativa única para registrar modelos
Base = declarative_base()

# 3. Generador de sesiones
@contextmanager
def get_db() -> Generator[Session, None, None]:
    """Proporciona un contexto seguro para manejar sesiones de DB."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables(bind=engine):
    """Crea todas las tablas definidas en los modelos."""
    Base.metadata.create_all(bind=bind)

def drop_tables(bind=engine):
    """Elimina todas las tablas definidas en los modelos."""
    Base.metadata.drop_all(bind=bind)
