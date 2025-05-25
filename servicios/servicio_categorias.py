from repositorios.RepositorioCategorias import RepositorioCategorias

class ServicioCategorias:
    @staticmethod
    def listar_categorias():
        return RepositorioCategorias.listar_categorias()

    @staticmethod
    def insertar_categoria(nombre_categoria: str):
        return RepositorioCategorias.insertar_categoria(nombre_categoria)

    @staticmethod
    def actualizar_categoria(id_categoria: int, nombre_categoria: str):
        return RepositorioCategorias.actualizar_categoria(id_categoria, nombre_categoria)

    @staticmethod
    def eliminar_categoria(id_categoria: int):
        return RepositorioCategorias.eliminar_categoria(id_categoria)
