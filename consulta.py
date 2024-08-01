import sqlite3

# Conectar ao banco de dados SQLite
con = sqlite3.connect("lista_componentes.db")
cur = con.cursor()

# Executar uma consulta para selecionar todos os itens da tabela lista_componentes
res = cur.execute("SELECT id_item FROM itens")
print(res.fetchall())