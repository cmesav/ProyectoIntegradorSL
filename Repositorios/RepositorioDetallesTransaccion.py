import pyodbc
from Utilidades import Configuracion

class RepositorioDetallesTransaccion:

    def ListarDetallesTransaccion(self) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM DetallesTransaccion"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for elemento in cursor:
                print(elemento)

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))

    def InsertarDetalleTransaccion(self, id_transaccion: int, id_producto: int, cantidad: int) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO DetallesTransaccion (IDTransaccion, IDProducto, Cantidad) VALUES (?, ?, ?)"""
            cursor.execute(consulta, (id_transaccion, id_producto, cantidad))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
