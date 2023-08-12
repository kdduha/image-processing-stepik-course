import numpy as np
from skimage.io import imread, imsave

# функция Гаусса
def gauss(simga, x, y):
    return 1 / (2 * np.pi * sigma**2) * np.exp((-x**2 -y**2) / (2 * sigma**2))

# ядро
def kernel(sigma):
    k = round(3 * sigma) * 2 + 1
    kernel = np.zeros((k, k))
    center = k // 2
    
    for x in range(-center, center + 1):
        for y in range(-center, center + 1):
            kernel[x + center][y + center] = gauss(sigma, x, y)
    
    kernel /= np.sum(kernel)
    return kernel

img = imread('img.png')
sigma = 0.66
kernel = kernel(sigma)

center = kernel.shape[0] // 2

# готовим шаблон из нулевых значений меньшей размерности (изображение уменьшится после свертки)
out_img = np.zeros((img.shape[0] - 2*center, img.shape[1] - 2*center))

# идем от центра постепенно в разные стороны
for i in range(center, img.shape[0] - center):
    for j in range(center, img.shape[1] - center):
        start = (i - center, j - center)
        end = (i + center, j + center)
        # заполняем значение результатом свертки
        out_img[i - center, j - center] = np.sum(kernel * img[start[0]:end[0] + 1, start[1]:end[1] + 1])

imsave('out_img.png', np.clip(out_img, 0, 255).astype('uint8'))
