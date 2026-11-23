def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []

    if mode == "row":
        for row in matrix:
            means.append(sum(row)/len(row))
    
    elif mode == "column":
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        for col in range(num_cols):
            col_sum = sum(matrix[row][col] for row in range(num_rows))
            means.append(col_sum/num_rows)

    return means