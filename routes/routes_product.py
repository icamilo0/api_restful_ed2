from flask import request, Blueprint, jsonify
from models.model_product import Product

products_bp = Blueprint('model_product', __name__)

# ruta para agregar usuarios en la tabla 'products'
@products_bp.route('/api/products', methods=['POST'])
def create_product():
    data = request.json
    create_product_result = Product.create(data)

    if 'error' in create_product_result:
        return jsonify(create_product_result), create_product_result[1]

    return jsonify(create_product_result[0]), create_product_result[1]

# ruta para llamar un registro de la tabla 'products' por el id
@products_bp.route('/api/products/<int:id>', methods=['GET'])
def get_product(id):
    id_product_result = Product.read(id)

    if 'error' in id_product_result:
        return jsonify(id_product_result), id_product_result[1]

    return jsonify(id_product_result[0]), id_product_result[1]

# ruta para llamar todos los registros de la tabla 'products'
@products_bp.route('/api/products/all', methods=['GET'])
def get_allproducts():
    all_products_result = Product.read_all()

    if 'error' in all_products_result:
        return jsonify(all_products_result), all_products_result[1]

    return jsonify(all_products_result[0]), all_products_result[1]

# ruta para actualizar un registro en la tabla 'products' por su id
@products_bp.route('/api/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    update_product_result = Product.update(id, data)

    if 'error' in update_product_result:
        return jsonify(update_product_result), update_product_result[1]

    return jsonify(update_product_result[0]), update_product_result[1]

# ruta para eliminar un registro de la tabla 'products' por su id
@products_bp.route('/api/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    delete_product_result = Product.delete(id)

    if 'error' in delete_product_result:
        return jsonify(delete_product_result), delete_product_result[1]

    return jsonify(delete_product_result[0]), delete_product_result[1]