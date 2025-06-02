import sqlite3

class DataBase:
    def __init__(self, banco):
        self.conn = sqlite3.connect("data/"+banco)
        self.cursor = self.conn.cursor()

    def __str__(self):
        result = '''-------
Tabelas
------- \n'''

        self.cursor.execute("Select name from sqlite_master WHERE type='table';")

        tabelas = self.cursor.fetchall()
        
        for tabela in tabelas:
            result += f'{tabela[0]} \n'

        return result


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
            
            self.cursor.execute(query)
            self.conn.commit()
            return True


        except Exception as e:
            return False
        

    def update(self, table, values, conditions):
        try:
            key = ''
            condition = ''

            for i in values:

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
        
    def select_all(self, table):
        try:
            query = f'''
                SELECT * FROM {table}
            '''

            self.cursor.execute(query)
            return self.cursor.fetchall()
        
        except Exception as e:
            return False