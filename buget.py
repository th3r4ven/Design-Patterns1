class Buget(object):

    def __init__(self):
        self.__itens = []

    @property
    def ammount(self):  # getter
        total = 0.0
        for item in self.__itens:
            total += item.ammount
        return total

    def get_itens(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    def add_itens(self, item):
        self.__itens.append(item)


class Item(object):

    def __init__(self, name, ammount):  # Constructor with setters
        self.__name = name
        self.__ammount = ammount

    @property
    def ammount(self):  # Getter
        return self.__ammount

    @property
    def name(self):  # Getter
        return self.__name

