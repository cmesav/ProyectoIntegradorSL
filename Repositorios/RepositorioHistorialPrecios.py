import pyodbc
from Utilidades import Configuracion

class RepositorioHistorialPrecios:

    def ListarHistorialPrecios(self) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM HistorialPrecios"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for elemento in cursor:
                print(elemento)

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))

    def InsertarHistorialPrecio(self, id_producto: int, fecha: str, precio_antiguo: float, precio_nuevo: float) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO HistorialPrecios (IDProducto, Fecha, PrecioAntiguo, PrecioNuevo) VALUES (?, ?, ?, ?)"""
            cursor.execute(consulta, (id_producto, fecha, precio_antiguo, precio_nuevo))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
