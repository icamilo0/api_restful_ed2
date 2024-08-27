from flask import Flask
from routes.routes_product import products_bp
from routes.routes_sale import sales_bp
from routes.routes_user import users_bp
from routes.routes_admin import admins_bp

app = Flask(__name__)

app.register_blueprint(products_bp)
app.register_blueprint(sales_bp)
app.register_blueprint(users_bp)
app.register_blueprint(admins_bp)

if __name__ == '__main__':
    app.run(debug=True)