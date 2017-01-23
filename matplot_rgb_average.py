import matplotlib.image as mpimg
import numpy as np
import glob

def rgb2gray(rgb):
    matrix = np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
    return np.dstack((matrix, matrix, matrix))

images = glob.glob('input/*.jpg')
color_images = []
for path in images:
    color_images.append(mpimg.imread(path))

gray_images = list(map(rgb2gray, color_images))
gray_image = np.zeros(gray_images[0].shape, gray_images[0].dtype)

color_image = np.zeros(color_images[0].shape)
for cri in color_images:
    color_image = np.add(color_image, cri)

for gri in gray_images:
    gray_image = np.add(gray_image, gri)

color_image /= len(color_images)
gray_image /= len(gray_images)

mpimg.imsave('output/output_color_rgb.jpg', color_image.astype('uint8'))
mpimg.imsave('output/output_gray_rgb.jpg', gray_image.astype('uint8'))