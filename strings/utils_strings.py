from dateutil.parser import parse


def is_date(input_string: str, fuzzy: bool = False) -> bool:
    """This function checks whether in the input string there is a date
    Args:
        input_string: str, string to check for date
        fuzzy: bool, ignore unknown tokens in string if True
    Returns:
         True: whether the string can be interpreted as a date.
         False: otherwise
    """
    try:
        parse(input_string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

    
def keep_only_digits(input_string: str) -> str:
    """This function takes as input a string and returns the same string but only containing digits
    Args:
        input_string (str): the input string from which we want to remove non-digit characters
    Returns:
        output_string (str): the output string that only contains digit characters
    """
    numeric_filter = filter(str.isdigit, input_string)
    output_string = "".join(numeric_filter)
    
    return output_string
