from repositorios.RepositorioEstadoTransaccion import RepositorioEstadoTransaccion

class ServicioEstadoTransaccion:
    @staticmethod
    def listar_estados_transaccion():
        return RepositorioEstadoTransaccion.listar_estados_transaccion()

    @staticmethod
    def insertar_estado_transaccion(nombre_estado: str):
        return RepositorioEstadoTransaccion.insertar_estado_transaccion(nombre_estado)

    @staticmethod
    def actualizar_estado_transaccion(id_estado_transaccion: int, nombre_estado: str):
        return RepositorioEstadoTransaccion.actualizar_estado_transaccion(id_estado_transaccion, nombre_estado)

    @staticmethod
    def eliminar_estado_transaccion(id_estado_transaccion: int):
        return RepositorioEstadoTransaccion.eliminar_estado_transaccion(id_estado_transaccion)
