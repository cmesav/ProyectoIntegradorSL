from flask import Blueprint, request, jsonify
from servicios.servicio_productos import ServicioProductos
from utilidades.autenticacion import requiere_token

productos_bp = Blueprint('productos_bp', __name__)

@productos_bp.route('/productos/listar', methods=["GET"])
@requiere_token
def listar_productos():
    return jsonify({"Productos": ServicioProductos.listar_productos()})

@productos_bp.route('/productos/listar_con_categoria', methods=["GET"])
@requiere_token
def listar_productos_con_categoria():
    return jsonify({"ProductosConCategoria": ServicioProductos.listar_productos_con_categoria()})

@productos_bp.route('/productos/insertar', methods=["POST"])
@requiere_token
def insertar_producto():
    datos = request.json
    return jsonify(ServicioProductos.insertar_producto(
        datos["NombreProducto"], datos["IDCategoria"], datos["Precio"]
    ))

@productos_bp.route('/productos/actualizar', methods=["PUT"])
@requiere_token
def actualizar_producto():
    datos = request.json
    return jsonify(ServicioProductos.actualizar_producto(
        datos["IDProducto"], datos["NombreProducto"], datos["IDCategoria"], datos["Precio"]
    ))

@productos_bp.route('/productos/eliminar/<int:id_producto>', methods=["DELETE"])
@requiere_token
def eliminar_producto(id_producto):
    return jsonify(ServicioProductos.eliminar_producto(id_producto))
