"""An example module containing simplistic functions."""


import numpy as np
from photutils.aperture import aperture_photometry
from PIL import Image


def read_bmp(file_name):
    img= Image.open(file_name)
    np_img = np.array(img)
    
    print(np_img.shape)