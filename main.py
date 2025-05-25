from flask import Flask, jsonify, request
from routes.usuarios import usuarios_bp
from routes.transacciones import transacciones_bp
from routes.productos import productos_bp
from routes.proveedores import proveedores_bp
from routes.roles import roles_bp
from routes.metodos_pago import metodos_pago_bp
from routes.inventario import inventario_bp
from routes.historial_precios import historial_precios_bp
from routes.estado_transaccion import estado_transaccion_bp
from routes.direcciones_usuarios import direcciones_usuarios_bp
from routes.devoluciones import devoluciones_bp
from routes.detalles_transaccion import detalles_transaccion_bp
from routes.categorias import categorias_bp
from routes.notificaciones import notificaciones_bp
from Utilidades.autenticacion import requiere_token, validar_token
from Utilidades.JWTEncriptador import JWTEncriptador

# Configurar Flask
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Configurar autenticación JWT
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
