from conexao.conexao import ConexaoClickhouse
from model.despesaOrcadaEmpenhadaPaga import DespesaOrcadaEmpenhadaPaga

class DespesaOrcadaEmpenhadaPagaRepository:
    def __init__(self):
        self.conexao = ConexaoClickhouse()

    def obter_despesaOrcadaEmpenhadaPagaRepository(self, entidades, idquadrimestres, ano): 

    # Join the values in each list separately
        entidades_str = ','.join([str(x) for x in entidades])
        idquadrimestres_str = ','.join([str(x) for x in idquadrimestres])
        ano_str = ','.join([str(x) for x in ano])
        
        query = """
                SELECT 
                    dsclassificacaodespesa, 
                    REPLACE(CAST(CAST(SUM(valororcado) AS NUMERIC(16,2)) AS TEXT), '.', ',') AS valororcado,
                    REPLACE(CAST(CAST(SUM(valorpago) AS NUMERIC(16,2)) AS TEXT), '.', ',') AS valorpago
                FROM {}.aud_despesa_orcada_paga
                WHERE cdentidade = 1
                    AND idquadrimestre IN ({})
                    AND nrano = {}
                    AND dsclassificacaodespesa <> 'OUTRAS DESPESAS'
                GROUP BY dsclassificacaodespesa
                ORDER BY dsclassificacaodespesa
        """.format(entidades_str, idquadrimestres_str, ano_str)
        

        # Debugging the generated query
        print("Generated SQL query: ", query)

        # Execute the query
        client = self.conexao.obter_cliente()
        resultado = client.query(query).result_rows
        
        # Process the results
        despesas = [DespesaOrcadaEmpenhadaPaga(r[0], r[1], r[2]) for r in resultado]

        return despesas

