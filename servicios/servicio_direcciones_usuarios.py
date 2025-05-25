from Repositorios.RepositorioDireccionesUsuarios import RepositorioDireccionesUsuarios

class ServicioDireccionesUsuarios:
    @staticmethod
    def listar_direcciones_usuarios():
        return RepositorioDireccionesUsuarios.listar_direcciones_usuarios()

    @staticmethod
    def insertar_direccion_usuario(id_usuario: int, direccion: str):
        return RepositorioDireccionesUsuarios.insertar_direccion_usuario(id_usuario, direccion)

    @staticmethod
    def actualizar_direccion_usuario(id_direccion: int, id_usuario: int, nueva_direccion: str):
        return RepositorioDireccionesUsuarios.actualizar_direccion_usuario(id_direccion, id_usuario, nueva_direccion)

    @staticmethod
    def eliminar_direccion_usuario(id_direccion: int):
        return RepositorioDireccionesUsuarios.eliminar_direccion_usuario(id_direccion)
