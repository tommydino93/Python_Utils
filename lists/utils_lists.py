import os
import pickle
from collections import Counter
import glob
from typing import Iterator, Dict, List, Any


def save_list_to_disk_with_pickle(list_to_save: list, out_dir: str, out_filename: str) -> None:
    """This function saves a list to disk
    Args:
        list_to_save (list): list that we want to save
        out_dir (str): path to output folder; will be created if not present
        out_filename (str): output filename
    Returns:
        None
    """
    if not os.path.exists(out_dir):  # if output folder does not exist
        os.makedirs(out_dir)  # create it
    open_file = open(os.path.join(out_dir, out_filename), "wb")
    pickle.dump(list_to_save, open_file)  # save list with pickle
    open_file.close()


def load_list_from_disk_with_pickle(path_to_list: str) -> list:
    """This function loads a list from disk
    Args:
        path_to_list (str): path to where the list is saved
    Returns:
        loaded_list (list): loaded list
    Raises:
        AssertionError: if list path does not exist
    """
    assert os.path.exists(path_to_list), "Path {} does not exist".format(path_to_list)
    open_file = open(path_to_list, "rb")
    loaded_list = pickle.load(open_file)  # load from disk
    open_file.close()
    
    return loaded_list


def load_list_from_partial_name_with_glob(input_dir: str, partial_filename: str) -> list:
    """This function loads a list from disk by knowing only part of the filename
    Args:
        input_dir (str): directory where list was saved
        partial_filename (str): partial filename (use * as wildcare)
    Returns:
        list_of_interest (list): loaded list
    Example:
        # suppose the filename is y_true_fold_1, we can call:
        >>> y_true = load_list_with_glob(path_to_dir, 'y_true*')
    """
    file_path = glob.glob(os.path.join(input_dir, partial_filename))  # type: list
    assert len(file_path) == 1, "We expect only one filename to match"
    list_of_interest = load_list_from_disk_with_pickle(file_path[0])

    return list_of_interest


def find_common_elements(list1: list, list2: list) -> list:
    """This function takes as input two lists and returns a list with the common elements
    Args:
        list1 (list): first list
        list2 (list): second list
    Returns:
        intersection_as_list (list): list containing the common elements between the two input lists
    """
    list1_as_set = set(list1)  # type: set
    intersection = list1_as_set.intersection(list2)  # type: set
    intersection_as_list = list(intersection)  # type: list
    
    return intersection_as_list


def most_frequent_n_elements(input_list: list, n: int) -> Any:
    """This function is given a list as input and it returns its most frequent element
    Args:
        input_list (list)
    Returns:
        most_frequent_item (*): most frequent item in the list; can be of Any type
    """
    occurrence_count = Counter(input_list)  # type: Counter
    most_frequent_n_items = occurrence_count.most_common(n)
    
    return most_frequent_n_items


def flatten_list(list_of_lists: list) -> list:
    """This function flattens the input list
    Args:
        list_of_lists (list): input list of lists that we want to flatten
    Returns:
        flattened_list (list): flattened list
    """
    flattened_list = [item for sublist in list_of_lists for item in sublist]
    
    return flattened_list


def find_difference_list(list1: list, list2: list) -> list:
    """This function takes as input two lists and returns the difference list between them
    Args:
        list1 (list): first list
        list2 (list): second list
    Returns:
        difference_list (list): list containing the difference elements between the two input lists
    """
    difference_list = list(set(list1) - set(list2))
    
    return difference_list


def split_list_equal_sized_groups(lst: list, n: int, seed: int = 123) -> list:
    """This function splits a list in n approximately equal-sized subgroups
    Args:
        lst (list): input list that we want to split
        n (int): number of splits
        seed (int): random seed to use; defaults to 123
    Returns:
        out_list (list): list of lists, where each internal list is one split
    """
    random.Random(seed).shuffle(lst)  # shuffle list with fixed seed
    division = len(lst) / float(n)  # find number of items per split
    out_list = [lst[int(round(division * i)): int(round(division * (i + 1)))] for i in range(n)]  # list of lists
    return out_list


def find_indexes_where_lists_differ(list1: list, list2: list) -> list:
    """This function returns the indexes where the two input lists differ. THe input lists are expected to have same length
    Args:
        list1 (list): first input list
        list2 (list): second input list
    Returns:
        out_list (list): output list containing the indexes where the two input list differ
    Raises:
        AssertionError: if the two input lists do not have the same length
    """
    assert len(list1) == len(list2), "The two input lists must have same length"
    out_list = [idx for idx, (first, second) in enumerate(zip(list1, list2)) if first != second]
    return out_list


def extract_unique_elements(lst: list, ordered=True) -> list:
    """This function extracts the unique elements of the input list (i.e. it removes the duplicates)
    and returns them as an output list; if ordered=True (as by defualt), the returned list is ordered.
    Args:
        lst (list): input list from which we want to extract the unique elements
        ordered (bool): whether the output list of unique values is sorted or not; True by default
    Returns:
        out_list (list): list containing unique values
    """
    out_list = list(set(lst))  # type: list
    
    if ordered:  # if we want to sort the list of unique values
        out_list.sort()  # type: list
    
    return out_list

def find_idxs_of_element_in_list(lst: list, element: Any) -> list:
    """This function returns the indexes of the input list that have value == element
    Args:
        lst (list): input list where we search for indexes
        element (Any): element of which we want to find the indexes
    Returns:
        idxs (list): list of indexes corresponding to element
    """
    idxs = [i for i, x in enumerate(lst) if x == element]
    
    return idxs


def list_is_nested(input_list: list) -> bool:
    """This function checks whether the input_list is nested (i.e. it is a list of lists).
    Args:
        input_list (list): the input list
    Returns:
        is_nested (bool): True if list is nested, False if it isn’t
    """
    is_nested = any(isinstance(i, list) for i in input_list)
    
    return is_nested


def list_has_duplicates(input_list: list) -> bool:
    """This function checks whether the input_list contains duplicates or not.
    Args:
        input_list (list): the input list where we look for duplicates
    Returns:
        has_duplicates (bool): True if list has duplicates, False if it doesn’t
    """
    if list_is_nested(input_list):
        input_list = flatten_list(input_list)  # flatten list
    has_duplicates = len(input_list) != len(set(input_list))
    
    return has_duplicates


def first_argmax(input_list) -> int:
    """This function returns the index of the max value. If there are duplicate max values in input_list,
    the index of the first maximum value found will be returned.
    Args:
        input_list (list): list for which we want to find the argmax
    Returns:
        idx_max (int): index corresponding to the maximum value
    """
    idx_max = input_list.index(max(input_list))
    
    return idx_max


def shuffle_two_lists_with_same_order(x: list, y: list, chosen_seed: int = 123):
    """This function shuffles the two input lists with the same order
    Args:
        x (list): first input list
        y (list): second input list
        chosen_seed (int): seed to set for reproducibility
    Returns:
        shuffled_x (list): shuffled version of first list
        shuffled_y (list): shuffled version of second list
    Raises:
        AssertionError: if the two input lists do not have the same length
    """
    assert len(x) == len(y), "The two input lists must have the same length"
    random.seed(chosen_seed)  # set seed for reproducibility
    zipped_x_and_y = list(zip(x, y))  # zip x and y together so we don't lose the order when shuffling
    random.shuffle(zipped_x_and_y)  # shuffle
    shuffled_x, shuffled_y = zip(*zipped_x_and_y)  # unzip into x and y
    
    return shuffled_x, shuffled_y
    

def slice_by_index(lst, indexes):
    """Slice list by positional indexes.
    Args:
        lst: list to slice.
        indexes: iterable of 0-based indexes of the list positions to return.
    Returns:
        a new list containing elements of lst on positions specified by indexes.
    Examples:
        >>> slice_by_index([], [])
        []
        >>> slice_by_index([], [0, 1])
        []
        >>> slice_by_index(['a', 'b', 'c'], [])
        []
        >>> slice_by_index(['a', 'b', 'c'], [0, 2])
        ['a', 'c']
        >>> slice_by_index(['a', 'b', 'c'], [0, 1])
        ['a', 'b']
        >>> slice_by_index(['a', 'b', 'c'], [1])
        ['b']
    """
    if not lst or not indexes:
        return []
    slice_ = itemgetter(*indexes)(lst)
    if len(indexes) == 1:
        return [slice_]
    return list(slice_)


def keep_only_duplicates(input_list: list):
    """This function removes all unique values from input_list and keeps only the duplicates
    Args:
        input_list (list): list from which we want to remove unique values
    Returns:
        list_only_with_duplicates (list): output list that only contains the duplicates
    Example:
        >>> l = [1, 2, 2, 3, 3, 3, 4]
        >>> out_list = keep_only_duplicates(l)
        >>> out_list
        [2,3]
    """
    counts = Counter(input_list)
    list_only_with_duplicates = [id for id in counts if counts[id] > 1]
    
    return list_only_with_duplicates
    
