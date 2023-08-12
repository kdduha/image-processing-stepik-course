from skimage.io import imread, imsave
import numpy as np

img = imread('img.png')
# сохраняем по отдельности каналы как слайсы третьего измерения 3-ех мерной матрицы
r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
# все заносим в матрицу с новым порядком (будет опять 3-ех мерный массив)
imsave('out_img.png', np.dstack((b, r, g)))
