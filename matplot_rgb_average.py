import matplotlib.image as mpimg
import numpy as np
import glob

images = glob.glob('input/*.jpg')
color_images = []
for path in images:
    color_images.append(mpimg.imread(path))

color_image = np.zeros(color_images[0].shape)
for cri in color_images:
    color_image = np.add(color_image, cri)

color_image /= len(color_images)
print(color_image)
mpimg.imsave('output/output_color_rgb.jpg', color_image.astype('uint8'))