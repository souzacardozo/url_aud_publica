from repository.receitasOrcadasArrecadadasEstaduaisGraficosRepository import ReceitasOrcadasArrecadadasEstaduaisGraficosRepository

class ReceitasOrcadasArrecadadasEstaduaisGraficosService:
    def __init__(self):
        self.repository = ReceitasOrcadasArrecadadasEstaduaisGraficosRepository()

    def obter_receitasOrcadasArrecadadasEstaduaisGraficosService(self, entidades, idquadrimestres, ano):
        receitas = self.repository.obter_receitasOrcadasArrecadadasEstaduaisGraficos(entidades, idquadrimestres, ano)
        return [receita.to_dict() for receita in receitas]
