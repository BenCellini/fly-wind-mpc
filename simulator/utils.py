import numpy as np
import copy

def wrapTo2Pi(rad):
    rad = copy.copy(rad)
    rad = rad % (2 * np.pi)
    return rad


def wrapToPi(rad):
    rad_wrap = copy.copy(rad)
    q = (rad_wrap < -np.pi) | (np.pi < rad_wrap)
    rad_wrap[q] = ((rad_wrap[q] + np.pi) % (2 * np.pi)) - np.pi
    return rad_wrap


def polar2cart(r, theta):
    # Transform polar to cartesian
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    return x, y


def cart2polar(x, y):
    # Transform cartesian to polar
    r = np.sqrt((x ** 2) + (y ** 2))
    theta = np.arctan2(y, x)

    return r, theta


def list_of_dicts_to_dict_of_lists(list_of_dicts, keynames=None, make_array=None):
    """ Takes a list containing dictionary with the same key names &
        converts it to a single dictionary where each key is a list.

        Inputs
            list_of_dicts:      input list
            keynames:           if None then use all the keys, otherwise set the key names here as a list of strings

        Outputs
            dict_of_lists:      output dictionary
    """

    # Get all the key names if not given as input
    if keynames is None:
        keynames = list_of_dicts[0].keys()  # use 1st dict to get key names

    # Create output dictionary
    dict_of_lists = {}
    for k in keynames:
        dict_of_lists[k] = []  # each key is a list

        # Get the values from the dictionaries & append to list in output dictionaries
        for n in list_of_dicts:
            dict_of_lists[k].append(n[k])

    if make_array is not None:
        for k in keynames:
            dict_of_lists[k] = np.hstack(dict_of_lists[k])

    return dict_of_lists
