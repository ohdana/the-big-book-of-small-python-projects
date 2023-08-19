def get_columns(width, height):
    columns = []
    for i in range(width):
        column = []
        for j in range(height):
            column.append((i, j))
        columns.append(column)

    return columns
