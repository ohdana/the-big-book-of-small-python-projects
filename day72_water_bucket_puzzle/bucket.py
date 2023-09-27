class Bucket:
    def __init__(self, capacity_litres):
        self.capacity = int(capacity_litres)
        self.current_water_level = 0

    def fill(self):
        self.current_water_level = self.capacity

    def empty(self):
        self.current_water_level = 0

    def add(self, litres):
        self.current_water_level = self.current_water_level + litres

    def remove(self, litres):
        self.current_water_level = self.current_water_level - litres

    def get_stats(self):
        return self.capacity, self.current_water_level

    def get_current_water_level(self):
        return self.current_water_level
