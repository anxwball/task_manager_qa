# src/tests/test_models.py
import pytest
from sqlalchemy import create_engine, inspect
from src.database import create_tables, drop_tables
from src.models import Task  # noqa: F401


def test_create_tables_function():
    # 1. Engine temporal aislado
    temp_engine = create_engine("sqlite:///:memory:")

    try:
        # 2. Ejecutar la función
        create_tables(bind=temp_engine)

        # 3. Inspeccionar el esquema de la base de datos
        inspector = inspect(temp_engine)
        tables = inspector.get_table_names()

        # 4. Verificación
        assert "tasks" in tables

    finally:
        # Limpieza
        drop_tables(bind=temp_engine)
        temp_engine.dispose()
