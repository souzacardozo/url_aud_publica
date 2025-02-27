from repository.despesasOrcadasEmpenhadasPagasGraficosRepository import DespesasOrcadasEmpenhadasPagasGraficosRepository

class DespesasOrcadasEmpenhadasPagasGraficosService:
    def __init__(self):
        self.repository = DespesasOrcadasEmpenhadasPagasGraficosRepository()

    def obter_despesasOrcadasEmpenhadasPagasGraficosService(self, entidades, idquadrimestres, ano):
        despesas = self.repository.obter_despesasOrcadasEmpenhadasPagasGraficosRepository(entidades, idquadrimestres, ano)
        
        return [despesa.to_dict() for despesa in despesas]
