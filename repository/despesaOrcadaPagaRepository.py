from conexao.conexao import ConexaoClickhouse
from model.despesaOrcadaPaga import DespesaOrcadaPaga

class DespesaOrcadaPagaRepository:
    def __init__(self):
        self.conexao = ConexaoClickhouse()
        
    def obter_despesas(self, idquadrimestres):
        query = """
        SELECT 
            dsclassificacaodespesa, 
            REPLACE(CAST(CAST(SUM(valororcado) AS NUMERIC(16,2)) AS TEXT), '.', ',') AS valororcado,
            REPLACE(CAST(CAST(SUM(valorpago) AS NUMERIC(16,2)) AS TEXT), '.', ',') AS valorpago
        FROM terraboapm.aud_despesa_orcada_paga
        WHERE cdentidade = 1
            AND idquadrimestre IN ({})
            AND nrano = 2024
            AND dsclassificacaodespesa <> 'OUTRAS DESPESAS'
        GROUP BY dsclassificacaodespesa
        ORDER BY dsclassificacaodespesa
        """.format(','.join([str(x) for x in idquadrimestres]))

        client = self.conexao.obter_cliente()
        resultado = client.query(query).result_rows
        despesas = [DespesaOrcadaPaga(r[0], r[1], r[2]) for r in resultado]
        
        return despesas
