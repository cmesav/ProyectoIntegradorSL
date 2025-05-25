from flask import Blueprint, request, jsonify
from servicios.servicio_transacciones import ServicioTransacciones
from Utilidades.autenticacion import requiere_token

transacciones_bp = Blueprint('transacciones_bp', __name__)

@transacciones_bp.route('/transacciones/listar', methods=["GET"])
@requiere_token
def listar_transacciones():
    return jsonify({"Transacciones": ServicioTransacciones.listar_transacciones()})

@transacciones_bp.route('/transacciones/insertar', methods=["POST"])
@requiere_token
def insertar_transaccion():
    datos = request.json
    return jsonify(ServicioTransacciones.insertar_transaccion(
        datos["IDUsuario"], datos["Fecha"], datos["IDMetodoPago"], datos["IDEstadoTransaccion"]
    ))

@transacciones_bp.route('/transacciones/actualizar', methods=["PUT"])
@requiere_token
def actualizar_transaccion():
    datos = request.json
    return jsonify(ServicioTransacciones.actualizar_transaccion(
        datos["IDTransaccion"], datos["Fecha"], datos["IDMetodoPago"], datos["IDEstadoTransaccion"]
    ))

@transacciones_bp.route('/transacciones/eliminar/<int:id_transaccion>', methods=["DELETE"])
@requiere_token
def eliminar_transaccion(id_transaccion):
    return jsonify(ServicioTransacciones.eliminar_transaccion(id_transaccion))
