from descontos import *


class Calculador_de_descontos(object):

    def calcula(self, orcamento):
        desconto = Desconto_por_cinco_itens(Desconto_por_mais_de_quinhentos_reais(Sem_desconto)).calcula(orcamento)

        return desconto


if __name__ == '__main__':
    from buget import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_itens(Item('Item 01', 100))
    orcamento.adiciona_itens(Item('Item 02', 50))
    orcamento.adiciona_itens(Item('Item 03', 400))

    calculador = Calculador_de_descontos()

    desconto = calculador.calcula(orcamento)

    print("Desconto calculado %s" % desconto)
