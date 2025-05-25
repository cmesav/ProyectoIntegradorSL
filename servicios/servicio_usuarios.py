from repositorios.RepositorioUsuarios import RepositorioUsuarios

class ServicioUsuarios:
    @staticmethod
    def listar_usuarios():
        return RepositorioUsuarios.listar_usuarios()

    @staticmethod
    def insertar_usuario(nombre: str, correo: str, contrasena: str, id_rol: int):
        return RepositorioUsuarios.insertar_usuario(nombre, correo, contrasena, id_rol)

    @staticmethod
    def actualizar_usuario(id_usuario: int, nombre: str, correo: str, contrasena: str):
        return RepositorioUsuarios.actualizar_usuario(id_usuario, nombre, correo, contrasena)

    @staticmethod
    def eliminar_usuario(id_usuario: int):
        return RepositorioUsuarios.eliminar_usuario(id_usuario)
