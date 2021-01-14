from abc import ABCMeta, abstractmethod


class Budget_state(object):

    __metaClass__ = ABCMeta

    @abstractmethod
    def apply_extra_discount(self, budget):
        pass

    @abstractmethod
    def approve(self, budget):
        pass

    @abstractmethod
    def reprove(self, budget):
        pass

    @abstractmethod
    def finalized(self, budget):
        pass


class Ongoing(Budget_state):

    def apply_extra_discount(self, budget):
        budget.add_extra_discount(budget.ammount * 0.05)

    def approve(self, budget):
        budget.presente_state = Approved()

    def reprove(self, budget):
        budget.presente_state = Reproved()

    def finalized(self, budget):
        raise Exception('Budget Ongoing can\'t be finalized')


class Approved(Budget_state):
    def apply_extra_discount(self, budget):
        budget.add_extra_discount(budget.ammount * 0.02)

    def approve(self, budget):
        raise Exception('Budget already approved.')

    def reprove(self, budget):
        raise Exception('Approved budgets can\'t be reproved')

    def finalized(self, budget):
        budget.presente_state = Finalized()


class Reproved(Budget_state):
    def apply_extra_discount(self, budget):
        raise Exception('Reproved budgets will not receive extra discounts')

    def approve(self, budget):
        raise Exception('Reproved budgets can\'t be approved.')

    def reprove(self, budget):
        raise Exception('budget already reproved')

    def finalized(self, budget):
        budget.presente_state = Finalized()


class Finalized(Budget_state):
    def apply_extra_discount(self, budget):
        raise Exception('Finalized budgets will not receive extra discounts')

    def approve(self, budget):
        raise Exception('Finalized budgets can\'t be approved.')

    def reprove(self, budget):
        raise Exception('Finalized budgets can\'t be approved.')

    def finalized(self, budget):
        raise Exception('Budget already finalized')


class Budget(object):

    def __init__(self):
        self.__itens = []
        self.presente_state = Ongoing()
        self.__extra_discount = 0

    def approve(self):
        self.presente_state.approve(budget)

    def reprove(self):
        self.presente_state.reprove(budget)

    def finalized(self):
        self.presente_state.finalized(budget)

    def apply_extra_discount(self):
        if self.full_price == self.ammount:
            self.presente_state.apply_extra_discount(self)
        else:
            raise Exception("You can only have one discount on your budget")

    def add_extra_discount(self, discount):
        self.__extra_discount += discount

    @property
    def full_price(self):
        total = 0.0
        for item in self.__itens:
            total += item.ammount
        return total

    @property
    def ammount(self):  # getter
        total = 0.0
        for item in self.__itens:
            total += item.ammount
        return total - self.__extra_discount

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


if __name__ == '__main__':
    budget = Budget()
    budget.add_itens(Item('Item 01', 100))
    budget.add_itens(Item('Item 02', 50))
    budget.add_itens(Item('Item 03', 400))
    budget.apply_extra_discount()
    print(budget.ammount)
    budget.approve()
    # budget.apply_extra_discount()
    budget.finalized()
    print(budget.ammount)
