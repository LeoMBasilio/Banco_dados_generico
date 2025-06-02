from controllers.clienteController import ClienteController # importa a classe ClienteController do arquivo clienteController.py
from views.clienteView import ClienteView # importa a classe ClienteView do arquivo clienteView.py

def main():
    """Função principal para executar o programa de gerenciamento de clientes."""
    controller = ClienteController('clientes.db') # Cria uma instância do controlador de clientes com o banco de dados especificado
    view = ClienteView() # Cria uma instância da visualização de clientes

    while True:
        
        opcao = view.menu() # Exibe o menu principal e obtém a opção escolhida pelo usuário

        match opcao: # Verifica a opção escolhida pelo usuário
            case "1":
                # Obtém os dados do cliente a serem cadastrados
                nome, email, telefone, endereco = view.obter_dados_cliente() # Obtém os dados do cliente através da visualização
                controller.inserir_cliente(nome, email, telefone, endereco) # Insere o cliente no banco de dados através do controlador
                view.mostrar_mensagem("Cliente cadastrado com sucesso!") # Exibe uma mensagem de sucesso após o cadastro do cliente

            case "2":
                # Lista todos os clientes cadastrados
                clientes = controller.listar_clientes() # Obtém a lista de clientes através do controlador
                view.mostrar_clientes(clientes) # Exibe a lista de clientes através da visualização

            case "3":
                # Atualiza os dados de um cliente específico
                cliente_id = view.obter_id_cliente() # Obtém o ID do cliente a ser atualizado
                nome, email = view.obter_dados_cliente() # Obtém os novos dados do cliente através da visualização
                controller.atualizar_cliente(cliente_id, nome, email) # Atualiza os dados do cliente no banco de dados através do controlador
                view.mostrar_mensagem("Cliente atualizado com sucesso!") # Exibe uma mensagem de sucesso após a atualização do cliente

            case "4":
                # Deleta um cliente específico
                cliente_id = view.obter_id_cliente() # Obtém o ID do cliente a ser deletado
                controller.deletar_cliente(cliente_id) # Deleta o cliente do banco de dados através do controlador
                view.mostrar_mensagem("Cliente deletado com sucesso!") # Exibe uma mensagem de sucesso após a exclusão do cliente

            case "0":
                # Encerra o programa
                view.mostrar_mensagem("Encerrando o programa...") # Exibe uma mensagem de encerramento
                break

            case _:
                # Caso a opção escolhida não seja válida, exibe uma mensagem de erro
                view.mostrar_mensagem("Opção inválida, tente novamente.") # Exibe uma mensagem de erro para opção inválida

if __name__ == "__main__": # Verifica se o script está sendo executado diretamente
    main() # Chama a função principal para iniciar o programa
