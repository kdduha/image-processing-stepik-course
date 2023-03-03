from skimage.io import imread, imsave
from skimage import img_as_float

imsave('out_img.png', abs(img_as_float(imread('img.png')) - 1))
