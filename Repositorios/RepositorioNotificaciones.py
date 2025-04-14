import pyodbc
from Utilidades import Configuracion

class RepositorioNotificaciones:

    def ListarNotificaciones(self) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM Notificaciones"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for elemento in cursor:
                print(elemento)

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))

    def InsertarNotificacion(self, id_usuario: int, mensaje: str, fecha: str) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO Notificaciones (IDUsuario, Mensaje, Fecha) VALUES (?, ?, ?)"""
            cursor.execute(consulta, (id_usuario, mensaje, fecha))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
