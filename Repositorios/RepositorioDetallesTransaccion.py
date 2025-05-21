import pyodbc
from Entidades.DetalleTransaccion import DetalleTransaccion
from Utilidades.configuracion import Configuracion  
from Utilidades.SeguridadAES import SeguridadAES  

class RepositorioDetallesTransaccion:

    encriptarAES = SeguridadAES()

    @staticmethod
    def obtener_conexion():
        try:
            return pyodbc.connect(Configuracion.strConnection)
        except Exception as ex:
            return {"Error": f"Fallo en la conexión: {ex}"}

    @staticmethod
    def listar_detalles_transaccion():
        try:
            conexion = RepositorioDetallesTransaccion.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            consulta = """SELECT IDDetalle, IDTransaccion, IDProducto, Cantidad FROM DetallesTransaccion"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            detalles_transaccion = []
            for elemento in cursor:
                try:
                    cantidad_descifrada = int(RepositorioDetallesTransaccion.encriptarAES.descifrar(elemento[3])) if elemento[3] else 0
                except Exception as ex:
                    cantidad_descifrada = f"Error al descifrar: {ex}"

                detalles_transaccion.append({
                    "IDDetalle": elemento[0],
                    "IDTransaccion": elemento[1],
                    "IDProducto": elemento[2],
                    "Cantidad": cantidad_descifrada
                })

            cursor.close()
            conexion.close()
            return detalles_transaccion

        except Exception as ex:
            return {"Error": f"Error al listar detalles de transacción: {ex}"}

    @staticmethod
    def insertar_detalle_transaccion(id_transaccion: int, id_producto: int, cantidad: int):
        try:
            conexion = RepositorioDetallesTransaccion.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            cantidad_cifrada = RepositorioDetallesTransaccion.encriptarAES.cifrar(str(cantidad))

            consulta = """INSERT INTO DetallesTransaccion (IDTransaccion, IDProducto, Cantidad) VALUES (?, ?, ?)"""
            cursor.execute(consulta, (id_transaccion, id_producto, cantidad_cifrada))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Detalle de transacción insertado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al insertar detalle de transacción: {ex}"}
