import matplotlib.image as mpimg
import numpy as np
import glob

def triangle_fun(rgb):
    if rgb <= 128:
        return (0.999 * rgb) / 128 + 0.001
    else:
        return 1 - 0.999 * (rgb - 128) / 127

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

mpimg.imsave('output/output_color_hsv_triangle.jpg', color_image.astype('uint8'))