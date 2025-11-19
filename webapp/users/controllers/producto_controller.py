from flask import Blueprint, request, jsonify
from users.models.producto_model import Productos
from users.models.db import db

producto_controller = Blueprint('producto_controller', __name__)

@producto_controller.route('/api/productos', methods=['GET'])
def get_productos():
    print("listado de productos")
    productos = Productos.query.all()
    result = [{'id':producto.id, 'nombre': producto.nombre, 'descripcion': producto.descripcion, 'precio': producto.precio, 'cantidad': producto.cantidad} for producto in productos]
    return jsonify(result)

# Get single producto by id
@producto_controller.route('/api/productos/<int:producto_id>', methods=['GET'])
def get_producto(producto_id):
    print("obteniendo producto")
    producto = Productos.query.get_or_404(producto_id)
    return jsonify({'id': producto.id, 'nombre': producto.nombre, 'descripcion': producto.descripcion, 'precio': producto.precio, 'cantidad': producto.cantidad})

@producto_controller.route('/api/productos', methods=['POST'])
def create_producto():
    print("creando producto")
    data = request.json
    #new_producto = Users(name="oscar", email="oscar@gmail", productoname="omondragon", password="123")
    new_producto = Productos(nombre=data['nombre'], descripcion=data['descripcion'], precio=data['precio'], cantidad=data['cantidad'])
    db.session.add(new_producto)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201

# Update an existing producto
@producto_controller.route('/api/productos/<int:producto_id>', methods=['PUT'])
def update_producto(producto_id):
    print("actualizando producto")
    producto = Productos.query.get_or_404(producto_id)
    data = request.json
    producto.nombre = data['nombre']
    producto.descripcion = data['descripcion']
    producto.precio = data['precio']
    producto.cantidad = data['cantidad']
    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})

# Delete an existing producto
@producto_controller.route('/api/productos/<int:producto_id>', methods=['DELETE'])
def delete_producto(producto_id):
    producto = Productos.query.get_or_404(producto_id)
    db.session.delete(producto)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})
