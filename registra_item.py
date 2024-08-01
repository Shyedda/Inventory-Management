import sqlite3

con = sqlite3.connect("lista_componentes.db")
cur = con.cursor()

def inserir_valor(valor_item):



cur.execute("""
    INSERT INTO itens VALUES
        ('0002', 'correia', 'B83', 'UN', 16, 'marca tigre')
""")

con.commit()
