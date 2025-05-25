from flask import Blueprint, request, jsonify
from servicios.servicio_historial_precios import ServicioHistorialPrecios
from Utilidades.autenticacion import requiere_token

historial_precios_bp = Blueprint('historial_precios_bp', __name__)

@historial_precios_bp.route('/historial_precios/listar', methods=["GET"])
@requiere_token
def listar_historial_precios():
    return jsonify({"HistorialPrecios": ServicioHistorialPrecios.listar_historial_precios()})

@historial_precios_bp.route('/historial_precios/insertar', methods=["POST"])
@requiere_token
def insertar_historial_precio():
    datos = request.json
    return jsonify(ServicioHistorialPrecios.insertar_historial_precio(
        datos["IDProducto"], datos["Fecha"], datos["PrecioAntiguo"], datos["PrecioNuevo"]
    ))

@historial_precios_bp.route('/historial_precios/actualizar', methods=["PUT"])
@requiere_token
def actualizar_historial_precio():
    datos = request.json
    return jsonify(ServicioHistorialPrecios.actualizar_historial_precio(
        datos["IDHistorial"], datos["Fecha"], datos["PrecioAntiguo"], datos["PrecioNuevo"]
    ))

@historial_precios_bp.route('/historial_precios/eliminar/<int:id_historial>', methods=["DELETE"])
@requiere_token
def eliminar_historial_precio(id_historial):
    return jsonify(ServicioHistorialPrecios.eliminar_historial_precio(id_historial))
