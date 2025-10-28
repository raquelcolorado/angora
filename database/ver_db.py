import sqlite3

db_path = "database/clientes.db"

conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute("SELECT * FROM clientes")
rows = c.fetchall()

for row in rows:
    print(row)

conn.close()
