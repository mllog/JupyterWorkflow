import os
from urllib.request import urlretrieve
import pandas as pd

FREEMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'


def get_data(filename='Fremont.csv', url=FREEMONT_URL, force_dowload=False):
    """Download and cache the data

    Parameters
    ----------
    filename: string (optional)
        location to save the data
    url: string (optional)
        web location of the data
    force_dowload: bool (optional)
        if True, force redownload the data

    Returns
    -------
    data: pandas.DataFrame
        The data in pandas DataFrame
    """
    if force_dowload or os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv('Fremont.csv', index_col='Date', parse_dates=True)
    data.columns = ['West', 'East']
    data['Total'] = data['West'] + data['East']
    return data