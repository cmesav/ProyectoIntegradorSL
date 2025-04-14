import pyodbc
from Utilidades import Configuracion

class RepositorioMetodosPago:

    def ListarMetodosPago(self) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM MetodosPago"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for elemento in cursor:
                print(elemento)

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))

    def InsertarMetodoPago(self, nombre_metodo: str) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO MetodosPago (NombreMetodo) VALUES (?)"""
            cursor.execute(consulta, (nombre_metodo,))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
