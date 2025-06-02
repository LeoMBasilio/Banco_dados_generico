'''
Módulo de visualização para gerenciar clientes.
Este módulo contém a classe ClienteView, que define métodos para exibir menus, obter dados do usuário e mostrar mensagens.
'''
class ClienteView:
    def menu():
        """Exibe o menu principal para o gerenciamento de clientes."""
        print("\n====== MENU CLIENTE ======")
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Atualizar Cliente")
        print("4 - Deletar Cliente")
        print("0 - Sair")
        return input("Escolha uma opção: ")

    def obter_dados_cliente():
        """Obtém os dados do cliente a serem cadastrados ou atualizados."""
        print("\n=== Cadastro de Cliente ===")
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")
        return nome, email, telefone, endereco

    def obter_id_cliente():
        """Obtém o ID do cliente para operações de atualização ou exclusão."""
        return int(input("ID do cliente: "))

    def mostrar_clientes(clientes):
        """Exibe a lista de clientes cadastrados."""
        if clientes:
            print("\n=== Lista de Clientes ===")
            for cliente in clientes:
                print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]}")
            print("==========================\n")
        else:
            print("\nNenhum cliente encontrado.\n")

    def mostrar_mensagem(mensagem):
        """Exibe uma mensagem para o usuário."""
        print(f"\n{mensagem}\n")
