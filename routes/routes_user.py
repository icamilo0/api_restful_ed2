from flask import request, Blueprint, jsonify
from models.model_user import User

users_bp = Blueprint('model_user', __name__)

# ruta para agregar usuarios en la tabla 'users'
@users_bp.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    create_user_result = User.create(data)

    if 'error' in create_user_result:
        return jsonify(create_user_result), create_user_result[1]

    return jsonify(create_user_result[0]), create_user_result[1]

# ruta para llamar un registro de la tabla 'users' por el id
@users_bp.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    id_user_result = User.read(id)

    if 'error' in id_user_result:
        return jsonify(id_user_result), id_user_result[1]

    return jsonify(id_user_result[0]), id_user_result[1]

# ruta para llamar todos los registros de la tabla 'users'
@users_bp.route('/api/users/all', methods=['GET'])
def get_allusers():
    all_users_resutl = User.read_all()

    if 'error' in all_users_resutl:
        return jsonify(all_users_resutl), all_users_resutl[1]

    return jsonify(all_users_resutl[0]), all_users_resutl[1]

# ruta para actualizar un registro en la tabla 'users' por su id
@users_bp.route('/api/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    update_user_result = User.update(id, data)

    if 'error' in update_user_result:
        return jsonify(update_user_result), update_user_result[1]

    return jsonify(update_user_result[0]), update_user_result[1]

# ruta para eliminar un registro de la tabla 'users' por su id
@users_bp.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    delete_user_result = User.delete(id)

    if 'error' in delete_user_result:
        return jsonify(delete_user_result), delete_user_result[1]

    return jsonify(delete_user_result[0]), delete_user_result[1]