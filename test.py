from fastsqlite import FastSQLite

db = FastSQLite()
db.connect('file.db')
db.create_table('gato', 'id int, rum varchar(300)')
