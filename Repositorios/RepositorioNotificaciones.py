import pyodbc
from Entidades import Notificacion
from Utilidades import configuracion
from Utilidades import SeguridadAES  

class RepositorioNotificaciones:
    encriptarAES = SeguridadAES.SeguridadAES()  

    def ListarNotificaciones(self) -> list:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT ID, IDUsuario, Mensaje, Fecha FROM Notificaciones"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = Notificacion.Notificacion()
                entidad.SetId(elemento[0])
                entidad.SetIdUsuario(elemento[1])

                mensaje_descifrado = self.encriptarAES.descifrar(elemento[2]) if elemento[2] else "Sin datos"
                fecha_descifrada = self.encriptarAES.descifrar(elemento[3]) if elemento[3] else "Sin datos"

                entidad.SetMensaje(mensaje_descifrado)
                entidad.SetFecha(fecha_descifrada)

                lista.append(entidad)

            cursor.close()
            conexion.close()
            return lista

        except Exception as ex:
            print(f"Error al listar notificaciones: {ex}")
            return []

    def InsertarNotificacion(self, id_usuario: int, mensaje: str, fecha: str) -> bool:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            mensaje_cifrado = self.encriptarAES.cifrar(mensaje)
            fecha_cifrada = self.encriptarAES.cifrar(fecha)

            consulta = """INSERT INTO Notificaciones (IDUsuario, Mensaje, Fecha) VALUES (?, ?, ?)"""
            cursor.execute(consulta, (id_usuario, mensaje_cifrado, fecha_cifrada))
            conexion.commit()

            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al insertar notificación: {ex}")
            return False