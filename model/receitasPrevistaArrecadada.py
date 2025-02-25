class ReceitaPrevistaArrecadada:
    def __init__(self, dsclassificacaoreceita, valororcado, valorarrecadado):
        self.dsclassificacaoreceita = dsclassificacaoreceita
        self.valororcado = valororcado
        self.valorarrecadado = valorarrecadado

    def to_dict(self):
        return {
            "dsclassificacaoreceita": self.dsclassificacaoreceita,
            "valororcado": self.valororcado,
            "valorarrecadado": self.valorarrecadado
        }
