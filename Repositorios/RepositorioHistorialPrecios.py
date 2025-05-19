import pyodbc
from Entidades import HistorialPrecio
from Utilidades import configuracion
from Utilidades import SeguridadAES  

class RepositorioHistorialPrecios:
    encriptarAES = SeguridadAES.SeguridadAES()  

    def ListarHistorialPrecios(self) -> list:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT ID, IDProducto, Fecha, PrecioAntiguo, PrecioNuevo FROM HistorialPrecios"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = HistorialPrecio.HistorialPrecio()
                entidad.SetId(elemento[0])
                entidad.SetIdProducto(elemento[1])

                fecha_descifrada = self.encriptarAES.descifrar(elemento[2]) if elemento[2] else "Sin datos"
                precio_antiguo_descifrado = float(self.encriptarAES.descifrar(elemento[3])) if elemento[3] else 0.0
                precio_nuevo_descifrado = float(self.encriptarAES.descifrar(elemento[4])) if elemento[4] else 0.0

                entidad.SetFecha(fecha_descifrada)
                entidad.SetPrecioAntiguo(precio_antiguo_descifrado)
                entidad.SetPrecioNuevo(precio_nuevo_descifrado)

                lista.append(entidad)

            cursor.close()
            conexion.close()
            return lista

        except Exception as ex:
            print(f"Error al listar historial de precios: {ex}")
            return []

    def InsertarHistorialPrecio(self, id_producto: int, fecha: str, precio_antiguo: float, precio_nuevo: float) -> bool:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            fecha_cifrada = self.encriptarAES.cifrar(fecha)
            precio_antiguo_cifrado = self.encriptarAES.cifrar(str(precio_antiguo))
            precio_nuevo_cifrado = self.encriptarAES.cifrar(str(precio_nuevo))

            consulta = """INSERT INTO HistorialPrecios (IDProducto, Fecha, PrecioAntiguo, PrecioNuevo) VALUES (?, ?, ?, ?)"""
            cursor.execute(consulta, (id_producto, fecha_cifrada, precio_antiguo_cifrado, precio_nuevo_cifrado))
            conexion.commit()

            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al insertar historial de precios: {ex}")
            return False
