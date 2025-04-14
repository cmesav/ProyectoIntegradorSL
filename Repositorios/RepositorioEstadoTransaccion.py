import pyodbc
from Utilidades import Configuracion

class RepositorioEstadoTransaccion:

    def ListarEstadoTransaccion(self) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM EstadoTransaccion"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for elemento in cursor:
                print(elemento)

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))

    def InsertarEstadoTransaccion(self, nombre_estado: str) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO EstadoTransaccion (NombreEstado) VALUES (?)"""
            cursor.execute(consulta, (nombre_estado,))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
