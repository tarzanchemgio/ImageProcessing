import matplotlib.pyplot as plt
from common import *


def to_grayscale(img_1d):
    gray_img_1d = np.asarray(img_1d)
    for i in range(len(img_1d)):
        tmp = gray_img_1d[i] * [0.2126, 0.7152, 0.0722]
        gray_img_1d[i] = sum(tmp)

    return gray_img_1d


def main():
    img = imageToRGBArray('samples/sample.png')
    newImg = to_grayscale(np.reshape(img, (-1, 3)))
    newImg = np.reshape(newImg, img.shape)
    plt.imshow(newImg)
    plt.show()


if __name__ == '__main__':
    main()
