from flask import Blueprint, request, jsonify
from servicios.servicio_usuarios import ServicioUsuarios
from Utilidades.autenticacion import requiere_token

usuarios_bp = Blueprint('usuarios_bp', __name__)

@usuarios_bp.route('/usuarios/listar', methods=["GET"])
@requiere_token
def listar_usuarios():
    return jsonify({"Usuarios": ServicioUsuarios.listar_usuarios()})

@usuarios_bp.route('/usuarios/insertar', methods=["POST"])
@requiere_token
def insertar_usuario():
    datos = request.json
    return jsonify(ServicioUsuarios.insertar_usuario(
        datos["Nombre"], datos["Correo"], datos["Contrasena"], datos["IDRol"]
    ))

@usuarios_bp.route('/usuarios/actualizar', methods=["PUT"])
@requiere_token
def actualizar_usuario():
    datos = request.json
    return jsonify(ServicioUsuarios.actualizar_usuario(
        datos["ID"], datos["Nombre"], datos["Correo"], datos["Contrasena"]
    ))

@usuarios_bp.route('/usuarios/eliminar/<int:id_usuario>', methods=["DELETE"])
@requiere_token
def eliminar_usuario(id_usuario):
    return jsonify(ServicioUsuarios.eliminar_usuario(id_usuario))
