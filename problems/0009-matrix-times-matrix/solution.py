import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    a, b = np.array(a), np.array(b)

    if a[0].size != b[0].size:
        return -1
    
    return a @ b