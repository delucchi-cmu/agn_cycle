"""Test this shit."""

import os

import numpy as np
import numpy.testing as npt

from agn_cycle import deeper_rectal_exam, read_bmp, regression


def test_read_bmp(test_nrao_33333_data_dir):
    """Verify the output of the read_bmp function."""

    result = read_bmp(os.path.join(test_nrao_33333_data_dir, "001.bmp"))
    assert result.shape == (489, 511)


def test_exam(test_nrao_33333_data_dir):
    """thing"""
    image = read_bmp(os.path.join(test_nrao_33333_data_dir, "001.bmp"))
    result = deeper_rectal_exam(image, [155, 195])
    npt.assert_approx_equal(result, -0.575, significant=3)


def test_regression():
    """ "more thing"""
    responses = np.array(
        [
            -0.5751548022080019,
            -1.1810301943716697,
            -0.4050233353693391,
            -0.03479685468053902,
            -0.7062942111012559,
            -0.6953677936197235,
            -0.24341856329826567,
            -0.14298910464187733,
            -0.4583989375001329,
            -0.2879962985934552,
            -0.3313780228263056,
            0.3010632552979254,
            0.008097738715229674,
            0.5120122217121389,
            -0.40417725086932205,
            0.956442825864301,
            -0.18548069807959613,
            -0.3165754336667814,
            -0.37660396144232905,
            -0.806524679033245,
            -0.25956567579236867,
            -1.323637465203398,
            -0.7318619893932852,
        ]
    )
    bristol_values = np.array([3, 3, 6, 1, 4, 6, 1, 1, 6, 4, 4, 7, 6, 7, 4, 7, 6, 4, 7, 1, 1, 4, 4])

    regression(responses, bristol_values)
