"""bar"""

import pandas as pd
from astropy.table import Table


def pull_jets(input_file):
    """foo"""
    dataframe = Table.read(input_file, format="fits").to_pandas()

    clean_up = ["NAME", "TYPE", "COMMENT", "R", "B", "CITE", "ZCITE", "XNAME", "RNAME", "LOBE1", "LOBE2"]
    for col_name in clean_up:
        dataframe[col_name] = [x.decode().strip() for x in dataframe[col_name].values]

    dataframe = dataframe[["2" in x for x in dataframe["TYPE"].values]]
    dataframe.to_csv("/home/delucchi/git/agn_cycle/data/milliquas/milliquas_lobes.csv", compression="gzip")


def read_fits(input_file):
    dataframe = Table.read(input_file, format="fits").to_pandas()
    _do_stuff(dataframe)


def read_csv(input_file):
    """foo"""
    _do_stuff(pd.read_csv(input_file))


def _do_stuff(dataframe):
    print(dataframe.columns)
    print(dataframe.groupby(["TYPE"])["TYPE"].count())
    filtered = dataframe[["A" in x for x in dataframe["TYPE"].values]]
    print(filtered)
    print(filtered.groupby(["TYPE"])["TYPE"].count())
