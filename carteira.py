class Carteira:
    def __init__(self, saldo_inicial=0.0):
        self.__saldo_inicial = float(saldo_inicial)
        self.__lancamentos = []

    def definir_saldo_inicial(self, valor):
        self.__saldo_inicial = float(valor)

    def saldo_inicial(self):
        return self.__saldo_inicial

    def adicionar(self, lancamento):
        self.__lancamentos.append(lancamento)

    def limpar(self):
        self.__saldo_inicial = 0.0
        self.__lancamentos.clear()

    def total_geral(self):
        return sum(item.valor() for item in self.__lancamentos)

    def saldo_atual(self):
        return self.__saldo_inicial - self.total_geral()

    def total_por_categoria(self, categoria):
        return sum(
            item.valor()
            for item in self.__lancamentos
            if item.categoria() == categoria
        )

    def lancamentos(self):
        return self.__lancamentos