class Desconto_por_cinco_itens(object):

    def __init__(self, prox_desc):
        self.__proximo_desc = prox_desc

    def calcula(self, orcamento):

        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        else:
            return self.__proximo_desc.calcula(orcamento)


class Desconto_por_mais_de_quinhentos_reais(object):

    def __init__(self, prox_desc):
        self.__proximo_desc = prox_desc

    def calcula(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return self.__proximo_desc.calcula(orcamento)


class Sem_desconto(object):

    def calcula(self):
        return 0