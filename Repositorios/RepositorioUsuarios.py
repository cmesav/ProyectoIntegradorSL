import pyodbc
from Entidades import Usuario
from Utilidades import configuracion

class RepositorioUsuarios:

    def ListarUsuarios(self) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM Usuarios"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = Usuario.Usuarios()
                entidad.SetIdUsuario(elemento[0])
                entidad.SetNombre(elemento[1])
                entidad.SetCorreo(elemento[2])
                entidad.SetContrasena(elemento[3])
                entidad.SetIdRol(elemento[4])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for usuario in lista:
                print(f"{usuario.GetIdUsuario()}, {usuario.GetNombre()}, {usuario.GetCorreo()}, {usuario.GetIdRol()}")

        except Exception as ex:
            print(str(ex))

    def ListarUsuariosDetallado(self) -> None:
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection)
            consulta = """SELECT u.IDUsuario, u.Nombre, u.Correo, r.NombreRol 
                          FROM Usuarios u INNER JOIN Roles r ON u.IDRol = r.IDRol"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for elemento in cursor:
                print(elemento)

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))

    def InsertarUsuario(self, nombre: str, correo: str, contrasena: str, id_rol: int) -> None:
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
