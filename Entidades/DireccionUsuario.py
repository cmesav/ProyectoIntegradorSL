class DireccionUsuario:
    id: int = 0
    id_usuario: int = 0
    direccion: str = None

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    def GetIdUsuario(self) -> int:
        return self.id_usuario
    def SetIdUsuario(self, value: int) -> None:
        self.id_usuario = value

    def GetDireccion(self) -> str:
        return self.direccion
    def SetDireccion(self, value: str) -> None:
        self.direccion = value