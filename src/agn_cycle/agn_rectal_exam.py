"""An example module containing simplistic functions."""


from dataclasses import dataclass, field

import numpy as np
from photutils.aperture import RectangularAnnulus, aperture_photometry
from PIL import Image


@dataclass
class AGN:
    """hold AGN data"""

    file: str = ""
    centroid: list[int] = field(default_factory=list)
    bristol_scale: int = 1


def read_bmp(file_name):
    """Fetch AGN image for file."""
    img = Image.open(file_name)
    np_img = np.array(img)

    return np_img


def deeper_rectal_exam(np_image, centroid):
    """Calculate Rectangular Annulus Log from AGN image."""

    aperture_a = RectangularAnnulus(centroid, 25.0, 100.0, 100.0, 25.0)
    aperture_b = RectangularAnnulus(centroid, 50.0, 150.0, 150.0, 50.0)
    aperture_c = RectangularAnnulus(centroid, 100.0, 260.0, 260.0, 100.0)
    phot_table = aperture_photometry(np_image, [aperture_a, aperture_b, aperture_c])
    # print(phot_table)

    return phot_table
