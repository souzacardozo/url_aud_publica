from repository.receitasPrevistaArrecadadaRepository import ReceitasPrevistaArrecadadaRepository

class ReceitasPrevistaArrecadadaService:
    def __init__(self):
        self.repository = ReceitasPrevistaArrecadadaRepository()

    def obter_receitasPrevistaArrecadada(self, idquadrimestres):
        receitas = self.repository.obter_receitasPrevistaArrecadada(idquadrimestres)
        return [receita.to_dict() for receita in receitas]
