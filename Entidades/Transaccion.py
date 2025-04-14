class Transaccion:
    id: int = 0
    id_usuario: int = 0
    fecha: str = None  # Puedes usar datetime.date si lo prefieres
    id_metodo_pago: int = 0
    id_estado_transaccion: int = 0

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    def GetIdUsuario(self) -> int:
        return self.id_usuario
    def SetIdUsuario(self, value: int) -> None:
        self.id_usuario = value

    def GetFecha(self) -> str:
        return self.fecha
    def SetFecha(self, value: str) -> None:
        self.fecha = value

    def GetIdMetodoPago(self) -> int:
        return self.id_metodo_pago
    def SetIdMetodoPago(self, value: int) -> None:
        self.id_metodo_pago = value

    def GetIdEstadoTransaccion(self) -> int:
        return self.id_estado_transaccion
    def SetIdEstadoTransaccion(self, value: int) -> None:
        self.id_estado_transaccion = value