from repository.despesasOrcadasEmpenhadasPorSecretariasRepository import DespesasOrcadasEmpenhadasPorSecretariasRepository

class DespesasOrcadasEmpenhadasPorSecretariasService:
    def __init__(self):
        self.repository = DespesasOrcadasEmpenhadasPorSecretariasRepository()

    def obter_despesasOrcadasEmpenhadasPorSecretariasService(self, entidades, idquadrimestres, ano):
        despesas = self.repository.obter_despesasOrcadasEmpenhadasPorSecretariasRepository(entidades, idquadrimestres, ano)
        
        return [despesa.to_dict() for despesa in despesas]
