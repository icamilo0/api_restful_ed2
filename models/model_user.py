from config.conection import db
import pymysql

class User:
    # constructor de la clase User
    def __init__(self, id, name, documentId):
        self.id = id
        self.name = name
        self.documentId = documentId

    @staticmethod
    # metodo para agregar usuarios en la tabla 'users'
    def create(data):
        cursor = db.cursor()
        try:
            query = "INSERT INTO users (name, documentId) VALUES (%s, %s)"
            cursor.execute(query, (data['name'], data['documentId'],))
            db.commit()
            return {{'message': 'Usuario agregado con exito.'}}, 201
        except pymysql.err.IntegrityError as e:
            # maneja la configuracion de la columna 'documentId' establecida como valor unico en la tabla 'users'
            if "UNIQUE constraint" in str(e):
                return{'error': "El número de documento ya existe. Use otro diferente."}, 400
            # mensaje generado si se incumple una regla establecida en las columnas de la tabla 'users'
            else:
                return {'error': 'Error al agregar el usuario. Se está violando alguna regla de integridad de la base de datos.'}, 400
        except Exception as e:
            # maneja cualquier otro tipo de error
            return {'error': f'Ha ocurrido un error: {str(e)}'}, 500
        finally:
            cursor.close()

    @staticmethod
    # metodo para llamar un registro en la tabla 'users' por su id 
    def read(id):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        try:
            query = "SELECT * FROM users WHERE userId = %s AND active = TRUE"
            cursor.execute(query, (id,))
            userId = cursor.fetchone()

            if userId:
                return userId, 200
            else:
                return {'error': 'Usuario no encontrado.'}, 404
        except Exception as e:
            # maneja cualquier otro tipo de error
            return {'error': f'Ha ocurrido un error: {str(e)}'}, 500
        finally:
            cursor.close()

    @staticmethod
    # metodo para llamar todos los registros de la tabla 'users'
    def read_all():
        cursor = db.cursor(pymysql.cursors.DictCursor)
        try:
            query = "SELECT * FROM users WHERE active = TRUE"
            cursor.execute(query)
            all_users = cursor.fetchall()
            return all_users, 200
        except Exception as e:
            # maneja cualquier otro tipo de error
            return {'error': f'Ha ocurrido un error: {str(e)}'}, 500
        finally:
            cursor.close()

    @staticmethod
    # metodo para actualizar un registro en la tabla 'users' por su id 
    def update(id, data):
        cursor = db.cursor()
        try:
            query = "UPDATE users SET name = %s, documentId = %s WHERE userId = %s"
            cursor.execute(query, (data['name'], data['documentId'], id))
            db.commit()

            if cursor.rowcount > 0:
                return {'message': 'Usuario actualizado correctamente.'}, 200
            else:
                return {'error': 'No se encontró el usuario para actualizar.'}, 404
        except pymysql.err.IntegrityError as e:
            if "UNIQUE constraint" in str(e):
                return{'error': "El número de documento ya existe. Use otro diferente."}, 400
            else:
                return {'error': 'Error al actualizar el usuario.Se está violando alguna regla de integridad de la base de datos.'}, 400
        except Exception as e:
            # maneja cualquier otro tipo de error
            return {'error': f'Ha ocurrido un error: {str(e)}'}, 500
        finally:
            cursor.close()

    @staticmethod
    # metodo para eliminar un registro en la tabla 'users' por su id
    def delete(id):
        cursor = db.cursor()
        try:
            query = "UPDATE users SET active = FALSE WHERE userId = %s AND active = TRUE"
            cursor.execute(query, (id,))
            db.commit()

            if cursor.rowcount > 0:
                return {'message': 'Usuario eliminado exitosamente.'}, 200
            else:
                return {'error': 'No se encontró el usuario para eliminar'}, 404
        except Exception as e:
            # maneja cualquier otro tipo de error
            return {'error': f'Ha ocurrido un error: {str(e)}'}, 500
        finally:
            cursor.close()