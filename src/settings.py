import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde el archivo .env

# Configuración de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")  # URL de la base de datos
