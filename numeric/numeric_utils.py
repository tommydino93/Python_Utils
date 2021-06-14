import math


def round_half_up(n: float, decimals: float = 0) -> float:
    """This function rounds to the nearest integer number (e.g 2.4 becomes 2.0 and 2.6 becomes 3);
     in case of tie, it rounds up (e.g. 1.5 becomes 2.0 and not 1.0)
    Args:
        n (float): number to round
        decimals (int): number of decimal figures that we want to keep; defaults to zero
    Returns:
        rounded_number (float): input number rounded with the desired decimals
    """
    multiplier = 10 ** decimals
    
    rounded_number = math.floor(n*multiplier + 0.5) / multiplier
    
    return rounded_number
