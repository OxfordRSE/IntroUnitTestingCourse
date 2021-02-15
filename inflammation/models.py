"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.
"""

import numpy as np
import inflammation
import os
import inspect

def get_data_dir():
    """get default directory holding data files"""
    return os.path.dirname(inspect.getfile(inflammation)) + '/data'

def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load. If it is not an absolute path the
    file is assumed to be in the default data directory
    """
    if not os.path.isabs(filename):
        filename = get_data_dir() + '/' + filename

    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2d inflammation data array."""
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2d inflammation data array."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2d inflammation data array."""
    return np.min(data, axis=0)


# TODO(lesson-design) Add Patient class
# TODO(lesson-design) Implement data persistence
# TODO(lesson-design) Add Doctor class
