class Lancamento:
    def __init__(self, valor, categoria, data, tipo="saida"):
        self.__valor = float(valor)
        self.__categoria = categoria
        self.__tipo = tipo
        self.__data = data

    def valor(self):
        return self.__valor

    def categoria(self):
        return self.__categoria

    def tipo(self):
        return self.__tipo

    def data(self):
        return self.__data