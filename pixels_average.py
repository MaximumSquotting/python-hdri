import glob

from scipy import misc

images = glob.glob('input/*.jpg')
print(images)

np_images = []
for path in images:
    np_images.append(misc.imread(path))

np_images[0].shape(), np_images[0].dtype()