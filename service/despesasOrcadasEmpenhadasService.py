from repository.despesasOrcadasEmpenhadasRepository import DespesasOrcadasEmpenhadasRepository

class DespesasOrcadasEmpenhadasService:
    def __init__(self):
        self.repository = DespesasOrcadasEmpenhadasRepository()

    def obter_despesasOrcadasEmpenhadasService(self, entidades, idquadrimestres, ano):
        despesas = self.repository.obter_despesasOrcadasEmpenhadasRepository(entidades, idquadrimestres, ano)
        
        return [despesa.to_dict() for despesa in despesas]
