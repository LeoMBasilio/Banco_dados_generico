from controllers.clienteController import ClienteController
from views.clienteView import ClienteView

def main():
    controller = ClienteController('clientes.db')
    view = ClienteView()

    while True:
        opcao = view.menu()

        if opcao == "1":
            nome, email, telefone, endereco = view.obter_dados_cliente()
            controller.inserir_cliente(nome, email, telefone, endereco)
            view.mostrar_mensagem("Cliente cadastrado com sucesso!")

        elif opcao == "2":
            clientes = controller.listar_clientes()
            view.mostrar_clientes(clientes)

        elif opcao == "3":
            cliente_id = view.obter_id_cliente()
            nome, email = view.obter_dados_cliente()
            controller.atualizar_cliente(cliente_id, nome, email)
            view.mostrar_mensagem("Cliente atualizado com sucesso!")

        elif opcao == "4":
            cliente_id = view.obter_id_cliente()
            controller.deletar_cliente(cliente_id)
            view.mostrar_mensagem("Cliente deletado com sucesso!")

        elif opcao == "0":
            view.mostrar_mensagem("Encerrando o programa...")
            break

        else:
            view.mostrar_mensagem("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
