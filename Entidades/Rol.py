class Rol:
    id: int = 0
    nombre_rol: str = None

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    def GetNombreRol(self) -> str:
        return self.nombre_rol
    def SetNombreRol(self, value: str) -> None:
        self.nombre_rol = value