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
                # para guardar un acceso exitoso en la base de datos
                Admin.accessHistory(admin_result['adminId'], 'success')
                return admin_result, 200
            else:
                Admin.accessHistory(None, 'failure', data['user'])
                return {'error': 'Usuario o contraseña incorrecta.'}, 404
        except Exception as e:
            # maneja cualquier otro tipo de error
            return {'error': f'Ha ocurrido un error: {str(e)}'}, 500
        finally:
            cursor.close()

    @staticmethod
    # metodo para agregar a la tabla "accesshistory" los registros cuando se intente loguear
    def accessHistory(adminId, state, user = None):
        cursor = db.cursor()
        try:
            if adminId:
                query = "INSERT INTO accesshistory (adminId, state) VALUES (%s, %s)"
                cursor.execute(query, (adminId, state))
            else:
                query = "INSERT INTO accesshistory (adminId, state) VALUES (NULL, %s)"
                cursor.execute(query, (state,))
            db.commit()
        except Exception as e:
            db.rollback()
            print(f"Error al registrar el acceso: {str(e)}")