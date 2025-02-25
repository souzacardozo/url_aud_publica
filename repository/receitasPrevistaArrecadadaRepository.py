from conexao.conexao import ConexaoClickhouse
from model.receitasPrevistaArrecadada import ReceitaPrevistaArrecadada

class ReceitasPrevistaArrecadadaRepository:
    def __init__(self):
        self.conexao = ConexaoClickhouse()
        
    def obter_receitasPrevistaArrecadada(self, idquadrimestres):
        query = """
                SELECT dsclassificacaoreceita::text , 
                    replace(cast(cast(sum(valororcado) as numeric(16,4)) as text),'.',',') as valororcado,
                    replace(cast(cast(sum(valorrealizado) as numeric(16,4)) as text),'.',',') as valorrealizado  
                from terraboapm.aud_receita_orcada_realizada 
                where cdentidade = 1
                    and idquadrimestre in ({})
                    and dsclassificacaoreceita <> 'OUTRAS RECEITAS' 
                    and nrano = 2024
                GROUP BY dsclassificacaoreceita
                order by dsclassificacaoreceita
        """.format(','.join([str(x) for x in idquadrimestres]))

        client = self.conexao.obter_cliente()
        resultado = client.query(query).result_rows
        receitas = [ReceitaPrevistaArrecadada(r[0], r[1], r[2]) for r in resultado]
        
        return receitas
