import numpy as np
from typing import Any


def find_most_frequent_value(input_array: np.ndarray) -> Any:
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
    
    
def has_nans(input_array: np.ndarray) -> bool:
    """"This function checks whether the input array contains any nan.
    If yes, it returns True, otherwise it returns False.
    Args:
        input_array (np.ndarray): input array where we check for nans
    Returns:
        array_has_nan (bool): True if input_array contains nans; False otherwise
    """
    array_sum = np.sum(input_array)
    array_has_nan = np.isnan(array_sum)
    
    return array_has_nan


def is_binary(input_array: np.ndarray) -> bool:
    """This function checks whether the input array is binary (i.e. contains only 0s and 1s).
    If yes, it returns True, otherwise it returns False.
    Args:
        input_array (np.ndarray): input array that we want to inspect
    Returns:
        array_is_binary (bool): True if input_array is binary; False otherwise
    """
    array_is_binary = np.array_equal(input_array, input_array.astype(bool))
    
    return array_is_binary
    

def has_values_all_in_range(input_array: np.ndarray, low: int, high: int) -> bool:
    """This function checks whether the input array has values that lie within the range (low, high).
    If yes, it returns True, otherwise it returns False.
    Args:
        input_array (np.ndarray): input array that we want to inspect
        low (int): lower bound
        high (int): upper bound
    Returns:
        array_is_withing_range (bool): True if input_array has values in range (low, high); False otherwise
    """
    mask_array_bool = (input_array > low) & (input_array < high)
        
    if False in mask_array_bool:  # if there is just one False value
        array_is_withing_range = False
    else:  # if instead all values are True
        array_is_withing_range = True
            
    return array_is_withing_range
