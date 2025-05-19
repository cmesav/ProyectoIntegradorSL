import pyodbc
from Entidades import Proveedor
from Utilidades import configuracion
from SeguridadAES import SeguridadAES  

class RepositorioProveedores:
    encriptarAES = SeguridadAES()  

    def ListarProveedores(self) -> list:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT ID, NombreProveedor, Contacto FROM Proveedores"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = Proveedor.Proveedor()
                entidad.SetId(elemento[0])

                nombre_descifrado = self.encriptarAES.descifrar(elemento[1]) if elemento[1] else "Sin datos"
                contacto_descifrado = self.encriptarAES.descifrar(elemento[2]) if elemento[2] else "Sin datos"

                entidad.SetNombreProveedor(nombre_descifrado)
                entidad.SetContacto(contacto_descifrado)

                lista.append(entidad)

            cursor.close()
            conexion.close()
            return lista

        except Exception as ex:
            print(f"Error al listar proveedores: {ex}")
            return []

    def InsertarProveedor(self, nombre_proveedor: str, contacto: str) -> bool:
        """Cifra y almacena un nuevo proveedor en la base de datos"""
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            nombre_cifrado = self.encriptarAES.cifrar(nombre_proveedor)
            contacto_cifrado = self.encriptarAES.cifrar(contacto)

            consulta = """INSERT INTO Proveedores (NombreProveedor, Contacto) VALUES (?, ?)"""
            cursor.execute(consulta, (nombre_cifrado, contacto_cifrado))
            conexion.commit()

            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al insertar proveedor: {ex}")
            return False