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
