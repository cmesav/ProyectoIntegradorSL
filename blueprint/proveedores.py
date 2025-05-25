from flask import Blueprint, request, jsonify
from servicios.servicio_proveedores import ServicioProveedores
from utilidades.autenticacion import requiere_token

proveedores_bp = Blueprint('proveedores_bp', __name__)

@proveedores_bp.route('/proveedores/listar', methods=["GET"])
@requiere_token
def listar_proveedores():
    return jsonify({"Proveedores": ServicioProveedores.listar_proveedores()})

@proveedores_bp.route('/proveedores/insertar', methods=["POST"])
@requiere_token
def insertar_proveedor():
    datos = request.json
    return jsonify(ServicioProveedores.insertar_proveedor(datos["NombreProveedor"], datos["Contacto"]))

@proveedores_bp.route('/proveedores/actualizar', methods=["PUT"])
@requiere_token
def actualizar_proveedor():
    datos = request.json
    return jsonify(ServicioProveedores.actualizar_proveedor(
        datos["IDProveedor"], datos["NombreProveedor"], datos["Contacto"]
    ))

@proveedores_bp.route('/proveedores/eliminar/<int:id_proveedor>', methods=["DELETE"])
@requiere_token
def eliminar_proveedor(id_proveedor):
    return jsonify(ServicioProveedores.eliminar_proveedor(id_proveedor))
