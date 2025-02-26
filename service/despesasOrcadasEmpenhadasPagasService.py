from repository.despesasOrcadasEmpenhadasPagasRepository import DespesasOrcadasEmpenhadasPagasRepository

class DespesasOrcadasEmpenhadasPagasService:
    def __init__(self):
        self.repository = DespesasOrcadasEmpenhadasPagasRepository()

    def obter_despesasOrcadasEmpenhadasPagasService(self, entidades, idquadrimestres, ano):
        despesas = self.repository.obter_despesasOrcadasEmpenhadasPagasRepository(entidades, idquadrimestres, ano)
        
        return [despesa.to_dict() for despesa in despesas]
