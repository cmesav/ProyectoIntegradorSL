class MetodoPago:
    id: int = 0
    nombre_metodo: str = None

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    def GetNombreMetodo(self) -> str:
        return self.nombre_metodo
    def SetNombreMetodo(self, value: str) -> None:
        self.nombre_metodo = value