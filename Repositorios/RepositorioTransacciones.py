import pyodbc
from Entidades import Transaccion
from Utilidades import configuracion
from SeguridadAES import SeguridadAES  

class RepositorioTransacciones:
    encriptarAES = SeguridadAES()  

    def ListarTransacciones(self) -> list:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT ID, IDUsuario, Fecha, IDMetodoPago, IDEstadoTransaccion FROM Transacciones"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = Transaccion.Transaccion()
                entidad.SetId(elemento[0])
                entidad.SetIdUsuario(elemento[1])

                fecha_descifrada = self.encriptarAES.descifrar(elemento[2]) if elemento[2] else "Sin datos"
                entidad.SetFecha(fecha_descifrada)

                entidad.SetIdMetodoPago(elemento[3])
                entidad.SetIdEstadoTransaccion(elemento[4])

                lista.append(entidad)

            cursor.close()
            conexion.close()
            return lista

        except Exception as ex:
            print(f"Error al listar transacciones: {ex}")
            return []

    def InsertarTransaccion(self, id_usuario: int, fecha: str, id_metodo_pago: int, id_estado_transaccion: int) -> bool:
       
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            fecha_cifrada = self.encriptarAES.cifrar(fecha)

            consulta = """INSERT INTO Transacciones (IDUsuario, Fecha, IDMetodoPago, IDEstadoTransaccion) 
                          VALUES (?, ?, ?, ?)"""
            cursor.execute(consulta, (id_usuario, fecha_cifrada, id_metodo_pago, id_estado_transaccion))
            conexion.commit()

            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al insertar transacción: {ex}")
            return False