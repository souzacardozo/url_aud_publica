from repository.despesasOrcadasEmpenhadasGraficosRepository import DespesasOrcadasEmpenhadasGraficosRepository

class DespesasOrcadasEmpenhadasGraficosService:
    def __init__(self):
        self.repository = DespesasOrcadasEmpenhadasGraficosRepository()

    def obter_despesasOrcadasEmpenhadasGraficosService(self, entidades, idquadrimestres, ano):
        despesas = self.repository.obter_despesasOrcadasEmpenhadasGraficosRepository(entidades, idquadrimestres, ano)
        
        return [despesa.to_dict() for despesa in despesas]
