import pyodbc
from Utilidades import Configuracion

class RepositorioDevoluciones:

    def ListarDevoluciones(self) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM Devoluciones"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for elemento in cursor:
                print(elemento)

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))

    def InsertarDevolucion(self, id_transaccion: int, motivo: str, fecha: str) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO Devoluciones (IDTransaccion, Motivo, Fecha) VALUES (?, ?, ?)"""
            cursor.execute(consulta, (id_transaccion, motivo, fecha))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
