from repository.receitasOrcadasArrecadadasGraficosRepository import ReceitasOrcadasArrecadadasGraficosRepository

class ReceitasOrcadasArrecadadasGraficosService:
    def __init__(self):
        self.repository = ReceitasOrcadasArrecadadasGraficosRepository()

    def obter_receitasOrcadasArrecadadasGraficos(self, entidades, idquadrimestres, ano):
        receitas = self.repository.obter_receitasOrcadasArrecadadasGraficos(entidades, idquadrimestres, ano)
        return [receita.to_dict() for receita in receitas]
