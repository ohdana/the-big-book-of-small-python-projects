def get_rows(width, height):
    rows = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append((j, i))
        rows.append(row)

    return rows
