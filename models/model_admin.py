from config.conection import db
import pymysql

class Admin:
    # constructor de la clase Admin
    def __init__(self, id, user, password):
        self.id = id
        self.user = user
        self.password = password

    @staticmethod
    # metodo para autenticar los datos ingresados en el login
    def authenticate(data):
        cursor = db.cursor(pymysql.cursors.DictCursor)
        try:
            query = "SELECT * FROM admins WHERE user = %s AND password = %s AND active = TRUE"
            cursor.execute(query, (data['user'], data['password']))

            admin_result = cursor.fetchone()

            if admin_result:
                return admin_result, 200
            else:
                return {'error': 'Usuario o contraseña incorrecta.'}, 404
        except Exception as e:
            # maneja cualquier otro tipo de error
            return {'error': f'Ha ocurrido un error: {str(e)}'}, 500
        finally:
            cursor.close()