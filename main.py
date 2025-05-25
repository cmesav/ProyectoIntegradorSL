from flask import Flask, request, jsonify
from Repositorios.RepositorioUsuarios import RepositorioUsuarios
from Repositorios.RepositorioTransacciones import RepositorioTransacciones
from Repositorios.RepositorioProductos import RepositorioProductos
from Repositorios.RepositorioProveedores import RepositorioProveedores
from Repositorios.RepositorioRoles import RepositorioRoles
from Repositorios.RepositorioMetodosPago import RepositorioMetodosPago
from Repositorios.RepositorioInventario import RepositorioInventario
from Repositorios.RepositorioHistorialPrecios import RepositorioHistorialPrecios
from Repositorios.RepositorioEstadoTransaccion import RepositorioEstadoTransaccion
from Repositorios.RepositorioDireccionesUsuarios import RepositorioDireccionesUsuarios
from Repositorios.RepositorioDevoluciones import RepositorioDevoluciones
from Repositorios.RepositorioDetallesTransaccion import RepositorioDetallesTransaccion
from Repositorios.RepositorioCategorias import RepositorioCategorias
from Repositorios.RepositorioNotificaciones import RepositorioNotificaciones
from Utilidades.JWTEncriptador import JWTEncriptador

app = Flask(__name__)  
app.config['JSON_SORT_KEYS'] = False

jwt_encriptador = JWTEncriptador()
jwt_encriptador.SetClave("12346467987987")


@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if data.get('username') == 'admin' and data.get('password') == 'admin123':
            token = jwt_encriptador.GenerarToken({'user': 'admin'})
            return jsonify({'token': token})
        return jsonify({'error': 'Credenciales inválidas'}), 401
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

def validar_token(token):
    datos = jwt_encriptador.DecodificarToken(token)
    return datos is not None

from functools import wraps

def requiere_token(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if not validar_token(token):
            return jsonify({'error': 'No autenticado'}), 401
        return f(*args, **kwargs)
    return decorador

@app.route('/usuarios/listar', methods=["GET"])
@requiere_token
def listar_usuarios():
    return jsonify({"Usuarios": RepositorioUsuarios.listar_usuarios()})

@app.route('/usuarios/insertar', methods=["POST"])
@requiere_token
def insertar_usuario():
    datos = request.json
    return jsonify(RepositorioUsuarios.insertar_usuario(
        datos["Nombre"], datos["Correo"], datos["Contrasena"], datos["IDRol"]
    ))

@app.route('/usuarios/actualizar', methods=["PUT"])
@requiere_token
def actualizar_usuario():
    datos = request.json
    return jsonify(RepositorioUsuarios.actualizar_usuario(
        datos["ID"], datos["Nombre"], datos["Correo"], datos["Contrasena"]
    ))

@app.route('/usuarios/eliminar/<int:id_usuario>', methods=["DELETE"])
@requiere_token
def eliminar_usuario(id_usuario):
    return jsonify(RepositorioUsuarios.eliminar_usuario(id_usuario))


@app.route('/transacciones/listar', methods=["GET"])
@requiere_token
def listar_transacciones():
    return jsonify({"Transacciones": RepositorioTransacciones.listar_transacciones()})

@app.route('/transacciones/insertar', methods=["POST"])
@requiere_token
def insertar_transaccion():
    datos = request.json
    return jsonify(RepositorioTransacciones.insertar_transaccion(datos["IDUsuario"], datos["Fecha"], datos["IDMetodoPago"], datos["IDEstadoTransaccion"]))

@app.route('/transacciones/actualizar', methods=["PUT"])
@requiere_token
def actualizar_transaccion():
    datos = request.json
    return jsonify(RepositorioTransacciones.actualizar_transaccion(datos["ID"], datos["Fecha"], datos["IDMetodoPago"], datos["IDEstadoTransaccion"]))

@app.route('/transacciones/eliminar/<int:id_transaccion>', methods=["DELETE"])
@requiere_token
def eliminar_transaccion(id_transaccion):
    return jsonify(RepositorioTransacciones.eliminar_transaccion(id_transaccion))

@app.route('/productos/listar', methods=["GET"])
@requiere_token
def listar_productos():
    return jsonify({"Productos": RepositorioProductos.listar_productos()})

@app.route('/productos/insertar', methods=["POST"])
@requiere_token
def insertar_producto():
    datos = request.json
    return jsonify(RepositorioProductos.insertar_producto(datos["Nombre"], datos["IDCategoria"], datos["Precio"]))

@app.route('/productos/actualizar', methods=["PUT"])
@requiere_token
def actualizar_producto():
    datos = request.json
    return jsonify(RepositorioProductos.actualizar_producto(
        datos["ID"], datos["Nombre"], datos["IDCategoria"], datos["Precio"]
    ))

@app.route('/productos/eliminar/<int:id_producto>', methods=["DELETE"])
@requiere_token
def eliminar_producto(id_producto):
    return jsonify(RepositorioProductos.eliminar_producto(id_producto))


@app.route('/proveedores/listar', methods=["GET"])
@requiere_token
def listar_proveedores():
    return jsonify({"Proveedores": RepositorioProveedores.listar_proveedores()})

@app.route('/proveedores/insertar', methods=["POST"])
@requiere_token
def insertar_proveedor():
    datos = request.json
    return jsonify(RepositorioProveedores.insertar_proveedor(datos["NombreProveedor"], datos["Contacto"]))

@app.route('/proveedores/actualizar', methods=["PUT"])
@requiere_token
def actualizar_proveedor():
    datos = request.json
    return jsonify(RepositorioProveedores.actualizar_proveedor(
        datos["ID"], datos["NombreProveedor"], datos["Contacto"]
    ))

@app.route('/proveedores/eliminar/<int:id_proveedor>', methods=["DELETE"])
@requiere_token
def eliminar_proveedor(id_proveedor):
    return jsonify(RepositorioProveedores.eliminar_proveedor(id_proveedor))


@app.route('/roles/listar', methods=["GET"])
@requiere_token
def listar_roles():
    return jsonify({"Roles": RepositorioRoles.listar_roles()})

@app.route('/roles/insertar', methods=["POST"])
@requiere_token
def insertar_rol():
    datos = request.json
    return jsonify(RepositorioRoles.insertar_rol(datos["NombreRol"]))

@app.route('/roles/actualizar', methods=["PUT"])
@requiere_token
def actualizar_rol():
    datos = request.json
    return jsonify(RepositorioRoles.actualizar_rol(
        datos["ID"], datos["NombreRol"]
    ))

@app.route('/roles/eliminar/<int:id_rol>', methods=["DELETE"])
@requiere_token
def eliminar_rol(id_rol):
    return jsonify(RepositorioRoles.eliminar_rol(id_rol))


@app.route('/metodos_pago/listar', methods=["GET"])
@requiere_token
def listar_metodos_pago():
    return jsonify({"MetodosPago": RepositorioMetodosPago.listar_metodos_pago()})

@app.route('/metodos_pago/insertar', methods=["POST"])
@requiere_token
def insertar_metodo_pago():
    datos = request.json
    return jsonify(RepositorioMetodosPago.insertar_metodo_pago(datos["NombreMetodo"]))

@app.route('/metodos_pago/actualizar', methods=["PUT"])
@requiere_token
def actualizar_metodo_pago():
    datos = request.json
    return jsonify(RepositorioMetodosPago.actualizar_metodo_pago(
        datos["ID"], datos["NombreMetodo"]
    ))

@app.route('/metodos_pago/eliminar/<int:id_metodo>', methods=["DELETE"])
@requiere_token
def eliminar_metodo_pago(id_metodo):
    return jsonify(RepositorioMetodosPago.eliminar_metodo_pago(id_metodo))

@app.route('/inventario/listar', methods=["GET"])
@requiere_token
def listar_inventario():
    return jsonify({"Inventario": RepositorioInventario.listar_inventario()})

@app.route('/inventario/insertar', methods=["POST"])
@requiere_token
def agregar_inventario():
    datos = request.json
    return jsonify(RepositorioInventario.insertar_inventario(datos["IDProducto"], datos["CantidadDisponible"]))

@app.route('/inventario/actualizar', methods=["PUT"])
@requiere_token
def actualizar_inventario():
    datos = request.json
    return jsonify(RepositorioInventario.actualizar_inventario(datos["ID"], datos["CantidadDisponible"]))

@app.route('/inventario/eliminar/<int:id_producto>', methods=["DELETE"])
@requiere_token
def eliminar_inventario(id_producto):
    return jsonify(RepositorioInventario.eliminar_inventario(id_producto))


@app.route('/historial_precios/listar', methods=["GET"])
@requiere_token
def listar_historial_precios():
    return jsonify({"HistorialPrecios": RepositorioHistorialPrecios.listar_historial_precios()})

@app.route('/historial_precios/insertar', methods=["POST"])
@requiere_token
def insertar_historial_precio():
    datos = request.json
    return jsonify(RepositorioHistorialPrecios.insertar_historial_precio(datos["IDProducto"], datos["Fecha"], datos["PrecioAntiguo"], datos["PrecioNuevo"]))

@app.route('/historial_precios/actualizar', methods=["PUT"])
@requiere_token
def actualizar_historial_precio():
    datos = request.json
    return jsonify(RepositorioHistorialPrecios.actualizar_historial_precio(
        datos["ID"], datos["IDProducto"], datos["Fecha"], datos["PrecioAntiguo"], datos["PrecioNuevo"]
    ))

@app.route('/historial_precios/eliminar/<int:id_historial>', methods=["DELETE"])
@requiere_token
def eliminar_historial_precio(id_historial):
    return jsonify(RepositorioHistorialPrecios.eliminar_historial_precio(id_historial))


@app.route('/estado_transaccion/listar', methods=["GET"])
@requiere_token
def listar_estados_transaccion():
    return jsonify({"EstadosTransaccion": RepositorioEstadoTransaccion.listar_estados_transaccion()})

@app.route('/estado_transaccion/insertar', methods=["POST"])
@requiere_token
def insertar_estado_transaccion():
    datos = request.json
    return jsonify(RepositorioEstadoTransaccion.insertar_estado_transaccion(datos["NombreEstado"]))

@app.route('/estado_transaccion/actualizar', methods=["PUT"])
@requiere_token
def actualizar_estado_transaccion():
    datos = request.json
    return jsonify(RepositorioEstadoTransaccion.actualizar_estado_transaccion(
        datos["ID"], datos["NombreEstado"]
    ))

@app.route('/estado_transaccion/eliminar/<int:id_estado>', methods=["DELETE"])
@requiere_token
def eliminar_estado_transaccion(id_estado):
    return jsonify(RepositorioEstadoTransaccion.eliminar_estado_transaccion(id_estado))


@app.route('/direcciones_usuarios/listar', methods=["GET"])
@requiere_token
def listar_direcciones_usuarios():
    return jsonify({"DireccionesUsuarios": RepositorioDireccionesUsuarios.listar_direcciones_usuarios()})

@app.route('/direcciones_usuarios/insertar', methods=["POST"])
@requiere_token
def insertar_direccion_usuario():
    datos = request.json
    return jsonify(RepositorioDireccionesUsuarios.insertar_direccion_usuario(datos["IDUsuario"], datos["Direccion"]))

@app.route('/direcciones_usuarios/actualizar', methods=["PUT"])
@requiere_token
def actualizar_direccion_usuario():
    datos = request.json
    return jsonify(RepositorioDireccionesUsuarios.actualizar_direccion_usuario(
        datos["ID"], datos["IDUsuario"], datos["Direccion"]
    ))

@app.route('/direcciones_usuarios/eliminar/<int:id_direccion>', methods=["DELETE"])
@requiere_token
def eliminar_direccion_usuario(id_direccion):
    return jsonify(RepositorioDireccionesUsuarios.eliminar_direccion_usuario(id_direccion))


@app.route('/devoluciones/listar', methods=["GET"])
@requiere_token
def listar_devoluciones():
    return jsonify({"Devoluciones": RepositorioDevoluciones.listar_devoluciones()})

@app.route('/devoluciones/insertar', methods=["POST"])
@requiere_token
def insertar_devolucion():
    datos = request.json
    return jsonify(RepositorioDevoluciones.insertar_devolucion(datos["IDTransaccion"], datos["Motivo"], datos["Fecha"]))

@app.route('/devoluciones/actualizar', methods=["PUT"])
@requiere_token
def actualizar_devolucion():
    datos = request.json
    return jsonify(RepositorioDevoluciones.actualizar_devolucion(
        datos["ID"], datos["IDTransaccion"], datos["Motivo"], datos["Fecha"]
    ))

@app.route('/devoluciones/eliminar/<int:id_devolucion>', methods=["DELETE"])
@requiere_token
def eliminar_devolucion(id_devolucion):
    return jsonify(RepositorioDevoluciones.eliminar_devolucion(id_devolucion))


@app.route('/detalles_transaccion/listar', methods=["GET"])
@requiere_token
def listar_detalles_transaccion():
    return jsonify({"DetallesTransaccion": RepositorioDetallesTransaccion.listar_detalles_transaccion()})

@app.route('/detalles_transaccion/insertar', methods=["POST"])
@requiere_token
def insertar_detalle_transaccion():
    datos = request.json
    return jsonify(RepositorioDetallesTransaccion.insertar_detalle_transaccion(datos["IDTransaccion"], datos["IDProducto"], datos["Cantidad"]))

@app.route('/detalles_transaccion/actualizar', methods=["PUT"])
@requiere_token
def actualizar_detalle_transaccion():
    datos = request.json
    return jsonify(RepositorioDetallesTransaccion.actualizar_detalle_transaccion(
        datos["ID"], datos["IDTransaccion"], datos["IDProducto"], datos["Cantidad"]
    ))

@app.route('/detalles_transaccion/eliminar/<int:id_detalle>', methods=["DELETE"])
@requiere_token
def eliminar_detalle_transaccion(id_detalle):
    return jsonify(RepositorioDetallesTransaccion.eliminar_detalle_transaccion(id_detalle))

@app.route('/categorias/listar', methods=["GET"])
@requiere_token
def listar_categorias():
    return jsonify({"Categorias": RepositorioCategorias.listar_categorias()})

@app.route('/categorias/insertar', methods=["POST"])
@requiere_token
def insertar_categoria():
    datos = request.json
    return jsonify(RepositorioCategorias.insertar_categoria(datos["NombreCategoria"]))

@app.route('/categorias/actualizar', methods=["PUT"])
@requiere_token
def actualizar_categoria():
    datos = request.json
    return jsonify(RepositorioCategorias.actualizar_categoria(
        datos["ID"], datos["NombreCategoria"]
    ))

@app.route('/categorias/eliminar/<int:id_categoria>', methods=["DELETE"])
@requiere_token
def eliminar_categoria(id_categoria):
    return jsonify(RepositorioCategorias.eliminar_categoria(id_categoria))

@app.route('/notificaciones/listar', methods=["GET"])
@requiere_token
def listar_notificaciones():
    return jsonify({"Notificaciones": RepositorioNotificaciones.listar_notificaciones()})

@app.route('/notificaciones/insertar', methods=["POST"])
@requiere_token
def insertar_notificacion():
    datos = request.json
    return jsonify(RepositorioNotificaciones.insertar_notificacion(
        datos["IDUsuario"], datos["Mensaje"], datos["Fecha"]
    ))

@app.route('/notificaciones/actualizar', methods=["PUT"])
@requiere_token
def actualizar_notificacion():
    datos = request.json
    return jsonify(RepositorioNotificaciones.actualizar_notificacion(
        datos["ID"], datos["Mensaje"], datos["Fecha"]
    ))

@app.route('/notificaciones/eliminar/<int:id_notificacion>', methods=["DELETE"])
@requiere_token
def eliminar_notificacion(id_notificacion):
    return jsonify(RepositorioNotificaciones.eliminar_notificacion(id_notificacion))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
