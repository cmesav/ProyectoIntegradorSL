from flask import Blueprint, request, jsonify
from servicios.servicio_notificaciones import ServicioNotificaciones
from utilidades.autenticacion import requiere_token

notificaciones_bp = Blueprint('notificaciones_bp', __name__)

@notificaciones_bp.route('/notificaciones/listar', methods=["GET"])
@requiere_token
def listar_notificaciones():
    return jsonify({"Notificaciones": ServicioNotificaciones.listar_notificaciones()})

@notificaciones_bp.route('/notificaciones/insertar', methods=["POST"])
@requiere_token
def insertar_notificacion():
    datos = request.json
    return jsonify(ServicioNotificaciones.insertar_notificacion(
        datos["IDUsuario"], datos["Mensaje"], datos["Fecha"]
    ))

@notificaciones_bp.route('/notificaciones/actualizar', methods=["PUT"])
@requiere_token
def actualizar_notificacion():
    datos = request.json
    return jsonify(ServicioNotificaciones.actualizar_notificacion(
        datos["IDNotificacion"], datos["Mensaje"], datos["Fecha"]
    ))

@notificaciones_bp.route('/notificaciones/eliminar/<int:id_notificacion>', methods=["DELETE"])
@requiere_token
def eliminar_notificacion(id_notificacion):
    return jsonify(ServicioNotificaciones.eliminar_notificacion(id_notificacion))
