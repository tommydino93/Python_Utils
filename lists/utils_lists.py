import os
import pickle
from collections import Counter
from typing import Iterator, Dict, List, Any


def save_pickle_list_to_disk(list_to_save: list, out_dir: str, out_filename: str) -> None:
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


def load_pickle_list_from_disk(path_to_list: str) -> List:
    """This function loads a list from disk
    Args:
        path_to_list (str): path to where the list is saved
    Returns:
        loaded_list (list): loaded list
    Raises:
        AssertionError: if list path does not exist
        AssertionError: if extension is not .pkl
    """
    assert os.path.exists(path_to_list), "Path {} does not exist".format(path_to_list)
    ext = os.path.splitext(path_to_list)[-1].lower()  # get the file extension
    assert ext == ".pkl", "Expected .pkl file, got {} instead".format(ext)
    open_file = open(path_to_list, "rb")
    loaded_list = pickle.load(open_file)  # load from disk
    open_file.close()
    return loaded_list


def find_common_elements(list1: list, list2: list) -> List:
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


def most_frequent(input_list: list) -> Any:
    """This function is given a list as input and it returns its most frequent element
    Args:
        input_list (list)
    Returns:
        most_frequent_item (*): most frequent item in the list; can be of Any type
    """
    occurence_count = Counter(input_list)
    most_frequent_item = occurence_count.most_common(1)[0][0]
    return most_frequent_item
