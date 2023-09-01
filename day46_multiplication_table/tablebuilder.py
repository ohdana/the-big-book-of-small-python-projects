class TableBuilder:
    def __init__(self, max_number):
        self.max_number = max_number
        self.gap = self.calculate_gap()

    def calculate_gap(self):
        max_product = self.max_number * self.max_number
        return len(str(max_product)) + 1

    def build(self):
        headers = self.get_headers()
        products = self.get_products_lines()
        return headers + products

    def show(self):
        canvas = self.build()
        print('\n'.join(canvas))

    def get_headers(self):
        numbers = range(self.max_number + 1)
        first_line = ' ' * self.gap + '|'
        for i in range(self.max_number + 1):
            first_line += self.get_formatted_number(i)

        second_line = '-' * self.gap + '+' + '-' * self.gap * len(numbers)
        return [first_line, second_line]

    def get_products_lines(self):
        return [self.get_products_line(i) for i in range(self.max_number + 1)]

    def get_products_line(self, number):
        line = ' ' * (self.gap - len(str(number))) + str(number) + '|'
        for i in range(self.max_number + 1):
            product = i * number
            line += self.get_formatted_number(product)

        return line

    def get_formatted_number(self, number):
        return (self.gap - len(str(number))) * ' ' + str(number)
