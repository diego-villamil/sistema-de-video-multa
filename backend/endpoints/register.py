from flask import Blueprint, request, jsonify
from models import Usuario
from app import db  # Importar db desde app.py

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"message": "Faltan datos", "status": "error"}), 400

    # Verificar si el usuario o email ya existen
    if Usuario.query.filter_by(email=email).first():
        return jsonify({"message": "El email ya está registrado", "status": "error"}), 400
    if Usuario.query.filter_by(username=username).first():
        return jsonify({"message": "El nombre de usuario ya está en uso", "status": "error"}), 400

    # Crear un nuevo usuario
    nuevo_usuario = Usuario(username=username, email=email, password=password, rol='user')
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({"message": f"Usuario {nuevo_usuario.username} registrado con éxito", "status": "success"}), 201
