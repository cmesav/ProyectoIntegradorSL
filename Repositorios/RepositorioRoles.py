import pyodbc
from Entidades import Rol
from Utilidades import configuracion

class RepositorioRoles:

    def ListarRoles(self) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM Roles"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = Rol.Rol()
                entidad.SetId(elemento[0])
                entidad.SetNombreRol(elemento[1])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for rol in lista:
                print(f"{rol.GetId()}, {rol.GetNombreRol()}")

        except Exception as ex:
            print(str(ex))

    def InsertarRol(self, nombre_rol: str) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO Roles (NombreRol) VALUES (?)"""
            cursor.execute(consulta, (nombre_rol,))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
 