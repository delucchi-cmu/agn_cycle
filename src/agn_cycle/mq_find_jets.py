"""bar"""

import pandas as pd
from astropy.table import Table


def pull_jets(input_file):
    """foo"""
    dataframe = Table.read(input_file, format="fits").to_pandas()

    clean_up = ["NAME", "TYPE", "COMMENT", "R", "B", "CITE", "ZCITE", "XNAME", "RNAME", "LOBE1", "LOBE2"]
    for col_name in clean_up:
        dataframe[col_name] = [x.decode().strip() for x in dataframe[col_name].values]

    dataframe = dataframe[["2" in x or 'R' in x or 'X' in x for x in dataframe["TYPE"].values]]

    dataframe["LOBE1_SURVEY"] = [str(x)[: str(x).find("J")].strip() for x in dataframe["LOBE1"].values]
    dataframe["LOBE2_SURVEY"] = [str(x)[: str(x).find("J")].strip() for x in dataframe["LOBE2"].values]
    dataframe["XNAME_SURVEY"] = [str(x)[: str(x).find("J")].strip() for x in dataframe["XNAME"].values]
    dataframe["RNAME_SURVEY"] = [str(x)[: str(x).find("J")].strip() for x in dataframe["RNAME"].values]
    dataframe.to_csv("/home/delucchi/git/agn_cycle/data/milliquas/milliquas_lobes.csv.gz", compression="gzip")


def read_fits(input_file):
    """foo"""
    dataframe = Table.read(input_file, format="fits").to_pandas()
    _do_stuff(dataframe)


def read_csv(input_file):
    """foo"""
    _do_stuff(pd.read_csv(input_file, compression="gzip"))


def _do_stuff(dataframe):
    print(len(dataframe))
    # print(dataframe.groupby(["LOBE1_SURVEY"])["LOBE1_SURVEY"].count())
