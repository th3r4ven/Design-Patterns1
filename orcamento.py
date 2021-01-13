class Orcamento(object):

    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):  # getter
        return self.__valor


