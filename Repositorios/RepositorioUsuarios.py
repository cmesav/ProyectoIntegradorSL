import pyodbc
from Entidades import Usuario
from Utilidades import configuracion
from SeguridadAES import SeguridadAES  

class RepositorioUsuarios:
    encriptarAES = SeguridadAES()  

    def ListarUsuarios(self) -> list:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT ID, Nombre, Correo, Contrasena, IDRol FROM Usuarios"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = Usuario.Usuario()
                entidad.SetId(elemento[0])

                nombre_descifrado = self.encriptarAES.descifrar(elemento[1]) if elemento[1] else "Sin datos"
                correo_descifrado = self.encriptarAES.descifrar(elemento[2]) if elemento[2] else "Sin datos"
                contrasena_descifrada = self.encriptarAES.descifrar(elemento[3]) if elemento[3] else "Sin datos"

                entidad.SetNombre(nombre_descifrado)
                entidad.SetCorreo(correo_descifrado)
                entidad.SetContrasena(contrasena_descifrada)
                entidad.SetIdRol(elemento[4])

                lista.append(entidad)

            cursor.close()
            conexion.close()
            return lista

        except Exception as ex:
            print(f"Error al listar usuarios: {ex}")
            return []

    def ListarUsuariosDetallado(self) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT u.IDUsuario, u.Nombre, u.Correo, r.NombreRol 
                          FROM Usuarios u INNER JOIN Roles r ON u.IDRol = r.IDRol"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for elemento in cursor:
                print(elemento)

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(f"Error al listar usuarios detallados: {ex}")

    def InsertarUsuario(self, nombre: str, correo: str, contrasena: str, id_rol: int) -> bool:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            nombre_cifrado = self.encriptarAES.cifrar(nombre)
            correo_cifrado = self.encriptarAES.cifrar(correo)
            contrasena_cifrada = self.encriptarAES.cifrar(contrasena)

            consulta = """INSERT INTO Usuarios (Nombre, Correo, Contrasena, IDRol) 
                          VALUES (?, ?, ?, ?)"""
            cursor.execute(consulta, (nombre_cifrado, correo_cifrado, contrasena_cifrada, id_rol))
            conexion.commit()

            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al insertar usuario: {ex}")
            return False