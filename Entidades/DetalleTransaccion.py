class DetalleTransaccion:
    id: int = 0
    id_transaccion: int = 0
    id_producto: int = 0
    cantidad: int = 0

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    def GetIdTransaccion(self) -> int:
        return self.id_transaccion
    def SetIdTransaccion(self, value: int) -> None:
        self.id_transaccion = value

    def GetIdProducto(self) -> int:
        return self.id_producto
    def SetIdProducto(self, value: int) -> None:
        self.id_producto = value

    def GetCantidad(self) -> int:
        return self.cantidad
    def SetCantidad(self, value: int) -> None:
        self.cantidad = value