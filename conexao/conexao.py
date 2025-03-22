from clickhouse_connect import get_client
import psycopg2

class ConexaoClickhouse:
    def __init__(self):
        self.host = "52.67.135.147"  # Alterar para o seu host do ClickHouse
        self.port = 8123         # Alterar para a porta do ClickHouse
        self.database = "terraboapm"
        self.username = "analytics"
        self.password = "toh4hahph9ooj4ja3Ohcohaic4ohpe"  # Substitua com a senha correta

    def obter_cliente(self):
        # Criação do cliente de conexão com ClickHouse
        return get_client(host=self.host, port=self.port, username=self.username, password=self.password, database=self.database)
    
