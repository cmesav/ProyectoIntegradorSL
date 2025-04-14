class Producto:
    id: int = 0
    nombre_producto: str = None
    id_categoria: int = 0
    precio: float = 0.0

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    def GetNombreProducto(self) -> str:
        return self.nombre_producto
    def SetNombreProducto(self, value: str) -> None:
        self.nombre_producto = value

    def GetIdCategoria(self) -> int:
        return self.id_categoria
    def SetIdCategoria(self, value: int) -> None:
        self.id_categoria = value

    def GetPrecio(self) -> float:
        return self.precio
    def SetPrecio(self, value: float) -> None:
        self.precio = value