import glob
import numpy as np

from scipy import misc

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

images = glob.glob('input/*.JPG')

color_images = []
for path in images:
    color_images.append(misc.imread(path))

gray_images = list(map(rgb2gray, color_images))

color_image = np.zeros(color_images[0].shape, color_images[0].dtype)
gray_image = np.zeros(gray_images[0].shape, gray_images[0].dtype)

for cri in color_images:
    color_image = np.add(color_image, cri)

for gri in gray_images:
    gray_image = np.add(gray_image, gri)

color_image = color_image // len(color_images)
gray_image = gray_image // len(gray_images)

misc.imsave('output/output_color.jpg', color_image)
misc.imsave('output/output_gray.jpg', gray_image)