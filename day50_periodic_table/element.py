class Element:
    def __init__(self, csv_data):
        self.init_element(csv_data)

    def get_details(self):
        return {
            'Atomic number': self.atomic_number,
            'Symbol': self.symbol,
            'Element': self.element,
            'Origin of name': self.origin_of_name,
            'Group': self.group,
            'Period': self.period,
            'Atomic weight': self.atomic_weight + ' u',
            'Density': self.density + ' g/cm^3',
            'Melting point': self.melting_point + ' K',
            'Boiling point': self.boiling_point + ' K',
            'Specific heat capacity': self.specific_heat_capacity + ' J/(g*K)',
            'Electronegativity': self.electronegativity,
            'Abundance in earth\'s crust': self.abundance_in_earths_crust + ' mg/kg'
        }

    def init_element(self, csv_data):
        self.atomic_number = csv_data[0]
        self.symbol = csv_data[1]
        self.element = csv_data[2]
        self.origin_of_name = csv_data[3]
        self.group = csv_data[4]
        self.period = csv_data[5]
        self.atomic_weight = csv_data[6]
        self.density = csv_data[7]
        self.melting_point = csv_data[8]
        self.boiling_point = csv_data[9]
        self.specific_heat_capacity = csv_data[10]
        self.electronegativity = csv_data[11]
        self.abundance_in_earths_crust = csv_data[12]
