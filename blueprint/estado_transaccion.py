from flask import Blueprint, request, jsonify
from servicios.servicio_estado_transaccion import ServicioEstadoTransaccion
from utilidades.autenticacion import requiere_token

estado_transaccion_bp = Blueprint('estado_transaccion_bp', __name__)

@estado_transaccion_bp.route('/estado_transaccion/listar', methods=["GET"])
@requiere_token
def listar_estados_transaccion():
    return jsonify({"EstadosTransaccion": ServicioEstadoTransaccion.listar_estados_transaccion()})

@estado_transaccion_bp.route('/estado_transaccion/insertar', methods=["POST"])
@requiere_token
def insertar_estado_transaccion():
    datos = request.json
    return jsonify(ServicioEstadoTransaccion.insertar_estado_transaccion(datos["NombreEstado"]))

@estado_transaccion_bp.route('/estado_transaccion/actualizar', methods=["PUT"])
@requiere_token
def actualizar_estado_transaccion():
    datos = request.json
    return jsonify(ServicioEstadoTransaccion.actualizar_estado_transaccion(
        datos["IDEstadoTransaccion"], datos["NombreEstado"]
    ))

@estado_transaccion_bp.route('/estado_transaccion/eliminar/<int:id_estado>', methods=["DELETE"])
@requiere_token
def eliminar_estado_transaccion(id_estado):
    return jsonify(ServicioEstadoTransaccion.eliminar_estado_transaccion(id_estado))
