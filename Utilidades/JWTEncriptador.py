import jwt

class JWTEncriptador:
    clave: str = None

    def GetClave(self) -> str:
        return self.clave
    def SetClave(self, value: str) -> None:
        self.clave = value

    def GenerarToken(self, datos: dict) -> str:
        try:
            token = jwt.encode(datos, self.clave, algorithm="HS256")
            return token
        except Exception as ex:
            print("Error al generar token:", ex)
            return None

    def DecodificarToken(self, token: str) -> dict:
        try:
            datos = jwt.decode(token, self.clave, algorithms=["HS256"])
            return datos
        except Exception as ex:
            print("Error al decodificar token:", ex)
            return None
