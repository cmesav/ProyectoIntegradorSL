import pyodbc
from Entidades import Notificacion
from Utilidades import configuracion

class RepositorioNotificaciones:

    def ListarNotificaciones(self) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM Notificaciones"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = Notificacion.Notificaciones()
                entidad.SetIdNotificacion(elemento[0])
                entidad.SetIdUsuario(elemento[1])
                entidad.SetMensaje(elemento[2])
                entidad.SetFecha(elemento[3])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for notificacion in lista:
                print(f"{notificacion.GetIdNotificacion()}, {notificacion.GetIdUsuario()}, {notificacion.GetMensaje()}, {notificacion.GetFecha()}")

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
