from repository.despesaOrcadaPagaRepository import DespesaOrcadaPagaRepository

class DespesaOrcadaPagaService:
    def __init__(self):
        self.repository = DespesaOrcadaPagaRepository()

    def obter_despesas(self, idquadrimestres):
        despesas = self.repository.obter_despesas(idquadrimestres)
        return [despesa.to_dict() for despesa in despesas]
