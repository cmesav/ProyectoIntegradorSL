import pyodbc
from Entidades import Producto
from Utilidades import configuracion
from SeguridadAES import SeguridadAES  

class RepositorioProductos:
    encriptarAES = SeguridadAES()  

    def ListarProductos(self) -> list:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT ID, NombreProducto, IDCategoria, Precio FROM Productos"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = Producto.Producto()
                entidad.SetId(elemento[0])

                nombre_descifrado = self.encriptarAES.descifrar(elemento[1]) if elemento[1] else "Sin datos"
                precio_descifrado = float(self.encriptarAES.descifrar(elemento[3])) if elemento[3] else 0.0

                entidad.SetNombreProducto(nombre_descifrado)
                entidad.SetIdCategoria(elemento[2])
                entidad.SetPrecio(precio_descifrado)

                lista.append(entidad)

            cursor.close()
            conexion.close()
            return lista

        except Exception as ex:
            print(f"Error al listar productos: {ex}")
            return []

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
            print(f"Error al listar productos con categoría: {ex}")

    def InsertarProducto(self, nombre: str, id_categoria: int, precio: float) -> bool:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            nombre_cifrado = self.encriptarAES.cifrar(nombre)
            precio_cifrado = self.encriptarAES.cifrar(str(precio))

            consulta = """INSERT INTO Productos (NombreProducto, IDCategoria, Precio) VALUES (?, ?, ?)"""
            cursor.execute(consulta, (nombre_cifrado, id_categoria, precio_cifrado))
            conexion.commit()

            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al insertar producto: {ex}")
            return False