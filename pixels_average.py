import glob
import numpy as np

from scipy import misc

images = glob.glob('input/*.jpg')

np_images = []
for path in images:
    np_images.append(misc.imread(path))

hdr_image = np.zeros(np_images[0].shape, np_images[0].dtype)

for npi in np_images:
    hdr_image = np.add(hdr_image, npi)

hdr_image = hdr_image // len(np_images)

misc.imsave('output/output.jpg', hdr_image)
misc.imsave('output/test.jpg', np_images[0])