import pyodbc
from Entidades import Inventario
from Utilidades import configuracion
from SeguridadAES import SeguridadAES  

class RepositorioInventario:
    encriptarAES = SeguridadAES()  

    def ListarInventario(self) -> list:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT ID, IDProducto, CantidadDisponible FROM Inventario"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = Inventario.Inventario()
                entidad.SetId(elemento[0])
                entidad.SetIdProducto(elemento[1])

                cantidad_descifrada = int(self.encriptarAES.descifrar(elemento[2])) if elemento[2] else 0
                entidad.SetCantidadDisponible(cantidad_descifrada)

                lista.append(entidad)

            cursor.close()
            conexion.close()
            return lista

        except Exception as ex:
            print(f"Error al listar inventario: {ex}")
            return []

    def ActualizarInventario(self, id_producto: int, cantidad_disponible: int) -> bool:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            cantidad_cifrada = self.encriptarAES.cifrar(str(cantidad_disponible))

            consulta = """UPDATE Inventario SET CantidadDisponible = ? WHERE IDProducto = ?"""
            cursor.execute(consulta, (cantidad_cifrada, id_producto))
            conexion.commit()

            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al actualizar inventario: {ex}")
            return False
