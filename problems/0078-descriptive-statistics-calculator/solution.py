import numpy as np
from collections import Counter

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    
    if len(data) == 0:
        raise ValueError("data must not be empty")

    data = np.asarray(data)
    q1, q2, q3 = np.percentile(data, 25), np.percentile(data, 50), np.percentile(data, 75)

    counts = Counter(data.tolist())
    max_count = max(counts.values())
    modes = [v for v, c in counts.items() if c == max_count]
    mode = modes[0]
    

    return {"mean": np.mean(data),
            "median": np.median(data),
            "mode": mode,
            "variance": np.var(data),
            "standard_deviation": np.std(data),
            "25th_percentile": q1,
            "50th_percentile": q2,
            "75th_percentile": q3,
            "interquartile_range": q3 - q1
    }