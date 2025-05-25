from flask import Blueprint, request, jsonify
from servicios.servicio_inventario import ServicioInventario
from utilidades.autenticacion import requiere_token

inventario_bp = Blueprint('inventario_bp', __name__)

@inventario_bp.route('/inventario/listar', methods=["GET"])
@requiere_token
def listar_inventario():
    return jsonify({"Inventario": ServicioInventario.listar_inventario()})

@inventario_bp.route('/inventario/insertar', methods=["POST"])
@requiere_token
def insertar_inventario():
    datos = request.json
    return jsonify(ServicioInventario.insertar_inventario(
        datos["IDProducto"], datos["CantidadDisponible"]
    ))

@inventario_bp.route('/inventario/actualizar', methods=["PUT"])
@requiere_token
def actualizar_inventario():
    datos = request.json
    return jsonify(ServicioInventario.actualizar_inventario(
        datos["IDProducto"], datos["CantidadDisponible"]
    ))

@inventario_bp.route('/inventario/eliminar/<int:id_producto>', methods=["DELETE"])
@requiere_token
def eliminar_inventario(id_producto):
    return jsonify(ServicioInventario.eliminar_inventario(id_producto))
