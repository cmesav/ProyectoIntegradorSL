import pyodbc
from Entidades.Notificacion import Notificacion
from Utilidades.configuracion import Configuracion  
from Utilidades.SeguridadAES import SeguridadAES  

class RepositorioNotificaciones:
    """Clase para gestionar notificaciones con cifrado AES-GCM"""

    encriptarAES = SeguridadAES()

    @staticmethod
    def obtener_conexion():
        """Obtiene una conexión segura a la base de datos"""
        try:
            return pyodbc.connect(Configuracion.strConnection)
        except Exception as ex:
            return {"Error": f"Fallo en la conexión: {ex}"}

    @staticmethod
    def listar_notificaciones():
        """Lista las notificaciones y descifra los datos si es posible"""
        try:
            conexion = RepositorioNotificaciones.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            consulta = """SELECT IDNotificacion, IDUsuario, Mensaje, Fecha FROM Notificaciones"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            notificaciones = []
            for elemento in cursor:
                try:
                    mensaje_descifrado = RepositorioNotificaciones.encriptarAES.descifrar(elemento[2]) if elemento[2] else "Sin datos"
                    fecha_descifrada = RepositorioNotificaciones.encriptarAES.descifrar(elemento[3]) if elemento[3] else "Sin datos"
                except Exception as ex:
                    mensaje_descifrado = f"Error al descifrar: {ex}"
                    fecha_descifrada = f"Error al descifrar: {ex}"

                notificaciones.append({
                    "IDNotificacion": elemento[0],
                    "IDUsuario": elemento[1],
                    "Mensaje": mensaje_descifrado,
                    "Fecha": fecha_descifrada
                })

            cursor.close()
            conexion.close()
            return notificaciones

        except Exception as ex:
            return {"Error": f"Error al listar notificaciones: {ex}"}

    @staticmethod
    def insertar_notificacion(id_usuario: int, mensaje: str, fecha: str):
        """Inserta una nueva notificación cifrando su mensaje y fecha"""
        try:
            conexion = RepositorioNotificaciones.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            mensaje_cifrado = RepositorioNotificaciones.encriptarAES.cifrar(mensaje)
            fecha_cifrada = RepositorioNotificaciones.encriptarAES.cifrar(fecha)

            consulta = """INSERT INTO Notificaciones (IDUsuario, Mensaje, Fecha) VALUES (?, ?, ?)"""
            cursor.execute(consulta, (id_usuario, mensaje_cifrado, fecha_cifrada))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Notificación insertada correctamente"}
        except Exception as ex:
            return {"Error": f"Error al insertar notificación: {ex}"}

    @staticmethod
    def actualizar_notificacion(id_notificacion: int, mensaje: str, fecha: str):
        """Actualiza una notificación cifrando sus nuevos datos"""
        try:
            conexion = RepositorioNotificaciones.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            mensaje_cifrado = RepositorioNotificaciones.encriptarAES.cifrar(mensaje)
            fecha_cifrada = RepositorioNotificaciones.encriptarAES.cifrar(fecha)

            consulta = """UPDATE Notificaciones SET Mensaje=?, Fecha=? WHERE IDNotificacion=?"""
            cursor.execute(consulta, (mensaje_cifrado, fecha_cifrada, id_notificacion))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Notificación actualizada correctamente"}
        except Exception as ex:
            return {"Error": f"Error al actualizar notificación: {ex}"}

    @staticmethod
    def eliminar_notificacion(id_notificacion: int):
        """Elimina una notificación por su ID"""
        try:
            conexion = RepositorioNotificaciones.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            consulta = """DELETE FROM Notificaciones WHERE IDNotificacion=?"""
            cursor.execute(consulta, (id_notificacion,))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Notificación eliminada correctamente"}
        except Exception as ex:
            return {"Error": f"Error al eliminar notificación: {ex}"}
 