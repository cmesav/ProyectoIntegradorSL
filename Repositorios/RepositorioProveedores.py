import pyodbc
from Entidades import Proveedores
from Utilidades import configuracion

class RepositorioProveedores:

    def ListarProveedores(self) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM Proveedores"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = Proveedores.Proveedores()
                entidad.SetIdProveedor(elemento[0])
                entidad.SetNombreProveedor(elemento[1])
                entidad.SetContacto(elemento[2])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for proveedor in lista:
                print(f"{proveedor.GetIdProveedor()}, {proveedor.GetNombreProveedor()}, {proveedor.GetContacto()}")

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
