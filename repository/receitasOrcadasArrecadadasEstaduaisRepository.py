from conexao.conexao import ConexaoClickhouse
from model.receitasOrcadasArrecadadasEstaduais import ReceitasOrcadasArrecadadasEstaduais

class ReceitasOrcadasArrecadadasEstaduaisRepository:
    def __init__(self):
        self.conexao = ConexaoClickhouse()
        
    def obter_receitasOrcadasArrecadadasEstaduais(self, entidades, idquadrimestres, ano): 

    # Join the values in each list separately
        entidades_str = ','.join([str(x) for x in entidades])
        idquadrimestres_str = ','.join([str(x) for x in idquadrimestres])
        ano_str = ','.join([str(x) for x in ano])
        ###replace(CAST(CAST((sum(valororcados) / sum(valorrealizados)*100) AS numeric(16,4)) AS text),'.',',') AS realizado
        query = """
                 select * from(
                    SELECT  dsclassificacaoreceita,
                                            replace(CAST(CAST(sum(valororcado) AS numeric(16,4)) AS text),'.',',') AS valororcado,
                                            replace(CAST(CAST(sum(valorrealizado) AS numeric(16,4)) AS text),'.',',') AS valorrealizado
                                        from(
                                        SELECT 
                                                dsclassificacaoreceita::text AS dsclassificacaoreceita,
                                                valororcado AS valororcado,
                                                valorrealizado AS valorrealizado,
                                                valororcado AS valororcados,
                                                valorrealizado AS valorrealizados
                                            FROM {}.aud_receita_orcada_realizada_estadual 
                                            WHERE cdentidade = 1
                                            AND idquadrimestre IN ({})
                                            AND dsclassificacaoreceita <> 'OUTRAS RECEITAS' 
                                            AND nrano = {} )receitas
                                        GROUP BY dsclassificacaoreceita
                    union all                  
                    SELECT  '99  - TOTAL ' as dsclassificacaoreceita,
                                            replace(CAST(CAST(sum(valororcado) AS numeric(16,4)) AS text),'.',',') AS valororcado,
                                            replace(CAST(CAST(sum(valorrealizado) AS numeric(16,4)) AS text),'.',',') AS valorrealizado
                                        from(
                                        SELECT 
                                                dsclassificacaoreceita::text AS dsclassificacaoreceita,
                                                valororcado AS valororcado,
                                                valorrealizado AS valorrealizado,
                                                valororcado AS valororcados,
                                                valorrealizado AS valorrealizados
                                            FROM {}.aud_receita_orcada_realizada_estadual 
                                            WHERE cdentidade = 1
                                            AND idquadrimestre IN ({})
                                            AND dsclassificacaoreceita <> 'OUTRAS RECEITAS' 
                                            AND nrano = {} )receitas
                                        GROUP BY dsclassificacaoreceita ) totalreceitas
                                order by 1
        """.format(entidades_str, idquadrimestres_str, ano_str,
                   entidades_str, idquadrimestres_str, ano_str)

        # Execute the query
        client = self.conexao.obter_cliente()
        resultado = client.query(query).result_rows
        
        # Process the results
        receitas = [ReceitasOrcadasArrecadadasEstaduais(r[0], r[1], r[2]) for r in resultado]

        return receitas