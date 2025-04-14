import pyodbc
from Entidades import Transaccion
from Utilidades import configuracion

class RepositorioTransacciones:

    def ListarTransacciones(self) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM Transacciones"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = Transaccion.Transaccion()
                entidad.SetId(elemento[0])
                entidad.SetIdUsuario(elemento[1])
                entidad.SetFecha(elemento[2])
                entidad.SetIdMetodoPago(elemento[3])
                entidad.SetIdEstadoTransaccion(elemento[4])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for transaccion in lista:
                print(f"{transaccion.GetId()}, {transaccion.GetIdUsuario()}, {transaccion.GetFecha()}, {transaccion.GetIdMetodoPago()}, {transaccion.GetIdEstadoTransaccion()}")

        except Exception as ex:
            print(str(ex))


    def InsertarTransaccion(self, id_usuario: int, fecha: str, id_metodo_pago: int, id_estado_transaccion: int) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO Transacciones (IDUsuario, Fecha, IDMetodoPago, IDEstadoTransaccion) 
                          VALUES (?, ?, ?, ?)"""
            cursor.execute(consulta, (id_usuario, fecha, id_metodo_pago, id_estado_transaccion))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
