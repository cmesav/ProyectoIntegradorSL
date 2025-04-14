class Categoria:
    id: int = 0
    nombre_categoria: str = None

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    def GetNombreCategoria(self) -> str:
        return self.nombre_categoria
    def SetNombreCategoria(self, value: str) -> None:
        self.nombre_categoria = value