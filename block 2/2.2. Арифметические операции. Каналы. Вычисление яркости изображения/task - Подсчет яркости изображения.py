from skimage.io import imread, imsave
from skimage import img_as_float, img_as_ubyte

img = img_as_float(imread('img.png'))
r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
imsave('out_img.png', img_as_ubyte(0.2126*r + 0.7152*g + 0.0722*b))
