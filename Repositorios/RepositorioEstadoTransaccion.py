import pyodbc
from Entidades import EstadoTransaccion
from Utilidades import configuracion

class RepositorioEstadoTransaccion:

    def ListarEstadoTransaccion(self) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM EstadoTransaccion"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = EstadoTransaccion.EstadoTransaccion()
                entidad.SetId(elemento[0])
                entidad.SetNombreEstado(elemento[1])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for estado in lista:
                print(f"{estado.GetId()}, {estado.GetNombreEstado()}")

        except Exception as ex:
            print(str(ex))


    def InsertarEstadoTransaccion(self, nombre_estado: str) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO EstadoTransaccion (NombreEstado) VALUES (?)"""
            cursor.execute(consulta, (nombre_estado,))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
