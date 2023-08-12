from skimage.io import imread, imsave
from skimage import img_as_float, img_as_ubyte

img = img_as_float(imread('img.png'))
r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
# считаем яркость по формуле поэлементно (каждый канал - 2-мерный numpy массив, так что так можно)
imsave('out_img.png', img_as_ubyte(0.2126*r + 0.7152*g + 0.0722*b))
