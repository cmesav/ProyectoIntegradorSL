class Usuario:
    id: int = 0
    nombre: str = None
    correo: str = None
    contrasena: str = None
    id_rol: int = 0

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    def GetNombre(self) -> str:
        return self.nombre
    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetCorreo(self) -> str:
        return self.correo
    def SetCorreo(self, value: str) -> None:
        self.correo = value

    def GetContrasena(self) -> str:
        return self.contrasena
    def SetContrasena(self, value: str) -> None:
        self.contrasena = value

    def GetIdRol(self) -> int:
        return self.id_rol
    def SetIdRol(self, value: int) -> None:
        self.id_rol = value