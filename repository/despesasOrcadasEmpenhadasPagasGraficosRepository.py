from conexao.conexao import ConexaoClickhouse
from model.despesasOrcadasEmpenhadasPagasGraficos import DespesasOrcadasEmpenhadasPagasGraficos

class DespesasOrcadasEmpenhadasPagasGraficosRepository:
    def __init__(self):
        self.conexao = ConexaoClickhouse()

    def obter_despesasOrcadasEmpenhadasPagasGraficosRepository(self, entidades, idquadrimestres, ano): 

    # Join the values in each list separately
        entidades_str = ','.join([str(x) for x in entidades])
        idquadrimestres_str = ','.join([str(x) for x in idquadrimestres])
        ano_str = ','.join([str(x) for x in ano])
        
        query = """
                 SELECT  dsclassificacaodespesa,
                        CEIL(valorpagos)::NUMERIC(16,2) AS valorpagos,
                        round(percentual,2) AS percentual
                        from(
                    SELECT dsclassificacaodespesa,
                        sum(valorpagos) AS valorpagos,
                        (((sum(valorpago) / valorTotal) *100))::numeric(16,4) AS percentual
                        from(
                    SELECT dsclassificacaodespesa,
                        valorpago::numeric(16,6) AS valorpagos,
                        valorpago::numeric(16,6) AS valorpago,
                        (SELECT sum(valorpago)::numeric(16,6) AS valortotal
                                FROM {}.aud_despesa_orcada_paga rt
                                    WHERE cdentidade = 1
                                    AND idquadrimestre IN ({})
                                    AND dsclassificacaodespesa <> 'OUTRAS RECEITAS'
                                    AND nrano = {}
                                    AND data_ano::numeric = {} )::numeric(16,4) AS valorTotal
                        from(
                    SELECT
                                cdentidade AS cdentidade,
                                dsclassificacaodespesa::text AS dsclassificacaodespesa,
                                idquadrimestre,
                                nrano,
                                data_ano::NUMERIC AS data_ano,
                                valorpago AS valorpago,
                                0 AS valorTotal,
                                0 AS percentual
                            FROM {}.aud_despesa_orcada_paga)valorRealizadoss
                            WHERE cdentidade = 1
                                AND idquadrimestre IN ({})
                                AND nrano = {}
                                AND data_ano = {}
                        ORDER BY 1)valorgrafico
                        GROUP BY dsclassificacaodespesa,valorTotal)graficoREceita
                        ORDER BY dsclassificacaodespesa
        """.format(entidades_str, idquadrimestres_str, ano_str, ano_str,
                   entidades_str, idquadrimestres_str, ano_str, ano_str)
        
        

        # Debugging the generated query
        print("Generated SQL query: ", query)

        # Execute the query
        client = self.conexao.obter_cliente()
        resultado = client.query(query).result_rows
        
        # Process the results
        despesas = [DespesasOrcadasEmpenhadasPagasGraficos(r[0], r[1], r[2]) for r in resultado]

        return despesas

