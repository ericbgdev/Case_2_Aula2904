from model.usuario import Usuario
from repository.usuario_repository import UsuarioRepository


class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str) -> Usuario:
        if "@" not in email:
            raise ValueError("Email inválido")
        usuario = Usuario(nome, email)
        return self.repository.salvar(usuario)

    def listar_usuarios(self):
        return self.repository.listar()

    def buscar_por_id(self, usuario_id: int):
        return self.repository.buscar_por_id(usuario_id)

    def atualizar(self, usuario_id: int, dados: dict):
        usuario = self.repository.buscar_por_id(usuario_id)
        if not usuario:
            return None
        usuario.nome = dados.get("nome", usuario.nome)
        usuario.email = dados.get("email", usuario.email)
        if "@" not in usuario.email:
            raise ValueError("Email inválido")
        return self.repository.atualizar(usuario)

    def deletar(self, usuario_id: int):
        self.repository.deletar(usuario_id)
