from conexao.conexao import ConexaoClickhouse
from model.despesasOrcadasEmpenhadasPorSecretariasGraficos import DespesasOrcadasEmpenhadasPorSecretariasGraficos

class DespesasOrcadasEmpenhadasPorSecretariasGraficosRepository:
    def __init__(self):
        self.conexao = ConexaoClickhouse()

    def obter_despesasOrcadasEmpenhadasPorSecretariasGraficosRepository(self, entidades, idquadrimestres, ano): 

    # Join the values in each list separately
        entidades_str = ','.join([str(x) for x in entidades])
        idquadrimestres_str = ','.join([str(x) for x in idquadrimestres])
        ano_str = ','.join([str(x) for x in ano])
        
        query = """
                 SELECT  dsclassificacaodespesa,
                         CEIL(valorrealizados)::NUMERIC(16,2) AS valorrealizados,
                         round(percentual,2) AS percentual
                    from( 
                    SELECT dsclassificacaodespesa,
                        sum(valorrealizados) AS valorrealizados,
                        (((sum(valorrealizado) / valorTotal) *100))::numeric(16,4) AS percentual
                        from(
                    SELECT dsclassificacaodespesa,
                        valorrealizado::numeric(16,6) AS valorrealizados,
                        valorrealizado::numeric(16,6) AS valorrealizado,
                        (SELECT sum(valorrealizado)::numeric(16,6) AS valortotal 
                                FROM {}.aud_despesa_orcada_empenhada_por_secretaria rt
                                    WHERE cdentidade = 1
                                    AND idquadrimestre IN ({}) 
                                    AND dsclassificacaodespesa <> 'OUTRAS RECEITAS'
                                    AND nrano = {} )::numeric(16,4) AS valorTotal
                        from(        
                    SELECT
                                cdentidade AS cdentidade,            
                                dsclassificacaodespesa::text AS dsclassificacaodespesa,
                                idquadrimestre,
                                nrano,
                                valorrealizado AS valorrealizado,
                                0 AS valorTotal,
                                0 AS percentual
                            FROM {}.aud_despesa_orcada_empenhada_por_secretaria)valorRealizadoss
                            WHERE cdentidade = 1
                                AND idquadrimestre IN ({}) 
                                AND nrano = {}
                        ORDER BY 1)valorgrafico
                        GROUP BY dsclassificacaodespesa,valorTotal)graficoREceita
                        ORDER BY dsclassificacaodespesa
        """.format(entidades_str, idquadrimestres_str, ano_str,
                   entidades_str, idquadrimestres_str, ano_str)
        
 
        # Execute the query
        client = self.conexao.obter_cliente()
        resultado = client.query(query).result_rows
        
        # Process the results
        despesas = [DespesasOrcadasEmpenhadasPorSecretariasGraficos(r[0], r[1], r[2]) for r in resultado]

        return despesas