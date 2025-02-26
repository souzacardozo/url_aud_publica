from repository.receitasOrcadasArrecadadasFederaisGraficosRepository import ReceitasOrcadasArrecadadasFederaisGraficosRepository

class ReceitasOrcadasArrecadadasFederaisGraficosService:
    def __init__(self):
        self.repository = ReceitasOrcadasArrecadadasFederaisGraficosRepository()

    def obter_receitasOrcadasArrecadadasFederaisGraficosService(self, entidades, idquadrimestres, ano):
        receitas = self.repository.obter_receitasOrcadasArrecadadasFederaisGraficos(entidades, idquadrimestres, ano)
        return [receita.to_dict() for receita in receitas]
