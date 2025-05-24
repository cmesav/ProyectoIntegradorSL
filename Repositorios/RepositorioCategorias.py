import pyodbc
from Entidades.Categoria import Categoria
from Utilidades.configuracion import Configuracion  
from Utilidades.SeguridadAES import SeguridadAES  

class RepositorioCategorias:
    """Clase para gestionar categorías con cifrado AES-GCM"""

    encriptarAES = SeguridadAES()

    @staticmethod
    def obtener_conexion():
        """Obtiene una conexión segura a la base de datos"""
        try:
            return pyodbc.connect(Configuracion.strConnection)
        except Exception as ex:
            return {"Error": f"Fallo en la conexión: {ex}"}

    @staticmethod
    def listar_categorias():
        """Lista las categorías, descifrando los nombres si es posible"""
        try:
            conexion = RepositorioCategorias.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            consulta = """SELECT IDCategoria, NombreCategoria FROM Categorias"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            categorias = []
            for elemento in cursor:
                try:
                    nombre_descifrado = RepositorioCategorias.encriptarAES.descifrar(elemento[1]) if elemento[1] else "Sin datos"
                except Exception as ex:
                    nombre_descifrado = f"Error al descifrar: {ex}"

                categorias.append({
                    "IDCategoria": elemento[0],
                    "NombreCategoria": nombre_descifrado
                })

            cursor.close()
            conexion.close()
            return categorias

        except Exception as ex:
            return {"Error": f"Error al listar categorías: {ex}"}

    @staticmethod
    def insertar_categoria(nombre_categoria: str):
        """Inserta una nueva categoría cifrando su nombre"""
        try:
            conexion = RepositorioCategorias.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            nombre_cifrado = RepositorioCategorias.encriptarAES.cifrar(nombre_categoria)

            consulta = """INSERT INTO Categorias (NombreCategoria) VALUES (?)"""
            cursor.execute(consulta, (nombre_cifrado,))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Categoría insertada correctamente"}
        except Exception as ex:
            return {"Error": f"Error al insertar categoría: {ex}"}

    @staticmethod
    def actualizar_categoria(id_categoria: int, nombre_categoria: str):
        """Actualiza una categoría cifrando su nuevo nombre"""
        try:
            conexion = RepositorioCategorias.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            nombre_cifrado = RepositorioCategorias.encriptarAES.cifrar(nombre_categoria)

            consulta = """UPDATE Categorias SET NombreCategoria=? WHERE IDCategoria=?"""
            cursor.execute(consulta, (nombre_cifrado, id_categoria))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Categoría actualizada correctamente"}
        except Exception as ex:
            return {"Error": f"Error al actualizar categoría: {ex}"}

    @staticmethod
    def eliminar_categoria(id_categoria: int):
        """Elimina una categoría por su ID"""
        try:
            conexion = RepositorioCategorias.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            consulta = """DELETE FROM Categorias WHERE IDCategoria=?"""
            cursor.execute(consulta, (id_categoria,))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Categoría eliminada correctamente"}
        except Exception as ex:
            return {"Error": f"Error al eliminar categoría: {ex}"}
 