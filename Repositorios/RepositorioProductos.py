import pyodbc
from Entidades.Producto import Producto
from Utilidades.configuracion import Configuracion  
from Utilidades.SeguridadAES import SeguridadAES  

class RepositorioProductos:

    encriptarAES = SeguridadAES()

    @staticmethod
    def obtener_conexion():
        try:
            return pyodbc.connect(Configuracion.strConnection)
        except Exception as ex:
            return {"Error": f"Fallo en la conexión: {ex}"}

    @staticmethod
    def listar_productos():
        try:
            conexion = RepositorioProductos.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            consulta = """SELECT IDProducto, NombreProducto, IDCategoria, Precio FROM Productos"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            productos = []
            for elemento in cursor:
                try:
                    nombre_descifrado = RepositorioProductos.encriptarAES.descifrar(elemento[1]) if elemento[1] else "Sin datos"
                    precio_descifrado = float(RepositorioProductos.encriptarAES.descifrar(elemento[3])) if elemento[3] else 0.0
                except Exception as ex:
                    nombre_descifrado = f"Error al descifrar: {ex}"
                    precio_descifrado = f"Error al descifrar: {ex}"

                productos.append({
                    "IDProducto": elemento[0],
                    "NombreProducto": nombre_descifrado,
                    "IDCategoria": elemento[2],
                    "Precio": precio_descifrado
                })

            cursor.close()
            conexion.close()
            return productos

        except Exception as ex:
            return {"Error": f"Error al listar productos: {ex}"}

    @staticmethod
    def listar_productos_con_categoria():
        try:
            conexion = RepositorioProductos.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            consulta = """SELECT p.IDProducto, p.NombreProducto, c.NombreCategoria, p.Precio 
                          FROM Productos p INNER JOIN Categorias c ON p.IDCategoria = c.IDCategoria"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            productos_categoria = []
            for elemento in cursor:
                productos_categoria.append({
                    "IDProducto": elemento[0],
                    "NombreProducto": elemento[1],
                    "NombreCategoria": elemento[2],
                    "Precio": elemento[3]
                })

            cursor.close()
            conexion.close()
            return productos_categoria

        except Exception as ex:
            return {"Error": f"Error al listar productos con categoría: {ex}"}

    @staticmethod
    def insertar_producto(nombre: str, id_categoria: int, precio: float):
        try:
            conexion = RepositorioProductos.obtener_conexion()
            if isinstance(conexion, dict):
                return conexion

            cursor = conexion.cursor()

            nombre_cifrado = RepositorioProductos.encriptarAES.cifrar(nombre)
            precio_cifrado = RepositorioProductos.encriptarAES.cifrar(str(precio))

            consulta = """INSERT INTO Productos (NombreProducto, IDCategoria, Precio) VALUES (?, ?, ?)"""
            cursor.execute(consulta, (nombre_cifrado, id_categoria, precio_cifrado))
            conexion.commit()

            cursor.close()
            conexion.close()
            return {"Mensaje": "Producto insertado correctamente"}
        except Exception as ex:
            return {"Error": f"Error al insertar producto: {ex}"}
