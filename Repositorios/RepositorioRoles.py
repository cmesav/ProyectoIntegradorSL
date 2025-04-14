import pyodbc
from Utilidades import Configuracion

class RepositorioRoles:

    def ListarRoles(self) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM Roles"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for elemento in cursor:
                print(elemento)

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))


class RepositorioUsuarios:

    def ListarUsuarios(self) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM Usuarios"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for elemento in cursor:
                print(elemento)

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))

    def InsertUsuario(self, nombre: str, correo: str, contrasena: str, id_rol: int) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO Usuarios (Nombre, Correo, Contrasena, IDRol) 
                          VALUES (?, ?, ?, ?)"""
            cursor.execute(consulta, (nombre, correo, contrasena, id_rol))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))


class RepositorioProductos:

    def ListarProductos(self) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM Productos"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for elemento in cursor:
                print(elemento)

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
