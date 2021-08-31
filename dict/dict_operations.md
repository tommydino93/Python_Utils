## Common operations on python dictionaries

1) Iterate over dictionary
```
for key, value in a_dict.items():
    print(key, '->', value)
```

2) Sort dictionary by value (from highest to lowest)
```
def sort_dict_by_value(d, reverse=False):
    """This function sorts the input dictionary by value; the argument bool is used to decide between ascending or descending order.
    Args:
        d (dict): input dictionary that we want to sort
        reverse (bool): if True, the dict is sorted in descending value order; if False, the dict is sorted in ascending value order
    Returns:
        sorted_dict = sorted dictionary
    """
    assert sys.version_info >= (3, 6), "This function only works with python >= 3.6" 
    sorted_dict = dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
    return sorted_dict
```
