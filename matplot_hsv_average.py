import matplotlib.colors as mc
import matplotlib.image as mpimg
import numpy as np
import glob

images = glob.glob('input/*.jpg')
color_images = []
for path in images:
    color_images.append(mc.rgb_to_hsv(mpimg.imread(path)/255))

color_image = np.zeros(color_images[0].shape)
for cri in color_images:
    color_image = np.add(color_image, cri)

color_image /= len(color_images)
color_image = mc.hsv_to_rgb(color_image)
print(color_image)
color_image *= 255
print(color_image)

mpimg.imsave('output/output_color_hsv.jpg', color_image.astype('uint8'))