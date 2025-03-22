import clickhouse_connect
import psycopg2


class PostgresConexao:
    
    @staticmethod
    def conectar_dataBaseEloWeb():
        conn = psycopg2.connect(
            dbname="banco1",     # Substitua pelo nome do seu primeiro banco de dados
            user="elotech",     # Substitua pelo usuário do banco 1
            password="elo",   # Substitua pela senha do banco 1
            host="acesso.terraboa.eloweb.net",    # Ou o endereço do servidor PostgreSQL
            port="5432"          # A porta padrão do PostgreSQL
        )
        return conn
    
    @staticmethod
    def conectar_dataBaseEloJr():
        conn = psycopg2.connect(
            dbname="banco1",     # Substitua pelo nome do seu primeiro banco de dados
            user="usuario1",     # Substitua pelo usuário do banco 1
            password="senha1",   # Substitua pela senha do banco 1
            host="localhost",    # Ou o endereço do servidor PostgreSQL
            port="5432"          # A porta padrão do PostgreSQL
        )
        return conn
    
    @staticmethod
    def conectar_ClicHose():
        conn = clickhouse_connect.connect(
            dbname="terraboapm",     # Substitua pelo nome do seu primeiro banco de dados
            user="analytics",     # Substitua pelo usuário do banco 1
            password="toh4hahph9ooj4ja3Ohcohaic4ohpe",   # Substitua pela senha do banco 1
            host="52.67.135.147" ,    # Ou o endereço do servidor PostgreSQL
            port="8123"          # A porta padrão do PostgreSQL
        )
        return conn