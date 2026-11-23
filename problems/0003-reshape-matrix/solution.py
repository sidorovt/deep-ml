import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    [[1,2,3,4],
     [5,6,7,8]]
    arr = np.array(a)
    try:
        reshaped_matrix = arr.reshape(new_shape).tolist()
    except ValueError:
        return []
    return reshaped_matrix