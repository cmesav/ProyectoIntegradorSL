import pyodbc
from utilidades.configuracion import Configuracion  
from utilidades.SeguridadAES import SeguridadAES  

class RepositorioHistorialPrecios:

    encriptarAES = SeguridadAES()

    @staticmethod
    def obtener_conexion():
        try:
            return pyodbc.connect(Configuracion.strConnection)
        except Exception as ex:
            return {"Error": f"Fallo en la conexión: {ex}"}

    @staticmethod
    def listar_historial_precios():
        try:
            conexion = RepositorioHistorialPrecios.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            consulta = """SELECT IDHistorial, IDProducto, Fecha, PrecioAntiguo, PrecioNuevo FROM HistorialPrecios"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            historial_precios = []
            for elemento in cursor:
                try:
                    fecha_descifrada = RepositorioHistorialPrecios.encriptarAES.descifrar(elemento[2]) if elemento[2] else "Sin datos"
                    precio_antiguo_descifrado = float(RepositorioHistorialPrecios.encriptarAES.descifrar(elemento[3])) if elemento[3] else 0.0
                    precio_nuevo_descifrado = float(RepositorioHistorialPrecios.encriptarAES.descifrar(elemento[4])) if elemento[4] else 0.0
                except Exception as ex:
                    fecha_descifrada = f"Error al descifrar: {ex}"
                    precio_antiguo_descifrado = f"Error al descifrar: {ex}"
                    precio_nuevo_descifrado = f"Error al descifrar: {ex}"

                historial_precios.append({
                    "IDHistorial": elemento[0],
                    "IDProducto": elemento[1],
                    "Fecha": fecha_descifrada,
                    "PrecioAntiguo": precio_antiguo_descifrado,
                    "PrecioNuevo": precio_nuevo_descifrado
                })

            cursor.close()
            conexion.close()
            return historial_precios

        except Exception as ex:
            return {"Error": f"Error al listar historial de precios: {ex}"}

    @staticmethod
    def insertar_historial_precio(id_producto: int, fecha: str, precio_antiguo: float, precio_nuevo: float):
        try:
            conexion = RepositorioHistorialPrecios.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            fecha_cifrada = RepositorioHistorialPrecios.encriptarAES.cifrar(fecha)
            precio_antiguo_cifrado = RepositorioHistorialPrecios.encriptarAES.cifrar(str(precio_antiguo))
            precio_nuevo_cifrado = RepositorioHistorialPrecios.encriptarAES.cifrar(str(precio_nuevo))

            consulta = """INSERT INTO HistorialPrecios (IDProducto, Fecha, PrecioAntiguo, PrecioNuevo) VALUES (?, ?, ?, ?)"""
            cursor.execute(consulta, (id_producto, fecha_cifrada, precio_antiguo_cifrado, precio_nuevo_cifrado))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Historial de precios insertado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al insertar historial de precios: {ex}"}

    @staticmethod
    def actualizar_historial_precio(id_historial: int, fecha: str, precio_antiguo: float, precio_nuevo: float):
        try:
            conexion = RepositorioHistorialPrecios.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            fecha_cifrada = RepositorioHistorialPrecios.encriptarAES.cifrar(fecha)
            precio_antiguo_cifrado = RepositorioHistorialPrecios.encriptarAES.cifrar(str(precio_antiguo))
            precio_nuevo_cifrado = RepositorioHistorialPrecios.encriptarAES.cifrar(str(precio_nuevo))

            consulta = """UPDATE HistorialPrecios SET Fecha=?, PrecioAntiguo=?, PrecioNuevo=? WHERE IDHistorial=?"""
            cursor.execute(consulta, (fecha_cifrada, precio_antiguo_cifrado, precio_nuevo_cifrado, id_historial))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Historial de precios actualizado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al actualizar historial de precios: {ex}"}

    @staticmethod
    def eliminar_historial_precio(id_historial: int):
        try:
            conexion = RepositorioHistorialPrecios.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            consulta = """DELETE FROM HistorialPrecios WHERE IDHistorial=?"""
            cursor.execute(consulta, (id_historial,))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Historial de precios eliminado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al eliminar historial de precios: {ex}"}
 