from skimage.io import imread, imsave
import numpy as np

# объединяю методы из предыдущих двух задач
img = imread('img.png').astype('float')
k, h = round(img.size * 0.05), sorted(img.ravel())
min_pix, max_pix = h[k], h[-k-1]

# иду по формуле + инструкции задачи
img = (img - min_pix) * (255 / (max_pix - min_pix))
imsave('out_img.png', np.clip(img, min_pix, max_pix).astype('uint8'))
