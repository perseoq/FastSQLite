import sqlite3 

class FastSQLite:
    
    def connect(self, file):
        self.archivo = file
        return self.archivo

# ------------- TABLE ACTIONS -------------

    def create_table(self, table, columns):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'CREATE TABLE {table}({columns})'
        self.conexion.execute(query)
        self.conexion.commit()

    def rename_table(self, table, rename):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'ALTER TABLE {table} RENAME TO {rename}'
        self.conexion.execute(query)
        self.conexion.commit()
    
    def drop_table(self, table):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'DROP TABLE {table}'
        self.conexion.execute(query)
        self.conexion.commit()

# ------------- Action Section -------------

    def insert(self, table, column, params):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'INSERT INTO {table}({column}) VALUES({params})'
        self.conexion.execute(query)
        self.conexion.commit()

    def update(self, table, params, where, condition):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'UPDATE {table} SET {params} WHERE {where} = {condition}'
        self.conexion.execute(query)
        self.conexion.commit()
    
    def delete(self, table, where, condition):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'DELETE FROM {table} WHERE WHERE {where} = {condition}'
        self.conexion.execute(query)
        self.conexion.commit()

    def add_column(self, table, new_column):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'ALTER TABLE {table} ADD COLUMN {new_column}'
        self.conexion.execute(query)
        self.conexion.commit()

# ------------- FOREIGN KEY -------------

    def add_fk_reference(self, table, fk_column, column_id):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'FOREIGN KEY({fk_column}) REFERENCES {table}({column_id})'
        self.conexion.execute(query)
        self.conexion.commit()

# ------------- Queries Section ------------- 

    def custom_fetch(self, query):
        self.conexion = sqlite3.connect(self.archivo)
        self.conexion.execute(query)
        self.cursor = self.conexion.cursor()
        return self.cursor.fetchall()

    def fetch_all(self, table):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'SELECT * FROM {table}'
        self.conexion.execute(query)
        self.cursor = self.conexion.cursor()
        return self.cursor.fetchall() 
    
    def fetch_one(self, table, column):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'SELECT {column} FROM {table}'
        self.conexion.execute(query)
        self.cursor = self.conexion.cursor()
        return self.cursor.fetchone()
    
    def fetch_many(self, table, columns):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'SELECT {columns} FROM {table}'
        self.conexion.execute(query)
        self.cursor = self.conexion.cursor()
        return self.cursor.fetchmany()
    
    def distinct(self, table, columns):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'SELECT DISTINCT {columns} FROM {table}'
        self.conexion.execute(query)
        self.cursor = self.conexion.cursor()
        return self.cursor.fetchall()
    
    def where(self, table, columns, where, param):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'SELECT {columns} FROM {table} WHERE {where} = {param}'
        self.conexion.execute(query)
        self.cursor = self.conexion.cursor()
        return self.cursor.fetchall()

    def like(self, table, columns, param):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'SELECT {columns} FROM {table} LIKE {param}'
        self.conexion.execute(query)
        self.cursor = self.conexion.cursor()
        return self.cursor.fetchall()
    
    def between(self, table, columns, where, param1, param2):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'SELECT {columns} FROM {table} WHERE {where} BETWEEN {param1} AND {param2}'
        self.conexion.execute(query)
        self.cursor = self.conexion.cursor()
        return self.cursor.fetchall()
    
    def left_join(self, table1, table2, columns, column1, column2):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'SELECT {columns} FROM {table1} LEFT JOIN {table2} ON {table1}.{column1}={table2}.{column2}'
        self.conexion.execute(query)
        self.cursor = self.conexion.cursor()
        return self.cursor.fetchall()
    
    def right_join(self, table1, table2, columns, column1, column2):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'SELECT {columns} FROM {table1} RIGHT JOIN {table2} ON {table1}.{column1}={table2}.{column2}'
        self.conexion.execute(query)
        self.cursor = self.conexion.cursor()
        return self.cursor.fetchall()
    
    def inner_join(self, table1, table2, columns, column1, column2):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'SELECT {columns} FROM {table1} INNER JOIN {table2} ON {table1}.{column1}={table2}.{column2}'
        self.conexion.execute(query)
        self.cursor = self.conexion.cursor()
        return self.cursor.fetchall()
    
    def union_all(self, table1, table2, columns_table1, columns_table2):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'SELECT {columns_table1} FROM {table1} UNION ALL SELECT {columns_table2} FROM {table2}'
        self.conexion.execute(query)
        self.cursor = self.conexion.cursor()
        return self.cursor.fetchall()
    
    def union(self, table1, table2, columns_table1, columns_table2):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'SELECT {columns_table1} FROM {table1} UNION SELECT {columns_table2} FROM {table2}'
        self.conexion.execute(query)
        self.cursor = self.conexion.cursor()
        return self.cursor.fetchall()

    def avg(self, table, column, name, where, param):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'SELECT AVG({column}) AS {name} FROM {table} WHERE {where} = {param}'
        self.conexion.execute(query)
        self.cursor = self.conexion.cursor()
        return self.cursor.fetchall()
    
    def count(self, table, column, name, where, param):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'SELECT COUNT({column}) AS {name} FROM {table} WHERE {where} = {param}'
        self.conexion.execute(query)
        self.cursor = self.conexion.cursor()
        return self.cursor.fetchall()

    def sum(self, table, column, name, where, param):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'SELECT SUM({column}) AS {name} FROM {table} WHERE {where} = {param}'
        self.conexion.execute(query)
        self.cursor = self.conexion.cursor()
        return self.cursor.fetchall()
    
    def max(self, table, column, name, where, param):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'SELECT MAX({column}) AS {name} FROM {table} WHERE {where} = {param}'
        self.conexion.execute(query)
        self.cursor = self.conexion.cursor()
        return self.cursor.fetchall()
    
    def min(self, table, column, name, where, param):
        self.conexion = sqlite3.connect(self.archivo)
        query = f'SELECT MIN({column}) AS {name} FROM {table} WHERE {where} = {param}'
        self.conexion.execute(query)
        self.cursor = self.conexion.cursor()
        return self.cursor.fetchall()