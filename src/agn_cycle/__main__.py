"""Main method to enable command line execution"""

import os

from agn_cycle.agn_rectal_exam import process_directory
from agn_cycle.mq_find_jets import pull_jets, read_csv, read_fits


def run_rectal():
    """Run for directories"""

    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data"))

    nrao_33333_dir = os.path.join(data_dir, "nrao_33333")
    process_directory(nrao_33333_dir)


def run_mq():
    """Run"""
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data"))
    mq_file = os.path.join(data_dir, "milliquas", "milliquas.fits")
    pull_jets(mq_file)

    mq_file = os.path.join(data_dir, "milliquas", "milliquas_lobes.csv.gz")
    read_csv(mq_file)


if __name__ == "__main__":
    run_mq()
