import psycopg2

# Configurações do banco
db_config = {
    'dbname': 'base_enem',
    'user': 'postgres',
    'password': 'm1cr00n4',
    'host': 'localhost',
    'port': '5432'
}

# Função para abrir conexão
def get_connection():
    return psycopg2.connect(**db_config)
