import pymysql

# conexion a la base de datos
db = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    db="api_restful_ed2"
)