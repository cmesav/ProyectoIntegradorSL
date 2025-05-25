from flask import Blueprint, request, jsonify
from servicios.servicio_detalles_transaccion import ServicioDetallesTransaccion
from utilidades.autenticacion import requiere_token

detalles_transaccion_bp = Blueprint('detalles_transaccion_bp', __name__)

@detalles_transaccion_bp.route('/detalles_transaccion/listar', methods=["GET"])
@requiere_token
def listar_detalles_transaccion():
    return jsonify({"DetallesTransaccion": ServicioDetallesTransaccion.listar_detalles_transaccion()})

@detalles_transaccion_bp.route('/detalles_transaccion/insertar', methods=["POST"])
@requiere_token
def insertar_detalle_transaccion():
    datos = request.json
    return jsonify(ServicioDetallesTransaccion.insertar_detalle_transaccion(
        datos["IDTransaccion"], datos["IDProducto"], datos["Cantidad"]
    ))

@detalles_transaccion_bp.route('/detalles_transaccion/actualizar', methods=["PUT"])
@requiere_token
def actualizar_detalle_transaccion():
    datos = request.json
    return jsonify(ServicioDetallesTransaccion.actualizar_detalle_transaccion(
        datos["ID"], datos["IDTransaccion"], datos["IDProducto"], datos["Cantidad"]
    ))

@detalles_transaccion_bp.route('/detalles_transaccion/eliminar/<int:id_detalle>', methods=["DELETE"])
@requiere_token
def eliminar_detalle_transaccion(id_detalle):
    return jsonify(ServicioDetallesTransaccion.eliminar_detalle_transaccion(id_detalle))
