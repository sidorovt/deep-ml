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
    if v1.size == 0 or v2.size == 0:
        return "Vectors cannot be empty"
    if v1.shape != v2.shape:
        return "Vectors cannot have different shape"

    # norm_v1, norm_v2 = np.sqrt(sum(x**2 for x in v1)), np.sqrt(sum(x**2 for x in v2))
    norm_v1, norm_v2 = np.linalg.norm(v1), np.linalg.norm(v2)
    if norm_v1 == 0 or norm_v2 == 0:
        return "Vectors cannot have zero magnitude"
    return np.dot(v1, v2)/(norm_v1*norm_v2)