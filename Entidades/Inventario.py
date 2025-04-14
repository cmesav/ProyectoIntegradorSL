class Inventario:
    id: int = 0
    id_producto: int = 0
    cantidad_disponible: int = 0

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    def GetIdProducto(self) -> int:
        return self.id_producto
    def SetIdProducto(self, value: int) -> None:
        self.id_producto = value

    def GetCantidadDisponible(self) -> int:
        return self.cantidad_disponible
    def SetCantidadDisponible(self, value: int) -> None:
        self.cantidad_disponible = value