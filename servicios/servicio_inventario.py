from repositorios.RepositorioInventario import RepositorioInventario

class ServicioInventario:
    @staticmethod
    def listar_inventario():
        return RepositorioInventario.listar_inventario()

    @staticmethod
    def insertar_inventario(id_producto: int, cantidad_disponible: int):
        return RepositorioInventario.insertar_inventario(id_producto, cantidad_disponible)

    @staticmethod
    def actualizar_inventario(id_producto: int, cantidad_disponible: int):
        return RepositorioInventario.actualizar_inventario(id_producto, cantidad_disponible)

    @staticmethod
    def eliminar_inventario(id_producto: int):
        return RepositorioInventario.eliminar_inventario(id_producto)
