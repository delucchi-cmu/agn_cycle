"""Test this shit."""

import os

import pandas as pd

from agn_cycle import AGN, read_bmp


def test_read_bmp(test_nrao_33333_data_dir):
    """Verify the output of the read_bmp function."""

    result = read_bmp(os.path.join(test_nrao_33333_data_dir, "001.bmp"))
    assert result.shape == (489, 511)
