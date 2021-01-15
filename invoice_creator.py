from datetime import date
from invoice import Invoice


class Invoice_creator(object):

    def __init__(self):
        self.__company_name = None
        self.__cnpj = None
        self.__emission_date = date.today()
        self.__items = None
        self.__details = ''
        self.__observer = []

    def with_company_name(self, company_name):
        self.__company_name = company_name
        return self

    def with_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def with_emission_date(self, emisison_date):
        self.__emission_date = emisison_date
        return self

    def with_items(self, items):
        self.__items = items
        return self

    def with_details(self, details):
        self.__details = details
        return self

    def with_observer(self, observer):
        for obs in observer:
            self.__observer.append(obs)
        return self

    def builder(self):

        if self.__company_name is None:
            raise Exception('Company name should be given')
        if self.__cnpj is None:
            raise Exception('CNPJ should be given')
        if self.__items is None:
            raise Exception('Items should be given')

        return Invoice(
            self.__company_name,
            self.__cnpj,
            self.__items,
            self.__emission_date,
            self.__details,
            self.__observer
        )
