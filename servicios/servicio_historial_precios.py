from repositorios.RepositorioHistorialPrecios import RepositorioHistorialPrecios

class ServicioHistorialPrecios:
    @staticmethod
    def listar_historial_precios():
        return RepositorioHistorialPrecios.listar_historial_precios()

    @staticmethod
    def insertar_historial_precio(id_producto: int, fecha: str, precio_antiguo: float, precio_nuevo: float):
        return RepositorioHistorialPrecios.insertar_historial_precio(id_producto, fecha, precio_antiguo, precio_nuevo)

    @staticmethod
    def actualizar_historial_precio(id_historial: int, fecha: str, precio_antiguo: float, precio_nuevo: float):
        return RepositorioHistorialPrecios.actualizar_historial_precio(id_historial, fecha, precio_antiguo, precio_nuevo)

    @staticmethod
    def eliminar_historial_precio(id_historial: int):
        return RepositorioHistorialPrecios.eliminar_historial_precio(id_historial)
