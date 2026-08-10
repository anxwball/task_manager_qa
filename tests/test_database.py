# src/tests/test_database.py
from sqlalchemy import text

def test_database_connection(test_engine):
    """Verifica la conexión usando el engine de pruebas."""
    with test_engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        assert result.scalar() == 1
