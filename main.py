from repository.usuario_repository import UsuarioRepository
from service.usuario_service import UsuarioService
from view.usuario_view import UsuarioView


def main():
    repository = UsuarioRepository()
    service = UsuarioService(repository)
    view = UsuarioView()

    while True:
        view.mostrar_menu()
        opcao = input("Opção: ")

        if opcao == "1":
            nome, email = view.obter_dados_usuario()
            try:
                service.criar_usuario(nome, email)
                view.mostrar_mensagem("Usuário criado com sucesso!")
            except ValueError as e:
                view.mostrar_mensagem(f"Erro: {e}")
        elif opcao == "2":
            usuarios = service.listar_usuarios()
            view.mostrar_usuarios(usuarios)
        elif opcao == "0":
            break
        else:
            view.mostrar_mensagem("Opção inválida")


if __name__ == "__main__":
    main()
