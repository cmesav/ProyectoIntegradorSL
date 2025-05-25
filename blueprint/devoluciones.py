from flask import Blueprint, request, jsonify
from servicios.servicio_devoluciones import ServicioDevoluciones
from utilidades.autenticacion import requiere_token

devoluciones_bp = Blueprint('devoluciones_bp', __name__)

@devoluciones_bp.route('/devoluciones/listar', methods=["GET"])
@requiere_token
def listar_devoluciones():
    return jsonify({"Devoluciones": ServicioDevoluciones.listar_devoluciones()})

@devoluciones_bp.route('/devoluciones/insertar', methods=["POST"])
@requiere_token
def insertar_devolucion():
    datos = request.json
    return jsonify(ServicioDevoluciones.insertar_devolucion(
        datos["IDTransaccion"], datos["Motivo"], datos["Fecha"]
    ))

@devoluciones_bp.route('/devoluciones/actualizar', methods=["PUT"])
@requiere_token
def actualizar_devolucion():
    datos = request.json
    return jsonify(ServicioDevoluciones.actualizar_devolucion(
        datos["ID"], datos["IDTransaccion"], datos["Motivo"], datos["Fecha"]
    ))

@devoluciones_bp.route('/devoluciones/eliminar/<int:id_devolucion>', methods=["DELETE"])
@requiere_token
def eliminar_devolucion(id_devolucion):
    return jsonify(ServicioDevoluciones.eliminar_devolucion(id_devolucion))
