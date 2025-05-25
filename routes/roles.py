from flask import Blueprint, request, jsonify
from servicios.servicio_roles import ServicioRoles
from Utilidades.autenticacion import requiere_token

roles_bp = Blueprint('roles_bp', __name__)

@roles_bp.route('/roles/listar', methods=["GET"])
@requiere_token
def listar_roles():
    return jsonify({"Roles": ServicioRoles.listar_roles()})

@roles_bp.route('/roles/insertar', methods=["POST"])
@requiere_token
def insertar_rol():
    datos = request.json
    return jsonify(ServicioRoles.insertar_rol(datos["NombreRol"]))

@roles_bp.route('/roles/actualizar', methods=["PUT"])
@requiere_token
def actualizar_rol():
    datos = request.json
    return jsonify(ServicioRoles.actualizar_rol(
        datos["IDRol"], datos["NombreRol"]
    ))

@roles_bp.route('/roles/eliminar/<int:id_rol>', methods=["DELETE"])
@requiere_token
def eliminar_rol(id_rol):
    return jsonify(ServicioRoles.eliminar_rol(id_rol))
