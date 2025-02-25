from conexao.conexao import ConexaoClickhouse
from model.receitasOrcadasArrecadadasProprios import ReceitasOrcadasArrecadadasProprios

class ReceitasArrecadadasPropriosRepository:
    def __init__(self):
        self.conexao = ConexaoClickhouse() 
        
    def obter_receitasArrecadadasProprios(self, entidades, idquadrimestres, ano): 

    # Join the values in each list separately
        entidades_str = ','.join([str(x) for x in entidades])
        idquadrimestres_str = ','.join([str(x) for x in idquadrimestres])
        ano_str = ','.join([str(x) for x in ano])
        
        query = """
                SELECT dsclassificacaoreceita::text , 
                    replace(cast(cast(sum(valororcado) as numeric(16,4)) as text),'.',',') as valororcado,
                    replace(cast(cast(sum(valorrealizado) as numeric(16,4)) as text),'.',',') as valorrealizado  
                from {}.aud_receita_orcada_realizada_proprias 
                where cdentidade = 1
                    and idquadrimestre in ({})
                    and dsclassificacaoreceita <> 'OUTRAS RECEITAS' 
                    and nrano = {}
                GROUP BY dsclassificacaoreceita
                order by dsclassificacaoreceita
        """.format(entidades_str, idquadrimestres_str, ano_str)
        
        # Debugging the generated query
        print("Generated SQL query: ", query)

        # Execute the query
        client = self.conexao.obter_cliente()
        resultado = client.query(query).result_rows
        
        # Process the results
        receitas = [ReceitasOrcadasArrecadadasProprios(r[0], r[1], r[2]) for r in resultado]

        return receitas

            

