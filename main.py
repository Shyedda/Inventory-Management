import sqlite3

con = sqlite3.connect("lista_componentes")
cur = con.cursor()

cur.execute("CREATE TABLE itens(id_item, segmento, nome, un_medida, valor, observacoes)")

