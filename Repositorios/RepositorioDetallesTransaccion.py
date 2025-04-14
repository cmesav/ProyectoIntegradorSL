import pyodbc
from Entidades import DetalleTransaccion
from Utilidades import configuracion

class RepositorioDetallesTransaccion:

    def ListarDetallesTransaccion(self) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM DetallesTransaccion"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = DetalleTransaccion.DetalleTransaccion()
                entidad.SetIdDetalle(elemento[0])
                entidad.SetIdTransaccion(elemento[1])
                entidad.SetIdProducto(elemento[2])
                entidad.SetCantidad(elemento[3])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for detalle in lista:
                print(f"{detalle.GetIdDetalle()}, {detalle.GetIdTransaccion()}, {detalle.GetIdProducto()}, {detalle.GetCantidad()}")

        except Exception as ex:
            print(str(ex))


    def InsertarDetalleTransaccion(self, id_transaccion: int, id_producto: int, cantidad: int) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO DetallesTransaccion (IDTransaccion, IDProducto, Cantidad) VALUES (?, ?, ?)"""
            cursor.execute(consulta, (id_transaccion, id_producto, cantidad))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
