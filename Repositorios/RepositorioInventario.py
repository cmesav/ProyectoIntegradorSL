import pyodbc
from Utilidades import Configuracion

class RepositorioInventario:

    def ListarInventario(self) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM Inventario"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for elemento in cursor:
                print(elemento)

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))

    def ActualizarInventario(self, id_producto: int, cantidad_disponible: int) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """UPDATE Inventario SET CantidadDisponible = ? WHERE IDProducto = ?"""
            cursor.execute(consulta, (cantidad_disponible, id_producto))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
