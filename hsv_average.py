import glob
import numpy as np
import matplotlib.colors as mc
from scipy import misc


def main():
    images = glob.glob('input/*.jpg')

    color_images = []
    for path in images:
        color_images.append(mc.rgb_to_hsv(misc.imread(path)/255))
    #print(color_images[0])

    color_image = np.zeros(color_images[0].shape, color_images[0].dtype)

    for cri in color_images:
        print(".")
        color_image = np.add(color_image, cri)

    color_image /= len(color_images)

    color_image = mc.hsv_to_rgb(color_image) * 255
    print(color_image)

    misc.imsave('output/output_color_hsv.png', color_image)

if __name__ == '__main__':
    main()
