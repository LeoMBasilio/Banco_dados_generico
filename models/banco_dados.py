import sqlite3
'''
    Classe para manipulação de banco de dados SQLite.
    Permite criar tabelas, inserir, atualizar, deletar e selecionar dados.
'''
class DataBase:
    '''
    Construtor da classe DataBase.
    :param banco: Nome do arquivo do banco de dados SQLite.
    :type banco: str
    '''
    def __init__(self, banco):
        
        self.conn = sqlite3.connect("data/"+banco) # Conecta ao banco de dados SQLite.
        self.cursor = self.conn.cursor() # Cria um cursor para executar comandos SQL.

    '''
    Metodo que retorna uma string com o nome das tabelas no banco de dados.
    :return: String com os nomes das tabelas.
    :rtype: str
    '''
    def __str__(self):
        result = '''-------
Tabelas
------- \n'''

        self.cursor.execute("Select name from sqlite_master WHERE type='table';")

        tabelas = self.cursor.fetchall()
        
        for tabela in tabelas:
            result += f'{tabela[0]} \n'

        return result


    '''
    Metodo para criar uma tabela no banco de dados.
    :param table: Nome da tabela a ser criada.
    :type table: str
    :param columns: Dicionário com os nomes e tipos das colunas da tabela.
    :type columns: dict
    :return: True se a tabela foi criada com sucesso, False caso contrário.
    :rtype: bool
    '''

    def create_table(self, table, columns):
        key = ''
        for i in columns:
            key += f'{i} {columns[i]}, '

        query = f'''
            CREATE TABLE IF NOT EXISTS {table}(
                {key[:-2]}
            );
        '''


        if self.cursor.execute(query):
            self.conn.commit()
            return True
        return False
    
    '''
    Metodo para inserir dados em uma tabela.
    :param table: Nome da tabela onde os dados serão inseridos.
    :type table: str
    :param values: Dicionário com os nomes das colunas e os valores a serem inseridos.
    :type values: dict
    :return: True se os dados foram inseridos com sucesso, False caso contrário.
    :rtype: bool
    '''

    def inserir(self, table, values):
        try:
            key = ''
            value = ''

            for i in values:
                key += f'{i}, '
                value += f'"{values[i]}", '

            query = f'''
                INSERT INTO {table}({key[:-2]}) VALUES({value[:-2]});
            '''
            
            if self.cursor.execute(query):
                self.conn.commit()
                return True
            return False


        except Exception as e:
            return False
        
    '''
    Metodo para atualizar dados em uma tabela.
    :param table: Nome da tabela onde os dados serão atualizados.
    :type table: str
    :param values: Dicionário com os nomes das colunas e os novos valores a serem atualizados.
    :type values: dict
    :param conditions: Dicionário com as condições para a atualização.
    :type conditions: dict
    :return: True se os dados foram atualizados com sucesso, False caso contrário.
    :rtype: bool
    '''

    def update(self, table, values, conditions):
        try:
            key = ''
            condition = ''

            for i in values:
                if values[i] != None:
                    key += f'{i} = "{values[i]}", '

            for j in conditions:
                condition = f'WHERE {conditions[j]}' if i == 'where' else ''

            query = f'''
                    UPDATE {table} SET ({key[:-2]}) {condition}
                '''
            if self.cursor.execute(query):
                self.conn.commit()
                return True
            return False

        except Exception as e:
            return False
        
    '''
    Metodo para deletar dados de uma tabela.
    :param table: Nome da tabela de onde os dados serão deletados.
    :type table: str
    :param condition: Dicionário com as condições para a deleção.
    :type condition: dict
    :return: True se os dados foram deletados com sucesso, False caso contrário.
    :rtype: bool
    '''

    def delete(self, table, condition):
        try:
            where = ''
            for i in condition:
                where += f' where {condition[i]}' if i == 'where' else ''

            query = f'''
                DELETE FROM {table} {where}
            '''

            if self.cursor.execute(query):
                self.conn.commit()
                return True
            return False
            
        except Exception as e:
            return False
        
    '''
    Metodo para selecionar dados de uma tabela com condições.
    :param table: Nome da tabela de onde os dados serão selecionados.
    :type table: str
    :param conditions: Dicionário com as condições para a seleção.
    :type conditions: dict
    :param columns: Lista com os nomes das colunas a serem selecionadas. Se None, seleciona todas as colunas.
    :type columns: list or None
    :return: Lista com os dados selecionados ou False em caso de erro.
    :rtype: list or bool
    '''

    def select(self, table, conditions, columns=None):
        try:
            condition = ''
            column = ''

            if not columns:
                for i in columns:
                    column += f'{i}, '
            else:
                column = '*'
                for i in columns:
                    condition += f'{i}, '

            for i in conditions:
                condition += f'WHERE {conditions[i]}' if i == 'where' else ''

            query = f'''
                SELECT {columns[:-2]} FROM {table} {condition}
            '''

            self.cursor.execute(query)
            return self.cursor.fetchall()
        
        except Exception as e:
            return False
        
    '''
    Metodo para selecionar todos os dados de uma tabela.
    :param table: Nome da tabela de onde os dados serão selecionados.
    :type table: str
    :return: Lista com todos os dados da tabela ou False em caso de erro.
    :rtype: list or bool
    '''

    def select_all(self, table):
        try:
            query = f'''
                SELECT * FROM {table}
            '''

            self.cursor.execute(query)
            return self.cursor.fetchall()
        
        except Exception as e:
            return False