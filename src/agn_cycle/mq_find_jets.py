"""bar"""

import pandas as pd
from astropy.table import Table


def read_fits(input_file):
    """foo"""
    dataframe = Table.read(input_file, format="fits").to_pandas()
    _do_stuff(dataframe)


def read_csv(input_file):
    """foo"""
    _do_stuff(pd.read_csv(input_file))


def _do_stuff(dataframe):
    print(dataframe.columns)
    print(dataframe.groupby(["TYPE"])["TYPE"].count())
