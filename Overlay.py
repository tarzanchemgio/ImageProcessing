import matplotlib.pyplot as plt
from common import *


def overlay(back_img_1Darr, front_img_1Darr):
    output = np.copy(back_img_1Darr)
    for i in range(len(back_img_1Darr)):
        output[i] = back_img_1Darr[i] + front_img_1Darr[i]
    return output


def main():
    img = imageToGrayScaleArray('samples/cat.png')
    img2 = imageToGrayScaleArray('samples/background.png')
    newImg = overlay(img, img2)
    plt.imshow(np.reshape(newImg, img.shape))
    plt.show()


if __name__ == '__main__':
    main()
