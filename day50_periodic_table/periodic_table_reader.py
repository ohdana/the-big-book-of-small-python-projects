from element import Element

FILENAME = 'periodictable.csv'

class PeriodicTableReader:
    def __init__(self):
        self.init_elements_data()

    def get_elements(self):
        return self.elements

    def init_elements_data(self):
        data = read_data_from_csv()
        elements = []
        for line in data:
            elements.append(Element(line))
        self.elements = elements
        print(elements)

    def read_data_from_csv(self):
        file = open(FILENAME, encoding='utf-8')
        csv_reader = file.reader(file)
        data = list(lines)
        file.close()

        return data
