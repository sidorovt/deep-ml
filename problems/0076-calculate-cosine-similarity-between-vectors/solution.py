import numpy as np

def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    if v1 is not None and v2 is not None:
        if len(v1) == len(v2):
            dot_product = np.dot(v1, v2)
            norm_v1, norm_v2 = np.sqrt(sum(x**2 for x in v1)), np.sqrt(sum(x**2 for x in v2))
            if norm_v1 == 0 or norm_v2 == 0:
                return "Vectors cannot have zero magnitude"
            result = dot_product/(norm_v1*norm_v2)
            return result
        else:
            return "Vectors must be the same shape"
    else:
        return "Vectors cannot be empty or have zero magnitude"