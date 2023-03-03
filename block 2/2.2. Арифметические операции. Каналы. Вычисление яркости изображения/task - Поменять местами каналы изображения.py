from skimage.io import imread, imsave
import numpy as np

img = imread('img.png')
r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
imsave('out_img.png', np.dstack((b, r, g)))
