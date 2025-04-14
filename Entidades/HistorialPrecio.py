class HistorialPrecio:
    id: int = 0
    id_producto: int = 0
    fecha: str = None
    precio_antiguo: float = 0.0
    precio_nuevo: float = 0.0

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    def GetIdProducto(self) -> int:
        return self.id_producto
    def SetIdProducto(self, value: int) -> None:
        self.id_producto = value

    def GetFecha(self) -> str:
        return self.fecha
    def SetFecha(self, value: str) -> None:
        self.fecha = value

    def GetPrecioAntiguo(self) -> float:
        return self.precio_antiguo
    def SetPrecioAntiguo(self, value: float) -> None:
        self.precio_antiguo = value

    def GetPrecioNuevo(self) -> float:
        return self.precio_nuevo
    def SetPrecioNuevo(self, value: float) -> None:
        self.precio_nuevo = value