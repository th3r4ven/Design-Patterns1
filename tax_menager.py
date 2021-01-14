from taxes import *


class Tax_calculator():

    def do_calculus(self, buget, tax):

        final_tax = tax.calculus(buget)

        print(final_tax)


if __name__ == '__main__':
    from buget import *

    calculador = Tax_calculator()

    buget = Buget()
    buget.add_itens(Item('Item 01', 50))
    buget.add_itens(Item('Item 02', 200))
    buget.add_itens(Item('Item 03', 250))

    print("Total buget: " + str(buget.ammount) + "\n")
    calculador.do_calculus(buget, ISS())
    calculador.do_calculus(buget, ISS(ICMS()))
    calculador.do_calculus(buget, ICMS())
    print("=====")
    calculador.do_calculus(buget, ICPP())
    calculador.do_calculus(buget, ICPP(IKCV(ISS(ICMS()))))
    calculador.do_calculus(buget, IKCV())
