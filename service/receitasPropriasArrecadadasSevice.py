from repository.receitasPropriasArrecadadasRepository import ReceitasPropriasArrecadadasRepository

class ReceitasPropriasArrecadadasService:
    def __init__(self):
        self.repository = ReceitasPropriasArrecadadasRepository()

    def obter_receitasPropriasArrecadadas(self, entidades, idquadrimestres, ano):
        receitas = self.repository.obter_receitasPropriasArrecadadas(entidades, idquadrimestres, ano)
        return [receita.to_dict() for receita in receitas]
