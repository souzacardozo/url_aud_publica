from repository.despesasOrcadasEmpenhadasPagasPorSecretariasGraficosRepository import DespesasOrcadasEmpenhadasPagasPorSecretariasGraficosRepository

class DespesasOrcadasEmpenhadasPagasPorSecretariasGraficosService:
    def __init__(self):
        self.repository = DespesasOrcadasEmpenhadasPagasPorSecretariasGraficosRepository()

    def obter_despesasOrcadasEmpenhadasPagasPorSecretariasGraficosService(self, entidades, idquadrimestres, ano):
        despesas = self.repository.obter_despesasOrcadasEmpenhadasPagasPorSecretariasGraficosRepository(entidades, idquadrimestres, ano)        
        return [despesa.to_dict() for despesa in despesas]
