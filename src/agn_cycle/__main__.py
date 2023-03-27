"""Main method to enable command line execution"""

import os

from agn_cycle.agn_rectal_exam import process_directory


def run():
    """Run for directories"""

    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data"))

    nrao_33333_dir = os.path.join(data_dir, "nrao_33333")
    process_directory(nrao_33333_dir)


if __name__ == "__main__":
    run()
