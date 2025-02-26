from repository.receitasOrcadasArrecadadasEstaduaisRepository import ReceitasOrcadasArrecadadasEstaduaisRepository

class ReceitasOrcadasArrecadadasEstaduaisService:
    def __init__(self):
        self.repository = ReceitasOrcadasArrecadadasEstaduaisRepository()

    def obter_receitasOrcadasArrecadadasEstaduaisService(self, entidades, idquadrimestres, ano):
        receitas = self.repository.obter_receitasOrcadasArrecadadasEstaduais(entidades, idquadrimestres, ano)
        return [receita.to_dict() for receita in receitas]
