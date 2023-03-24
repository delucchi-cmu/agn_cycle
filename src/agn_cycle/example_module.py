"""An example module containing simplistic functions."""


import numpy as np
from photutils.aperture import RectangularAnnulus, aperture_photometry
from PIL import Image


def read_bmp(file_name, centroid):
    """perform RectAL analysis on AGN jet image."""
    img = Image.open(file_name)
    np_img = np.array(img)

    # print(np_img.shape)

    aperture_a = RectangularAnnulus(centroid, 25.0, 100.0, 100.0, 25.0)
    aperture_b = RectangularAnnulus(centroid, 50.0, 150.0, 150.0, 50.0)
    aperture_c = RectangularAnnulus(centroid, 100.0, 260.0, 260.0, 100.0)
    phot_table = aperture_photometry(np_img, [aperture_a, aperture_b, aperture_c])
    # print(phot_table)

    return phot_table
