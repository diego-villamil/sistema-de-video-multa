from flask import Blueprint, request, jsonify
from models import Usuario
from app import db  # Importar db desde app.py

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Faltan datos", "status": "error"}), 400

    # Buscar al usuario en la base de datos
    usuario = Usuario.query.filter_by(email=email).first()

    # Verificar si el usuario existe y si la contraseña coincide
    if usuario and usuario.password == password:
        return jsonify({"message": "Login exitoso", "rol": usuario.rol, "status": "success"}), 200
    else:
        return jsonify({"message": "Email o contraseña incorrectos", "status": "error"}), 401
