import sqlite3

conn = sqlite3.connect('mercado.db')
conn.execute("PRAGMA foreign_keys = ON")

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS carrinho 
(
   id_carrinho INTEGER PRIMARY KEY,
   id_usuario INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS produto 
(
  id_produto INTEGER PRIMARY KEY,
  nome VARCHAR(45) NOT NULL,
  preco FLOAT NOT NULL,
  categoria VARCHAR(45) NOT NULL,
  desconto FLOAT NOT NULL,
  marca VARCHAR(45) NULL,
  descricao VARCHAR(100) NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS carrinho_produto 
(
  id_carrinho INTEGER,
  id_produto INTEGER,
  quantidade INTEGER NOT NULL,
  PRIMARY KEY (id_carrinho, id_produto),
  FOREIGN KEY (id_carrinho) REFERENCES carrinho (id_carrinho),
  FOREIGN KEY (id_produto) REFERENCES produto (id_produto)
)
''')


cursor.execute('''
INSERT OR IGNORE INTO carrinho (id_carrinho, id_usuario)
VALUES (1, 1), (2, 1), (3, 2), (4, 3)
''')

cursor.execute('''
INSERT OR IGNORE INTO produto (id_produto, nome, preco, categoria, desconto, marca, descricao) 
VALUES (1, "creme de avelã", "30.0", "doces", 0.0, "Nutella", "pote com 650g"),
       (2, "macarrão", "2.0", "massas", 0.0, "Aurora", "pacote com 500g"),
       (3, "refrigerante", "10.0", "bebidas", 0.0, "Coca-Cola", "garrafa pet de 2L")
''')

cursor.execute('''
INSERT OR IGNORE INTO carrinho_produto (id_carrinho, id_produto, quantidade) 
VALUES (1, 1, 1),
       (1, 2, 5),
       (1, 3, 2),
       (2, 1, 2),
       (3, 1, 1),
       (4, 2, 4)
''')

conn.commit()