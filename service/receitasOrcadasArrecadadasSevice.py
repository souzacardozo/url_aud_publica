from repository.receitasOrcadasArrecadadasRepository import ReceitasOrcadasArrecadadasRepository

class ReceitasOrcadasArrecadadasService:
    def __init__(self):
        self.repository = ReceitasOrcadasArrecadadasRepository()

    def obter_receitasOrcadasArrecadadas(self, idquadrimestres):
        receitas = self.repository.obter_receitasOrcadasArrecadadas(idquadrimestres)
        return [receita.to_dict() for receita in receitas]
