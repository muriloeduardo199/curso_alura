import os 


SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'postgresql+psycopg2',
        usuario = 'postgres',
        senha = 'novasenha',
        servidor = 'localhost',
        database = 'alura'
    )



UPLOAD_PATH = os.path.dirname(os.path.abspath( __file__)) + '/uploads'