import pyodbc
from Entidades import Rol
from Utilidades import configuracion
from SeguridadAES import SeguridadAES  

class RepositorioRoles:
    encriptarAES = SeguridadAES()  

    def ListarRoles(self) -> list:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT ID, NombreRol FROM Roles"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = Rol.Rol()
                entidad.SetId(elemento[0])

                nombre_descifrado = self.encriptarAES.descifrar(elemento[1]) if elemento[1] else "Sin datos"
                entidad.SetNombreRol(nombre_descifrado)

                lista.append(entidad)

            cursor.close()
            conexion.close()
            return lista

        except Exception as ex:
            print(f"Error al listar roles: {ex}")
            return []

    def InsertarRol(self, nombre_rol: str) -> bool:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            nombre_cifrado = self.encriptarAES.cifrar(nombre_rol)

            consulta = """INSERT INTO Roles (NombreRol) VALUES (?)"""
            cursor.execute(consulta, (nombre_cifrado,))
            conexion.commit()

            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al insertar rol: {ex}")
            return False