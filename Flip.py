import matplotlib.pyplot as plt
from common import *


def flip_image(rgb_img, option):
    flipped = np.asarray(rgb_img)
    if option == 'h':  # horizontal
        for j in range(len(rgb_img[0])):
            for i in range(int(len(rgb_img) / 2)):
                tmp = np.copy(flipped[i][j])
                flipped[i][j] = flipped[len(rgb_img) - i - 1][j]
                flipped[len(rgb_img) - i - 1][j] = tmp
    elif option == 'v':  # vertical
        for i in range(len(rgb_img)):
            # noinspection PyTypeChecker
            for j in range(int(len(rgb_img[i]) / 2)):
                tmp = np.copy(flipped[i][j])
                flipped[i][j] = flipped[i][len(rgb_img[j]) - j - 1]
                flipped[i][len(rgb_img[j]) - j - 1] = tmp
    else:
        raise ValueError

    return flipped


def main():
    img = imageToRGBArray('samples/sample.png')
    # 'h' for horizontal and 'v' for vertical
    newImg = flip_image(img, 'v')
    plt.imshow(newImg)
    plt.show()


if __name__ == '__main__':
    main()
