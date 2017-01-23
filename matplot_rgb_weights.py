import matplotlib.image as mpimg
import numpy as np
from math import *
import glob

def triangle_fun(rgb):
    if rgb <= 128:
        return (0.999 * rgb) / 128 + 0.001
    else:
        return 1 - 0.999 * (rgb - 128) / 127

def norm_fun(rgb):
    w = rgb - 128
    w /= 255
    return exp(-w**2/2)/sqrt(2*pi)

def rgb2gray(rgb):
    matrix = np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
    return np.dstack((matrix, matrix, matrix))

images = glob.glob('input/*.jpg')
color_images = []
for path in images:
    color_images.append(mpimg.imread(path))
print("Image loading: done.")

vf = np.vectorize(triangle_fun)
color_image = np.zeros(color_images[0].shape)
weights = np.zeros(color_images[0].shape)
for cri in color_images:
    w = vf(rgb2gray(cri))
    print("Image vectorize: done.")
    color_image = np.add(color_image, cri * w)
    weights = np.add(weights, w)
color_image /= weights
print("Image triangle: done.")

vf = np.vectorize(norm_fun)
norm_image = np.zeros(color_images[0].shape)
weights = np.zeros(color_images[0].shape)
for cri in color_images:
    w = vf(rgb2gray(cri))
    print("Image vectorize: done.")
    norm_image = np.add(color_image, cri * w)
    weights = np.add(weights, w)
norm_image /= weights
print("Image norm: done.")

mpimg.imsave('output/output_color_rgb_triangle.jpg', color_image.astype('uint8'))
mpimg.imsave('output/output_color_rgb_norm.jpg', norm_image.astype('uint8'))