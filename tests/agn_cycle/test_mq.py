"""Test this shit."""

import os

import numpy as np
import numpy.testing as npt

from agn_cycle import read_csv


def test_read_csv(test_mq_head_file):
    """"""
    read_csv(test_mq_head_file)
