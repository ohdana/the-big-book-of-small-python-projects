class LinesBuilder():
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def get_rows(self):
        rows = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append((j, i))
            rows.append(row)

        return rows

    def get_columns(self):
        columns = []
        for i in range(self.width):
            column = []
            for j in range(self.height):
                column.append((i, j))
            columns.append(column)

        return columns

    def get_diagonals(self):
        return self.get_downward_diagonals() + self.get_upward_diagonals()

    def get_downward_diagonals(self):
        diagonals = []
        start_cells = []
        for i in range(self.height - 1):
            start_cells.append((i, 0))
        for j in range(self.width):
            start_cells.append((0, j))

        diagonals = []
        for cell in set(start_cells):
            diagonals.append(self.build_downward_diagonal(cell))

        return diagonals

    def get_upward_diagonals(self):
        diagonals = []
        start_cells = []
        for i in range(self.height):
            start_cells.append((i, 0))
        for j in range(self.width):
            start_cells.append((self.height - 1, j))

        diagonals = []
        for cell in set(start_cells):
            diagonals.append(self.build_upward_diagonal(cell))

        return diagonals

    def build_downward_diagonal(self, cell):
        x, y = cell
        cells = []
        while y < self.width and x < self.height:
            cells.append((y, x))
            x += 1
            y += 1
        return cells

    def build_upward_diagonal(self, cell):
        x, y = cell
        cells = []
        while x >= 0 and y >= 0:
            if y < self.width and x < self.height:
                cells.append((y, x))
            x -= 1
            y += 1

        return cells
