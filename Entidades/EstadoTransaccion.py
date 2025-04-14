class EstadoTransaccion:
    id: int = 0
    nombre_estado: str = None

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    def GetNombreEstado(self) -> str:
        return self.nombre_estado
    def SetNombreEstado(self, value: str) -> None:
        self.nombre_estado = value