from flask import request, Blueprint, jsonify
from models.model_sale import Sale

sales_bp = Blueprint('model_sale', __name__)

# ruta para agregar usuarios en la tabla 'sales'
@sales_bp.route('/api/sales', methods=['POST'])
def create_sale():
    data = request.json
    create_sale_result = Sale.create(data)

    if 'error' in create_sale_result:
        return jsonify(create_sale_result), create_sale_result[1]

    return jsonify(create_sale_result[0]), create_sale_result[1]

# ruta para llamar un registro de la tabla 'sales' por el id
@sales_bp.route('/api/sales/<int:id>', methods=['GET'])
def get_sale(id):
    id_sale_result = Sale.read(id)

    if 'error' in id_sale_result:
        return jsonify(id_sale_result), id_sale_result[1]

    return jsonify(id_sale_result[0]), id_sale_result[1]

# ruta para llamar todos los registros de la tabla 'sales'
@sales_bp.route('/api/sales/all', methods=['GET'])
def get_allsales():
    all_sales_result = Sale.read_all()

    if 'error' in all_sales_result:
        return jsonify(all_sales_result), all_sales_result[1]

    return jsonify(all_sales_result[0]), all_sales_result[1]

# ruta para actualizar un registro en la tabla 'sales' por su id
@sales_bp.route('/api/sales/<int:id>', methods=['PUT'])
def update_sale(id):
    data = request.json
    update_sale_result = Sale.update(id, data)

    if 'error' in update_sale_result:
        return jsonify(update_sale_result), update_sale_result[1]

    return jsonify(update_sale_result[0]), update_sale_result[1]

# ruta para eliminar un registro de la tabla 'sales' por su id
@sales_bp.route('/api/sales/<int:id>', methods=['DELETE'])
def delete_sale(id):
    delete_user_result = Sale.delete(id)

    if 'error' in delete_user_result:
        return jsonify(delete_user_result), delete_user_result[1]

    return jsonify(delete_user_result[0]), delete_user_result[1]