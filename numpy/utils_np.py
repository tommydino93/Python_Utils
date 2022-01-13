import numpy as np
from typing import Any


def find_most_frequent_value(input_array: np.ndarray):
    """This function finds the most common value in the input numpy array
    Args:
        input_array (np.ndarray): input array for which we want to find the most frequent value
    Returns:
        most_frequent_value (*): most frequent value
    """
    values, counts = np.unique(input_array, return_counts=True)

    idx = np.argmax(counts)
    most_frequent_value = values[idx]  # extract the most frequent element

    return most_frequent_value
    
