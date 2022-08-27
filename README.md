# FastSQLite Documentation

### Example

```python
from fastsqlite import FastSQLite

db = FastSQLite()
db.connect('file.db')
db.create_table('gato', 'id int, rum varchar(300)')
```  

### Using FastSQLite

```python
db = FastSQLite()
```

db.**connect**( file):

```python
db.connect('database.db')
```
  
**Important**: 
 
```
ALTERtable [table] RENAME TO [rename];
[variable] = variable: str

db.rename_table(str, str)

example:
	db.rename_table('old_name', 'new_name')
```

### Table Actions 

db.**create_table**(table, columns):

```SQL 
CREATE table [table]([columns]);
```

db.**rename_table**(table, rename):

```SQL 
ALTER table [table] RENAME TO [rename];
```

db.**drop_table**(table):

```SQL 
DROP table [table];
```


### Column Actions

db.**insert**(table, column, params):

```SQL 
INSERT INTO [table]([column]) VALUES([params]);
```

db.**update**(table, params, where, condition):

```SQL 
UPDATE [table] SET [params] WHERE [where] = [condition];
```

db.**delete**(table, where, condition):

```SQL
DELETE FROM [table] WHERE WHERE [where] = [condition];
```

db.**add_column**(table, new_column):

```SQL 
ALTERtable [table] ADD COLUMN [new_column];
```

db.**add_fk_reference**(table, fk_column, column_id):

```SQL 
FOREIGN KEY([fk_column]) REFERENCES [table]([column_id]);
```

### Queries Section 

db.**custom_fetch**( query):

```python
query = 'SELECT nombre as n, precio as p FROM productos WHERE precio < 5.60;'
db.custom_fetch(query):
```

db.**fetch_all**(table):

```SQL 
SELECT * FROM [table];
```

db.**fetch_one**(table, column):

```SQL 
SELECT [column] FROM [table];
```

db.**fetch_many**(table, columns):

```SQL 
SELECT [columns] FROM [table];
```

db.**distinct**(table, columns):

```SQL
SELECT DISTINCT [columns] FROM [table];
```

db.**where**(table, columns, where, param):

```SQL
SELECT [columns] FROM [table] WHERE [where] = [param];
```

db.**like**(table, columns, param):

```SQL 
SELECT [columns] FROM [table] LIKE [param];
```

db.**between**(table, columns, where, param1, param2):

```SQL 
SELECT [columns] FROM [table] WHERE [where] BETWEEN [param1] AND [param2];
```

db.**left_join**(table1, table2, columns, column1, column2):

```SQL
SELECT [columns] FROM [table1] LEFT JOIN [table2] ON [table1].[column1]=[table2].[column2];
```

db.**right_join**(table1, table2, columns, column1, column2):

```SQL
SELECT [columns] FROM [table1] RIGHT JOIN [table2] ON [table1].[column1]=[table2].[column2];
```

db.**inner_join**(table1, table2, columns, column1, column2):

```SQL
SELECT [columns] FROM [table1] INNER JOIN [table2] ON [table1].[column1]=[table2].[column2];
```

db.**union_all**(table1, table2, columns_table1, columns_table2):

```SQL
SELECT [columns_table1] FROM [table1] UNION ALL SELECT [columns_table2] FROM [table2];
```

db.**union**(table1, table2, columns_table1, columns_table2):

```SQL
SELECT [columns_table1] FROM [table1] UNION SELECT [columns_table2] FROM [table2];
```

db.**avg**(table, column, name, where, param):

```SQL 
SELECT AVG([column]) AS [name] FROM [table] WHERE [where] = [param];
```

db.**count**(table, column, name, where, param):

```SQL 
SELECT COUNT([column]) AS [name] FROM [table] WHERE [where] = [param];
```

db.**sum**(table, column, name, where, param):

```SQL 
SELECT SUM([column]) AS [name] FROM [table] WHERE [where] = [param];
```

db.**max**(table, column, name, where, param):

```SQL
SELECT MAX([column]) AS [name] FROM [table] WHERE [where] = [param];
```

db.**min**(table, column, name, where, param):

```SQL
SELECT MIN([column]) AS [name] FROM [table] WHERE [where] = [param];
```

