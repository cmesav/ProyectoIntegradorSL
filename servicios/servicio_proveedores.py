from Repositorios.RepositorioProveedores import RepositorioProveedores

class ServicioProveedores:
    @staticmethod
    def listar_proveedores():
        return RepositorioProveedores.listar_proveedores()

    @staticmethod
    def insertar_proveedor(nombre_proveedor: str, contacto: str):
        return RepositorioProveedores.insertar_proveedor(nombre_proveedor, contacto)

    @staticmethod
    def actualizar_proveedor(id_proveedor: int, nombre_proveedor: str, contacto: str):
        return RepositorioProveedores.actualizar_proveedor(id_proveedor, nombre_proveedor, contacto)

    @staticmethod
    def eliminar_proveedor(id_proveedor: int):
        return RepositorioProveedores.eliminar_proveedor(id_proveedor)
