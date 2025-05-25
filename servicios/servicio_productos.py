from repositorios.RepositorioProductos import RepositorioProductos

class ServicioProductos:
    @staticmethod
    def listar_productos():
        return RepositorioProductos.listar_productos()

    @staticmethod
    def listar_productos_con_categoria():
        return RepositorioProductos.listar_productos_con_categoria()

    @staticmethod
    def insertar_producto(nombre: str, id_categoria: int, precio: float):
        return RepositorioProductos.insertar_producto(nombre, id_categoria, precio)

    @staticmethod
    def actualizar_producto(id_producto: int, nombre: str, id_categoria: int, precio: float):
        return RepositorioProductos.actualizar_producto(id_producto, nombre, id_categoria, precio)

    @staticmethod
    def eliminar_producto(id_producto: int):
        return RepositorioProductos.eliminar_producto(id_producto)
