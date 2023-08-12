from skimage.io import imread, imsave
import numpy as np

img = imread('img.png')

img = imread('img.png')
# центр окна
center = 7 // 2
# шаблон для итогового изображения с меньшей размерностью
# т.к. фильтр будет являться одним из вариантов простой линейной свертки, где размерность будет уменьшаться
out_img = np.zeros((img.shape[0] - 2*center, img.shape[1] - 2*center))

# т.к. это вариант свертки, то алгоритм такой же как и в предыдущих заданиях на фильтрацию
for i in range(center, img.shape[0] - center):
    for j in range(center, img.shape[1] - center):
        start = (i - center, j - center)
        end = (i + center, j + center)
        # заполняем значения результатом свертки (вместа значений ядра берем медиану в нужном диапазоне)
        out_img[i - center, j - center] = np.median(img[start[0]:end[0] + 1, start[1]:end[1] + 1])
        
imsave('out_img.png', np.clip(out_img, 0, 255).astype('uint8'))
