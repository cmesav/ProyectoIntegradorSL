import pyodbc
from Entidades.DireccionUsuario import DireccionUsuario
from Utilidades.configuracion import Configuracion  
from Utilidades.SeguridadAES import SeguridadAES  

class RepositorioDireccionesUsuarios:

    encriptarAES = SeguridadAES()

    @staticmethod
    def obtener_conexion():
        try:
            return pyodbc.connect(Configuracion.strConnection)
        except Exception as ex:
            return {"Error": f"Fallo en la conexión: {ex}"}

    @staticmethod
    def listar_direcciones_usuarios():
        try:
            conexion = RepositorioDireccionesUsuarios.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            consulta = """SELECT IDDirecciones, IDUsuario, Direccion FROM DireccionesUsuarios"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            direcciones_usuarios = []
            for elemento in cursor:
                try:
                    direccion_descifrada = RepositorioDireccionesUsuarios.encriptarAES.descifrar(elemento[2]) if elemento[2] else "Sin datos"
                except Exception as ex:
                    direccion_descifrada = f"Error al descifrar: {ex}"

                direcciones_usuarios.append({
                    "IDDirecciones": elemento[0],
                    "IDUsuario": elemento[1],
                    "Direccion": direccion_descifrada
                })

            cursor.close()
            conexion.close()
            return direcciones_usuarios

        except Exception as ex:
            return {"Error": f"Error al listar direcciones de usuario: {ex}"}

    @staticmethod
    def insertar_direccion_usuario(id_usuario: int, direccion: str):
        try:
            conexion = RepositorioDireccionesUsuarios.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            direccion_cifrada = RepositorioDireccionesUsuarios.encriptarAES.cifrar(direccion)

            consulta = """INSERT INTO DireccionesUsuarios (IDUsuario, Direccion) VALUES (?, ?)"""
            cursor.execute(consulta, (id_usuario, direccion_cifrada))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Dirección de usuario insertada correctamente"}
        except Exception as ex:
            return {"Error": f"Error al insertar dirección de usuario: {ex}"}
