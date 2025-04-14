import pyodbc
from Entidades import HistorialPrecio
from Utilidades import configuracion

class RepositorioHistorialPrecios:

    def ListarHistorialPrecios(self) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM HistorialPrecios"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = HistorialPrecio.HistorialPrecio()
                entidad.SetId(elemento[0])
                entidad.SetIdProducto(elemento[1])
                entidad.SetFecha(elemento[2])
                entidad.SetPrecioAntiguo(elemento[3])
                entidad.SetPrecioNuevo(elemento[4])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for historial in lista:
                print(f"{historial.GetId()}, {historial.GetIdProducto()}, {historial.GetFecha()}, {historial.GetPrecioAntiguo()}, {historial.GetPrecioNuevo()}")

        except Exception as ex:
            print(str(ex))


    def InsertarHistorialPrecio(self, id_producto: int, fecha: str, precio_antiguo: float, precio_nuevo: float) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO HistorialPrecios (IDProducto, Fecha, PrecioAntiguo, PrecioNuevo) VALUES (?, ?, ?, ?)"""
            cursor.execute(consulta, (id_producto, fecha, precio_antiguo, precio_nuevo))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
