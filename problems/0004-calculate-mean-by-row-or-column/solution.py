import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    matrix = np.array(matrix)
    if mode == "row":
        return matrix.mean(axis=1).tolist()
    elif mode == "column":
        return matrix.mean(axis=0).tolist()
    raise ValueError(f"Unknown mode: {mode}")