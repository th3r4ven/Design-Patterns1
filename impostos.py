from abc import ABCMeta, abstractmethod


class Template_de_imposto(object):

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.should_max_tax(orcamento):
            return self.max_tax(orcamento)
        else:
            return self.min_tax(orcamento)

    @abstractmethod
    def should_max_tax(self, orcamento):
        pass

    @abstractmethod
    def max_tax(self, orcamento):
        pass

    @abstractmethod
    def min_tax(self, orcamento):
        pass


class ISS(object):

    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ICMS(object):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06


class ICPP(Template_de_imposto):

    def should_max_tax(self, orcamento):
        return orcamento.valor > 500

    def max_tax(self, orcamento):
        return orcamento.valor * 0.07

    def min_tax(self, orcamento):
        return orcamento.valor * 0.05


class IKCV(Template_de_imposto):

    def should_max_tax(self, orcamento):
        return orcamento.valor > 500 and self.__item_maior_que_cem(orcamento)

    def max_tax(self, orcamento):
        return orcamento.valor * 0.1

    def min_tax(self, orcamento):
        return orcamento.valor * 0.06

    def __item_maior_que_cem(self, orcamento):

        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True

        return False

