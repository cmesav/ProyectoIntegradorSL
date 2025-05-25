from Repositorios.RepositorioNotificaciones import RepositorioNotificaciones

class ServicioNotificaciones:
    @staticmethod
    def listar_notificaciones():
        return RepositorioNotificaciones.listar_notificaciones()

    @staticmethod
    def insertar_notificacion(id_usuario: int, mensaje: str, fecha: str):
        return RepositorioNotificaciones.insertar_notificacion(id_usuario, mensaje, fecha)

    @staticmethod
    def actualizar_notificacion(id_notificacion: int, mensaje: str, fecha: str):
        return RepositorioNotificaciones.actualizar_notificacion(id_notificacion, mensaje, fecha)

    @staticmethod
    def eliminar_notificacion(id_notificacion: int):
        return RepositorioNotificaciones.eliminar_notificacion(id_notificacion)
