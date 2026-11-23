class Grafico:
    def __init__(self, carteira):
        self.__carteira = carteira

    def percentuais_por_categoria(self, categorias):
        total = self.__carteira.total_geral()
        resultado = {}

        for categoria in categorias:
            valor_cat = self.__carteira.total_por_categoria(categoria)
            if total > 0:
                percentual = (valor_cat / total) * 100
            else:
                percentual = 0.0
            resultado[categoria] = round(percentual, 1)

        return resultado