import pyodbc
from Entidades.Categoria import Categoria
from Utilidades.configuracion import Configuracion  
from Utilidades.SeguridadAES import SeguridadAES  

class RepositorioCategorias:

    encriptarAES = SeguridadAES()

    @staticmethod
    def obtener_conexion():
        try:
            return pyodbc.connect(Configuracion.strConnection)
        except Exception as ex:
            return {"Error": f"Fallo en la conexión: {ex}"}

    @staticmethod
    def listar_categorias():
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
