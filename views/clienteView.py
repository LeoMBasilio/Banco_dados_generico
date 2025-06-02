class ClienteView:
    @staticmethod
    def menu():
        print("\n====== MENU CLIENTE ======")
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Atualizar Cliente")
        print("4 - Deletar Cliente")
        print("0 - Sair")
        return input("Escolha uma opção: ")

    @staticmethod
    def obter_dados_cliente():
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")
        return nome, email, telefone, endereco

    @staticmethod
    def obter_id_cliente():
        return int(input("ID do cliente: "))

    @staticmethod
    def mostrar_clientes(clientes):
        if clientes:
            print("\n=== Lista de Clientes ===")
            for cliente in clientes:
                print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]}")
            print("==========================\n")
        else:
            print("\nNenhum cliente encontrado.\n")

    @staticmethod
    def mostrar_mensagem(mensagem):
        print(f"\n{mensagem}\n")
