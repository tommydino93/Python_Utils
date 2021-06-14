import pickle
from typing import Iterator, Dict, List


def save_list_to_disk(list_to_save: list, out_dir: str, out_filename: str) -> None:
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


def load_list_from_disk(path_to_list: str) -> List:
    """This function loads a list from disk
    Args:
        path_to_list (str): path to where the list is saved
    Returns:
        loaded_list (list): loaded list
    """
    open_file = open(path_to_list, "rb")
    loaded_list = pickle.load(open_file)  # load from disk
    open_file.close()
    return loaded_list
  
  
