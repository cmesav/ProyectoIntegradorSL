import pyodbc
from Entidades import Devolucion
from Utilidades import configuracion
from Utilidades import SeguridadAES  

class RepositorioDevoluciones:
    encriptarAES = SeguridadAES.SeguridadAES()  

    def ListarDevoluciones(self) -> list:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT ID, IDTransaccion, Motivo, Fecha FROM Devoluciones"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = Devolucion.Devolucion()
                entidad.SetId(elemento[0])
                entidad.SetIdTransaccion(elemento[1])

                motivo_descifrado = self.encriptarAES.descifrar(elemento[2]) if elemento[2] else "Sin datos"
                fecha_descifrada = self.encriptarAES.descifrar(elemento[3]) if elemento[3] else "Sin datos"

                entidad.SetMotivo(motivo_descifrado)
                entidad.SetFecha(fecha_descifrada)

                lista.append(entidad)

            cursor.close()
            conexion.close()
            return lista

        except Exception as ex:
            print(f"Error al listar devoluciones: {ex}")
            return []

    def InsertarDevolucion(self, id_transaccion: int, motivo: str, fecha: str) -> bool:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            motivo_cifrado = self.encriptarAES.cifrar(motivo)
            fecha_cifrada = self.encriptarAES.cifrar(fecha)

            consulta = """INSERT INTO Devoluciones (IDTransaccion, Motivo, Fecha) VALUES (?, ?, ?)"""
            cursor.execute(consulta, (id_transaccion, motivo_cifrado, fecha_cifrada))
            conexion.commit()

            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al insertar devolución: {ex}")
            return False
