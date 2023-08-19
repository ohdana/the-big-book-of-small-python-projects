def get_diagonals(width, height):
    return get_downward_diagonals(width, height) + get_upward_diagonals(width, height)

def get_downward_diagonals(width, height):
    diagonals = []
    start_cells = []
    for i in range(height - 1):
        start_cells.append((i, 0))
    for j in range(width):
        start_cells.append((0, j))

    diagonals = []
    for cell in set(start_cells):
        diagonals.append(build_downward_diagonal(width, height, cell))

    return diagonals

def get_upward_diagonals(width, height):
    diagonals = []
    start_cells = []
    for i in range(height):
        start_cells.append((i, 0))
    for j in range(width):
        start_cells.append((height - 1, j))

    diagonals = []
    for cell in set(start_cells):
        diagonals.append(build_upward_diagonal(width, height, cell))

    return diagonals

def build_downward_diagonal(width, height, cell):
    x, y = cell
    cells = []
    while y < width and x < height:
        cells.append((y, x))
        x += 1
        y += 1
    return cells

def build_upward_diagonal(width, height, cell):
    x, y = cell
    cells = []
    while x >= 0 and y >= 0:
        if y < width and x < height:
            cells.append((y, x))
        x -= 1
        y += 1

    return cells
