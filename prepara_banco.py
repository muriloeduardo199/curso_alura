import psycopg2
from flask_bcrypt import generate_password_hash

# Crie uma conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    host='127.0.0.1',
    port='5432',
    user="postgres",
    password="novasenha",
    database = 'alura'
    
)

# Crie uma tabela
cur = conn.cursor()
cur.execute('''
CREATE TABLE jogos (
  id serial PRIMARY KEY,
  nome varchar(50) NOT NULL,
  categoria varchar(40) NOT NULL,
  console varchar(20) NOT NULL
);
''')




cur.execute("""CREATE TABLE usuarios (
      nome varchar(20) NOT NULL,
      nickname varchar(8) NOT NULL,
      senha varchar(100) NOT NULL,
      PRIMARY KEY (nickname)
      ) ;""")

# Insira alguns dados na tabela
cur.executemany('''
INSERT INTO jogos (nome, categoria, console) VALUES (%s, %s, %s)
''', [
    ('Tetris', 'Puzzle', 'Atari'),
    ('God of War', 'Hack n Slash', 'PS2'),
    ('Mortal Kombat', 'Luta', 'PS2'),
    ('Valorant', 'FPS', 'PC'),
    ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
    ('Need for Speed', 'Corrida', 'PS2'),
])

cur.executemany('''
    INSERT INTO usuarios (nome, nickname, senha) VALUES (%s,%s,%s)''',
    [("Bruno Divino", "BD",generate_password_hash( "alohomora").decode('utf-8')),
    ("Camila Ferreira", "Mila", generate_password_hash("paozinho").decode('utf-8')),
    ("Guilherme Louro", "Cake", generate_password_hash("python_eh_vida").decode('utf-8'))
    ])

cur.execute('SELECT * FROM jogos')

for row in cur:
    print(row)

# Commite as alterações
conn.commit()

# Feche a conexão
conn.close()