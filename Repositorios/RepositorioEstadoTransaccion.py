import pyodbc
from Entidades import EstadoTransaccion
from Utilidades import configuracion
from SeguridadAES import SeguridadAES 

class RepositorioEstadoTransaccion:
    encriptarAES = SeguridadAES()  

    def ListarEstadoTransaccion(self) -> list:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT ID, NombreEstado FROM EstadoTransaccion"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = EstadoTransaccion.EstadoTransaccion()
                entidad.SetId(elemento[0])

                nombre_descifrado = self.encriptarAES.descifrar(elemento[1]) if elemento[1] else "Sin datos"
                entidad.SetNombreEstado(nombre_descifrado)

                lista.append(entidad)

            cursor.close()
            conexion.close()
            return lista

        except Exception as ex:
            print(f"Error al listar estados de transacción: {ex}")
            return []

    def InsertarEstadoTransaccion(self, nombre_estado: str) -> bool:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            nombre_cifrado = self.encriptarAES.cifrar(nombre_estado)

            consulta = """INSERT INTO EstadoTransaccion (NombreEstado) VALUES (?)"""
            cursor.execute(consulta, (nombre_cifrado,))
            conexion.commit()

            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al insertar estado de transacción: {ex}")
            return False
