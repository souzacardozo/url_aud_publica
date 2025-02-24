from flask import Flask, jsonify, request
from clickhouse_connect import get_client

app = Flask(__name__)

# Função para conectar ao banco ClickHouse
def get_clickhouse_client():
    client = get_client(host='52.67.135.147', port=8123, username='analytics', password='toh4hahph9ooj4ja3Ohcohaic4ohpe')
    return client

# Rota para consultar a despesa orçada e paga
@app.route('/despesa', methods=['GET'])
def get_despesa():
    # Pegando o quadrimestre da URL
    quadrimestre = request.args.get('quadrimestre', '')
    if not quadrimestre:
        return jsonify({'error': 'Quadrimestre é obrigatório'}), 400

    # Criar a consulta com o quadrimestre fornecido
    query = f"""
        SELECT dsclassificacaodespesa,
               REPLACE(CAST(CAST(SUM(valororcado) AS NUMERIC(16,2)) AS TEXT), '.', ',') AS valororcado,
               REPLACE(CAST(CAST(SUM(valorpago) AS NUMERIC(16,2)) AS TEXT), '.', ',') AS valorpago
        FROM terraboapm.aud_despesa_orcada_paga
        WHERE cdentidade = 1
          AND idquadrimestre IN ({quadrimestre})
          AND nrano = 2024
          AND dsclassificacaodespesa <> 'OUTRAS DESPESAS'
        GROUP BY dsclassificacaodespesa
        ORDER BY dsclassificacaodespesa
    """

    # Conectar ao ClickHouse e executar a consulta
    client = get_clickhouse_client()
    result = client.query(query)
    
    # Formatar os resultados em JSON
    data = result.result_set
    response_data = []
    for row in data:
        response_data.append({
            'dsclassificacaodespesa': row[0],
            'valororcado': row[1],
            'valorpago': row[2]
        })

    return jsonify(response_data)

# Iniciar o servidor Flask
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)