import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

original_image = mpimg.imread('tests/input.jpg')
mpimg.imsave('tests/output_load_save.jpg', original_image)
normalize_image = original_image / 255
normalize_image *= 255
normalize_image = normalize_image.astype('uint8')
print(original_image.dtype)
print(normalize_image.dtype)
mpimg.imsave('tests/output_normalize.jpg', normalize_image)
