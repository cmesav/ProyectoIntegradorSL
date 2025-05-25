from Repositorios.RepositorioDevoluciones import RepositorioDevoluciones

class ServicioDevoluciones:
    @staticmethod
    def listar_devoluciones():
        return RepositorioDevoluciones.listar_devoluciones()

    @staticmethod
    def insertar_devolucion(id_transaccion: int, motivo: str, fecha: str):
        return RepositorioDevoluciones.insertar_devolucion(id_transaccion, motivo, fecha)

    @staticmethod
    def actualizar_devolucion(id_devolucion: int, id_transaccion: int, motivo: str, fecha: str):
        return RepositorioDevoluciones.actualizar_devolucion(id_devolucion, id_transaccion, motivo, fecha)

    @staticmethod
    def eliminar_devolucion(id_devolucion: int):
        return RepositorioDevoluciones.eliminar_devolucion(id_devolucion)
