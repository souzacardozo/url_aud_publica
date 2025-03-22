class ReceitasOrcadasArrecadadasGraficos:
    def __init__(self, dsclassificacaoreceita, valororcado, percentual):
        self.dsclassificacaoreceita = dsclassificacaoreceita
        self.valororcado = valororcado
        self.percentual = percentual 

    def to_dict(self):
        return {
            "dsclassificacaoreceita": self.dsclassificacaoreceita,
            "valororcado": self.valororcado,
            "percentual": self.percentual
        }