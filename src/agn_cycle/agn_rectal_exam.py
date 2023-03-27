"""An example module containing simplistic functions."""


import os
from dataclasses import dataclass, field

import numpy as np
import pandas as pd
from photutils.aperture import RectangularAnnulus, aperture_photometry
from PIL import Image
from sklearn.linear_model import LinearRegression


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
    qtable = aperture_photometry(np_image, [aperture_a, aperture_b, aperture_c])
    dataframe = qtable.to_pandas()
    # print(dataframe)
    # print(dataframe["aperture_sum_0"][0])

    return np.log(dataframe["aperture_sum_0"][0] / dataframe["aperture_sum_2"][0])


def regression(rectal_values, bristol_test):
    """Perform a basic linear regression on the test values."""
    bristol_test = bristol_test.reshape((-1, 1))
    model = LinearRegression().fit(bristol_test, rectal_values)

    r_sq = model.score(bristol_test, rectal_values)
    print(f"coefficient of determination: {r_sq}")

def process_directory(base_dir):
    """Assumes directory has the following format:
    <base_dir>/
      - files.csv
      - bmp/
         <file_name>
    """

    files_csv = pd.read_csv(os.path.join(base_dir, "files.csv"))

    responses = []
    for _, row in files_csv.iterrows():
        file_name = os.path.join(base_dir, "bmp", row["file_name"])
        image = read_bmp(file_name)
        responses.append(deeper_rectal_exam(image, [row["x_center"], row["y_center"]]))

    # print(responses)

    regression(responses, files_csv["bristol"].to_numpy())