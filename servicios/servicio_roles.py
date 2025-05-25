from Repositorios.RepositorioRoles import RepositorioRoles

class ServicioRoles:
    @staticmethod
    def listar_roles():
        return RepositorioRoles.listar_roles()

    @staticmethod
    def insertar_rol(nombre_rol: str):
        return RepositorioRoles.insertar_rol(nombre_rol)

    @staticmethod
    def actualizar_rol(id_rol: int, nombre_rol: str):
        return RepositorioRoles.actualizar_rol(id_rol, nombre_rol)

    @staticmethod
    def eliminar_rol(id_rol: int):
        return RepositorioRoles.eliminar_rol(id_rol)
