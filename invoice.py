from datetime import date


class Item(object):

    def __init__(self, description, value):
        self.__description = description
        self.__value = value

    @property
    def description(self):
        return self.__description

    @property
    def value(self):
        return self.__value


class Invoice(object):

    def __init__(self, company_name, cnpj, items, emission_date, details):
        self.__company_name = company_name
        self.__cnpj = cnpj
        self.__emission_date = emission_date

        if len(details) > 20:
            raise Exception('Details can\'t have more than 20 characters')
        self.__details = details
        self.__items = items

    @property
    def company_name(self):
        return self.__company_name

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def items(self):
        return self.__items

    @property
    def emission_date(self):
        return self.__emission_date

    @property
    def details(self):
        return self.__details


if __name__ == '__main__':
    from invoice_creator import Invoice_creator

    items = [
        Item('Item A', 200),
        Item('ItemB', 200)
    ]

    invoice_builder = (
                        Invoice_creator()
                        .with_company_name('FHSA Limitada')
                        .with_cnpj('012345678901234')
                        .with_items(items).builder()
                       )
