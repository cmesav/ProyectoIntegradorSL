import pyodbc
from Entidades import Inventario
from Utilidades import configuracion

class RepositorioInventario:

    def ListarInventario(self) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM Inventario"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = Inventario.Inventario()
                entidad.SetId(elemento[0])
                entidad.SetIdProducto(elemento[1])
                entidad.SetCantidadDisponible(elemento[2])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for inventario in lista:
                print(f"{inventario.GetId()}, {inventario.GetIdProducto()}, {inventario.GetCantidadDisponible()}")

        except Exception as ex:
            print(str(ex))

    def ActualizarInventario(self, id_producto: int, cantidad_disponible: int) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """UPDATE Inventario SET CantidadDisponible = ? WHERE IDProducto = ?"""
            cursor.execute(consulta, (cantidad_disponible, id_producto))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
