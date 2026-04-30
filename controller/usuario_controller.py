from service.usuario_service import UsuarioService


class UsuarioController:
    def __init__(self, service: UsuarioService):
        self.service = service

    def request_consulta(self, usuario_id: int):
        usuario = self.service.buscar_por_id(usuario_id)
        return usuario.to_dict() if usuario else None

    def request_criacao(self, dados: dict):
        usuario = self.service.criar_usuario(dados["nome"], dados["email"])
        return usuario.to_dict()

    def request_atualizacao(self, usuario_id: int, dados: dict):
        usuario = self.service.atualizar(usuario_id, dados)
        return usuario.to_dict() if usuario else None

    def request_delecao(self, usuario_id: int):
        self.service.deletar(usuario_id)
        return {"mensagem": "Usuário removido com sucesso."}
