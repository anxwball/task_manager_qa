# src/tests/conftest.py
import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, Session
from src.database import Base

# Importa tus modelos para que Base.metadata los reconozca
import src.models  # noqa: F401

TEST_DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture(scope="session")
def test_engine():
    """Engine persistente que mantiene la DB en memoria durante la sesión."""
    engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
    )
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)
    engine.dispose()


@pytest.fixture(scope="function")
def db_session(test_engine):
    """Proporciona una sesión aislada con Soporte para SAVEPOINT en SQLite."""
    connection = test_engine.connect()
    transaction = connection.begin()

    # Se crea la sesión ligada a la conexión persistente
    session = Session(bind=connection, join_transaction_mode="create_savepoint")

    # Si el código dentro del test invoca session.commit(), creará un SAVEPOINT
    # en lugar de hacer un commit real a la base de datos.
    @event.listens_for(session, "after_transaction_end")
    def restart_savepoint(session, transaction):
        if transaction.nested and not transaction._parent.nested:
            session.begin_nested()

    session.begin_nested()

    yield session

    session.close()
    transaction.rollback()
    connection.close()
