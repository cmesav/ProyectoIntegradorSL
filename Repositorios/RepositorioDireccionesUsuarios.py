import pyodbc
from Utilidades import Configuracion

class RepositorioDireccionesUsuarios:

    def ListarDireccionesUsuarios(self) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM DireccionesUsuarios"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for elemento in cursor:
                print(elemento)

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))

    def InsertarDireccionUsuario(self, id_usuario: int, direccion: str) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO DireccionesUsuarios (IDUsuario, Direccion) VALUES (?, ?)"""
            cursor.execute(consulta, (id_usuario, direccion))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
