import matplotlib.colors as mc
import matplotlib.image as mpimg
from math import *
import numpy as np
import glob

def norm_fun(hsv):
    w = hsv - 0.5
    return exp(-w**2/2)/sqrt(2*pi)

def triangle_fun(hsv):
    if hsv <= 0.5:
        return (0.999 * hsv) / 0.5 + 0.001
    else:
        return 1 - 0.999 * (hsv - 0.5) / 0.5

images = glob.glob('input/*.jpg')
color_images = []
for path in images:
    color_images.append(mc.rgb_to_hsv(mpimg.imread(path) / 255))
print("Image loading: done.")

vf = np.vectorize(triangle_fun)
color_image = np.zeros(color_images[0].shape)
weights = np.zeros(color_images[0].shape)
for cri in color_images:
    w = vf(cri)
    print("Image vectorize: done.")
    color_image = np.add(color_image, cri * w)
    weights = np.add(weights, w)
color_image /= weights
color_image = mc.hsv_to_rgb(color_image)
color_image *= 255
print("Image triangle: done.")

vf = np.vectorize(norm_fun)
norm_image = np.zeros(color_images[0].shape)
weights = np.zeros(color_images[0].shape)
for cri in color_images:
    w = vf(cri)
    print("Image vectorize: done.")
    norm_image = np.add(color_image, cri * w)
    weights = np.add(weights, w)
norm_image /= weights
norm_image = mc.hsv_to_rgb(norm_image)
norm_image *= 255
print("Image triangle: done.")

mpimg.imsave('output/output_color_hsv_triangle.jpg', color_image.astype('uint8'))
mpimg.imsave('output/output_color_hsv_norm.jpg', norm_image.astype('uint8'))