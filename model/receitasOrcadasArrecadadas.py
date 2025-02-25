class ReceitasOrcadasArrecadadas:
    def __init__(self, dsclassificacaoreceita, valororcado, valorarrecadado, realizado):
        self.dsclassificacaoreceita = dsclassificacaoreceita
        self.valororcado = valororcado
        self.valorarrecadado = valorarrecadado
        self.realizado = realizado

    def to_dict(self):
        return {
            "dsclassificacaoreceita": self.dsclassificacaoreceita,
            "valororcado": self.valororcado,
            "valorarrecadado": self.valorarrecadado,
            "realizado": self.realizado
        }
