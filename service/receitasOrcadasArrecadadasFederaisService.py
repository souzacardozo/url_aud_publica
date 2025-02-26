from repository.receitasOrcadasArrecadadasFederaisRepository import ReceitasOrcadasArrecadadasFederaisRepository

class ReceitasOrcadasArrecadadasFederaisService:
    def __init__(self):
        self.repository = ReceitasOrcadasArrecadadasFederaisRepository()

    def obter_receitasOrcadasArrecadadasFederaisService(self, entidades, idquadrimestres, ano):
        receitas = self.repository.obter_receitasOrcadasArrecadadasFederais(entidades, idquadrimestres, ano)
        return [receita.to_dict() for receita in receitas]
