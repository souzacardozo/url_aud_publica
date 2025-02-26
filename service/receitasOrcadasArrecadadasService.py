from repository.receitasOrcadasArrecadadasRepository import ReceitasOrcadasArrecadadasRepository

class ReceitasOrcadasArrecadadasService:
    def __init__(self):
        self.repository = ReceitasOrcadasArrecadadasRepository()

    def obter_receitasOrcadasArrecadadas(self, entidades, idquadrimestres, ano):
        receitas = self.repository.obter_receitasOrcadasArrecadadas(entidades, idquadrimestres, ano)
        return [receita.to_dict() for receita in receitas]
