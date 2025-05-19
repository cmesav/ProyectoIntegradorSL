import pyodbc
from Entidades import MetodoPago
from Utilidades import configuracion
from SeguridadAES import SeguridadAES  

class RepositorioMetodosPago:
    encriptarAES = SeguridadAES()  

    def ListarMetodosPago(self) -> list:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT ID, NombreMetodo FROM MetodosPago"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = MetodoPago.MetodoPago()
                entidad.SetId(elemento[0])

                nombre_descifrado = self.encriptarAES.descifrar(elemento[1]) if elemento[1] else "Sin datos"
                entidad.SetNombreMetodo(nombre_descifrado)

                lista.append(entidad)

            cursor.close()
            conexion.close()
            return lista

        except Exception as ex:
            print(f"Error al listar métodos de pago: {ex}")
            return []

    def InsertarMetodoPago(self, nombre_metodo: str) -> bool:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            nombre_cifrado = self.encriptarAES.cifrar(nombre_metodo)

            consulta = """INSERT INTO MetodosPago (NombreMetodo) VALUES (?)"""
            cursor.execute(consulta, (nombre_cifrado,))
            conexion.commit()

            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al insertar método de pago: {ex}")
            return False