from flask import Blueprint, request, jsonify
from servicios.servicio_categorias import ServicioCategorias
from Utilidades.autenticacion import requiere_token

categorias_bp = Blueprint('categorias_bp', __name__)

@categorias_bp.route('/categorias/listar', methods=["GET"])
@requiere_token
def listar_categorias():
    return jsonify({"Categorias": ServicioCategorias.listar_categorias()})

@categorias_bp.route('/categorias/insertar', methods=["POST"])
@requiere_token
def insertar_categoria():
    datos = request.json
    return jsonify(ServicioCategorias.insertar_categoria(datos["NombreCategoria"]))

@categorias_bp.route('/categorias/actualizar', methods=["PUT"])
@requiere_token
def actualizar_categoria():
    datos = request.json
    return jsonify(ServicioCategorias.actualizar_categoria(datos["IDCategoria"], datos["NombreCategoria"]))

@categorias_bp.route('/categorias/eliminar/<int:id_categoria>', methods=["DELETE"])
@requiere_token
def eliminar_categoria(id_categoria):
    return jsonify(ServicioCategorias.eliminar_categoria(id_categoria))
