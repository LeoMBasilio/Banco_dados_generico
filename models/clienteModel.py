from models.banco_dados import DataBase # Importa a classe DataBase do módulo banco_dados

'''
Classe ClienteModel que herda de DataBase para manipulação de dados de clientes
'''
class ClienteModel(DataBase):
    '''
    Construtor da classe ClienteModel.
    :param banco: Nome do arquivo do banco de dados SQLite.
    :type banco: str
    '''
    def __init__(self, banco):
        super().__init__(banco) # Chama o construtor da classe DataBase
        self.table = 'clientes' # Define o nome da tabela de clientes
        self.columns = {
            'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'nome': 'TEXT NOT NULL',
            'email': 'TEXT NOT NULL',
            'telefone': 'TEXT NOT NULL',
            'endereco': 'TEXT NOT NULL'
        } # Define as colunas da tabela de clientes e seus tipos
        self.create_table(self.table, self.columns) # Cria a tabela de clientes se não existir

    '''
    Método para inserir um novo cliente na tabela.
    :param nome: Nome do cliente.
    :type nome: str
    :param email: Email do cliente.
    :type email: str
    :param telefone: Telefone do cliente.
    :type telefone: str
    :param endereco: Endereço do cliente.
    :type endereco: str
    :return: Resultado da inserção.
    :rtype: bool
    '''

    def inserir_cliente(self, nome, email, telefone, endereco):
        values = {
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'endereco': endereco
        }
        return self.inserir(self.table, values)
    
    '''
    Método para listar todos os clientes na tabela.
    :return: Lista de clientes.
    :rtype: list
    '''

    def listar_clientes(self):
        return self.select_all(self.table)
    
    '''
    Método para buscar um cliente específico pelo ID.
    :param cliente_id: ID do cliente a ser buscado.
    :type cliente_id: int
    :return: Dados do cliente encontrado.
    :rtype: dict
    '''

    def buscar_cliente(self, cliente_id):
        condition = {'where': f'id = {cliente_id}'}
        return self.select(self.table, condition)
    
    '''
    Método para atualizar os dados de um cliente.
    :param cliente_id: ID do cliente a ser atualizado.
    :type cliente_id: int
    :param nome: Novo nome do cliente.
    :type nome: str
    :param email: Novo email do cliente.
    :type email: str
    :param telefone: Novo telefone do cliente.
    :type telefone: str
    :param endereco: Novo endereço do cliente.
    :type endereco: str
    :return: Resultado da atualização.
    :rtype: bool
    '''

    def atualizar_cliente(self, cliente_id, nome=None, email=None, telefone=None, endereco=None):
        values = {
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'endereco': endereco
        } # Cria um dicionário com os novos valores a serem atualizados

        condition = {
            'where': f'id = {cliente_id}'
        } # Define a condição para a atualização, filtrando pelo ID do cliente

        return self.update(self.table, values, condition) # Atualiza os dados do cliente na tabela com os novos valores fornecidos
    
    '''
    Método para deletar um cliente pelo ID.
    :param cliente_id: ID do cliente a ser deletado.
    :type cliente_id: int
    :return: Resultado da deleção.
    :rtype: bool
    '''

    def deletar_cliente(self, cliente_id):
        condition = {
            'where': f'id = {cliente_id}'
        }
        return self.delete(self.table, condition)