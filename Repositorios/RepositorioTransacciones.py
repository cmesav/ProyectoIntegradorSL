import pyodbc
from Utilidades import Configuracion

class RepositorioTransacciones:

    def ListarTransacciones(self) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM Transacciones"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for elemento in cursor:
                print(elemento)

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))

    def InsertarTransaccion(self, id_usuario: int, fecha: str, id_metodo_pago: int, id_estado_transaccion: int) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO Transacciones (IDUsuario, Fecha, IDMetodoPago, IDEstadoTransaccion) 
                          VALUES (?, ?, ?, ?)"""
            cursor.execute(consulta, (id_usuario, fecha, id_metodo_pago, id_estado_transaccion))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
