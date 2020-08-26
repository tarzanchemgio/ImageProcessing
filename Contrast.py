import matplotlib.pyplot as plt
from common import *


def adjust_contrast(img_1d, amount):
    factor = (259 * (amount + 255)) / (255 * (259 - amount))
    pixels = np.asarray(img_1d, dtype=float)
    for i in range(len(pixels)):
        pixels[i] = factor*(pixels[i] - 128) + 128

    return np.asarray(pixels, dtype=int)


def main():
    img = imageToArray('samples/sample.png')
    contrastAmount = 128
    newImg = adjust_contrast(np.reshape(img, (-1, 3)), contrastAmount)
    newImg = np.reshape(newImg, img.shape)
    plt.imshow(newImg)
    plt.show()


if __name__ == '__main__':
    main()
