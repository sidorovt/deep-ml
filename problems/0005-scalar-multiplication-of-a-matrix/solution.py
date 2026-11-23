def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    new_matrix = []
    for row in matrix:
        new_row = []
        for col in row:
            new_row.append(col * scalar)
        new_matrix.append(new_row)
    
    return new_matrix