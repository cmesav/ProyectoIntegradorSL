from Repositorios.RepositorioTransacciones import RepositorioTransacciones

class ServicioTransacciones:
    @staticmethod
    def listar_transacciones():
        return RepositorioTransacciones.listar_transacciones()

    @staticmethod
    def insertar_transaccion(id_usuario: int, fecha: str, id_metodo_pago: int, id_estado_transaccion: int):
        return RepositorioTransacciones.insertar_transaccion(id_usuario, fecha, id_metodo_pago, id_estado_transaccion)

    @staticmethod
    def actualizar_transaccion(id_transaccion: int, fecha: str, id_metodo_pago: int, id_estado_transaccion: int):
        return RepositorioTransacciones.actualizar_transaccion(id_transaccion, fecha, id_metodo_pago, id_estado_transaccion)

    @staticmethod
    def eliminar_transaccion(id_transaccion: int):
        return RepositorioTransacciones.eliminar_transaccion(id_transaccion)
