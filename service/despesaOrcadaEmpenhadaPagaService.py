from repository.despesaOrcadaEmpenhadaPagaRepository import DespesaOrcadaEmpenhadaPagaRepository

class DespesaOrcadaEmpenhadaPagaService:
    def __init__(self):
        self.repository = DespesaOrcadaEmpenhadaPagaRepository()

    def obter_despesaOrcadaEmpenhadaPagaService(self, entidades, idquadrimestres, ano):
        despesas = self.repository.obter_despesaOrcadaEmpenhadaPagaRepository(entidades, idquadrimestres, ano)
        
        return [despesa.to_dict() for despesa in despesas]
