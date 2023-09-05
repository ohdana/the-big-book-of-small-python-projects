from element import Element
import csv

FILENAME = 'periodictable.csv'

class PeriodicTableReader:
    def __init__(self):
        self.init_elements_data()

    def get_element(self, user_input):
        if user_input.isdigit():
            return self.lookup_by_atomic_number(int(user_input))

        return self.lookup_by_symbol(user_input.upper())

    def lookup_by_atomic_number(self, atomic_number):
        matching_elements = [element for element in self.elements if element.atomic_number == atomic_number]
        if matching_elements:
            return matching_elements[0]

    def lookup_by_symbol(self, symbol):
        matching_elements = [element for element in self.elements if element.symbol.upper() == symbol]
        if matching_elements:
            return matching_elements[0]

    def get_elements(self):
        return self.elements

    def init_elements_data(self):
        data = self.read_data_from_csv()
        elements = []
        for line in data:
            elements.append(Element(line))
        self.elements = elements

    def read_data_from_csv(self):
        file = open(FILENAME, encoding='utf-8')
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        file.close()

        return data
