import pyodbc
from Entidades.Proveedor import Proveedor
from Utilidades.configuracion import Configuracion  
from Utilidades.SeguridadAES import SeguridadAES  

class RepositorioProveedores:
    """Clase para gestionar proveedores con cifrado AES-GCM"""

    encriptarAES = SeguridadAES()

    @staticmethod
    def obtener_conexion():
        """Obtiene una conexión segura a la base de datos"""
        try:
            return pyodbc.connect(Configuracion.strConnection)
        except Exception as ex:
            return {"Error": f"Fallo en la conexión: {ex}"}

    @staticmethod
    def listar_proveedores():
        """Lista los proveedores, descifrando los datos si es posible"""
        try:
            conexion = RepositorioProveedores.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            consulta = """SELECT IDProveedor, NombreProveedor, Contacto FROM Proveedores"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            proveedores = []
            for elemento in cursor:
                try:
                    nombre_descifrado = RepositorioProveedores.encriptarAES.descifrar(elemento[1]) if elemento[1] else "Sin datos"
                    contacto_descifrado = RepositorioProveedores.encriptarAES.descifrar(elemento[2]) if elemento[2] else "Sin datos"
                except Exception as ex:
                    nombre_descifrado = f"Error al descifrar: {ex}"
                    contacto_descifrado = f"Error al descifrar: {ex}"

                proveedores.append({
                    "IDProveedor": elemento[0],
                    "NombreProveedor": nombre_descifrado,
                    "Contacto": contacto_descifrado
                })

            cursor.close()
            conexion.close()
            return proveedores

        except Exception as ex:
            return {"Error": f"Error al listar proveedores: {ex}"}

    @staticmethod
    def insertar_proveedor(nombre_proveedor: str, contacto: str):
        """Inserta un nuevo proveedor cifrando su información"""
        try:
            conexion = RepositorioProveedores.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            nombre_cifrado = RepositorioProveedores.encriptarAES.cifrar(nombre_proveedor)
            contacto_cifrado = RepositorioProveedores.encriptarAES.cifrar(contacto)

            consulta = """INSERT INTO Proveedores (NombreProveedor, Contacto) VALUES (?, ?)"""
            cursor.execute(consulta, (nombre_cifrado, contacto_cifrado))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Proveedor insertado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al insertar proveedor: {ex}"}

    @staticmethod
    def actualizar_proveedor(id_proveedor: int, nombre_proveedor: str, contacto: str):
        """Actualiza un proveedor cifrando sus nuevos datos"""
        try:
            conexion = RepositorioProveedores.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            nombre_cifrado = RepositorioProveedores.encriptarAES.cifrar(nombre_proveedor)
            contacto_cifrado = RepositorioProveedores.encriptarAES.cifrar(contacto)

            consulta = """UPDATE Proveedores SET NombreProveedor=?, Contacto=? WHERE IDProveedor=?"""
            cursor.execute(consulta, (nombre_cifrado, contacto_cifrado, id_proveedor))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Proveedor actualizado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al actualizar proveedor: {ex}"}

    @staticmethod
    def eliminar_proveedor(id_proveedor: int):
        """Elimina un proveedor por su ID"""
        try:
            conexion = RepositorioProveedores.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            consulta = """DELETE FROM Proveedores WHERE IDProveedor=?"""
            cursor.execute(consulta, (id_proveedor,))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Proveedor eliminado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al eliminar proveedor: {ex}"}
 