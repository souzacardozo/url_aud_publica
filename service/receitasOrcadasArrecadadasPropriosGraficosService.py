from repository.receitasOrcadasArrecadadasPropriosGraficosRepository import ReceitasOrcadasArrecadadasPropriosGraficosRepository

class ReceitasOrcadasArrecadadasPropriosGraficosService:
    def __init__(self):
        self.repository = ReceitasOrcadasArrecadadasPropriosGraficosRepository()

    def obter_receitasOrcadasArrecadadasPropriosGraficosService(self, entidades, idquadrimestres, ano):
        receitas = self.repository.obter_receitasOrcadasArrecadadasPropriosGraficos(entidades, idquadrimestres, ano)
        return [receita.to_dict() for receita in receitas]
