from flask import Flask, jsonify, request
from blueprint.usuarios import usuarios_bp
from blueprint.transacciones import transacciones_bp
from blueprint.productos import productos_bp
from blueprint.proveedores import proveedores_bp
from blueprint.roles import roles_bp
from blueprint.metodos_pago import metodos_pago_bp
from blueprint.inventario import inventario_bp
from blueprint.historial_precios import historial_precios_bp
from blueprint.estado_transaccion import estado_transaccion_bp
from blueprint.direcciones_usuarios import direcciones_usuarios_bp
from blueprint.devoluciones import devoluciones_bp
from blueprint.detalles_transaccion import detalles_transaccion_bp
from blueprint.categorias import categorias_bp
from blueprint.notificaciones import notificaciones_bp
from utilidades.autenticacion import JWTEncriptador

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

# Registro de Blueprints
app.register_blueprint(usuarios_bp)
app.register_blueprint(transacciones_bp)
app.register_blueprint(productos_bp)
app.register_blueprint(proveedores_bp)
app.register_blueprint(roles_bp)
app.register_blueprint(metodos_pago_bp)
app.register_blueprint(inventario_bp)
app.register_blueprint(historial_precios_bp)
app.register_blueprint(estado_transaccion_bp)
app.register_blueprint(direcciones_usuarios_bp)
app.register_blueprint(devoluciones_bp)
app.register_blueprint(detalles_transaccion_bp)
app.register_blueprint(categorias_bp)
app.register_blueprint(notificaciones_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
