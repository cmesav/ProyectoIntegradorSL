import pyodbc
from Entidades import Categoria
from Utilidades import configuracion

class RepositorioCategorias:

    def ListarCategorias(self) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM Categorias"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = Categoria.Categoria()
                entidad.SetIdCategoria(elemento[0])
                entidad.SetNombreCategoria(elemento[1])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for categoria in lista:
                print(f"{categoria.GetIdCategoria()}, {categoria.GetNombreCategoria()}")

        except Exception as ex:
            print(str(ex))


    def InsertarCategoria(self, nombre_categoria: str) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO Categorias (NombreCategoria) VALUES (?)"""
            cursor.execute(consulta, (nombre_categoria,))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
