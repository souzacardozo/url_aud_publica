class DespesasOrcadasEmpenhadasPagasPorSecretarias:
    def __init__(self, dsclassificacaodespesa, valororcado, valorpago):
        self.dsclassificacaodespesa = dsclassificacaodespesa
        self.valororcado = valororcado
        self.valorpago = valorpago

    def to_dict(self):
        return {
            "dsclassificacaodespesa": self.dsclassificacaodespesa,
            "valororcado": self.valororcado,
            "valorpago": self.valorpago
        }