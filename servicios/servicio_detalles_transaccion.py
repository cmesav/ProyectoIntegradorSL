from repositorios.RepositorioDetallesTransaccion import RepositorioDetallesTransaccion

class ServicioDetallesTransaccion:
    @staticmethod
    def listar_detalles_transaccion():
        return RepositorioDetallesTransaccion.listar_detalles_transaccion()

    @staticmethod
    def insertar_detalle_transaccion(id_transaccion: int, id_producto: int, cantidad: int):
        return RepositorioDetallesTransaccion.insertar_detalle_transaccion(id_transaccion, id_producto, cantidad)

    @staticmethod
    def actualizar_detalle_transaccion(id_detalle: int, id_transaccion: int, id_producto: int, cantidad: int):
        return RepositorioDetallesTransaccion.actualizar_detalle_transaccion(id_detalle, id_transaccion, id_producto, cantidad)

    @staticmethod
    def eliminar_detalle_transaccion(id_detalle: int):
        return RepositorioDetallesTransaccion.eliminar_detalle_transaccion(id_detalle)
