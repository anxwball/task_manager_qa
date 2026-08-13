from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from src.database import create_tables

def main():
    """Función principal para ejecutar la aplicación."""
    # Crear la base de datos y las tablas si no existen.
    try:
        create_tables()
        print("Base de datos y tablas creadas exitosamente.")
    except Exception as e:
        print(f"Error al crear la base de datos o las tablas: {e}")

if __name__ == "__main__":
    main()
