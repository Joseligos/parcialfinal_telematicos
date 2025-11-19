# web/views.py
from flask import Flask, render_template
from users.controllers.user_controller import user_controller
from users.models.db import db
from users.controllers.producto_controller import producto_controller
from config import Config
import time
import os
from mysql.connector import connect, Error

def wait_for_mysql():
    host = os.getenv('MYSQL_HOST', 'db')
    user = os.getenv('MYSQL_USER', 'flaskuser')
    password = os.getenv('MYSQL_PASSWORD', 'flaskpass')
    database = os.getenv('MYSQL_DB', 'myflaskapp')
    
    print("Esperando a que MySQL esté listo...")
    for _ in range(30):  # 30 intentos
        try:
            with connect(
                host=host,
                user=user,
                password=password,
                database=database
            ) as connection:
                print("MySQL conectado! Creando tablas...")
                return
        except Error as e:
            print(f"MySQL no listo aún... reintentando en 1s ({e})")
            time.sleep(1)
    raise Exception("No se pudo conectar a MySQL después de 30 segundos")

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Registrar Blueprints
    app.register_blueprint(user_controller)
    app.register_blueprint(producto_controller)

    # Rutas
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/edit/<string:id>')
    def edit_user(id):
        print("id recibido:", id)
        return render_template('edit.html', id=id)

    @app.route('/productos')
    def productos_page():
        return render_template('productos.html')

    @app.route('/edit_producto/<int:id>')
    def edit_producto(id):
        print("id recibido:", id)
        return render_template('edit_producto.html', id=id)

    # ESPERAR A MYSQL ANTES DE CREAR TABLAS
    with app.app_context():
        wait_for_mysql()
        db.create_all()

    return app

# Solo para desarrollo local
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
