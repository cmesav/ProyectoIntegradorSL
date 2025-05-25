import pyodbc
from utilidades.configuracion import Configuracion  
from utilidades.SeguridadAES import SeguridadAES  

class RepositorioTransacciones:

    encriptarAES = SeguridadAES()

    @staticmethod
    def obtener_conexion():
        try:
            return pyodbc.connect(Configuracion.strConnection)
        except Exception as ex:
            return {"Error": f"Fallo en la conexión: {ex}"}

    @staticmethod
    def listar_transacciones():
        try:
            conexion = RepositorioTransacciones.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            consulta = """SELECT IDTransaccion, IDUsuario, Fecha, IDMetodoPago, IDEstadoTransaccion FROM Transacciones"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            transacciones = []
            for elemento in cursor:
                try:
                    fecha_descifrada = RepositorioTransacciones.encriptarAES.descifrar(elemento[2]) if elemento[2] else "Sin datos"
                except Exception as ex:
                    fecha_descifrada = f"Error al descifrar: {ex}"

                transacciones.append({
                    "IDTransaccion": elemento[0],
                    "IDUsuario": elemento[1],
                    "Fecha": fecha_descifrada,
                    "IDMetodoPago": elemento[3],
                    "IDEstadoTransaccion": elemento[4]
                })

            cursor.close()
            conexion.close()
            return transacciones

        except Exception as ex:
            return {"Error": f"Error al listar transacciones: {ex}"}

    @staticmethod
    def insertar_transaccion(id_usuario: int, fecha: str, id_metodo_pago: int, id_estado_transaccion: int):
        try:
            conexion = RepositorioTransacciones.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            fecha_cifrada = RepositorioTransacciones.encriptarAES.cifrar(fecha)

            consulta = """INSERT INTO Transacciones (IDUsuario, Fecha, IDMetodoPago, IDEstadoTransaccion) 
                          VALUES (?, ?, ?, ?)"""
            cursor.execute(consulta, (id_usuario, fecha_cifrada, id_metodo_pago, id_estado_transaccion))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Transacción insertada correctamente"}
        except Exception as ex:
            return {"Error": f"Error al insertar transacción: {ex}"}

    @staticmethod
    def actualizar_transaccion(id_transaccion: int, fecha: str, id_metodo_pago: int, id_estado_transaccion: int):
        try:
            conexion = RepositorioTransacciones.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            fecha_cifrada = RepositorioTransacciones.encriptarAES.cifrar(fecha)

            consulta = """UPDATE Transacciones SET Fecha=?, IDMetodoPago=?, IDEstadoTransaccion=? WHERE IDTransaccion=?"""
            cursor.execute(consulta, (fecha_cifrada, id_metodo_pago, id_estado_transaccion, id_transaccion))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Transacción actualizada correctamente"}
        except Exception as ex:
            return {"Error": f"Error al actualizar transacción: {ex}"}

    @staticmethod
    def eliminar_transaccion(id_transaccion: int):
        try:
            conexion = RepositorioTransacciones.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            consulta = """DELETE FROM Transacciones WHERE IDTransaccion=?"""
            cursor.execute(consulta, (id_transaccion,))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Transacción eliminada correctamente"}
        except Exception as ex:
            return {"Error": f"Error al eliminar transacción: {ex}"}
 