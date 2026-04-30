from flask import Flask, jsonify, request
from http import HTTPStatus


class UsuarioViewWeb:
    def __init__(self, controller):
        self.app = Flask(__name__)
        self.controller = controller
        self._configurar_rotas()

    def _configurar_rotas(self):
        @self.app.route("/usuarios/<int:usuario_id>", methods=["GET"])
        def consultar_usuario(usuario_id):
            return self._handle(self.controller.request_consulta, usuario_id)

        @self.app.route("/usuarios", methods=["POST"])
        def criar_usuario():
            dados = request.get_json(silent=True)
            if not dados:
                return self._erro("Corpo da requisição inválido ou ausente.", HTTPStatus.BAD_REQUEST)
            return self._handle(self.controller.request_criacao, dados)

        @self.app.route("/usuarios/<int:usuario_id>", methods=["PUT"])
        def atualizar_usuario(usuario_id):
            dados = request.get_json(silent=True)
            if not dados:
                return self._erro("Corpo da requisição inválido ou ausente.", HTTPStatus.BAD_REQUEST)
            return self._handle(self.controller.request_atualizacao, usuario_id, dados)

        @self.app.route("/usuarios/<int:usuario_id>", methods=["DELETE"])
        def deletar_usuario(usuario_id):
            return self._handle(self.controller.request_delecao, usuario_id)

        @self.app.errorhandler(404)
        def nao_encontrado(e):
            return self._erro("Recurso não encontrado.", HTTPStatus.NOT_FOUND)

        @self.app.errorhandler(405)
        def metodo_nao_permitido(e):
            return self._erro("Método não permitido.", HTTPStatus.METHOD_NOT_ALLOWED)

    def _handle(self, metodo_controller, *args):
        try:
            resposta = metodo_controller(*args)
            status = HTTPStatus.OK if resposta else HTTPStatus.NOT_FOUND
            return jsonify(resposta), status
        except ValueError as e:
            return self._erro(str(e), HTTPStatus.UNPROCESSABLE_ENTITY)
        except Exception as e:
            return self._erro("Erro interno do servidor.", HTTPStatus.INTERNAL_SERVER_ERROR)

    @staticmethod
    def _erro(mensagem: str, status: HTTPStatus):
        return jsonify({"erro": mensagem}), status

    def run(self, host: str = "0.0.0.0", port: int = 5000, debug: bool = False):
        self.app.run(host=host, port=port, debug=debug)
