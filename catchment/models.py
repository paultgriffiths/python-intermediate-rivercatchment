"""Module containing models representing catchment data.

The Model layer is responsible for the 'business logic' part of the software.

Catchment data is held in a Pandas dataframe (2D array) where each column contains
data for a single measurement site, and each row represents a single measurement
time across all sites.
"""

import pandas as pd

def read_variable_from_csv(filename):
    """Reads a named variable from a CSV file, and returns a
    pandas dataframe containing that variable. The CSV file must contain
    a column of dates, a column of site ID's, and (one or more) columns
    of data - only one of which will be read.

    :param filename: Filename of CSV to load
    :return: 2D array of given variable. Index will be dates,
             Columns will be the individual sites
    """
    dataset = pd.read_csv(filename, usecols=['Date', 'Site', 'Rainfall (mm)'])

    dataset = dataset.rename({'Date':'OldDate'}, axis='columns')

    dataset = dataset.drop('OldDate', axis='columns')

    newdataset = pd.DataFrame(index=dataset['Date'].unique())

    for site in dataset['Site'].unique():
        newdataset[site] = dataset[dataset['Site'] == site].set_index('Date')['Rainfall (mm)']

    newdataset = newdataset.sort_index()

    return newdataset

def daily_total(data):
    """Calculate the daily total of a Pandas DataFrame.


    :param data: a Pandas dataframe
    :raises Nothing - FIXME!
    :returns a Pandas dataframe

    Index must be np.datetime64 compatible format.
    """
    return data.groupby(data.index.date).sum()

def daily_mean(data):
    """Calculate the daily mean of a 2D Pandas DataFrame
    Uses the inbuilt Pandas groupby function to generate a mean value over
    the column of interest

    :param data: a Pandas dataframe
    :raises Nothing - FIXME!
    :returns a Pandas dataframe

    Index must be np.datetime64 compatible format.
    """
    return data.groupby(data.index.date).mean()


def daily_max(data):
    """Calculate the daily max of of a 2D Pandas DataFrame
    Uses the inbuilt Pandas groupby function to generate a mean value over
    the column of interest

    :param data: a Pandas dataframe
    :raises Nothing - FIXME!
    :returns a Pandas dataframe
    Index must be np.datetime64 compatible format.
    """

    return data.groupby(data.index.date).max()


def daily_min(data):
    """Calculate the daily min ofof a 2D Pandas DataFrame
    Uses the inbuilt Pandas groupby function to generate a mean value over
    the column of interest

    :param data: a Pandas dataframe
    :raises Nothing - FIXME!
    :returns a Pandas dataframe
    """
    return data.groupby(data.index.date).min()
