import pyodbc
import re
from Utilidades.configuracion import Configuracion  
from Utilidades.SeguridadAES import SeguridadAES  

class RepositorioUsuarios:

    encriptarAES = SeguridadAES()

    @staticmethod
    def obtener_conexion():
        try:
            return pyodbc.connect(Configuracion.strConnection)
        except Exception as ex:
            return {"Error": f"Fallo en la conexión: {ex}"}

    @staticmethod
    def es_correo_valido(correo: str) -> bool:
        patron_correo = r"^[\w.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(patron_correo, correo) is not None

    @staticmethod
    def listar_usuarios():
        try:
            conexion = RepositorioUsuarios.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            consulta = """SELECT IDUsuario, Nombre, Correo, Contrasena, IDRol FROM Usuarios"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            usuarios = []
            for usuario in cursor:
                try:
                    correo_descifrado = RepositorioUsuarios.encriptarAES.descifrar(usuario[2])

                    if not RepositorioUsuarios.es_correo_valido(correo_descifrado):
                        correo_descifrado = usuario[2]  # Si el descifrado falla, usa el valor cifrado original

                except Exception as ex:
                    correo_descifrado = f"Error al descifrar: {ex}"

                usuarios.append({
                    "ID": usuario[0],
                    "Nombre": RepositorioUsuarios.encriptarAES.descifrar(usuario[1]),
                    "Correo": correo_descifrado,
                    "Contraseña": "******",
                    "Rol": usuario[4]
                })

            cursor.close()
            conexion.close()
            return usuarios

        except Exception as ex:
            return {"Error": f"Error al listar usuarios: {ex}"}

    @staticmethod
    def insertar_usuario(nombre: str, correo: str, contrasena: str, id_rol: int):
        try:
            conexion = RepositorioUsuarios.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            if not RepositorioUsuarios.es_correo_valido(correo):
                return {"Error": "El correo ingresado tiene un formato incorrecto"}

            nombre_cifrado = RepositorioUsuarios.encriptarAES.cifrar(nombre)
            correo_cifrado = RepositorioUsuarios.encriptarAES.cifrar(correo)
            contrasena_cifrada = RepositorioUsuarios.encriptarAES.cifrar(contrasena)

            consulta = """INSERT INTO Usuarios (Nombre, Correo, Contrasena, IDRol) VALUES (?, ?, ?, ?)"""
            cursor.execute(consulta, (nombre_cifrado, correo_cifrado, contrasena_cifrada, id_rol))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Usuario insertado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al insertar usuario: {ex}"}

    @staticmethod
    def actualizar_usuario(id_usuario: int, nombre: str, correo: str, contrasena: str):
        try:
            conexion = RepositorioUsuarios.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()
            
            if not RepositorioUsuarios.es_correo_valido(correo):
                return {"Error": "El correo ingresado tiene un formato incorrecto"}

            nombre_cifrado = RepositorioUsuarios.encriptarAES.cifrar(nombre)
            correo_cifrado = RepositorioUsuarios.encriptarAES.cifrar(correo)
            contrasena_cifrada = RepositorioUsuarios.encriptarAES.cifrar(contrasena)

            consulta = """UPDATE Usuarios SET Nombre=?, Correo=?, Contrasena=? WHERE IDUsuario=?"""
            cursor.execute(consulta, (nombre_cifrado, correo_cifrado, contrasena_cifrada, id_usuario))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Usuario actualizado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al actualizar usuario: {ex}"}

    @staticmethod
    def eliminar_usuario(id_usuario: int):
        try:
            conexion = RepositorioUsuarios.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            consulta = """DELETE FROM Usuarios WHERE IDUsuario=?"""
            cursor.execute(consulta, (id_usuario,))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Usuario eliminado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al eliminar usuario: {ex}"}
