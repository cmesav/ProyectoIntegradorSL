from flask import Blueprint, request, jsonify
from servicios.servicio_direcciones_usuarios import ServicioDireccionesUsuarios
from Utilidades.autenticacion import requiere_token

direcciones_usuarios_bp = Blueprint('direcciones_usuarios_bp', __name__)

@direcciones_usuarios_bp.route('/direcciones_usuarios/listar', methods=["GET"])
@requiere_token
def listar_direcciones_usuarios():
    return jsonify({"DireccionesUsuarios": ServicioDireccionesUsuarios.listar_direcciones_usuarios()})

@direcciones_usuarios_bp.route('/direcciones_usuarios/insertar', methods=["POST"])
@requiere_token
def insertar_direccion_usuario():
    datos = request.json
    return jsonify(ServicioDireccionesUsuarios.insertar_direccion_usuario(
        datos["IDUsuario"], datos["Direccion"]
    ))

@direcciones_usuarios_bp.route('/direcciones_usuarios/actualizar', methods=["PUT"])
@requiere_token
def actualizar_direccion_usuario():
    datos = request.json
    return jsonify(ServicioDireccionesUsuarios.actualizar_direccion_usuario(
        datos["IDDireccion"], datos["IDUsuario"], datos["Direccion"]
    ))

@direcciones_usuarios_bp.route('/direcciones_usuarios/eliminar/<int:id_direccion>', methods=["DELETE"])
@requiere_token
def eliminar_direccion_usuario(id_direccion):
    return jsonify(ServicioDireccionesUsuarios.eliminar_direccion_usuario(id_direccion))
