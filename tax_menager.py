from taxes import *


class Tax_calculator():

    def do_calculus(self, Budget, tax):

        final_tax = tax.calculus(Budget)

        print(final_tax)


if __name__ == '__main__':
    from budget import *

    calculador = Tax_calculator()

    budget = Budget()
    budget.add_itens(Item('Item 01', 50))
    budget.add_itens(Item('Item 02', 200))
    budget.add_itens(Item('Item 03', 250))

    print("Total budget: " + str(budget.ammount) + "\n")
    calculador.do_calculus(budget, ISS())
    calculador.do_calculus(budget, ISS(ICMS()))
    calculador.do_calculus(budget, ICMS())
    print("=====")
    calculador.do_calculus(budget, ICPP())
    calculador.do_calculus(budget, ICPP(IKCV(ISS(ICMS()))))
    calculador.do_calculus(budget, IKCV())
