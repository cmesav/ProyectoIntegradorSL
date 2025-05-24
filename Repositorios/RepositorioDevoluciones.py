import pyodbc

from Utilidades.configuracion import Configuracion  
from Utilidades.SeguridadAES import SeguridadAES  

class RepositorioDevoluciones:

    encriptarAES = SeguridadAES()

    @staticmethod
    def obtener_conexion():
        try:
            return pyodbc.connect(Configuracion.strConnection)
        except Exception as ex:
            return {"Error": f"Fallo en la conexión: {ex}"}

    @staticmethod
    def listar_devoluciones():
        try:
            conexion = RepositorioDevoluciones.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            consulta = """SELECT IDDevolucion, IDTransaccion, Motivo, Fecha FROM Devoluciones"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            devoluciones = []
            for elemento in cursor:
                try:
                    motivo_descifrado = RepositorioDevoluciones.encriptarAES.descifrar(elemento[2]) if elemento[2] else "Sin datos"
                    fecha_descifrada = RepositorioDevoluciones.encriptarAES.descifrar(elemento[3]) if elemento[3] else "Sin datos"
                except Exception as ex:
                    motivo_descifrado = f"Error al descifrar: {ex}"
                    fecha_descifrada = f"Error al descifrar: {ex}"

                devoluciones.append({
                    "IDDevolucion": elemento[0],
                    "IDTransaccion": elemento[1],
                    "Motivo": motivo_descifrado,
                    "Fecha": fecha_descifrada
                })

            cursor.close()
            conexion.close()
            return devoluciones

        except Exception as ex:
            return {"Error": f"Error al listar devoluciones: {ex}"}

    @staticmethod
    def insertar_devolucion(id_transaccion: int, motivo: str, fecha: str):
        try:
            conexion = RepositorioDevoluciones.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            motivo_cifrado = RepositorioDevoluciones.encriptarAES.cifrar(motivo)
            fecha_cifrada = RepositorioDevoluciones.encriptarAES.cifrar(fecha)

            consulta = """INSERT INTO Devoluciones (IDTransaccion, Motivo, Fecha) VALUES (?, ?, ?)"""
            cursor.execute(consulta, (id_transaccion, motivo_cifrado, fecha_cifrada))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Devolución insertada correctamente"}
        except Exception as ex:
            return {"Error": f"Error al insertar devolución: {ex}"}

    @staticmethod
    def actualizar_devolucion(id_devolucion: int, id_transaccion: int, motivo: str, fecha: str):
        try:
            conexion = RepositorioDevoluciones.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            motivo_cifrado = RepositorioDevoluciones.encriptarAES.cifrar(motivo)
            fecha_cifrada = RepositorioDevoluciones.encriptarAES.cifrar(fecha)

            consulta = """UPDATE Devoluciones SET IDTransaccion=?, Motivo=?, Fecha=? WHERE IDDevolucion=?"""
            cursor.execute(consulta, (id_transaccion, motivo_cifrado, fecha_cifrada, id_devolucion))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Devolución actualizada correctamente"}
        except Exception as ex:
            return {"Error": f"Error al actualizar devolución: {ex}"}

    @staticmethod
    def eliminar_devolucion(id_devolucion: int):
        try:
            conexion = RepositorioDevoluciones.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            consulta = """DELETE FROM Devoluciones WHERE IDDevolucion=?"""
            cursor.execute(consulta, (id_devolucion,))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Devolución eliminada correctamente"}
        except Exception as ex:
            return {"Error": f"Error al eliminar devolución: {ex}"}
 