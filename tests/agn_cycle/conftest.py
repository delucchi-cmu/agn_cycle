import os

import pytest

TEST_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data"))

# pylint: disable=missing-function-docstring, redefined-outer-name


@pytest.fixture
def test_data_dir():
    return DATA_DIR


@pytest.fixture
def test_nrao_33333_data_dir(test_data_dir):
    return os.path.join(test_data_dir, "nrao_33333", "bmp")


@pytest.fixture
def test_mq_head_file(test_data_dir):
    return os.path.join(test_data_dir, "milliquas", "milliquas_head.csv")
