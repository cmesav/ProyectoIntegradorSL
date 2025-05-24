import pyodbc
from Utilidades.configuracion import Configuracion  
from Utilidades.SeguridadAES import SeguridadAES  

class RepositorioEstadoTransaccion:

    encriptarAES = SeguridadAES()

    @staticmethod
    def obtener_conexion():
        try:
            return pyodbc.connect(Configuracion.strConnection)
        except Exception as ex:
            return {"Error": f"Fallo en la conexión: {ex}"}

    @staticmethod
    def listar_estados_transaccion():
        try:
            conexion = RepositorioEstadoTransaccion.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            consulta = """SELECT IDEstadoTransaccion, NombreEstado FROM EstadoTransaccion"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            estados_transaccion = []
            for elemento in cursor:
                try:
                    nombre_descifrado = RepositorioEstadoTransaccion.encriptarAES.descifrar(elemento[1]) if elemento[1] else "Sin datos"
                except Exception as ex:
                    nombre_descifrado = f"Error al descifrar: {ex}"

                estados_transaccion.append({
                    "IDEstadoTransaccion": elemento[0],
                    "NombreEstado": nombre_descifrado
                })

            cursor.close()
            conexion.close()
            return estados_transaccion

        except Exception as ex:
            return {"Error": f"Error al listar estados de transacción: {ex}"}

    @staticmethod
    def insertar_estado_transaccion(nombre_estado: str):
        try:
            conexion = RepositorioEstadoTransaccion.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            nombre_cifrado = RepositorioEstadoTransaccion.encriptarAES.cifrar(nombre_estado)

            consulta = """INSERT INTO EstadoTransaccion (NombreEstado) VALUES (?)"""
            cursor.execute(consulta, (nombre_cifrado,))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Estado de transacción insertado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al insertar estado de transacción: {ex}"}

    @staticmethod
    def actualizar_estado_transaccion(id_estado_transaccion: int, nombre_estado: str):
        try:
            conexion = RepositorioEstadoTransaccion.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            nombre_cifrado = RepositorioEstadoTransaccion.encriptarAES.cifrar(nombre_estado)

            consulta = """UPDATE EstadoTransaccion SET NombreEstado=? WHERE IDEstadoTransaccion=?"""
            cursor.execute(consulta, (nombre_cifrado, id_estado_transaccion))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Estado de transacción actualizado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al actualizar estado de transacción: {ex}"}

    @staticmethod
    def eliminar_estado_transaccion(id_estado_transaccion: int):
        try:
            conexion = RepositorioEstadoTransaccion.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            consulta = """DELETE FROM EstadoTransaccion WHERE IDEstadoTransaccion=?"""
            cursor.execute(consulta, (id_estado_transaccion,))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Estado de transacción eliminado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al eliminar estado de transacción: {ex}"}
 