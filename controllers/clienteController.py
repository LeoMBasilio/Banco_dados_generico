from models.clienteModel import ClienteModel # importa a classe ClienteModel do arquivo clienteModel.py

class ClienteController:
    ''' Classe ClienteController para gerenciar operações de clientes.
    Esta classe utiliza a ClienteModel para realizar operações CRUD (Create, Read, Update, Delete) em clientes.
    '''
    def __init__(self, banco):
        ''' Construtor da classe ClienteController.'''
        self.cliente_model = ClienteModel(banco) # Cria uma instância de ClienteModel com o banco de dados fornecido

    def inserir_cliente(self, nome, email, telefone, endereco):
        ''' Método para inserir um novo cliente.'''
        return self.cliente_model.inserir_cliente(nome, email, telefone, endereco) # insere um cliente no banco de dados passando os dados fornecidos

    def listar_clientes(self):
        ''' Método para listar todos os clientes.'''
        return self.cliente_model.listar_clientes() # lista todos os clientes cadastrados no banco de dados

    def buscar_cliente(self, cliente_id):
        ''' Método para buscar um cliente pelo ID.'''
        return self.cliente_model.buscar_cliente(cliente_id) # busca um cliente específico pelo ID fornecido

    def atualizar_cliente(self, cliente_id, nome=None, email=None, telefone=None, endereco=None):
        ''' Método para atualizar os dados de um cliente.'''
        return self.cliente_model.atualizar_cliente(cliente_id, nome, email, telefone, endereco) # atualiza os dados de um cliente específico pelo ID fornecido

    def deletar_cliente(self, cliente_id):
        ''' Método para deletar um cliente pelo ID.'''
        return self.cliente_model.deletar_cliente(cliente_id) # deleta um cliente específico pelo ID fornecido
    