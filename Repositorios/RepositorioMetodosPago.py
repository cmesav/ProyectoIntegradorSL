import pyodbc
from utilidades.configuracion import Configuracion  
from utilidades.SeguridadAES import SeguridadAES  

class RepositorioMetodosPago:

    encriptarAES = SeguridadAES()

    @staticmethod
    def obtener_conexion():
        try:
            return pyodbc.connect(Configuracion.strConnection)
        except Exception as ex:
            return {"Error": f"Fallo en la conexión: {ex}"}

    @staticmethod
    def listar_metodos_pago():
        try:
            conexion = RepositorioMetodosPago.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            consulta = """SELECT IDMetodoPago, NombreMetodo FROM MetodosPago"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            metodos_pago = []
            for elemento in cursor:
                try:
                    nombre_descifrado = RepositorioMetodosPago.encriptarAES.descifrar(elemento[1]) if elemento[1] else "Sin datos"
                except Exception as ex:
                    nombre_descifrado = f"Error al descifrar: {ex}"

                metodos_pago.append({
                    "IDMetodoPago": elemento[0],
                    "NombreMetodo": nombre_descifrado
                })

            cursor.close()
            conexion.close()
            return metodos_pago

        except Exception as ex:
            return {"Error": f"Error al listar métodos de pago: {ex}"}

    @staticmethod
    def insertar_metodo_pago(nombre_metodo: str):
        try:
            conexion = RepositorioMetodosPago.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            nombre_cifrado = RepositorioMetodosPago.encriptarAES.cifrar(nombre_metodo)

            consulta = """INSERT INTO MetodosPago (NombreMetodo) VALUES (?)"""
            cursor.execute(consulta, (nombre_cifrado,))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Método de pago insertado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al insertar método de pago: {ex}"}

    @staticmethod
    def actualizar_metodo_pago(id_metodo_pago: int, nombre_metodo: str):
        try:
            conexion = RepositorioMetodosPago.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            nombre_cifrado = RepositorioMetodosPago.encriptarAES.cifrar(nombre_metodo)

            consulta = """UPDATE MetodosPago SET NombreMetodo=? WHERE IDMetodoPago=?"""
            cursor.execute(consulta, (nombre_cifrado, id_metodo_pago))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Método de pago actualizado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al actualizar método de pago: {ex}"}

    @staticmethod
    def eliminar_metodo_pago(id_metodo_pago: int):
        try:
            conexion = RepositorioMetodosPago.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            consulta = """DELETE FROM MetodosPago WHERE IDMetodoPago=?"""
            cursor.execute(consulta, (id_metodo_pago,))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Método de pago eliminado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al eliminar método de pago: {ex}"}
 