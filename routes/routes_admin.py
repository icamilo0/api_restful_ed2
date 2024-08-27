from flask import request, Blueprint, jsonify
from models.model_admin import Admin

admins_bp = Blueprint('model_admin', __name__)
# ruta para autentificar en la tabla 'admins' los datos ingresados
@admins_bp.route('/api/admins/authenticate', methods=['POST'])
def authenticate_admin():
    data = request.json
    authenticate_admin_result = Admin.authenticate(data)

    if 'error' in authenticate_admin_result:
        return jsonify(authenticate_admin_result), authenticate_admin_result[1]

    return jsonify(authenticate_admin_result[0]), authenticate_admin_result[1]