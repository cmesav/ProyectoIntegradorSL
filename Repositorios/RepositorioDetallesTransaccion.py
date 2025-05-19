import pyodbc
from Entidades import DetalleTransaccion
from Utilidades import configuracion
from Utilidades import SeguridadAES  

class RepositorioDetallesTransaccion:
    encriptarAES = SeguridadAES.SeguridadAES()

    def ListarDetallesTransaccion(self) -> list:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT ID, IDTransaccion, IDProducto, Cantidad FROM DetallesTransaccion"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = DetalleTransaccion.DetalleTransaccion()
                entidad.SetId(elemento[0])
                entidad.SetIdTransaccion(elemento[1])
                entidad.SetIdProducto(elemento[2])

                cantidad_descifrada = self.encriptarAES.descifrar(elemento[3]) if elemento[3] else "Sin datos"
                entidad.SetCantidad(cantidad_descifrada)

                lista.append(entidad)

            cursor.close()
            conexion.close()
            return lista

        except Exception as ex:
            print(f"Error al listar detalles de transacción: {ex}")
            return []

    def InsertarDetalleTransaccion(self, id_transaccion: int, id_producto: int, cantidad: int) -> bool:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            # Cifrar la cantidad antes de insertarla en la base de datos
            cantidad_cifrada = self.encriptarAES.cifrar(str(cantidad))

            consulta = """INSERT INTO DetallesTransaccion (IDTransaccion, IDProducto, Cantidad) VALUES (?, ?, ?)"""
            cursor.execute(consulta, (id_transaccion, id_producto, cantidad_cifrada))
            conexion.commit()

            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al insertar detalle de transacción: {ex}")
            return False
