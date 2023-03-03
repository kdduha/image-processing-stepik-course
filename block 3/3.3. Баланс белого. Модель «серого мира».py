from skimage.io import imread, imsave
from skimage import img_as_float
import numpy as np

img = img_as_float(imread('img.png'))
r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]

r_avg, g_avg, b_avg = np.mean(r), np.mean(g), np.mean(b)    # среднее значение
avg = (r_avg + g_avg + b_avg)/3
r, g, b = r*avg/r_avg, g*avg/g_avg, b*avg/b_avg             # вычисление 2 и 3 пункта сразу

imsave('out_img.png', np.clip(np.dstack((r, g, b)), 0., 1.))
