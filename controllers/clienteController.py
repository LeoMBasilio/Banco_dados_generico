from models.clienteModel import ClienteModel

class ClienteController:
    def __init__(self, banco):
        self.cliente_model = ClienteModel(banco)

    def inserir_cliente(self, nome, email, telefone, endereco):
        return self.cliente_model.inserir_cliente(nome, email, telefone, endereco)

    def listar_clientes(self):
        return self.cliente_model.listar_clientes()

    def buscar_cliente(self, cliente_id):
        return self.cliente_model.buscar_cliente(cliente_id)

    def atualizar_cliente(self, cliente_id, nome=None, email=None, telefone=None, endereco=None):
        return self.cliente_model.atualizar_cliente(cliente_id, nome, email, telefone, endereco)

    def deletar_cliente(self, cliente_id):
        return self.cliente_model.deletar_cliente(cliente_id)
    