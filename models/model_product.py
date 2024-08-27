from config.conection import db
import pymysql

class Product:
    # constructor de la clase Product
    def __init__(self, id, description, cost):
        self.id = id
        self.description = description
        self.cost = cost

    @staticmethod
    # metodo para crear usuarios en la tabla 'products'
    def create(data):
        cursor = db.cursor()
        try:
            query = "INSERT INTO products (description, cost) VALUES (%s, %s)"
            cursor.execute(query, (data['description'], data['cost']))
            db.commit()
            return {'message': 'Producto agregado con exito.'} , 201
        except pymysql.err.IntegrityError as e:
            # mensaje generado si se incumple una regla establecida en las columnas de la tabla 'products'
            return {'error': 'Error al agregar el producto. Se está violando alguna regla de integridad de la base de datos.'}, 400
        except Exception as e:
            # maneja cualquier otro tipo de error
            return {'error': f'Ha ocurrido un error: {str(e)}'}, 500
        finally:
            cursor.close()

    @staticmethod
    # metodo para llamar un registro en la tabla 'products' por su id 
    def read(id):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        try:
            query = "SELECT * FROM products WHERE productId = %s"
            cursor.execute(query, (id,))
            productId = cursor.fetchone()

            if productId:
                return productId, 200
            else:
                return {'error': 'Producto no encontrado.'}, 404
        except Exception as e:
            # maneja cualquier otro tipo de error
            return {'error': f'Ha ocurrido un error: {str(e)}'}, 500
        finally:
            cursor.close()

    @staticmethod
    # metodo para llamar todos los registros de la tabla 'products'
    def read_all():
        cursor = db.cursor(pymysql.cursors.DictCursor)
        try:
            query = "SELECT * FROM products"
            cursor.execute(query)
            all_products = cursor.fetchall()
            return all_products, 200
        except Exception as e:
            # maneja cualquier otro tipo de error
            return {'error': f'Ha ocurrido un error: {str(e)}'}, 500
        finally:
            cursor.close()

    @staticmethod
    # metodo para actualizar un registro en la tabla 'products' por su id
    def update(id, data):
        cursor = db.cursor()
        try:
            query = "UPDATE products SET description = %s, cost = %s WHERE productId = %s"
            cursor.execute(query, (data['description'], data['cost'], id))
            db.commit()
            
            if cursor.rowcount > 0:
                return {'message': 'Producto actualizado correctamente.'}, 200
            else:
                return {'error': 'Producto no encontrado.'}, 404
        except pymysql.err.IntegrityError as e:
            return {'error': 'Error al actualizar el producto. Se está violando alguna regla de integridad de la base de datos.'}, 400
        except Exception as e:
            # maneja cualquier otro tipo de error
            return {'error': f'Ha ocurrido un error: {str(e)}'}, 500
        finally:
            cursor.close()
    
    @staticmethod
    # metodo para eliminar un registro en la tabla 'products' por su id
    def delete(id):
        cursor = db.cursor()
        try:            
            query = "UPDATE products SET active = FALSE WHERE productId = %s AND active = TRUE"
            cursor.execute(query, (id,))
            db.commit()
            
            if cursor.rowcount > 0:
                return {'message': 'Producto eliminado exitosamente.'}, 200
            else:
                return {'error': 'No se encontró el producto para eliminar'}, 404
        except Exception as e:
            # maneja cualquier otro tipo de error
            return {'error': f'Ha ocurrido un error: {str(e)}'}, 500
        finally:
            cursor.close()