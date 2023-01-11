## Common operations on python dictionaries

1) Iterate over dictionary
```python
for key, value in a_dict.items():
    print(key, '->', value)
```

2) Sort dictionary by value
```python
def sort_dict_by_value(input_dict, reverse=False):
    """This function sorts the input dictionary by value; the argument bool is used to decide between ascending or descending order.
    Args:
        input_dict (dict): input dictionary that we want to sort
        reverse (bool): if True, the dict is sorted in descending value order; if False, the dict is sorted in ascending value order
    Returns:
        sorted_dict = sorted dictionary
    """
    assert sys.version_info >= (3, 6), "This function only works with python >= 3.6" 
    sorted_dict = dict(sorted(input_dict.items(), key=lambda x: x[1], reverse=reverse))
    return sorted_dict
```

3) Sort dictionary by list of keys
```python
def sort_dict_by_list_of_keys(input_dict, list_of_keys):
    """This function sorts the input dict according to a list of keys (also given as input).
    Args:
        input_dict (dict): input dictionary that we want to sort
        list_of_keys (list): list of keys; the order of the keys in the list is the exact same order of (key, value) that we want in the sorted dict
    Returns:
        reordered_dict (dict): sorted dict according to the key values in list_of_keys
    """
    assert sys.version_info >= (3, 6), "This function only works with python >= 3.6" 
    reordered_dict = {k: input_dict[k] for k in list_of_keys if k in input_dict.keys()}
    return reordered_dict
```

4) Find key by value
```python
def find_key_by_value(input_dict: dict, value_of_interest):
    """This function finds the key of input_dict corresponding to the value_of_interest.
    Args:
        input_dict (dict): input dictionary
        value_of_interest (*): value of which we want to find the key
    Returns:
        key_of_interest (*): key corresponding to value_of_interest; if value_of_interest is not among the dict values, None is returned
    """
    # list out keys and values separately
    key_list = list(input_dict.keys())  # type: list
    val_list = list(input_dict.values())  # type: list

    unq, cnt = np.unique(val_list, return_counts=True)  # find unique values and corresponding counts
    idx_value_of_interest = np.where(unq == value_of_interest)  # find index of value identical to value_of_interest
    cnt_value_of_interest = cnt[idx_value_of_interest]  # extract the corresponding count

    if cnt_value_of_interest == 1:  # if the key value is unique
        idx_of_interest = val_list.index(value_of_interest)
        key_of_interest = key_list[idx_of_interest]
    elif cnt_value_of_interest.size == 0:  # if the key value is not among the dict values
        key_of_interest = None
    elif cnt_value_of_interest > 1:  # if there are multiple values identical to value_of_interest
        print("WARNING: there are multiple values identical to value_of_interest: the first one is returned")
        idx_of_interest = val_list.index(value_of_interest)
        key_of_interest = key_list[idx_of_interest]
    else:
        raise ValueError("cnt_value_of_interest cannot be negative")

    return key_of_interest
```

5) Find value by key
```python
value = d["key_of_interest"]
```

6) Find key with max value
```python
def key_with_max_val(d: dict):
    """This function takes as input a dict and returns the key with the max value by
    a) creating a list of the dict's keys and values;
    b) returning the key with the max value"""
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]
```
