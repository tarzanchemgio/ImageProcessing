from PIL import Image
import numpy as np


def imageToRGBArray(path):
    """

    :return: np array with shape (numberOfPixel, 3)
    """
    img = Image.open(path).convert('RGB')
    return np.array(img)


def imageToGrayScaleArray(path):
    img = Image.open(path).convert('LA').convert('RGB')
    return np.array(img)


def clamp_pixel(pix, left, right):
    for i in range(len(pix)):
        pix[i] = max(min(pix[i], right), left)
    return pix
