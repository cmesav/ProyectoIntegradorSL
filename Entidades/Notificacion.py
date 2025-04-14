class Notificacion:
    id: int = 0
    id_usuario: int = 0
    mensaje: str = None
    fecha: str = None

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    def GetIdUsuario(self) -> int:
        return self.id_usuario
    def SetIdUsuario(self, value: int) -> None:
        self.id_usuario = value

    def GetMensaje(self) -> str:
        return self.mensaje
    def SetMensaje(self, value: str) -> None:
        self.mensaje = value

    def GetFecha(self) -> str:
        return self.fecha
    def SetFecha(self, value: str) -> None:
        self.fecha = value