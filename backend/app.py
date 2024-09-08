from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

# Crear instancia de la app y configurar
app = Flask(__name__)
app.config.from_object(Config)

# Inicializar CORS para permitir solicitudes desde localhost:3000
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Inicializar SQLAlchemy
db = SQLAlchemy(app)
