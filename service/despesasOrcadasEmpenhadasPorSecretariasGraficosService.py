from repository.despesasOrcadasEmpenhadasPorSecretariasGraficosRepository import DespesasOrcadasEmpenhadasPorSecretariasGraficosRepository

class DespesasOrcadasEmpenhadasPorSecretariasGraficosService:
    def __init__(self):
        self.repository = DespesasOrcadasEmpenhadasPorSecretariasGraficosRepository()

    def obter_despesasOrcadasEmpenhadasPorSecretariasGraficosService(self, entidades, idquadrimestres, ano):
        despesas = self.repository.obter_despesasOrcadasEmpenhadasPorSecretariasGraficosRepository(entidades, idquadrimestres, ano)
        
        return [despesa.to_dict() for despesa in despesas]
