from skimage.io import imread, imsave
import numpy as np

img = imread('img.png')
k, h = round(img.size * 0.05), sorted(img.ravel())
min_pix, max_pix = h[k], h[-k-1]

img = (np.clip(img, min_pix, max_pix) - min_pix)*(255/(max_pix - min_pix))
imsave('out_img.png', img.astype('uint8'))
