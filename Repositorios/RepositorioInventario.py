import pyodbc
from Utilidades.configuracion import Configuracion  
from Utilidades.SeguridadAES import SeguridadAES  

class RepositorioInventario:

    encriptarAES = SeguridadAES()

    @staticmethod
    def obtener_conexion():
        try:
            return pyodbc.connect(Configuracion.strConnection)
        except Exception as ex:
            return {"Error": f"Fallo en la conexión: {ex}"}

    @staticmethod
    def listar_inventario():
        try:
            conexion = RepositorioInventario.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            consulta = """SELECT IDInventario, IDProducto, CantidadDisponible FROM Inventario"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            inventario = []
            for elemento in cursor:
                try:
                    cantidad_descifrada = int(RepositorioInventario.encriptarAES.descifrar(elemento[2])) if elemento[2] else 0
                except Exception as ex:
                    cantidad_descifrada = f"Error al descifrar: {ex}"

                inventario.append({
                    "IDInventario": elemento[0],
                    "IDProducto": elemento[1],
                    "CantidadDisponible": cantidad_descifrada
                })

            cursor.close()
            conexion.close()
            return inventario

        except Exception as ex:
            return {"Error": f"Error al listar inventario: {ex}"}

    @staticmethod
    def insertar_inventario(id_producto: int, cantidad_disponible: int):
        try:
            conexion = RepositorioInventario.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            cantidad_cifrada = RepositorioInventario.encriptarAES.cifrar(str(cantidad_disponible))

            consulta = """INSERT INTO Inventario (IDProducto, CantidadDisponible) VALUES (?, ?)"""
            cursor.execute(consulta, (id_producto, cantidad_cifrada))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Inventario insertado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al insertar inventario: {ex}"}

    @staticmethod
    def actualizar_inventario(id_producto: int, cantidad_disponible: int):
        try:
            conexion = RepositorioInventario.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            cantidad_cifrada = RepositorioInventario.encriptarAES.cifrar(str(cantidad_disponible))

            consulta = """UPDATE Inventario SET CantidadDisponible = ? WHERE IDProducto = ?"""
            cursor.execute(consulta, (cantidad_cifrada, id_producto))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Inventario actualizado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al actualizar inventario: {ex}"}

    @staticmethod
    def eliminar_inventario(id_producto: int):
        try:
            conexion = RepositorioInventario.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            consulta = """DELETE FROM Inventario WHERE IDProducto=?"""
            cursor.execute(consulta, (id_producto,))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Inventario eliminado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al eliminar inventario: {ex}"}
 