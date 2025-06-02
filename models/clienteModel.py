from models.banco_dados import DataBase

class ClienteModel(DataBase):
    def __init__(self, banco):
        super().__init__(banco)
        self.table = 'clientes'
        self.columns = {
            'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'nome': 'TEXT NOT NULL',
            'email': 'TEXT NOT NULL',
            'telefone': 'TEXT NOT NULL',
            'endereco': 'TEXT NOT NULL'
        }
        self.create_table(self.table, self.columns)

    def inserir_cliente(self, nome, email, telefone, endereco):
        values = {
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'endereco': endereco
        }
        return self.inserir(self.table, values)
    
    def listar_clientes(self):
        return self.select_all(self.table)
    
    def buscar_cliente(self, cliente_id):
        condition = {'where': f'id = {cliente_id}'}
        return self.select(self.table, condition)
    
    def atualizar_cliente(self, cliente_id, nome=None, email=None, telefone=None, endereco=None):
        values = {
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'endereco': endereco
        }

        condition = {
            'where': f'id = {cliente_id}'
        }

        return self.update(self.table, values, condition)
    
    def deletar_cliente(self, cliente_id):
        condition = {
            'where': f'id = {cliente_id}'
        }
        return self.delete(self.table, condition)