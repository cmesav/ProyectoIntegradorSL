import pyodbc
from Entidades import MetodoPago
from Utilidades import configuracion

class RepositorioMetodosPago:

    def ListarMetodosPago(self) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            consulta = """SELECT * FROM MetodosPago"""
            cursor = conexion.cursor()
            cursor.execute(consulta)

            lista = []
            for elemento in cursor:
                entidad = MetodoPago.MetodoPago()
                entidad.SetId(elemento[0])
                entidad.SetNombreMetodo(elemento[1])
                lista.append(entidad)

            cursor.close()
            conexion.close()

            for metodo in lista:
                print(f"{metodo.GetId()}, {metodo.GetNombreMetodo()}")

        except Exception as ex:
            print(str(ex))


    def InsertarMetodoPago(self, nombre_metodo: str) -> None:
        try:
            conexion = pyodbc.connect(configuracion.Configuracion.strConnection)
            cursor = conexion.cursor()

            consulta = """INSERT INTO MetodosPago (NombreMetodo) VALUES (?)"""
            cursor.execute(consulta, (nombre_metodo,))
            conexion.commit()

            cursor.close()
            conexion.close()
        except Exception as ex:
            print(str(ex))
