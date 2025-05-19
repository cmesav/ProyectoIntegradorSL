import pyodbc
from Entidades import Categoria
from Utilidades import configuracion
from Utilidades import SeguridadAES

class RepositorioCategorias:
    encriptarAES = SeguridadAES.SeguridadAES()

    def ListarCategorias(self) -> list:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT ID, NombreCategoria FROM Categorias"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = Categoria.Categoria()
                entidad.SetId(elemento[0])

                nombre_descifrado = self.encriptarAES.descifrar(elemento[1]) if elemento[1] else "Sin datos"
                entidad.SetNombreCategoria(nombre_descifrado)

                lista.append(entidad)

            cursor.close()
            conexion.close()
            return lista

        except Exception as ex:
            print(f"Error al listar categorías: {ex}")
            return []

    def InsertarCategoria(self, nombre_categoria: str) -> bool:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            # Cifrar el nombre de la categoría antes de insertarla en la base de datos
            nombre_cifrado = self.encriptarAES.cifrar(nombre_categoria)

            consulta = """INSERT INTO Categorias (NombreCategoria) VALUES (?)"""
            cursor.execute(consulta, (nombre_cifrado,))
            conexion.commit()

            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al insertar categoría: {ex}")
            return False
