import random

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from common import *


def change_brightness(img_1d, amount):
    pixels = np.asarray(img_1d, dtype=int)
    for i in range(len(pixels)):
        pixels[i] += amount

    return pixels


def main():
    img = imageToArray('samples/sample.png')
    deltaBrightness = 200
    newImg = change_brightness(np.reshape(img, (-1, 3)), deltaBrightness)
    newImg = np.reshape(newImg, img.shape)
    plt.imshow(newImg)
    plt.show()


if __name__ == '__main__':
    main()
