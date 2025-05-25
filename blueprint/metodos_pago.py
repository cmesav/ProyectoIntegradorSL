from flask import Blueprint, request, jsonify
from servicios.servicio_metodos_pago import ServicioMetodosPago
from utilidades.autenticacion import requiere_token

metodos_pago_bp = Blueprint('metodos_pago_bp', __name__)

@metodos_pago_bp.route('/metodos_pago/listar', methods=["GET"])
@requiere_token
def listar_metodos_pago():
    return jsonify({"MetodosPago": ServicioMetodosPago.listar_metodos_pago()})

@metodos_pago_bp.route('/metodos_pago/insertar', methods=["POST"])
@requiere_token
def insertar_metodo_pago():
    datos = request.json
    return jsonify(ServicioMetodosPago.insertar_metodo_pago(datos["NombreMetodo"]))

@metodos_pago_bp.route('/metodos_pago/actualizar', methods=["PUT"])
@requiere_token
def actualizar_metodo_pago():
    datos = request.json
    return jsonify(ServicioMetodosPago.actualizar_metodo_pago(
        datos["IDMetodoPago"], datos["NombreMetodo"]
    ))

@metodos_pago_bp.route('/metodos_pago/eliminar/<int:id_metodo>', methods=["DELETE"])
@requiere_token
def eliminar_metodo_pago(id_metodo):
    return jsonify(ServicioMetodosPago.eliminar_metodo_pago(id_metodo))
