import pyodbc
from Entidades import DireccionUsuario
from Utilidades import configuracion
from SeguridadAES import SeguridadAES  

class RepositorioDireccionesUsuarios:
    encriptarAES = SeguridadAES()  

    def ListarDireccionesUsuarios(self) -> list:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT ID, IDUsuario, Direccion FROM DireccionesUsuarios"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = DireccionUsuario.DireccionUsuario()
                entidad.SetId(elemento[0])
                entidad.SetIdUsuario(elemento[1])

                direccion_descifrada = self.encriptarAES.descifrar(elemento[2]) if elemento[2] else "Sin datos"
                entidad.SetDireccion(direccion_descifrada)

                lista.append(entidad)

            cursor.close()
            conexion.close()
            return lista

        except Exception as ex:
            print(f"Error al listar direcciones: {ex}")
            return []

    def InsertarDireccionUsuario(self, id_usuario: int, direccion: str) -> bool:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            direccion_cifrada = self.encriptarAES.cifrar(direccion)

            consulta = """INSERT INTO DireccionesUsuarios (IDUsuario, Direccion) VALUES (?, ?)"""
            cursor.execute(consulta, (id_usuario, direccion_cifrada))
            conexion.commit()

            cursor.close()
            conexion.close()
            return True
        except Exception as ex:
            print(f"Error al insertar dirección: {ex}")
