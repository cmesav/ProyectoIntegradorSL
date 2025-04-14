import pyodbc
from Entidades import DireccionUsuario
from Utilidades import configuracion

class RepositorioDireccionesUsuarios:

    def ListarDireccionesUsuarios(self) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM DireccionesUsuarios"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = DireccionUsuario.DireccionUsuario()
                entidad.SetId(elemento[0])
                entidad.SetIdUsuario(elemento[1])
                entidad.SetDireccion(elemento[2])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for direccion in lista:
                print(f"{direccion.GetId()}, {direccion.GetIdUsuario()}, {direccion.GetDireccion()}")

        except Exception as ex:
            print(str(ex))


    def InsertarDireccionUsuario(self, id_usuario: int, direccion: str) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO DireccionesUsuarios (IDUsuario, Direccion) VALUES (?, ?)"""
            cursor.execute(consulta, (id_usuario, direccion))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
