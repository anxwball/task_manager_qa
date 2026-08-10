# src/database.py
from contextlib import contextmanager
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from settings import DATABASE_URL # src/db/tasks.db

if DATABASE_URL is None:
    raise ValueError("La variable de entorno DATABASE_URL no está configurada.")

# 1. Instancias globales thread-safe
engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)
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


def create_tables() -> None:
    """Crea todas las tablas registradas en Base.metadata."""
    Base.metadata.create_all(bind=engine)


def drop_tables() -> None:
    """Elimina todas las tablas registradas en Base.metadata."""
    Base.metadata.drop_all(bind=engine)
