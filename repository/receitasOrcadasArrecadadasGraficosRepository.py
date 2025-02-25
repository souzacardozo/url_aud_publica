from conexao.conexao import ConexaoClickhouse
from model.receitasOrcadasArrecadadasGraficos import ReceitasOrcadasArrecadadasGraficos

class ReceitasOrcadasArrecadadasGraficosRepository:
    def __init__(self):
        self.conexao = ConexaoClickhouse()
        
    def obter_receitasOrcadasArrecadadasGraficos(self, entidades, idquadrimestres, ano): 

    # Join the values in each list separately
        entidades_str = ','.join([str(x) for x in entidades])
        idquadrimestres_str = ','.join([str(x) for x in idquadrimestres])
        ano_str = ','.join([str(x) for x in ano])
        
        query = """
                SELECT  dsclassificacaoreceita,
                        CEIL(valorrealizados)::NUMERIC(16,2) AS valorrealizados,
                        percentual::numeric(16,2) AS percentual
                        from( 
                    SELECT dsclassificacaoreceita,
                        sum(valorrealizados) AS valorrealizados,
                        (((sum(valorrealizado) / valorTotal) *100))::numeric(16,2) AS percentual
                        from(
                    SELECT dsclassificacaoreceita,
                        valorrealizado::numeric(16,6) AS valorrealizados,
                        valorrealizado::numeric(16,6) AS valorrealizado,
                        (SELECT sum(valorrealizado)::numeric(16,6) AS valortotal 
                                FROM {}.aud_receita_orcada_realizada rt
                                    WHERE cdentidade = 1
                                    AND idquadrimestre IN ({})
                                    AND dsclassificacaoreceita <> 'OUTRAS RECEITAS'
                                    AND nrano = {} )::numeric(16,4) AS valorTotal
                        from(        
                    SELECT
                                cdentidade AS cdentidade,            
                                dsclassificacaoreceita::text AS dsclassificacaoreceita,
                                idquadrimestre,
                                nrano,
                                valorrealizado AS valorrealizado,
                                0 AS valorTotal,
                                0 AS percentual
                            FROM {}.aud_receita_orcada_realizada)valorRealizadoss
                            WHERE cdentidade = 1
                                AND idquadrimestre IN ({}) 
                                AND nrano = {}
                        ORDER BY 1)valorgrafico
                        GROUP BY dsclassificacaoreceita,valorTotal)graficoREceita
                        ORDER BY dsclassificacaoreceita
        """.format(entidades_str, idquadrimestres_str, ano_str,
                   entidades_str, idquadrimestres_str, ano_str)
        

        # Debugging the generated query
        print("Generated SQL query: ", query)

        # Execute the query
        client = self.conexao.obter_cliente()
        resultado = client.query(query).result_rows
        
        # Process the results
        receitas = [ReceitasOrcadasArrecadadasGraficos(r[0], r[1], r[2]) for r in resultado]

        return receitas
