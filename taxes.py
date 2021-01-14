from abc import ABCMeta, abstractmethod


class Taxes(object):

    def __init__(self, other_tax=None):
        self.__other_tax = other_tax

    def calculus_other_tax(self, buget):
        if self.__other_tax is None:
            return 0
        else:
            return self.__other_tax.calculus(buget)

    @abstractmethod
    def calculus(self, buget):
        pass


class Tax_template(Taxes):

    __metaclass__ = ABCMeta

    def calculus(self, buget):
        if self.should_max_tax(buget):
            return self.max_tax(buget) + self.calculus_other_tax(buget)
        else:
            return self.min_tax(buget) + self.calculus_other_tax(buget)

    @abstractmethod
    def should_max_tax(self, buget):
        pass

    @abstractmethod
    def max_tax(self, buget):
        pass

    @abstractmethod
    def min_tax(self, buget):
        pass


def IPVX(method_or_function):
    def wrapper(self, buget):
        return method_or_function(self, buget) + 50
    return wrapper


class ISS(Taxes):

    @IPVX
    def calculus(self, buget):
        return buget.ammount * 0.1 + self.calculus_other_tax(buget)


class ICMS(Taxes):
    def calculus(self, buget):
        return buget.ammount * 0.06 + self.calculus_other_tax(buget)


class ICPP(Tax_template):

    def should_max_tax(self, buget):
        return buget.ammount > 500

    def max_tax(self, buget):
        return buget.ammount * 0.07

    def min_tax(self, buget):
        return buget.ammount * 0.05


class IKCV(Tax_template):

    def should_max_tax(self, buget):
        return buget.ammount > 500 and self.__item_has_more_than_one_hundred(buget)

    def max_tax(self, buget):
        return buget.ammount * 0.1

    def min_tax(self, buget):
        return buget.ammount * 0.06

    def __item_has_more_than_one_hundred(self, buget):

        for item in buget.get_itens():
            if item.ammount > 100:
                return True

        return False

