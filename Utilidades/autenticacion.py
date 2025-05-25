import jwt
from flask import request, jsonify
from functools import wraps
from Utilidades.JWTEncriptador import JWTEncriptador

jwt_encriptador = JWTEncriptador()
jwt_encriptador.SetClave("12346467987987")

def validar_token(token):
    datos = jwt_encriptador.DecodificarToken(token)
    return datos is not None

def requiere_token(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if not validar_token(token):
            return jsonify({'error': 'No autenticado'}), 401
        return f(*args, **kwargs)
    return decorador
