from flask import Blueprint, jsonify
from models import User  # Asegúrate de tener un modelo User que se ajuste a tu estructura de base de datos

get_info_user_bp = Blueprint('get_info_user', __name__)

@get_info_user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_info(user_id):
    try:
        user = User.query.get(user_id)  # Consulta a la base de datos
        if not user:
            return jsonify({'status': 'error', 'message': 'Usuario no encontrado'}), 404

        # Devolver información del usuario
        return jsonify({
            'status': 'success',
            'data': {
                'id': user.id,
                'nombre': user.nombre,
                'email': user.email
            }
        }), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
