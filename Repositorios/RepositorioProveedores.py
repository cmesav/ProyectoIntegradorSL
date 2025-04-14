import pyodbc
from Utilidades import Configuracion

class RepositorioProveedores:

    def ListarProveedores(self) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM Proveedores"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for elemento in cursor:
                print(elemento)

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))

    def InsertarProveedor(self, nombre_proveedor: str, contacto: str) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO Proveedores (NombreProveedor, Contacto) VALUES (?, ?)"""
            cursor.execute(consulta, (nombre_proveedor, contacto))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
