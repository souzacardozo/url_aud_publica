from repository.receitasOrcadasArrecadadasPropriosRepository import ReceitasOrcadasArrecadadasPropriosRepository

class ReceitasOrcadasArrecadadasPropriosService:
    def __init__(self):
        self.repository = ReceitasOrcadasArrecadadasPropriosRepository()

    def obter_receitasOrcadasArrecadadasPropriosService(self, entidades, idquadrimestres, ano):
        receitas = self.repository.obter_receitasOrcadasArrecadadasProprios(entidades, idquadrimestres, ano)
        return [receita.to_dict() for receita in receitas]
