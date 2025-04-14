import pyodbc
from Entidades import Devolucion
from Utilidades import configuracion

class RepositorioDevoluciones:

    def ListarDevoluciones(self) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM Devoluciones"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = Devolucion.Devolucion()
                entidad.SetIdDevolucion(elemento[0])
                entidad.SetIdTransaccion(elemento[1])
                entidad.SetMotivo(elemento[2])
                entidad.SetFecha(elemento[3])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for devolucion in lista:
                print(f"{devolucion.GetIdDevolucion()}, {devolucion.GetIdTransaccion()}, {devolucion.GetMotivo()}, {devolucion.GetFecha()}")

        except Exception as ex:
            print(str(ex))


    def InsertarDevolucion(self, id_transaccion: int, motivo: str, fecha: str) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO Devoluciones (IDTransaccion, Motivo, Fecha) VALUES (?, ?, ?)"""
            cursor.execute(consulta, (id_transaccion, motivo, fecha))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
