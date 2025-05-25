import pyodbc
from utilidades.configuracion import Configuracion  
from utilidades.SeguridadAES import SeguridadAES  

class RepositorioRoles:

    encriptarAES = SeguridadAES()

    @staticmethod
    def obtener_conexion():
        try:
            return pyodbc.connect(Configuracion.strConnection)
        except Exception as ex:
            return {"Error": f"Fallo en la conexión: {ex}"}

    @staticmethod
    def listar_roles():
        try:
            conexion = RepositorioRoles.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            consulta = """SELECT IDRol, NombreRol FROM Roles"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            roles = []
            for elemento in cursor:
                try:
                    nombre_descifrado = RepositorioRoles.encriptarAES.descifrar(elemento[1]) if elemento[1] else "Sin datos"
                except Exception as ex:
                    nombre_descifrado = f"Error al descifrar: {ex}"

                roles.append({
                    "IDRol": elemento[0],
                    "NombreRol": nombre_descifrado
                })

            cursor.close()
            conexion.close()
            return roles

        except Exception as ex:
            return {"Error": f"Error al listar roles: {ex}"}

    @staticmethod
    def insertar_rol(nombre_rol: str):
        try:
            conexion = RepositorioRoles.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            nombre_cifrado = RepositorioRoles.encriptarAES.cifrar(nombre_rol)

            consulta = """INSERT INTO Roles (NombreRol) VALUES (?)"""
            cursor.execute(consulta, (nombre_cifrado,))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Rol insertado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al insertar rol: {ex}"}

    @staticmethod
    def actualizar_rol(id_rol: int, nombre_rol: str):
        try:
            conexion = RepositorioRoles.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            nombre_cifrado = RepositorioRoles.encriptarAES.cifrar(nombre_rol)

            consulta = """UPDATE Roles SET NombreRol=? WHERE IDRol=?"""
            cursor.execute(consulta, (nombre_cifrado, id_rol))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Rol actualizado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al actualizar rol: {ex}"}

    @staticmethod
    def eliminar_rol(id_rol: int):
        try:
            conexion = RepositorioRoles.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            consulta = """DELETE FROM Roles WHERE IDRol=?"""
            cursor.execute(consulta, (id_rol,))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Rol eliminado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al eliminar rol: {ex}"}

 