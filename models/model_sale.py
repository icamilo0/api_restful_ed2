from config.conection import db
import pymysql

class Sale:
    # constructor de la clase Sale
    def __init__(self, id, userId, productId, purchaseDate):
        self.id = id
        self.userId = userId
        self.productId = productId
        self.purchaseDate = purchaseDate

    @staticmethod
    # metodo para crear usuarios en la tabla 'sales'
    def create(data):
        cursor = db.cursor()
        try:
            query = '''
                    INSERT INTO sales (userId, productId, purchaseDate)
                    SELECT %s, %s, CURRENT_TIMESTAMP
                    FROM dual
                    WHERE EXISTS (
                        SELECT 1 FROM users WHERE userId = %s AND active = TRUE
                    )
                    AND EXISTS (
                        SELECT 1 FROM products WHERE productId = %s AND active = TRUE
                    );
                    '''
            cursor.execute(query, (data['userId'], data['productId'], data['userId'], data['productId']))
            db.commit()

            if cursor.rowcount > 0:
                return {'message': 'Venta agregada correctamente.'}, 201
            else:
                # maneja los errores relacionados a llaves foraneas en la tabla 'sales'
                return {'error': "No se pudo agregar la venta a la base de datos. Ha ingresado un usuario o producto que no existe."}, 400
        except Exception as e:
            # maneja cualquier otro tipo de error
            return {'error': f'Ha ocurrido un error: {str(e)}'}, 500
        finally:
            cursor.close()

    @staticmethod
    # metodo para llamar un registro en la tabla 'sales' por su id 
    def read(id):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        try:
            query = '''
                    SELECT s.saleId, u.name AS nameuser, p.description AS descproduct, s.purchaseDate
                    FROM sales s
                    JOIN users u ON s.userId = u.userId
                    JOIN products p ON s.productId = p.productId
                    WHERE s.saleId = %s
                    '''
            cursor.execute(query, (id,))
            saleId = cursor.fetchone()

            if saleId:
                return saleId
            else:
                return {'error': 'Registro de venta no encontrado.'}, 404
        except Exception as e:
                # maneja cualquier otro tipo de error
                return {'error': f'Ha ocurrido un error: {str(e)}'}, 500
        finally:
                cursor.close()

    @staticmethod
    # metodo para llamar todos los registros de la tabla 'sales'
    def read_all():
        cursor = db.cursor(pymysql.cursors.DictCursor)
        try:
            query = "SELECT * FROM sales"
            cursor.execute(query)
            all_sales = cursor.fetchall()
            return all_sales, 200
        except Exception as e:
            # maneja cualquier otro tipo de error
            return {'error': f'Ha ocurrido un error: {str(e)}'}, 500
        finally:
            cursor.close()

    @staticmethod
    # metodo para actualizar un registro en la tabla 'sales' por su id
    def update(id, data):
        cursor = db.cursor()
        try:
            query = '''
                    UPDATE sales
                    SET userId = %s, productId = %s, purchaseDate = %s
                    WHERE saleId = %s
                    '''
            cursor.execute(query, (data['userId'], data['productId'], data['purchaseDate'], id))
            db.commit()
            
            if cursor.rowcount > 0:
                return {'message': 'Registro de venta actualizado correctamente.'}, 200
            else:
                return {'error': 'No se encontró el registro de venta para actualizar.'}, 404
        except pymysql.err.IntegrityError as e:
            if "FOREIGN KEY constraint" in str(e):
                # maneja los errores relacionados a llaves foraneas en la tabla 'sales'
                return {'error': "No se pudo actualizar el registro de venta. Ha ingresado un usuario o producto que no existe."}, 400
            else:
                # mensaje generado si se incumple una regla establecida en las columnas de la tabla 'sales'
                return {'error': 'Error al actualizar el registro de venta. Se está violando alguna regla de integridad de la base de datos.'}, 400
        except Exception as e:
            # maneja cualquier otro tipo de error
            return {'error': f'Ha ocurrido un error: {str(e)}'}, 500
        finally:
            cursor.close()

    @staticmethod
    # metodo para eliminar un registro en la tabla 'sales' por su id
    def delete(id):
        cursor = db.cursor()
        try:
            query = "UPDATE sales SET is_deleted = TRUE WHERE saleId = %s AND is_deleted = FALSE"
            cursor.execute(query, (id,))
            db.commit()
            
            if cursor.rowcount > 0:
                return {'message': 'Registro de venta eliminado correctamente.'}, 200
            else:
                return {'error': 'No se encontró el registro de venta para eliminar.'}, 404
        except Exception as e:
            # maneja cualquier otro tipo de error
            return {'error': f'Ha ocurrido un error: {str(e)}'}, 500
        finally:
            cursor.close()