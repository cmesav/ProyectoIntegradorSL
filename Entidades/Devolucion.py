class Devolucion:
    id: int = 0
    id_transaccion: int = 0
    motivo: str = None
    fecha: str = None

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    def GetIdTransaccion(self) -> int:
        return self.id_transaccion
    def SetIdTransaccion(self, value: int) -> None:
        self.id_transaccion = value

    def GetMotivo(self) -> str:
        return self.motivo
    def SetMotivo(self, value: str) -> None:
        self.motivo = value

    def GetFecha(self) -> str:
        return self.fecha
    def SetFecha(self, value: str) -> None:
        self.fecha = value