from repositorios.RepositorioMetodosPago import RepositorioMetodosPago

class ServicioMetodosPago:
    @staticmethod
    def listar_metodos_pago():
        return RepositorioMetodosPago.listar_metodos_pago()

    @staticmethod
    def insertar_metodo_pago(nombre_metodo: str):
        return RepositorioMetodosPago.insertar_metodo_pago(nombre_metodo)

    @staticmethod
    def actualizar_metodo_pago(id_metodo_pago: int, nombre_metodo: str):
        return RepositorioMetodosPago.actualizar_metodo_pago(id_metodo_pago, nombre_metodo)

    @staticmethod
    def eliminar_metodo_pago(id_metodo_pago: int):
        return RepositorioMetodosPago.eliminar_metodo_pago(id_metodo_pago)
