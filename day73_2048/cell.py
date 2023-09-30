class Cell:
    def __init__(self, x, y, value=None):
        self.set_coords(x, y)
        self.set_value(value)

    def get_coords(self):
        return self.x, self.y

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
