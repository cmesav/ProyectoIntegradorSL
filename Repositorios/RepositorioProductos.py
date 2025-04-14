import pyodbc
from Entidades import Producto
from Utilidades import configuracion

class RepositorioProductos:

    def ListarProductos(self) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM Productos"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = Producto.Producto()
                entidad.SetIdProducto(elemento[0])
                entidad.SetNombreProducto(elemento[1])
                entidad.SetIdCategoria(elemento[2])
                entidad.SetPrecio(elemento[3])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for producto in lista:
                print(f"{producto.GetIdProducto()}, {producto.GetNombreProducto()}, {producto.GetIdCategoria()}, {producto.GetPrecio()}")

        except Exception as ex:
            print(str(ex))


    def ListarProductosConCategoria(self) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT p.IDProducto, p.NombreProducto, c.NombreCategoria, p.Precio 
                          FROM Productos p INNER JOIN Categorias c ON p.IDCategoria = c.IDCategoria"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            for elemento in cursor:
                print(elemento)

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))

    def InsertarProducto(self, nombre: str, id_categoria: int, precio: float) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO Productos (NombreProducto, IDCategoria, Precio) VALUES (?, ?, ?)"""
            cursor.execute(consulta, (nombre, id_categoria, precio))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
