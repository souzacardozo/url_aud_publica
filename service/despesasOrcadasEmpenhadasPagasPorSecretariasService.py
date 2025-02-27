from repository.despesasOrcadasEmpenhadasPagasPorSecretariasRepository import DespesasOrcadasEmpenhadasPagasPorSecretariasRepository

class DespesasOrcadasEmpenhadasPagasPorSecretariasService:
    def __init__(self):
        self.repository = DespesasOrcadasEmpenhadasPagasPorSecretariasRepository()

    def obter_despesasOrcadasEmpenhadasPagasPorSecretariasService(self, entidades, idquadrimestres, ano):
        despesas = self.repository.obter_despesasOrcadasEmpenhadasPagasPorSecretariasRepository(entidades, idquadrimestres, ano)        
        return [despesa.to_dict() for despesa in despesas]
