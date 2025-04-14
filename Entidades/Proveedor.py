class Proveedor:
    id: int = 0
    nombre_proveedor: str = None
    contacto: str = None

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    def GetNombreProveedor(self) -> str:
        return self.nombre_proveedor
    def SetNombreProveedor(self, value: str) -> None:
        self.nombre_proveedor = value

    def GetContacto(self) -> str:
        return self.contacto
    def SetContacto(self, value: str) -> None:
        self.contacto = value