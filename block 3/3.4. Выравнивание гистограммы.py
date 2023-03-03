from skimage.io import imread, imsave
import numpy as np

img = imread('img.png')
values, bin_edges = np.histogram(img.ravel(), bins=range(257))

# считаем количество значений пикселей для каждого промежутка [0, x], где x - значения корзины
# cdf(x) = h(0) + h(1) + ... + h(x)
# сdf = [cdf(0), cdf(1) ... cdf(255)]
cdf = np.array([sum(values[i] for i in range(1, each_bin+1)) for each_bin in bin_edges[:-1]])

# берем минимум от среза без нулей
cdf_min = np.min(cdf[cdf > 0])

# для каждого пикселя применяем f(x)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i, j] = round((cdf[img[i, j]] - cdf_min)/(np.size(img) - 1)*255)
        
imsave('out_img.png', img)
