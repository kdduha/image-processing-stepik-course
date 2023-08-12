import numpy as np
from skimage.io import imread, imsave

img = imread('img.png')

# создаем заранее готовое ядро шаблон
kernel = np.array([[-1, -2, -1], [-2, 22, -2], [-1, -2, -1]]) / 10
center = kernel.shape[0] // 2

# свертка делается по алгоритму из прошлого задания с гауссовской фильтрацией
out_img = np.zeros((img.shape[0] - 2*center, img.shape[1] - 2*center))

for i in range(center, img.shape[0] - center):
    for j in range(center, img.shape[1] - center):
        start = (i - center, j - center)
        end = (i + center, j + center)
        out_img[i - center, j - center] = np.sum(kernel * img[start[0]:end[0] + 1, start[1]:end[1] + 1])

imsave('out_img.png', np.clip(out_img, 0, 255).astype('uint8'))
