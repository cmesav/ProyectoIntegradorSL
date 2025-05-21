import pyodbc
import re
from Entidades import Usuario
from Utilidades.configuracion import Configuracion  
from Utilidades.SeguridadAES import SeguridadAES  

class RepositorioUsuarios:
    """Clase estática para gestionar usuarios con cifrado AES-GCM"""

    encriptarAES = SeguridadAES()

    @staticmethod
    def obtener_conexion():
        """Obtiene una conexión segura a la base de datos"""
        try:
            return pyodbc.connect(Configuracion.strConnection)
        except Exception as ex:
            return {"Error": f"Fallo en la conexión: {ex}"}

    @staticmethod
    def es_correo_valido(correo: str) -> bool:
        """Valida si el correo tiene un formato correcto sin eliminar caracteres especiales válidos"""
        patron_correo = r"^[\w.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(patron_correo, correo) is not None

    @staticmethod
    def listar_usuarios():
        """Lista los usuarios descifrando los datos con validación mejorada"""
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

                    # ✅ Usa la validación corregida
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
        """Inserta un usuario cifrando datos sensibles"""
        try:
            conexion = RepositorioUsuarios.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            # ✅ Validación de correo antes de cifrarlo
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
        """Actualiza un usuario cifrando sus nuevos datos"""
        try:
            conexion = RepositorioUsuarios.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            # ✅ Validación del correo antes de actualizarlo
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
        """Elimina un usuario por su ID"""
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
