from impostos import *


class Calculador_de_impostos():

    def realiza_calculo(self, orcamento, imposto):

        imposto_calculado = imposto.calcula(orcamento)

        print(imposto_calculado)


if __name__ == '__main__':
    from orcamento import *

    calculador = Calculador_de_impostos()

    orcamento = Orcamento()
    orcamento.adiciona_itens(Item('Item 01', 100))
    orcamento.adiciona_itens(Item('Item 02', 50))
    orcamento.adiciona_itens(Item('Item 03', 400))

    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())
